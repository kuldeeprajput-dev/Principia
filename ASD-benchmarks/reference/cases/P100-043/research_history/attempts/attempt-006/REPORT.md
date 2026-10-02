# Pre-fit hypothesis

Combined aspect/size005 worsens mean error0.007405 vs0030.007249 but reduces worst-group0.01868 to0.01403; continuation is justified by robustness gain. Test a finite-size saturation beta=b_inf+a/(1+N/Nc), which approaches finite positive rate at large and small model size, unlike an unbounded exponent-size power law. Retain three coefficients and compare identifiability, held-architecture accuracy and late horizon. Unknown crossover outside data range is not extrapolation evidence.

## Executable candidate and development evidence

Lhat=L0+(L0-L1)*R(beta_inf+a/(1+N/Nc)).

Coefficients: [0.5534062306997947, 0.17331982561972256, 0.3380698126883672]. Units and information budget are fixed in the parent protocol.

Grouped out-of-fold MAE: 0.00761659395 nats per token; worst-group MAE: 0.0190599922. Late-horizon MAE: 0.00937394452. All held groups and fold training states are retained in metrics.json and predictions.csv.gz.

Preserved alternative; not selected. No material primary gain over selected model.

## Falsification and identifiability

{"folds": 17, "all_folds_exclude_held_group": true, "coefficient_min": [0.5156748232634082, 0.1499490180383813, 0.13306310154020878], "coefficient_max": [0.5834783626325665, 0.20786837250698226, 0.6375911830682567], "boundary_folds": 0}. Coefficient extrema are descriptive fold sensitivity, not confidence intervals. Boundary contact or a poorly conditioned Jacobian weakens parameter-level interpretation. Exact values and condition numbers remain in model.json/metrics.json.

All candidate families use the same declared input budget. Physical dimensions enter only through dimensionless ratios. The nonlinear functions are empirical, physically/computationally motivated models; fit quality does not prove a mechanism.

## Reproduction and chronology

Run develop.py 006 from the case workspace with the scientific dependencies. Parent native.py reconstructs hash-verified data. Current confirmation is exposed: such a rerun is exploratory, not new confirmation. This attempt was evaluated before the final FREEZE.json. The separate confirm.py performed no fitting.
