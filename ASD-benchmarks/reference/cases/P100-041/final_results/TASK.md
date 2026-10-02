# P100-041.original.v1

**Target.** Unimputed hourly balancing-authority demand

**Target units.** MW

**Metric kind.** mae

**Timing contract.** Retrospective published-snapshot forecast correction. Input official forecast for target hour, preceding-hour forecast, and actual/forecast residuals 48 and168 hours before target. Nominal issuance t−24h is an analysis convention, not observed release timestamp. Inputs at least24h older than nominal issuance; exact publication and revision vintages unavailable. No target-hour demand, generation or interchange predictor.

**Calibration.** No confirmation target fitting. Causal target histories only for 38/41/95 as explicitly declared.

**Independent unit.** Authority-month groups; rolling train Jan–Feb->March, Jan–March->April, Jan–April->May. June confirmation. Same authorities across time, correlated national weather; no independence claim across all authorities.

**Scope limits.** Unimputed native Demand/Forecast only. Revised final public snapshot is not an as-issued operational backtest. Negative/nonfinite demand/forecasts excluded by validity rule before fitting. Primary MW MAE is not normalized by authority load.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| forecast | MW |
| error48 | MW |
| error168 | MW |
| load48 | MW |
| load168 | MW |
| ramp | MW |
| hour | UTC hour |
| weekend | indicator |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-041.original.v1 --output NEW_SUBMISSION; then score --task P100-041.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
