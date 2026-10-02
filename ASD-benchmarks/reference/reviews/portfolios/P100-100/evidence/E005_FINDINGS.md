# Case 100: Mobile latency: a stronger causal history control

**Evidence status:** Retrospective development and exposed-group transfer assessment. All original cohorts are exposed. Original final results remain unchanged; no fresh confirmation or new physical law is claimed here.

## 1. Scenario and endpoint

The Vigo/Málaga platform measurements were collected on 20–22 November 2024 and released inJanuary 2025. Six original development PING runs cover three calibrated routes, with two constant-payload runs per route. There are 5965 assigned next-probe forecasts and 5938 finite RTT targets;27 missing targets remain assigned. The endpoint is successful-probe RTT in milliseconds. Every model can use five completed previous probes, their causal history summaries, payload and radio measurements available at the previous completion. Current response timestamps, row parity, ICMP sequence, target-derived counters and the current lost flag are not predictors.

## 2. Experimental method

Outer validation leaves one complete run out and trains on the other five; inner tuning also holds out complete runs. Past completed RTTs within a validation run are explicitly permitted online calibration, never a fit on future responses. The primary score averages within-run MAE equally across six runs. A fixed 50 ms threshold provides a supplementary illustrative decision diagnostic, not a claimed service requirement, deployment cost or packet-loss forecast. The mandatory two-probe-lag persistence comparator exposes a recurring history pattern that ordinary persistence misses.

## 3. Tested equation and interpretation

The strongest causal control is

$$\widehat r_n=r_{n-2},$$

where successful-probe RTT \(r_n\) is in milliseconds. The robust challenger is

$$\widehat r_n=r_{n-2}+b_c+\alpha(\overline r_{n-5:n-1}-r_{n-2})+\beta C\tanh\!\left(\frac{r_{n-1}-r_{n-3}}C\right)+\gamma\sigma_{n-5:n-1}+\delta[-90-\operatorname{RSRP}]_++\epsilon[-15-\operatorname{RSRQ}]_+.$$

Only completed past probes enter the history terms. Radio values are available at the previous completion. Every coefficient and trained robust-loss/clip parameter is in `cycle-002/model.json`; coefficient units follow their displayed inputs. Native completion spacing is about 0.1 s and lag-two correlations are 0.707–0.951 across the six development runs. That supports a recurring measurement/history pattern, not a proven network scheduler mechanism.

## 4. Performance and preserved alternatives

Selected compact candidate: `cycle-002`. Its development mae is **2.4771391 ms**, versus **2.422715 ms** for `baseline-lag2`. Physical-unit mean group error is 2.4771391 ms. All paired groups and counterexamples appear in `PAIRED_GROUP_EVIDENCE.csv` and `BY_SYSTEM.csv`. Descriptive leave-one-system-out sensitivity is reported without a population confidence claim.

| Cycle | Tested hypothesis family | Development error | Disposition |
|---|---|---:|---|
| cycle-001 | lag2 memory | 3.0003048 | Preserved alternative or failure |
| cycle-002 | bounded lag2 | 2.4771391 | Selected retrospective candidate |

### Retrospective transfer on the original exposed reserved groups

After selection and stopping were frozen, unchanged full-development states were evaluated on 3 original reserved groups (2943 assigned rows; 2942 finite targets). These targets were previously exposed. No fitting, reselection or fresh confirmation occurred. Errors use the same whole-group weighting as development; the acoustic normalization uses full-development condition means only.

| Frozen model | Primary error (ms) | Physical error (ms) |
|---|---:|---:|
| `cycle-002` | 1.720813 | 1.720813 |
| `baseline-flex` | 1.631070 | 1.631070 |
| `baseline-lag2` | 1.682686 | 1.682686 |
| `baseline-last` | 13.071518 | 13.071518 |
| `baseline-old` | 2.072309 | 2.072309 |
| `baseline-rolling` | 8.094475 | 8.094475 |

The extra bounded terms lose to lag-two persistence in all three reserved runs. The flexible comparator is also stronger, with 1.631070 ms MAE. At the fixed illustrative 50 ms threshold, the candidate and lag-two control have identical mean group classification error (3.425%). One missing native RTT is excluded from error scoring and remains in assigned-row coverage. No service deadline, fabricated lost-packet RTT or deployment benefit is asserted.

Scores and individual counterexamples are in `retrospective_transfer/metrics.csv`, `by_group.csv` and `paired_group_evidence.csv`. The frozen development record remains in `CASE_RESULT.json`; exposed-group results are an append-only `TRANSFER_ADDENDUM.json`.

## 5. Value, limitations and next experiment

The robust challenger is 2.246% worse than lag-two persistence and loses on every development run. The simpler control changes the interpretation of earlier history-model gains. The value is a stronger reproducible comparator and a clear falsification of unnecessary correction terms; no queue law, scheduler cause or deployment advantage is admitted.

The next independent experiment should address: A fresh campaign with randomized probe spacing/payload order, logged request/send/completion times and reserved routes/days/networks. Compare lag 2, adjacent persistence and causal features under varied probe periods; freeze a real service deadline and measure actual operational utility.

## 6. Reproduction and assessment

From this folder, run `python cycle-002/run.py` to replay frozen outer-fold predictions. Submit other agents’ predictions with `python score.py --predictions predictions.csv --out evaluation-new`. This task-specific evaluator checks exact IDs/groups, missing outcomes and abstention coverage, then compares baselines on identical scored rows. It does not certify scientific mechanism or novelty. See `EVALUATION_CONTRACT.md`, `PROTOCOL.json` and `HYPOTHESIS_LEDGER.json`.

Source and prior art: [source 1](https://zenodo.org/records/14635635).
