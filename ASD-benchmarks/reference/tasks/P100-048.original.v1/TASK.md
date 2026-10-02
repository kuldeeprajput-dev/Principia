# P100-048.original.v1

**Target.** Daylight downwelling longwave irradiance

**Target units.** W/m2

**Metric kind.** mae

**Timing contract.** Contemporaneous daytime downwelling longwave from independently measured temperature/RH and solar/diffuse channels. Zenith<75deg, globalSW>20W/m2, required QC=0. Cloud proxy is clipped diffuse/global ratio; not net-radiation closure.

**Calibration.** No confirmation target fitting. Causal target histories only for 38/41/95 as explicitly declared.

**Independent unit.** Whole site-day blocks; forward folds Jan21–31,July8–15,July16–24 trained on preceding dates. July25–31 both sites reserved. Two sites only and correlated days.

**Scope limits.** Only daytime empirical clear/all-sky emissivity diagnostics; no nighttime extension, no independent cloud observations, no cloud causality.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| temperature | degC |
| humidity | percent |
| solar | W/m2 |
| diffuse | W/m2 |
| zenith | degree |
| site_dra | indicator |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-048.original.v1 --output NEW_SUBMISSION; then score --task P100-048.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
