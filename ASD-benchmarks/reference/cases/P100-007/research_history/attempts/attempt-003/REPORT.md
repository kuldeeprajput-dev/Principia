# Attempt 3

Phase plus local slope100.79N remains worse than phase-copy. Test a distinct load-transfer constraint: contralateral force velocity may anticipate the target plate loading beyond its own velocity/curvature, while allowing signed platform forces.

attempt_001_damped=130.9386; attempt_002_phase=100.7851

Primary group-balanced error: 123.43777727268997. Previous incumbent: 86.91507844976033. Gain>1%: False. Worst-group MAE: 139.54989190007032.

Equation: F+b0*v+b1*a+b2*vO; F=current plate1 force(N), v=2*(F-F_t-50ms), a=F-2*F_t-50ms+F_t-100ms, C=past-cycle target phase force, vO=2*(opposite-opposite_t-50ms). Coefficients dimensionless except stated flexible response coefficients N.

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
