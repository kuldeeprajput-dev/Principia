# P100-043: scientific portfolio

hot-run validation log-perplexity at20–100B tokens.

7 substantive attempts; reference selected before confirmation: **attempt_003**.

| Candidate | Development MAE | Parameters | Confirmation MAE |
|---|---:|---:|---:|
| log_tangent | 0.113653 | 0 | 0.1092518 |
| persist | 0.1228435 | 0 | 0.1328579 |
| power | 0.008292089 | 1 | 0.007991415 |
| rbf | 0.01091212 | 33 | 0.01084989 |
| attempt_001 | 0.008597901 | 2 | 0.008299588 |
| attempt_002 | 0.008286375 | 3 | 0.008299093 |
| attempt_003 | 0.007248515 | 2 | 0.005276654 |
| attempt_004 | 0.008280941 | 2 | 0.00836947 |
| attempt_005 | 0.007405269 | 3 | 0.005419787 |
| attempt_006 | 0.007616594 | 3 | 0.005087856 |
| attempt_007 | 0.007721227 | 3 | 0.007182623 |

Units: nats per token. All final results are exposed; confirmation alternatives did not change selection.

Attempts006 and007 improve neither the selected003 primary/late accuracy nor the robust005 worst-group error. Both are more complex. No distinct evidence-led extension remains within the frozen two-anchor task. Seven substantive attempts retained.

One source corpus, tokenizer, optimization protocol and fixed validation set;22 architectures without repeated independent training seeds. Calibration losses from each evaluated architecture are required. Forecast20–100B tokens only; no universal compute-optimal rule.
