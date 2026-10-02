# Calibrated microwave conversion-amplitude response to pump strength

The native HDF 5 record combines measured microwave experiments with other numerical and visualization products. This task uses the 13-mode pure frequency-conversion experiment and its 51 pump settings. Every directed off-diagonal pair is retained; complete pump matrices are the validation units. Three fixed lower settings supply the same per-pair calibration to every model.

The development-selected six-term response control reaches $3.758\times 10^{-5}$ fsu reserved MAE, compared with $4.034\times 10^{-5}$ for first-order extrapolation and $6.691\times 10^{-5}$ for holding the last calibration. This is a modest calibrated forecasting improvement. Five restricted physical explanations - shared saturation, coherent rotation, detuning-dependent saturation, incoherent power mixing and pump-induced loss - did not improve development transfer.

Let r=(g−g_lo)/(g_hi−g_lo), and let L, H, N denote measured lower, higher and zero-pump response magnitudes. The reference combines L, H, (H−L)r, (H−L)r², N and frequency-bin separation times (H−L)r with six fitted global coefficients. This transparent predictor does not establish a unique physical mechanism.

The endpoint is the magnitude of native instrument response in full-scale units. It is not an independently normalized scattering coefficient. Phase, passivity, reciprocity and quantum fidelity are outside this task, and the source paper’s existing inverse-design results are disclosed as prior art.

## Experimental scope and evaluation

Predict conversion response above the two calibration pump strengths; each directed mode pair is calibrated at 0,.13,.1402040816 pump units. Whole stronger pump matrices are reserved, not selected edges.

Calibration: Native response magnitudes at three fixed low/zero-pump conditions per directed mode pair. No high-pump outcome or target standard-deviation is a predictor.

Validation unit: Complete pump-strength matrix; all 156 off-diagonal directed pairs linked. One instrument/day; strength levels are not independent devices.

Report entire pump matrix errors and extrema; no independent-device confidence interval.

Target: magnitude of native complex USB off-diagonal response (fsu; instrument full-scale units). Errors use fsu; instrument full-scale units. The selected reference is **flexible**. Selection was frozen before confirmation; diagnostic winners are not substituted afterward.

| Predictor | Unit |
|---|---|
| lo | fsu; low-pump amplitude response |
| hi | fsu; second calibration response |
| noise | fsu; zero-pump response |
| r | dimensionless normalized pump increment |
| g | fsu; pump amplitude control |
| glo | fsu; low pump control |
| ghi | fsu; high calibration pump control |
| sep | integer frequency-bin separation; 100 kHz bins |


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


## Selected equation and coefficients

$$
\widehat A=b_0L+b_1H+(H-L)(b_2r+b_3r^2+b_5sr)+b_4N_0
$$

L and H are the two permitted calibrated magnitudes; r is normalized pump increment, s is mode separation, and N0 is the zero-pump magnitude (the implementation calls this input noise). These are instrument full-scale units, not a quantum-noise calibration.

| Coefficient | Frozen value |
|---|---:|
| b0 | 1.19924824 |
| b1 | -0.227625824 |
| b2 | 0.423759771 |
| b3 | 0.109658285 |
| b4 | 0.0972934482 |
| b5 | 0.0294952339 |

All comparator expressions, numerical guards and full-precision values remain in EQUATIONS.md, rules.json and run.py.

## Applicability and limitations

- Magnitude in native fsu is not a calibrated dimensionless scattering coefficient; no passivity, quantum fidelity or reciprocity claim is inferred.
- Only the pure frequency conversion 13 mode experiment is targeted.31 mode parametric gain and numerical inverse-problem products remain context, not duplicate independent observations.
- Final ten higher-strength settings test within-sweep extrapolation; no hardware transfer.

Schema audit accidentally printed source USB standard-deviation arrays; measured complex USB targets remained unprinted. Uncertainty arrays are excluded from predictors and selection.

## Reproduction

Run `python run.py` in this final package to verify hashes and reproduce every saved prediction. Use `python run.py --inputs new.csv --output predictions.csv --model reference` only with the declared inputs and units. Numerical prediction evaluation does not certify novelty or mechanism. Source anchors and reserved observations are separate from predictor inputs.

Source: https://zenodo.org/records/18938314. See source/units audit and prior-art records in research history.
