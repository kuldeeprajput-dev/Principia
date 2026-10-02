# P100-006.original.v1

**Target.** Ion-readout amplitude

**Target units.** arbitrary units

**Metric kind.** mae

**Timing contract.** Eight contiguous 30-condition Rabi blocks were used for leave-block-out development; blocks 06 and 09 were reserved. Frequencies and nearby Rabi coordinates are dependent. The task covers only the fixed ±60 MHz spectral neighborhood on one cesium cell.

**Calibration.** None. Inputdetuning/Rabi only. Fixed43D5/2 neighborhood abs(detuning)<=60MHz.

**Independent unit.** Entire contiguous probe-Rabi blocks; one vapor cell. No independent atomic-cell replication.

**Scope limits.** Entire contiguous probe-Rabi blocks; one vapor cell. No independent atomic-cell replication.; The asymmetric dual-response equation improves prediction on two reserved contiguous Rabi blocks compared with the single-line and polynomial controls. Its practical contribution is a scoped response surrogate with explicit uncertainty about mechanism, not a new atomic law.; No independent population confidence interval from dependent rows.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| detuning_MHz | MHz |
| rabi_MHz | MHz |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-006.original.v1 --output NEW_SUBMISSION; then score --task P100-006.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
