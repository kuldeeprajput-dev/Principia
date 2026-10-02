# P100-001: Exact-prefix sequence extrapolation

## Scenario and question

The OEIS integer snapshot is sampled by a fixed accession hash. Each eligible sequence supplies16 exact prefix terms and one five-step-ahead target. Affine-equivalent observed prefixes are linked before splitting. Sequence names and source descriptions are excluded from prediction.

When can compact exact arithmetic hypotheses extrapolate a prefix, and where do they fail?

## Experimental contract

Only first16 terms and horizon5 supplied; names, OEIS IDs and published formulas are forbidden predictors. Sixteen observed prefix terms per sequence, including confirmation sequences; no suffix term used in rules.

The campaign completed 7 substantive hypotheses. Native bytes and exact sample anchors are preserved. Model selection uses whole-group development error and a1% simplicity tolerance; selection and stopping were frozen before the separate no-fitting confirmation process. All outcomes are now exposed for future users.

## Main result and interpretation

Seven exact-family investigations test finite differences, recurrences, residue classes, rational ratios, polynomial forcing, a cascade and an internal falsification gate. They do not beat the constrained learned comparator on the primary signed-asinh endpoint. Exact prefix agreement is compatible with many incompatible continuations; it is not a proof of an integer-sequence law.

The reference uses a Gaussian radial-basis residual of all16 prefix terms in signed-asinh coordinates; the baseline is the last observed transformed term. Exact recognizers and their failed continuations remain separate scientific evidence.

The exact executable expression is: Frozen 24-center Gaussian radial-basis ridge comparator; all feature means, scales, centers, coefficients and ridge=0.3 are in rules.json. Additive residual for cases2/3/4/45; multiplicative clipped-log ratio for cases11/46..

Parameters: 25 frozen coefficients, feature scaling and centers are listed in rules.json; no hidden fitted state. Coefficient ordering follows run.py and rules.json.

## Performance and adverse evidence

| Model | Development MAE | Confirmation MAE |
|---|---:|---:|
| rbf | 2.02965 | 2.23335 |
| persist | 3.08003 | 3.35643 |

MAE is averaged within each complete group and then equally over the 474 reserved groups (479 observations). Errors are in asinh(integer term). Per-group RMSE, bias and failures are available in evidence/by_group.csv; small or dependent group counts do not support population confidence claims.

The lowest retrospective confirmation error belongs to rbf. It did not change the frozen selection. Seven exact-prefix families remain worse than the learned comparator on the declared transformed endpoint; a formula that fits the prefix is not confirmed as an infinite rule.

## Value, limits and evaluation

A radial-basis residual predictor is retained as the numerical reference. This provides a challenging open extrapolation task and preserves exact mathematical counterexamples, but it does not establish new combinatorial principles. A finite prefix cannot uniquely identify an infinite sequence. Related OEIS families beyond the linked affine prefixes can remain dependent. Very large integers are scored in signed-asinh coordinates, not as a percentage of exact integer matches.

Alternative agents can submit any predictor under this task's information budget. The shared evaluator reports physical-unit errors, whole-group and worst-group results, coverage, abstention, optional intervals and meaningful event diagnostics. A different endpoint requires an independently reviewed new-task contract. Numerical success alone does not certify mechanism, novelty or deployed impact.

## Reproducibility and source

Run `python run.py` for the frozen reference replay. `rules.json` contains every fitted value; `task_spec.json` defines units and access; `evidence/` contains compact predictions and numerical evidence. Research history preserves all hypotheses, failed candidates, technical corrections and the first confirmation receipt.

Authoritative source: https://oeis.org/wiki/Download. Redistribution terms: CC BY-SA 4.0. Primary-source prior-art searches and limitations are recorded in PRIOR_ART.json.
