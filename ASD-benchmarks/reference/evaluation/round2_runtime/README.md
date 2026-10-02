# Frozen continuation reference runtime

This package standardizes the 15 older scenario continuations into executable prediction-only references. It does not fit models or choose a scientific winner.

`materialize.export_case(case_id, output_directory)` is a one-time migration tool. It reads already frozen historical state, verifies the historical prediction checksum, and writes the standalone files below without touching prepared data or evidence supplied by the benchmark builder:

- `run.py`: `read_table(path)`, `load_model(name, mode="oof")`, and `predict(model, dataframe)`.
- `model.json`: initial preregistered round2 candidate, with independent outer-fold models and an explicit sample-to-fold routing map.
- `states/`: all competing frozen models, including unfavorable controls and predecessor baselines.
- `rules.json`: reference names, numerical evidence, and explicit default-reference meaning.
- `reference_runtime/`: audited static numerical functions with no fitting or research-history imports.
- `runtime_manifest.json`: hashes checked before importing numerical dependency modules.
- `reference_provenance.json`: source-state and source-prediction hashes.

The migration tool requires the preserved historical collection. Exported references do not. Only NumPy, pandas and SciPy are needed for prediction.

## Out-of-fold versus deployment prediction

The default mode reconstructs historically independent outer-fold predictions. A sample ID routes to its frozen fold model; it never looks up a stored prediction. Model inputs remain the task-declared measurements. Reordering or selecting a subset does not change the model assigned to a sample. Unknown or duplicate sample IDs fail clearly.

The separately stored full-development state is available only with explicit `mode="deployment"` or CLI `--mode deployment`. It is not an out-of-fold reference and must not be presented as independent evaluation evidence.

```
python run.py --input inputs.csv.gz --output predictions.csv --model current/cycle-001
```

The first round2 candidate is the default for reproducibility, not an automatic finding admission or assertion that it is the best model. All 180 historical models remain separately executable. Future submissions may use different equations and are scored by the shared evaluator.

## Required input extensions

The union of all historical reference inputs contains three fields beyond the frozen round2 `NUM`/`CAT` lists: scenario 27 needs `saturation_temperature_K`, scenario 61 needs `membrane_index`, and scenario 82 needs the declared causal `past_temperature` history used by predecessor comparators. These fields must be declared in the task contract. Identifiers used only for fold routing are not numerical predictors.

For scenario 82, `past_temperature` is the mean observed temperature over strictly earlier dates at the same site within 30 days, defaulting to 10 °C when unavailable. No respiration response enters this transform.

## Verification

All 180 model/cohort combinations across 15 cases reproduce 1,353,974 stored predictions with maximum absolute difference 2.14e-13. Additional checks cover reordered rows, target poisoning, unknown and duplicate OOF IDs, explicit deployment mode, isolated subprocess prediction and corrupted-state rejection before loading numerical modules. No scientific parameter was refitted during migration.
