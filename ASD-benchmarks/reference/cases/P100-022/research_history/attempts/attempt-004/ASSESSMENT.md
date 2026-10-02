# Development result

Linear leakage modestly improves89.92 to89.25 microampere but worsens the worst device282.43 and SCLC gave a negative I-rich precursor coefficient. Test an explicit finite onset voltage before weakest-link activation. A shifted Weibull hazard separates a true field threshold from continuous leakage and is challenged by held-device current prediction, not a fit to supplied switching labels.

Whole-group MAE: 92.7496716454717; worst group: 271.7493759166284. Numerical optimizer success: True.

Parameter vector and bounds are in model.json; predictions are entirely out of fold. No causal mechanism or novelty is established by predictive fit.


## Mechanistic assessment and counterexamples

The selected I-rich coefficient is negative; the model must remain an empirical ensemble surrogate, and a flexible control is marginally better in confirmation.

Candidate equation: `mem_hazard` in the frozen `run.py:predict` implementation. It has 8 fitted coefficients. Parameter bounds and Jacobian conditioning are in model.json; a poorly conditioned coefficient is not an independently measured physical constant. Full out-of-fold states are retained for reproducibility. The case-level source audit states the applicability and dimensional conventions.
