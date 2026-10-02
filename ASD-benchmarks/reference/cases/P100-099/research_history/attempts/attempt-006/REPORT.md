# Attempt 6

Region-specific recovery0.0002447 loses to heterogeneity0.0002408 and does not explain the gain. Test a final mechanistic rival: processed events may relax asymmetrically during rising versus declining population activity. Keep the local set point and replace the common trend with separate positive/negative gains.

attempt_001_decay=0.0002784271; attempt_002_relaxation=0.0002456698; attempt_003_inertia=0.0002449329; attempt_004_heterogeneity=0.0002407902; attempt_005_region=0.0002447443

Primary group-balanced error: 0.00024038328845030384. Previous incumbent: 0.0002407902453857426. Gain>1%: False. Worst-group MAE: 0.0005602514420717622.

Equation: e+b0*r+b1*max(v,0)+b2*min(v,0); e=current30frame population mean,v=2*(e-e_t-30frames),r=prior300frame mean-e,a=e-2*e_t-30+e_t-60,sd=across-neuron SD of current30frame means,z=fraction of exactly-zero current neuron means,V=ventralCA1,G=sourcegroup3. All trace terms author processed units; coefficients dimensionless except RBF response coefficients in trace units.

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
