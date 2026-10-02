# Attempt 5

Pre-dose drift adds error and a fast compartment is unidentifiable. Test an asymmetric log-time release pulse as an alternative to exponential compartment kinetics.

attempt_001_bateman=0.02528724; attempt_002_relative_decay=0.02744227; attempt_003_two_decay=0.0247156; attempt_004_baseline_drift=0.0292559

Primary group-balanced error: 0.02460145270267817. Previous incumbent: 0.024515140600000002. Gain>1%: False. Worst-group MAE: 0.04430422426047086.

Equation: yhat=max(0,baseline+A*exp(-.5*(log(hours/tpeak)/sigma)^2))

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
