# P100-026: campaign summary

A two-parameter, causal prefix-conditioned forecast improves persistence and straight-line continuation on two reserved reactor runs. It loses to the flexible control and several other frozen candidates, so evidence supports useful short-horizon calibration rather than a superior or universal kinetic law.

The raw adapter, contracts, every attempt, stopping decision and confirmation freeze are preserved. No subsequent model was selected using confirmation.

| Attempt | Hypothesis/model | Grouped development MAE | Coefficients | Disposition |
|---|---|---:|---:|---|
| attempt-001 | Single relaxing prefix rate | 1.66542 | 1 | Retained alternative; not selected |
| attempt-002 | Algebraic aging rate | 1.46814 | 1 | Retained alternative; not selected |
| attempt-003 | Loading-dependent relaxation | 1.29877 | 2 | Retained alternative; not selected |
| attempt-004 | Two-timescale induction | 0.960614 | 3 | Retained alternative; not selected |
| attempt-005 | Shrunk prefix relaxation | 1.48464 | 2 | Retained alternative; not selected |
| attempt-006 | Relaxation plus slow drift | 0.954747 | 2 | Development-selected reference |
| attempt-007 | Loading-dependent equilibrium | 4.86762 | 3 | Retained alternative; not selected |
| attempt-008 | Rational rate decay | 1.52153 | 1 | Retained alternative; not selected |

Confirmation MAE: **1.43487 percentage points**. The lowest observed confirmation error among all frozen models is 0.612867 for Loading-dependent equilibrium. This is a diagnostic comparison; it does not replace the development-selected reference.

Read [final results](package/FINDINGS.md). Calibration and source limitations are documented in [SOURCE_AND_UNITS.md](SOURCE_AND_UNITS.md).
