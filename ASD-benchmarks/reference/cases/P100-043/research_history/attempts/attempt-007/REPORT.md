# Pre-fit hypothesis

Bounded-size006 worsens MAE0.007617 and worst-group0.01906; its three-parameter crossover is less stable than the two-parameter size law. Last distinct development-led alternative: optimization penalty depends on distance from a balanced width/depth ratio, not signed aspect. Test beta=exp(b0+b1 log(N/0.5B)+b2 abs(log((width/depth)/32))). The balance32 is a fixed geometric reference, not fitted to target losses. This challenges linear-aspect005 and size003; only meaningful accuracy/robustness gains justify further continuation.

## Executable candidate and development evidence

Lhat=L0+(L0-L1)*R(exp(b0+b1*ln(N/0.5B)+b2*abs(ln((width/depth)/32)))).

Coefficients: [-0.43392321316350424, -0.05338829366378818, -0.027661744429196927]. Units and information budget are fixed in the parent protocol.

Grouped out-of-fold MAE: 0.00772122735 nats per token; worst-group MAE: 0.0188457628. Late-horizon MAE: 0.00945431757. All held groups and fold training states are retained in metrics.json and predictions.csv.gz.

Preserved alternative; not selected. No material primary gain over selected model.

## Falsification and identifiability

{"folds": 17, "all_folds_exclude_held_group": true, "coefficient_min": [-0.46012651691926104, -0.06704765834594086, -0.04603804762482966], "coefficient_max": [-0.41718862045538124, -0.04225494595006678, -0.0015974201876996013], "boundary_folds": 0}. Coefficient extrema are descriptive fold sensitivity, not confidence intervals. Boundary contact or a poorly conditioned Jacobian weakens parameter-level interpretation. Exact values and condition numbers remain in model.json/metrics.json.

All candidate families use the same declared input budget. Physical dimensions enter only through dimensionless ratios. The nonlinear functions are empirical, physically/computationally motivated models; fit quality does not prove a mechanism.

## Reproduction and chronology

Run develop.py 007 from the case workspace with the scientific dependencies. Parent native.py reconstructs hash-verified data. Current confirmation is exposed: such a rerun is exploratory, not new confirmation. This attempt was evaluated before the final FREEZE.json. The separate confirm.py performed no fitting.
