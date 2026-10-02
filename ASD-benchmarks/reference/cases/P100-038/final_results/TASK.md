# P100-038.original.v1

**Target.** First reported RSRP-vector component at first recorded point 1.0–1.6 s after issuance

**Target units.** dBm

**Metric kind.** mae

**Timing contract.** At a recorded RSRP sample, use only component 1 in the native comma-separated RSRP vector over the preceding 20 seconds. Predict first subsequently recorded component-1 value at 1.0–1.6 s. First qualifying issuance per target; no actual future horizon feature in predictor. Unknown component antenna/beam semantics prevent propagation-law claims.

**Calibration.** No confirmation target fitting. Causal target histories only for 38/41/95 as explicitly declared.

**Independent unit.** Entire flight; forward folds 1->2,1–2->3,1–3->4; flight5 confirmation. Same installation/day only.

**Scope limits.** Telemetry files1–2 do not overlap the radio clock windows and contain repeated headers; no invented offset or geometry pairing. Vector component ordering is taken literally, not identified as a specific antenna.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| last | dBm |
| mean5 | dBm |
| mean20 | dBm |
| slope | dB/s |
| spread | dB |
| elapsed | s |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-038.original.v1 --output NEW_SUBMISSION; then score --task P100-038.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
