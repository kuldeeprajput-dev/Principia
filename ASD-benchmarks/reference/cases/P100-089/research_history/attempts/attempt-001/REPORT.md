# Attempt 1

Expected-value logits improve unconditional means but lose to flexible predictions. Test nonlinear utility and probability weighting as a compact competing behavioral account.

Initial post-baseline hypothesis

Primary group-balanced error: 0.17246173012850086. Previous incumbent: 0.1273648253813338. Gain>1%: False. Worst-group MAE: 0.4494413124947634.

Equation: p_hat=sigmoid(beta*(w(p)*(reward/2)^alpha-1)+bias); w(p)=p^gamma/(p^gamma+(1-p)^gamma)^(1/gamma)

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
