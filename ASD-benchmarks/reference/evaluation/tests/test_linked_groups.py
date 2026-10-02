"""Audit frozen linked groups and recorded OOF scopes without fitting or source parsing.

Run directly to produce receipts, or use unittest discovery. This verifies the
exposed evaluation contracts; it does not create a fresh confirmation cohort.
"""
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime
import argparse
import csv
import gzip
import hashlib
import json
import re
import unittest

BENCHMARK = Path(__file__).resolve().parents[2]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class Audit:
    def __init__(self, benchmark):
        self.benchmark = Path(benchmark)
        self.assets = {}
        self.checks = []

    def record_asset(self, path):
        self.assets[path.relative_to(self.benchmark).as_posix()] = digest(path)

    def read_json(self, relative):
        path = self.benchmark / relative
        self.record_asset(path)
        return json.loads(path.read_text())

    def table(self, case, family, name='inputs'):
        path = self.benchmark / 'tasks' / f'P100-{case:03d}.{family}.v1' / 'data' / f'{name}.csv.gz'
        self.record_asset(path)
        with gzip.open(path, 'rt', newline='') as stream:
            rows = list(csv.DictReader(stream))
        require(len(rows) == len({r['sample_id'] for r in rows}), 'Duplicate table identity')
        return rows

    def check(self, name, function):
        try:
            detail = function()
            result = {'name': name, 'status': 'pass', **detail}
        except Exception as error:
            result = {'name': name, 'status': 'fail', 'error': str(error)}
        self.checks.append(result)

    def split(self, case):
        return self.read_json(f'evaluation/preparation/metadata/{case}_split.json')

    def screw(self):
        split = self.split(53)
        groups = split['groups']
        operations = split['operations']
        require(len(groups) == 250 and len(operations) == 12500, 'Unexpected native split inventory')
        require(len({op['run_id'] for op in operations}) == 12500, 'Duplicate native operation identity')
        by_group = defaultdict(list)
        by_class = defaultdict(list)
        for group, metadata in groups.items():
            by_class[metadata['class']].append(group)
        for op in operations:
            require(op['workpiece_id'] in groups, 'Operation without workpiece split')
            by_group[op['workpiece_id']].append(op)
        for group, ops in by_group.items():
            expected = {(str(i), location) for i in range(25) for location in ('left', 'right')}
            require(len(ops) == 50, 'Incomplete linked workpiece operation inventory')
            require({(r['workpiece_usage'], r['workpiece_location']) for r in ops} == expected,
                    'Workpiece does not preserve all locations/reuse cycles')
        for condition, members in by_class.items():
            ranked = sorted(members, key=lambda g: hashlib.sha256(
                f"{split['salt']}|{condition}|{g}".encode()).hexdigest())
            count = len(members) // 5
            for rank, group in enumerate(ranked):
                info = groups[group]
                expected_partition = 'sealed_test' if rank < count else 'development'
                require(info['partition'] == expected_partition, 'Stratified hash allocation changed')
                require(info['hash_rank_in_class'] == rank, 'Hash rank changed')
                require(info['fold'] == (None if rank < count else (rank - count) % 5), 'Development workpiece fold changed')
        original = self.table(53, 'original'); development = self.table(53, 'round2')
        lookup = {r['run_id']: r['workpiece_id'] for r in operations}
        for rows, role in [(original, 'sealed_test'), (development, 'development')]:
            for row in rows:
                require(lookup[row['sample_id']] == row['group'], 'Operation split from its linked workpiece')
                require(groups[row['group']]['partition'] == role, 'Workpiece crosses historical partitions')
        require(not ({r['group'] for r in original} & {r['group'] for r in development}), 'Workpiece overlap')
        return {'workpieces': 250, 'native_operations': 12500, 'confirmation_workpieces': 50,
                'development_workpieces': 200, 'conditions': len(by_class),
                'scope': 'Complete frozen operation inventory, hash allocation and eligible task rows.'}

    def settling(self):
        split = self.split(67)
        development = set(split['development_configs']); confirmation = set(split['final_test_configs'])
        require(len(development) == 6 and len(confirmation) == 3 and not development & confirmation, 'Configuration split overlap')
        for group, value in split['hashes'].items():
            require(hashlib.sha256(f"{split['salt']}|P100-067|{group}".encode()).hexdigest() == value, 'Configuration hash changed')
        for family in ('1', '2', '3'):
            members = [g for g in split['hashes'] if g.startswith(family + '.')]
            selected = min(members, key=lambda g: split['hashes'][g])
            require(selected in confirmation and len(set(members) & confirmation) == 1, 'Family allocation mismatch')
        for version, expected in [('original', confirmation), ('round2', development)]:
            rows = self.table(67, version)
            require({r['group'] for r in rows} == expected, 'Missing or misplaced complete configuration')
            require(all(r['sample_id'].split('/')[0] == r['group'] for r in rows), 'Particle/window split from configuration')
        return {'development_configurations': 6, 'confirmation_configurations': 3,
                'scope': 'All particle identities inherit their full configuration allocation.'}

    def cho(self):
        split = self.split(71); entries = split['entries']
        require(len(entries) == 12 and len({e['experiment'] for e in entries}) == 12, 'Duplicate experiment')
        lookup = {e['experiment']: e for e in entries}
        for entry in entries:
            require(set(entry['reactors']) == {'R01', 'R02'}, 'Experiment pair separated')
            expected_hash = hashlib.sha256(f"{split['salt']}|P100-071|{entry['mode']}|{entry['experiment']}".encode()).hexdigest()
            require(expected_hash == entry['hash'], 'Experiment hash changed')
        for mode, count in [('batch', 2), ('fed-batch', 1)]:
            ranked = sorted([e for e in entries if e['mode'] == mode], key=lambda e: e['hash'])
            for rank, entry in enumerate(ranked, 1):
                require(entry['rank_within_mode'] == rank, 'Experiment hash rank changed')
                require(entry['split'] == ('locked_confirmation' if rank <= count else 'development'), 'Paired allocation changed')
        for version, role in [('original', 'locked_confirmation'), ('round2', 'development')]:
            rows = self.table(71, version); reactors = defaultdict(set)
            for row in rows:
                tokens = row['sample_id'].split('_')
                require(row['group'] == tokens[0], 'Observation split from experiment')
                require(lookup[row['group']]['split'] == role, 'Experiment crosses historical partition')
                reactors[row['group']].add(tokens[1])
            require(all(v == {'R01', 'R02'} for v in reactors.values()), 'One reactor absent from eligible paired experiment')
        return {'paired_experiments': 12, 'reactors': 24, 'confirmation_pairs': 3,
                'scope': 'Frozen paired manifest and eligible observations; no repeated XLSX parsing.'}

    def ble(self):
        split = self.split(92); date_roles = defaultdict(set)
        for group, record in split['groups'].items():
            date_roles[record['date']].add(record['role'])
        require(all(len(v) == 1 for v in date_roles.values()), 'Furniture states on one date split across partitions')
        by_role = defaultdict(list)
        for date, roles in date_roles.items():
            by_role[next(iter(roles))].append(datetime.strptime(date, '%d%m%Y'))
        require(max(by_role['calibration']) < min(by_role['development']), 'Calibration follows development')
        require(max(by_role['development']) < min(by_role['confirmation']), 'Development follows confirmation')
        confirmation_dates = set(split['confirmation_dates'])
        require(confirmation_dates == {d for d, roles in date_roles.items() if roles == {'confirmation'}}, 'Confirmation dates mismatch')
        require(len(confirmation_dates) == 3, 'Expected three final date groups')
        for version, expected_role in [('original', 'confirmation'), ('round2', 'development')]:
            rows = self.table(92, version)
            for row in rows:
                source_group = row['sample_id'].split('/')[0]
                metadata = split['groups'][source_group]
                require(metadata['role'] == expected_role, 'BLE observation crosses date partition')
                require(row['group'] == metadata['date'], 'BLE date grouping inconsistent')
        return {'historical_confirmation_dates': sorted(confirmation_dates, key=lambda d: datetime.strptime(d, '%d%m%Y')),
                'furniture_variants_share_date_role': True,
                'scope': 'Chronological calibration/development/confirmation dates; future users must treat outcomes as exposed.'}

    def router(self):
        native = self.read_json('evaluation/preparation/metadata/source_assets.json')['37']
        native_runs = {Path(a['path']).name for a in native if a['path'].endswith('.csv')}
        original = self.table(37, 'original'); development = self.table(37, 'round2')
        held = {r['group'] for r in original}; dev = {r['group'] for r in development}
        require(len(native_runs) == 15 and len(held) == 5 and len(dev) == 10, 'Router run count mismatch')
        require(held.isdisjoint(dev) and held | dev == native_runs, 'Router source run split inconsistent')
        require(all('iteration3.csv' in g for g in held), 'Confirmation is not whole repetition 3')
        require(all(re.search(r'iteration[12]\.csv$', g) for g in dev), 'Development contains repetition 3')
        for rows in (original, development):
            require(all(r['sample_id'].rsplit(':', 1)[0] == r['group'] for r in rows), 'Router row split from its run')
        return {'native_runs': 15, 'development_runs': 10, 'confirmation_runs': 5,
                'scope': 'Complete source filenames and eligible task rows; no rowwise repartitioning.'}

    def oof(self, task):
        case = task['case_number']; rows = self.table(case, 'round2')
        indexed = {r['sample_id']: r for r in rows}; by_group = defaultdict(set)
        for row in rows:
            by_group[row['group']].add(row['fold'])
        require(all(len(v) == 1 for v in by_group.values()), 'One evaluation group appears in multiple OOF folds')
        scope = self.read_json(f"{task['package']}/reference_training_scope.json")
        counts = Counter(); missing = []
        for model, record in scope['models'].items():
            seen = []; model_groups = defaultdict(set)
            for fold, state in record['folds'].items():
                ids = state['validation_ids']; seen.extend(ids)
                require(all(i in indexed for i in ids), 'OOF metadata references an absent observation')
                require(all(indexed[i]['fold'] == str(fold) for i in ids), 'Table and model fold labels disagree')
                groups = {indexed[i]['group'] for i in ids}
                require(groups == set(state['validation_groups']), 'Recorded validation groups disagree with observations')
                for group in groups:
                    model_groups[group].add(fold)
                train = state['training_groups']
                if train is None:
                    missing.append({'model': model, 'fold': fold, 'status': state['scope_status']})
                else:
                    require(not set(train) & groups, 'Training and validation evaluation groups overlap')
                    counts['folds_with_recorded_training_scope'] += 1
                    if case == 92:
                        require(max(datetime.strptime(g, '%d%m%Y') for g in train) < min(datetime.strptime(g, '%d%m%Y') for g in groups), 'BLE forward fold uses future training date')
                    if case == 83:
                        train_blocks = [int(g.rsplit(':block', 1)[1]) for g in train]
                        val_blocks = [int(g.rsplit(':block', 1)[1]) for g in groups]
                        require(max(train_blocks) < min(val_blocks), 'Hive forward block uses future training block')
                    if case == 82:
                        require(all(g.endswith('|development') for g in train), 'Soil frozen training scope unexpected')
                        require(all(g.endswith('|' + str(fold)) for g in groups), 'Soil evaluation windows inconsistent')
                counts['fold_records'] += 1
            require(len(seen) == len(set(seen)) and set(seen) == set(indexed), 'OOF validation identities missing or repeated')
            require(all(len(v) == 1 for v in model_groups.values()), 'Model splits linked evaluation group across folds')
            counts['models'] += 1
        detail = {'task_id': task['task_id'], 'rows': len(rows), 'evaluation_groups': len(by_group), **dict(counts),
                  'missing_historical_training_scope_records': len(missing),
                  'missing_historical_training_scope_details': missing,
                  'scope': 'Frozen exposed OOF identities, fold assignments and recorded training scope.'}
        if case in (82, 83, 92):
            detail['temporal_contract'] = {82: 'Same sites may occur in declared development calibration and forward windows. Evaluation site-window groups are disjoint. Absolute source dates are covered by native reconstruction, not reparsed here.', 83: 'Same sensor streams may recur in strictly later blocks; training block indices must precede validation.', 92: 'Earlier complete dates train later dates; calibrated positions may recur.'}[case]
        return detail

    def run(self):
        for name, method in [('53_complete_workpieces', self.screw), ('67_whole_configurations', self.settling),
                             ('71_whole_experiment_pairs', self.cho), ('92_historical_date_chronology', self.ble),
                             ('37_complete_router_iterations', self.router)]:
            self.check(name, method)
        registry = self.read_json('registry.json')
        tasks = [t for t in registry['tasks'] if t['family'] == 'round2' and not t.get('documentation_correction')]
        require(len(tasks) == 15, 'Expected fifteen round2 contracts')
        for task in tasks:
            self.check(task['task_id'] + '_oof_linkage', lambda task=task: self.oof(task))
        for t in registry['tasks']:
            if not t.get('documentation_correction'): continue
            def alias(t=t):
                original=t['documentation_correction']['supersedes']; prior=next(z for z in registry['tasks'] if z['task_id']==original)
                for name in ['data/inputs.csv.gz','data/observations.csv.gz','reference_training_scope.json','rules.json']:
                    require(digest(self.benchmark/t['package']/name)==digest(self.benchmark/prior['package']/name), 'Corrected contract changed '+name)
                return {'task_id':t['task_id'],'same_scientific_contract_as':original,'scope':'Documentation correction preserves cohort, models and recorded fold scopes; no additional experiment.'}
            self.check(t['task_id']+'_same_scientific_scope',alias)
        return {'schema': 'principia.linked-group-audit/v1',
                'status': 'pass' if all(c['status'] == 'pass' for c in self.checks) else 'fail',
                'checks': self.checks, 'assets_sha256': self.assets,
                'scope': 'Frozen group allocations, exposed task identities and recorded OOF scopes. No model fitting, no new native scientific parsing, no fresh confirmation.',
                'limitations': ['Some historical alternative models did not record training-group lists; their validation linkage can be checked, but missing training membership is not reconstructed or claimed independently verified.', 'Site/sensor reuse in declared forward-calibration tasks is allowed. Raw prefix safety and native-value parity have separate receipts.', 'Every historical outcome is exposed to future benchmark users.']}


