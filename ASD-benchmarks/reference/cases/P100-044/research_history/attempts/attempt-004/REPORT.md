# Pre-fit hypothesis

Smooth-cap003 error759.79 still trails exp-size629.72. Hypothesis: formulation-specific growth thresholds matter because formulations introduce different variable/constraint scaling with n. Add formulation-by-log-size interactions to sigmoid-cap model, without peeking at held instances. Test group error, fold coefficient stability and whether superior numerical fit is extrapolation-sensitive rather than an algorithmic law.

## Executable candidate and development evidence

t_hat=7200*sigmoid(b0+b1*ln(n/25)+b2*ln(n/(1+d^2))+b3*I_flow+b4*I_linear+b5*I_flow*ln(n/25)+b6*I_linear*ln(n/25)).

Coefficients: [-3.4386930215767593, 14.655031312617973, 3.858034618951169, 4.841390510620211, -0.5105866671415976, 6.540929866474488, 1.9919470977878204]. Units and information budget are fixed in the parent protocol.

Grouped out-of-fold MAE: 767.238168 seconds; worst-group MAE: 2407.19231. Offline formulation-selection regret: 35.7316667 seconds. All held groups and fold training states are retained in metrics.json and predictions.csv.gz.

Preserved alternative; not selected. No material primary gain over selected model.

## Falsification and identifiability

{"folds": 12, "all_folds_exclude_held_group": true, "coefficient_min": [-3.8625922425851686, 12.288773596563, 2.7860672728600524, 3.7008988362438906, -0.9111864770221316, 1.7461766263968226, 1.018448589203854], "coefficient_max": [-2.3962689206485, 15.579071115857149, 4.592364987586851, 5.6135509891769075, -0.35782604606049806, 8.999388966240517, 3.5276389753386397], "boundary_folds": 0}. Coefficient extrema are descriptive fold sensitivity, not confidence intervals. Boundary contact or a poorly conditioned Jacobian weakens parameter-level interpretation. Exact values and condition numbers remain in model.json/metrics.json.

All candidate families use the same declared input budget. Physical dimensions enter only through dimensionless ratios. The nonlinear functions are empirical, physically/computationally motivated models; fit quality does not prove a mechanism.

## Reproduction and chronology

Run develop.py 004 from the case workspace with the scientific dependencies. Parent native.py reconstructs hash-verified data. Current confirmation is exposed: such a rerun is exploratory, not new confirmation. This attempt was evaluated before the final FREEZE.json. The separate confirm.py performed no fitting.
