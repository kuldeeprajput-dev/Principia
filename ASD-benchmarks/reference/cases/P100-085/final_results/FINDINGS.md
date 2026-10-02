# Flask glycolic-acid recovery from independent HPLC substrate measurements

## Scenario and task

Flask glycolic-acid recovery from independent HPLC substrate measurements. Native measurements come from [the authoritative source](https://zenodo.org/records/17396158). Complete flask conditions; three development conditions and one metadata-hash confirmation condition; leave-one-condition-out folds keep all replicates together.

Diagnostic contemporaneous assay: initial and current independently measured EG and current pH, known medium and elapsed time. No GA calibration. Not an online forecast or replacement of HPLC.

## Experimental method

5 substantive development attempts tested distinct dynamic, mechanistic or ablation hypotheses. Selection used equally weighted whole-group MAE, with a 1% simpler-model tie rule. Baseline fitting and preparation did not count as attempts. All states and stopping were frozen before a separate confirmation command; confirmation never changed the reference.

Native CSV previews exposed several GA observations in all four flask conditions before task freezing; explicitly retrospective; no confirmation metrics used in model selection.

## Reference equation and interpretation

$$
\widehat P=\max(0,E_0-E).
$$

P is glycolic-acid concentration in g/L; E0 and E are independently assayed initial and current ethylene-glycol concentrations in g/L. This is an empirical unit-mass screening baseline, not a chemical identity. Complete EG-to-GA oxidation has the distinct stoichiometric mass ratio 76.05/62.07=1.22531; side assimilation, incomplete recovery and measurement error can change observed yield.

Full-precision coefficients and all comparator states are in `rules.json`. 

<!-- pagebreak -->

## Findings and performance

No new mechanistic extension passes the development selection test. Unit mass recovery has leave-condition-out MAE 1.74842 g/L and retrospective reserved-condition MAE 0.945 g/L. The flexible control obtains 0.379299 g/L on that condition but was worse on development and remains a diagnostic comparison. The four reserved measurements do not establish broad accuracy.

| Frozen model | Confirmation MAE (g/L) |
|---|---:|
| reference | 0.945 |
| baseline zero | 3.015 |
| baseline unit yield | 0.945 |
| baseline stoichiometric | 1.02919 |
| baseline global yield | 0.989799 |
| baseline flexible | 0.379299 |

All candidate results and per-group errors remain in `evidence/metrics.csv` and `evidence/by_group.csv`. The reference is the preselected model, not the retrospectively best confirmation model. No error is converted into invented percentage accuracy.

| Reserved group | Selected reference MAE |
|---|---:|
| Flask_EG_OD0.5 | 0.945 |

## Value, limits and negative evidence

The source already established acetate-enhanced EG assimilation and GA synthesis, with isotope analyses. This campaign does not rebrand that result as new. The reserved high-inoculum EG-only condition contains two culture curves and four samples; all four scored glycolic-acid targets were visible in the schema audit before fitting. pH is contemporaneous and confounded, not an intervention. The duplicate bioreactor files are excluded without guessing a correction.

Check archive-member hashes before contrasting conditions. Keep the oxidation mass-ratio control separate from the empirically useful unit-yield predictor. A small internal holdout and known source results cannot support a novel metabolic mechanism or industrial savings.

## Reproduction and sources

Run `python run.py` inside this final package to verify its manifest and replay every frozen model. `rules.json` defines the exact coefficients, permitted input columns and units. `task_spec.json` and the shared evaluator provide the evaluation contract; valid alternative equations need not resemble these references.

Original study: [https://doi.org/10.1016/j.biortech.2025.133540](https://doi.org/10.1016/j.biortech.2025.133540). The authors already report acetate-enhanced EG assimilation and GA production with isotope evidence. Mass-ratio stoichiometry is a comparator, not a discovery. We test predictive recovery heterogeneity without asserting causal pH effects.
All packaged outcomes are exposed to future users. Agent review is computational/scientific criticism, not independent experimental replication or proof of novelty.
