# P100-026: Catalytic induction trajectory transfer

## What the scenario contains

Six complete reactor runs were developed with leave-run-out validation; the 220°C-labelled and calcined-catalyst runs were reserved. All models receive the same fixed 300-minute calibration prefix. The long-term figure duplicated in the source is counted once. No instantaneous conversion or other selectivity enters the predictor. The endpoint is dimethoxymethane selectivity, reported in percentage points. Native files remain unchanged; preparation is deterministic and hash-verified.

## Supported result and its interpretation

A two-parameter, causal prefix-conditioned forecast improves persistence and straight-line continuation on two reserved reactor runs. It loses to the flexible control and several other frozen candidates, so evidence supports useful short-horizon calibration rather than a superior or universal kinetic law.

**Admission:** partially supported; **classification:** validated extension.

Let $t$ be minutes after the last calibration observation at or before 300 min, $S_0$ that observation's DMM selectivity in percent, and $s_0$ the fixed 120–300 min calibration slope in percentage points per minute. Then


$$
\widehat S(t)=S_0+s_0\tau(1-e^{-t/\tau})+kt.
$$


$\tau$ is a relaxation time in minutes; $k$ is a slow drift in percentage points per minute. This is a local forecast for total time on stream up to 1500 min. The drift is not an identified reaction intermediate or a justified infinite-time extrapolation.

| Coefficient | Value | Unit |
|---|---:|---|
| `tau` | 243.6425 | min |
| `k` | 0.0035609534 | percentage points/min |

## Validation and performance

The selected reference was fixed after 8 substantive development attempts. Whole-group development MAE was **0.954747**; reserved-group MAE was **1.43487 percentage points** across 233 scored rows and 2 top-level groups. Groups, not individual dependent rows, define the scope of validation.

| Model | Confirmation MAE |
|---|---:|
| Selected: Relaxation plus slow drift | 1.43487 |
| Last calibration value | 5.47827 |
| Prefix slope persistence | 7.79773 |
| Constant response | 19.3163 |
| Flexible calibrated trajectory | 1.21104 |

The lowest observed confirmation error among all frozen models is 0.612867 for Loading-dependent equilibrium. This is a diagnostic comparison; it does not replace the development-selected reference.

Additional diagnostic figure: [Confirmation evidence](evidence/confirmation.png).

## Failures, limitations and value

The second fitted relaxation time is not separately identified. The two-timescale fit reaches the 20000-minute upper bound; its identifiable local drift limit is retained with a 1500-minute scope and no intermediate-species claim. All attempts and unfavorable results remain traceable in research history. Parameter vectors, group errors and all predictions are supplied; population confidence claims are not justified by this small or single-system campaign.

The useful contribution is an executable, auditable test of the stated response and its alternatives. No independent experiment, exhaustive novelty adjudication, validated deployment benefit or new universal physical law is claimed. Source-author analyses are prior art. Current outcomes are exposed and cannot become a fresh holdout by renaming this task.

## Reproduce or evaluate another finding

Run `python run.py` in this folder to verify integrity and reproduce saved predictions and metrics. `python run.py --input INPUT.csv --output predictions.csv` applies all frozen equations to a compatible input table. `task_spec.json` defines allowed inputs, calibration, units and grouping; use the shared Principia-100 evaluator for comparable prediction submissions. A different endpoint or information budget requires a separate frozen task.

The numerical score is equal-group MAE, supplemented by group RMSE, bias, error quantiles and applicable physical checks. Predictive accuracy and mechanistic/novelty review are separate; abstention and valid alternative discoveries remain admissible.

## Source and prior art

[Primary source study](https://pubs.rsc.org/en/content/articlepdf/2025/cy/d5cy00544b); [authoritative dataset](https://zenodo.org/records/15691695). See `SOURCE_MANIFEST.json` for byte-level provenance and research history for the native-semantics audit, exclusions and literature record.
