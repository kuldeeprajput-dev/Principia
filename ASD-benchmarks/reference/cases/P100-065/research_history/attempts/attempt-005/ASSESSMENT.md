# Development result

The common white floor ties the feedback-exponent candidate3.865dB and remains worse than the fixed domain baseline3.226dB. Synthesize nonnegative fixed f^-2 and f^-1 environmental components plus inverse-injection white floor. This tests a physically interpretable sum of noise sources rather than a single freely fitted exponent, under identical information access.

Whole-group MAE: 4.354583816347761; worst group: 4.705673824614249. Numerical optimizer success: True.

Parameter vector and bounds are in model.json; predictions are entirely out of fold. No causal mechanism or novelty is established by predictive fit.


## Mechanistic assessment and counterexamples

The chosen shared-floor extension loses to the fixed f^-2/inverse-feedback control; a later-looking best confirmation candidate is explicitly not promoted.

Candidate equation: `laser_twoflicker` in the frozen `run.py:predict` implementation. It has 3 fitted coefficients. Parameter bounds and Jacobian conditioning are in model.json; a poorly conditioned coefficient is not an independently measured physical constant. Full out-of-fold states are retained for reproducibility. The case-level source audit states the applicability and dimensional conventions.
