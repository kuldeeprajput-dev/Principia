# Case 72: Fermentation chemistry: residual-sugar forecasting

**Evidence status:** Retrospective development and exposed-group transfer assessment. All original cohorts are exposed. Original final results remain unchanged; no fresh confirmation or new physical law is claimed here.

## 1. Scenario and endpoint

This is a new HPLC chemistry task, separate from the original qPCR abundance forecast. The IATA-CSIC workbook contains a November 2020 fermentation sequence, analyzed/exported in 2021 and publicly deposited in February 2026; the associated paper was published in 2023. The development cohort has six strain labels, with monoculture and CR 85 co-culture experiments and their biological replicates kept together. There are 153 later measurements. The target is measured remaining glucose plus fructose in g/L. Permitted predictors are each fermentation’s own glucose/fructose concentrations at 22 and 72 hours, the requested future time and the known inoculation context. No later chemistry, qPCR abundance or unverified amino-acid experiment is used.

## 2. Experimental method

Outer validation leaves one complete strain out, training on the other five; inner tuning also leaves complete strains out. Monoculture/co-culture conditions, replicates and future times of each strain remain together. Prefix assays at 22 and 72 hours are declared calibration, including for a validation strain. All baselines use the same allowable assays. Simple persistence, linear consumption, first-order depletion and a nested flexible residual model are evaluated fairly. This is retrospective transfer within one fermentation campaign, not fresh strain or medium confirmation.

## 3. Tested equation and interpretation

Let \(q\in\{G,F\}\) denote glucose or fructose, and fix \(q_{\rm ref}=1\,\mathrm{g/L}\). The separate-pool hypothesis is

$$\frac{dq}{dt}=-a_qv_q\frac{q}{K+q},\qquad v_q=\frac{q_{22}-q_{72}+K\log(q_{22}/q_{72})}{50\,\mathrm h}.$$

The forecast solves

$$q_t+K\log\frac{q_t}{q_{\rm ref}}=q_{72}+K\log\frac{q_{72}}{q_{\rm ref}}-a_qv_q(t-72\,\mathrm h),\qquad\widehat S_t=G_t+F_t.$$

The concentrations \(G,F,S,K\) are in g/L; \(v_q\) is in g/L/h and \(a_q\) is dimensionless. The all-development state is \(K=200\) g/L, \(a_G=2.55389076\) and \(a_F=1.41036852\). Nested folds fit their own coefficients. \(K\) is the upper searched value, so it is not an identified biochemical Monod constant. Separate effective rates are consistent with known substrate-uptake differences; they do not identify a nitrogen, biomass or genetic mechanism.

## 4. Performance and preserved alternatives

Selected compact candidate: `cycle-002`. Its development mae is **14.656974 g/L**, versus **17.782176 g/L** for `baseline-flex`. Physical-unit mean group error is 14.656974 g/L. All paired groups and counterexamples appear in `PAIRED_GROUP_EVIDENCE.csv` and `BY_SYSTEM.csv`. Descriptive leave-one-system-out sensitivity is reported without a population confidence claim.

| Cycle | Tested hypothesis family | Development error | Disposition |
|---|---|---:|---|
| cycle-001 | monod | 16.059389 | Preserved alternative or failure |
| cycle-002 | separate pool | 14.656974 | Selected retrospective candidate |
| cycle-003 | coculture pool | 14.809076 | Preserved alternative or failure |
| cycle-004 | arrested pool | 14.873695 | Preserved alternative or failure |

### Retrospective transfer on the original exposed reserved groups

After selection and stopping were frozen, unchanged full-development states were evaluated on 2 original reserved groups (48 assigned rows; 48 finite targets). These targets were previously exposed. No fitting, reselection or fresh confirmation occurred. Errors use the same whole-group weighting as development; the acoustic normalization uses full-development condition means only.

| Frozen model | Primary error (g/L) | Physical error (g/L) |
|---|---:|---:|
| `cycle-002` | 8.390050 | 8.390050 |
| `baseline-first_order` | 24.361333 | 24.361333 |
| `baseline-flex` | 10.469339 | 10.469339 |
| `baseline-linear_sugar` | 13.585238 | 13.585238 |
| `baseline-persistence` | 94.074961 | 94.074961 |

The two reserved strain labels are T73 and D245. This is the new residual-sugar task, using declared 22/72 h HPLC calibration; it is not a comparison with the original qPCR target. The selected candidate beats the frozen flexible comparator in both strains. The three linked T73 co-culture R3 injections at 360 h contain two finite sugar measurements and one missing measurement. All three remain in the native injection inventory; the frozen scoring cohort has 48 finite assays. The predeclared secondary metric averages native injection errors within biological sample-tag/time before averaging strains: 8.477608 versus 10.598097 g/L. Its 47 sample-tag/times are not independent biological replicates. Missing assays and unresolved repetition metadata are disclosed without imputing targets or changing the frozen cohort.

Scores and individual counterexamples are in `retrospective_transfer/metrics.csv`, `by_group.csv` and `paired_group_evidence.csv`. The frozen development record remains in `CASE_RESULT.json`; exposed-group results are an append-only `TRANSFER_ADDENDUM.json`.

## 5. Value, limitations and next experiment

The separate-pool candidate improves the matched flexible comparator by 17.575% and wins five of six strains; NCAIM is a counterexample. Co-culture-specific rates and late activity arrest do not improve transfer. Substrate specificity is already known prior art. The new practical endpoint is residual-sugar forecasting; neither industrial deployment benefit nor a novel biological mechanism is established.

The next independent experiment should address: A new independently prepared strain/medium campaign with reserved strain labels and actual inoculation-ratio contrasts; repeated early sugar/ethanol/biomass and nitrogen assays with resolved units. Freeze 72 h prefix forecast and remaining-sugar primary before future measurements. Vary starting sugar to identify K rather than use a single high-concentration regime.

## 6. Reproduction and assessment

From this folder, run `python cycle-002/run.py` to replay frozen outer-fold predictions. Submit other agents’ predictions with `python score.py --predictions predictions.csv --out evaluation-new`. This task-specific evaluator checks exact IDs/groups, missing outcomes and abstention coverage, then compares baselines on identical scored rows. It does not certify scientific mechanism or novelty. See `EVALUATION_CONTRACT.md`, `PROTOCOL.json` and `HYPOTHESIS_LEDGER.json`.

Source and prior art: [source 1](https://zenodo.org/records/18757697), [source 2](https://pubmed.ncbi.nlm.nih.gov/37290881/), [source 3](https://doi.org/10.1146/annurev.mi.03.100149.002103), [source 4](https://doi.org/10.1016/j.ijfoodmicro.2026.111813).
