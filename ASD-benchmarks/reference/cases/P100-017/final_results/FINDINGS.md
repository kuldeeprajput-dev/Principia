# Reported earthquake depth uncertainty: geometry and source-estimator regimes

A compact robust geometry/reporting-regime equation predicts supplied depth uncertainty better than the original controls on held event clusters. The result concerns the catalog estimator, not independent true earthquake-depth accuracy or a new seismic law.

## Data and evaluation

2607 July 2026 catalog events each have exactly one QuakeML origin. Positive, finite uncertainty/RMS/count eligibility yields 2274 development and 271 confirmation events, in 516/130 complete spatiotemporal clusters. Source coordinates/times define 100 km/7 day connected components before error analysis.

Target: **Author-reported origin depth uncertainty**, measured as km. Primary error: absolute natural-log ratio. Contemporaneous reported location-quality diagnostics, never pre-event earthquake forecast or independent true depth error.

Transitive clusters within 100 km great-circle chord and 7 days; complete cluster hashfolds. Distant events may still share network/systematic velocity model errors. Complete spatiotemporal connected clusters held out; same snapshot networks/measurement procedures. No new waveform or independent hypocenter calibration.

## Findings and equations

$$
\widehat\sigma=\exp\!\left(a+b_R\ln R+b_N\ln N+c_GG+c_AA+c_D\ln(1+|d|)+c_{10}I_{10}+c_SI_{<5}\right)
$$

The notation and all fitted coefficients are defined below.

**P100-017-F01  -  validated_extension (partially_supported).** Reporting-regime and geometry covariates provide a compact predictor of author-supplied positive depth uncertainty in this source snapshot.

The selected robust log-uncertainty equation and its coefficients are given below.

Near-station leverage and angular coverage have known localization roles, but exact-depth indicators also encode catalog processing practices. Improvement cannot isolate equation structure from fitting loss without the disclosed later controls.

Falsifying evidence and limits: Worst cluster does not uniformly improve; cross-network uncertainty conventions, fixed-depth reporting and no independent truth limit mechanism claims. Matched robust controls were added only after first confirmation.

**P100-017-F02  -  informative_falsification (supported).** Naive inverse-square-root phase-count scaling is insufficient as a universal uncertainty law here.

sigma proportional RMS/sqrt(Nphase) is the domain family; estimated free exponents/regimes in 002-006 challenge it.

Correlated arrivals, network geometry and differing source procedures violate independent identical measurements.

Falsifying evidence and limits: Reference predicts author formal uncertainty only; it cannot demonstrate true physical accuracy or hazard forecasting.

Selected executable model: `attempt_004`. sigma_hat=exp(a+bR ln(RMS)+bN ln(Nphase)+cG G+cA A+cD ln(1+|depth|)+c10 I(depth=10)+cS I(depth<5)), with G=0.5ln[1+(dmin/(1+|depth|))²] and A=-ln(max(1-gap/360, 0.02)). Numerical inputs use seconds, km andcounts as declared fixed reference units. Coefficients inthat order=[0.5059683260395523, 0.38408763491978104, -0.1245459549330374, 0.08698001732673424, 0.3868077313593952, 0.36476450158184914, -0.6216509362540282, 0.08021397958958204]. This is phenomenological regression with dimensionless normalized numerical ratios; bN is not automatically the independent-phase exponent-0.5.

All coefficients, input definitions, training groups and transformations are in `rules.json`; the runnable reference performs no fitting.

## Compact numerical evidence

Errors are computed within declared complete groups (with final survey weights when supplied), then averaged equally across groups.

| Frozen model | Development error | Confirmation error | Worst confirmation group |
|---|---:|---:|---:|
| reference | 0.3109677 | 0.2997433 | 1.755308 |
| constant | 0.7105668 | 0.7107532 | 2.576025 |
| domain | 0.6745367 | 0.6954668 | 1.566295 |
| flexible | 0.4301596 | 0.4341116 | 1.683547 |

Postfreeze diagnostic controls were fitted on development data after original confirmation exposure, without reselection. They address estimation-loss asymmetry; they are not fresh preregistered confirmation.

| Added control | Development error | Exposed-cohort error |
|---|---:|---:|
| postfreeze_robust_domain | 0.6632764 | 0.6813104 |
| postfreeze_robust_flexible | 0.4109096 | 0.4157607 |

Confirmation contains 271 scored observations in 130 groups. Individual-group scores and every attempted model remain available. Original confirmation log-ratioMAE 0.299743 versus constant 0.710753, information baseline 0.695467 and flexible 0.434112. Worst reference cluster 1.755308 exceeds domain 1.566295. After-exposure matched robust controls yield 0.681310 domain and 0.415761 flexible; these diagnostics keep reference unchanged and are not fresh confirmation.

## Interpretation, limitations and use

One July 2026 catalog snapshot. Positive uncertainty reports only; mixed network estimation conventions, no universal standard-error confidence interpretation. Counts/geometry are outputs of location processing and causality is not identified. Whole-group errors/ranges; no row bootstrap or manufactured independent-population confidence. Confirmation becomes exposed after freeze.

Useful as a source-quality diagnostic and a benchmark for distinguishing physical inverse-information arguments from reporting/model conventions. No supplied confidence interval is validated against independently located events, waveforms or velocity structures.

## Reproducibility and prior art

Run `python run.py` to verify hashes and replay every frozen equation. Predictions use declared input columns only. The shared benchmark evaluator can score alternative equations under the same task; numerical agreement with these coefficients is not required. Public source-aware confirmation is now exposed. No independent experimental replication or certified novelty is claimed.

- [Location quality and uncertainty definitions depend on contributing networks; not independent error truth.](https://earthquake.usgs.gov/data/comcat/index.php) (checked 2026-10-02).
- [Depth is often least-constrained, reference frames differ and fixed/negative depths occur.](https://www.usgs.gov/faqs/what-does-it-mean-earthquake-occurred-a-depth-0-km-how-can-earthquake-have-a-negative-depth) (checked 2026-10-02).
- [Known importance of nearest-station distance relative to depth, phase counts and velocity model; inverse-information and geometry hypotheses are prior-inspired.](https://pubs.usgs.gov/of/1993/0309/of93-309_v1.1.pdf) (checked 2026-10-02).
