# P100-005: Stable-set certificates and a degenerate accuracy task

## Scenario and question

The authoritative replacement source contains 4107 obstruction graphs grouped into 168 source implication families. Exact independent-set enumeration reconstructs the target. The fixed split reserves 36 complete families.

Which cheap structural bounds can certify stable-set cardinality on difficult LS+ obstruction graphs?

## Experimental contract

Full graph adjacency is permitted; certificate facet coefficients and published ranks are forbidden predictors. None for deterministic bounds; source-independent exhaustive bitset search supplies labels. Labels are computable mathematical invariants, not physical measurements.

The campaign completed 6 substantive hypotheses. Native bytes and exact sample anchors are preserved. Model selection uses whole-group development error and a 1% simplicity tolerance; selection and stopping were frozen before the separate no-fitting confirmation process. All outcomes are now exposed for future users.

## Main result and interpretation

Every eligible graph has independence number 4. A training-only constant therefore attains zero error, as does independent exact enumeration. That perfect score provides no evidence for a newly discovered general graph rule.

$$
\widehat\alpha=4,\qquad \alpha(G)\leq\lfloor U_{\mathrm{LP}}(G)\rfloor
$$

The exact executable expression is: y_hat = training-fold median(target); final coefficient refit on development only.

Parameters: b[0] = 4. Coefficient ordering follows run.py and rules.json.

## Performance and adverse evidence

| Model | Development MAE | Confirmation MAE |
|---|---:|---:|
| constant | 0 | 0 |
| edge lp | 2 | 2 |
| exact | 0 | 0 |

MAE is averaged within each complete group and then equally over the 36 reserved groups (391 observations). Errors are in vertices. Per-group RMSE, bias and failures are available in evidence/by_group.csv; small or dependent group counts do not support population confidence claims.

The lowest retrospective confirmation error belongs to constant. It did not change the frozen selection. Prediction at the midpoint of lower and upper bounds is not a logically valid stable-set certificate, even when its average numerical error decreases.

## Value, limits and evaluation

The substantive investigations compare degree, inertia, clique-partition and polyhedral certificates. Triangle and induced-five-cycle inequalities tighten the classical LP bound, while midpoint prediction can reduce error without being a valid certificate. These distinctions are useful for evaluating future mathematical claims. This finite, deliberately selected obstruction family is not a representative graph distribution. Classical bounds and exact enumeration are reproductions. A prediction must not be mistaken for a proof or extrapolated to arbitrary graphs.

Alternative agents can submit any predictor under this task's information budget. The shared evaluator reports task-unit errors, whole-group and worst-group results, coverage, abstention, optional intervals and meaningful event diagnostics. A different endpoint requires an independently reviewed new-task contract. Numerical success alone does not certify mechanism, novelty or deployed impact.

## Reproducibility and source

Run `python run.py` for the frozen reference replay. `rules.json` contains every fitted value; `task_spec.json` defines units and access; `evidence/` contains compact predictions and numerical evidence. Research history preserves all hypotheses, failed candidates, technical corrections and the first confirmation receipt.

Authoritative source: https://zenodo.org/records/15483991. Redistribution terms: cc-by-4.0. Primary-source prior-art searches and limitations are recorded in PRIOR_ART.json.
