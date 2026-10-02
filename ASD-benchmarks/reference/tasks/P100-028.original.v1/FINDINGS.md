# Calibrated microwave conversion-amplitude response to pump strength

The native HDF5 record combines measured microwave experiments with other numerical and visualization products. This task uses the 13-mode pure frequency-conversion experiment and its 51 pump settings. Every directed off-diagonal pair is retained; complete pump matrices are the validation units. Three fixed lower settings supply the same per-pair calibration to every model.

The development-selected six-term response control reaches 3.758×10⁻⁵ fsu reserved MAE, compared with 4.034×10⁻⁵ for first-order extrapolation and 6.691×10⁻⁵ for holding the last calibration. This is a modest calibrated forecasting improvement. Five restricted physical explanations—shared saturation, coherent rotation, detuning-dependent saturation, incoherent power mixing and pump-induced loss—did not improve development transfer.

Let r=(g−g_lo)/(g_hi−g_lo), and let L,H,N denote measured lower, higher and zero-pump response magnitudes. The reference combines L, H, (H−L)r, (H−L)r², N and frequency-bin separation times (H−L)r with six fitted global coefficients. This transparent predictor does not establish a unique physical mechanism.

The endpoint is the magnitude of native instrument response in full-scale units. It is not an independently normalized scattering coefficient. Phase, passivity, reciprocity and quantum fidelity are outside this task, and the source paper’s existing inverse-design results are disclosed as prior art.

## Experimental scope and evaluation

Predict conversion response above the two calibration pump strengths; each directedmodepair is calibrated at0,.13,.1402040816pumpunits. Whole strongerpumpmatrices are reserved, not selected edges.

Calibration: Native response magnitudes atthreefixedlow/zeropumpconditionsperdirectedmodepair. No highpumpoutcome or targetstandarddeviation is a predictor.

Validation unit: Completepumpstrengthmatrix; all156offdiagonaldirectedpairslinked. Oneinstrument/day; strengthlevels are not independent devices.

Report entirepumpmatrix errors and extrema; no independent-deviceconfidenceinterval.

Target: magnitude of native complex USB off-diagonal response (fsu; instrument full-scale units). Errors use fsu; instrument full-scale units. The selected reference is **flexible**. Selection was frozen before confirmation; diagnostic winners are not substituted afterward.

| Predictor | Unit |
|---|---|
| lo | fsu;lowpumpamplituderesponse |
| hi | fsu;secondcalibrationresponse |
| noise | fsu;zero-pumpresponse |
| r | dimensionless normalizedpumpincrement |
| g | fsu;pumpamplitudecontrol |
| glo | fsu;lowpumpcontrol |
| ghi | fsu;highcalibrationpumpcontrol |
| sep | integer frequency-bin separation;100kHzbins |


## Matched comparison

| Model | Development MAE | Reserved MAE | Reserved worst-group MAE |
|---|---:|---:|---:|
| flexible | 1.53321e-05 | 3.75775e-05 | 4.82525e-05 |
| hold_calibration | 2.69472e-05 | 6.69148e-05 | 7.79037e-05 |
| linear_increment | 1.64086e-05 | 4.03412e-05 | 5.13983e-05 |
| saturating_increment | 1.65034e-05 | 4.10959e-05 | 5.22937e-05 |
| coherent_rotation | 1.64722e-05 | 4.1091e-05 | 5.22994e-05 |
| detuning_saturation | 1.6549e-05 | 4.11822e-05 | 5.19933e-05 |
| incoherent_power_mixing | 1.70114e-05 | 3.90719e-05 | 4.91777e-05 |
| pump_induced_loss | 1.64472e-05 | 4.10921e-05 | 5.23002e-05 |


The primary error is mean group MAE. RMSE and signed bias are complementary; rows within a group do not establish independent replication. No accuracy percentage or industrial tolerance is invented.


## Executable equations and parameters

Each expression below uses the named inputs in the units table. `exp`, `log`, and `sqrt` have their conventional mathematical meanings. Coefficients are fitted on development data only; all calibration is declared above. The portable `rules.json` contains full precision and each model’s complete training scope.

**flexible**

`b0*lo+b1*hi+b2*(hi-lo)*r+b3*(hi-lo)*r**2+b4*noise+b5*sep*(hi-lo)*r`

Parameters: b0 = 1.1992482, b1 = -0.22762582, b2 = 0.42375977, b3 = 0.10965828, b4 = 0.097293448, b5 = 0.029495234.

**hold_calibration**

`hi`

Parameters: none.

**linear_increment**

`lo+(hi-lo)*r`

Parameters: none.

**saturating_increment**

`maximum(lo+(hi-lo)*r*(1+k)/(1+k*r),0)`

Parameters: k = 0.009944332.

**coherent_rotation**

`maximum(lo+(hi-lo)*(sin(k*g)-sin(k*glo))/(sin(k*ghi)-sin(k*glo)),0)`

Parameters: k = 3.4152271.

**detuning_saturation**

`maximum(lo+(hi-lo)*r*(1+k0+k1*sep)/(1+(k0+k1*sep)*r),0)`

Parameters: k0 = 1.350705e-16, k1 = 0.0087108042.

**incoherent_power_mixing**

`sqrt(maximum(lo**2+(hi**2-lo**2)*r,0))`

Parameters: none.

**pump_induced_loss**

`maximum(lo+(hi-lo)*(g*exp(-k*g**2)-glo*exp(-k*glo**2))/(ghi*exp(-k*ghi**2)-glo*exp(-k*glo**2)),0)`

Parameters: k = 2.0044305.


## Applicability and limitations

- Magnitude in native fsu is not a calibrated dimensionless scattering coefficient; no passivity, quantumfidelity or reciprocity claim is inferred.
- Only the purefrequencyconversion13mode experiment is targeted.31modeparametricgain andnumericalinverseproblemproducts remain context,notduplicateindependentobservations.
- Finaltenhigherstrengthsettings test within-sweepextrapolation; no hardwaretransfer.

Schema audit accidentally printed sourceUSBstandarddeviation arrays; measuredcomplexUSBtargets remained unprinted. Uncertainty arrays are excluded from predictors andselection.

## Reproduction

Run `python run.py` in this final package to verify hashes and reproduce every saved prediction. Use `python run.py --inputs new.csv --output predictions.csv --model reference` only with the declared inputs and units. Numerical prediction evaluation does not certify novelty or mechanism. Source anchors and reserved observations are separate from predictor inputs.

Source: https://zenodo.org/records/18938314. See source/units audit and prior-art records in research history.
