# Causal short-horizon flow-depth prediction at the USGS flume

The source provides high-frequency analog-laser measurements from five controlled gate releases, together with additional rangefinder data and the authors’ swath-processing script. This task keeps the analog depth measurements at the 33 m station in their native units and predicts the signal 200 ms ahead. It uses causal recent history, without future-peak alignment or target smoothing.

Five mechanistic or measurement hypotheses were tested after the baseline controls. The development-selected oscillatory memory model achieves 12.228 mm reserved MAE, beating the flexible control (13.688 mm) but losing to simple native persistence (11.667 mm). It therefore does not earn a positive claim of improved general prediction. The clearest supported finding is negative: unattenuated slope extrapolation roughly doubles error relative to persistence.

The oscillatory equation ĥ=h+v sin(ωH)/ω+a[1−cos(ωH)]/ω² propagates a local level, slope and curvature over H=0.2 s. Its fitted ω is an effective forecast parameter, not an independently measured flow-mode frequency. This distinction prevents a useful equation comparison from becoming a false constitutive-law claim.

## Experimental scope and evaluation

Predict analog-laser depth200ms ahead, issuing every50ms after400ms of history. All features end at the issuance time; the target remains one native1kHz sample.

Calibration: Causal recent laser history is permitted at every issuance. No peak alignment, future smoothing or held-run fitted offset.

Validation unit: Complete gate-release run/date; firstfour columns develop, final11April2024 column confirms. Five controlled events are not a field-hazard population.

Report individual complete-run error; one confirmation run supports no population confidence interval.

Target: analog laser flow-depth signal 200 ms ahead (m). Errors use m. The selected reference is **oscillatory_memory**. Selection was frozen before confirmation; diagnostic winners are not substituted afterward.

| Predictor | Unit |
|---|---|
| h0 | m |
| h | m; mean of last20 native samples |
| v | m/s; causal100ms difference |
| a | m/s²; causal100ms second difference |
| median | m; median of last20 native samples |


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


## Executable equations and parameters

Each expression below uses the named inputs in the units table. `exp`, `log`, and `sqrt` have their conventional mathematical meanings. Coefficients are fitted on development data only; all calibration is declared above. The portable `rules.json` contains full precision and each model’s complete training scope.

**constant_velocity**

`h+0.2*v`

Parameters: none.

**flexible**

`b0+b1*h0+b2*h+b3*v+b4*a+b5*median`

Parameters: b0 = 0.0057035073, b1 = 0.68530464, b2 = 1.307392, b3 = -0.041932873, b4 = 0.0013639129, b5 = -1.1107696.

**persistence**

`h0`

Parameters: none.

**damped_velocity**

`h+v*tau*(1-exp(-0.2/tau))`

Parameters: tau = 0.002.

**oscillatory_memory**

`h+v*sin(omega*0.2)/omega+a*(1-cos(omega*0.2))/omega**2`

Parameters: omega = 24.355282.

**depth_dependent_memory**

`h+v*0.2/(1+k*sqrt(maximum(h,0)))`

Parameters: k = 10000.

**front_recession_asymmetry**

`h+v*where(v>0,tau_up*(1-exp(-0.2/tau_up)),tau_down*(1-exp(-0.2/tau_down)))`

Parameters: tau_up = 0.002, tau_down = 0.002.

**robust_surface_level**

`median`

Parameters: none.


## Applicability and limitations

- This is a within-station nowcast, not advance warning upstream or a forecast before sensor detection.
- The archived swath-processing example trims around a future peak; that operation is excluded. Cross-instrument alignment is not inferred.
- Four debris flows and one water-only flood are described by the source, but filecolumns do not provide a reliable event-type map; no material-specific claim is made.

Only first9ms near-zero rows were seen in schema audit. Target horizon starts600ms; reserved future values were not inspected before freeze. All final outcomes become exposed.

## Reproduction

Run `python run.py` in this final package to verify hashes and reproduce every saved prediction. Use `python run.py --inputs new.csv --output predictions.csv --model reference` only with the declared inputs and units. Numerical prediction evaluation does not certify novelty or mechanism. Source anchors and reserved observations are separate from predictor inputs.

Source: https://doi.org/10.5066/P1HXHGZN. See source/units audit and prior-art records in research history.
