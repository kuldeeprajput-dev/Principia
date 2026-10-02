# Attempt 4

Smooth additive, saturating and coupled responses fail donor transfer. Test a regime transition between the 30-kPa condition and the two stiffer conditions, with a separate shear-dependent step. The fixed 200-kPa boundary reflects the measured design, not an inferred biological critical stiffness; challenge it against calibration and report the lack of resolution between 30 and 200 kPa.

attempt_001_saturation=0.9473969; attempt_002_synergy=1.090535; attempt_003_mechanical_only=0.9789567

Primary group-balanced error: 1.0334340523834242. Previous incumbent: 0.9191598813389589. Gain>1%: False. Worst-group MAE: 1.1479603386624202.

Equation: y_hat=max(0,c+b1*I(E>=200)+b2*s+b3*s*I(E>=200))

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
