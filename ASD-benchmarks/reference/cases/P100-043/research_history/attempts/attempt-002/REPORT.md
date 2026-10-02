# Pre-fit hypothesis

The aspect-dependent exponent (001 MAE0.008598) did not improve shared power (0.008292). Competing explanation: two relaxation rates contribute to optimization, rather than aspect controlling one exponent. Fit a convex mixture of slow and fast anchored power responses; test whether the extra identifiable timescale improves grouped accuracy and late-horizon error. Boundary collapse or large Jacobian condition falsifies evidence for two rates.

## Executable candidate and development evidence

Lhat=L0+(L0-L1)*[w*R(beta_slow)+(1-w)*R(beta_fast)].

Coefficients: [0.39999999999999997, 1.1627403654141304, 0.600440869549186]. Units and information budget are fixed in the parent protocol.

Grouped out-of-fold MAE: 0.00828637527 nats per token; worst-group MAE: 0.0198385711. Late-horizon MAE: 0.0103358591. All held groups and fold training states are retained in metrics.json and predictions.csv.gz.

Preserved alternative; not selected. No material primary gain over selected model.

## Falsification and identifiability

{"folds": 17, "all_folds_exclude_held_group": true, "coefficient_min": [0.39999998067425657, 1.104094492294891, 0.5803795311967203], "coefficient_max": [0.39999999999999997, 1.2342635663664865, 0.6156855154516586], "boundary_folds": 17}. Coefficient extrema are descriptive fold sensitivity, not confidence intervals. Boundary contact or a poorly conditioned Jacobian weakens parameter-level interpretation. Exact values and condition numbers remain in model.json/metrics.json.

All candidate families use the same declared input budget. Physical dimensions enter only through dimensionless ratios. The nonlinear functions are empirical, physically/computationally motivated models; fit quality does not prove a mechanism.

## Reproduction and chronology

Run develop.py 002 from the case workspace with the scientific dependencies. Parent native.py reconstructs hash-verified data. Current confirmation is exposed: such a rerun is exploratory, not new confirmation. This attempt was evaluated before the final FREEZE.json. The separate confirm.py performed no fitting.
