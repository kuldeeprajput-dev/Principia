# Attempt 5

Additive finite reserve beats the flexible model by about3.8percent and genotype reserve offset is small. Ablate the genotype term to test whether calibration already accounts for genotype-associated amplitude variation.

attempt_001_genotype_hill=38.45277; attempt_002_local_hill=710.6454; attempt_003_two_pool=41.33442; attempt_004_reserve=16.39608

Primary group-balanced error: 15.624515432869753. Previous incumbent: 16.396078081201296. Gain>1%: True. Worst-group MAE: 31.8377748354692.

Equation: Ihat=I(.75)+max(A-lambda*I(.75),0)*(1-exp(-(Ca-.75)/K)); common reserve across both genotypes.

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
