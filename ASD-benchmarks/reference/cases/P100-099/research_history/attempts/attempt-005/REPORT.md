# Attempt 5

Dispersion/zero-component interaction improves development to0.0002408, but this could reflect regional recording/processing differences. Test a competing region-dependent recovery/inertia equation using known dorsal/ventral identity without dispersion; do not interpret region coefficients as causal physiology.

attempt_001_decay=0.0002784271; attempt_002_relaxation=0.0002456698; attempt_003_inertia=0.0002449329; attempt_004_heterogeneity=0.0002407902

Primary group-balanced error: 0.0002447443148579463. Previous incumbent: 0.0002407902453857426. Gain>1%: False. Worst-group MAE: 0.0005705458723678173.

Equation: e+b0*r+b1*v+b2*r*V+b3*v*V; e=current30frame population mean,v=2*(e-e_t-30frames),r=prior300frame mean-e,a=e-2*e_t-30+e_t-60,sd=across-neuron SD of current30frame means,z=fraction of exactly-zero current neuron means,V=ventralCA1,G=sourcegroup3. All trace terms author processed units; coefficients dimensionless except RBF response coefficients in trace units.

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
