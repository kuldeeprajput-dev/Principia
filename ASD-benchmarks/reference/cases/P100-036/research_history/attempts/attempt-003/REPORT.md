# Attempt 3

Recovery plus quenching improves plant-held MAE to0.005047, stronger than the reciprocal coordinate0.005971. Test whether leaf pigment/color modifies that fluorescence relation by adding NGRDI and a quenching-by-color term. This distinguishes biochemical stress-proxy coupling from merely cultivar-specific offsets, while retaining the shared-assay interpretation limit.

attempt_001_quenching=0.005971382; attempt_002_recovery=0.005046485

Primary group-balanced error: 0.004882579262944402. Previous incumbent: 0.005046485387240412. Gain>1%: True. Worst-group MAE: 0.03242346073113145.

Equation: sigmoid(b0+b1*r+b2*q+b3*NGRDI+b4*q*NGRDI+b5*tiny); r=Rfd/(1+abs(Rfd)), q=asinh(NPQ), size=ln(1+max(AREA_MM,0))/10

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
