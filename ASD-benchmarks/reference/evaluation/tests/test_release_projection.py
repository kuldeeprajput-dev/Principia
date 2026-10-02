"""Audit a standalone export without executing any submission or native reader."""
from pathlib import Path
import argparse
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'evaluation'))
from common import load_json, save_json, verify_assets, digest, safe_path

parser = argparse.ArgumentParser()
parser.add_argument('--output', type=Path, required=True)
args = parser.parse_args()
checks = []


def check(name, function):
    try:
        detail = function()
        checks.append({'check': name, 'status': 'pass', 'detail': detail})
    except (ValueError, AssertionError, KeyError, OSError) as exc:
        checks.append({'check': name, 'status': 'fail', 'detail': str(exc)})


allow = load_json(ROOT / 'RELEASE_ALLOWLIST.json')['files']


def file_inventory():
    assert all('export_path' not in item for item in allow), 'Run on the standalone export'
    assert not any(Path(item['path']).name == '.DS_Store' for item in allow)
    admitted = {item['path'] for item in allow}
    actual = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file()}
    assert actual == admitted | {'RELEASE_ALLOWLIST.json', 'RELEASE_MANIFEST.json', 'EXPORT_RECEIPT.json'}, sorted(actual - admitted)
    return {'explicitly_admitted_files': verify_assets(ROOT, allow)}


def rights():
    rows = load_json(ROOT / 'docs/ASSET_LICENSE_REGISTER.json')['files']
    assert {item['path'] for item in rows} == {item['path'] for item in allow} - {'docs/ASSET_LICENSE_REGISTER.json'}
    return {'portable_asset_rights_records': verify_assets(ROOT, rows)}


def evidence():
    count = 0
    def walk(value):
        nonlocal count
        if isinstance(value, dict):
            if isinstance(value.get('path'), str) and 'sha256' in value:
                assert digest(safe_path(ROOT, value['path'])) == value['sha256'], value['path']
                count += 1
            for child in value.values():
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)
    walk(load_json(ROOT / 'quality/FINDING_REGISTER.json'))
    for path in sorted((ROOT / 'reviews/adjudicated').glob('*.json')):
        walk(load_json(path))
    return {'exact_evidence_bindings': count}


def registered_scope():
    registry = load_json(ROOT / 'registry.json')
    quality = load_json(ROOT / 'quality/ELIGIBILITY.json')
    raw = load_json(ROOT / 'contracts/RAW_ACCESS_REGISTRY.json')
    ids = {row['task_id'] for row in registry['tasks']}
    assert len(registry['cases']) == len(quality['cases']) == 100
    assert len(ids) == 134 and ids == {row['task_id'] for row in quality['tasks']}
    assert ids == {row['parent_task_id'] for row in raw['contracts']}
    assert 'P100-096.continuation.v1' not in ids
    assert not (ROOT / 'tasks/P100-096.continuation.v1').exists()
    assert all(row['baseline_label'] == 'implemented by GPT-6 Astra' for row in quality['cases'])
    return {'cases': 100, 'tasks': len(ids), 'baseline_label': 'implemented by GPT-6 Astra'}


check('closed_allowlist_and_no_finder_files', file_inventory)
check('portable_per_asset_rights_paths', rights)
check('projected_finding_and_adjudication_bindings', evidence)
check('registered_scope_and_baseline_attribution', registered_scope)
result = {'status': 'pass' if all(c['status'] == 'pass' for c in checks) else 'fail', 'checks': checks}
save_json(args.output, result)
print(result)
raise SystemExit(0 if result['status'] == 'pass' else 1)
