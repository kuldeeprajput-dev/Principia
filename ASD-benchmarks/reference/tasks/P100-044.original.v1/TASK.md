# P100-044.original.v1

**Target.** capped elapsed solver resource consumption min(Total Runtime,7200s)

**Target units.** seconds

**Metric kind.** mae

**Timing contract.** All inputs are instance parameters and formulation choice known before solving; no runtime/gap/objective/work measure as input

**Calibration.** No evaluated-instance calibration

**Independent unit.** complete topology instance containing all three formulations

**Scope limits.** One solver/hardware experiment,16 structural instances,three formulations,one run each. Consumption censored by a7200s resource cap; not latent solve time or general computational complexity. No deployed impact evidence.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| nodes | node count |
| max_degree | degree bound |
| is_flow | indicator |
| is_linear | indicator |
| is_quadratic | indicator |
| moore2_occupancy | dimensionless n/(1+d^2) |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-044.original.v1 --output NEW_SUBMISSION; then score --task P100-044.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
