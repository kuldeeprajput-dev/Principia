# Development result

The single-line alternative failed (MAE0.06713 vs asymmetric dual-response0.03073), supporting structural rather than mere parameter refinement. Test quadrature power broadening in both overlapping responses instead of linear linewidth addition. This directly distinguishes independent homogeneous broadening contributions from a merely empirical width slope; compare complete-Rabi blocks and parameter conditioning.

Whole-group MAE: 0.040287844245878474; worst group: 0.06646602808835063. Numerical optimizer success: True.

Parameter vector and bounds are in model.json; predictions are entirely out of fold. No causal mechanism or novelty is established by predictive fit.


## Mechanistic assessment and counterexamples

The failed single-line candidate has larger grouped development and confirmation error; the result does not uniquely prove two microscopic channels.

Candidate equation: `atom_powerwidth` in the frozen `run.py:predict` implementation. It has 11 fitted coefficients. Parameter bounds and Jacobian conditioning are in model.json; a poorly conditioned coefficient is not an independently measured physical constant. Full out-of-fold states are retained for reproducibility. The case-level source audit states the applicability and dimensional conventions.
