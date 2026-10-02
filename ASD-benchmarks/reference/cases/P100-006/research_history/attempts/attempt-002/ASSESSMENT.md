# Development result

Attempt001 reduced MAE0.0667 to0.0404 but high-Rabi residuals remain. Test electrode-collection asymmetry through an odd dispersive component, which must improve complete-block transfer rather than simply fit symmetric peak depth.

Whole-group MAE: 0.030733781628645096; worst group: 0.05664731295084537. Numerical optimizer success: True.

Parameter vector and bounds are in model.json; predictions are entirely out of fold. No causal mechanism or novelty is established by predictive fit.


## Mechanistic assessment and counterexamples

The failed single-line candidate has larger grouped development and confirmation error; the result does not uniquely prove two microscopic channels.

Candidate equation: `atom_asym` in the frozen `run.py:predict` implementation. It has 12 fitted coefficients. Parameter bounds and Jacobian conditioning are in model.json; a poorly conditioned coefficient is not an independently measured physical constant. Full out-of-fold states are retained for reproducibility. The case-level source audit states the applicability and dimensional conventions.
