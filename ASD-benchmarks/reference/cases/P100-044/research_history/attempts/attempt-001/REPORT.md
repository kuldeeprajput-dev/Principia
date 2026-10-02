# Pre-fit hypothesis

The size/degree exponential baseline reaches629.72s grouped MAE. Hypothesis: proximity to the classical diameter-two Moore bound, rho=n/(1+d^2), governs search consumption more simply than separate size and degree. Test an exponential in log rho with formulation offsets, keeping all capped and failed runs. The bound itself is prior mathematics, never a discovery. Compare grouped error, systematic formulation bias and offline selection regret.

## Executable candidate and development evidence

t_hat=clip(exp(b0+b1*ln(n/(1+d^2))+b2*I_flow+b3*I_linear),0,7200).

Coefficients: [7.312946833452945, 1.1531958389314516, 0.8674074408109148, -0.05434527319971749]. Units and information budget are fixed in the parent protocol.

Grouped out-of-fold MAE: 2701.92252 seconds; worst-group MAE: 5951.61112. Offline formulation-selection regret: 19.0408333 seconds. All held groups and fold training states are retained in metrics.json and predictions.csv.gz.

Preserved alternative; not selected. No material primary gain over selected model.

## Falsification and identifiability

{"folds": 12, "all_folds_exclude_held_group": true, "coefficient_min": [6.7259381000130585, 0.4568112916899969, 0.47161887416685383, -0.07907684070731276], "coefficient_max": [7.551246489190694, 1.836390320315317, 1.17795148460765, -0.030271148029714985], "boundary_folds": 0}. Coefficient extrema are descriptive fold sensitivity, not confidence intervals. Boundary contact or a poorly conditioned Jacobian weakens parameter-level interpretation. Exact values and condition numbers remain in model.json/metrics.json.

All candidate families use the same declared input budget. Physical dimensions enter only through dimensionless ratios. The nonlinear functions are empirical, physically/computationally motivated models; fit quality does not prove a mechanism.

## Reproduction and chronology

Run develop.py 001 from the case workspace with the scientific dependencies. Parent native.py reconstructs hash-verified data. Current confirmation is exposed: such a rerun is exploratory, not new confirmation. This attempt was evaluated before the final FREEZE.json. The separate confirm.py performed no fitting.
