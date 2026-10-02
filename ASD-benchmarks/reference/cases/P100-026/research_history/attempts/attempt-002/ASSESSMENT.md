# Development result

Exponential induction continuation MAE1.665 greatly beats persistence8.294pp. Test a competing distributed-aging mechanism whose derivative decays algebraically and whose integrated response is logarithmic; complete-run transfer must distinguish asymptotic relaxation from persistent aging.

Whole-group MAE: 1.4681383981672755; worst group: 2.2430459095238846. Numerical optimizer success: True.

Parameter vector and bounds are in model.json; predictions are entirely out of fold. No causal mechanism or novelty is established by predictive fit.


## Mechanistic assessment and counterexamples

The two-timescale fit reaches the 20000-minute upper bound; its identifiable local drift limit is retained with a 1500-minute scope and no intermediate-species claim.

Candidate equation: `cat_log` in the frozen `run.py:predict` implementation. It has 1 fitted coefficients. Parameter bounds and Jacobian conditioning are in model.json; a poorly conditioned coefficient is not an independently measured physical constant. Full out-of-fold states are retained for reproducibility. The case-level source audit states the applicability and dimensional conventions.
