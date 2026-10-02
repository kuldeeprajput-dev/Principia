# Attempt 5

Motion/contact fusion remains28.59bpm. Challenge shrinkage with a discrete physiological harmonic correction: accept a half-frequency candidate only when sufficient half-frequency power exists and it is closer to the independent autocorrelation estimate; train only the finite threshold grid.

attempt_001_alias=34.25331; attempt_002_fusion=30.50684; attempt_003_shrinkage=11.2705; attempt_004_motion_fusion=28.59009

Primary group-balanced error: 32.52944448965567. Previous incumbent: 11.270495874562176. Gain>1%: False. Worst-group MAE: 55.941141764322914.

Equation: clip(C=H if S>=threshold else F; select C only when abs(C-A)<abs(F-A),30,240) bpm; F=FFT rate,A=ACF rate,H=half-rate candidate,Q=spectral concentration,S=half-frequency relative power,D=abs(F-A)/60

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
