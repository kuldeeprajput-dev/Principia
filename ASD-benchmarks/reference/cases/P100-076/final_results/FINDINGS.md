# Neuronal current–spike transfer across recording dates

The native FI table provides injected current, spike count, stiffness, Piezo1 condition, recording date, dish and cell identifiers at DIV7. This task predicts responses above 10 pA from the lower-current prefix of the same recording. Multiple recording files from a cell remain linked by dish. The complete final recording date is reserved; development also includes a two-date stress test.

## Question and information budget

Predict higher-current evoked spike counts after the lower-current prefix for that cell. No future rheobase or peak-response calibration. Per-cell spike counts at applied current<=10 pA; later currents>10 pA forecast. Source manual FI eligibility preserved.

## Findings and interpretation

A calibrated no-increase control is a strong reference in this sparse-response cohort. Its advantage is evidence about forecast difficulty and calibration value, not proof that neurons lack current dependence or mechanosensitivity.

The selected executable relation is:

$$
\widehat N=N_{\mathrm{last\ prefix}}.
$$

The full coefficient table and variable ordering are in `EQUATIONS.md`; `rules.json` contains exact precision. All equation inputs and their units are declared in `task_spec.json`.

Condition thresholds, pooled saturation, prefix-dependent recruitment, high-current block and condition-specific gain fail to improve the selected control in whole-dish development testing.

## Experimental design and performance

The reference `baseline_persistence` was chosen before confirmation. Development error was **0.72486772**; reserved-group error is **0.44196429 spikes per stimulus** across **8 groups and 266 observations**. Scores use equal group weights, with equal row weights within each group. No population confidence interval is inferred from these small samples.

| Frozen model | Confirmation primary error |
|---|---:|
| reference | 0.44196429 |
| baseline_persistence | 0.44196429 |
| baseline_rheobase | 0.72560674 |
| baseline_flexible | 0.73781354 |

5 substantive development attempts were preserved. Selection used whole-group out-of-fold errors and preferred the simplest model within 1% of the minimum. Continuation ended only after two consecutive substantive attempts failed to improve prediction and no supported mechanism/robustness gain justified another candidate. Confirmation ran separately after code, source, states, selection and stopping were frozen. No later diagnostic winner was promoted.

## Scope, prior work and value

Only three recording dates exist; final validation is across 8 dishes on one date, not8 independent donor batches. Many responses are small or zero. The retained data do not identify animal/culture-batch independence. No causal challenge of the published stiffness pathway follows from prediction failure.

Kreysing et al., Nature Communications 2025, already show stiffness- and Piezo1-associated maturation. Rheobase shifts, gain changes, saturation and depolarization block are established explanatory families. These source findings are not newly discovered here.

No new universal law, independent experimental replication, clinical benefit or demonstrated industrial impact is claimed. Alternative valid discoveries can be evaluated using the same task contract; exact agreement with this equation is unnecessary. Negative findings describe failed tested hypotheses, not a lack of scientific phenomena.

## Reproduction and evaluation

Run `python run.py` inside this folder to verify frozen asset hashes and reproduce all saved predictions. It uses no network, fitting, research-history import or hidden model state. Submitter predictions must use the same sample IDs, units, information budget and group cohort. `scientific_checks.py` adds domain diagnostics to the shared benchmark scorer; it does not execute submitted code. New endpoints require a separately reviewed task.

Sources: [authoritative data](https://zenodo.org/records/12802682), [primary study](https://doi.org/10.1038/s41467-025-64810-3). Source assets are CC BY 4.0; citations and exact native hashes are retained in the scenario research layer. Current confirmation outcomes are exposed for all future users.
