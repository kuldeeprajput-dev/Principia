# Microplastic interface transit: causal windows and a failed transport correction

**P100-067 · Continuation of 30 September 2026 · 2 substantive cycles**

Neither the new dimensionless interface-energy/size correction nor the upstream slowdown/variability correction transfers reliably enough to establish a transport law. The selected slowdown correction fails the elementary constant-speed approximation on the three already-exposed diagnostic configurations. The strongest development kernel predictor also transfers poorly. The main contribution is a clear counterexample and a correctly scoped calibration-dependent task.

## Scientific task and information access

Six complete original-development fluid configurations, each holding all trajectory replicates and particle categories together. Outer and inner validation hold out complete configurations. The primary metric first balances particle categories within each configuration, then weights configurations equally. Three previously exposed configurations are diagnostic only.

Only native trajectory rows available before the first sample beyond the boundary 2 mm upstream of the measured interface are used. Upstream slope and near/far speeds use actual available rows, with declared fallback windows. Longest particle dimension is allowed; ambiguous thickness and unmeasured normal stress are excluded. Source density-profile interface boundaries are declared calibration inputs with unresolved measurement timing.

All original development and confirmation outcomes were exposed before this continuation. Development comparisons are grouped retrospective experiments. The original confirmation partition is scored once after candidate choice and stopping are frozen, solely to inspect transfer. It supplies no fresh independent confirmation and does not determine a new winner. Existing final-results packages remain unchanged.

## Hypotheses and experimental method

**Cycle 1: Interface energy/size dimensionless response.**

`T=(h/vup)*exp(bR*log1p(Ri)+bL*log1p(h/longest)); Ri=9.81m/s2*(delta_density/(1000kg/m3))*h/vup2; bR,bL>=0`

Development primary error: 0.528587 absolute log ratio. Not selected; retained with counterexamples.

**Cycle 2: Conservative observed slowdown and orientation variability.**

`T=(h/vup)*exp(bS*max(0,-log(vnear/vfar))+bD*orientation_dispersion); bS,bD>=0`

Development primary error: 0.470794 absolute log ratio. Retrospective operational candidate; not admitted physical law.

All learned normalization, missing-value medians and model coefficients are fitted inside each training partition. Shape parameters use nested whole-group validation. Chronological validation is used when the task predicts later dates. Eight fixed robust fitting iterations use group-balanced weights. The flexible model uses the same expanded inputs and refits inside every outer fold. RBF tuning is also nested where used. Failed constraints, competing explanations and technical failures remain traceable.

## Complete numerical comparison

Errors are in **absolute log ratio**; lower is better. Mean absolute log transit ratio, particle-balanced within each configuration then equal configurations. Current missing targets are excluded only from scoring, and original eligibility is retained. None of these regression metrics is classification accuracy.

| Model | Development error | Exposed original-confirmation error |
|---|---:|---:|
| simple | 0.469607 | 0.117418 |
| linear | 3.21321 | 0.382991 |
| flexible | 0.412035 | 0.300893 |
| cycle1 | 0.528587 | 0.117418 |
| cycle2 | 0.470794 | 0.12719 |
| unconstrained1 | 0.480365 | 0.154362 |
| unconstrained2 | 0.459613 | 0.127319 |
| rbf | 0.364888 | 0.325453 |


The frozen candidate is **cycle2**. On development it has 29.02% higher error than the strongest matched control **rbf**, winning 1 of 6 groups. After the freeze, the exposed original-confirmation comparison finds 8.32% higher error than the descriptively best control **simple**, with 2 of 3 group wins. Every group, including losses, appears in `CONTROL_ANALYSIS.json` and `exposed-confirmation/by_group.csv`. This diagnostic comparison does not change the development selection.



The earlier frozen selected rule had error 0.366041; this continuation selected rule has error 0.12719 on the same exposed target groups (65.25% relative reduction; a negative value means deterioration). Predictor access or representation changed, so this comparison does not isolate a physical mechanism. Exact earlier scores and source hashes are in `OLD_REFERENCE_COMPARISON.json`.

## Executable selected equation

Full-development shape: `1.0`. Exact coefficients, training-only transform states and every fold model are in `results-v2/cycle2/`. The equation above defines the basis; each coefficient carries the units required to yield the target. Where a logarithm, exponent or shape ratio appears, its argument is dimensionless as specified in the protocol.

| Coefficient | Full-development value |
|---|---:|
| upstream_slowdown_response | 0.302678647 |
| orientation_dispersion_response | 0 |


Fold shapes, coefficient ranges and collapses at imposed bounds are recorded in `PARAMETER_STABILITY.json`. They are identifiability diagnostics, not measurements of physical constants. Zero coefficients and missingness terms remain explicit.

## Contribution, limits and next experiment

The benchmark exposes how an apparently sophisticated regression can underperform a physically elementary approximation under condition transfer. It provides a falsifying test for claims of orientation or energy-controlled residence time, rather than a separation-process or environmental-retention intervention.

An apparent density/kinematic Ri proxy is not the full buoyancy balance because particle density, rheological mapping and normal stress are incomplete.

The interface position and width derive from source profiles. Their availability before each trajectory is not established; this is a conditional calibrated-system task.

Strict upstream windows fix the historical crossing/interpolation defect. No predictor uses a right interpolation bracket beyond the causal cutoff.

Six development and three diagnostic configurations do not identify general rheology or particle-fluid mechanisms. Within-configuration trajectory counts are not independent environments.

The homogeneous-fluid dataset DOI 10.17632/pb7fjnwcw4.2 has no matching interface transit target; using it as fresh confirmation of this rule would change the scientific task.

**Next independent experiment.** Measure fresh layered configurations with pre-trajectory interface calibration, particle density and complete geometry, matched rheology including relaxation/normal stress, and full trajectories. Freeze transit target, upstream observation windows and whole-configuration splits before outcome access.

## Evidence and replay

Read `CASE_RESULT.json` for the integration record, `HYPOTHESIS_LEDGER.json` for revisions, `LESSONS.md` for actionable experience and `PRIOR_ART.json` for literature scope. `data/sample_anchors.csv.gz` links predictions to source rows, native members, time bounds or workbook cells. `INPUT_AUDIT.json` verifies frozen preparation, group separation, current-target poisoning, source hashes and preservation of existing final results.

From this continuation folder, run:

```sh
python run.py replay --output results-v2
python verify_inputs.py
python verify_exposed.py
```

Replay recomputes saved predictions and metrics without refitting. `evaluate_exposed.py` is the preserved one-shot diagnostic scorer and refuses an existing output directory; its result is already frozen. Numerical evidence is computational review, not independent experimental replication or expert adjudication. No physical law or ground-truth novelty claim is admitted by this continuation.

Primary sources: [https://pubmed.ncbi.nlm.nih.gov/40120384/](https://pubmed.ncbi.nlm.nih.gov/40120384/), [https://doi.org/10.17632/pb7fjnwcw4.2](https://doi.org/10.17632/pb7fjnwcw4.2). Their specific relevance and access limits are disclosed in `PRIOR_ART.json`.
