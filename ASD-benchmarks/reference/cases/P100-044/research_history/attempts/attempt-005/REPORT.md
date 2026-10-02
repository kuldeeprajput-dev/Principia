# Pre-fit hypothesis

Form-specific sigmoid thresholds004 do not improve mean error(767.24), worsen formulation selection regret, and only modestly reduce worst error compared with003; both lose to established size-degree baseline. Simplification/falsification: remove degree entirely from capped exponential, retaining size and formulation. If error grows, branching/connectivity cannot be omitted from resource planning. This is a material reduced explanatory claim, not a new coefficient trial. No further model is justified unless it improves development prediction/robustness/interpretation.

## Executable candidate and development evidence

t_hat=clip(exp(b0+b1*ln(n/25)+b2*I_flow+b3*I_linear),0,7200).

Coefficients: [7.040700568851163, 7.12670059095427, 1.6801401526222925, -0.11318474647379945]. Units and information budget are fixed in the parent protocol.

Grouped out-of-fold MAE: 1182.69267 seconds; worst-group MAE: 3705.72661. Offline formulation-selection regret: 19.0408333 seconds. All held groups and fold training states are retained in metrics.json and predictions.csv.gz.

Preserved alternative; not selected. No material primary gain over selected model.

## Falsification and identifiability

{"folds": 12, "all_folds_exclude_held_group": true, "coefficient_min": [6.437944196442801, 6.561511358843643, 1.496236083677194, -0.11801467249077043], "coefficient_max": [7.217410298176279, 8.984819954721392, 2.2832796232126924, -0.0143380179329483], "boundary_folds": 0}. Coefficient extrema are descriptive fold sensitivity, not confidence intervals. Boundary contact or a poorly conditioned Jacobian weakens parameter-level interpretation. Exact values and condition numbers remain in model.json/metrics.json.

All candidate families use the same declared input budget. Physical dimensions enter only through dimensionless ratios. The nonlinear functions are empirical, physically/computationally motivated models; fit quality does not prove a mechanism.

## Reproduction and chronology

Run develop.py 005 from the case workspace with the scientific dependencies. Parent native.py reconstructs hash-verified data. Current confirmation is exposed: such a rerun is exploratory, not new confirmation. This attempt was evaluated before the final FREEZE.json. The separate confirm.py performed no fitting.
