# Attempt 6

Removing the genotype reserve offset improves whole-animal development error. Test whether the earlier0.4mM measurement adds identifiable pool-size information beyond the0.75mM anchor, without assigning genotype-specific capacity.

attempt_001_genotype_hill=38.45277; attempt_002_local_hill=710.6454; attempt_003_two_pool=41.33442; attempt_004_reserve=16.39608; attempt_005_reserve_pooled=15.62452

Primary group-balanced error: 14.769448401873257. Previous incumbent: 15.624515432869753. Gain>1%: True. Worst-group MAE: 27.058604488703878.

Equation: Ihat=I(.75)+max(A+B*I(.4)-lambda*I(.75),0)*(1-exp(-(Ca-.75)/K)); test information from second calibration anchor.

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
