# P100-029 campaign summary

The reference `baseline_persistence` was chosen before confirmation. Development error was **26573.566**; reserved-group error is **38661.131 source fluorescence a.u.** across **2 groups and 48 observations**. Scores use equal group weights, with equal row weights within each group. No population confidence interval is inferred from these small samples.

| Attempt | Hypothesis/model | Development error | Parameters | Improvement over incumbent>1% |
|---|---|---:|---:|---|
| 001 | attempt_001_hill | 33709.808 | 2 | False |
| 002 | attempt_002_quenching | 37695.565 | 2 | False |
| 003 | attempt_003_local | 48730.505 | 1 | False |
| 004 | attempt_004_dye_hill | 93745.82 | 3 | False |
| 005 | attempt_005_shrink_local | 33360.553 | 2 | False |

| Frozen model | Confirmation primary error |
|---|---:|
| reference | 38661.131 |
| baseline_persistence | 38661.131 |
| baseline_linear | 74640.382 |
| baseline_langmuir | 38656.412 |
| baseline_flexible | 38849.936 |

Useful scientific failures are preserved in `attempts/`. No unfavorable attempt is deleted. See `DEVELOPMENT_DIAGNOSTICS.json`, source/split/protocol freezes, first `CONFIRMATION.json`, and final reader.
