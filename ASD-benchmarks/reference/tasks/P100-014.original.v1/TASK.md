# P100-014.original.v1

**Target.** Household sometimes/often lacked enough food during prior7days

**Target units.** binary FD_SUFF in3,4

**Metric kind.** brier

**Timing contract.** Contemporaneous survey association; income-loss and food sufficiency recall windows overlap. No causal income effect or individual longitudinal forecast.

**Calibration.** March2026 survey only; complete-region cross-validation; May2026 transfer without outcome calibration.

**Independent unit.** Household/respondent nested in Census region and wave; no linked March/May SCRAMIDs in released files. Four geographic aggregates are not independent populations.

**Scope limits.** Responding complete-case households; region-balanced HWEIGHT risk, not a national prevalence estimate. Bracket midpoints including175k open upper bracket are declared proxies; source topcodes preserved; missing/negative codes and nonpositive weights excluded, no imputation.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| income_proxy | thousands USD/year, bracket proxy not observed amount |
| household_size | persons, source topcoded7 |
| shock | household lost employment income past4weeks binary |
| age | respondent years |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: source sample weights normalize within each complete group, then groups receive equal total weight. This defines the registered estimand; dependent rows do not generate population confidence intervals. Weight column: `sample_weight`. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-014.original.v1 --output NEW_SUBMISSION; then score --task P100-014.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
