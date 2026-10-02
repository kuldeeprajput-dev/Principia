# Development result

Field-dependent coupling also failed (0.009706), leaving cold-temperature extrapolation dominant. Test whether the dominant temperature-transfer error is an unremoved frequency-dependent background rather than altered magnetic physics. Add a common linear/quadratic frequency background while preserving thermal contrast and resonance dispersion.

Whole-group MAE: 0.009697867862221238; worst group: 0.016304856884748916. Numerical optimizer success: True.

Parameter vector and bounds are in model.json; predictions are entirely out of fold. No causal mechanism or novelty is established by predictive fit.


## Mechanistic assessment and counterexamples

Their development errors exceed the simpler thermal family; source termination heating must not be silently interpreted as film heating.

Candidate equation: `mag_bg` in the frozen `run.py:predict` implementation. It has 8 fitted coefficients. Parameter bounds and Jacobian conditioning are in model.json; a poorly conditioned coefficient is not an independently measured physical constant. Full out-of-fold states are retained for reproducibility. The case-level source audit states the applicability and dimensional conventions.
