# Attempt 2

Multiplicative response3510.7units strongly improves shift8722.6. A rival explanation is subpopulation recruitment rather than uniform scaling: let genotype-specific induction rise sigmoidally across source quantiles, with the recruitment threshold chosen only within training blocks.

attempt_001_multiplicative=3510.698

Primary group-balanced error: 3821.6993050652363. Previous incumbent: 3510.697536698588. Gain>1%: False. Worst-group MAE: 3829.7666025945514.

Equation: c+delta_line*sigmoid((q-q0)/.1); c=paired uninduced AF488 quantile(native units),q=quantile probability,line coefficient order MFSD5/WT SLC30A8/mutant; width=control q.9-q.1. Shift coefficients and K are native fluorescence units; multiplicative/location-scale coefficients dimensionless. Profile threshold/K is additional fitted state.

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
