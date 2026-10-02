# Development result

Concentration-dependent transition improves0.00970 to0.00683 and worst-group0.02021 to0.01346. Test an additive viscous/shear contribution anchored to vanish at both calibration speeds. It competes with pure load-sharing and may explain a low-speed residual trend; any negative drag coefficient or unstable transfer limits a physical interpretation.

Whole-group MAE: 0.008950918729712232; worst group: 0.018779468964835542. Numerical optimizer success: True.

Parameter vector and bounds are in model.json; predictions are entirely out of fold. No causal mechanism or novelty is established by predictive fit.


## Mechanistic assessment and counterexamples

The reserved-formulation reference MAE exceeds log-speed interpolation despite a large development improvement.

Candidate equation: `trib_drag` in the frozen `run.py:predict` implementation. It has 3 fitted coefficients. Parameter bounds and Jacobian conditioning are in model.json; a poorly conditioned coefficient is not an independently measured physical constant. Full out-of-fold states are retained for reproducibility. The case-level source audit states the applicability and dimensional conventions.
