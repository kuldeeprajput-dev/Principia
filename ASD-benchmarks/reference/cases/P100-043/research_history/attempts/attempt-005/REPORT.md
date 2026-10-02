# Pre-fit hypothesis

Amplitude attenuation004 MAE0.008281 cannot explain the better parameter-size model0030.007249. Synthesize size and aspect effects: beta=exp(b0+b1 log(N/0.5B)+b2 log((width/depth)/32)). Test whether aspect has independent predictive support after size adjustment, unlike failed aspect-only001. Added complexity must beat the1% simplicity tolerance and remain stable across architecture folds. Otherwise retain simpler size response.

## Executable candidate and development evidence

Lhat=L0+(L0-L1)*R(exp(b0+b1*ln((width/depth)/32)+b2*ln(N/0.5B))).

Coefficients: [-0.5076427144076395, 0.0488159695673223, -0.09615007921224746]. Units and information budget are fixed in the parent protocol.

Grouped out-of-fold MAE: 0.00740526894 nats per token; worst-group MAE: 0.014033552. Late-horizon MAE: 0.0092160826. All held groups and fold training states are retained in metrics.json and predictions.csv.gz.

Preserved alternative; not selected. No material primary gain over selected model.

## Falsification and identifiability

{"folds": 17, "all_folds_exclude_held_group": true, "coefficient_min": [-0.5332769451860396, 0.03363598555436129, -0.11855507115907708], "coefficient_max": [-0.4894130450346823, 0.060698065918068464, -0.08059639207850419], "boundary_folds": 0}. Coefficient extrema are descriptive fold sensitivity, not confidence intervals. Boundary contact or a poorly conditioned Jacobian weakens parameter-level interpretation. Exact values and condition numbers remain in model.json/metrics.json.

All candidate families use the same declared input budget. Physical dimensions enter only through dimensionless ratios. The nonlinear functions are empirical, physically/computationally motivated models; fit quality does not prove a mechanism.

## Reproduction and chronology

Run develop.py 005 from the case workspace with the scientific dependencies. Parent native.py reconstructs hash-verified data. Current confirmation is exposed: such a rerun is exploratory, not new confirmation. This attempt was evaluated before the final FREEZE.json. The separate confirm.py performed no fitting.
