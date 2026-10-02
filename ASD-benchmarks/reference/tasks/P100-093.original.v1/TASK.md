# P100-093.original.v1

**Target.** Induced AF488 fluorescence quantile

**Target units.** native AF488 channel units

**Metric kind.** mae

**Timing contract.** After paired uninduced control well is measured, before observing induced well target. Quantiles0.1–0.9 and cell-line identity are known; no induced fluorescence enters predictors.

**Calibration.** Same-block, same-cell-line uninduced distribution is permitted calibration for every model. Source identity compensation retained; no fitted manual gates or target-based threshold.

**Independent unit.** Matched technical replicate block across cell lines; three blocks on one plate

**Scope limits.** One plate and three technical replicate blocks. Does not establish biological-replicate transfer, transporter causality or glycan concentration. The channel/caption inconsistency prevents unqualified dye-specific biological claims.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| control | native AF488 channel units |
| control_median | native AF488 channel units |
| control_width | native AF488 channel units |
| quantile | dimensionless |
| wt | binary |
| mutant | binary |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-093.original.v1 --output NEW_SUBMISSION; then score --task P100-093.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
