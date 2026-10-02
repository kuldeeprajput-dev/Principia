# Screw driving: a six-coefficient engagement-history approximation

**P100-053 · Continuation of 30 September 2026 · 2 substantive cycles**

A six-coefficient equation compresses the earlier multi-branch history model into a readable operational approximation. Its mean workpiece error is slightly worse than a newly refitted, equally informed tree comparator. A disturbance-reset hypothesis adds complexity without improving grouped development error. This is a measured accuracy–simplicity tradeoff, not a discovered friction mechanism.

## Scientific task and information access

The original surface-friction campaign contains 250 workpieces with two holes and repeated use under eight conditions. The continuation fits on 200 original-development workpieces using the frozen five stratified workpiece folds. Both holes and every reuse cycle remain linked. Fifty previously exposed workpieces are diagnostic only.

The current operation stops at the first native acquisition sample with relative thread-forming angle ≥250 degrees; the sampled overshoot is included. The earlier Finding phase is allowed. Prior late torque is available only after completed same-hole operations. Surface labels and controller OK/NOK outputs are excluded. The target is angle-mean thread-forming torque from 700–1300 degrees, not joint strength or clamping force.

All original development and confirmation outcomes were exposed before this continuation. Development comparisons are grouped retrospective experiments. The original confirmation partition is scored once after candidate choice and stopping are frozen, solely to inspect transfer. It supplies no fresh independent confirmation and does not determine a new winner. Existing final-results packages remain unchanged.

## Hypotheses and experimental method

**Cycle 1: Bounded retained engagement state.**

`T=early+b0+bE*has_history*(prev_y-prev_early)+bF*(finding-early)+bq/(1+usage)+bL*left+bV*I(usage=0); 0<=bE<=1,bq>=0`

Development primary error: 0.0244117 Nm. Retrospective operational candidate; not admitted physical law.

**Cycle 2: Disturbance resets engagement memory.**

`T=cycle001 with state multiplied by exp(-abs(early-prev_early)/(k*(abs(prev_early)+0.05Nm))) and added causal gradient innovation`

Development primary error: 0.0244366 Nm. Not selected; retained with counterexamples.

All learned normalization, missing-value medians and model coefficients are fitted inside each training partition. Shape parameters use nested whole-group validation. Chronological validation is used when the task predicts later dates. Eight fixed robust fitting iterations use group-balanced weights. The flexible model uses the same expanded inputs and refits inside every outer fold. RBF tuning is also nested where used. Failed constraints, competing explanations and technical failures remain traceable.

## Complete numerical comparison

Errors are in **Nm**; lower is better. Mean MAE across complete workpieces. Current missing targets are excluded only from scoring, and original eligibility is retained. None of these regression metrics is classification accuracy.

| Model | Development error | Exposed original-confirmation error |
|---|---:|---:|
| simple | 0.0245044 | 0.0235999 |
| linear | 0.0237966 | 0.0227325 |
| flexible | 0.0229473 | 0.0222525 |
| cycle1 | 0.0244117 | 0.0237515 |
| cycle2 | 0.0244366 | 0.0236959 |
| unconstrained1 | 0.0244117 | 0.0237515 |
| unconstrained2 | 0.0244366 | 0.0236959 |


The frozen candidate is **cycle1**. On development it has 6.38% higher error than the strongest matched control **flexible**, winning 52 of 200 groups. After the freeze, the exposed original-confirmation comparison finds 6.74% higher error than the descriptively best control **flexible**, with 12 of 50 group wins. Every group, including losses, appears in `CONTROL_ANALYSIS.json` and `exposed-confirmation/by_group.csv`. This diagnostic comparison does not change the development selection.



The earlier frozen selected rule had error 0.0231636; this continuation selected rule has error 0.0237515 on the same exposed target groups (-2.54% relative reduction; a negative value means deterioration). Predictor access or representation changed, so this comparison does not isolate a physical mechanism. Exact earlier scores and source hashes are in `OLD_REFERENCE_COMPARISON.json`.

## Executable selected equation

Full-development shape: `1.0`. Exact coefficients, training-only transform states and every fold model are in `results-v2/cycle1/`. The equation above defines the basis; each coefficient carries the units required to yield the target. Where a logarithm, exponent or shape ratio appears, its argument is dimensionless as specified in the protocol.

| Coefficient | Full-development value |
|---|---:|
| offset_Nm | 0.00675272861 |
| retained_engagement_fraction | 0.383527741 |
| finding_to_early_fraction | -0.0271184417 |
| reuse_amplitude_Nm | 0.130270785 |
| left_offset_Nm | -0.0161557975 |
| virgin_offset_Nm | 0.137902102 |


Fold shapes, coefficient ranges and collapses at imposed bounds are recorded in `PARAMETER_STABILITY.json`. They are identifiability diagnostics, not measurements of physical constants. Zero coefficients and missingness terms remain explicit.

## Contribution, limits and next experiment

The simple equation offers an auditable early-to-late torque estimator and a controlled compression example. It requires completed same-hole warm-start information; first-operation behavior is explicitly represented. No production alarm accuracy, scrap reduction, joint reliability or closed-loop control improvement was measured.

The six-coefficient approximation does not beat the strongest matched predictor. Reduced parameter count is a tradeoff rather than predictive superiority.

Friction, geometry, wear, material and station effects are not separately measured or identified. The retained-state coefficient is an operational parameter.

Original-development scoring has 9,895 eligible operations; the 105 unavailable late windows cannot be extrapolated. Original confirmation has 2,473 of 2,500 assigned operations.

Timestamp origin and timezone are unspecified. All included historical targets were independently checked using conservative start-or-completion bounds with one-second uncertainty.

Fresh natural-degradation S01 responses were not acquired. The author GitHub tree exposes labels, not the required raw torque traces; a truncated label download is not admitted evidence.

**Next independent experiment.** Use the frozen S01 adapter on the complete official natural-degradation archive. Exclude every old S02 workpiece and byte-identical operation before scoring. The fixed selected six-coefficient model and all matched baselines must be evaluated once without refitting. If stations/materials differ, report transfer limits rather than recasting the cohort.

## Evidence and replay

Read `CASE_RESULT.json` for the integration record, `HYPOTHESIS_LEDGER.json` for revisions, `LESSONS.md` for actionable experience and `PRIOR_ART.json` for literature scope. `data/sample_anchors.csv.gz` links predictions to source rows, native members, time bounds or workbook cells. `INPUT_AUDIT.json` verifies frozen preparation, group separation, current-target poisoning, source hashes and preservation of existing final results.

From this continuation folder, run:

```sh
python run.py replay --output results-v2
python verify_inputs.py
python verify_exposed.py
```

Replay recomputes saved predictions and metrics without refitting. `evaluate_exposed.py` is the preserved one-shot diagnostic scorer and refuses an existing output directory; its result is already frozen. Numerical evidence is computational review, not independent experimental replication or expert adjudication. No physical law or ground-truth novelty claim is admitted by this continuation.

Primary sources: [https://arxiv.org/abs/2505.11925](https://arxiv.org/abs/2505.11925), [https://github.com/nikolaiwest/pyscrew](https://github.com/nikolaiwest/pyscrew). Their specific relevance and access limits are disclosed in `PRIOR_ART.json`.
