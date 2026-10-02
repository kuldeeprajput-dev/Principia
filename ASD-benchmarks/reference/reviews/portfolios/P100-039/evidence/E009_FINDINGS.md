# Public earnings ranks: a reproducible association with strict disclosure limits

A standard education/age-proxy model remains competitive with more elaborate alternatives on reserved respondents. The strongest result is a well-scoped reproduction, not a new skill-return or absolute-wage law.

## Data and evaluation

PIAAC USA/Japan public files suppress exactage and absolute/PPP hourly wages. Valid earningsdeciles and source education among ages25–65 yield4236development and1054confirmation respondents. Country-linkedhashblocks preserve eachperson, with finalSPFWT0withinblocks andequalcountry/blockloss. Alltenbackground-conditioned plausiblevalues are excluded from predictors.

Target: **Upper three country-specific hourly-earnings deciles, excluding bonuses**, measured as binary EARNHRDCLC2>=8. Primary error: squared probability (Brier). Contemporaneous cross-sectional earnings association using age/education/country. All10 plausible numeracy values are excluded: conditioned on background and unsuitable individual prediction scores. This is not future earnings or causal education return.

Respondents nested in country and deterministic ten hashblocks; not10 independent samples from plausible values. Repeated respondent information stays linked. Survey clustering not publicly fully reconstructible. Respondent hashblocks within both countries; no held respondent wage fitting. Country intercepts use training respondents in that same country. No transfer to an unseen economy.

## Findings and equations

**P100-039-F01 — reproduction (partially_supported).** A standard education and coarse experience-proxy association predicts upper within-country earnings ranks better than countryprevalence and comparably to flexible controls.

p=logistic(a+bJ J+bS S+bX X+bXX X²).

Consistent with establishedMincer-style labor associations, but the binaryranktarget is notalog-wage equation and coefficients arenotpercentageearningsreturns.

Falsifying evidence and limits: Coarseage, unobservedactualexperience, employmentselection andcountry-specific ranks preventcausality/absoluteearningsclaims; numericalgainoverflexible ismodest.

**P100-039-F02 — informative_falsification (supported).** AbsolutePPP-wage and independentindividualskill-return hypotheses are not evaluable using these released fields.

No admitted absolute-wage/individual-PV equation; rejected beforefitting.

ExactAGE_R andPPPearnings areall suppressed; OECDPVs areconditionedpopulation-inferencequantities, notindividualscores.

Falsifying evidence and limits: SUPPRESSION_AUDIT.json andprimaryOECDmethodologydocument therejected prerequisites. Newdata/independentmeasurement wouldberequired.

Selected executable model: `domain`. S=educationyears-12; X=max(agebinmidpoint-educationyears-6,0)/10; J=Japanindicator. p(topthreecountryearningsdeciles)=logistic(a+bJ*J+bS*S+bX*X+bXX*X²). Coefficients inthatorder=[-3.1358399163295814, 0.11186246189215215, 0.370679096774003, 1.2373931631741675, -0.19547907390628247]. Midpoints encode publishedagebins, notexactage orworktenure; earningsranks arecountryrelative, not comparable dollaramounts.

All coefficients, input definitions, training groups and transformations are in `rules.json`; the runnable reference performs no fitting.

## Compact numerical evidence

Errors are computed within declared complete groups (with final survey weights when supplied), then averaged equally across groups.

| Frozen model | Development error | Confirmation error | Worst confirmation group |
|---|---:|---:|---:|
| reference | 0.191515 | 0.1820236 | 0.2103406 |
| constant | 0.2249295 | 0.2194144 | 0.2411918 |
| domain | 0.191515 | 0.1820236 | 0.2103406 |
| flexible | 0.192086 | 0.1836466 | 0.2108711 |

Confirmation contains 1054 scored observations in 4 groups. Individual-group scores and every attempted model remain available. Confirmation Brier0.182024 for the development-selected domainmodel versuscountryprevalence0.219414 andflexible0.183647. More elaborateattempts range lower retrospectively, but all werewithin1percent of the bestdevelopmentmodel and the simpler domainmodelwasfrozen. Fourheldhashblocks are computational partitions, notfourindependent economies.

## Interpretation, limitations and use

Only valid reported earnings deciles, ages25–65 and complete education. Final weights within equal country×respondent blocks; not a pooled national population estimand. Potential experience age-schooling-6 is proxy, not measured tenure. No skill-wage causal claim; income reporting/topcoding and nonresponse remain. Whole-group errors/ranges; no row bootstrap or manufactured independent-population confidence. Confirmation becomes exposed after freeze.

Useful for benchmark discipline: suppressed monetaryvalues and population-oriented plausiblevalues cannot become invented individualtargets/predictors. The executable task supports legitimate country-relative rank-association comparisons without claiming causal returns or individual skillmeasurement.

## Reproducibility and prior art

Run `python run.py` to verify hashes and replay every frozen equation. Predictions use declared input columns only. The shared benchmark evaluator can score alternative equations under the same task; numerical agreement with these coefficients is not required. Public source-aware confirmation is now exposed. No independent experimental replication or certified novelty is claimed.

- [Plausible values conditioned on background and intended for population inference, not individual scores.](https://www.oecd.org/en/publications/survey-of-adult-skills-2023-technical-report_80d9f692-en.html) (checked 2026-10-02).
- [Do not average10PVs into an individual score; final and replicate weights serve survey uncertainty.](https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/03/survey-of-adult-skills-2023-data-analysis-manual_07d531f6/25a87a9d-en.pdf) (checked 2026-10-02).
- [Mincer-style earnings/skill associations are extensive prior art; no new discovery from recovering education/experience gradients.](https://www.oecd.org/en/publications/how-workers-use-or-don-t-use-their-skills-in-the-workplace_0e7c6dc9-en/full-report/why-skills-use-matters_dfceb654.html) (checked 2026-10-02).
