# Attempt 2

Tonic relaxation0.8367uS is worse than persistence0.8210, while unit drift badly overshoots. Test damped causal drift jointly with tonic relaxation: a short-term trend may need a small gain rather than a full30s extrapolation.

attempt_001_relaxation=0.8367453

Primary group-balanced error: 0.859898917944228. Previous incumbent: 0.8210218422084464. Gain>1%: False. Worst-group MAE: 4.956825819353019.

Equation: e+b0*v+b1*r; e=current5s EDA mean(uS), v=3*(e-e_t-10s),r=prior120s mean-e,A=prior10s acceleration magnitude SD(g),dT=T-T_t-30s(degreeC). v/r coefficients dimensionless,A coefficientuS/g,dT coefficientuS/degreeC,interaction coefficient1/g.

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
