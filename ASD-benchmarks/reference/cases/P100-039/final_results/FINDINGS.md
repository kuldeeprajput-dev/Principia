# Public earnings ranks: a reproducible association with strict disclosure limits

A standard education/age-proxy model remains competitive with more elaborate alternatives on reserved respondents. The strongest result is a well-scoped reproduction, not a new skill-return or absolute-wage law.

## Data and evaluation

PIAAC USA/Japan public files suppress exact age and absolute/PPP hourly wages. Valid earnings deciles and source education among ages 25-65 yield 4236 development and 1054 confirmation respondents. Country-linked hash blocks preserve each person, with final `SPFWT0` within blocks and equal country/block loss. All ten background-conditioned plausible values are excluded from predictors.

Target: **Upper three country-specific hourly-earnings deciles, excluding bonuses**, measured as binary `EARNHRDCLC2`>=8. Primary error: squared probability (Brier). Contemporaneous cross-sectional earnings association using age/education/country. All 10 plausible numeracy values are excluded: conditioned on background and unsuitable individual prediction scores. This is not future earnings or causal education return.

Respondents nested in country and deterministic ten hash blocks; not 10 independent samples from plausible values. Repeated respondent information stays linked. Survey clustering not publicly fully reconstructible. Respondent hash blocks within both countries; no held respondent wage fitting. Country intercepts use training respondents in that same country. No transfer to an unseen economy.

## Findings and equations

$$
p=\operatorname{logistic}\!\left(a+b_JJ+b_SS+b_XX+b_{XX}X^2\right)
$$

The notation and all fitted coefficients are defined below. Here logistic denotes the inverse-logit function; a positive-part subscript denotes max(x, 0).

**P100-039-F01  -  reproduction (partially_supported).** A standard education and coarse experience-proxy association predicts upper within-country earnings ranks better than country prevalence and comparably to flexible controls.

p=logistic(a+bJ J+bS S+bX X+bXX X²).

Consistent with established Mincer-style labor associations, but the binary rank target is not a log-wage equation and coefficients are not percentage earnings returns.

Falsifying evidence and limits: Coarse age, unobserved actual experience, employment selection and country-specific ranks prevent causality/absolute earnings claims; numerical gain over flexible ismodest.

**P100-039-F02  -  informative_falsification (supported).** Absolute PPP-wage and independent individual skill-return hypotheses are not evaluable using these released fields.

No admitted absolute-wage/individual-PV equation; rejected before fitting.

Exact AGE_R and PPP earnings are all suppressed; OECD PVs are conditioned population-inference quantities, not individual scores.

Falsifying evidence and limits: SUPPRESSION_AUDIT.json and primary OECD methodology document the rejected prerequisites. New data/independent measurement would be required.

Selected executable model: `domain`. S=education years-12; X=max(age-bin midpoint-education years-6, 0)/10; J=Japan indicator. p(top three country earnings deciles)=logistic(a+bJ*J+bS*S+bX*X+bXX*X²). Coefficients in that order=[-3.1358399163295814, 0.11186246189215215, 0.370679096774003, 1.2373931631741675, -0.19547907390628247]. Midpoints encode published age bins, not exact age orwork tenure; earnings ranks are country relative, not comparable dollar amounts.

All coefficients, input definitions, training groups and transformations are in `rules.json`; the runnable reference performs no fitting.

## Compact numerical evidence

Errors are computed within declared complete groups (with final survey weights when supplied), then averaged equally across groups.

| Frozen model | Development error | Confirmation error | Worst confirmation group |
|---|---:|---:|---:|
| reference | 0.191515 | 0.1820236 | 0.2103406 |
| constant | 0.2249295 | 0.2194144 | 0.2411918 |
| domain | 0.191515 | 0.1820236 | 0.2103406 |
| flexible | 0.192086 | 0.1836466 | 0.2108711 |

Confirmation contains 1054 scored observations in 4 groups. Individual-group scores and every attempted model remain available. Confirmation Brier 0.182024 for the development-selected domain model versus country prevalence 0.219414 and flexible 0.183647. More elaborate attempts range lower retrospectively, but all were within 1 percent of the best development model and the simpler domain model was frozen. Four held hash blocks are computational partitions, not four independent economies.

## Interpretation, limitations and use

Only valid reported earnings deciles, ages 25-65 and complete education. Final weights within equal country×respondent blocks; not a pooled national population estimand. Potential experience age-schooling-6 is proxy, not measured tenure. No skill-wage causal claim; income reporting/topcoding and nonresponse remain. Whole-group errors/ranges; no row bootstrap or manufactured independent-population confidence. Confirmation becomes exposed after freeze.

Useful for benchmark discipline: suppressed monetary values and population-oriented plausible values cannot become invented individual targets/predictors. The executable task supports legitimate country-relative rank-association comparisons without claiming causal returns or individual skill measurement.

## Reproducibility and prior art

Run `python run.py` to verify hashes and replay every frozen equation. Predictions use declared input columns only. The shared benchmark evaluator can score alternative equations under the same task; numerical agreement with these coefficients is not required. Public source-aware confirmation is now exposed. No independent experimental replication or certified novelty is claimed.

- [Plausible values conditioned on background and intended for population inference, not individual scores.](https://www.oecd.org/en/publications/survey-of-adult-skills-2023-technical-report_80d9f692-en.html) (checked 2026-10-02).
- [Do not average 10 PVs into an individual score; final and replicate weights serve survey uncertainty.](https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/03/survey-of-adult-skills-2023-data-analysis-manual_07d531f6/25a87a9d-en.pdf) (checked 2026-10-02).
- [Mincer-style earnings/skill associations are extensive prior art; no new discovery from recovering education/experience gradients.](https://www.oecd.org/en/publications/how-workers-use-or-don-t-use-their-skills-in-the-workplace_0e7c6dc9-en/full-report/why-skills-use-matters_dfceb654.html) (checked 2026-10-02).
