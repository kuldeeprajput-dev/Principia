# P100-002: Short-horizon stellar-flux response

5 substantive attempts; selected reference **attempt_003**. Primary units: relative flux (native normalization).

| Model | Development MAE | Complexity | Confirmation MAE |
|---|---:|---:|---:|
| persist | 0.003589126 | 0 | 0.001029239 |
| rbf | 0.003425151 | 25 | 0.0009076032 |
| attempt_001 | 0.003116286 | 1 | 0.0009112714 |
| attempt_002 | 0.003267639 | 1 | 0.0008512352 |
| attempt_003 | 0.002969666 | 2 | 0.0008651912 |
| attempt_004 | 0.003150634 | 2 | 0.0008423981 |
| attempt_005 | 0.003193505 | 2 | 0.0008460324 |

Attempts4 and5 degrade both mean and worst-star error relative to the two-term local response. No identified additional timescale is supported by development.

The selected two-term local response improves one-hour-ahead error over persistence and the constrained nonlinear comparator. Its negative slope coefficient damps the latest increment. That is consistent with short-timescale measurement fluctuations or mean reversion; it does not identify a physical rotation frequency or prove an oscillation mechanism.

Two stars do not establish population-level precision. Later diagnostic candidates score better on confirmation but were not promoted. No period estimated from the full sector is a predictor.
