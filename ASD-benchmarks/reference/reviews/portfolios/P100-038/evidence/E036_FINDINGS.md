# Short-horizon drone RSRP: a failed transferable correction

**P100-038 · Source-aware scientific reference.** Unsupported as an improvement: the development-selected reference fails against the strongest confirmation comparator. It remains a reproducible negative reference; no replacement was selected after exposure.

## Scenario and measured endpoint

First reported RSRP-vector component at first recorded point 1.0–1.6 s after issuance in dBm. At a recorded RSRP sample, use only component 1 in the native comma-separated RSRP vector over the preceding 20 seconds. Predict first subsequently recorded component-1 value at 1.0–1.6 s. First qualifying issuance per target; no actual future horizon feature in predictor. Unknown component antenna/beam semantics prevent propagation-law claims.

Entire flight; forward folds 1->2,1–2->3,1–3->4; flight5 confirmation. Same installation/day only. Development contains 3,595 eligible observations in 4 groups. Confirmation contains 486 eligible observations in 1 groups. Telemetry files1–2 do not overlap the radio clock windows and contain repeated headers; no invented offset or geometry pairing. Vector component ordering is taken literally, not identified as a specific antenna.

## Findings and executable relation

The correction represents noise-dependent mean reversion. Its apparent development benefit did not transfer to the final flight. No new propagation law or operational reliability improvement is supported.

The reference selected before confirmation is `attempt-005`:

$$
\widehat r_{t+h}=r_t+c\,(\overline r_{5,t}-r_t)\,\frac{s_{5,t}}{1\,\mathrm{dB}+s_{5,t}}
$$

r is the first comma-separated component of the native RSRP vector (dBm); h is the next measured horizon in[1.0,1.6]s, never a prediction input. The trailing5s mean and population standard deviation s use only available past records. c is dimensionless. The component is not mapped to a known antenna or beam.

| Coefficient | Exact fitted value |
|---|---:|
| c | 0.6778972850975561 |

All numerical constants, transformations, alternative equations and fitted coefficients are executable in `run.py` and serialized in `rules.json`. Any algebraic consequence of this equation is an implication of the same fitted model, not a second independently validated finding.

## Experimental method and evidence

5 substantive development attempts tested competing representations, controls and ablations. Fits use equal-group weighted least squares or declared robust loss, with all coefficients and radial-basis centers learned only inside each training fold. Selection minimizes mean group MAE, preferring fewer coefficients within1% of the minimum. Separate confirmation checks the frozen states and performs no fitting. Baselines share permitted information.

Primary errors are in dB; each group contributes equally regardless of row count.

| Frozen model | Development MAE | Confirmation MAE | Worst confirmation group |
|---|---:|---:|---:|
| reference | 1.21588 | 1.04082 | 1.04082 |
| constant | 4.48961 | 4.46257 | 4.46257 |
| flexible | 1.20931 | 0.928604 | 0.928604 |
| persistence | 1.25461 | 0.944856 | 0.944856 |
| attempt-001 | 1.25773 | 0.99601 | 0.99601 |
| attempt-002 | 1.2287 | 1.04244 | 1.04244 |
| attempt-003 | 1.21577 | 1.00498 | 1.00498 |
| attempt-004 | 1.21068 | 0.987291 | 0.987291 |
| attempt-005 | 1.21588 | 1.04082 | 1.04082 |

The frozen reference changes confirmation MAE by -12.1% relative to the strongest evaluated baseline `flexible` (0.928604dB); it wins on 0/1 whole groups. This is descriptive, not a population significance test. Rows within runs, days, weeks, profiles or casts are dependent. The complete group errors, bias, RMSE and90th-percentile errors are in `evidence/by_group.csv`.

## Falsification, limits and value

- Trend extrapolation is not a reliable improvement over persistence in this cohort.
- The source telemetry clocks for flights1–2 do not overlap radio windows. This is an input audit limitation, not a discovered physical relationship.
- Report whole-group errors and ranges; no independent-row population CI. Temporal/spatial dependence and small number of sites/floats limit inference.
- Public data and known physical parameterizations preclude automatic novelty certification. Predictive accuracy does not establish an industrial intervention or a new physical law.

Schema semantics come before geometric modeling: clock-incompatible telemetry and unlabelled vector entries do not justify altitude or antenna claims. Preserve failed transfer even when development scores improve.

## Reproduction and future evaluation

Run `python run.py` in this folder to verify allowlisted hashes and reproduce every saved confirmation prediction. This executes trusted bundled reference code; scoring an external prediction file should use the shared Principia evaluator without executing submitted code. Numerical alternatives need not resemble this equation. Use the exact registered task, timing/input budget, units, eligibility and group weighting. New endpoints or information access require a separately reviewed task version.

All confirmation outcomes are now exposed to future users. Source-stage exposure is recorded in `task_spec.json`; the first-use internal freeze history is preserved in research history. Independent source data are needed for a new confirmation campaign.

## Primary sources and existing analyses

- [https://zenodo.org/records/16673883](https://zenodo.org/records/16673883) — Dataset creator describes five drone measurement iterations from one private5G network. Native vector component identities and mismatched earlier telemetry windows are unresolved.
- [https://www.etsi.org/deliver/etsi_ts/138200_138299/138215/17.04.00_60/ts_138215v170400p.pdf](https://www.etsi.org/deliver/etsi_ts/138200_138299/138215/17.04.00_60/ts_138215v170400p.pdf) — 3GPP/ETSI physical-layer RSRP measurement definition; provides quantity context, not identification of each Nemo export vector component.
