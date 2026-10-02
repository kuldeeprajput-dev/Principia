# Calf breath DMS: baseline-calibrated post-treatment forecasting

The antibiotic-trial workbook retains seven complete calves, each measured twice before treatment and at1,24,48,72 and96hours afterward. The endpoint is the author-reported(C2H6S)H+ emission assigned to dimethyl sulphide. Only pre-dose DMS baseline, baseline change, age and scheduled time are available to predictors. The separate respiratory-disease trial is not used.

## Question and information budget

Prediction at treatment administration from pre-dose breath samples and scheduled post-dose time. Mean DMS emission at-48/-24h, difference and age at first post-dose row; five post-dose points are forecast. Other VOCs and disease labels excluded.

## Findings and interpretation

The development-selected persistence reference is preserved even when a later diagnostic comparator wins on the two reserved calves. No reliable transferable new kinetic law is admitted.

The selected executable relation is:

`yhat=baseline`

The full coefficient table and variable ordering are in `EQUATIONS.md`; `rules.json` contains exact precision. All equation inputs and their units are declared in `task_spec.json`.

Finite uptake, baseline-scaled amplitudes, two-component washout, pre-dose drift and log-time pulses do not improve the development selection. Several fitted parameters reach boundaries or collapse, undermining kinetic identifiability.

## Experimental design and performance

The reference `baseline_persistence` was chosen before confirmation. Development error was **0.024515141**; reserved-group error is **0.061158553 ug animal^-1 h^-1** across **2 groups and 10 observations**. Scores use equal group weights, with equal row weights within each group. No population confidence interval is inferred from these small samples.

| Frozen model | Confirmation primary error |
|---|---:|
| reference | 0.061158553 |
| baseline_persistence | 0.061158553 |
| baseline_decay | 0.052842084 |
| baseline_flexible | 0.055993567 |

5 substantive development attempts were preserved. Selection used whole-group out-of-fold errors and preferred the simplest model within1% of the minimum. Continuation ended only after two consecutive substantive attempts failed to improve prediction and no supported mechanism/robustness gain justified another candidate. Confirmation ran separately after code, source, states, selection and stopping were frozen. No later diagnostic winner was promoted.

## Scope, prior work and value

The paper describes ten antibiotic-trial calves, while this workbook contains seven complete calves. Only two are reserved. There is no untreated parallel group or dose series in this task; treatment, age and calendar time are inseparable. The paper reports a dosing statement that this benchmark does not use as a verified dosing recommendation.

Langford et al., PLOS ONE2026, already report antibiotic-associated breath changes and diagnostic confounding. Exponential washout, Bateman kinetics and lognormal pulses are established temporal response families. This small forecasting test does not newly discover treatment confounding.

No new universal law, independent experimental replication, clinical benefit or demonstrated industrial impact is claimed. Alternative valid discoveries can be evaluated using the same task contract; exact agreement with this equation is unnecessary. Negative findings describe failed tested hypotheses, not a lack of scientific phenomena.

## Reproduction and evaluation

Run `python run.py` inside this folder to verify frozen asset hashes and reproduce all saved predictions. It uses no network, fitting, research-history import or hidden model state. Submitter predictions must use the same sample IDs, units, information budget and group cohort. `scientific_checks.py` adds domain diagnostics to the shared benchmark scorer; it does not execute submitted code. New endpoints require a separately reviewed task.

Sources: [authoritative data](https://zenodo.org/records/17940806), [primary study](https://doi.org/10.1371/journal.pone.0351838). Source assets are CC BY4.0; citations and exact native hashes are retained in the scenario research layer. Current confirmation outcomes are exposed for all future users.
