# Mountain turbulence: a bounded energy-memory forecast

**P100-095 · Source-aware scientific reference.** Supported as a scoped predictive extension; novelty and demonstrated industrial impact are not established.

## Scenario and measured endpoint

Next half-hour author-derived turbulent kinetic energy in m2/s2. Predict next 30-min author-derived TKE from completed previous 30-min TKE, mean velocity and two-height temperature gradient. No contemporaneous target variance/covariance inputs. Both intervals RawAnyS2/H2 flags 0; predictor MetT0.

Whole ISO weeks. Forward folds week 4, weeks 7–8, weeks 9–10 with all earlier weeks training. March15 onward weeks 11–13 confirmation. One mountain station during one winter. Development contains 775 eligible observations in 11 groups. Confirmation contains 266 eligible observations in 3 groups. MeanTKE2 is author-derived from turbulent measurements; mean wind/thermal gradients are observational predictors, not mechanical interventions. Flag0 subset can select calmer/instrument-quality regimes; no universal turbulence closure.

## Findings and executable relation

A positive mean-flow-production proxy and negative energy-dependent decay term give modest temporal-transfer improvement. Their signs are compatible with an energy budget, but temporal averaging, shared sensor derivation and omitted advection/buoyancy prevent identification of a complete turbulence closure.

The reference selected before confirmation is `attempt-002`:

$$
\widehat E_{t+30\,min}=\max[0,E_t+aU_t^3+bE_t^{3/2}]
$$

E is author-derived30min turbulent kinetic energy(m²/s²); U is the preceding interval horizontal mean-speed magnitude(m/s). Both a and b have numerical units s/m for this discrete30min map. They absorb sampling interval and unresolved scales and must not be read as independently measured dissipation lengths or rates.

| Coefficient | Exact fitted value |
|---|---:|
| a | 0.0001258407653048686 |
| b | -0.06084383152145573 |

All numerical constants, transformations, alternative equations and fitted coefficients are executable in `run.py` and serialized in `rules.json`. Any algebraic consequence of this equation is an implication of the same fitted model, not a second independently validated finding.

## Experimental method and evidence

5 substantive development attempts tested competing representations, controls and ablations. Fits use equal-group weighted least squares or declared robust loss, with all coefficients and radial-basis centers learned only inside each training fold. Selection minimizes mean group MAE, preferring fewer coefficients within 1% of the minimum. Separate confirmation checks the frozen states and performs no fitting. Baselines share permitted information.

Primary errors are in m2/s2; each group contributes equally regardless of row count.

| Frozen model | Development MAE | Confirmation MAE | Worst confirmation group |
|---|---:|---:|---:|
| reference | 0.312265 | 0.247284 | 0.37833 |
| constant | 1.18388 | 1.21072 | 1.41604 |
| flexible | 0.322589 | 0.262726 | 0.380423 |
| persistence | 0.342338 | 0.266345 | 0.402092 |
| shear_energy | 0.783922 | 0.542453 | 0.867022 |
| attempt-001 | 0.317397 | 0.246266 | 0.377981 |
| attempt-002 | 0.312265 | 0.247284 | 0.37833 |
| attempt-003 | 0.333066 | 0.247401 | 0.379777 |
| attempt-004 | 0.314263 | 0.246238 | 0.378384 |
| attempt-005 | 0.328762 | 0.246267 | 0.377995 |

The frozen reference changes confirmation MAE by 5.88% relative to the strongest evaluated baseline `flexible` (0.262726 m2/s2); it wins on 3/3 whole groups. This is descriptive, not a population significance test. Rows within runs, days, weeks, profiles or casts are dependent. The complete group errors, bias, RMSE and 90th-percentile errors are in `evidence/by_group.csv`.

## Falsification, limits and value

- Mean-wind-squared without energy history has substantially worse confirmation error than causal persistence.
- The added stability-regime representation is rank deficient in at least one development fit; its parameters do not identify separate physical regimes.
- Report whole-group errors and ranges; no independent-row population CI. Temporal/spatial dependence and small number of sites/floats limit inference.
- Public data and known physical parameterizations preclude automatic novelty certification. Predictive accuracy does not establish an industrial intervention or a new physical law.

A mean-flow-only energy fit is a weak baseline compared with causal energy persistence. Compare mechanism-shaped predictors against that baseline and disclose that target TKE is author-derived. Rank-deficient stability terms cannot support a new stability law.

## Reproduction and future evaluation

Run `python run.py` in this folder to verify allowlisted hashes and reproduce every saved confirmation prediction. This executes trusted bundled reference code; scoring an external prediction file should use the shared Principia evaluator without executing submitted code. Numerical alternatives need not resemble this equation. Use the exact registered task, timing/input budget, units, eligibility and group weighting. New endpoints or information access require a separately reviewed task version.

All confirmation outcomes are now exposed to future users. Source-stage exposure is recorded in `task_spec.json`; the first-use internal freeze history is preserved in research history. Independent source data are needed for a new confirmation campaign.

## Primary sources and existing analyses

- [https://zenodo.org/records/18670232](https://zenodo.org/records/18670232) — Author releases observational validation measurements alongside model output; only observations retained in local-data bundle are used.
- [https://tc.copernicus.org/articles/18/849/2024/](https://tc.copernicus.org/articles/18/849/2024/) — Primary study describes glacier/terrain context and sonic anemometry. A statistical energy-budget proxy is not evidence of an identified snow-drift law.
- [https://doi.org/10.5194/egusphere-2025-5608](https://doi.org/10.5194/egusphere-2025-5608) — Dataset-linked SNOWstorm preprint is disclosed as existing analysis; our narrow turbulence forecast is not an independent reproduction of full model validation.
