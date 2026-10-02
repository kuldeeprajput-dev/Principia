# Case 57: Viscosity history: forecasting and identifiability

**Evidence status:** Retrospective development and exposed-group transfer assessment. All original cohorts are exposed. Original final results remain unchanged; no fresh confirmation or new physical law is claimed here.

## 1. Scenario and endpoint

The NYU rheometer exports were acquired in 2024–2025 and released in April 2026. This new forecasting track contains 40 original development Test IDs: four repeated tests for each of 10 calibrated formulations. Each test contributes 25 shear-sweep points at each of nine later temperature steps, giving 9,000 observations. The target is native reported viscosity in cP at the next completed temperature block. Earlier viscosity measurements from the same test are declared online calibration. They are matched by nominal sweep-point ordinal; actual current and preceding shear rates are supplied separately. Native Result Start Time determines chronology because some export files list blocks in reverse order.

## 2. Experimental method

Outer validation leaves out one whole Test ID per formulation, using the four original group folds: 30 tests train and 10 tests validate in each fold. Inner tuning also keeps complete Test IDs together. Every model receives the same declared causal history; the static Arrhenius comparator may ignore it, while the flexible residual model uses all allowed inputs. This evaluates later ramp observations in repeated tests of known formulations. It does not test new material lots or disentangle thermal equilibrium from aging, curing or shear history.

## 3. Tested equation and interpretation

Define \(\theta_j=(T_{C,j}+273.15)\,\mathrm K\). The compact history candidate is

$$\widehat\eta_j=\eta_{j-1}\exp\left[B_f(1000\,\mathrm K)\left(\frac 1{\theta_j}-\frac 1{\theta_{j-1}}\right)\right],\qquad 0\le B_f\le 30.$$

Viscosity \(\eta\) is in cP and \(B_f\) is dimensionless. The conventional apparent activation descriptor is \(E_f/R=1000 B_f\,\mathrm K\). Every formulation coefficient is stored in `cycle-001/model.json`. Four all-development coefficients reach the zero bound. The numerical implementation floors nonpositive log inputs at \(10^{-9}\)cP, while retaining all native outcomes in scores. The 190 negative viscosity outcomes and 64 values at or above 100,000 cP make a clean equilibrium constitutive interpretation untenable.

## 4. Performance and preserved alternatives

Selected compact candidate: `cycle-001`. Its development mae is **3628.0325 cP**, versus **3637.3972 cP** for `baseline-old`. Physical-unit mean group error is 3628.0325 cP. All paired groups and counterexamples appear in `PAIRED_GROUP_EVIDENCE.csv` and `BY_SYSTEM.csv`. Descriptive leave-one-system-out sensitivity is reported without a population confidence claim.

| Cycle | Tested hypothesis family | Development error | Disposition |
|---|---|---:|---|
| cycle-001 | thermal history | 3628.0325 | Selected retrospective candidate |
| cycle-002 | curved history | 3604.8023 | Preserved alternative or failure |
| cycle-003 | additive structure | 6143.2146 | Preserved alternative or failure |

### Retrospective transfer on the original exposed reserved groups

After selection and stopping were frozen, unchanged full-development states were evaluated on 10 original reserved groups (2250 assigned rows; 2250 finite targets). These targets were previously exposed. No fitting, reselection or fresh confirmation occurred. Errors use the same whole-group weighting as development; the acoustic normalization uses full-development condition means only.

| Frozen model | Primary error (cP) | Physical error (cP) |
|---|---:|---:|
| `cycle-001` | 3628.056384 | 3628.056384 |
| `baseline-flex` | 5656.927695 | 5656.927695 |
| `baseline-old` | 3637.345033 | 3637.345033 |
| `baseline-previous` | 3647.359687 | 3647.359687 |
| `baseline-signed_history` | 3640.728070 | 3640.728070 |

The repeated-test forecast has new causal history access and fewer eligible temperature blocks than the original static task. Its improvement remains negligible: the candidate wins four of ten reserved Test IDs. This does not establish a dynamic constitutive law or identify equilibrium activation.

Scores and individual counterexamples are in `retrospective_transfer/metrics.csv`, `by_group.csv` and `paired_group_evidence.csv`. The frozen development record remains in `CASE_RESULT.json`; exposed-group results are an append-only `TRANSFER_ADDENDUM.json`.

## 5. Value, limitations and next experiment

The selected history model improves its strongest comparator by only 0.257%, wins 16 of 40 test groups and reaches a coefficient boundary in several formulations. The additive structure-growth alternative increases error sharply. The useful outcome is an audited causal-history task and evidence that these measurements cannot identify a new equilibrium or curing law. No new rule is admitted as ground truth.

The next independent experiment should address: Independently synthesized lots with randomized temperature order, upward/downward ramps, dwell times and verified torque-resolution calibration; preserve native negative readings and acquisition flags. Separate thermal equilibrium from curing/shear-history response before fitting a constitutive law.

## 6. Reproduction and assessment

From this folder, run `python cycle-001/run.py` to replay frozen outer-fold predictions. Submit other agents’ predictions with `python score.py --predictions predictions.csv --out evaluation-new`. This task-specific evaluator checks exact IDs/groups, missing outcomes and abstention coverage, then compares baselines on identical scored rows. It does not certify scientific mechanism or novelty. See `EVALUATION_CONTRACT.md`, `PROTOCOL.json` and `HYPOTHESIS_LEDGER.json`.

Source and prior art: [source 1](https://zenodo.org/records/19699588), [source 2](https://doi.org/10.1122/1.549276), [source 3](https://doi.org/10.1016/0095-8522(65)90022-X).
