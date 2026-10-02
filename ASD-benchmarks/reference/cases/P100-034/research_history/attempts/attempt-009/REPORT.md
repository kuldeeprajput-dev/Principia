# Attempt 9

Fixing unit depletion further improves error and removes a coefficient. Test whether genotype still changes the incremental calcium recruitment scale after both calibration anchors account for amplitude; this challenges apparent genotype-invariant transfer.

attempt_001_genotype_hill=38.45277; attempt_002_local_hill=710.6454; attempt_003_two_pool=41.33442; attempt_004_reserve=16.39608; attempt_005_reserve_pooled=15.62452; attempt_006_reserve_low04=14.76945; attempt_007_reserve_rational=14.52533; attempt_008_reserve_conserved=13.65332

Primary group-balanced error: 14.28940869620984. Previous incumbent: 13.653319600314854. Gain>1%: False. Worst-group MAE: 27.247040871181767.

Equation: Ihat=I(.75)+max(A+B*I(.4)-I(.75),0)*(Ca-.75)/(K*exp(bg*mutant)+Ca-.75)

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
