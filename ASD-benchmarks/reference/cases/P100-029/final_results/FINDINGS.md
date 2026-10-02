# Peptide-barrel fluorescence: limits of calibrated binding transfer

The native archive contains spectroscopy and structural experiments for designed peptide barrels. This task uses all six peptide–dye binding conditions, four linked replicate dose curves per condition, and the mean of every recorded emission-wavelength channel. Native low-dose spectra provide declared calibration; no future peak wavelength or maximum fluorescence normalizes the target.

## Question and information budget

Predict remaining higher-dose assay values after declared lower-dose measurements; sequential assay not real-time kinetics. Spectrum-wide mean fluorescence at native concentrations 0, 1, 2 and 5 nominal micromolar, per replicate; target concentrations 7.5 to 30. No maximal-response normalization.

## Findings and interpretation

Persistent low-dose signal is a conservative assay control. Its error is substantial, and near-equality with the domain comparator on two conditions provides no claim of molecular universality or strong predictive accuracy.

The selected executable relation is:

$$
\widehat F=F_{5\,\mathrm{\mu M}}.
$$

The full coefficient table and variable ordering are in `EQUATIONS.md`; `rules.json` contains exact precision. All equation inputs and their units are declared in `task_spec.json`.

Shared cooperativity, effective quenching, local curvature inversion, dye-specific affinity and shrunk affinity all fail to improve the development-selected control. Boundary parameters and leave-condition failures limit identifiable binding interpretations.

## Experimental design and performance

The reference `baseline_persistence` was chosen before confirmation. Development error was **26573.566**; reserved-group error is **38661.131 source fluorescence a.u.** across **2 groups and 48 observations**. Scores use equal group weights, with equal row weights within each group. No population confidence interval is inferred from these small samples.

| Frozen model | Confirmation primary error |
|---|---:|
| reference | 38661.131 |
| baseline_persistence | 38661.131 |
| baseline_linear | 74640.382 |
| baseline_langmuir | 38656.412 |
| baseline_flexible | 38849.936 |

5 substantive development attempts were preserved. Selection used whole-group out-of-fold errors and preferred the simplest model within 1% of the minimum. Continuation ended only after two consecutive substantive attempts failed to improve prediction and no supported mechanism/robustness gain justified another candidate. Confirmation ran separately after code, source, states, selection and stopping were frozen. No later diagnostic winner was promoted.

## Scope, prior work and value

Four development and two confirmation peptide–dye conditions share peptides and dyes. Spectral means mix intensity and band-shape responses. Fluorescence is not independently measured occupancy; optical controls would be needed to distinguish binding from quenching. Replicates are linked, not counted as independent conditions.

Petrenas et al., JACS 2025, already demonstrate binding and confinement effects, FRET and anthracene photochemistry. Equilibrium binding, Hill curves and fluorescence quenching are established model families. This experiment tests condition transfer of those families; it does not establish a new binding law.

No new universal law, independent experimental replication, clinical benefit or demonstrated industrial impact is claimed. Alternative valid discoveries can be evaluated using the same task contract; exact agreement with this equation is unnecessary. Negative findings describe failed tested hypotheses, not a lack of scientific phenomena.

## Reproduction and evaluation

Run `python run.py` inside this folder to verify frozen asset hashes and reproduce all saved predictions. It uses no network, fitting, research-history import or hidden model state. Submitter predictions must use the same sample IDs, units, information budget and group cohort. `scientific_checks.py` adds domain diagnostics to the shared benchmark scorer; it does not execute submitted code. New endpoints require a separately reviewed task.

Sources: [authoritative data](https://zenodo.org/records/13335904), [primary study](https://pubs.acs.org/doi/10.1021/jacs.4c16633). Source assets are CC BY 4.0; citations and exact native hashes are retained in the scenario research layer. Current confirmation outcomes are exposed for all future users.
