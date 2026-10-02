# Attempt 5

Image-size interaction fails to improve pigment/quenching MAE0.004883. Test a biologically distinct stress-regime explanation: salt and drought may change the NPQ-yield slope differently despite similar aggregate color. Add declared treatment and quenching-by-treatment terms, keeping whole plants held out and excluding ambiguous time/dose units. Reject universal stress-specific mechanisms if transfer does not improve.

attempt_001_quenching=0.005971382; attempt_002_recovery=0.005046485; attempt_003_pigment=0.004882579; attempt_004_morphology=0.004930112

Primary group-balanced error: 0.005016528400332869. Previous incumbent: 0.004882579262944402. Gain>1%: False. Worst-group MAE: 0.031049316278457233.

Equation: sigmoid(b0+b1*r+b2*q+b3*NGRDI+b4*tiny+b5*salt+b6*drought+b7*highstress+b8*q*salt+b9*q*drought); r=Rfd/(1+abs(Rfd)), q=asinh(NPQ), size=ln(1+max(AREA_MM,0))/10

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
