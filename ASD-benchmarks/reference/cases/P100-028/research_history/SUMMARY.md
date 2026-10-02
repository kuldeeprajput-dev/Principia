# P100-028 exploration summary

The native HDF5 record combines measured microwave experiments with other numerical and visualization products. This task uses the 13-mode pure frequency-conversion experiment and its 51 pump settings. Every directed off-diagonal pair is retained; complete pump matrices are the validation units. Three fixed lower settings supply the same per-pair calibration to every model.

The development-selected six-term response control reaches 3.758×10⁻⁵ fsu reserved MAE, compared with 4.034×10⁻⁵ for first-order extrapolation and 6.691×10⁻⁵ for holding the last calibration. This is a modest calibrated forecasting improvement. Five restricted physical explanations—shared saturation, coherent rotation, detuning-dependent saturation, incoherent power mixing and pump-induced loss—did not improve development transfer.

Let r=(g−g_lo)/(g_hi−g_lo), and let L,H,N denote measured lower, higher and zero-pump response magnitudes. The reference combines L, H, (H−L)r, (H−L)r², N and frequency-bin separation times (H−L)r with six fitted global coefficients. This transparent predictor does not establish a unique physical mechanism.

The endpoint is the magnitude of native instrument response in full-scale units. It is not an independently normalized scattering coefficient. Phase, passivity, reciprocity and quantum fidelity are outside this task, and the source paper’s existing inverse-design results are disclosed as prior art.

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


## Attempt history

**attempt-001 — saturating_increment**: Attempt1: a shared saturating conversion response bends linearpump extrapolation while exactlymatching both calibrationlevels. Test whether a single effectivecoupling scale transfers across themodepairs. Development MAE=1.65034e-05; worst group=3.01229e-05; fitted parameters=1.

**attempt-002 — coherent_rotation**: Development evidence available before this fit: saturating_increment: MAE 1.65034e-05, worst group 3.01229e-05.

Shared monotone saturation failed to improve the first-ordercontrol. Test coherentconversionrotation, where amplitude follows a sine of couplingstrength rather than a dissipativerationalresponse. Development MAE=1.64722e-05; worst group=3.01677e-05; fitted parameters=1.

**attempt-003 — detuning_saturation**: Development evidence available before this fit: saturating_increment: MAE 1.65034e-05, worst group 3.01229e-05; coherent_rotation: MAE 1.64722e-05, worst group 3.01677e-05.

Test whether conversionpath detuning, represented only byknownfrequency-bin separation, changes saturation. This challenges the sharedcoupling assumption without adding pair-specific fittedstates. Development MAE=1.6549e-05; worst group=3.03777e-05; fitted parameters=2.

**attempt-004 — incoherent_power_mixing**: Development evidence available before this fit: coherent_rotation: MAE 1.64722e-05, worst group 3.01677e-05; detuning_saturation: MAE 1.6549e-05, worst group 3.03777e-05.

Test incoherentpower rather than amplitude interpolation. Unknownrelativephases can make a power-addition law behave differently from a coherentlinear-amplitude extrapolation; completepumpmatrices provide thefalsifier. Development MAE=1.70114e-05; worst group=2.91966e-05; fitted parameters=0.

**attempt-005 — pump_induced_loss**: Development evidence available before this fit: detuning_saturation: MAE 1.6549e-05, worst group 3.03777e-05; incoherent_power_mixing: MAE 1.70114e-05, worst group 2.91966e-05.

Test pump-dependentattenuation/depletion: increasingdrive introduces a quadraticstrength loss envelope on top of linearcoupling. A transferableloss coefficient would differ from a pureunitaryrotation interpretation. Development MAE=1.64472e-05; worst group=3.01639e-05; fitted parameters=1.

All substantive attempts and failures are retained. See FREEZE.json and CONFIRMATION_RECEIPT.json for chronology and exact evidence binding.
