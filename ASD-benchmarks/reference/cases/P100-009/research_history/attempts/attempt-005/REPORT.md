# Attempt 5

Asymmetric dilation/constriction1.2348px also fails. Test whether the missing ingredient is local acceleration rather than direction or locomotion: add the causal second difference while retaining equilibrium relaxation and damped slope. If unsuccessful, persistence remains the justified reference.

attempt_001_relaxation=1.213808; attempt_002_inertia=1.222108; attempt_003_arousal=1.303822; attempt_004_asymmetry=1.234848

Primary group-balanced error: 1.210643454299523. Previous incumbent: 1.2138077270855026. Gain>1%: False. Worst-group MAE: 1.6084884843622311.

Equation: max(0,p+b0*r+b1*v+b2*a); p=current quarter-second radius(px), r=preceding5s mean-p, v=2*(p-p_t-0.5s), a=p-2*p_t-0.5s+p_t-1s, u=ln(1+speed/(1cm/s)),du=u-u_t-1s. Coefficients of pixel features dimensionless; u/du coefficients px.

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
