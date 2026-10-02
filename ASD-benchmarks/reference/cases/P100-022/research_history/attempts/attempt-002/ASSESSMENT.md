# Development result

Weibull turn-on MAE96.88 did not improve logistic96.26 microampere. Independently test a pre-forming V^2 space-charge-like channel plus activated transition; this challenges whether turn-on-tail residuals require a conductive precursor rather than a different threshold distribution.

Whole-group MAE: 89.91603895209667; worst group: 277.4400994536406. Numerical optimizer success: True.

Parameter vector and bounds are in model.json; predictions are entirely out of fold. No causal mechanism or novelty is established by predictive fit.


## Mechanistic assessment and counterexamples

The selected I-rich coefficient is negative; the model must remain an empirical ensemble surrogate, and a flexible control is marginally better in confirmation.

Candidate equation: `mem_sclc` in the frozen `run.py:predict` implementation. It has 8 fitted coefficients. Parameter bounds and Jacobian conditioning are in model.json; a poorly conditioned coefficient is not an independently measured physical constant. Full out-of-fold states are retained for reproducibility. The case-level source audit states the applicability and dimensional conventions.
