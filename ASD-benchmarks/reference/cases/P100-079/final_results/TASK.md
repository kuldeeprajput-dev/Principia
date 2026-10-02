# P100-079.original.v1

**Target.** post_treatment_DMS_emission

**Target units.** ug animal^-1 h^-1

**Metric kind.** mae

**Timing contract.** Prediction at treatment administration from pre-dose breath samples and scheduled post-dose time.

**Calibration.** Mean DMS emission at-48/-24h, difference and age at first post-dose row; five post-dose points are forecast. Other VOCs and disease labels excluded.

**Independent unit.** calf

**Scope limits.** Seven retained complete calves, while paper describes ten antibiotic-trial calves. Two reserved calves permit bounded internal transfer only. No untreated controls, dose-response or molecule-specific mechanism identification.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| hours | h |
| baseline | ug animal^-1 h^-1 |
| baseline_change | ug animal^-1 h^-1 |
| age | days |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-079.original.v1 --output NEW_SUBMISSION; then score --task P100-079.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
