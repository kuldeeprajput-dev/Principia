# Attempt 2

Uniform effective decay0.0002784 does not match flexible0.0002586 and cannot identify a calcium lifetime. Test local set-point recovery instead: departures from the preceding300-frame mean may relax toward the session state without assuming decay to zero.

attempt_001_decay=0.0002784271

Primary group-balanced error: 0.0002456698160697357. Previous incumbent: 0.0002585612117811051. Gain>1%: True. Worst-group MAE: 0.0005712857337912394.

Equation: e+b0*r; e=current30frame population mean,v=2*(e-e_t-30frames),r=prior300frame mean-e,a=e-2*e_t-30+e_t-60,sd=across-neuron SD of current30frame means,z=fraction of exactly-zero current neuron means,V=ventralCA1,G=sourcegroup3. All trace terms author processed units; coefficients dimensionless except RBF response coefficients in trace units.

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
