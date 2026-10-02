# Calibrated X-ray reflectivity transfer across hafnia deposition batches

The NIST source contains 56 measured X-ray reflectivity spectra from twelve hafnia-coated silicon wafers, produced in four deposition batches. The target is native intensity in counts at higher angles; a fixed five-point band near 2θ=1° supplies an explicitly allowed calibration for each spectrum. Whole deposition batches define validation, so positions from a wafer never cross partitions.

The selected finite-film interference surrogate reaches 6,200 counts wafer-balanced MAE on the fourth deposition batch, versus 11,368 for a smooth flexible envelope and 53,216 for the asymptotic Fresnel tail. Its fitted effective period is consistent with an approximately 8.64 nm optical thickness scale. This reproduces established thin-film interference and supports a useful calibrated transfer model; it does not establish a new optical law or certified absolute thickness.

Define $q=4\pi\sin\theta/\lambda$ with wavelength $\lambda=1.540593\,\AA$. The Fresnel intensity factor is $F(q)=[(q-\sqrt{q^2-q_c^2})/(q+\sqrt{q^2-q_c^2})]^2$. The selected expression below combines this factor with a roughness envelope and film-interference term. Wavevectors have units $\AA^{-1}$; roughness and thickness are in angstroms, contrast is dimensionless, and phase is in radians. The implementation guards the square root outside its admitted range.

Further fringe decoherence, position-dependent thickness and additive background were tested and preserved. None improved the primary development criterion; several trade small secondary-error differences. One reserved batch is too little for population claims, and correlated parameters prevent a unique structural interpretation.

## Experimental scope and evaluation

Predict higher-angle intensity after measuring a fixed low-angle calibration band of the same spectrum. Position and angle are known acquisition settings.

Calibration: Five native intensity samples near 2 theta 1.0 deg per spectrum; no other held-out intensity is a predictor. Same calibration for every model.

Validation unit: Complete deposition batch is the split unit; wafer is the primary aggregation unit. All positions on a wafer stay together. Three deposition batches develop; fourth confirms.

Show each held-out wafer; one reserved deposition batch supplies no independent-batch confidence interval.

Target: native higher-angle XRR intensity (counts). Errors use counts. The selected reference is **kiessig_interference**. Selection was frozen before confirmation; diagnostic winners are not substituted afterward.

| Predictor | Unit |
|---|---|
| q | $\AA^{-1}$; 4πsin(theta)/lambda |
| q0 | $\AA^{-1}$; calibration mean wavevector |
| I0 | counts; mean at 2 theta 1.0±0.008 deg |
| outer | binary non-center measurement position |


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


## Selected equation and coefficients

$$
\widehat I(q)=I_0\frac{F(q)}{F(q_0)}e^{-\sigma^2(q^2-q_0^2)}\frac{1+r\cos(qd+\phi)}{1+r\cos(q_0d+\phi)}
$$

The variables and physical dimensions are defined above; the guarded executable expression and all alternatives are in EQUATIONS.md.

| Coefficient | Frozen value |
|---|---:|
| qc | 0.0616271453 |
| sigma | 4.56630901 |
| d | 86.3623525 |
| r | 0.861594601 |
| phase | 1.32242034 |

All comparator expressions, numerical guards and full-precision values remain in EQUATIONS.md, rules.json and run.py.

## Applicability and limitations

- Twelve 200 mm wafers with 65 ALD cycles from one process; three confirmation wafers share one deposition run.
- Intensity-envelope and fringe parameters are effective metrology surrogates; density/thickness/roughness are not independently identified or verified by the author-fitted SE outputs.
- The fixed angle range lies above critical-angle effects; calibrated counts are not absolute reflectivity.

Schema inspection saw first three low-angle counts and last two points near 6 deg in wafer 11, outside the eligible target/calibration bands. Higher-angle eligible confirmation values were not inspected.

## Reproduction

Run `python run.py` in this final package to verify hashes and reproduce every saved prediction. Use `python run.py --inputs new.csv --output predictions.csv --model reference` only with the declared inputs and units. Numerical prediction evaluation does not certify novelty or mechanism. Source anchors and reserved observations are separate from predictor inputs.

Source: https://data.nist.gov/od/id/mds2-3930. See source/units audit and prior-art records in research history.
