# Development result

Temperature-dependent linewidth worsened MAE0.00971 to0.01033. Test field-dependent coupling amplitude rather than temperature-dependent linewidth. Finite waveguide/mode coupling can vary with resonance field; the added coefficient must improve complete-temperature prediction and must not be interpreted as a change of thermal equilibrium.

Whole-group MAE: 0.009706068537787507; worst group: 0.01632310141170322. Numerical optimizer success: True.

Parameter vector and bounds are in model.json; predictions are entirely out of fold. No causal mechanism or novelty is established by predictive fit.


## Mechanistic assessment and counterexamples

Their development errors exceed the simpler thermal family; source termination heating must not be silently interpreted as film heating.

Candidate equation: `mag_field` in the frozen `run.py:predict` implementation. It has 7 fitted coefficients. Parameter bounds and Jacobian conditioning are in model.json; a poorly conditioned coefficient is not an independently measured physical constant. Full out-of-fold states are retained for reproducibility. The case-level source audit states the applicability and dimensional conventions.
