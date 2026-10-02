# Calibrated X-ray reflectivity transfer across hafnia deposition batches

The NIST source contains 56 measured X-ray reflectivity spectra from twelve hafnia-coated silicon wafers, produced in four deposition batches. The target is native intensity in counts at higher angles; a fixed five-point band near 2θ=1° supplies an explicitly allowed calibration for each spectrum. Whole deposition batches define validation, so positions from a wafer never cross partitions.

The selected finite-film interference surrogate reaches 6,200 counts wafer-balanced MAE on the fourth deposition batch, versus 11,368 for a smooth flexible envelope and 53,216 for the asymptotic Fresnel tail. Its fitted effective period is consistent with an approximately 8.64 nm optical thickness scale. This reproduces established thin-film interference and supports a useful calibrated transfer model; it does not establish a new optical law or certified absolute thickness.

Define q=4π sinθ/λ, λ=1.540593 Å and F(q)=[(q−√(q²−q_c²))/(q+√(q²−q_c²))]². The selected expression is Î(q)=I₀ F(q)/F(q₀) exp[−σ²(q²−q₀²)] [1+r cos(qd+φ)]/[1+r cos(q₀d+φ)]. Here q,q₀,q_c are Å⁻¹; σ,d are Å; r is dimensionless; φ is radians. The implementation guards the square root outside its admitted range. Every coefficient is listed below.

Further fringe decoherence, position-dependent thickness and additive background were tested and preserved. None improved the primary development criterion; several trade small secondary-error differences. One reserved batch is too little for population claims, and correlated parameters prevent a unique structural interpretation.

## Experimental scope and evaluation

Predict higher-angle intensity after measuring a fixed low-angle calibration band of the same spectrum. Position and angle are known acquisition settings.

Calibration: Five native intensity samples near2theta1.0deg per spectrum; no other held-out intensity is a predictor. Same calibration for every model.

Validation unit: Complete deposition batch is the split unit; wafer is the primary aggregation unit. All positions on a wafer stay together. Three deposition batches develop; fourth confirms.

Show each held-out wafer; one reserved deposition batch supplies no independent-batch confidence interval.

Target: native higher-angle XRR intensity (counts). Errors use counts. The selected reference is **kiessig_interference**. Selection was frozen before confirmation; diagnostic winners are not substituted afterward.

| Predictor | Unit |
|---|---|
| q | Å⁻¹;4πsin(theta)/lambda |
| q0 | Å⁻¹; calibration mean wavevector |
| I0 | counts; mean at2theta1.0±0.008deg |
| outer | binary noncenter measurement position |


## Matched comparison

| Model | Development MAE | Reserved MAE | Reserved worst-group MAE |
|---|---:|---:|---:|
| flat_calibration | 1.92561e+06 | 1.94494e+06 | 2.16329e+06 |
| flexible | 10890.6 | 11368.2 | 14725.5 |
| fresnel_tail | 53063.8 | 53215.6 | 61941.9 |
| roughness_envelope | 14609.1 | 14928.4 | 15641.2 |
| finite_angle_fresnel | 10932 | 11243.9 | 11337.8 |
| kiessig_interference | 5988.58 | 6199.69 | 11319.3 |
| contrast_decoherence | 6031.67 | 6257.75 | 11123.3 |
| center_outer_thickness | 6166.24 | 6266.36 | 11109.5 |
| instrument_background | 6467.69 | 6693.92 | 11599.2 |


The primary error is mean group MAE. RMSE and signed bias are complementary; rows within a group do not establish independent replication. No accuracy percentage or industrial tolerance is invented.


## Executable equations and parameters

Each expression below uses the named inputs in the units table. `exp`, `log`, and `sqrt` have their conventional mathematical meanings. Coefficients are fitted on development data only; all calibration is declared above. The portable `rules.json` contains full precision and each model’s complete training scope.

**flat_calibration**

`I0`

Parameters: none.

**flexible**

`I0*(q0/q)**4*(b0+b1*q+b2*q**2+b3*q**3)+b4`

Parameters: b0 = -5.4676375, b1 = 103.0535, b2 = -559.28605, b3 = 815.90249, b4 = 20611.473.

**fresnel_tail**

`I0*(q0/q)**4`

Parameters: none.

**roughness_envelope**

