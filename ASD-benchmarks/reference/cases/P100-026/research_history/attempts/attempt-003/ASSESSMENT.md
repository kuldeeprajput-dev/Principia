# Development result

Log aging improved MAE1.665 to1.468. Test whether induction relaxation time varies with silver loading, tau=tau20*(Ag/20)^p. The six development runs include1,5,20wtpercent; hold each run out so loading-specific kinetics must generalize and cannot absorb the held trajectory.

Whole-group MAE: 1.2987659891581265; worst group: 2.2467950288089766. Numerical optimizer success: True.

Parameter vector and bounds are in model.json; predictions are entirely out of fold. No causal mechanism or novelty is established by predictive fit.


## Mechanistic assessment and counterexamples

The two-timescale fit reaches the 20000-minute upper bound; its identifiable local drift limit is retained with a 1500-minute scope and no intermediate-species claim.

Candidate equation: `cat_loading` in the frozen `run.py:predict` implementation. It has 2 fitted coefficients. Parameter bounds and Jacobian conditioning are in model.json; a poorly conditioned coefficient is not an independently measured physical constant. Full out-of-fold states are retained for reproducibility. The case-level source audit states the applicability and dimensional conventions.
