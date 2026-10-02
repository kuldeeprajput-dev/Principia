# P100-015.original.v1

**Target.** Unable to pay hypothetical400USD emergency expense by any listed means

**Target units.** binary EF3_h

**Metric kind.** brier

**Timing contract.** Contemporaneous2025 household survey association. No future distress observation and no income intervention.

**Calibration.** Development states only; five whole-state hash folds. No held-state outcomes/calibration. EF3 other response checkboxes and EF1 savings coverage excluded to avoid near-endpoint restatement.

**Independent unit.** Respondents nested in whole states; source respondents may share unreported household/environmental dependencies. States not independent populations.

**Scope limits.** Positive-weight complete cases, state-balanced within-state survey-weighted predictive risk; not national prevalence or causal financial access. Income proxy upper bracket175k is a modeling convention. D1A0 reflects no paid work, not unemployment or a job-loss shock.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| income_proxy | thousands USD/year bracket proxy |
| household_size | persons |
| shock | no paid/profit work lastmonth (D1A0) binary, not jobloss |
| age | years |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: source sample weights normalize within each complete group, then groups receive equal total weight. This defines the registered estimand; dependent rows do not generate population confidence intervals. Weight column: `sample_weight`. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-015.original.v1 --output NEW_SUBMISSION; then score --task P100-015.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
