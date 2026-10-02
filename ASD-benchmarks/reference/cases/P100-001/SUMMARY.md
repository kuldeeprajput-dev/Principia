# P100-001: Exact-prefix sequence extrapolation

7 substantive attempts; selected reference **rbf**. Primary units: asinh(integer term).

| Model | Development MAE | Complexity | Confirmation MAE |
|---|---:|---:|---:|
| linear | 3.967247 | 1 | 4.222516 |
| persist | 3.080031 | 0 | 3.356433 |
| rbf | 2.029648 | 25 | 2.233349 |
| attempt_001 | 3.067098 | 2 | 3.348145 |
| attempt_002 | 2.839002 | 3 | 3.135276 |
| attempt_003 | 3.070237 | 4 | 3.352933 |
| attempt_004 | 3.071003 | 4 | 3.356433 |
| attempt_005 | 2.791184 | 5 | 3.127768 |
| attempt_006 | 2.786368 | 6 | 3.125847 |
| attempt_007 | 2.786612 | 7 | 3.125847 |

Attempts6 and7 do not materially improve the best error under the prespecified1% simplicity tolerance or worst-family error. Preserve the false-continuation risk rather than adding unbounded formula searches.

Seven exact-family investigations test finite differences, recurrences, residue classes, rational ratios, polynomial forcing, a cascade and an internal falsification gate. They do not beat the constrained learned comparator on the primary signed-asinh endpoint. Exact prefix agreement is compatible with many incompatible continuations; it is not a proof of an integer-sequence law.

A finite prefix cannot uniquely identify an infinite sequence. Related OEIS families beyond the linked affine prefixes can remain dependent. Very large integers are scored in signed-asinh coordinates, not as a percentage of exact integer matches.
