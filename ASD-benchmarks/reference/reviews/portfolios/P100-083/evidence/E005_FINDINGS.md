# Case 83: Hive temperature: a constrained-physics falsification

**Evidence status:** Retrospective development and exposed-group transfer assessment. All original cohorts are exposed. Original final results remain unchanged; no fresh confirmation or new physical law is claimed here.

## 1. Scenario and endpoint

The UFC apiary data were measured in December 2024–March 2025 for Apis streams and September 2025–March 2026 for Meliponini streams, then released in May 2026. Five calibrated sensor streams contribute 5531 development prediction origins in four chronological blocks per stream. The target is the native internal temperature approximately one hour later. An origin uses the first observation in the first 15 minutes of an hour; the target must lie within five minutes of the requested horizon on the same calendar day. Internal and external temperature lags are causal observations at least one hour before the origin. Current external temperature/humidity and source-clock daily phase are available to all comparators. Rainfall and future weather are excluded.

## 2. Experimental method

The earliest block initializes training. Forward outer folds then train on blocks earlier than the validation block, evaluating blocks 1–3 for every stream: 15 validation blocks and 4111 scored forecasts. All transforms and fits use those earlier blocks; the nested flexible baseline receives the same causal external lag. Group errors are averaged equally. The five streams come from one apiary and are not established as independent colony populations. Source-clock phase has no independently verified time zone.

## 3. Tested equation and interpretation

The sign-constrained competing equation is

$$\widehat T_{t+1}=T_t+b_s+\alpha(T^e_t-T_t)+m(T_t-T_{t-1})-k\operatorname{VPD}_t+u\sin\omega t+v\cos\omega t,$$

with \(0\le\alpha\le 1\), \(0\le m\le 0.95\), \(k\ge 0\) and \(\omega=2\pi/(24\,\mathrm h)\). Temperatures are in degrees Celsius; VPD is in kPa. Offsets/phase terms have temperature-change units over the nominal one-hour forecast; \(k\) has degC/kPa. The all-development \(\alpha=0.00680385\), \(m=0.20691326\), and \(k\) reaches zero. All remaining coefficients are stored in `cycle-001/model.json`. Positive signs impose a testable response hypothesis; they do not prove passive conductance, a brood setpoint or metabolic heat.

## 4. Performance and preserved alternatives

Selected compact candidate: `cycle-001`. Its development rmse is **0.19148704 degC**, versus **0.16096145 degC** for `baseline-flex`. Physical-unit mean group error is 0.19148704 degC. All paired groups and counterexamples appear in `PAIRED_GROUP_EVIDENCE.csv` and `BY_SYSTEM.csv`. Descriptive leave-one-system-out sensitivity is reported without a population confidence claim.

| Cycle | Tested hypothesis family | Development error | Disposition |
|---|---|---:|---|
| cycle-001 | positive exchange | 0.19148704 | Selected retrospective candidate |
| cycle-002 | delayed exchange | 0.19148704 | Preserved alternative or failure |
| cycle-003 | heterogeneous exchange | 0.23288858 | Preserved alternative or failure |

### Retrospective transfer on the original exposed reserved groups

After selection and stopping were frozen, unchanged full-development states were evaluated on 5 original reserved groups (1282 assigned rows; 1282 finite targets). These targets were previously exposed. No fitting, reselection or fresh confirmation occurred. Errors use the same whole-group weighting as development; the acoustic normalization uses full-development condition means only.

| Frozen model | Primary error (degC) | Physical error (degC) |
|---|---:|---:|
| `cycle-001` | 0.224754 | 0.224754 |
| `baseline-flex` | 0.201686 | 0.201686 |
| `baseline-old` | 0.204548 | 0.204548 |
| `baseline-persistence` | 0.215706 | 0.215706 |
| `baseline-unconstrained_exchange` | 0.211918 | 0.211918 |

The candidate loses to the flexible comparator in every one of the five calibrated future stream blocks. Its error is 11.437% larger on average. The result reinforces the negative development finding; imposing positive thermal signs does not by itself create a predictive or causal mechanism.

Scores and individual counterexamples are in `retrospective_transfer/metrics.csv`, `by_group.csv` and `paired_group_evidence.csv`. The frozen development record remains in `CASE_RESULT.json`; exposed-group results are an append-only `TRANSFER_ADDENDUM.json`.

## 5. Value, limitations and next experiment

The positive model is 18.965% worse than the matched flexible comparator. Removing instantaneous ambient exchange slightly improves its development error, while removing memory worsens it; delayed exchange reaches zero and stream-specific positive rates degrade prediction. This falsifies a claim of superior passive-physics prediction on this cohort. It does not disprove thermoregulation in bees.

The next independent experiment should address: Independent colonies/apiaries with verified sensor placement, causal external weather and measured metabolic/ventilation proxies; controlled environmental perturbations with held-out days/colonies. Predeclare a temperature forecast endpoint separately from colony health utility.

## 6. Reproduction and assessment

From this folder, run `python cycle-001/run.py` to replay frozen outer-fold predictions. Submit other agents’ predictions with `python score.py --predictions predictions.csv --out evaluation-new`. This task-specific evaluator checks exact IDs/groups, missing outcomes and abstention coverage, then compares baselines on identical scored rows. It does not certify scientific mechanism or novelty. See `EVALUATION_CONTRACT.md`, `PROTOCOL.json` and `HYPOTHESIS_LEDGER.json`.

Source and prior art: [source 1](https://zenodo.org/records/20399470), [source 2](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0008967).
