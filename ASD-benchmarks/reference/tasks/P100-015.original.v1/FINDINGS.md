# Emergency-expense resilience: a scoped household-resource reference

A compact piecewise-resource probability model predicts the SHED inability-to-pay400USD response better than matched controls on reserved states. The gain is modest and observational; it is not a causal poverty threshold, lending rule or demonstrated intervention.

## Data and evaluation

2025 Federal Reserve SHED public-use cross-section,12934respondents. Forty-one states supply10719development respondents; ten complete hash-reserved states supply2215confirmation respondents. Final survey weights operate within equal state losses. Official source-coded labels map deterministically to values, with no imputation.

Target: **Unable to pay hypothetical400USD emergency expense by any listed means**, measured as binary EF3_h. Primary error: squared probability (Brier). Contemporaneous2025 household survey association. No future distress observation and no income intervention.

Respondents nested in whole states; source respondents may share unreported household/environmental dependencies. States not independent populations. Development states only; five whole-state hash folds. No held-state outcomes/calibration. EF3 other response checkboxes and EF1 savings coverage excluded to avoid near-endpoint restatement.

## Findings and equations

**P100-015-F01 — validated_extension (partially_supported).** Piecewise resource and age/work associations yield a compact regional-transfer predictor of the reported inability-to-pay response.

p=logistic(a+bL(3-R)_+ +bH(R-3)_+ +cS+dA+eA²)

A saturation-shaped resource association is consistent with heterogeneous liquidity constraints, but proxies/topcodes and overlapping self-reports preclude identifying a physical/economic threshold.

Falsifying evidence and limits: Very small margin over flexible comparator; source-aware cross-section and onlytenheldstates; endpoint is hypothetical response, not observed emergency outcome.

**P100-015-F02 — informative_falsification (supported).** Removing work status or freeing household equivalence scaling did not improve the development-selected threshold model.

Attempt005 removesS;006 replaces resource hinge with independent logI/logH coefficients.

Independent predictive contribution does not establish causal unemployment risk; S includes retirement and voluntary nonparticipation.

Falsifying evidence and limits: Attempt005 is retrospectivelybetteronconfirmationmean; it was not promoted or retuned, showing model-selection uncertainty.

Selected executable model: `attempt_004`. Let R=ln(I/sqrt(H)), where I is the declared household-income bracket proxy inthousandUSD/year and H householdsize; A=(age-45)/20; S=1 for no paid/profit work lastmonth. Selected p=logistic(a+bL*max(3-R,0)+bH*max(R-3,0)+c*S+d*A+e*A²). Coefficients inthat order are [-0.8836098559778368, 0.31380714954933303, -1.6092569888184314, 0.8557459418933252, -0.3187511278524709, -0.3612550550290176]. The fixed R=3 hinge is a model diagnostic, not an official poverty or acceptance threshold.

All coefficients, input definitions, training groups and transformations are in `rules.json`; the runnable reference performs no fitting.

## Compact numerical evidence

Errors are computed within declared complete groups (with final survey weights when supplied), then averaged equally across groups.

| Frozen model | Development error | Confirmation error | Worst confirmation group |
|---|---:|---:|---:|
| reference | 0.08374207 | 0.07371215 | 0.1212739 |
| constant | 0.1042601 | 0.08555106 | 0.1522752 |
| domain | 0.08852593 | 0.07583128 | 0.1289653 |
| flexible | 0.08519179 | 0.07404488 | 0.1254853 |

Confirmation contains 2215 scored observations in 10 groups. Individual-group scores and every attempted model remain available. Reserved-state Brier0.073712 versus constant0.085551, simple resource0.075831 and flexible0.074045. This is only about0.45percent relative better than the flexible comparator; no decisive population superiority claimed. Worst-state reference0.121274 versus flexible0.125485. Attempt005 has a lower confirmationmean but was not development-selected and remains diagnostic.

## Interpretation, limitations and use

Positive-weight complete cases, state-balanced within-state survey-weighted predictive risk; not national prevalence or causal financial access. Income proxy upper bracket175k is a modeling convention. D1A0 reflects no paid work, not unemployment or a job-loss shock. Whole-group errors/ranges; no row bootstrap or manufactured independent-population confidence. Confirmation becomes exposed after freeze.

Useful for evaluating grouped, weighted survey-risk modeling and whether compact interpretable equations can match flexible models. No causal effect of employment, actual household income amount or achieved financial-welfare benefit is demonstrated. The question measures inability to pay by any listed means, not inability to pay usingcash alone.

## Reproducibility and prior art

Run `python run.py` to verify hashes and replay every frozen equation. Predictions use declared input columns only. The shared benchmark evaluator can score alternative equations under the same task; numerical agreement with these coefficients is not required. Public source-aware confirmation is now exposed. No independent experimental replication or certified novelty is claimed.

- [Official SHED public data/codebook; emergency expense resilience is a published descriptive endpoint. Resource equivalence and age/life-cycle associations are prior model families, not established causal mechanisms in this snapshot.](https://www.federalreserve.gov/consumerscommunities/shed_data.htm) (checked 2026-10-02).
