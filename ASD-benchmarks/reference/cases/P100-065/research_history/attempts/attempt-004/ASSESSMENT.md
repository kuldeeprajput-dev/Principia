# Development result

Finite-bandwidth rolloff worsened MAE3.87 to7.40dB despite acceptable optimization, arguing against adding curvature indiscriminately. Test an injection-independent white floor in addition to inverse-feedback floor and colored environment. This checks whether residuals arise from a detector/common floor rather than enhanced cavity coupling; identifiability must be reported with only two development ratios.

Whole-group MAE: 3.8650039489702115; worst group: 4.306646894495754. Numerical optimizer success: True.

Parameter vector and bounds are in model.json; predictions are entirely out of fold. No causal mechanism or novelty is established by predictive fit.


## Mechanistic assessment and counterexamples

The chosen shared-floor extension loses to the fixed f^-2/inverse-feedback control; a later-looking best confirmation candidate is explicitly not promoted.

Candidate equation: `laser_sharedfloor` in the frozen `run.py:predict` implementation. It has 4 fitted coefficients. Parameter bounds and Jacobian conditioning are in model.json; a poorly conditioned coefficient is not an independently measured physical constant. Full out-of-fold states are retained for reproducibility. The case-level source audit states the applicability and dimensional conventions.
