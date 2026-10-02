# P100-051.original.v1

**Target.** measured drain current between three disclosed gate-voltage calibration anchors

**Target units.** uA

**Metric kind.** mae

**Timing contract.** offline sparse-characterization task: three responses at -20,0,20 V are obtained before reconstructing other gate points; not an uncalibrated or causal sweep forecast

**Calibration.** Exactly three same-device current measurements at Vg=-20,0,20 V; all models see the same anchors; those points excluded from scores.

**Independent unit.** complete source FET column/device

**Scope limits.** 36 fabricated FET curves from source Fig2e, not independent lots; no memory-retention extrapolation, no device-geometry control or interventions.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| gate_V | V |
| cal_minus20_uA | uA |
| cal_zero_uA | uA |
| cal_plus20_uA | uA |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-051.original.v1 --output NEW_SUBMISSION; then score --task P100-051.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
