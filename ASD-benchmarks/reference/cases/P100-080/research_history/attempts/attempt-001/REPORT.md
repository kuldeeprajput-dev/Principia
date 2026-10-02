# Attempt 1

Persistence0.8210uS outperforms velocity1.4699 and flexible0.8902. Test a tonic relaxation mechanism: departure from the causal120s EDA mean should weakly pull the30s future state back toward recent tonic level.

Initial post-baseline hypothesis

Primary group-balanced error: 0.8367452862817596. Previous incumbent: 0.8210218422084464. Gain>1%: False. Worst-group MAE: 4.8231560568155665.

Equation: e+b0*r; e=current5s EDA mean(uS), v=3*(e-e_t-10s),r=prior120s mean-e,A=prior10s acceleration magnitude SD(g),dT=T-T_t-30s(degreeC). v/r coefficients dimensionless,A coefficientuS/g,dT coefficientuS/degreeC,interaction coefficient1/g.

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
