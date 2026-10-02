# P100-075.original.v1

**Target.** VCAM1 log2(1+CPM)

**Target units.** log2(1+CPM)

**Metric kind.** mae

**Timing contract.** Before target-condition expression assay: known stiffness/shear design and same-donor LSS30kPa calibration expression. Contemporaneous designed-culture response diagnostic; no real-time sensor or uncalibrated donor claim.

**Calibration.** One LSS/30kPa VCAM1 measurement per donor. Calibration rows excluded from target cohort; every comparator receives identical value.

**Independent unit.** Donor; four donors, three development and one confirmation

**Scope limits.** Condition response in four cultured endothelial donors; one held donor cannot establish population generalization. One measured LSS/30kPa VCAM1 calibration per donor is required.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| stiffness_kpa | kPa |
| hss | indicator HSS (10 versus 4 dyn/cm2) |
| calibration | log2(1+CPM) |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-075.original.v1 --output NEW_SUBMISSION; then score --task P100-075.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
