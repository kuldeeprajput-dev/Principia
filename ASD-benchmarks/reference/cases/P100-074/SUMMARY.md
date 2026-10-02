# Calibrated Src biosensor fluorescence trajectories

Selected on development: `attempt_006_slope_gate`. Confirmation cannot change selection.

| Model | OOF development MAE | Confirmation MAE |
|---|---:|---:|
| baseline_persistence | 232.4836 | 291.1549 |
| baseline_linear | 75.74199 | 126.7249 |
| baseline_mm | 183.7251 | 82.72898 |
| baseline_flexible | 72.47328 | 111.2139 |
| attempt_001_saturation | 81.54524 | 158.5652 |
| attempt_002_accelerating | 83.11992 | 158.5677 |
| attempt_003_power | 88.35053 | 155.147 |
| attempt_004_dose_saturation | 67.68396 | 129.7257 |
| attempt_005_curvature | 72.95884 | 106.9727 |
| attempt_006_slope_gate | 64.61872 | 130.2333 |
| attempt_007_slope_only | 89.56278 | 161.0739 |
| attempt_008_physical_saturation | 81.54524 | 158.5652 |

Attempts: 8. At least5 material attempts and two consecutive candidates did not improve incumbent development MAE by >1%; no identified robust/interpretive gain justifies expansion.

First9 lines and schemas inspected; early values through6.75 min were visible across doses, outside target window. Later outcomes not printed before freeze.

See each attempt for hypothesis, parent evidence, negative outcomes, coefficients, fold predictions and native anchors.
