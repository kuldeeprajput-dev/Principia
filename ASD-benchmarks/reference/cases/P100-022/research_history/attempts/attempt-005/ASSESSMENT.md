# Development result

Finite-onset hazard MAE92.75 did not beat the leakage models. Synthesize a parsimonious ensemble model with a shared current ceiling and transition width, retaining only a composition shift in midpoint. This is a falsifiable simplification of separate composition kinetics, and the ceiling remains an instrument/circuit property.

Whole-group MAE: 100.40027221425098; worst group: 265.6362960751255. Numerical optimizer success: True.

Parameter vector and bounds are in model.json; predictions are entirely out of fold. No causal mechanism or novelty is established by predictive fit.


## Mechanistic assessment and counterexamples

The selected I-rich coefficient is negative; the model must remain an empirical ensemble surrogate, and a flexible control is marginally better in confirmation.

Candidate equation: `mem_shared` in the frozen `run.py:predict` implementation. It has 4 fitted coefficients. Parameter bounds and Jacobian conditioning are in model.json; a poorly conditioned coefficient is not an independently measured physical constant. Full out-of-fold states are retained for reproducibility. The case-level source audit states the applicability and dimensional conventions.
