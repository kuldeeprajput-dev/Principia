# Development result

The source attributes sub-kHz noise to environmental pickup. A fitted colored-noise exponent shared by injection ratios plus inverse-power feedback floor may outperform the fixed random-walk f^-2 model.

Whole-group MAE: 5.519746420878376; worst group: 5.708943863472854. Numerical optimizer success: True.

Parameter vector and bounds are in model.json; predictions are entirely out of fold. No causal mechanism or novelty is established by predictive fit.


## Mechanistic assessment and counterexamples

The chosen shared-floor extension loses to the fixed f^-2/inverse-feedback control; a later-looking best confirmation candidate is explicitly not promoted.

Candidate equation: `laser_colored` in the frozen `run.py:predict` implementation. It has 3 fitted coefficients. Parameter bounds and Jacobian conditioning are in model.json; a poorly conditioned coefficient is not an independently measured physical constant. Full out-of-fold states are retained for reproducibility. The case-level source audit states the applicability and dimensional conventions.
