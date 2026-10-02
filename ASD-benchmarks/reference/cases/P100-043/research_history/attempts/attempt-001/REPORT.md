# Attempt001: aspect-dependent calibrated decay\n\nThe strong one-exponent anchored power law obtains development MAE0.008292 nats/token. Test beta=exp(b0+b1 log((width/depth)/32)). Both calibration losses are held fixed and shared across controls. A gain must survive whole-architecture development folds, not just pooled checkpoint fit. Reject shape interpretation if coefficient varies across folds or gains concentrate in one architecture. This cannot establish universal compute-optimal scaling.\n
## Executable candidate and development evidence

Lhat=L0+(L0-L1)*R(exp(b0+b1*ln((width/depth)/32))).

Coefficients: [-0.45185871503155584, -0.010971438510930279]. Units and information budget are fixed in the parent protocol.

Grouped out-of-fold MAE: 0.00859790052 nats per token; worst-group MAE: 0.0217961426. Late-horizon MAE: 0.0107738954. All held groups and fold training states are retained in metrics.json and predictions.csv.gz.

Preserved alternative; not selected. No material primary gain over selected model.

## Falsification and identifiability

{"folds": 17, "all_folds_exclude_held_group": true, "coefficient_min": [-0.4644976230310028, -0.0266694535815981], "coefficient_max": [-0.43221938842031765, 0.0007798143163402999], "boundary_folds": 0}. Coefficient extrema are descriptive fold sensitivity, not confidence intervals. Boundary contact or a poorly conditioned Jacobian weakens parameter-level interpretation. Exact values and condition numbers remain in model.json/metrics.json.

All candidate families use the same declared input budget. Physical dimensions enter only through dimensionless ratios. The nonlinear functions are empirical, physically/computationally motivated models; fit quality does not prove a mechanism.

## Reproduction and chronology

Run develop.py 001 from the case workspace with the scientific dependencies. Parent native.py reconstructs hash-verified data. Current confirmation is exposed: such a rerun is exploratory, not new confirmation. This attempt was evaluated before the final FREEZE.json. The separate confirm.py performed no fitting.
