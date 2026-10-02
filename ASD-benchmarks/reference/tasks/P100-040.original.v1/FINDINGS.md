# Taxi duration: a scoped piecewise travel-time reference

A compact distance-regime model with clock and route context improves reserved-quarter duration error over matched simple, flexible and robust controls. It is a diagnostic of completed trips, since recorded distance is known only after travel.

## Data and evaluation

The native 2025 NYC green-taxi Parquets supply pickup/dropoff timestamps, recorded distance and zones. Source-month consistency, positive duration up to 1,440 minutes, distance up to 1,000 km and known zones define eligibility before fitting. Development uses 425,327 trips in 273 complete days from January through September; confirmation uses 139,747 trips in 92 days from October through December. Forward development blocks preserve time ordering; daily aggregation prevents busy days from dominating.

Target: **Recorded completed-trip duration conditional on recorded trip distance**, measured as minutes. Primary error: minutes. Trip distance is recorded after the journey. Task is retrospective travel-time diagnostics with completed distance, not pickup-time ETA. Pickup time and endpoint categories are known; no fare/payment/duration-derived predictors.

Whole pickup calendar days; serial weather/traffic/vendor dependence persists. Forward month blocks, not random trips. Forward training on earlier whole days. Jan–Sepdevelopment,Oct–Decconfirmation. Same city/provider system; no future-day targets enter coefficients. Fixed clock windows, no held tuning.

## Findings and equations

**P100-040-F01 — validated_extension (partially_supported).** A short/long-distance and cyclic-clock equation improves completed-trip duration prediction in a reserved quarter against the frozen matched controls.

See rules.json models.reference: T_hat=clip[a+bS min(d,3)+bL max(d-3,0)+cA A+cM M+u d sin(2pi h/24)+v d cos(2pi h/24),0,10000].

A parsimonious phenomenological account of route mixtures and time-dependent congestion within this provider release.

Falsifying evidence and limits: Recorded distance is post-trip; only one city/year is tested. Negative airport offset, high residual errors and provider quality limitations exclude a universal speed or operational dispatch claim.

**P100-040-F02 — informative_falsification (supported).** Simple distance proportionality and an operational pickup-time interpretation are inadequate for this task.

Domain T=a+b*d and matched robust variant are retained; input availability excludes pickup-time use of actual trip distance.

Better fitting needs route/time structure, but that structure remains observational and calibrated to the source cohort.

Falsifying evidence and limits: The causal and information-budget limits persist even where the numerical gain is strong; no prospective intervention was performed.

Selected executable model: `attempt_005`. Let d be recorded kilometres, h pickup hour, A an airport endpoint indicator and M a Manhattan endpoint indicator. The selected equation is duration_hat=clip[a+bS*min(d,3)+bL*max(d-3,0)+cA*A+cM*M+u*d*sin(2*pi*h/24)+v*d*cos(2*pi*h/24),0,10000] minutes. Coefficients in that order are [0.3962172060772582, 4.206218762142937, 1.4586951712642668, -8.496199167224495, -0.5458579682975798, -0.2701114288660162, -0.40350729807752167]. The 3 km knot was a preregistered regime hypothesis, not an estimated physical transition.

All coefficients, input definitions, training groups and transformations are in `rules.json`; the runnable reference performs no fitting.

## Compact numerical evidence

Errors are computed within declared complete groups (with final survey weights when supplied), then averaged equally across groups.

| Frozen model | Development error | Confirmation error | Worst confirmation group |
|---|---:|---:|---:|
| reference | 9.57775 | 9.453892 | 16.74107 |
| constant | 16.02238 | 16.14732 | 23.79932 |
| domain | 13.47659 | 12.82198 | 20.94968 |
| flexible | 13.49233 | 12.7087 | 21.29829 |
| robust_domain | 10.3276 | 10.15615 | 17.40729 |
| robust_flexible | 10.54388 | 10.26902 | 17.69616 |

Confirmation contains 139747 scored observations in 92 groups. Individual-group scores and every attempted model remain available. Confirmation mean daily MAE is 9.453892 minutes versus 12.821982 for overhead-plus-distance, 12.708702 for the flexible control, 10.156146 for a matched robust distance control and 10.269022 for matched robust flexible fitting. Worst-day reference MAE is 16.741070 minutes. Attempt006 performs slightly better on confirmation but remains unselected under the frozen development parsimony rule.

## Interpretation, limitations and use

Green-taxi2025 declared routine records, duration0–24h and distance0–1000km; known officialzones and source-month-consistent timestamps. Provider-reported records may contain errors; no congestion intervention, routing policy or achieved operational benefit. Whole-group errors/ranges; no row bootstrap or manufactured independent-population confidence. Confirmation becomes exposed after freeze.

The different short/long-distance slopes are consistent with a mixture of local stopping, route composition and faster longer-distance travel. They do not identify causal road speeds. A negative airport offset creates unphysical extrapolations for very short hypothetical airport trips; nonnegative clipping is explicit. Provider-record errors and large tails remain. No operational ETA or routing benefit has been measured.

## Reproducibility and prior art

Run `python run.py` to verify hashes and replay every frozen equation. Predictions use declared input columns only. The shared benchmark evaluator can score alternative equations under the same task; numerical agreement with these coefficients is not required. Public source-aware confirmation is now exposed. No independent experimental replication or certified novelty is claimed.

- [Official trip dictionaries/zone lookup; provider-submitted records have no accuracy guarantee. Distance/time scaling and daily traffic cycles are established; no prospective routing benefit follows from post-trip distance prediction.](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) (checked 2026-10-02).
