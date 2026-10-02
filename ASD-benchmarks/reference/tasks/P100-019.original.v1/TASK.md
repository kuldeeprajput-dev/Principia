# P100-019.original.v1

**Target.** Next-month unique received vehicle complaints per known make/model

**Target units.** complaints/month

**Metric kind.** mae

**Timing contract.** Only prior-month LDATE received counts predict next month. Retrospective snapshot may revise product labels and records; historical DATEA/report publication lag means calendar causality is not verified as-issued availability. No incident-date future information used.

**Calibration.** Cohort selected before targetperiod using>=6receivedJan–Jun2025complaints. Development targetsJul2025–Apr2026, rolling forward blocks; May–Jul2026confirmation. No target-month counts enter predictors.

**Independent unit.** Whole target months; same known vehicle cohorts repeat, lag windows overlap. Three held months are not independent fleets or defect experiments.

**Scope limits.** Administrative complaint workload among known productVmake/model labels, not vehicle failures or safety risk. No fleet-at-risk denominator, reporting propensity or causal recall effect; dedupODINO/vehicle across components, snapshot relabeling remains.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| lag1 | prior calendar month unique ODINO count |
| lag3 | mean prior3monthly counts |
| lag6 | mean prior6monthly counts |
| month | target calendar month1–12 |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-019.original.v1 --output NEW_SUBMISSION; then score --task P100-019.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
