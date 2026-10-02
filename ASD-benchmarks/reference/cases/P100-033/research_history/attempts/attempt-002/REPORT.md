# Attempt 2

Half-frequency gating worsened development error to34.25bpm. Test a competing explanation: pulse spectral and autocorrelation estimators have complementary failures, with weights depending on concentration and disagreement; reject harmonic-only attribution if fusion dominates.

attempt_001_alias=34.25331

Primary group-balanced error: 30.506836577095225. Previous incumbent: 11.741575415810953. Gain>1%: False. Worst-group MAE: 53.17029558014108.

Equation: clip(w*F+(1-w)*A; w=sigmoid(b0+b1*(Q-.3)+b2*D),30,240) bpm; F=FFT rate,A=ACF rate,H=half-rate candidate,Q=spectral concentration,S=half-frequency relative power,D=abs(F-A)/60

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
