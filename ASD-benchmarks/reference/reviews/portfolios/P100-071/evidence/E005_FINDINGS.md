# CHO sensing: causal decline correction and a spectral sign counterexample

**P100-071 · Continuation of 30 September 2026 · 3 substantive cycles**

Three new scientific cycles distinguish a causal decline gate, a positive spectral-density hypothesis, and a negative logarithmic spectral correction. The simplest decline-gated candidate is selected using original development only. It improves the earlier frozen spectral rule on exposed retrospective cultivation pairs, while a nonsaturating negative correction is stronger on development but does not transfer as well. The spectral and decline parameters do not identify cell-size, viability or membrane mechanisms.

## Scientific task and information access

Nine original-development paired experiments, seven batch and two fed-batch, with two reactors kept together. Outer and inner validation leave out complete experiment pairs. The three previously exposed pairs EXP005, EXP009 and EXP012 are retrospective diagnostic only; they do not establish plant, cell-line or population transfer.

Valid causal native inline permittivity, spectral and optical/process channels, current mode/time and past sensor-only summaries. Readings use the existing trailing 0.5 h summary or a last-valid fallback at most 2 h old; source status and Cole R²≥0.9 are retained. Running permittivity peak uses past samples only, and 24 h differences are causal. Offline VCD and its SEM supply target/context only. Imputation, spectral normalization and scales are fitted inside training partitions.

All original development and confirmation outcomes were exposed before this continuation. Development comparisons are grouped retrospective experiments. The original confirmation partition is scored once after candidate choice and stopping are frozen, solely to inspect transfer. It supplies no fresh independent confirmation and does not determine a new winner. Existing final-results packages remain unchanged.

## Hypotheses and experimental method

**Cycle 1: Causal decline-gated dielectric response.**

`VCD=max(0,b0+bP*perm*exp(-c*perm_decline_fraction)+bM*missing_perm), bP>=0,c>=0; the decline is from running past peak only`

Development primary error: 1.97183 million cells/mL. Retrospective operational candidate; not admitted physical law.

**Cycle 2: Conductivity-normalized positive spectral density.**

`Q=deltaeps*((fc/median_train_fc)/(conductivity/median_train_conductivity))^p; VCD=max(0,b0+bP*perm+bQ*Q+bMP*missing_perm+bMQ*missing_Q), bP,bQ>=0`

Development primary error: 2.00107 million cells/mL. Not selected; retained with counterexamples.

**Cycle 3: Sublinear logarithmic spectral bias correction versus positive-density interpretation.**

`Q=deltaeps*((fc/trainmedian(fc))/(conductivity/trainmedian(conductivity)))^p; Q0=train positive median(Q); VCD=max(0,b0+bP*perm*exp(-c*past_decline_fraction)-aQ*log1p(max(Q,0)/Q0)+bMP*missingPerm+bMQ*missingQ),bP,aQ>=0.`

Development primary error: 1.94792 million cells/mL. Logarithmic compression is not supported: the matched linear-magnitude correction attains 1.7936503583155745 versus 1.947917724887787.

All learned normalization, missing-value medians and model coefficients are fitted inside each training partition. Shape parameters use nested whole-group validation. Chronological validation is used when the task predicts later dates. Eight fixed robust fitting iterations use group-balanced weights. The flexible model uses the same expanded inputs and refits inside every outer fold. RBF tuning is also nested where used. Failed constraints, competing explanations and technical failures remain traceable.

## Complete numerical comparison

Errors are in **million cells/mL**; lower is better. Mean within-pair RMSE, equal complete paired experiments. Current missing targets are excluded only from scoring, and original eligibility is retained. None of these regression metrics is classification accuracy.

| Model | Development error | Exposed original-confirmation error |
|---|---:|---:|
| simple | 2.00921 | 1.81742 |
| linear | 2.38605 | 1.30873 |
| flexible | 2.20971 | 1.38697 |
| cycle1 | 1.97183 | 1.26089 |
| cycle2 | 2.00107 | 1.7531 |
| unconstrained1 | 1.97183 | 1.26089 |
| unconstrained2 | 1.8259 | 1.66436 |
| rbf | 2.12294 | 1.30542 |
| availability | 1.96271 | 1.7531 |
| adaptive_bounded_correction | 1.94792 | 1.30889 |
| adaptive_availability | 1.893 | 1.36744 |
| adaptive_linear_magnitude | 1.79365 | 1.3365 |
| adaptive_unconstrained | 1.94792 | 1.30889 |


