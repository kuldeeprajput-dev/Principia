# P100-013.original.v1

**Target.** conversion

**Target units.** 1

**Metric kind.** mae

**Timing contract.** Predict author-observed DSC conversion from temperature and imposed constant heating rate; no target history.

**Calibration.** Predict author-observed DSC conversion from temperature and imposed constant heating rate; no target history.

**Independent unit.** Complete heating-rate experiment; not independent material batches

**Scope limits.** Source-fitted conversion excluded. Four development traces; one high-rate extrapolation confirmation. Audit exposed first four rows near zero of every trace.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| temperature_K | K |
| heating_rate_K_min | K/min |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-013.original.v1 --output NEW_SUBMISSION; then score --task P100-013.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
