# Development result

Power broadening remained worse than the asymmetric model (0.04029 vs0.03073) and conditioning worsened. Test a bounded background population contribution u^2/(1+u^2) in the two-response model. This targets the saturation residual without changing line symmetry; compare the simpler competing models and reject unsupported population attribution.

Whole-group MAE: 0.04254598271928149; worst group: 0.06704817806950102. Numerical optimizer success: True.

Parameter vector and bounds are in model.json; predictions are entirely out of fold. No causal mechanism or novelty is established by predictive fit.


## Mechanistic assessment and counterexamples

The failed single-line candidate has larger grouped development and confirmation error; the result does not uniquely prove two microscopic channels.

Candidate equation: `atom_saturate` in the frozen `run.py:predict` implementation. It has 12 fitted coefficients. Parameter bounds and Jacobian conditioning are in model.json; a poorly conditioned coefficient is not an independently measured physical constant. Full out-of-fold states are retained for reproducibility. The case-level source audit states the applicability and dimensional conventions.
