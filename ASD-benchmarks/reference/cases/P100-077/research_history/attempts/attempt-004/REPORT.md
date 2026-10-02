# Attempt 4

A common competent fraction (0.09967) fails to improve the odds-ratio incumbent0.07938. Test whether delivery-dose-dependent competence rather than constant association explains the residual: alpha(dose)=sigmoid(b0+b1*ln dose). This adds a physically motivated dose modulation, challenged by only three doses and complete held replicate blocks.

attempt_001_competence=0.1008181; attempt_002_odds_ratio=0.07938147; attempt_003_common_fraction=0.09966647

Primary group-balanced error: 0.11430573439877537. Previous incumbent: 0.07938146560427811. Gain>1%: False. Worst-group MAE: 0.11636208497615552.

Equation: j=p*q+sigmoid(b0+b1*ln(dose))*(min(p,q)-p*q); y_hat=100*j, L=max(0,p+q-1), U=min(p,q)

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
