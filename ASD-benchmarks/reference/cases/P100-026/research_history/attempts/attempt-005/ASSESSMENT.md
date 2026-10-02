# Development result

Two-channel induction achieved0.9606pp but condition number60127 signals correlated timescales. Synthesize a calibrated relaxation model with a single gain on the early measured slope. This tests whether noisy or still-changing prefix kinetics need shrinkage, without loading-specific or extra-state terms; evaluate calibration dependence and held-run robustness.

Whole-group MAE: 1.4846397166288388; worst group: 2.24248945448576. Numerical optimizer success: True.

Parameter vector and bounds are in model.json; predictions are entirely out of fold. No causal mechanism or novelty is established by predictive fit.


## Mechanistic assessment and counterexamples

The two-timescale fit reaches the 20000-minute upper bound; its identifiable local drift limit is retained with a 1500-minute scope and no intermediate-species claim.

Candidate equation: `cat_shrink` in the frozen `run.py:predict` implementation. It has 2 fitted coefficients. Parameter bounds and Jacobian conditioning are in model.json; a poorly conditioned coefficient is not an independently measured physical constant. Full out-of-fold states are retained for reproducibility. The case-level source audit states the applicability and dimensional conventions.
