# P100-089 campaign summary

The reference `baseline_flexible` was chosen before confirmation. Development error was **0.12736483**; reserved-group error is **0.14335862 probability squared** across **12 groups and 6008 observations**. Scores use equal group weights, with equal row weights within each group. No population confidence interval is inferred from these small samples. Brier score is the mean squared probability error; lower is better. Supplementary threshold statistics are row-count diagnostics, while Brier and log loss are group balanced.

| Attempt | Hypothesis/model | Development error | Parameters | Improvement over incumbent>1% |
|---|---|---:|---:|---|
| 001 | attempt_001_prospect | 0.17246173 | 4 | False |
| 002 | attempt_002_context | 0.15364021 | 8 | False |
| 003 | attempt_003_memory | 0.13136662 | 11 | False |
| 004 | attempt_004_description | 0.13067264 | 12 | False |
| 005 | attempt_005_history_interaction | 0.13079309 | 13 | False |

| Frozen model | Confirmation primary error |
|---|---:|
| reference | 0.14335862 |
| baseline_mean | 0.24762301 |
| baseline_utility | 0.18844055 |
| baseline_persistence | 0.23265573 |
| baseline_flexible | 0.14335862 |

Useful scientific failures are preserved in `attempts/`. No unfavorable attempt is deleted. See `DEVELOPMENT_DIAGNOSTICS.json`, source/split/protocol freezes, first `CONFIRMATION.json`, and final reader.
