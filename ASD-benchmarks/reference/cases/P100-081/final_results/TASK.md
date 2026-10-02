# P100-081.original.v1

**Target.** measured soil bulk density

**Target units.** g/cm³

**Metric kind.** mae

**Timing contract.** Same soil-sampling occasion; Corg, sampling depth and pH are measured covariates available before BD inference. This is a laboratory-measurement substitution task, not a future forecast.

**Calibration.** No held-out country BD calibration; country identifiers are grouping metadata, never predictors.

**Independent unit.** Entire country/site portfolio, with all transects, fields and depths linked. Eight countries are convenience samples, not a random population sample.

**Scope limits.** Texture is unavailable in six countries and excluded rather than imputed. C stocks are excluded because they use bulk density algebraically.; Observational associations do not identify an agroforestry treatment effect. Protocol adaptations and country effects may limit transfer.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| C | mass % organic carbon |
| depth | cm midpoint of sampled interval |
| pH | pH unit in water |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-081.original.v1 --output NEW_SUBMISSION; then score --task P100-081.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
