# attempt-011

# Preregistered development attempt

Recorded UTC: 2026-10-02T02:55:38.355013+00:00

Parent evidence: attempt010

Attempt010 improves mean and worst-family transfer strongly, but Tket and BQSKIT startup floors are negligible and the full Jacobian is rank deficient. Remove those two unidentifiable floors; retain only Staq floor and a common exponent. This tests whether startup overhead, rather than arbitrary nonlinear complexity, explains the gain.

Equation: `t=Staq_only_floor+scale_SDK*pilot^shared_power`. Confirmation remains unread; inspect development residuals and whole-group errors as falsifiers.


Development primary error: 0.2265188903. Worst-group error: 0.3486392744. 24groups/98observations. Model and fold states contain all coefficients, rank, training groups and training-row hashes. No confirmation feedback used.
