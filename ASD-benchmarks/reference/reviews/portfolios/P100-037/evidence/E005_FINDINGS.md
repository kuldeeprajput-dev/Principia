# Router power: positive component constraints versus operational accuracy

**P100-037 · Continuation of 30 September 2026 · 2 substantive cycles**

Nonnegative workload components repair the previous negative standalone throughput coefficient, but they do not outperform the equally informed flexible predictor. The stronger fold-refitted tree model supplies a useful retrospective power-estimation comparator. No independent per-packet or byte-processing energy cost is identified.

## Scientific task and information access

Ten complete original-development runs, from five router/protocol combinations and repetitions 1–2. Outer and inner validation hold out complete runs. The five already-exposed repetition-3 runs are scored only after stopping and selection freeze. Two measured router models limit hardware transfer.

Current measured throughput and packet size, and known router identity. Dimensionless u=B/(200 Gbit/s), q=[B/(8L)]/(10^8 packets/s). The effective packet rate is an algebraic proxy, not an independently measured quantity. No target-power history, future traffic, temperature or protocol identifiers enter prediction.

All original development and confirmation outcomes were exposed before this continuation. Development comparisons are grouped retrospective experiments. The original confirmation partition is scored once after candidate choice and stopping are frozen, solely to inspect transfer. It supplies no fresh independent confirmation and does not determine a new winner. Existing final-results packages remain unchanged.

## Hypotheses and experimental method

**Cycle 1: Nonnegative processing-cost state.**

`P=P0_router+a_router*u+b_router*q/(k+q)+c_router*u*q/(k+q), all component costs nonnegative`

Development primary error: 4.19072 W. Retrospective operational candidate; not admitted physical law.

**Cycle 2: Competing independent activation limits.**

`P=P0_router+a_router*(1-exp(-u/ku))+b_router*(1-exp(-q/kq)), nonnegative amplitudes`

Development primary error: 4.1835 W. Not selected; retained with counterexamples.

All learned normalization, missing-value medians and model coefficients are fitted inside each training partition. Shape parameters use nested whole-group validation. Chronological validation is used when the task predicts later dates. Eight fixed robust fitting iterations use group-balanced weights. The flexible model uses the same expanded inputs and refits inside every outer fold. RBF tuning is also nested where used. Failed constraints, competing explanations and technical failures remain traceable.

## Complete numerical comparison

Errors are in **W**; lower is better. Mean MAE across complete runs. Current missing targets are excluded only from scoring, and original eligibility is retained. None of these regression metrics is classification accuracy.

| Model | Development error | Exposed original-confirmation error |
|---|---:|---:|
| simple | 4.82093 | 4.63006 |
| linear | 5.00743 | 4.4737 |
| flexible | 3.45226 | 3.47462 |
| cycle1 | 4.19072 | 4.01845 |
| cycle2 | 4.1835 | 4.05819 |
| unconstrained1 | 4.0453 | 3.99301 |
| unconstrained2 | 4.31626 | 4.05819 |


The frozen candidate is **cycle1**. On development it has 21.39% higher error than the strongest matched control **flexible**, winning 0 of 10 groups. After the freeze, the exposed original-confirmation comparison finds 15.65% higher error than the descriptively best control **flexible**, with 0 of 5 group wins. Every group, including losses, appears in `CONTROL_ANALYSIS.json` and `exposed-confirmation/by_group.csv`. This diagnostic comparison does not change the development selection.



The earlier frozen selected rule had error 4.00588; this continuation selected rule has error 4.01845 on the same exposed target groups (-0.31% relative reduction; a negative value means deterioration). Predictor access or representation changed, so this comparison does not isolate a physical mechanism. Exact earlier scores and source hashes are in `OLD_REFERENCE_COMPARISON.json`.

## Executable selected equation

Full-development shape: `0.1`. Exact coefficients, training-only transform states and every fold model are in `results-v2/cycle1/`. The equation above defines the basis; each coefficient carries the units required to yield the target. Where a logarithm, exponent or shape ratio appears, its argument is dimensionless as specified in the protocol.

| Coefficient | Full-development value |
|---|---:|
| A:baseline_W | 704.432926 |
| A:byte_cost_W | 5.54000451 |
| A:packet_cost_W | 14.9996642 |
| A:interaction_W | 12.8196731 |
| B:baseline_W | 69.8924805 |
| B:byte_cost_W | 9.79273998 |
| B:packet_cost_W | 0.757259322 |
| B:interaction_W | 3.22095238 |


Fold shapes, coefficient ranges and collapses at imposed bounds are recorded in `PARAMETER_STABILITY.json`. They are identifiability diagnostics, not measurements of physical constants. Zero coefficients and missingness terms remain explicit.

## Contribution, limits and next experiment

A power estimator can support offline workload accounting studies. The improved tree comparator reduces retrospective reserved-run error relative to the earlier flexible workload comparator. It does not demonstrate energy saving, controller benefit, or a physical processing-cost decomposition.

Byte load and the packet-rate proxy are coupled by the traffic design; positive regression coefficients alone do not identify independent energy costs.

Only two routers and five repeated combinations are measured. Mixed-flow mean packet size hides packet distributions.

Native timestamps include an old inconsistency; no thermal sensor supports a memory or heat mechanism. This continuation deliberately tests static hypotheses.

Seven development power targets and one exposed-confirmation target are missing; they remain assigned and are not imputed.

**Next independent experiment.** Collect new router units and repeated traffic sweeps with power-meter repeatability, temperature and processing counters. Freeze static and dynamic alternatives before obtaining new response measurements.

## Evidence and replay

Read `CASE_RESULT.json` for the integration record, `HYPOTHESIS_LEDGER.json` for revisions, `LESSONS.md` for actionable experience and `PRIOR_ART.json` for literature scope. `data/sample_anchors.csv.gz` links predictions to source rows, native members, time bounds or workbook cells. `INPUT_AUDIT.json` verifies frozen preparation, group separation, current-target poisoning, source hashes and preservation of existing final results.

From this continuation folder, run:

```sh
python run.py replay --output results-v2
python verify_inputs.py
python verify_exposed.py
```

Replay recomputes saved predictions and metrics without refitting. `evaluate_exposed.py` is the preserved one-shot diagnostic scorer and refuses an existing output directory; its result is already frozen. Numerical evidence is computational review, not independent experimental replication or expert adjudication. No physical law or ground-truth novelty claim is admitted by this continuation.

Primary sources: [https://zenodo.org/records/17282065](https://zenodo.org/records/17282065), [https://github.com/MMB-UPM/Router_Power_Consumption_ML/blob/main/CITATION.cff](https://github.com/MMB-UPM/Router_Power_Consumption_ML/blob/main/CITATION.cff). Their specific relevance and access limits are disclosed in `PRIOR_ART.json`.
