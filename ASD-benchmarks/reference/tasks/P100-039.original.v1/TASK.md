# P100-039.original.v1

**Target.** Upper three country-specific hourly-earnings deciles, excluding bonuses

**Target units.** binary EARNHRDCLC2>=8

**Metric kind.** brier

**Timing contract.** Contemporaneous cross-sectional earnings association using age/education/country. All10 plausible numeracy values are excluded: conditioned on background and unsuitable individual prediction scores. This is not future earnings or causal education return.

**Calibration.** Respondent hashblocks within both countries; no held respondent wage fitting. Country intercepts use training respondents in that same country. No transfer to an unseen economy.

**Independent unit.** Respondents nested in country and deterministic ten hashblocks; not10 independent samples from plausible values. Repeated respondent information stays linked. Survey clustering not publicly fully reconstructible.

**Scope limits.** Only valid reported earnings deciles, ages25–65 and complete education. Final weights within equal country×respondent blocks; not a pooled national population estimand. Potential experience age-schooling-6 is proxy, not measured tenure. No skill-wage causal claim; income reporting/topcoding and nonresponse remain.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| education | source derived years of formal education |
| age | fixed midpoint of published five-year age bin; final60–65midpoint62.5 |
| japan | country indicator |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: source sample weights normalize within each complete group, then groups receive equal total weight. This defines the registered estimand; dependent rows do not generate population confidence intervals. Weight column: `sample_weight`. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-039.original.v1 --output NEW_SUBMISSION; then score --task P100-039.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
