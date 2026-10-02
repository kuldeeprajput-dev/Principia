# Attempt 3

Tail recruitment3821.7units is competitive but worse than multiplicative3510.7. Test a location-scale transformation: line-specific shift plus width-dependent quantile stretching separates uniform brightness shifts from distribution broadening using only paired uninduced width.

attempt_001_multiplicative=3510.698; attempt_002_recruitment=3821.699

Primary group-balanced error: 3510.1931635743467. Previous incumbent: 3510.697536698588. Gain>1%: False. Worst-group MAE: 3846.8752309574697.

Equation: c+delta_line+s_line*control_width*(q-.5); c=paired uninduced AF488 quantile(native units),q=quantile probability,line coefficient order MFSD5/WT SLC30A8/mutant; width=control q.9-q.1. Shift coefficients and K are native fluorescence units; multiplicative/location-scale coefficients dimensionless. Profile threshold/K is additional fitted state.

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
