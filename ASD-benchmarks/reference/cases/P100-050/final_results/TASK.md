# P100-050.original.v1

**Target.** analog laser flow-depth signal 200 ms ahead

**Target units.** m

**Metric kind.** mae

**Timing contract.** Predict analog-laser depth200ms ahead, issuing every50ms after400ms of history. All features end at the issuance time; the target remains one native1kHz sample.

**Calibration.** Causal recent laser history is permitted at every issuance. No peak alignment, future smoothing or held-run fitted offset.

**Independent unit.** Complete gate-release run/date; firstfour columns develop, final11April2024 column confirms. Five controlled events are not a field-hazard population.

**Scope limits.** This is a within-station nowcast, not advance warning upstream or a forecast before sensor detection.; The archived swath-processing example trims around a future peak; that operation is excluded. Cross-instrument alignment is not inferred.; Four debris flows and one water-only flood are described by the source, but filecolumns do not provide a reliable event-type map; no material-specific claim is made.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| h0 | m |
| h | m; mean of last20 native samples |
| v | m/s; causal100ms difference |
| a | m/s²; causal100ms second difference |
| median | m; median of last20 native samples |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-050.original.v1 --output NEW_SUBMISSION; then score --task P100-050.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
