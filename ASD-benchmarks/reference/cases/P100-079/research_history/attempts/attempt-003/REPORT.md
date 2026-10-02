# Attempt 3

Baseline-proportional amplitude fails. Test separate fast and slow washout components while preserving positivity; rank deficiency would reject mechanistic compartment identification.

attempt_001_bateman=0.02528724; attempt_002_relative_decay=0.02744227

Primary group-balanced error: 0.02471559513232458. Previous incumbent: 0.024515140600000002. Gain>1%: False. Worst-group MAE: 0.03975952546519421.

Equation: yhat=max(0,baseline+Afast*exp(-hours/tfast)+Aslow*exp(-hours/tslow))

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
