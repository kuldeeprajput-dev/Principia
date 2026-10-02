# P100-032.original.v1

**Target.** gauge_pressure_200ms_future

**Target units.** cmH2O

**Metric kind.** mae

**Timing contract.** At each fixed1s origin predict native gauge pressure0.20s later using only present/past pressure and differential-pressure signals.

**Calibration.** Source fixed ADC-to-cmH2O conversion; no target-participant fitted coefficients. All history at or before forecast origin.

**Independent unit.** participant

**Scope limits.** Twenty healthy participants; three complete trials linked. Forecasts assess device/airway signal continuity under rapid occlusion, not separately identified lung compliance or clinical accuracy.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| p0 | cmH2O |
| p05 | cmH2O |
| p10 | cmH2O |
| p20 | cmH2O |
| p30 | cmH2O |
| p40 | cmH2O |
| p50 | cmH2O |
| di0 | cmH2O |
| de0 | cmH2O |
| di20 | cmH2O |
| de20 | cmH2O |
| trial_BH | binary |
| trial_FEM | binary |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-032.original.v1 --output NEW_SUBMISSION; then score --task P100-032.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
