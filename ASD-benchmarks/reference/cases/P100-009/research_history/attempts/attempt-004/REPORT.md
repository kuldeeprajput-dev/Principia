# Attempt 4

Movement coupling1.3038px worsens transfer, so it cannot be interpreted as a portable arousal law here. Test asymmetric pupil dynamics: dilation and constriction slopes may have different damping while sharing a local equilibrium.

attempt_001_relaxation=1.213808; attempt_002_inertia=1.222108; attempt_003_arousal=1.303822

Primary group-balanced error: 1.2348477833782285. Previous incumbent: 1.2138077270855026. Gain>1%: False. Worst-group MAE: 1.642519983231828.

Equation: max(0,p+b0*r+b1*max(v,0)+b2*min(v,0)); p=current quarter-second radius(px), r=preceding5s mean-p, v=2*(p-p_t-0.5s), a=p-2*p_t-0.5s+p_t-1s, u=ln(1+speed/(1cm/s)),du=u-u_t-1s. Coefficients of pixel features dimensionless; u/du coefficients px.

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
