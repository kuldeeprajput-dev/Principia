# P100-011.original.v1

**Target.** Closed-division Server throughput for matched token-generating workloads

**Target units.** tokens/s

**Metric kind.** mae

**Timing contract.** Predict reported Server throughput using same-system Offline benchmark result, workload label and accelerator count. This is calibrated scenario transfer, not performance prediction before benchmarking.

**Calibration.** Matched Offline throughput on every evaluation system; held-system Server/Interactive results forbidden.

**Independent unit.** Submitter+platform system; all model/scenario aliases linked

**Scope limits.** Self-selected published MLPerf submissions; quality99.9 aliases removed and inferred results excluded. Different task families, software and latency constraints confound mechanism. No hardware causal efficiency ranking.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| offline | tokens/s; measured matched Offline calibration |
| accelerators | count |
| nodes | count |
| workload | source workload category |
| precision | source precision label |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-011.original.v1 --output NEW_SUBMISSION; then score --task P100-011.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
