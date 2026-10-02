# Development result

A mixed-lubrication entrainment probability exp(-(v/vs)^p), normalized to two independently declared endpoint calibrations, may transfer the low-speed curve shape across formulations.

Whole-group MAE: 0.009693650490481279; worst group: 0.020375299188943933. Numerical optimizer success: True.

Parameter vector and bounds are in model.json; predictions are entirely out of fold. No causal mechanism or novelty is established by predictive fit.


## Mechanistic assessment and counterexamples

The reserved-formulation reference MAE exceeds log-speed interpolation despite a large development improvement.

Candidate equation: `trib_domain` in the frozen `run.py:predict` implementation. It has 2 fitted coefficients. Parameter bounds and Jacobian conditioning are in model.json; a poorly conditioned coefficient is not an independently measured physical constant. Full out-of-fold states are retained for reproducibility. The case-level source audit states the applicability and dimensional conventions.
