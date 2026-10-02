# Causal short-horizon flow-depth prediction at the USGS flume

The source provides high-frequency analog-laser measurements from five controlled gate releases, together with additional rangefinder data and the authors’ swath-processing script. This task keeps the analog depth measurements at the 33 m station in their native units and predicts the signal 200 ms ahead. It uses causal recent history, without future-peak alignment or target smoothing.

Five mechanistic or measurement hypotheses were tested after the baseline controls. The development-selected oscillatory memory model achieves 12.228 mm reserved MAE, beating the flexible control (13.688 mm) but losing to simple native persistence (11.667 mm). It therefore does not earn a positive claim of improved general prediction. The clearest supported finding is negative: unattenuated slope extrapolation roughly doubles error relative to persistence.

The oscillatory equation ĥ=h+v sin(ωH)/ω+a[1−cos(ωH)]/ω² propagates a local level, slope and curvature over H=0.2 s. Its fitted ω is an effective forecast parameter, not an independently measured flow-mode frequency. This distinction prevents a useful equation comparison from becoming a false constitutive-law claim.

## Experimental scope and evaluation

Predict analog-laser depth 200 ms ahead, issuing every 50 ms after 400 ms of history. All features end at the issuance time; the target remains one native 1 kHz sample.

Calibration: Causal recent laser history is permitted at every issuance. No peak alignment, future smoothing or held-run fitted offset.

Validation unit: Complete gate-release run/date; first four columns develop, final 11 April 2024 column confirms. Five controlled events are not a field-hazard population.

Report individual complete-run error; one confirmation run supports no population confidence interval.

Target: analog laser flow-depth signal 200 ms ahead (m). Errors use m. The selected reference is **oscillatory_memory**. Selection was frozen before confirmation; diagnostic winners are not substituted afterward.

| Predictor | Unit |
|---|---|
| h0 | m |
| h | m; mean of last 20 native samples |
| v | m/s; causal 100 ms difference |
| a | m/s²; causal 100 ms second difference |
| median | m; median of last 20 native samples |


## Matched comparison

| Model | Development MAE | Reserved MAE | Reserved worst-group MAE |
|---|---:|---:|---:|
| constant_velocity | 0.0289558 | 0.0231933 | 0.0231933 |
| flexible | 0.0142275 | 0.0136883 | 0.0136883 |
| persistence | 0.0137181 | 0.0116672 | 0.0116672 |
| damped_velocity | 0.013819 | 0.0120813 | 0.0120813 |
| oscillatory_memory | 0.0132228 | 0.0122284 | 0.0122284 |
| depth_dependent_memory | 0.0138252 | 0.0120793 | 0.0120793 |
| front_recession_asymmetry | 0.0138483 | 0.0120813 | 0.0120813 |
| robust_surface_level | 0.0139806 | 0.0121693 | 0.0121693 |


The primary error is mean group MAE. RMSE and signed bias are complementary; rows within a group do not establish independent replication. No accuracy percentage or industrial tolerance is invented.


## Selected equation and coefficients

$$
\widehat h(t+\Delta)=h+\frac{v\sin(\omega\Delta)}{\omega}+\frac{a[1-\cos(\omega\Delta)]}{\omega^2}
$$

The horizon Delta is 0.2 s. Height h is in m, v in m/s, acceleration a in m/s^2 and omega in s^-1. This candidate failed its primary transfer comparison.

| Coefficient | Frozen value |
|---|---:|
| omega | 24.3552821 |

All comparator expressions, numerical guards and full-precision values remain in EQUATIONS.md, rules.json and run.py.

## Applicability and limitations

- This is a within-station nowcast, not advance warning upstream or a forecast before sensor detection.
- The archived swath-processing example trims around a future peak; that operation is excluded. Cross-instrument alignment is not inferred.
- Four debris flows and one water-only flood are described by the source, but file columns do not provide a reliable event-type map; no material-specific claim is made.

Only first 9 ms near-zero rows were seen in schema audit. Target horizon starts 600 ms; reserved future values were not inspected before freeze. All final outcomes become exposed.

## Reproduction

Run `python run.py` in this final package to verify hashes and reproduce every saved prediction. Use `python run.py --inputs new.csv --output predictions.csv --model reference` only with the declared inputs and units. Numerical prediction evaluation does not certify novelty or mechanism. Source anchors and reserved observations are separate from predictor inputs.

Source: https://doi.org/10.5066/P1HXHGZN. See source/units audit and prior-art records in research history.
