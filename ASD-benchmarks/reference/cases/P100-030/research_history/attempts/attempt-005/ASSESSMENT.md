# Development result

The drag channel worsened concentration-model MAE0.00683 to0.00895. Test a fixed square-root speed dependence as a parsimonious mixed-lubrication model, eliminating the free shape exponent. If it matches flexible shape within1percent, prefer the simpler equation; do not promote mere parameter changes as independent findings.

Whole-group MAE: 0.010562608962931638; worst group: 0.02031655979649781. Numerical optimizer success: True.

Parameter vector and bounds are in model.json; predictions are entirely out of fold. No causal mechanism or novelty is established by predictive fit.


## Mechanistic assessment and counterexamples

The reserved-formulation reference MAE exceeds log-speed interpolation despite a large development improvement.

Candidate equation: `trib_sqrt` in the frozen `run.py:predict` implementation. It has 1 fitted coefficients. Parameter bounds and Jacobian conditioning are in model.json; a poorly conditioned coefficient is not an independently measured physical constant. Full out-of-fold states are retained for reproducibility. The case-level source audit states the applicability and dimensional conventions.
