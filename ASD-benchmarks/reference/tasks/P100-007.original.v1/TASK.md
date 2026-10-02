# P100-007.original.v1

**Target.** Plate1 vertical force,100ms ahead,10ms mean

**Target units.** N

**Metric kind.** mae

**Timing contract.** Causal10ms block means sampled100Hz from source1000Hz sequence. At block end t, predict the10ms block ending t+100ms. Every feature uses blocks ending at or before t.

**Calibration.** No target calibration from held run; preceding five seconds of its force waveform supply causal period and history. Known treadmill speed is permitted.

**Independent unit.** Entire speed run within one participant; only two development runs and one faster reserved run

**Scope limits.** One participant, three treadmill speeds; no independent-person generalization. Force-platform channels are signed and the source timing columns are unusable.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| force | N |
| lag20 | N |
| lag50 | N |
| lag100 | N |
| opposite | N |
| opposite50 | N |
| cycle | N |
| cycle_previous | N |
| period | s |
| speed | m/s |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-007.original.v1 --output NEW_SUBMISSION; then score --task P100-007.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
