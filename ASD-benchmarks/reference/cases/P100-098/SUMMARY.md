# P100-098: Exact polytope construction and descriptor counterexamples

6 substantive attempts; selected reference **qhull**. Primary units: facets.

| Model | Development MAE | Complexity | Confirmation MAE |
|---|---:|---:|---:|
| generic | 8.419355 | 0 | 6.933333 |
| qhull | 0 | 5 | 0 |
| attempt_001 | 1.01523 | 2 | 0.7545924 |
| attempt_002 | 1.774572 | 2 | 1.458504 |
| attempt_003 | 0.3117702 | 4 | 0.1634868 |
| attempt_004 | 0 | 6 | 0 |
| attempt_005 | 51.58065 | 4 | 53.06667 |

Exact construction and independent convex-hull baseline already reproduce development counts. The star-only simplification and scalar-descriptor sufficiency tests fail; neither improves prediction or supports a simpler exact rule.

Exact enumeration of feasible signed-spanning-tree Lipschitz potentials reproduces all reserved facet counts and agrees with an independent convex-hull control. This construction is established mathematics, independently implemented here.

The catalog is small and source-selected. Descriptor regression is an approximation; independent exact constructions already achieve zero error. No inference to larger metrics or theorem-level novelty is claimed.
