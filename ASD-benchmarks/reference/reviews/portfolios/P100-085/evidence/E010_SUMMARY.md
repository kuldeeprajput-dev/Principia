# Flask glycolic-acid recovery from independent HPLC substrate measurements

Selected on development: `baseline_unit_yield`. Confirmation cannot change selection.

| Model | OOF development MAE | Confirmation MAE |
|---|---:|---:|
| baseline_zero | 7.117056 | 3.015 |
| baseline_unit_yield | 1.748417 | 0.945 |
| baseline_stoichiometric | 3.074085 | 1.029193 |
| baseline_global_yield | 2.63565 | 0.9897992 |
| baseline_flexible | 1.89834 | 0.3792985 |
| attempt_001_ph_yield | 3.700334 | 1.107417 |
| attempt_002_loss_flux | 3.889337 | 0.7087417 |
| attempt_003_composition | 5.854903 | 1.331833 |
| attempt_004_saturation | 4.689122 | 0.9834052 |
| attempt_005_acid | 2.992533 | 0.9644419 |

Attempts: 5. At least5 material attempts and two consecutive candidates did not improve incumbent development MAE by >1%; no identified robust/interpretive gain justifies expansion.

Native CSV previews exposed several GA observations in all four flask conditions before task freezing; explicitly retrospective; no confirmation metrics used in model selection.

See each attempt for hypothesis, parent evidence, negative outcomes, coefficients, fold predictions and native anchors.
