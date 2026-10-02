# Development result

Circuit impedance mismatch should produce a dispersive admixture to thermal Lorentzian noise. Test an antisymmetric component with amplitude proportional to the termination-to-film temperature contrast, with field-dependent resonance center.

Whole-group MAE: 0.009705739641020112; worst group: 0.016326249894476823. Numerical optimizer success: True.

Parameter vector and bounds are in model.json; predictions are entirely out of fold. No causal mechanism or novelty is established by predictive fit.


## Mechanistic assessment and counterexamples

Their development errors exceed the simpler thermal family; source termination heating must not be silently interpreted as film heating.

Candidate equation: `mag_asym` in the frozen `run.py:predict` implementation. It has 7 fitted coefficients. Parameter bounds and Jacobian conditioning are in model.json; a poorly conditioned coefficient is not an independently measured physical constant. Full out-of-fold states are retained for reproducibility. The case-level source audit states the applicability and dimensional conventions.
