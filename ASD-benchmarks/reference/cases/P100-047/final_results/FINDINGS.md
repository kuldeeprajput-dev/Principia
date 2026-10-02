# Argo oxygen: water-mass prediction and a nitrate-mechanism falsification

**P100-047 · Source-aware scientific reference.** Supported as a scoped predictive extension; novelty and demonstrated industrial impact are not established.

## Scenario and measured endpoint

Adjusted dissolved oxygen at observed nitrate/water-mass state in umol/kg. Contemporaneous adjusted oxygen diagnostic using independently instrumented nitrate and CTD measurements from the same aligned synthetic profile. No prospective acquisition claim. Adjusted T/S flags 1,2,8 permit source interpolation; oxygen/nitrate/pressure flags 1,2 only.

Whole float profiles; rolling half-year tests 2023H2,2024H1,H2,2025H1, earlier times train. July2025 onward reserved. Two serially sampled floats, not hundreds of independent oceans. Development contains 14,723 eligible observations in 222 groups. Confirmation contains 4,253 eligible observations in 64 groups. Author-adjusted, aligned/calibrated products. In-situ-temperature surface oxygen-solubility proxy used for comparison; no potential-temperature or pressure-corrected AOU claim. No causal Redfield stoichiometry from correlated water masses.

## Findings and executable relation

The nitrate-free equation predicts later profiles better than the richer nitrate alternatives and the flexible control. This supports a scoped diagnostic of water-mass/vertical structure and contradicts the necessity of a nitrate-stoichiometry explanation for these data. It does not refute remineralization biology or identify causal mixing rates.

The reference selected before confirmation is `attempt-005`:

$$
\widehat O=O_*(T,S)+a+b(S-34)+cT+d\ln(1+p/100)+e\exp(-p/100)
$$

O is adjusted dissolved oxygen(µmol/kg), T is adjusted in-situ temperature(°C), S is practical salinity(psu), and p is pressure(dbar). Pressure ratios use100 dbar. O* is the published Garcia–Gordon surface-equilibrium solubility expression evaluated with in-situ temperature; it is a proxy, not a formal potential-temperature/pressure-corrected AOU calculation. Coefficients a,d,e have oxygen units; b and c have oxygen units per psu and per°C.

| Coefficient | Exact fitted value |
|---|---:|
| a | -623.3540344708498 |
| b | 10.3216218537414 |
| c | 18.32390735957119 |
| d | 101.5034159695018 |
| e | 109.4030412808184 |

All numerical constants, transformations, alternative equations and fitted coefficients are executable in `run.py` and serialized in `rules.json`. Any algebraic consequence of this equation is an implication of the same fitted model, not a second independently validated finding.

## Experimental method and evidence

7 substantive development attempts tested competing representations, controls and ablations. Fits use equal-group weighted least squares or declared robust loss, with all coefficients and radial-basis centers learned only inside each training fold. Selection minimizes mean group MAE, preferring fewer coefficients within 1% of the minimum. Separate confirmation checks the frozen states and performs no fitting. Baselines share permitted information.

Primary errors are in umol/kg; each group contributes equally regardless of row count.

| Frozen model | Development MAE | Confirmation MAE | Worst confirmation group |
|---|---:|---:|---:|
| reference | 9.17733 | 8.85346 | 17.3864 |
| constant | 33.6373 | 31.1798 | 57.7512 |
| depth_only | 20.3923 | 19.8098 | 36.8106 |
| flexible | 10.1788 | 9.94856 | 18.6098 |
| redfield | 36.8398 | 34.7556 | 42.7783 |
| attempt-001 | 29.773 | 27.6627 | 39.0061 |
| attempt-002 | 17.4256 | 17.0401 | 27.5928 |
| attempt-003 | 9.41192 | 9.42853 | 17.2065 |
| attempt-004 | 12.9442 | 12.0295 | 22.8664 |
| attempt-005 | 9.17733 | 8.85346 | 17.3864 |
| attempt-006 | 12.9551 | 12.0169 | 22.8367 |
| attempt-007 | 15.6638 | 15.3845 | 27.2069 |

The frozen reference changes confirmation MAE by 11% relative to the strongest evaluated baseline `flexible` (9.94856umol/kg); it wins on 54/64 whole groups. This is descriptive, not a population significance test. Rows within runs, days, weeks, profiles or casts are dependent. The complete group errors, bias, RMSE and 90th-percentile errors are in `evidence/by_group.csv`.

## Falsification, limits and value

- A fixed 138:16 oxygen–nitrate comparator is inadequate here; different published stoichiometries and preformed nutrient mixing preclude a universal stoichiometric conclusion.
- The nitrate-free water-mass/depth ablation beats the best development nitrate model on the mean reserved-profile metric; all profiles remain dependent within only two floats.
- Report whole-group errors and ranges; no independent-row population CI. Temporal/spatial dependence and small number of sites/floats limit inference.
- Public data and known physical parameterizations preclude automatic novelty certification. Predictive accuracy does not establish an industrial intervention or a new physical law.

A mechanistic-looking cross-variable slope needs an information ablation. When removing nitrate improves transfer, report that counterexample rather than presenting an effective slope as new Redfield chemistry.

## Reproduction and future evaluation

Run `python run.py` in this folder to verify allowlisted hashes and reproduce every saved confirmation prediction. This executes trusted bundled reference code; scoring an external prediction file should use the shared Principia evaluator without executing submitted code. Numerical alternatives need not resemble this equation. Use the exact registered task, timing/input budget, units, eligibility and group weighting. New endpoints or information access require a separately reviewed task version.

All confirmation outcomes are now exposed to future users. Source-stage exposure is recorded in `task_spec.json`; the first-use internal freeze history is preserved in research history. Independent source data are needed for a new confirmation campaign.

## Primary sources and existing analyses

- [https://argo.ucsd.edu/data/how-to-use-argo-files/](https://argo.ucsd.edu/data/how-to-use-argo-files/) — Argo instructs use of adjusted BGC measurements and documents synthetic profile alignment and quality flags.
- [https://www.teos-10.org/pubs/gsw/html/gsw_O2sol_SP_pt.html](https://www.teos-10.org/pubs/gsw/html/gsw_O2sol_SP_pt.html) — TEOS oxygen solubility uses practical salinity and potential temperature; our in-situ-temperature implementation is explicitly only a surface-equilibrium proxy.
- [https://doi.org/10.4319/lo.1992.37.6.1307](https://doi.org/10.4319/lo.1992.37.6.1307) — Garcia and Gordon oxygen solubility dependence on temperature/salinity is prior art; frozen coefficients are not a discovery.
- [https://www.gfdl.noaa.gov/bibliography/related_files/laa9401.pdf](https://www.gfdl.noaa.gov/bibliography/related_files/laa9401.pdf) — Anderson and Sarmiento distinguish preformed water-mass mixing and biological remineralization. Published stoichiometries vary; single observed oxygen–nitrate slopes do not establish a biological law. The classical138:16 comparison is only one benchmark, not a universal standard.
