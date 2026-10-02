# attempt-006

# Preregistered development attempt

Recorded UTC: 2026-10-02T02:41:19.463229+00:00

Parent evidence: 005MAE3.996079/worst4.599113 worse0043.923358/4.493416; one no-gain.

Removing six-month history005 worsens mean and tail, so long memory remains useful. Test a robust square-root response to distinguish rare administrativereportingbursts from stablecountnoise; retain everymonth/cohort in physical-countscore anddo not claimdefectrobustness.

Equation: `count_hat=max(0,a+b1sqrt(lag1)+b3sqrt(lag3)+b6sqrt(lag6))²;robustfit`. Confirmation remains unread; inspect development residuals and whole-group errors as falsifiers.


Development primary error: 3.937112153. Worst-group error: 4.483109599. 6groups/2604observations. Model and fold states contain all coefficients, rank, training groups and training-row hashes. No confirmation feedback used.
