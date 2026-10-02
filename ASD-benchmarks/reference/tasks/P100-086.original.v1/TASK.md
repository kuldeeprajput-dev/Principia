# P100-086.original.v1

**Target.** Chemical potency six hours ahead

**Units.** source potency unit (undocumented)

**Error units.** source potency unit (undocumented)

**Primary metric.** mae

**Primary metric units.** source potency unit (undocumented)

**Cohort.** P100-086.original.v1.cohort-1

**Prediction time.** Strictly causal potency history and cultivation clock. Matching plus/minus 6 h uses source clock; future values only become targets.

**Independent unit.** whole production batch; chronologically latest 81 reserved

**Hierarchy.** group

**Calibration and history.** Native hx is the source-loader target. Other undocumented abbreviations are excluded. Source units are not asserted to be mg/L or activity U/mL. 406 independent production batches; rows with exact 6 h lag/horizon only. No target smoothing or imputation. This is a six-hour prediction conditional on an available current potency assay, not an inline soft sensor.

**Limits.** One industrial facility and one year; historical operational forecasting, no mechanistic law from unmapped sensors. Earlier batches only train later validation blocks.

**Historical exposure record.** All packaged targets are exposed for future agents; future scoring is retrospective. Public source-aware corpus. Illustrative header/first-row values were inspected during the semantics audit; these do not constitute blind source acquisition. All delivered targets become exposed after confirmation.

**Current exposure.** All outcomes exposed; future scoring is retrospective.

**Source scope.** original_corpus

**Source.** https://zenodo.org/records/14619074

**Source terms.** cc-by-4.0

## Permitted prediction inputs

| Variable | Unit / interpretation |
|---|---|
| `time_h` | h since cultivation, source hh |
| `current` | source potency unit; last available potency measurement |
| `slope6` | source potency unit/h from strictly past 6 h |

Identifiers and source locators are alignment metadata. They may route documented frozen calibration states; they are not a license to look up a scored target. Additional columns outside this list are not predictors.

## Reproduction and comparison

`run.py` and `rules.json` contain executable frozen equations and every coefficient. `evidence/metrics.csv` and `evidence/predictions.csv.gz` preserve the historical comparisons. The shared evaluator recalculates them and compares submitted predictions on identical covered observations. Model IDs are local to this task and are distinct from finding IDs.

Primary aggregation and eligible observations are frozen. Excluded/nonpositive log targets are reported separately from physical-unit error. Uncertainty is described at independent-group level; no row bootstrap is used. The raw adapter emits native anchors, eligibility, calibration and group records. Preparation does not fit or tune a model.

Default reference: `reference`. Comparator models: `reference`, `mechanistic_reference`, `attempt_001`, `attempt_002`, `attempt_003`, `attempt_004`, `attempt_005`, `attempt_006`, `attempt_007`, `baseline_mean`, `baseline_domain`, `baseline_rbf`, `baseline_persistence`, `attempt_008`, `attempt_009`.

Use `python evaluation/benchmark.py example --task P100-086.original.v1 --output NEW_FOLDER` from the benchmark root. Historical development/confirmation separation cannot be reused as a fresh holdout after exposure.
