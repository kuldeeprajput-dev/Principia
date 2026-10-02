# Pre-fit hypothesis

Two-rate002 is practically indistinguishable from shared power (0.008286vs0.008292), with slow beta at0.4 boundary and condition1564; two timescales are not identified. Hypothesis: model parameter count governs optimization exponent instead of aspect ratio. Fit beta=exp(b0+b1 log(N/0.5B)). This competing physical-computational size response is tested with held-architecture folds, coefficient stability and late-horizon bias.

## Executable candidate and development evidence

Lhat=L0+(L0-L1)*R(exp(b0+b1*ln(N/0.5B))).

Coefficients: [-0.47112414456370594, -0.05777846172593952]. Units and information budget are fixed in the parent protocol.

Grouped out-of-fold MAE: 0.00724851465 nats per token; worst-group MAE: 0.018681842. Late-horizon MAE: 0.00886204899. All held groups and fold training states are retained in metrics.json and predictions.csv.gz.

Development-selected reference

## Falsification and identifiability

{"folds": 17, "all_folds_exclude_held_group": true, "coefficient_min": [-0.47783205526850264, -0.06738434115777862], "coefficient_max": [-0.4619397100295623, -0.05072562999297772], "boundary_folds": 0}. Coefficient extrema are descriptive fold sensitivity, not confidence intervals. Boundary contact or a poorly conditioned Jacobian weakens parameter-level interpretation. Exact values and condition numbers remain in model.json/metrics.json.

All candidate families use the same declared input budget. Physical dimensions enter only through dimensionless ratios. The nonlinear functions are empirical, physically/computationally motivated models; fit quality does not prove a mechanism.

## Reproduction and chronology

Run develop.py 003 from the case workspace with the scientific dependencies. Parent native.py reconstructs hash-verified data. Current confirmation is exposed: such a rerun is exploratory, not new confirmation. This attempt was evaluated before the final FREEZE.json. The separate confirm.py performed no fitting.
