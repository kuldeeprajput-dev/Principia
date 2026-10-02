# P100-074.original.v1

**Target.** Src kinetic fluorescence in source instrument units

**Target units.** source fluorescence units

**Metric kind.** mae

**Timing contract.** Predict all t>7.5 min from source dose and same-curve measurements at 3,4.5,6 min. Calibration fixed at6 min; no later response access.

**Calibration.** Predict all t>7.5 min from source dose and same-curve measurements at 3,4.5,6 min. Calibration fixed at6 min; no later response access.

**Independent unit.** Complete dose curves; seven development and two hash-selected confirmation doses; leave-one-dose-out validation. No biological replicate identifiers.

**Scope limits.** One source assay, source units are not enzyme concentration or clinical activity.; Kinetic export lacks raw triplicate labels. Dose validation is not independent biological replication.; Akt1 response copying time is excluded; source fitted velocity tables are never targets.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| concentration_uM | uM |
| time_min | min |
| calibration_F6 | source fluorescence units |
| calibration_v6 | source fluorescence units/min |
| calibration_curvature | source fluorescence units/min^2 |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-074.original.v1 --output NEW_SUBMISSION; then score --task P100-074.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