class LinkedGroupTests(unittest.TestCase):
    def test_frozen_linked_groups_and_oof_scopes(self):
        result = Audit(BENCHMARK).run()
        failures = [c for c in result['checks'] if c['status'] != 'pass']
        self.assertEqual([], failures)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--benchmark', type=Path, default=BENCHMARK)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    result = Audit(args.benchmark).run()
    report = args.report or args.benchmark / 'reports/LINKED_GROUPS.json'
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(json.dumps(result, indent=2) + '\n')
    missing = sum(c.get('missing_historical_training_scope_records', 0) for c in result['checks'])
    lines = ['# Linked-group and chronological audit', '', result['scope'], '',
             '| Check | Status | Scope |', '|---|---|---|']
    for check in result['checks']:
        lines.append(f"| {check['name']} | {check['status']} | {check.get('scope', check.get('error', ''))} |")
    lines += ['', f"{len(result['checks'])} checks completed. The fifteen round2 task versions retain one fold per evaluation group and consistent frozen OOF identities.", '',
              f"{missing} older model/fold records have no source-recorded training-group list. Their validation identities and linkage pass; this audit does not manufacture or independently verify absent training membership. The current cycle-001 scopes include recorded training groups.", '',
              'For soil respiration, the same site can appear in declared development calibration and subsequent forward windows. For hive and BLE tasks, earlier complete blocks/dates may train later blocks/dates. This is distinct from claiming transfer to unseen sites, sensors or positions.', '',
              'The audit does not parse large native workbooks or repeat scientific fitting. Native reconstruction and causal-prefix guards remain separate evidence. All historical outcomes remain exposed.']
    report.with_suffix('.md').write_text('\n'.join(lines) + '\n')
    print(json.dumps({'status': result['status'], 'checks': len(result['checks']), 'missing_historical_training_scope_records': missing}))
    if result['status'] != 'pass':
        raise SystemExit(1)


if __name__ == '__main__':
    main()
