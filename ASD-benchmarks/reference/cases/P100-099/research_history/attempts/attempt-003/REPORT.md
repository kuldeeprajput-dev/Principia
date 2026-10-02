# Attempt 3

Local set-point recovery improves group MAE to0.0002457 versus flexible0.0002586; alpha0.795 indicates strong return to recent state. Test whether short-term trace momentum adds independently to recovery instead of mistaking a transient event for a persistent level.

attempt_001_decay=0.0002784271; attempt_002_relaxation=0.0002456698

Primary group-balanced error: 0.00024493288968559414. Previous incumbent: 0.0002456698160697357. Gain>1%: False. Worst-group MAE: 0.0005710575980456187.

Equation: e+b0*r+b1*v; e=current30frame population mean,v=2*(e-e_t-30frames),r=prior300frame mean-e,a=e-2*e_t-30+e_t-60,sd=across-neuron SD of current30frame means,z=fraction of exactly-zero current neuron means,V=ventralCA1,G=sourcegroup3. All trace terms author processed units; coefficients dimensionless except RBF response coefficients in trace units.

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
