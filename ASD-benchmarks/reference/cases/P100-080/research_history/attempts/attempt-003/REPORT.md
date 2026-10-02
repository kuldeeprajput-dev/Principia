# Attempt 3

Damped drift0.8599uS still loses to persistence. Test an independent sweat-driver hypothesis: preceding accelerometer activity may predict subsequent EDA increment after controlling local drift and tonic state; any coefficient remains protocol-specific rather than a sweat secretion constant.

attempt_001_relaxation=0.8367453; attempt_002_damped_drift=0.8598989

Primary group-balanced error: 0.8732695345138582. Previous incumbent: 0.8210218422084464. Gain>1%: False. Worst-group MAE: 4.944581574089797.

Equation: e+b0*v+b1*r+b2*A; e=current5s EDA mean(uS), v=3*(e-e_t-10s),r=prior120s mean-e,A=prior10s acceleration magnitude SD(g),dT=T-T_t-30s(degreeC). v/r coefficients dimensionless,A coefficientuS/g,dT coefficientuS/degreeC,interaction coefficient1/g.

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
