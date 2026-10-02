# BLE radio-map drift: exact power redistribution

**P100-092 · Continuation of 30 September 2026 · 2 substantive cycles**

Replacing the old linearized power-addition approximation with an exact positive-power redistribution produces a compact three-parameter correction. It improves the earlier compact rule on both forward development dates and exposed future dates, but remains weaker than the refitted flexible comparator. It is a readable calibrated-map response relation, not an identified propagation law or a localization result.

## Scientific task and information access

Five original-development dates are prepared. The three outer forward-validation dates have calendar elapsed days 14, 22 and 29, and inner tuning uses earlier dates only. All furniture states stay with a date. The previously exposed dates at elapsed days 51, 86 and 94 are diagnostic only.

The initial 3,120-cell measured radio map at all 130 positions, eight ports and three channels is explicitly available. The global power reference is 10log10(mean across positions of 10^(initial RSSI/10)) per port/channel, computed exclusively from that initial map. Known furniture, date/antenna/channel metadata are allowed to matched controls. No response or offset from a target date is supplied.

All original development and confirmation outcomes were exposed before this continuation. Development comparisons are grouped retrospective experiments. The original confirmation partition is scored once after candidate choice and stopping are frozen, solely to inspect transfer. It supplies no fresh independent confirmation and does not determine a new winner. Existing final-results packages remain unchanged.

## Hypotheses and experimental method

**Cycle 1: Exact positive-power redistribution.**

`RSSI=10log10((1-lambda)*10^(r0/10)+lambda*10^(calibrated_global_port_channel_power/10))+b0+bf*furniture; 0<=lambda<=1`

Development primary error: 3.48789 dB. Retrospective operational candidate; not admitted physical law.

**Cycle 2: Finite orthogonal contrast response.**

`RSSI=r0+b0+bf*furniture+bc_f*tanh(channel_contrast/k)+bs_f*tanh(position_contrast/k), bc_f,bs_f<=0`

Development primary error: 3.62207 dB. Not selected; retained with counterexamples.

All learned normalization, missing-value medians and model coefficients are fitted inside each training partition. Shape parameters use nested whole-group validation. Chronological validation is used when the task predicts later dates. Eight fixed robust fitting iterations use group-balanced weights. The flexible model uses the same expanded inputs and refits inside every outer fold. RBF tuning is also nested where used. Failed constraints, competing explanations and technical failures remain traceable.

## Complete numerical comparison

Errors are in **dB**; lower is better. Mean within-date burst-cell MAE, equal chronological dates. Current missing targets are excluded only from scoring, and original eligibility is retained. None of these regression metrics is classification accuracy.

| Model | Development error | Exposed original-confirmation error |
|---|---:|---:|
| simple | 3.80045 | 3.92336 |
| linear | 3.53537 | 3.62404 |
| flexible | 3.34806 | 3.4389 |
| cycle1 | 3.48789 | 3.5813 |
| cycle2 | 3.62207 | 3.66667 |
| unconstrained1 | 3.48789 | 3.5813 |
| unconstrained2 | 3.62207 | 3.66667 |


The frozen candidate is **cycle1**. On development it has 4.18% higher error than the strongest matched control **flexible**, winning 0 of 3 groups. After the freeze, the exposed original-confirmation comparison finds 4.14% higher error than the descriptively best control **flexible**, with 0 of 3 group wins. Every group, including losses, appears in `CONTROL_ANALYSIS.json` and `exposed-confirmation/by_group.csv`. This diagnostic comparison does not change the development selection.



The earlier frozen selected rule had error 3.68956; this continuation selected rule has error 3.5813 on the same exposed target groups (2.93% relative reduction; a negative value means deterioration). Predictor access or representation changed, so this comparison does not isolate a physical mechanism. Exact earlier scores and source hashes are in `OLD_REFERENCE_COMPARISON.json`.

## Executable selected equation

Full-development shape: `0.1`. Exact coefficients, training-only transform states and every fold model are in `results-v2/cycle1/`. The equation above defines the basis; each coefficient carries the units required to yield the target. Where a logarithm, exponent or shape ratio appears, its argument is dimensionless as specified in the protocol.

| Coefficient | Full-development value |
|---|---:|
| offset_dB | -0.740888794 |
| furniture_offset_dB | -0.219292485 |


Fold shapes, coefficient ranges and collapses at imposed bounds are recorded in `PARAMETER_STABILITY.json`. They are identifiability diagnostics, not measurements of physical constants. Zero coefficients and missingness terms remain explicit.

## Contribution, limits and next experiment

The exact correction improves the readability and performance of a compact calibrated-map comparator without target-date recalibration. It could support future recalibration studies, but no reduced calibration schedule, localization accuracy or deployment saving was tested.

The 3,120-cell initial calibration map is part of information access; three fitted parameters do not make the model calibration-free.

Power redistribution is an empirical positive-power ensemble. It does not mean simultaneously mixing different carrier channels or separating multipath, receiver drift and environmental change.

Every position was calibrated previously. This is temporal transfer at known positions in one installation, not unseen-position localization.

Three diagnostic dates have few independent temporal units; burst packet counts do not create independent environments. Native day labels differ from calendar time, and the actual timestamps are retained.

The flexible comparator is more accurate; the compact relation is a transparency–accuracy tradeoff, not the strongest predictive discovery.

**Next independent experiment.** Freeze the exact redistribution relation and flexible comparator before collecting new dates and another installation with separately declared initial calibration. Add device/receiver stability checks and a downstream localization evaluation if recalibration savings are the scientific target.

## Evidence and replay

Read `CASE_RESULT.json` for the integration record, `HYPOTHESIS_LEDGER.json` for revisions, `LESSONS.md` for actionable experience and `PRIOR_ART.json` for literature scope. `data/sample_anchors.csv.gz` links predictions to source rows, native members, time bounds or workbook cells. `INPUT_AUDIT.json` verifies frozen preparation, group separation, current-target poisoning, source hashes and preservation of existing final results.

From this continuation folder, run:

```sh
python run.py replay --output results-v2
python verify_inputs.py
python verify_exposed.py
```

Replay recomputes saved predictions and metrics without refitting. `evaluate_exposed.py` is the preserved one-shot diagnostic scorer and refuses an existing output directory; its result is already frozen. Numerical evidence is computational review, not independent experimental replication or expert adjudication. No physical law or ground-truth novelty claim is admitted by this continuation.

Primary sources: [https://www.nature.com/articles/s41597-025-04581-0](https://www.nature.com/articles/s41597-025-04581-0), [https://doi.org/10.1016/j.iot.2025.101732](https://doi.org/10.1016/j.iot.2025.101732). Their specific relevance and access limits are disclosed in `PRIOR_ART.json`.
