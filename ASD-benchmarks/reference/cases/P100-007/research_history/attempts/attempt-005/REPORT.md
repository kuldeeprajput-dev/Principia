# Attempt 5

Stance-gated local dynamics128.10N fail to improve periodic copy. Synthesize the two justified signals: previous-cycle phase plus local velocity and opposite-plate load transfer, testing whether bilateral coupling repairs cycle mismatch.

attempt_001_damped=130.9386; attempt_002_phase=100.7851; attempt_003_bilateral=123.4378; attempt_004_stance=128.1003

Primary group-balanced error: 101.22723607782588. Previous incumbent: 86.91507844976033. Gain>1%: False. Worst-group MAE: 101.75163574391384.

Equation: F+b0*(C-F)+b1*v+b2*vO; F=current plate1 force(N), v=2*(F-F_t-50ms), a=F-2*F_t-50ms+F_t-100ms, C=past-cycle target phase force, vO=2*(opposite-opposite_t-50ms). Coefficients dimensionless except stated flexible response coefficients N.

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
