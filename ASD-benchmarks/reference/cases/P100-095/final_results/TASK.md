# P100-095.original.v1

**Target.** Next half-hour author-derived turbulent kinetic energy

**Target units.** m2/s2

**Metric kind.** mae

**Timing contract.** Predict next30-min author-derived TKE from completed previous30-min TKE, mean velocity and two-height temperature gradient. No contemporaneous target variance/covariance inputs. Both intervals RawAnyS2/H2 flags0; predictor MetT0.

**Calibration.** No confirmation target fitting. Causal target histories only for 38/41/95 as explicitly declared.

**Independent unit.** Whole ISO weeks. Forward folds week4, weeks7–8, weeks9–10 with all earlier weeks training. March15 onward weeks11–13 confirmation. One mountain station during one winter.

**Scope limits.** MeanTKE2 is author-derived from turbulent measurements; mean wind/thermal gradients are observational predictors, not mechanical interventions. Flag0 subset can select calmer/instrument-quality regimes; no universal turbulence closure.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| energy | m2/s2 |
| wind | m/s |
| vertical | m/s |
| temperature | degC |
| gradient | K/m |
| sin_direction | unitless |
| cos_direction | unitless |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-095.original.v1 --output NEW_SUBMISSION; then score --task P100-095.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
