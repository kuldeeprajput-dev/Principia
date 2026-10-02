# Development result

Algebraic and exponential mixing are nearly tied (0.00970 vs0.00969), leaving PCH about0.0202 error. Test whether mixture transition speed changes exponentially with particle concentration, motivated by particle entrainment/film separation rather than arbitrary formula labels. A loading interaction must transfer to held formulations and preserve fixed endpoint behavior.

Whole-group MAE: 0.006831450120367674; worst group: 0.013462997372499001. Numerical optimizer success: True.

Parameter vector and bounds are in model.json; predictions are entirely out of fold. No causal mechanism or novelty is established by predictive fit.


## Mechanistic assessment and counterexamples

The reserved-formulation reference MAE exceeds log-speed interpolation despite a large development improvement.

Candidate equation: `trib_concentration` in the frozen `run.py:predict` implementation. It has 3 fitted coefficients. Parameter bounds and Jacobian conditioning are in model.json; a poorly conditioned coefficient is not an independently measured physical constant. Full out-of-fold states are retained for reproducibility. The case-level source audit states the applicability and dimensional conventions.
