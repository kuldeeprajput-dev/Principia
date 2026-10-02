# Banking channels: a regional transfer limit

A multivariable model improves development prediction of branch use, but its gain does not transfer to the reserved region. This portfolio provides a reproducible negative result and resolves a consequential native codebook inconsistency.

## Data and evaluation

The CFPB National Age-Friendly Banking Survey contains paired coded and labeled native CSVs. BRANCH, MOBILE and WEB use 1=Yes and 2=No. Two local-access indicators also use 1/2 in the actual coded file despite a nominal 0/1 dictionary. CASEID-matched comparisons with all 2,721 labeled records resolve the discrepancy. The corrected eligible cohort contains 2,232 development respondents in three regions and 327 confirmation respondents in one reserved region. Positive WEIGHT_FINAL values normalize loss within each region; regions then receive equal weight.

Target: **Used primary bank or credit union in-person branch during past month**, measured as binary BRANCH = 1 versus 2. Primary error: squared probability (Brier). Contemporaneous self-reported channels; ZIP branch access covariates from source linked records. Association, no causal digital substitution or closure effect.

Respondents nested in four Census regions. Only one held region: within-survey regional transfer, no population-level precision. Three whole regions leave-one-region-out development; hash-reserved fourth region, no target calibration.

## Findings and equations

$$
p=\operatorname{logistic}\!\left(a+b_MM+b_WW+b_AA+b_II+b_PP+b_CC\right)
$$

The notation and all fitted coefficients are defined below. Here logistic denotes the inverse-logit function; a positive-part subscript denotes max(x, 0).

**P100-042-F01  -  informative_falsification (supported).** The proposed contextual digital-substitution predictor fails to improve reserved-region branch-use risk over the frozen controls.

See rules.json models.reference: p=logistic(a+bM*M+bW*W+bA*A+bI*I+bP*P+bC*C).

Development associations depend on region and information distribution. Predictive improvement in three regions does not establish a portable mechanism.

Falsifying evidence and limits: The positive transfer claim is unsupported: reference Brier exceeds prevalence, channel-count and flexible controls in region 1.

**P100-042-F02  -  informative_falsification (supported).** The source dictionary alone is insufficient to decode local branch-access indicators in this release.

Actual native indicators: Yes=1, No=2; decode to binary using CASEID-matched labeled CSV evidence.

This is a source-semantics correction, not a new banking law. ENCODING_EVIDENCE.json records the exact concordance.

Falsifying evidence and limits: The dictionary describes 0/1 while actual coded observations use 1/2; the invalid cohort and all preliminary failures remain preserved.

Selected executable model: `attempt_005`. Let M and W denote reported mobile and web banking, A and I the declared ordinal age and income categories, P local branch presence, and C local net closure. The selected equation is p(branch use)=logistic(a+bM*M+bW*W+bA*A+bI*I+bP*P+bC*C). Coefficients in that order are [-0.5079079571484614, -0.2876866081107598, 0.2821823804919333, 0.2325154626114306, -0.07144261651671474, -0.12083207960705532, -0.03127868393386126]. Categories are ordinal encodings, not exact years or monetary measurements.

All coefficients, input definitions, training groups and transformations are in `rules.json`; the runnable reference performs no fitting.

## Compact numerical evidence

Errors are computed within declared complete groups (with final survey weights when supplied), then averaged equally across groups.

| Frozen model | Development error | Confirmation error | Worst confirmation group |
|---|---:|---:|---:|
| reference | 0.2357445 | 0.2517003 | 0.2517003 |
| constant | 0.2489585 | 0.2499101 | 0.2499101 |
| domain | 0.2492668 | 0.2489066 | 0.2489066 |
| flexible | 0.2349023 | 0.2489342 | 0.2489342 |

Confirmation contains 327 scored observations in 1 groups. Individual-group scores and every attempted model remain available. Confirmation Brier error is 0.251700, compared with 0.249910 for prevalence, 0.248907 for the digital-channel count control, and 0.248934 for the flexible control. The reference loses to all three controls in the single held region. One region cannot support a population-level confidence claim.

## Interpretation, limitations and use

Complete-case banked adult survey with positive WEIGHT_FINAL; WEIGHT_ALT is not used. Region-balanced survey-weighted risk is not national prevalence. DK/refused/skipped are exclusions, not non-use. Geographic author-derived indicators are not measured travel distance. Whole-group errors/ranges; no row bootstrap or manufactured independent-population confidence. Confirmation becomes exposed after freeze.

Useful for testing whether apparently plausible digital substitution associations survive regional transfer. Mobile and web coefficients have opposite signs, but contemporaneous self-reports, selection and confounding prevent a causal interpretation. No reduction in access barriers or branch-service benefit was demonstrated.

## Reproducibility and prior art

Run `python run.py` to verify hashes and replay every frozen equation. Predictions use declared input columns only. The shared benchmark evaluator can score alternative equations under the same task; numerical agreement with these coefficients is not required. Public source-aware confirmation is now exposed. No independent experimental replication or certified novelty is claimed.

- [Official survey/codebook/technical report; banking channel and access outcomes previously described by CFPB. Digital complementarity versus substitution is an associational challenge, not evidence of causal closures or welfare effects.](https://www.consumerfinance.gov/data-research/national-age-friendly-banking-survey-data/) (checked 2026-10-02).
