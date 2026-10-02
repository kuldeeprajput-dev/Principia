# Pre-fit hypothesis

The Moore-occupancy-only law001 fails badly (2701.92s vs629.72s), despite similar selection regret; geometry feasibility cannot replace absolute combinatorial scale. Test exp(b0+b1*n*log(d)/40+formulation offset) motivated by exponential search-space growth. Reject if node-degree entanglement fails held-instance transfer; retain capped resource interpretation.

## Executable candidate and development evidence

t_hat=clip(exp(b0+b1*n*ln(d)/40+b2*I_flow+b3*I_linear),0,7200).

Coefficients: [4.52329832071441, 2.7727461670603137, 1.5652714186223515, -0.026722951455689276]. Units and information budget are fixed in the parent protocol.

Grouped out-of-fold MAE: 1742.76901 seconds; worst-group MAE: 4115.06304. Offline formulation-selection regret: 19.0408333 seconds. All held groups and fold training states are retained in metrics.json and predictions.csv.gz.

Preserved alternative; not selected. No material primary gain over selected model.

## Falsification and identifiability

{"folds": 12, "all_folds_exclude_held_group": true, "coefficient_min": [1.879429338073961, 1.955082632363654, 1.1458761078916153, -0.10251112552466671], "coefficient_max": [5.461791726478628, 4.455918470861676, 2.8883152447638794, -0.006944500078458709], "boundary_folds": 0}. Coefficient extrema are descriptive fold sensitivity, not confidence intervals. Boundary contact or a poorly conditioned Jacobian weakens parameter-level interpretation. Exact values and condition numbers remain in model.json/metrics.json.

All candidate families use the same declared input budget. Physical dimensions enter only through dimensionless ratios. The nonlinear functions are empirical, physically/computationally motivated models; fit quality does not prove a mechanism.

## Reproduction and chronology

Run develop.py 002 from the case workspace with the scientific dependencies. Parent native.py reconstructs hash-verified data. Current confirmation is exposed: such a rerun is exploratory, not new confirmation. This attempt was evaluated before the final FREEZE.json. The separate confirm.py performed no fitting.
