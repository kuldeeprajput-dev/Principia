# Airway-pressure prediction during rapid occlusion

The Canterbury study records raw gauge and differential pressures at nominal 100 Hz from 20 healthy participants during PEEP, breath-hold and forced-expiration trials. Fixed source calibration converts ADC counts to cm H2O. At uniformly selected one-second origins, the task predicts gauge pressure200 ms later using only the previous 500 ms and present pressure channels.

## Question and information budget

At each fixed 1s origin predict native gauge pressure0.20s later using only present/past pressure and differential-pressure signals. Source fixed ADC-to-cm H2O conversion; no target-participant fitted coefficients. All history at or before forecast origin.

## Findings and interpretation

The selected autoregressive control gives a usable signal-prediction reference for this instrument/protocol. Its gain is a bounded signal-model result, not a new respiratory law.

The selected executable relation is:

$$
\widehat P(t+0.20\,\mathrm{s})=\beta_0+\sum_{j=1}^{13}\beta_j\phi_j(t).
$$

Here phi=(p0,p05,p10,p20,p30,p40,p50,di0,de0,di20,de20,p0*FEM,p0*BH). The p terms are gauge pressures at lags0,0.05,0.10,0.20,0.30,0.40 and 0.50s; di and de are inspiratory/expiratory differential pressures, with 0 and 0.20s lags. Every pressure is in cm H2O; FEM and BH are declared trial indicators. The intercept is 0.04519408 cm H2O, and the current gauge-pressure coefficient is 1.739696. All coefficients are already transformed back from training feature-RMS scaling: apply this dot product directly to the physical-unit inputs, with no additional scaling.

The full coefficient table and variable ordering are in `EQUATIONS.md`; `rules.json` contains exact precision. All equation inputs and their units are declared in `task_spec.json`.

Damped slopes, occlusion-period acceleration, differential-pressure drive, regime interactions and bounded inertia were tested. None displaced the flexible control on participant-held-out development data.

## Experimental design and performance

The reference `baseline_flexible` was chosen before confirmation. Development error was **0.30952647**; reserved-group error is **0.37185336 cm H2O** across **5 groups and 3768 observations**. Scores use equal group weights, with equal row weights within each group. No population confidence interval is inferred from these small samples.

| Frozen model | Confirmation primary error |
|---|---:|
| reference | 0.37185336 |
| baseline_persistence | 0.49150667 |
| baseline_tangent | 0.5091419 |
| baseline_flexible | 0.37185336 |

5 substantive development attempts were preserved. Selection used whole-group out-of-fold errors and preferred the simplest model within 1% of the minimum. Continuation ended only after two consecutive substantive attempts failed to improve prediction and no supported mechanism/robustness gain justified another candidate. Confirmation ran separately after code, source, states, selection and stopping were frozen. No later diagnostic winner was promoted.

## Scope, prior work and value

Five reserved participants are a small internal cohort, and all are from a healthy study. Trial duration affects within-person weighting; complete trials stay linked. The target is one recorded pressure signal, not an independently measured physiological parameter.

The source study describes respiratory monitoring under rapid occlusion and model-based work-of-breathing analysis. Persistence, pressure-slope extrapolation and autoregressive forecasting are established controls; predictive success does not identify resistance, compliance, muscle pressure or clinical utility.

No new universal law, independent experimental replication, clinical benefit or demonstrated industrial impact is claimed. Alternative valid discoveries can be evaluated using the same task contract; exact agreement with this equation is unnecessary. Negative findings describe failed tested hypotheses, not a lack of scientific phenomena.

## Reproduction and evaluation

Run `python run.py` inside this folder to verify frozen asset hashes and reproduce all saved predictions. It uses no network, fitting, research-history import or hidden model state. Submitter predictions must use the same sample IDs, units, information budget and group cohort. `scientific_checks.py` adds domain diagnostics to the shared benchmark scorer; it does not execute submitted code. New endpoints require a separately reviewed task.

Sources: [authoritative data](https://physionet.org/content/respiratory-heartrate-dataset/1.0.0/), [primary study](https://doi.org/10.1016/j.ifacol.2023.10.1107). Source assets are CC BY 4.0; citations and exact native hashes are retained in the scenario research layer. Current confirmation outcomes are exposed for all future users.
