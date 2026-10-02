# P100-100.original.v1

**Target.** Next successful ICMP probe RTT

**Units.** ms

**Error units.** ms

**Primary metric.** mae

**Primary metric units.** ms

**Cohort.** P100-100.original.v1.cohort-1

**Prediction time.** Predict next probe RTT using only five previous completed RTTs and radio asof previous completion, <=0.5s old. No current response-completion timestamp, ICMPseq, cumulative average/loss, future gap, throughput or same-probe radio in inputs. Successful response conditional target; missing lost responses retained when inputs eligible.

**Independent unit.** whole PING run; sequential packets correlated

**Hierarchy.** group

**Calibration and history.** r_n and r_(n−1) are completed previous RTTs in milliseconds; rbar5 averages the last five completed probes. c_q in ms is−0.002897 for indoor random,−0.069945 for indoor rectangle and−0.049676 for outdoor rectangle. The55ms breakpoint was selected using nested development groups. Payload and causal radio measurements are available to comparators, but the selected equation uses history and the calibrated route offset only. It predicts a conditional successful next response, not a missing lost-packet RTT.

**Limits.** Three complete PING runs, one per calibrated route, one platform; online previous-probe calibration. No new-network or packet-loss reliability prediction.

**Historical exposure record.** All packaged targets are now exposed; future scoring is retrospective. First indoor-rectangle1000B file audit responses viewed; this complete file excluded from reserved allocation. Metadata hash chooses one run per route from remaining source-defined runs.

**Current exposure.** All outcomes exposed; future scoring is retrospective.

**Source scope.** original_corpus

**Source.** https://zenodo.org/records/14635635

**Source terms.** cc-by-4.0

## Permitted prediction inputs

| Variable | Unit / interpretation |
|---|---|
| `route` | calibrated route label |
| `payload_B` | B |
| `last_rtt` | ms,previous completion |
| `mean5_rtt` | ms,previous5 completions |
| `mean3_rtt` | ms,previous3 completions |
| `trend_rtt` | ms,previous RTT difference |
| `RSRP` | dBm,asof previouscompletion |
| `RSRQ` | dB,asof previouscompletion |

Identifiers and source locators are alignment metadata. They may route documented frozen calibration states; they are not a license to look up a scored target. Additional columns outside this list are not predictors.

## Reproduction and comparison

`run.py` and `rules.json` contain executable frozen equations and every coefficient. `evidence/metrics.csv` and `evidence/predictions.csv.gz` preserve the historical comparisons. The shared evaluator recalculates them and compares submitted predictions on identical covered observations. Model IDs are local to this task and are distinct from finding IDs.

Primary aggregation and eligible observations are frozen. Excluded/nonpositive log targets are reported separately from physical-unit error. Uncertainty is described at independent-group level; no row bootstrap is used. The raw adapter emits native anchors, eligibility, calibration and group records. Preparation does not fit or tune a model.

Default reference: `reference`. Comparator models: `reference`, `challenger`, `baseline_persistence`, `baseline_rbf`, `baseline_residual_rbf`, `baseline_rolling`, `baseline_static`.

Use `python evaluation/benchmark.py example --task P100-100.original.v1 --output NEW_FOLDER` from the benchmark root. Historical development/confirmation separation cannot be reused as a fresh holdout after exposure.
