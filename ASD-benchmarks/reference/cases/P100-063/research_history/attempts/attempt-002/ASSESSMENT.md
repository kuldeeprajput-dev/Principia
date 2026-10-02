# Development result

Dispersive admixture failed to improve thermal-Lorentzian transfer (0.009706 vs0.009703). Test whether termination heating changes linewidth, a falsifier of the assumed film-equilibrium response; a temperature-dependent linewidth must improve unseen-temperature validation.

Whole-group MAE: 0.010329516322810801; worst group: 0.018218676925898333. Numerical optimizer success: True.

Parameter vector and bounds are in model.json; predictions are entirely out of fold. No causal mechanism or novelty is established by predictive fit.


## Mechanistic assessment and counterexamples

Their development errors exceed the simpler thermal family; source termination heating must not be silently interpreted as film heating.

Candidate equation: `mag_tempwidth` in the frozen `run.py:predict` implementation. It has 7 fitted coefficients. Parameter bounds and Jacobian conditioning are in model.json; a poorly conditioned coefficient is not an independently measured physical constant. Full out-of-fold states are retained for reproducibility. The case-level source audit states the applicability and dimensional conventions.
