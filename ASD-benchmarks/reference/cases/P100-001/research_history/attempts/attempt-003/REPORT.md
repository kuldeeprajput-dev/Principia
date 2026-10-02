# Quasipolynomial

Many arithmetic sequences are polynomial only within residue classes. Test independently exact degree<=2 residue-class continuations for periods2–4, with all classes checked on the observed prefix.

This hypothesis/configuration was recorded before execution. Selection uses development data only. Every failure remains part of scientific history.

## Executable candidate

a(n)=p_(n mod m)(n), m in {2,3,4}, each residue polynomial degree<=2.

Coefficients: [].

## Grouped development evidence

Mean-group MAE 3.07023677 asinh(integer term); worst-group MAE 85.4564652. Preserved alternative; not the selected reference.

## Falsification and interpretation

Seven exact-family investigations test finite differences, recurrences, residue classes, rational ratios, polynomial forcing, a cascade and an internal falsification gate. They do not beat the constrained learned comparator on the primary signed-asinh endpoint. Exact prefix agreement is compatible with many incompatible continuations; it is not a proof of an integer-sequence law. A finite prefix cannot uniquely identify an infinite sequence. Related OEIS families beyond the linked affine prefixes can remain dependent. Very large integers are scored in signed-asinh coordinates, not as a percentage of exact integer matches.

Parameter sensitivity is in parameter_sensitivity.json. Fold extrema are descriptive, not population confidence intervals. All validation/training group memberships are retained in metrics.json and SCIENTIFIC_CHECKS.json.

## Replay

Run `python develop.py PATH_TO_LOCAL_DATAS attempts/attempt-003` only in a new exploratory workspace; the script refuses to overwrite completed evidence. The current confirmation outcomes are exposed. Frozen prediction replay is `python run.py` inside final_results.
