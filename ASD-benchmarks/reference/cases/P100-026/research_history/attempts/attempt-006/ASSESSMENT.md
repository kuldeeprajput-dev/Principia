# Development result

Attempt004 achieves0.9606pp but its slow timescale reaches the20000min bound, while amplitude and timescale are highly correlated. Attempt005 slope shrinkage fails at1.4846pp. Test the identifiable limiting model: an early relaxing calibrated slope plus an explicitly constant slow drift. Removing the unidentifiable slow timescale should preserve validation within1percent with fewer parameters; no claim of a second chemical state follows.

Whole-group MAE: 0.954747089078023; worst group: 2.013857530974744. Numerical optimizer success: True.

Parameter vector and bounds are in model.json; predictions are entirely out of fold. No causal mechanism or novelty is established by predictive fit.


## Mechanistic assessment and counterexamples

The two-timescale fit reaches the 20000-minute upper bound; its identifiable local drift limit is retained with a 1500-minute scope and no intermediate-species claim.

Candidate equation: `cat_relaxdrift` in the frozen `run.py:predict` implementation. It has 2 fitted coefficients. Parameter bounds and Jacobian conditioning are in model.json; a poorly conditioned coefficient is not an independently measured physical constant. Full out-of-fold states are retained for reproducibility. The case-level source audit states the applicability and dimensional conventions.
