# Tornado geometry and reported loss: a bounded negative industrial result

Path geometry and contextual variables improve broad loss-estimate prediction over simple controls, but errors remain very large and stronger flexible controls beat the selected compact equation. No reliable industrial damage law is demonstrated.

## Data and evaluation

2025NOAA tornado segments with explicit damage estimates,positivepathlength/maximumwidth and validtiming:1072development/224confirmation segments in363/94complete episodegroups. Reportedzero damage remainszero; missing damage is excluded, never imputed. SourceEFdamage-derivedratings and narratives are forbiddenpredictors.

Target: **Log transformed reported tornado property-damage estimate**, measured as ln(1+property damage in USD). Primary error: natural-log dollars offset1USD. Post-event path and timing diagnostic of reported loss. EF damage-derived scale, casualty counts, narratives, monetary/crop losses excluded from predictors.

NOAA EPISODE_ID outbreak groups; nearby episodes may still be correlated or linked across offices. Not individual property samples. Whole EPISODE_ID groups held; no held-event monetary outcomes. Linked tornado segments within episode remain together.

## Findings and equations

**P100-018-F01 — reproduction (partially_supported).** Recorded pathgeometry carries descriptive information about broad reported property losses.

The selected robust log-loss equation above.

Dimensions and regional/seasonal composition correlate with losses but also with reporting and asset exposure; maximumwidth timeslength is onlya bounding proxy.

Falsifying evidence and limits: Flexiblecontrols outperform, verylarge logerrors and worseextremeepisodes remain. No wind/asset exposure or independent insuredloss truth.

**P100-018-F02 — informative_falsification (supported).** The available geometry doesnot demonstrate an accurate transferable industrialdamage law.

Duration andcontext ablations005/006, plus matched robust controls, challenge the proposed law.

Negative duration slope conditional on geometry and strongfitlossdependence prevent a simple energy/exposuretime interpretation.

Falsifying evidence and limits: Reportedmonetary losses are broad estimates, not direct mechanicalresponse; heldworsterror andstrongerflexiblecontrol reject deploymentclaim.

Selected executable model: `attempt_005`. y=ln(1+damageUSD), predicted y=clip(a+bL ln(1+length_km)+bW ln(1+width_m)+bLat latitude+bSin sin(2pi month/12)+bCos cos(2pi month/12),0,50). Robust train-only residual fitting; coefficients=[3.099796961781409, 1.0765641714752674, 1.5023316079008489, -0.1478989662476028, 0.8455297618332634, -0.00746860537787219]. The length/maximumwidth proxy is not actual exposed assets, swept damage area or kinetic energy.

All coefficients, input definitions, training groups and transformations are in `rules.json`; the runnable reference performs no fitting.

## Compact numerical evidence

Errors are computed within declared complete groups (with final survey weights when supplied), then averaged equally across groups.

| Frozen model | Development error | Confirmation error | Worst confirmation group |
|---|---:|---:|---:|
| reference | 4.284359 | 4.275538 | 12.86898 |
| constant | 5.490342 | 5.439115 | 7.487723 |
| domain | 4.978277 | 5.02809 | 15.14759 |
| flexible | 4.589906 | 4.243949 | 9.299377 |

Postfreeze diagnostic controls were fitted on development data after original confirmation exposure, without reselection. They address estimation-loss asymmetry; they are not fresh preregistered confirmation.

| Added control | Development error | Exposed-cohort error |
|---|---:|---:|
| postfreeze_robust_domain | 4.920522 | 4.978022 |
| postfreeze_robust_flexible | 4.433188 | 4.05943 |

Confirmation contains 224 scored observations in 94 groups. Individual-group scores and every attempted model remain available. Selected005 confirmation MAE4.275538logunits versusconstant5.439115,areabaseline5.028090 andflexible4.243949. Worstselectedepisode12.868983 is farworse thanconstant7.487723. Postfreeze robustflexible diagnostic improves to4.059430; it was fitted ondevelopment onlyafter firstconfirmation and was not promoted. Huge log errors defeat precise financial-loss use.

## Interpretation, limitations and use

2025 tornado segments with nonmissing explicit damage. Broad estimates including reported0, not insured claim totals. Maximum width times length is bounding footprint proxy, not actual damaged area. Exposure/building stock and wind speed unavailable; no prospective loss or causal damage law. Whole-group errors/ranges; no row bootstrap or manufactured independent-population confidence. Confirmation becomes exposed after freeze.

Provides a realistic benchmark for scientific abstention: incomplete exposure and wind information cannot be replaced by a visually plausible damage-scaling formula. The practical result is a reproducible demonstration of limitedpredictability, not a pricing/insurance tool.

## Reproducibility and prior art

Run `python run.py` to verify hashes and replay every frozen equation. Predictions use declared input columns only. The shared benchmark evaluator can score alternative equations under the same task; numerical agreement with these coefficients is not required. Public source-aware confirmation is now exposed. No independent experimental replication or certified novelty is claimed.

- [Property/crop damage are broad estimates.](https://www.ncei.noaa.gov/access/storm-events-database/assets/pdf/Storm_Events_Database_User_Guide.pdf) (checked 2026-10-02).
- [Path length in miles and maximum width in yards; multi-segment tornadoes reported in segments. Geometry-loss scaling is a known descriptive approach; absent exposure forbids mechanistic damage claims.](https://www.ncei.noaa.gov/stormevents/pd01016005curr.pdf) (checked 2026-10-02).
