# Development result

A weakest-link activation hazard may explain the ensemble initial-forming current better than a logistic threshold distribution. Compare composition-specific Weibull turn-on with Gaussian/logistic and flexible controls, without interpreting controller current saturation as new physics.

Whole-group MAE: 96.88019260203684; worst group: 267.18782105041. Numerical optimizer success: True.

Parameter vector and bounds are in model.json; predictions are entirely out of fold. No causal mechanism or novelty is established by predictive fit.


## Mechanistic assessment and counterexamples

The selected I-rich coefficient is negative; the model must remain an empirical ensemble surrogate, and a flexible control is marginally better in confirmation.

Candidate equation: `mem_weibull` in the frozen `run.py:predict` implementation. It has 6 fitted coefficients. Parameter bounds and Jacobian conditioning are in model.json; a poorly conditioned coefficient is not an independently measured physical constant. Full out-of-fold states are retained for reproducibility. The case-level source audit states the applicability and dimensional conventions.
