# Attempt 4

Activity-driven increment0.8733uS degrades held-person development. Test the competing sensor/thermoregulation explanation: preceding temperature change may explain conductance drift after conditioning on its own trend and tonic level; avoid causal sweat-rate attribution.

attempt_001_relaxation=0.8367453; attempt_002_damped_drift=0.8598989; attempt_003_activity=0.8732695

Primary group-balanced error: 0.8601812123717242. Previous incumbent: 0.8210218422084464. Gain>1%: False. Worst-group MAE: 4.956826644559799.

Equation: e+b0*v+b1*r+b2*dT; e=current5s EDA mean(uS), v=3*(e-e_t-10s),r=prior120s mean-e,A=prior10s acceleration magnitude SD(g),dT=T-T_t-30s(degreeC). v/r coefficients dimensionless,A coefficientuS/g,dT coefficientuS/degreeC,interaction coefficient1/g.

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
