# attempt-002

# Preregistered development attempt

Recorded UTC: 2026-10-02T02:01:42.020699+00:00

Parent evidence: 001 Brier0.0508288,worst0.0543555; flexible0.0500413. Evaluate household-scale identifiability, not just parameter gain.

Shock001 improved resource baseline but still trails flexible. Challenge the imposed sqrt household equivalence scale by separately estimating log-income and log-size response. If household exponent -c/b differs unstably across regions, resource equivalence is not identified as a universal scaling law.

Equation: `p=logistic(a+b*log(income_proxy)+c*log(hhsize)+d*workloss)`. Confirmation remains unread; inspect development residuals and whole-group errors as falsifiers.


Development primary error: 0.05088464433. Worst-group error: 0.05530000342. 4groups/10799observations. Model and fold states contain all coefficients, rank, training groups and training-row hashes. No confirmation feedback used.
