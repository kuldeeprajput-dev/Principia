# P100-098: Exact polytope construction and descriptor counterexamples

## Scenario and question

The retained five-point KRW metric files provide 77 native metric/combinatorial records. Distance scaling is normalized exactly and metadata trailing incidence arrays are excluded from facet counts. Fifteen complete native types are reserved.

Which distance degeneracy information is sufficient to recover facet complexity without source facet lookup?

## Experimental contract

Ten exact pairwise distances permitted; source facets/incidence/f-vector forbidden predictors. None for exact geometric algorithms; training-only coefficients for coarse degeneracy heuristics.

The campaign completed 6 substantive hypotheses. Native bytes and exact sample anchors are preserved. Model selection uses whole-group development error and a 1% simplicity tolerance; selection and stopping were frozen before the separate no-fitting confirmation process. All outcomes are now exposed for future users.

## Main result and interpretation

Exact enumeration of feasible signed-spanning-tree Lipschitz potentials reproduces all reserved facet counts and agrees with an independent convex-hull control. This construction is established mathematics, independently implemented here.

$$
f(P_d)=\#\{\text{vertices of }\phi_0=0,\ |\phi_i-\phi_j|\leq d_{ij}\}
$$

The frozen numerical reference constructs the convex hull of the signed normalized edge vectors and counts distinct facet equations, rounded to nine decimals. Separately, attempt_004 enumerates exact signed-tree potentials satisfying all pairwise distance inequalities. Both reproduce the finite source counts. Their numerical and exact roles are distinct.

Neither construction has fitted coefficients. The supplied distances, exact rational scaling and full algorithms are explicit in run.py and rules.json.

## Performance and adverse evidence

| Model | Development MAE | Confirmation MAE |
|---|---:|---:|
| qhull | 0 | 0 |
| generic | 8.41935 | 6.93333 |
| attempt 004 | 0 | 0 |

MAE is averaged within each complete group and then equally over the 15 reserved groups (15 observations). Errors are in facets. Per-group RMSE, bias and failures are available in evidence/by_group.csv; small or dependent group counts do not support population confidence claims.

The lowest retrospective confirmation error belongs to qhull. It did not change the frozen selection. Equal tie count and equality-normal rank do not imply equal facet counts; the archived 52-versus 54 pair is an executable counterexample. Star-only potential enumeration misses facets.

## Value, limits and evaluation

A proposed scalar degeneracy description is falsified: two development metrics have the same five distance ties and equality-normal rank 3 but 52 and 54 facets. Restricting the exact construction to star trees also fails. These are precise finite counterexamples to tested simplifications, not a claim to a new classification theorem. The catalog is small and source-selected. Descriptor regression is an approximation; independent exact constructions already achieve zero error. No inference to larger metrics or theorem-level novelty is claimed.

Alternative agents can submit any predictor under this task's information budget. The shared evaluator reports task-unit errors, whole-group and worst-group results, coverage, abstention, optional intervals and meaningful event diagnostics. A different endpoint requires an independently reviewed new-task contract. Numerical success alone does not certify mechanism, novelty or deployed impact.

## Reproducibility and source

Run `python run.py` for the frozen reference replay. `rules.json` contains every fitted value; `task_spec.json` defines units and access; `evidence/` contains compact predictions and numerical evidence. Research history preserves all hypotheses, failed candidates, technical corrections and the first confirmation receipt.

Authoritative source: https://zenodo.org/records/19496811. Redistribution terms: cc-by-4.0. Primary-source prior-art searches and limitations are recorded in PRIOR_ART.json.
