# Pre-fit hypothesis

Combinatorial002 MAE1742.77 is worse than separate-size/degree baseline629.72. Hypothesis: observed capped consumption has a smooth resource-limit transition rather than an unbounded exponential abruptly clipped at7200. Fit logistic7200/[1+exp(-z)] with size, Moore occupancy and formulation offsets. This models resource consumption and may not estimate actual uncensored solve time; test all held instances, including capped runs.

## Executable candidate and development evidence

t_hat=7200*sigmoid(b0+b1*ln(n/25)+b2*ln(n/(1+d^2))+b3*I_flow+b4*I_linear).

Coefficients: [-3.3683101645082045, 15.54653709565169, 3.3649187032141006, 4.393195360450941, -0.21389031833812377]. Units and information budget are fixed in the parent protocol.

Grouped out-of-fold MAE: 759.786993 seconds; worst-group MAE: 2585.96482. Offline formulation-selection regret: 19.0408333 seconds. All held groups and fold training states are retained in metrics.json and predictions.csv.gz.

Preserved alternative; not selected. No material primary gain over selected model.

## Falsification and identifiability

{"folds": 12, "all_folds_exclude_held_group": true, "coefficient_min": [-3.9613945961415986, 14.233160436808522, 2.5303292766318006, 3.4751373024825885, -0.2462073527510485], "coefficient_max": [-2.3264084072962925, 17.192042451382644, 4.447017533510923, 5.648249943715607, -0.16247617997279795], "boundary_folds": 0}. Coefficient extrema are descriptive fold sensitivity, not confidence intervals. Boundary contact or a poorly conditioned Jacobian weakens parameter-level interpretation. Exact values and condition numbers remain in model.json/metrics.json.

All candidate families use the same declared input budget. Physical dimensions enter only through dimensionless ratios. The nonlinear functions are empirical, physically/computationally motivated models; fit quality does not prove a mechanism.

## Reproduction and chronology

Run develop.py 003 from the case workspace with the scientific dependencies. Parent native.py reconstructs hash-verified data. Current confirmation is exposed: such a rerun is exploratory, not new confirmation. This attempt was evaluated before the final FREEZE.json. The separate confirm.py performed no fitting.
