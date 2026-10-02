# Development result

Loading-dependent relaxation improves1.468 to1.299pp; residuals remain in the highest-temperature and20wtpercent baseline runs. Test two competing induction contributions: a prefix-anchored relaxing rate plus a distinct slow contribution with common amplitude. Development discrepancies between temperatures/pretreatment could indicate a second activation timescale; reject if held-run errors or conditioning worsen.

Whole-group MAE: 0.9606136613455515; worst group: 2.0113505909137217. Numerical optimizer success: True.

Parameter vector and bounds are in model.json; predictions are entirely out of fold. No causal mechanism or novelty is established by predictive fit.


## Mechanistic assessment and counterexamples

The two-timescale fit reaches the 20000-minute upper bound; its identifiable local drift limit is retained with a 1500-minute scope and no intermediate-species claim.

Candidate equation: `cat_twochannel` in the frozen `run.py:predict` implementation. It has 3 fitted coefficients. Parameter bounds and Jacobian conditioning are in model.json; a poorly conditioned coefficient is not an independently measured physical constant. Full out-of-fold states are retained for reproducibility. The case-level source audit states the applicability and dimensional conventions.
