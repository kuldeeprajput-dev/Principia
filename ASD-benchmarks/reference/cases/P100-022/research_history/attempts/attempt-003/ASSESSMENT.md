# Development result

The SCLC precursor improved MAE96.88 to89.92 but worsened worst-device error267.19 to277.44. It is now challenged by a linear Ohmic precursor under the same threshold model. Compare V versusV^2 tails with whole-device validation, including current-clamp effects; no claim of microscopic transport solely from a better fit.

Whole-group MAE: 89.2473632976089; worst group: 282.42963666017755. Numerical optimizer success: True.

Parameter vector and bounds are in model.json; predictions are entirely out of fold. No causal mechanism or novelty is established by predictive fit.


## Mechanistic assessment and counterexamples

The selected I-rich coefficient is negative; the model must remain an empirical ensemble surrogate, and a flexible control is marginally better in confirmation.

Candidate equation: `mem_leak` in the frozen `run.py:predict` implementation. It has 8 fitted coefficients. Parameter bounds and Jacobian conditioning are in model.json; a poorly conditioned coefficient is not an independently measured physical constant. Full out-of-fold states are retained for reproducibility. The case-level source audit states the applicability and dimensional conventions.
