# Attempt 6

Discrete harmonic correction32.53bpm failed; the added balanced median control11.66 confirms most shrinkage performance is a population prior. A distinct remaining hypothesis is that agreement between Fourier and ACF identifies recoverable windows: shrink their consensus when disagreement is high. Test before final stopping.

attempt_001_alias=34.25331; attempt_002_fusion=30.50684; attempt_003_shrinkage=11.2705; attempt_004_motion_fusion=28.59009; attempt_005_agreement_gate=32.52944

Primary group-balanced error: 11.427280079973588. Previous incumbent: 11.270495874562176. Gain>1%: False. Worst-group MAE: 31.861184911356183.

Equation: clip(w*(F+A)/2+(1-w)*mu; w=sigmoid(b0+b1*(Q-.3)-b2*D), mu=b3,30,240) bpm; F=FFT rate,A=ACF rate,H=half-rate candidate,Q=spectral concentration,S=half-frequency relative power,D=abs(F-A)/60

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
