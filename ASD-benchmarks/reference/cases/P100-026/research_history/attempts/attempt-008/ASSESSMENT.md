# Development result

The loading-dependent equilibrium approach failed to transfer as well as the local calibration model. Challenge relaxation-plus-drift with a one-timescale algebraic decay of the measured prefix rate; this has a finite asymptote and fewer coefficients. Retain it only if complete-run accuracy or robustness is indistinguishable; otherwise stop after two consecutive unsupported structural alternatives.

Whole-group MAE: 1.5215290294142683; worst group: 2.2604418143183262. Numerical optimizer success: True.

Parameter vector and bounds are in model.json; predictions are entirely out of fold. No causal mechanism or novelty is established by predictive fit.


## Mechanistic assessment and counterexamples

The two-timescale fit reaches the 20000-minute upper bound; its identifiable local drift limit is retained with a 1500-minute scope and no intermediate-species claim.

Candidate equation: `cat_rational` in the frozen `run.py:predict` implementation. It has 1 fitted coefficients. Parameter bounds and Jacobian conditioning are in model.json; a poorly conditioned coefficient is not an independently measured physical constant. Full out-of-fold states are retained for reproducibility. The case-level source audit states the applicability and dimensional conventions.
