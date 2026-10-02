# Pre-fit hypothesis

Parameter-size exponent003 improves MAE to0.007249,13% below shared power; exponent slope is small negative. Alternative explanation: early checkpoint noise/optimization transients bias the two-anchor amplitude. Fit a common amplitude attenuation c and exponent instead of model-size dependence, retaining the same permitted anchors and full held-architecture folds. A c different from1 would indicate empirical forecast calibration, not a new scaling exponent. Compare matched complexity, late errors and fold coefficient spread.

## Executable candidate and development evidence

Lhat=L0+c*(L0-L1)*R(beta).

Coefficients: [0.5617016920857099, 0.9297695494126422]. Units and information budget are fixed in the parent protocol.

Grouped out-of-fold MAE: 0.00828094122 nats per token; worst-group MAE: 0.0198190162. Late-horizon MAE: 0.010327112. All held groups and fold training states are retained in metrics.json and predictions.csv.gz.

Preserved alternative; not selected. No material primary gain over selected model.

## Falsification and identifiability

{"folds": 17, "all_folds_exclude_held_group": true, "coefficient_min": [0.5555854461769345, 0.9211203389775798], "coefficient_max": [0.568812743250558, 0.9371530634415871], "boundary_folds": 0}. Coefficient extrema are descriptive fold sensitivity, not confidence intervals. Boundary contact or a poorly conditioned Jacobian weakens parameter-level interpretation. Exact values and condition numbers remain in model.json/metrics.json.

All candidate families use the same declared input budget. Physical dimensions enter only through dimensionless ratios. The nonlinear functions are empirical, physically/computationally motivated models; fit quality does not prove a mechanism.

## Reproduction and chronology

Run develop.py 004 from the case workspace with the scientific dependencies. Parent native.py reconstructs hash-verified data. Current confirmation is exposed: such a rerun is exploratory, not new confirmation. This attempt was evaluated before the final FREEZE.json. The separate confirm.py performed no fitting.
