# Attempt 1

Simple exponential loss does not improve baseline persistence. Test finite uptake followed by washout through a Bateman difference of exponentials.

Initial post-baseline hypothesis

Primary group-balanced error: 0.02528723873298807. Previous incumbent: 0.024515140600000002. Gain>1%: False. Worst-group MAE: 0.04441671918247995.

Equation: yhat=max(0,baseline+A*(exp(-hours/tau_decay)-exp(-hours/tau_rise)))

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
