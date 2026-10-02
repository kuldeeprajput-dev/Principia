# Causal contribution forecasts in asymmetric threshold public-goods games

## Scenario and task

Causal contribution forecasts in asymmetric threshold public-goods games. Native measurements come from [the authoritative source](https://zenodo.org/records/16918146). Complete first-session interacting pair;20% hash heldout in each treatment; remaining groups in 5 deterministic whole-pair folds. Both players remain together.

One-step prediction before round 3..20 using strictly prior own/peer contributions and publicly announced rules. Earlier confirmation responses are permitted causal online history, never fitted parameters. Surveys and session 2 excluded.

## Experimental method

5 substantive development attempts tested distinct dynamic, mechanistic or ablation hypotheses. Selection used equally weighted whole-group MAE, with a 1% simpler-model tie rule. Baseline fitting and preparation did not count as attempts. All states and stopping were frozen before a separate confirmation command; confirmation never changed the reference.

Schema inspection exposed first two full-equality pairs and their duplicate records. Exact overlap with hash confirmation recorded; no aggregate confirmation metrics before freeze.

## Reference equation and interpretation

$$
\widehat c_{i,t}=c_{i,t-1},\qquad 0\leq c_{i,t}\leq e_i.
$$

c is an individual contribution in experimental tokens, e is their announced per-round endowment, i indexes players and t is round 3-20. This forecast uses the previous round observed before the next decision. It is persistence, not an equilibrium derivation or a causal policy rule.

Full-precision coefficients and all comparator states are in `rules.json`. 

<!-- pagebreak -->

## Findings and performance

Persistence is the development-selected reference: MAE 0.768894 tokens on 222 development pairs and 0.364646 on 55 reserved pairs. The lag-two mean gives 0.422980 tokens, the flexible quadratic control 0.601943, and the best post-hoc mechanistic candidate 0.387530. The outcome supports a strong simple benchmark; it does not establish a new behavioral law.

| Frozen model | Confirmation MAE (experimental tokens) |
|---|---:|
| reference | 0.364646 |
| baseline persistence | 0.364646 |
| baseline lag 2 mean | 0.42298 |
| baseline half endowment | 1.70253 |
| baseline flexible | 0.601943 |

All candidate results and per-group errors remain in `evidence/metrics.csv` and `evidence/by_group.csv`. The reference is the preselected model, not the retrospectively best confirmation model. No error is converted into invented percentage accuracy.

## Value, limits and negative evidence

Session 2 reuses the same participants and is excluded; Type 2 sheets duplicate the canonical Type 1 interaction records. Both players and every retained round stay in the same pair split. Post-game survey preferences are unavailable at prediction time and excluded. Groups are from one experimental program, and repeated rounds are not independent people. Later individual behavior is observed causally for subsequent one-step forecasts; this is not an open-loop 20-round trajectory test.

Remove duplicated interaction representations and reused participants before splitting. Persistence is a necessary strong control in repeated-choice data. Do not confuse deterministic payoff/threshold formulas with discoveries about measured decisions. Keep one-step online information distinct from multi-step forecasting.

## Reproduction and sources

Run `python run.py` inside this final package to verify its manifest and replay every frozen model. `rules.json` defines the exact coefficients, permitted input columns and units. `task_spec.json` and the shared evaluator provide the evaluation contract; valid alternative equations need not resemble these references.

Original study: [https://doi.org/10.1073/pnas.2525760123](https://doi.org/10.1073/pnas.2525760123). The source paper analyzes equilibrium, reciprocity, relative contributions and coordination. We compare causal forecasts beyond these mechanisms, without claiming a new universal behavioral law.
All packaged outcomes are exposed to future users. Agent review is computational/scientific criticism, not independent experimental replication or proof of novelty.
