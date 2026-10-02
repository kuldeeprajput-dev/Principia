# Development result

Attempt001 exponential entrainment MAE0.00969 leaves PCH/PEG worst. Test algebraic load-sharing survival rather than exponential entrainment, preserving both endpoint calibrations and testing whole formulations.

Whole-group MAE: 0.009701937353106031; worst group: 0.020207615459760162. Numerical optimizer success: True.

Parameter vector and bounds are in model.json; predictions are entirely out of fold. No causal mechanism or novelty is established by predictive fit.


## Mechanistic assessment and counterexamples

The reserved-formulation reference MAE exceeds log-speed interpolation despite a large development improvement.

Candidate equation: `trib_rational` in the frozen `run.py:predict` implementation. It has 2 fitted coefficients. Parameter bounds and Jacobian conditioning are in model.json; a poorly conditioned coefficient is not an independently measured physical constant. Full out-of-fold states are retained for reproducibility. The case-level source audit states the applicability and dimensional conventions.
