# P100-003.original.v1

**Target.** Next nonoverlapping16-second recorded 30–80Hz strain RMS

**Target units.** 10^-21 strain

**Metric kind.** mae

**Timing contract.** Only earlier16-second strain summaries used. Quality masks applied to entire predictor and target windows; no centered filters or future PSD.

**Calibration.** Four preceding16-second windows; training-only global coefficients.

**Independent unit.** Contiguous512-second block in one detector segment; blocks not independent experiments

**Scope limits.** Single4096-second H1 segment; this is detector-noise monitoring, not GW detection or source parameter inference. Conditional on supplied quality mask. The entire source has injectionmask23: a continuous-wave hardware injection is present. This study concerns recorded strain-band power including possible injected contribution, NOT uncontaminated detector noise or astrophysical inference. No-cbc/burst/detchar/stochastic injections required; CW status retained.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| lag1 | RMS strain in units of 1e-21 |
| lag2 | RMS strain in units of 1e-21 |
| lag3 | RMS strain in units of 1e-21 |
| lag4 | RMS strain in units of 1e-21 |
| median4 | RMS strain in units of 1e-21 |
| mad4 | RMS strain in units of 1e-21 |
| low1 | RMS strain in units of 1e-21 |
| high1 | RMS strain in units of 1e-21 |
| line1 | RMS strain in units of 1e-21 |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-003.original.v1 --output NEW_SUBMISSION; then score --task P100-003.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
