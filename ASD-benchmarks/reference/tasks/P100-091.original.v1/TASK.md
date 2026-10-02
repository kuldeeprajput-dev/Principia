# P100-091.original.v1

**Target.** Mean UDP trial one-way end-to-end latency

**Target units.** ms

**Metric kind.** mae

**Timing contract.** Conditional reconstruction after a60-second run. Same-run achieved throughput is permitted; all latency-derived fields, NetPwr, loss, jitter, current location targets and future TCP calibration are forbidden. Not a prospective offered-load forecast.

**Calibration.** No held-out location latency calibration. Six global offered-rate offsets and shared slope are fitted on development locations only.

**Independent unit.** Complete measurement location; all offered rates and repetitions linked. Locations share one network installation.

**Scope limits.** Q4/Q5 within the same seven-location installation; six offered rates1,10,50,100,200,500Mbit/s. No unseen offered-rate extrapolation, hardware transfer, pure radio latency or intervention claim.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| offered_Mbps | Mbit/s, configured target |
| achieved_Mbps | Mbit/s, same-run server report |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-091.original.v1 --output NEW_SUBMISSION; then score --task P100-091.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
