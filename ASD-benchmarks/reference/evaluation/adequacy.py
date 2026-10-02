"""Source-adequacy assessment without fabricated prediction targets or scores."""
from pathlib import Path
import importlib.util
import pandas as pd
from common import ROOT, registry, load_json, save_json, verify_assets, digest, new_output, safe_path

def assess(identifier, data_root, output):
    entries = [a for a in registry().get('assessments', []) if identifier in [a['case_id'], a['assessment_id'], str(a['case_number'])]]
    if len(entries) != 1:
        raise ValueError('Unknown or ambiguous source-adequacy assessment')
    entry = entries[0]
    package = ROOT / entry['package']
    if digest(package / 'MANIFEST.json') != entry['manifest_sha256']:
        raise ValueError('Registered adequacy package manifest mismatch')
    verify_assets(package, load_json(package / 'MANIFEST.json')['files'])
    verify_assets(ROOT, load_json(ROOT / 'EVALUATOR_MANIFEST.json')['files'])
    # All curated code and declared source bytes are checked before import.
    manifest = load_json(package / 'SOURCE_MANIFEST.json')
    verify_assets(data_root, manifest['assets'])
    base = package / 'preparation/native.py'
    spec = importlib.util.spec_from_file_location('principia_source_adequacy', base)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    d = module.prepare(Path(data_root))
    mr = d[d.modality == 'MR']
    measured = {'instances': len(d), 'patients': d.group.nunique(), 'modalities': d.modality.value_counts().to_dict(),
                'mr_echo_times_ms': sorted(mr.echo_time_ms.dropna().unique().tolist()),
                'mr_repetition_times_ms': sorted(mr.repetition_time_ms.dropna().unique().tolist()),
                'series_count': d.series.nunique(), 'frame_count': d.frame.nunique()}
    expected = load_json(package / 'data/source_evidence.json')
    for key, value in measured.items():
        if value != expected[key]:
            raise ValueError('Native adequacy evidence changed: ' + key)
    # Absence of labels is an inventory-level assessment, not a DICOM inference.
    declared = {a['path'] for a in manifest['assets']}
    source_folder = Path(manifest['assets'][0]['path']).parts[0]
    actual = {str(p.relative_to(data_root)) for p in (Path(data_root) / source_folder / 'raw').rglob('*') if p.is_file() and p.name != '.DS_Store'}
    if actual != declared:
        raise ValueError('Raw inventory changed; reassess label/calibration availability')
    out = new_output(output)
    out.mkdir(parents=True)
    d.to_csv(out / 'native_anchors.csv', index=False)
    report = {'schema_version': 'principia.adequacy/1.0', 'case_id': entry['case_id'],
              'assessment_id': entry['assessment_id'], 'status': 'scientific_abstention',
              'source_files_verified': len(declared), 'native_evidence': measured,
              'inventory_assessment': {k: expected[k] for k in expected if k not in measured},
              'prediction_metrics': None, 'predictive_comparability': False,
              'bindings': {'package_manifest_sha256': entry['manifest_sha256'], 'source_manifest_sha256': digest(package / 'SOURCE_MANIFEST.json')},
              'new_task_route': 'propose-task and independent review of a measured endpoint before comparative scoring'}
    save_json(out / 'report.json', report)
    (out / 'REPORT.md').write_text('# Source adequacy assessment\n\nThe native evidence reproduces the documented scientific abstention. No predictive score is defined for this retained subset. A new endpoint requires a separately reviewed and frozen task contract.\n')
    return report
