# P100-024: Glass-fiber composite fatigue under different cure profiles

> Principia-100 | Standardized portfolio | 1 October 2026

## Scenario and evaluation contract

Domain: structural materials. The current default task predicts Future measured composite stiffness conditional on continued recorded survival in GPa. Independent unit: complete specimen. Its packaged cohort contains 3,086 assigned rows in 6 groups.

**All supplied outcomes are now exposed.** Historical reserved evaluations remain part of the evidence record; future scores are retrospective. No newly established fundamental law or measured deployment impact is admitted by this packaging.

## Current portfolio findings

**Unsupported or falsified:** Parallel-floor and load-feedback degradation extensions add no supported mechanism.

Limit: The parallel floor collapses to zero; a fitted load-feedback floor can be removed with unchanged predictions. The older logarithmic reference remains selected.

**Unsupported or falsified:** Freeing the strain exponent fails to improve the established family; floor and load-feedback hypotheses are unidentifiable or inactive.

Limit: Changing an exponent has no fresh confirmation and performs worse. A fitted surviving fraction can have zero effect on all development predictions.

## Versioned tasks

| Task family | Target and information | Source scope |
|---|---|---|
| original | Future measured composite stiffness conditional on continued recorded survival (GPa) | original corpus |
| round2 | Future measured composite stiffness conditional on continued recorded survival (GPa) | original corpus |

Different targets, calibration budgets and cohorts have different task IDs. Their raw error values cannot be pooled into a scenario ranking. Exact equations, coefficients, permitted variables, timing, groups and per-model results are bound in the task packages.

Evaluation: the shared CLI provides numerical scoring, explicit coverage and abstention, uncertainty and event diagnostics. Agent review separately assesses scientific support; no aggregate discovery score is produced.

<!-- pagebreak -->

## Detailed reference note: Composite fatigue: a stiffness-monitoring reference
> Principia-100 · Case 24 · Calibrated experimental reproduction

## 1. Scenario and available measurements

The DTU corpus contains 23 cyclic tension specimens from three glass-fiber/epoxy laminate and cure conditions. Native TXT files preserve author-extracted stress, strain, stiffness and damping; workbooks supply plans and existing fatigue fits. Measurements date to 2015; the public release is 2025. The target is later mean extracted stiffness in GPa, conditional on a specimen remaining under recorded testing. Runouts are not treated as failures.

## 2. Experimental method

Metadata hashing reserved six complete specimens, two per laminate/cure; 17 specimens supported development. Median stiffness from cycles 10-20 in each specimen is declared early calibration; targets begin at 1,000 cycles. Later measured strain, stress, stiffness and failure time are excluded. Whole-specimen development validation tested five substantive hypotheses plus a baseline reproduction. Selection and stopping were frozen before confirmation. A flexible RBF comparator selected bandwidth and ridge within inner training-group folds.

## 3. Equation and physical interpretation

Let N be cycle count, E<sub>0</sub> the early median modulus and e the native nominal E-max value divided by 1%. The reference is

$$
\widehat{E}(N)=E_0\exp\left[-\kappa e^2\ln\left(1+\dfrac{N-20}{1000}\right)\right].
$$

Here κ = 0.02014880 is dimensionless; E and E<sub>0</sub> are in GPa. The constants 20 and 1,000 represent cycles. This describes gradual distributed degradation with decreasing incremental damage. It is a plausible approximation, not proof of one microscopic process. E-max is initial nominal metadata; actual strain can evolve. Full-precision parameters and competing states are in `rules.json`.

<!-- pagebreak -->

## 4. Findings and predictive performance

The primary error averages absolute errors within each reserved specimen, then averages the six specimen errors equally. Native adaptive sampling is preserved. 3,081 of 3,086 assigned rows were scored; five nonpositive extraction values remain flagged with native values and anchors.

| Frozen representation | Mean specimen MAE (GPa) |
|---|---:|
| Compact logarithmic reference | 1.825448 |
| Early-modulus persistence | 2.491034 |
| Fixed flexible RBF | 2.144380 |
| Group-tuned flexible RBF | 1.938008 |
| Logarithmic domain baseline | 1.825448 |
| Added late-acceleration competitor | 1.825448 |

Error is 26.72% lower than persistence, with improvement in all six specimens. Individual MAE ranges 0.402-4.369 GPa. The selected equation reproduces the domain baseline; no new material law is admitted. Extra positive late and frequency terms collapse toward zero; cure-specific sensitivity fails development transfer. Saturation and logarithmic explanations remain difficult to distinguish.

## 5. Practical value and limits

The reference supplies a transparent stiffness-monitoring correction after early calibration. It cannot predict remaining lifetime, sudden fracture, strength or unseen laminates. Cure and laminate are confounded. Extracted modulus shares stress/strain instrumentation; two terminal readings (136 and 251 GPa versus early modulus 37.5 GPa) remain included. Native row weighting differs from uniform cycle-time weighting; a separate cycle-interval sensitivity is supplied. Six specimens do not establish a population-wide industrial guarantee or a causal treatment effect.

## 6. Evidence and use

`run.py` reproduces frozen predictions and metrics without fitting. `rules.json`, prepared source anchors and compact evidence make calculations traceable; the evaluator scores other agents' equations under the same information contract. Packaged outcomes are now exposed, so later scores are retrospective. Negative hypotheses remain in research history.

Source: [DTU dataset, Zenodo 15665325](https://zenodo.org/records/15665325). Prior analysis: Kristiansen, Rasmussen and Mikkelsen (2025), [strain-based fatigue SN curves](https://doi.org/10.1088/1757-899X/1338/1/012018). This reference does not claim their published relationship as a new discovery.
