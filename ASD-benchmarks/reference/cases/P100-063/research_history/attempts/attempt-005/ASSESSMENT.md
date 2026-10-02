# Development result

Frequency-background terms changed MAE by less than0.1percent, with cold extrapolation still dominant. Challenge the linear thermal-contrast constraint with a quadratic temperature term in resonant amplitude. This deliberately tests a violation of equilibrium linear response; with only two temperatures per fold it may be unidentifiable, which is evidence against admission.

Whole-group MAE: 0.009867190667577849; worst group: 0.016731632431081833. Numerical optimizer success: True.

Parameter vector and bounds are in model.json; predictions are entirely out of fold. No causal mechanism or novelty is established by predictive fit.


## Mechanistic assessment and counterexamples

Their development errors exceed the simpler thermal family; source termination heating must not be silently interpreted as film heating.

Candidate equation: `mag_thermalnonlinear` in the frozen `run.py:predict` implementation. It has 7 fitted coefficients. Parameter bounds and Jacobian conditioning are in model.json; a poorly conditioned coefficient is not an independently measured physical constant. Full out-of-fold states are retained for reproducibility. The case-level source audit states the applicability and dimensional conventions.
