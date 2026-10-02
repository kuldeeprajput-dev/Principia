# Development result

Two overlapping readout contributions with distinct linewidths can explain the source-reported peak-to-dip reversal without assigning a new atomic transition. Test positive broad resonance minus saturating narrow collection response.

Whole-group MAE: 0.040400544803891734; worst group: 0.06705851458910593. Numerical optimizer success: True.

Parameter vector and bounds are in model.json; predictions are entirely out of fold. No causal mechanism or novelty is established by predictive fit.


## Mechanistic assessment and counterexamples

The failed single-line candidate has larger grouped development and confirmation error; the result does not uniquely prove two microscopic channels.

Candidate equation: `atom_double` in the frozen `run.py:predict` implementation. It has 11 fitted coefficients. Parameter bounds and Jacobian conditioning are in model.json; a poorly conditioned coefficient is not an independently measured physical constant. Full out-of-fold states are retained for reproducibility. The case-level source audit states the applicability and dimensional conventions.
