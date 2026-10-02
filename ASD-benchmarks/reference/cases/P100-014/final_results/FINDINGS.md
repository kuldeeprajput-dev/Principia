# Household food insufficiency: cross-wave limits of resource-response models

A compact resource-threshold model improves development risk, but its advantage over a matched flexible model does not transfer to May 2026. The portfolio supports limited descriptive resource associations and preserves a failed cross-wave extension.

## Data and evaluation

Census March/May 2026 HTOPS HPS cross-sections, 10799 complete development households and 10986 May confirmation households; four regions each. No linked SCRAMID overlap. HWEIGHT operates within equal regions. Household-size topcodes and source missing codes remain explicit.

Target: **Household sometimes/often lacked enough food during prior 7 days**, measured as binary FD_SUFF in 3, 4. Primary error: squared probability (Brier). Contemporaneous survey association; income-loss and food sufficiency recall windows overlap. No causal income effect or individual longitudinal forecast.

Household/respondent nested in Census region and wave; no linked March/May SCRAMIDs in released files. Four geographic aggregates are not independent populations. March 2026 survey only; complete-region cross-validation; May 2026 transfer without outcome calibration.

## Findings and equations

$$
p=\operatorname{logistic}\!\left(a+b_L(3-R)_++b_H(R-3)_++cS+dA\right)
$$

The notation and all fitted coefficients are defined below. Here logistic denotes the inverse-logit function; a positive-part subscript denotes max(x, 0).

**P100-014-F01  -  reproduction (partially_supported).** Declared household resources and reported income loss help describe food-insufficiency responses relative to prevalence-only prediction.

The selected resource-hinge logistic equation and its coefficients are given below.

Consistent with established material-resource vulnerability, with coarse brackets and overlapping recall windows.

Falsifying evidence and limits: May flexible model outperforms reference; four regions, complete-case selection and cross-wave composition limit generalization.

**P100-014-F02  -  informative_falsification (supported).** Development preference for a fixed resource hinge does not establish its cross-wave superiority or a physical household threshold.

Attempts 002/003/006/008/009 challenge equivalence, buffering, age curvature, link andper-capita scales.

Conflicting mean/worst-region tradeoffs and future-wave reversal expose model-selection uncertainty.

Falsifying evidence and limits: Held Brier reference 0.060243 exceeds flexible 0.059176; source has no independent intervention outcome.

Selected executable model: `attempt_005`. R=ln(I/sqrt(H)), A=(age-45)/20, S=employment-income-loss flag. p=logistic(a+bL*(3-R)_+ +bH*(R-3)_+ +c*S+d*A). Coefficients [a, bL, bH, c, d]=[-1.7111056039151187, 0.311445242697529, -2.0804188967995554, 1.126870451085675, -0.5980075149258]. I uses declared income-bracket thousand USD proxies; fixed log resource hinge 3 is not an official poverty boundary.

All coefficients, input definitions, training groups and transformations are in `rules.json`; the runnable reference performs no fitting.

## Compact numerical evidence

Errors are computed within declared complete groups (with final survey weights when supplied), then averaged equally across groups.

| Frozen model | Development error | Confirmation error | Worst confirmation group |
|---|---:|---:|---:|
| reference | 0.04928435 | 0.06024321 | 0.09721438 |
| constant | 0.05563451 | 0.06374909 | 0.1038848 |
| domain | 0.0516187 | 0.06080753 | 0.09757871 |
| flexible | 0.05004129 | 0.05917555 | 0.09484553 |

Confirmation contains 10986 scored observations in 4 groups. Individual-group scores and every attempted model remain available. Selected 005 confirmation Brier 0.060243 versus constant 0.063749, resource baseline 0.060808 and flexible 0.059176. The flexible control is better, as are several unselected alternatives; no post-confirmation reselection. Worst region 0.097214 shows substantial regional heterogeneity.

## Interpretation, limitations and use

Responding complete-case households; region-balanced HWEIGHT risk, not a national prevalence estimate. Bracket midpoints including 175 k open upper bracket are declared proxies; source topcodes preserved; missing/negative codes and nonpositive weights excluded, no imputation. Whole-group errors/ranges; no row bootstrap or manufactured independent-population confidence. Confirmation becomes exposed after freeze.

Useful for assessing whether an interpretable survey relationship transfers across survey waves and whether development-selected simplicity survives changing household composition. It does not establish a causal income-loss intervention or a new universal household-needs scale.

## Reproducibility and prior art

Run `python run.py` to verify hashes and replay every frozen equation. Predictions use declared input columns only. The shared benchmark evaluator can score alternative equations under the same task; numerical agreement with these coefficients is not required. Public source-aware confirmation is now exposed. No independent experimental replication or certified novelty is claimed.

- [March/May 2026 are cross-sectional; corrected weights 10 Sep 2026. Food insufficiency and income-shock questions are established survey constructs; household resource equivalence is a modeling hypothesis, not a new economic law.](https://www.census.gov/programs-surveys/household-pulse-survey/data/datasets.html) (checked 2026-10-02).
