# P100-006: Rydberg ionization spectral transfer

## What the scenario contains

Eight contiguous 30-condition Rabi blocks were used for leave-block-out development; blocks 06 and 09 were reserved. Frequencies and nearby Rabi coordinates are dependent. The task covers only the fixed ±60 MHz spectral neighborhood on one cesium cell. The endpoint is ion-readout amplitude, reported in arbitrary units. Native files remain unchanged; preparation is deterministic and hash-verified.

## Supported result and its interpretation

The asymmetric dual-response equation improves prediction on two reserved contiguous Rabi blocks compared with the single-line and polynomial controls. Its practical contribution is a scoped response surrogate with explicit uncertainty about mechanism, not a new atomic law.

**Admission:** supported; **classification:** validated extension.

Let $u$ denote probe Rabi frequency in MHz and $\delta$ the coupling detuning in MHz. Define


$$
L(w)=\frac{1}{1+[(\delta-\delta_0)/w]^2},\quad W=w_0+w_1u,\quad N=n_0+n_1u.
$$


The selected predictor is


$$
\widehat I=b_0+b_1u+\frac{Au}{1+u/u_s}L(W)-\frac{Du^2}{u_d^2+u^2}L(N)+a u\frac{\delta-\delta_0}{W}L(W).
$$


The broad and narrow responses have opposite signs; the last term permits line asymmetry. This is a compact response model, not a unique identification of two microscopic species. Both zero-power width intercepts, $w_0$ and $n_0$, reached the imposed 0.1 MHz lower bound; intrinsic zero-power linewidths are therefore not identified by this fit.

| Coefficient | Value | Unit |
|---|---:|---|
| `delta_0` | -1.7559412 | MHz |
| `b_0` | 0.35221313 | a.u. |
| `b_1` | -0.0089651743 | a.u./MHz |
| `A` | 0.44222886 | a.u./MHz |
| `u_s` | 6.7036497 | MHz |
| `w_0` | 0.1 | MHz |
| `w_1` | 8.503336 | dimensionless |
| `n_0` | 0.1 | MHz |
| `n_1` | 4.1345462 | dimensionless |
| `D` | 2.3394102 | a.u. |
| `u_d` | 3.3972567 | MHz |
| `a` | 0.017249622 | a.u./MHz |

## Validation and performance

The selected reference was fixed after 5 substantive development attempts. Whole-group development MAE was **0.0307338**; reserved-group MAE was **0.0492859 arbitrary units** across 4800 scored rows and 2 top-level groups. Groups, not individual dependent rows, define the scope of validation.

| Model | Confirmation MAE |
|---|---:|
| Selected: Asymmetric dual response | 0.0492859 |
| Single Lorentzian with power broadening | 0.0771298 |
| Constant response | 0.232168 |
| Polynomial response surface | 0.111713 |

The lowest observed confirmation error among all frozen models is 0.0492859 for Asymmetric dual response. This is a diagnostic comparison; it does not replace the development-selected reference.

Additional diagnostic figure: [Confirmation evidence](evidence/confirmation.png).

## Failures, limitations and value

A single saturating line fails to explain the response as well as the two-sign line-shape family. The failed single-line candidate has larger grouped development and confirmation error; the result does not uniquely prove two microscopic channels. All attempts and unfavorable results remain traceable in research history. Parameter vectors, group errors and all predictions are supplied; population confidence claims are not justified by this small or single-system campaign.

The useful contribution is an executable, auditable test of the stated response and its alternatives. No independent experiment, exhaustive novelty adjudication, validated deployment benefit or new universal physical law is claimed. Source-author analyses are prior art. Current outcomes are exposed and cannot become a fresh holdout by renaming this task.

## Reproduce or evaluate another finding

Run `python run.py` in this folder to verify integrity and reproduce saved predictions and metrics. `python run.py --input INPUT.csv --output predictions.csv` applies all frozen equations to a compatible input table. `task_spec.json` defines allowed inputs, calibration, units and grouping; use the shared Principia-100 evaluator for comparable prediction submissions. A different endpoint or information budget requires a separate frozen task.

The numerical score is equal-group MAE, supplemented by group RMSE, bias, error quantiles and applicable physical checks. Predictive accuracy and mechanistic/novelty review are separate; abstention and valid alternative discoveries remain admissible.

## Source and prior art

[Primary source study](https://arxiv.org/html/2509.15463v1); [authoritative dataset](https://data.nist.gov/od/id/mds2-3951). See `SOURCE_MANIFEST.json` for byte-level provenance and research history for the native-semantics audit, exclusions and literature record.