`I0*(q0/q)**4*exp(-sigma**2*(q**2-q0**2))`

Parameters: sigma = 15.90302.

**finite_angle_fresnel**

`I0*(((q-sqrt(maximum(q**2-qc**2,0.0000001)))/(q+sqrt(maximum(q**2-qc**2,0.0000001))))**2)/(((q0-sqrt(maximum(q0**2-qc**2,0.0000001)))/(q0+sqrt(maximum(q0**2-qc**2,0.0000001))))**2)*exp(-sigma**2*(q**2-q0**2))`

Parameters: qc = 0.069569551, sigma = 2.4887345e-12.

**kiessig_interference**

`I0*(((q-sqrt(maximum(q**2-qc**2,0.0000001)))/(q+sqrt(maximum(q**2-qc**2,0.0000001))))**2)/(((q0-sqrt(maximum(q0**2-qc**2,0.0000001)))/(q0+sqrt(maximum(q0**2-qc**2,0.0000001))))**2)*exp(-sigma**2*(q**2-q0**2))*(1+r*cos(q*d+phase))/(1+r*cos(q0*d+phase))`

Parameters: qc = 0.061627145, sigma = 4.566309, d = 86.362353, r = 0.8615946, phase = 1.3224203.

**contrast_decoherence**

`I0*(((q-sqrt(maximum(q**2-qc**2,0.0000001)))/(q+sqrt(maximum(q**2-qc**2,0.0000001))))**2)/(((q0-sqrt(maximum(q0**2-qc**2,0.0000001)))/(q0+sqrt(maximum(q0**2-qc**2,0.0000001))))**2)*exp(-sigma**2*(q**2-q0**2))*(1+r*exp(-sc**2*q**2)*cos(q*d+phase))/(1+r*exp(-sc**2*q0**2)*cos(q0*d+phase))`

Parameters: qc = 0.060431698, sigma = 4.4534327, d = 87.303891, r = 0.95, phase = 1.1981691, sc = 3.2411437.

**center_outer_thickness**

`I0*(((q-sqrt(maximum(q**2-qc**2,0.0000001)))/(q+sqrt(maximum(q**2-qc**2,0.0000001))))**2)/(((q0-sqrt(maximum(q0**2-qc**2,0.0000001)))/(q0+sqrt(maximum(q0**2-qc**2,0.0000001))))**2)*exp(-sigma**2*(q**2-q0**2))*(1+r*cos(q*(d+dr*outer)+phase))/(1+r*cos(q0*(d+dr*outer)+phase))`

Parameters: qc = 0.061608648, sigma = 4.5473148, d = 87.642909, r = 0.86269467, phase = 1.3016794, dr = -1.4265312.

**instrument_background**

`I0*(((q-sqrt(maximum(q**2-qc**2,0.0000001)))/(q+sqrt(maximum(q**2-qc**2,0.0000001))))**2)/(((q0-sqrt(maximum(q0**2-qc**2,0.0000001)))/(q0+sqrt(maximum(q0**2-qc**2,0.0000001))))**2)*exp(-sigma**2*(q**2-q0**2))*(1+r*cos(q*d+phase))/(1+r*cos(q0*d+phase))+background`

Parameters: qc = 0.057375778, sigma = 6.1574655, d = 86.372444, r = 0.86971607, phase = 1.27576, background = 1677.5033.


## Applicability and limitations

- Twelve200mmwafers with65ALDcycles from one process; three confirmation wafers share one deposition run.
- Intensity-envelope and fringe parameters are effective metrology surrogates; density/thickness/roughness are not independently identified or verified by the author-fitted SE outputs.
- The fixed angle range lies above critical-angle effects; calibrated counts are not absolute reflectivity.

Schema inspection saw firstthree low-angle counts and lasttwo points near6deg in wafer11, outside the eligible target/calibration bands. Higher-angle eligible confirmation values were not inspected.

## Reproduction

Run `python run.py` in this final package to verify hashes and reproduce every saved prediction. Use `python run.py --inputs new.csv --output predictions.csv --model reference` only with the declared inputs and units. Numerical prediction evaluation does not certify novelty or mechanism. Source anchors and reserved observations are separate from predictor inputs.

Source: https://data.nist.gov/od/id/mds2-3930. See source/units audit and prior-art records in research history.
