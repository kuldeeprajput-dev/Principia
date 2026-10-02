# Attempt 2

Reciprocal quenching slightly improves the flexible control (0.005971 vs0.006065). Test a competing fluorescence-recovery mechanism using bounded Rfd/(1+abs(Rfd)) and signed asinh(NPQ), with cultivar offset. This asks whether recovery dynamics provide information beyond steady dissipation; shared source fluorescence calibration prevents treating it as independent molecular validation.

attempt_001_quenching=0.005971382

Primary group-balanced error: 0.005046485387240412. Previous incumbent: 0.005971382448357383. Gain>1%: True. Worst-group MAE: 0.03327525650142663.

Equation: sigmoid(b0+b1*Rfd/(1+abs(Rfd))+b2*asinh(NPQ)+b3*tiny); r=Rfd/(1+abs(Rfd)), q=asinh(NPQ), size=ln(1+max(AREA_MM,0))/10

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
