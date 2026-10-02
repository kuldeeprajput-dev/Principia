# Development result

A causal induction-rate calibration followed by exponential rate decay predicts later DMM selectivity; test finite relaxation time inferred across complete reactor runs, beyond constant-prefix persistence.

Whole-group MAE: 1.6654238805122612; worst group: 2.5628079691906156. Numerical optimizer success: True.

Parameter vector and bounds are in model.json; predictions are entirely out of fold. No causal mechanism or novelty is established by predictive fit.


## Mechanistic assessment and counterexamples

The two-timescale fit reaches the 20000-minute upper bound; its identifiable local drift limit is retained with a 1500-minute scope and no intermediate-species claim.

Candidate equation: `cat_relax` in the frozen `run.py:predict` implementation. It has 1 fitted coefficients. Parameter bounds and Jacobian conditioning are in model.json; a poorly conditioned coefficient is not an independently measured physical constant. Full out-of-fold states are retained for reproducibility. The case-level source audit states the applicability and dimensional conventions.
