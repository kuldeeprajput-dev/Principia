# Attempt 6

Removing stiffness improves whole-donor MAE from 0.919 to 0.884. Continue by testing whether baseline VCAM1 modifies the HSS response: include (c-5)*HSS alongside coupled mechanics. This asks whether apparent donor heterogeneity can be explained using the one permitted baseline assay rather than hidden donor-specific coefficients. With only two training donors per fold, rank and transfer are decisive falsifiers.

attempt_001_saturation=0.9473969; attempt_002_synergy=1.090535; attempt_003_mechanical_only=0.9789567; attempt_004_threshold=1.033434; attempt_005_shear_only=0.8840575

Primary group-balanced error: 1.4301191942998202. Previous incumbent: 0.8840575403221771. Gain>1%: False. Worst-group MAE: 1.5629457446030348.

Equation: y_hat=max(0,c+b1*x+b2*s+b3*x*s+b4*(c-5)*s), x=ln(E/30)

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
