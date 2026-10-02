# Case 60: Ultrasonic excitation: normalized response assessment

**Evidence status:** Retrospective development and exposed-group transfer assessment. All original cohorts are exposed. Original final results remain unchanged; no fresh confirmation or new physical law is claimed here.

## 1. Scenario and endpoint

The TU Graz reference experiment was measured in 2020 and converted/released as MATLAB data inOctober 2025. Development data contain five pulse widths—2.5,7.5,10,12.5 and 15 microseconds—at six calibrated distance/sensor conditions, with 10 waveform repetitions per file: 30 files and 300 observations. The endpoint is the maximum absolute post-trigger receiver voltage after subtracting the pre-trigger mean. Distance, nominal receiver resonance and pulse width are the only physical predictors. Contact and air coupling are different regimes; nominal resonance is confounded with receiver identity.

## 2. Experimental method

Each outer fold reserves one complete pulse width across all six conditions: 24 files train and six files validate. Inner tuning reserves another complete width from the outer training cohort. Repetitions stay with their source file. The new primary robustness measure is MAE divided by the corresponding outer-training condition mean voltage, averaged equally over files. It is dimensionless and is not MAPE. Physical voltage MAE is reported alongside it, without changing the original benchmark’s voltage endpoint. The five held-width folds share one calibrated apparatus; 30 files do not represent 30 independent devices.

## 3. Tested equation and interpretation

The selected conditional excitation model is

$$\widehat V_c(w)=A_c\max\left\{1,\sqrt{1+e^{-2 w/\tau_f}-2 e^{-w/\tau_f}\cos(2\pi f w)}\right\}.$$

Pulse width \(w\) and damping descriptor \(\tau_f\) are in microseconds; \(f\) is in MHz, converted from native kHz, so \(fw\) is dimensionless. The gain \(A_c\) is in volts. The all-development state uses \(\tau_{110}=10\,\mu\mathrm s\) and \(\tau_{500}=2\,\mu\mathrm s\); each outer fold fits/tunes its own state. The six gains are 12.5343151, 1.08938060,0.00309132,0.000698495,0.00232901 and 0.000532670 V in the stored condition order. A leading-edge floor is retained. These are calibrated response descriptors, not independently measured damping constants or an air-propagation law.

## 4. Performance and preserved alternatives

Selected compact candidate: `cycle-001`. Its development normalized_mae is **0.15576147 dimensionless**, versus **0.19526332 dimensionless** for `baseline-global_edge`. Physical-unit mean group error is 0.53662871 V. All paired groups and counterexamples appear in `PAIRED_GROUP_EVIDENCE.csv` and `BY_SYSTEM.csv`. Descriptive leave-one-system-out sensitivity is reported without a population confidence claim.

| Cycle | Tested hypothesis family | Development error | Disposition |
|---|---|---:|---|
| cycle-001 | edge frequency | 0.15576147 | Selected retrospective candidate |
| cycle-002 | edge mixture | 2.7834418 | Preserved alternative or failure |
| cycle-003 | bounded edge | 0.15853988 | Preserved alternative or failure |
| cycle-004 | hybrid contact | 0.18338797 | Preserved alternative or failure |

### Retrospective transfer on the original exposed reserved groups

After selection and stopping were frozen, unchanged full-development states were evaluated on 6 original reserved groups (60 assigned rows; 60 finite targets). These targets were previously exposed. No fitting, reselection or fresh confirmation occurred. Errors use the same whole-group weighting as development; the acoustic normalization uses full-development condition means only.

| Frozen model | Primary error (dimensionless) | Physical error (V) |
|---|---:|---:|
| `cycle-001` | 0.194023 | 0.256019 |
| `baseline-constant` | 0.139710 | 0.780303 |
| `baseline-flex` | 0.167319 | 0.780315 |
| `baseline-global_edge` | 0.367711 | 0.318159 |
| `baseline-old` | 0.367711 | 0.318159 |

The candidate improves on the frozen shared-damping comparator in all three 500 kHz conditions and ties it in the three 110 kHz conditions. However, the constant baseline has lower normalized transfer error (0.139710 versus 0.194023), and the flexible baseline also has lower normalized error (0.167319). Their physical errors are larger (about 0.780 V versus 0.256 V), so the performance ranking depends on the declared objective. This is evidence against a claim that the candidate dominates all strong comparators. The previously selected model is retained without reselection.

Scores and individual counterexamples are in `retrospective_transfer/metrics.csv`, `by_group.csv` and `paired_group_evidence.csv`. The frozen development record remains in `CASE_RESULT.json`; exposed-group results are an append-only `TRANSFER_ADDENDUM.json`.

## 5. Value, limitations and next experiment

The aggregate normalized gain is 20.230%, but it is not uniform across conditions or widths. Shared sensor-family damping remains confounded with hardware and coupling; the 500 kHz damping descriptor reaches the lower search grid. The unrestricted leading/trailing mixture extrapolates catastrophically, and the bounded mixture/contact-only alternatives do not outperform the simpler selection. The candidate is a scoped instrument-response hypothesis pending independent confirmation.

The next independent experiment should address: A metadata-frozen new campaign with independent sensor remounts, repeated calibration days and additional intermediate/noncommensurate pulse widths at every distance/sensor; reserve widths and devices before target exposure. Measure waveform energy/shape independently of peak voltage to distinguish competing response mechanisms.

## 6. Reproduction and assessment

From this folder, run `python cycle-001/run.py` to replay frozen outer-fold predictions. Submit other agents’ predictions with `python score.py --predictions predictions.csv --out evaluation-new`. This task-specific evaluator checks exact IDs/groups, missing outcomes and abstention coverage, then compares baselines on identical scored rows. It does not certify scientific mechanism or novelty. See `EVALUATION_CONTRACT.md`, `PROTOCOL.json` and `HYPOTHESIS_LEDGER.json`.

Source and prior art: [source 1](https://zenodo.org/records/17266427), [source 2](https://repository.tugraz.at/records/ph0jm-8ax 76/files/ts3_techdescr.pdf).
