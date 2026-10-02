# Daylight longwave radiation: calibrated vapor and cloud interaction

**P100-048 · Source-aware scientific reference.** Supported as a scoped predictive extension; novelty and demonstrated industrial impact are not established.

## Scenario and measured endpoint

Daylight downwelling longwave irradiance in W/m2. Contemporaneous daytime downwelling longwave from independently measured temperature/RH and solar/diffuse channels. Zenith<75deg, globalSW>20W/m2, required QC=0. Cloud proxy is clipped diffuse/global ratio; not net-radiation closure.

Whole site-day blocks; forward folds Jan21–31,July8–15,July16–24 trained on preceding dates. July25–31 both sites reserved. Two sites only and correlated days. Development contains 57,610 eligible observations in 110 groups. Confirmation contains 9,464 eligible observations in 14 groups. Only daytime empirical clear/all-sky emissivity diagnostics; no nighttime extension, no independent cloud observations, no cloud causality.

## Findings and executable relation

The equation refines established atmospheric-emissivity parameterizations with a humidity–cloud interaction and fixed site calibration. These terms represent effective radiative conditions, not directly measured cloud fraction. Same-site temporal validation cannot establish unseen-site portability or novel radiative physics.

The reference selected before confirmation is `attempt-005`:

$$
\widehat L=\sigma T_K^4\,[a+bv+cq+dvq+es+fsq]
$$

L is downwelling longwave irradiance(W/m²); T_K=T+273.15K and σ=5.670374419×10⁻⁸W m⁻²K⁻⁴. Vapor pressure e_v=(RH/100)6.112exp[17.67T/(T+243.5)]hPa with T in°C; v=[(e_v/1hPa)/(T_K/1K)]^(1/7). q=clip(diffuse/global shortwave,0,1). s=1 for Desert Rock and0 for Penn State. All coefficients are dimensionless in these declared numerical units.

| Coefficient | Exact fitted value |
|---|---:|
| a | 0.0965272872130538 |
| b | 0.9884558987683114 |
| c | 0.6605476582997828 |
| d | -0.7218246875949597 |
| e | 0.03646540226237648 |
| f | -0.09159769949092146 |

All numerical constants, transformations, alternative equations and fitted coefficients are executable in `run.py` and serialized in `rules.json`. Any algebraic consequence of this equation is an implication of the same fitted model, not a second independently validated finding.

## Experimental method and evidence

8 substantive development attempts tested competing representations, controls and ablations. Fits use equal-group weighted least squares or declared robust loss, with all coefficients and radial-basis centers learned only inside each training fold. Selection minimizes mean group MAE, preferring fewer coefficients within1% of the minimum. Separate confirmation checks the frozen states and performs no fitting. Baselines share permitted information.

Primary errors are in W/m2; each group contributes equally regardless of row count.

| Frozen model | Development MAE | Confirmation MAE | Worst confirmation group |
|---|---:|---:|---:|
| reference | 12.4413 | 9.2422 | 18.9915 |
| brutsaert | 25.1985 | 16.4157 | 45.2452 |
| emissivity | 29.4149 | 36.1018 | 62.4732 |
| flexible | 18.5273 | 13.2546 | 26.6605 |
| attempt-001 | 26.0886 | 23.0945 | 52.4217 |
| attempt-002 | 15.6173 | 11.8634 | 23.7099 |
| attempt-003 | 16.5192 | 14.513 | 29.4903 |
| attempt-004 | 13.3776 | 10.5665 | 20.3463 |
| attempt-005 | 12.4413 | 9.2422 | 18.9915 |
| attempt-006 | 15.8723 | 12.123 | 21.1958 |
| attempt-007 | 13.4956 | 10.4627 | 19.1729 |
| attempt-008 | 14.2708 | 11.2282 | 18.432 |

The frozen reference changes confirmation MAE by 30.3% relative to the strongest evaluated baseline `flexible` (13.2546W/m2); it wins on 12/14 whole groups. This is descriptive, not a population significance test. Rows within runs, days, weeks, profiles or casts are dependent. The complete group errors, bias, RMSE and90th-percentile errors are in `evidence/by_group.csv`.

## Falsification, limits and value

- Cloud-gap closure and alternative Brunt/clearness representations expose accuracy–worst-day tradeoffs; they remain available instead of being hidden behind a single winner.
- A site coefficient is a calibration term, not a universal atmospheric constant. No nighttime or uninstrumented-site claim is admitted.
- Report whole-group errors and ranges; no independent-row population CI. Temporal/spatial dependence and small number of sites/floats limit inference.
- Public data and known physical parameterizations preclude automatic novelty certification. Predictive accuracy does not establish an industrial intervention or a new physical law.

Independent longwave sensing provides a genuine response target; net-radiation closure would only reproduce an accounting identity. Distinguish mean-error gains from worst-day robustness and disclose site calibration.

## Reproduction and future evaluation

Run `python run.py` in this folder to verify allowlisted hashes and reproduce every saved confirmation prediction. This executes trusted bundled reference code; scoring an external prediction file should use the shared Principia evaluator without executing submitted code. Numerical alternatives need not resemble this equation. Use the exact registered task, timing/input budget, units, eligibility and group weighting. New endpoints or information access require a separately reviewed task version.

All confirmation outcomes are now exposed to future users. Source-stage exposure is recorded in `task_spec.json`; the first-use internal freeze history is preserved in research history. Independent source data are needed for a new confirmation campaign.

## Primary sources and existing analyses

- [https://gml.noaa.gov/grad/surfrad/overview.html](https://gml.noaa.gov/grad/surfrad/overview.html) — NOAA describes independent shortwave/longwave instruments, auxiliary meteorology and public quality-controlled daily products.
- [https://doi.org/10.1029/WR011i005p00742](https://doi.org/10.1029/WR011i005p00742) — Brutsaert clear-sky effective emissivity is established physical parameterization; cloud extensions must be disclosed as empirical.
- [https://journals.ametsoc.org/view/journals/apme/46/6/jam2503.1.xml](https://journals.ametsoc.org/view/journals/apme/46/6/jam2503.1.xml) — Published all-sky longwave work compares vapor-state formulations and cloud increases in downwelling irradiance; our families are source-aware reproductions/extensions, not first principles newly found.
