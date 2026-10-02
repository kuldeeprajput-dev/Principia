# Development result

The free feedback exponent improved attempt001 (5.52 to3.87dB) but remains worse than the2-parameter domain model3.23dB. Test the independently motivated cavity-bandwidth response: an f^2 increase of the feedback floor plus common colored environmental noise. High-frequency residuals may be finite-bandwidth effects rather than a new injection exponent.

Whole-group MAE: 7.403150975820976; worst group: 8.138748107174237. Numerical optimizer success: True.

Parameter vector and bounds are in model.json; predictions are entirely out of fold. No causal mechanism or novelty is established by predictive fit.


## Mechanistic assessment and counterexamples

The chosen shared-floor extension loses to the fixed f^-2/inverse-feedback control; a later-looking best confirmation candidate is explicitly not promoted.

Candidate equation: `laser_rolloff` in the frozen `run.py:predict` implementation. It has 4 fitted coefficients. Parameter bounds and Jacobian conditioning are in model.json; a poorly conditioned coefficient is not an independently measured physical constant. Full out-of-fold states are retained for reproducibility. The case-level source audit states the applicability and dimensional conventions.
