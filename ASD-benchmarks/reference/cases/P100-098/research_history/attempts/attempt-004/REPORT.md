# Polar

A facet is dual to a feasible Lipschitz-potential vertex. Enumerate signed spanning-tree tight constraints with exact integer-scaled distances, deduplicate potentials, and compare to nativefacet counts. This is an independently implemented established construction, not a new theorem.

This hypothesis/configuration was recorded before execution. Selection uses development data only. Every failure remains part of scientific history.

## Executable candidate

f=number of distinct exact feasible potentials phi with phi_0=0 and abs(phi_i-phi_j)<=d_ij; enumerate all signed spanning trees.

Coefficients: [].

## Grouped development evidence

Mean-group MAE 0 facets; worst-group MAE 0. Preserved alternative; not the selected reference.

## Falsification and interpretation

Exact enumeration of feasible signed-spanning-tree Lipschitz potentials reproduces all reserved facet counts and agrees with an independent convex-hull control. This construction is established mathematics, independently implemented here. The catalog is small and source-selected. Descriptor regression is an approximation; independent exact constructions already achieve zero error. No inference to larger metrics or theorem-level novelty is claimed.

Parameter sensitivity is in parameter_sensitivity.json. Fold extrema are descriptive, not population confidence intervals. All validation/training group memberships are retained in metrics.json and SCIENTIFIC_CHECKS.json.

## Replay

Run `python develop.py PATH_TO_LOCAL_DATAS attempts/attempt-004` only in a new exploratory workspace; the script refuses to overwrite completed evidence. The current confirmation outcomes are exposed. Frozen prediction replay is `python run.py` inside final_results.
