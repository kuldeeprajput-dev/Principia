# P100-005: Stable-set certificates and a degenerate accuracy task

6 substantive attempts; selected reference **constant**. Primary units: vertices.

| Model | Development MAE | Complexity | Confirmation MAE |
|---|---:|---:|---:|
| constant | 0 | 1 | 0 |
| edge_lp | 2 | 4 | 2 |
| exact | 0 | 8 | 0 |
| vertices | 8 | 0 | 8 |
| attempt_001 | 1 | 2 | 1 |
| attempt_002 | 1.825692 | 3 | 1.827751 |
| attempt_003 | 1.838486 | 3 | 1.903838 |
| attempt_004 | 0.4358466 | 5 | 0.3550563 |
| attempt_005 | 0.1332963 | 6 | 0.08333333 |
| attempt_006 | 0.06664814 | 7 | 0.04166667 |

The last two LP/midpoint candidates do not improve the zero-error training-median or exact-algorithm controls. The LP tightening is a known finite certificate property; the midpoint is not a certificate. Constant-alpha eligibility prevents meaningful accuracy-based discovery claims.

Every eligible graph has independence number4. A training-only constant therefore attains zero error, as does independent exact enumeration. That perfect score provides no evidence for a newly discovered general graph rule.

This finite, deliberately selected obstruction family is not a representative graph distribution. Classical bounds and exact enumeration are reproductions. A prediction must not be mistaken for a proof or extrapolated to arbitrary graphs.
