# Development result

The two-parameter relaxation-plus-drift limit preserves the dual-channel development error (0.9547 vs0.9606pp) and removes an unidentifiable timescale. Challenge its local nature with a bounded approach to a silver-loading-dependent asymptote. If this more global equilibrium hypothesis fails whole-run transfer, retain the local1500min applicability limit rather than claiming a universal kinetic law.

Whole-group MAE: 4.867621520462321; worst group: 8.946120489562357. Numerical optimizer success: True.

Parameter vector and bounds are in model.json; predictions are entirely out of fold. No causal mechanism or novelty is established by predictive fit.


## Mechanistic assessment and counterexamples

The two-timescale fit reaches the 20000-minute upper bound; its identifiable local drift limit is retained with a 1500-minute scope and no intermediate-species claim.

Candidate equation: `cat_equilibrium` in the frozen `run.py:predict` implementation. It has 3 fitted coefficients. Parameter bounds and Jacobian conditioning are in model.json; a poorly conditioned coefficient is not an independently measured physical constant. Full out-of-fold states are retained for reproducibility. The case-level source audit states the applicability and dimensional conventions.
