# Contact and adhesion in calibrated AFM retraction curves

The source contains paired approach/retraction AFM curves from flat, low-roughness and high-roughness cellulose acetate surfaces. The task predicts later retraction force after the complete approach and the first five retraction measurements are available. Those measurements constitute explicit calibration, rather than hidden target information. Measured deflection at the predicted point is excluded because force is its calibrated multiple.

A spherical-contact shape plus localized attraction is the development-selected reference. It obtains 1.360 nN reserved curve-balanced MAE, compared with 2.212 nN for the repulsive spherical shape and 1.522 nN for the flexible polynomial. It also improves reserved RMSE and worst-curve error over the polynomial. A later diagnostic exponent model has lower confirmation MAE but does not replace the frozen reference.

The equation F̂=B+P max(x,0)³ᐟ²−A P exp(−|x|/ℓ) uses force baseline B and early-retraction amplitude P in nN. The coordinate x is dimensionless normalized piezo position relative to a fixed approach-force crossing; A and ℓ are dimensionless. The attraction term captures a localized force deficit around detachment. Because x is not true indentation, this equation is an effective calibrated surrogate and cannot certify Young’s modulus, adhesion energy or a new constitutive law.

There are 13 curve locations and three physical sample categories, with one whole curve per category reserved. Neither independent manufacturing transfer nor a biological cell-response claim is established.

## Experimental scope and evaluation

Predict late retraction after the entire approach and firstfive retraction samples are available. Targets begin at retractionindex16. Measured retraction deflection is excluded because it algebraically determines force.

Calibration: Approach baseline, first5nNabovebaselinecrossing, known ramp extent, and initialfive retractionforce samples. Everycandidate receives the same frozen summaries.

Validation unit: Complete approach/retraction curve is held together; one hashselectedcurveper surface type confirms. Curves are locations on three samples, not independentmanufacturingbatches.

Curve-wise errors; three heldcurve locations do not justify independentmaterialpopulationconfidence.

Target: native AFM retraction force (nN). Errors use nN. The selected reference is **localized_adhesion**. Selection was frozen before confirmation; diagnostic winners are not substituted afterward.

| Predictor | Unit |
|---|---|
| x | dimensionless normalized piezo position relative to fixed5nNapproach crossing |
| base | nN; mean first10approachpoints |
| amp | nN; initialretractionlevel minusbase |
| progress | dimensionless fraction ofretractionramp |


## Matched comparison

| Model | Development MAE | Reserved MAE | Reserved worst-group MAE |
|---|---:|---:|---:|
| flexible | 1.66724 | 1.52241 | 1.81065 |
| hertz_shape | 2.11141 | 2.21229 | 2.9722 |
| initial_level | 38.1091 | 38.0093 | 38.7841 |
| conical_contact | 2.01419 | 2.12941 | 2.78362 |
| localized_adhesion | 1.56177 | 1.35975 | 1.72774 |
| shifted_contact_pull_off | 1.81803 | 1.39355 | 1.88172 |
| rough_asperity_exponent | 1.64024 | 1.28194 | 1.54597 |
| hysteretic_detachment | 1.72594 | 1.3856 | 2.21132 |


The primary error is mean group MAE. RMSE and signed bias are complementary; rows within a group do not establish independent replication. No accuracy percentage or industrial tolerance is invented.


## Executable equations and parameters

Each expression below uses the named inputs in the units table. `exp`, `log`, and `sqrt` have their conventional mathematical meanings. Coefficients are fitted on development data only; all calibration is declared above. The portable `rules.json` contains full precision and each model’s complete training scope.

**flexible**

`base+amp*(b0+b1*x+b2*x**2+b3*x**3+b4*x**4)`

Parameters: b0 = -0.14312993, b1 = -0.13844709, b2 = -0.03699308, b3 = -0.0014587107, b4 = 0.00030246077.

**hertz_shape**

`base+amp*maximum(x,0)**1.5`

Parameters: none.

**initial_level**

`base+amp`

Parameters: none.

**conical_contact**

`base+amp*maximum(x,0)**2`

Parameters: none.

**localized_adhesion**

`base+amp*maximum(x,0)**1.5-A*amp*exp(-abs(x)/ell)`

Parameters: A = 0.28997713, ell = 0.53665727.

**shifted_contact_pull_off**

`base+amp*(maximum(x+shift,0)/(1+shift))**1.5-A*amp*exp(-((x-center)/width)**2)`

Parameters: shift = -0.3, A = 0.23257463, center = 0.5, width = 0.96865225.

**rough_asperity_exponent**

`base+amp*maximum(x,0)**p-A*amp*exp(-abs(x)/ell)`

Parameters: p = 4, A = 0.26500518, ell = 0.40913028.

**hysteretic_detachment**

`base+amp*maximum(x,0)**1.5-A*amp*0.5*(1+tanh((x-xoff)/width))*(1-minimum(maximum(x,0),1))`

Parameters: A = 1.7107473, xoff = 0.5, width = 0.5.


## Applicability and limitations

- Piezo position is not true indentation; effective contact models are predictive surrogates, not certified elasticmoduli.
- No stem-cell response measurements are present in this retained package; no osteogenesis conclusion follows.
- Ramp sampling frequency is not resolved; progress is dimensionless and no relaxation time in seconds is inferred.

Schema showed initialretraction rows that are inside the declaredfirstfivecalibrationwindow, plus a few firstapproachrows. Late reserved retraction targets were not inspected.

## Reproduction

Run `python run.py` in this final package to verify hashes and reproduce every saved prediction. Use `python run.py --inputs new.csv --output predictions.csv --model reference` only with the declared inputs and units. Numerical prediction evaluation does not certify novelty or mechanism. Source anchors and reserved observations are separate from predictor inputs.

Source: https://zenodo.org/records/20281797. See source/units audit and prior-art records in research history.
