# P100-080.original.v1

**Target.** EDA mean over t+25s to t+30s

**Target units.** uS

**Metric kind.** mae

**Timing contract.** After120s observed history, every5s predict a future5s EDA mean ending30s later. All EDA,temperature and accelerometer summaries are causal and aligned by native starts/sample rates.

**Calibration.** No held-person outcome calibration. Past120s EDA is permitted state, identical for every model; response coefficients and flexible transforms fit training people only.

**Independent unit.** Participant; all aerobic segments of a person linked

**Scope limits.** One aerobic study with two protocol versions; no mental-stress or clinical diagnosis. Source device clocks are not necessarily calendar measurement dates, and manufacturer EDA calibration remains author-provided.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| level | uS |
| lag10 | uS |
| lag30 | uS |
| mean120 | uS |
| activity | g |
| temperature | degree C |
| temperature30 | degree C |
| elapsed | min |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-080.original.v1 --output NEW_SUBMISSION; then score --task P100-080.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
