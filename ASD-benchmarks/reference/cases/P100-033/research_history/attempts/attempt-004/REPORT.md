# Attempt 4

Quality-dependent shrinkage improves development to11.27bpm but may conceal recoverable waveform information. Test a competing physical artifact explanation: known motion changes FFT-versus-ACF weighting, with a contact-specific rate offset; reject if no advantage over shrinkage.

attempt_001_alias=34.25331; attempt_002_fusion=30.50684; attempt_003_shrinkage=11.2705

Primary group-balanced error: 28.590090076740523. Previous incumbent: 11.270495874562176. Gain>1%: False. Worst-group MAE: 53.489499386774604.

Equation: clip(w*F+(1-w)*A+b4*ear; w=sigmoid(b0+b1*(Q-.3)+b2*D+b3*motion),30,240) bpm; F=FFT rate,A=ACF rate,H=half-rate candidate,Q=spectral concentration,S=half-frequency relative power,D=abs(F-A)/60

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