The frozen candidate is **cycle1**. On development it has 9.93% higher error than the strongest matched control **adaptive_linear_magnitude**, winning 2 of 9 groups. After the freeze, the exposed original-confirmation comparison finds 3.41% lower error than the descriptively best control **rbf**, with 1 of 3 group wins. Every group, including losses, appears in `CONTROL_ANALYSIS.json` and `exposed-confirmation/by_group.csv`. This diagnostic comparison does not change the development selection.

The unconstrained cycle1 sign ablation is exactly the selected fitted equation and is retained in the full table; it is excluded from the strongest alternative comparator summary because it supplies no competing prediction.

The earlier frozen selected rule had error 1.63107; this continuation selected rule has error 1.26089 on the same exposed target groups (22.70% relative reduction; a negative value means deterioration). Predictor access or representation changed, so this comparison does not isolate a physical mechanism. Exact earlier scores and source hashes are in `OLD_REFERENCE_COMPARISON.json`.

## Executable selected equation

Full-development shape: `2`. Exact coefficients, training-only transform states and every fold model are in `results-v2/cycle1/`. The equation above defines the basis; each coefficient carries the units required to yield the target. Where a logarithm, exponent or shape ratio appears, its argument is dimensionless as specified in the protocol.

| Coefficient | Full-development value |
|---|---:|
| offset_million_ml | -0.0906864273 |
| permittivity_slope | 0.905923785 |
| missing_perm_offset | -3.91923007 |


Fold shapes, coefficient ranges and collapses at imposed bounds are recorded in `PARAMETER_STABILITY.json`. They are identifiability diagnostics, not measurements of physical constants. Zero coefficients and missingness terms remain explicit.

## Contribution, limits and next experiment

Frequency-spectrum correction for cell state is established prior art in [Downey et al. (2014)](https://pubmed.ncbi.nlm.nih.gov/24851255/). A [CHO culture sensitivity study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12000645/) reports that bulk spectral parameters combine cell-size and dielectric changes; they do not separately identify membrane or internal-conductivity parameters. The present fitted corrections therefore cannot establish those mechanisms.



The decline gate supplies an interpretable soft-sensor correction worthy of fresh independent testing. The negative spectral sign and availability ablations warn against assigning a biological interpretation to a prediction gain. No assay replacement, yield benefit, feeding decision or offline-sampling saving was demonstrated.

All original outcomes were exposed before this continuation. The improved reserved-pair error is retrospective; it cannot establish fresh validation or novelty.

A characteristic-frequency correction depends on cell size, membrane and conductivity assumptions that are not independently measured. Medium conductivity is not intracellular conductivity.

Spectral availability itself is predictive; it must be included in matched controls. Positive cell-density contribution and the logarithmic magnitude correction are unsupported by the new comparisons. The frozen name bounded_correction denotes a log1p term; that term is sublinear but unbounded, so it is not a physical saturation law.

Only three diagnostic pairs, including one fed-batch pair, provide limited mode-level evidence. Report individual pairs and mode failures; no precise population confidence interval is justified.

The selected decline rate c is fitted from development and is an operational shape parameter, not a biological kinetic rate.

**Next independent experiment.** Acquire fresh CHO pairs with independent offline VCD, cell-size distribution and membrane/conductivity measurements, including several fed-batch pairs and sensor missingness regimes. Freeze the decline-gated and negative spectral alternatives before receiving responses, and assess grouped prediction plus independent mechanistic measurements.

## Evidence and replay

Read `CASE_RESULT.json` for the integration record, `HYPOTHESIS_LEDGER.json` for revisions, `LESSONS.md` for actionable experience and `PRIOR_ART.json` for literature scope. `data/sample_anchors.csv.gz` links predictions to source rows, native members, time bounds or workbook cells. `INPUT_AUDIT.json` verifies frozen preparation, group separation, current-target poisoning, source hashes and preservation of existing final results.

From this continuation folder, run:

```sh
python run.py replay --output results-v2
python verify_inputs.py
python verify_exposed.py
python adaptive-003/adaptive.py replay
```

Replay recomputes saved predictions and metrics without refitting. `evaluate_exposed.py` is the preserved one-shot diagnostic scorer and refuses an existing output directory; its result is already frozen. Numerical evidence is computational review, not independent experimental replication or expert adjudication. No physical law or ground-truth novelty claim is admitted by this continuation.

Primary sources: [https://pubmed.ncbi.nlm.nih.gov/24851255/](https://pubmed.ncbi.nlm.nih.gov/24851255/), [https://pmc.ncbi.nlm.nih.gov/articles/PMC12000645/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12000645/), [https://zenodo.org/records/20829178](https://zenodo.org/records/20829178). Their specific relevance and access limits are disclosed in `PRIOR_ART.json`.
