# Attempt 4

Pigment coupling improves plant-held MAE to0.004883. Challenge whether image size, a developmental/geometry proxy, explains the residual through a size-by-quenching interaction. Use only ln(1+AREA_MM) in its source scale; because area units and age labels are uncertain, this is a geometric proxy test and cannot identify heat flux or a time-development law.

attempt_001_quenching=0.005971382; attempt_002_recovery=0.005046485; attempt_003_pigment=0.004882579

Primary group-balanced error: 0.004930111881433809. Previous incumbent: 0.004882579262944402. Gain>1%: False. Worst-group MAE: 0.03242120163341581.

Equation: sigmoid(b0+b1*r+b2*q+b3*NGRDI+b4*size+b5*size*q+b6*tiny); r=Rfd/(1+abs(Rfd)), q=asinh(NPQ), size=ln(1+max(AREA_MM,0))/10

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
