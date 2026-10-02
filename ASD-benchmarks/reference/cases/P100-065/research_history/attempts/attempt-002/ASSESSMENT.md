# Development result

A free colored-noise exponent worsened blocked-frequency MAE5.52 vs3.23dB. Test whether the feedback floor deviates from inverse injection power; shared environmental noise and fitted feedback exponent may separate spectral-shape misspecification from feedback-gain mismatch.

Whole-group MAE: 3.865006158465979; worst group: 4.306655102793239. Numerical optimizer success: True.

Parameter vector and bounds are in model.json; predictions are entirely out of fold. No causal mechanism or novelty is established by predictive fit.


## Mechanistic assessment and counterexamples

The chosen shared-floor extension loses to the fixed f^-2/inverse-feedback control; a later-looking best confirmation candidate is explicitly not promoted.

Candidate equation: `laser_feedback` in the frozen `run.py:predict` implementation. It has 4 fitted coefficients. Parameter bounds and Jacobian conditioning are in model.json; a poorly conditioned coefficient is not an independently measured physical constant. Full out-of-fold states are retained for reproducibility. The case-level source audit states the applicability and dimensional conventions.
