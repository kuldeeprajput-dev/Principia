# P100-042.original.v1

**Target.** Used primary bank or credit union in-person branch during pastmonth

**Target units.** binary BRANCH1 versus2

**Metric kind.** brier

**Timing contract.** Contemporaneous self-reported channels; ZIP branch access covariates from source linked records. Association, no causal digital substitution or closure effect.

**Calibration.** Three whole regions leave-one-region-out development; hash-reserved fourth region, no target calibration.

**Independent unit.** Respondents nested in four Census regions. Only one held region: within-survey regional transfer, no population-level precision.

**Scope limits.** Complete-case banked adult survey with positive WEIGHT_FINAL; WEIGHT_ALT is not used. Region-balanced survey-weighted risk is not national prevalence. DK/refused/skipped are exclusions, not non-use. Geographic author-derived indicators are not measured travel distance.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| mobile | pastmonth app use binary |
| web | pastmonth website use binary |
| age_category | ordered seven source bins |
| income_category | ordered nine source bins |
| branch_present | ZIP branch present Q12024 binary author-derived |
| branch_closed | ZIP net branch decrease2019Q4–2024Q1 binary author-derived |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: source sample weights normalize within each complete group, then groups receive equal total weight. This defines the registered estimand; dependent rows do not generate population confidence intervals. Weight column: `sample_weight`. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-042.original.v1 --output NEW_SUBMISSION; then score --task P100-042.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
