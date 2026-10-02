# Attempt 4

Inertia0.0002449 is within1% of one-parameter local recovery0.0002457, with a small negative trend coefficient. Test a distinct population-recruitment explanation: cross-component dispersion and the exactly-zero component fraction may identify transient concentration beyond the aggregate mean.

attempt_001_decay=0.0002784271; attempt_002_relaxation=0.0002456698; attempt_003_inertia=0.0002449329

Primary group-balanced error: 0.0002407902453857426. Previous incumbent: 0.00024493288968559414. Gain>1%: True. Worst-group MAE: 0.0005577339247108813.

Equation: e+b0*r+b1*v+b2*sd+b3*sd*z; e=current30frame population mean,v=2*(e-e_t-30frames),r=prior300frame mean-e,a=e-2*e_t-30+e_t-60,sd=across-neuron SD of current30frame means,z=fraction of exactly-zero current neuron means,V=ventralCA1,G=sourcegroup3. All trace terms author processed units; coefficients dimensionless except RBF response coefficients in trace units.

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
