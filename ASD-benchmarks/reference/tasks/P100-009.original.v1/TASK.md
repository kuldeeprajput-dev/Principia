# P100-009.original.v1

**Target.** Mean pupil radius over final0.25s of horizon1s

**Target units.** px

**Metric kind.** mae

**Timing contract.** Predict1s-ahead author-released pupil radius from prior pupil and treadmill samples. Source prior filtering may be noncausal; causal-prefix guarantee applies to released traces only, not original camera pixels.

**Calibration.** No held-target calibration; observed past5s from each session supplies history. Pixel units are retained without invented millimeter scaling.

**Independent unit.** Animal, all sessions linked; two development animals and one reserved animal

**Scope limits.** Only three retained animals. Optical pixel calibration differs by animal/session; source ACh-M1/V1 recordings confound region and animal. No retinal physiology or real-time instrument claim.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| radius | px |
| lag05 | px |
| lag1 | px |
| mean5 | px |
| speed | cm/s |
| speed1 | cm/s |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-009.original.v1 --output NEW_SUBMISSION; then score --task P100-009.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
