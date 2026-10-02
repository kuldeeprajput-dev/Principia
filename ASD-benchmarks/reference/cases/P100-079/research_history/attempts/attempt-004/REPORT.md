# Attempt 4

The fast compartment disappears and two-decay fitting reproduces a single exponential. Test whether pre-dose drift accounts for individual deviations while the post-dose response remains one-component.

attempt_001_bateman=0.02528724; attempt_002_relative_decay=0.02744227; attempt_003_two_decay=0.0247156

Primary group-balanced error: 0.029255904965527012. Previous incumbent: 0.024515140600000002. Gain>1%: False. Worst-group MAE: 0.057789492436507016.

Equation: yhat=max(0,baseline+A*exp(-hours/tau)+b*baseline_change*exp(-hours/24))

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
