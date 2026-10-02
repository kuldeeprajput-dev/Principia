# Arctic CDOM: a scoped halocline mixing diagnostic

**P100-094 · Source-aware scientific reference.** Supported as a scoped predictive extension; novelty and demonstrated industrial impact are not established.

## Scenario and measured endpoint

Calibrated CDOM fluorescence channel in ppb. Contemporaneous calibrated CDOM fluorescence diagnostic using pressure,T1,S1; no other optical or oxygen response input. Good T/S flags0, pump on,5–500dbar. CDOM has no independent QC column.

Entire station casts02,06,08 development (cast04 has no eligible good-QC observations) leave-one-cast-out; casts10 and12 confirmation. Same expedition/instrument, spatial transfer not independent sensor calibration. Development contains 7,386 eligible observations in 3 groups. Confirmation contains 4,893 eligible observations in 2 groups. CDOM ppb is the publisher-calibrated fluorescence channel, not chemically measured DOC concentration. Quality control does not establish a universal conservative-mixing relationship. No target-based outlier removal.

## Findings and executable relation

A continuous two-slope salinity relation with a thermal endmember correction improves held-cast CDOM prediction. It is compatible with changing water-mass mixtures across a halocline. CDOM fluorescence does not independently measure chemical DOC, and the model cannot separate mixing, biology or photochemistry.

The reference selected before confirmation is `attempt-003`:

$$
\widehat C=a+b(S-34)+c\max(S-33,0)+dT
$$

C is the source-calibrated CDOM fluorescence channel(ppb), S is practical salinity(psu), and T is in-situ temperature(°C). The33psu hinge is fixed before fitting, not a newly identified phase boundary. a is in ppb, b,c in ppb/psu, and d in ppb/°C.

| Coefficient | Exact fitted value |
|---|---:|
| a | 1.03476665527121 |
| b | 0.02073697165798316 |
| c | -0.346510001524961 |
| d | -0.01956237763234016 |

All numerical constants, transformations, alternative equations and fitted coefficients are executable in `run.py` and serialized in `rules.json`. Any algebraic consequence of this equation is an implication of the same fitted model, not a second independently validated finding.

## Experimental method and evidence

5 substantive development attempts tested competing representations, controls and ablations. Fits use equal-group weighted least squares or declared robust loss, with all coefficients and radial-basis centers learned only inside each training fold. Selection minimizes mean group MAE, preferring fewer coefficients within1% of the minimum. Separate confirmation checks the frozen states and performs no fitting. Baselines share permitted information.

Primary errors are in ppb; each group contributes equally regardless of row count.

| Frozen model | Development MAE | Confirmation MAE | Worst confirmation group |
|---|---:|---:|---:|
| reference | 0.066903 | 0.0410217 | 0.0449196 |
| constant | 0.161173 | 0.176219 | 0.193638 |
| flexible | 0.0690253 | 0.0458915 | 0.0489194 |
| salinity_mixing | 0.0767451 | 0.0822193 | 0.0853564 |
| attempt-001 | 0.0695723 | 0.0570697 | 0.0602191 |
| attempt-002 | 0.0825597 | 0.063476 | 0.0658707 |
| attempt-003 | 0.066903 | 0.0410217 | 0.0449196 |
| attempt-004 | 0.080249 | 0.0556904 | 0.0608181 |
| attempt-005 | 0.0705357 | 0.0629561 | 0.0648967 |

The frozen reference changes confirmation MAE by 10.6% relative to the strongest evaluated baseline `flexible` (0.0458915ppb); it wins on 2/2 whole groups. This is descriptive, not a population significance test. Rows within runs, days, weeks, profiles or casts are dependent. The complete group errors, bias, RMSE and90th-percentile errors are in `evidence/by_group.csv`.

## Falsification, limits and value

- A purely depth-based relation is weaker than the selected salinity-hinge relation on the reserved casts.
- The threshold is a tested fixed representation, not evidence of a discovered universal salinity transition.
- Report whole-group errors and ranges; no independent-row population CI. Temporal/spatial dependence and small number of sites/floats limit inference.
- Public data and known physical parameterizations preclude automatic novelty certification. Predictive accuracy does not establish an industrial intervention or a new physical law.

Use complete casts and retain calibration/quality metadata. One planned development cast had every T1/S1 value flagged bad and was excluded by the prefit rule, reducing independent evidence to three development and two confirmation casts.

## Reproduction and future evaluation

Run `python run.py` in this folder to verify allowlisted hashes and reproduce every saved confirmation prediction. This executes trusted bundled reference code; scoring an external prediction file should use the shared Principia evaluator without executing submitted code. Numerical alternatives need not resemble this equation. Use the exact registered task, timing/input budget, units, eligibility and group weighting. New endpoints or information access require a separately reviewed task version.

All confirmation outcomes are now exposed to future users. Source-stage exposure is recorded in `task_spec.json`; the first-use internal freeze history is preserved in research history. Independent source data are needed for a new confirmation campaign.

## Primary sources and existing analyses

- [https://zenodo.org/records/17530624](https://zenodo.org/records/17530624) — Dataset creator documents calibrated downcast sensors, paired packs and flags. CDOM is reported in ppb; no chemically measured DOC response or CDOM quality flag is supplied.
- [https://pmc.ncbi.nlm.nih.gov/articles/PMC5034254/](https://pmc.ncbi.nlm.nih.gov/articles/PMC5034254/) — Primary Chukchi Sea study reports that optical DOM and DOC need not correlate simply with salinity; multiple water masses matter. Different region and date, so it informs falsification rather than validating this expedition.
