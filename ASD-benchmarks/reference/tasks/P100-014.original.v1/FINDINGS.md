# Household food insufficiency: cross-wave limits of resource-response models

A compact resource-threshold model improves development risk, but its advantage over a matched flexible model does not transfer to May2026. The portfolio supports limited descriptive resource associations and preserves a failed cross-wave extension.

## Data and evaluation

Census March/May2026 HTOPS HPS cross-sections,10799complete development households and10986Mayconfirmation households; fourregions each. No linkedSCRAMID overlap. HWEIGHT operates within equalregions. Household-size topcodes and source missing codes remain explicit.

Target: **Household sometimes/often lacked enough food during prior7days**, measured as binary FD_SUFF in3,4. Primary error: squared probability (Brier). Contemporaneous survey association; income-loss and food sufficiency recall windows overlap. No causal income effect or individual longitudinal forecast.

Household/respondent nested in Census region and wave; no linked March/May SCRAMIDs in released files. Four geographic aggregates are not independent populations. March2026 survey only; complete-region cross-validation; May2026 transfer without outcome calibration.

## Findings and equations

**P100-014-F01 — reproduction (partially_supported).** Declared household resources and reported income loss help describe food-insufficiency responses relative to prevalence-only prediction.

Resource-hinge logistic equation above.

Consistent with established material-resource vulnerability, with coarse brackets and overlapping recall windows.

Falsifying evidence and limits: Mayflexible model outperforms reference; fourregions,complete-case selection and cross-wave composition limit generalization.

**P100-014-F02 — informative_falsification (supported).** Development preference for a fixed resource hinge does not establish its cross-wave superiority or a physical household threshold.

Attempts002/003/006/008/009 challenge equivalence,buffering,agecurvature,link andper-capita scales.

Conflicting mean/worst-region tradeoffs and future-wave reversal expose model-selection uncertainty.

Falsifying evidence and limits: HeldBrierreference0.060243 exceedsflexible0.059176; source has no independent intervention outcome.

Selected executable model: `attempt_005`. R=ln(I/sqrt(H)), A=(age-45)/20, S=employment-income-loss flag. p=logistic(a+bL*(3-R)_+ +bH*(R-3)_+ +c*S+d*A). Coefficients [a,bL,bH,c,d]=[-1.7111056039151187, 0.311445242697529, -2.0804188967995554, 1.126870451085675, -0.5980075149258]. I uses declared income-bracket thousandUSD proxies; fixed logresource hinge3 is not an official poverty boundary.

All coefficients, input definitions, training groups and transformations are in `rules.json`; the runnable reference performs no fitting.

## Compact numerical evidence

Errors are computed within declared complete groups (with final survey weights when supplied), then averaged equally across groups.

| Frozen model | Development error | Confirmation error | Worst confirmation group |
|---|---:|---:|---:|
| reference | 0.04928435 | 0.06024321 | 0.09721438 |
| constant | 0.05563451 | 0.06374909 | 0.1038848 |
| domain | 0.0516187 | 0.06080753 | 0.09757871 |
| flexible | 0.05004129 | 0.05917555 | 0.09484553 |

Confirmation contains 10986 scored observations in 4 groups. Individual-group scores and every attempted model remain available. Selected005 confirmation Brier0.060243 versusconstant0.063749,resourcebaseline0.060808 andflexible0.059176. The flexible control is better, as are several unselected alternatives; no post-confirmation reselection. Worstregion0.097214 shows substantial regional heterogeneity.

## Interpretation, limitations and use

Responding complete-case households; region-balanced HWEIGHT risk, not a national prevalence estimate. Bracket midpoints including175k open upper bracket are declared proxies; source topcodes preserved; missing/negative codes and nonpositive weights excluded, no imputation. Whole-group errors/ranges; no row bootstrap or manufactured independent-population confidence. Confirmation becomes exposed after freeze.

Useful for assessing whether an interpretable survey relationship transfers across surveywaves and whether development-selected simplicity survives changing household composition. It does not establish a causal income-loss intervention or a new universal household-needs scale.

## Reproducibility and prior art

Run `python run.py` to verify hashes and replay every frozen equation. Predictions use declared input columns only. The shared benchmark evaluator can score alternative equations under the same task; numerical agreement with these coefficients is not required. Public source-aware confirmation is now exposed. No independent experimental replication or certified novelty is claimed.

- [March/May2026 are cross-sectional; corrected weights10Sep2026. Food insufficiency and income-shock questions are established survey constructs; household resource equivalence is a modeling hypothesis, not a new economic law.](https://www.census.gov/programs-surveys/household-pulse-survey/data/datasets.html) (checked 2026-10-02).
