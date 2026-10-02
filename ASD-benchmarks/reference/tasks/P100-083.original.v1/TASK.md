# P100-083.original.v1

**Target.** One-hour future internal sensor temperature

**Units.** degC

**Error units.** degC

**Primary metric.** rmse

**Primary metric units.** degC

**Cohort.** P100-083.original.v1.cohort-1

**Prediction time.** One hourly origin: first native observation within first15min. Forecast nominal1hour, score nearest native target within5min, same calendar day, no interpolation. Causal lag<=origin−1hour within15min. Latest20percent native dates per stream reserved. Native response outliers retained.

**Independent unit.** future native-date block per calibrated sensor stream

**Hierarchy.** group

**Calibration and history.** T and Te are current internal/external Celsius temperatures; T−1 is a causal one-hour lag, He is current external relative humidity percent, and v is external vapor-pressure deficit in kPa. Five offsets c_s are−0.384543,−0.316614,−0.340834,+0.138741,+0.323654degC in rules.json sensor order. Coefficients ba=−0.002878, br=0.050874, bm=0.083403 are dimensionless; bv=0.481876degC/kPa and bvr=0.084243/kPa. The reference30degC is an algebraic centering constant, not a prescribed biological setpoint.

**Limits.** Latest native dates at five calibrated sensor streams from one apiary; sensor/colony, species and season are confounded. No unseen-apiary or colony-health prediction.

**Historical exposure record.** All packaged targets are now exposed; future scoring is retrospective. Timestamp/input dictionaries examined; no future confirmation targets or score viewed before protocol freezing.

**Current exposure.** All outcomes exposed; future scoring is retrospective.

**Source scope.** original_corpus

**Source.** https://zenodo.org/records/20399470

**Source terms.** cc-by-4.0

## Permitted prediction inputs

| Variable | Unit / interpretation |
|---|---|
| `stream` | calibrated sensor label |
| `T_now` | degC |
| `T_lag` | degC,causal lag1h |
| `T_external` | degC,current |
| `RH_external` | percent,current |
| `hour_sin` | dimensionless source-clock phase |
| `hour_cos` | dimensionless source-clock phase |

Identifiers and source locators are alignment metadata. They may route documented frozen calibration states; they are not a license to look up a scored target. Additional columns outside this list are not predictors.

## Reproduction and comparison

`run.py` and `rules.json` contain executable frozen equations and every coefficient. `evidence/metrics.csv` and `evidence/predictions.csv.gz` preserve the historical comparisons. The shared evaluator recalculates them and compares submitted predictions on identical covered observations. Model IDs are local to this task and are distinct from finding IDs.

Primary aggregation and eligible observations are frozen. Excluded/nonpositive log targets are reported separately from physical-unit error. Uncertainty is described at independent-group level; no row bootstrap is used. The raw adapter emits native anchors, eligibility, calibration and group records. Preparation does not fit or tune a model.

Default reference: `reference`. Comparator models: `reference`, `challenger`, `baseline_newton`, `baseline_persistence`, `baseline_rbf`, `baseline_residual_rbf`.

Use `python evaluation/benchmark.py example --task P100-083.original.v1 --output NEW_FOLDER` from the benchmark root. Historical development/confirmation separation cannot be reused as a fresh holdout after exposure.
