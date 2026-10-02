# P100-063: Temperature-transfer magnon noise

## What the scenario contains

All 77, 293 and 389 K traces were used for whole-temperature leave-out development; all 195 and 352 K traces were reserved. Field traces and frequency bins are nested within temperature. Source background subtraction is retained and disclosed; it is not fitted by this campaign. The endpoint is noise power spectral density, reported in nV^2/Hz. Native files remain unchanged; preparation is deterministic and hash-verified.

## Supported result and its interpretation

The measured thermal peak/dip response is reproducible with a compact Lorentzian family across two reserved termination temperatures. The extra dispersive term is effectively tied with the symmetric control; no new magnon law is established.

**Admission:** supported; **classification:** reproduction.

Let $f$ be frequency in GHz, $B$ magnetic field in tesla and $T$ termination temperature in kelvin. The film temperature stays near 293 K. Define


$$
\theta=(T-293)/200,\quad f_r=f_0+s_B(B-0.1702),\quad z=(f-f_r)/w,\quad L=(1+z^2)^{-1}.
$$


The selected model is


$$
\widehat S_n=b_0+b_T\theta-A\theta[L+\eta zL].
$$


$S_n,b_0,b_T,A$ are in nV$^2$/Hz; $w,f_0$ are in GHz and $s_B$ in GHz/T. The local resonance-field relation avoids separately claiming magnetization and gyromagnetic ratio from a narrow field interval. The dispersive coefficient does not establish an independent new mechanism.

| Coefficient | Value | Unit |
|---|---:|---|
| `f_0` | 6.9953488 | GHz |
| `s_B` | 29.430891 | GHz/T |
| `w` | 0.0058164879 | GHz |
| `b_0` | 0.20871222 | nV^2/Hz |
| `b_T` | 0.031358887 | nV^2/Hz |
| `A` | 0.029570047 | nV^2/Hz |
| `eta` | 0.086292151 | dimensionless |

## Validation and performance

The selected reference was fixed after 5 substantive development attempts. Whole-group development MAE was **0.00970574**; reserved-group MAE was **0.00297729 nV^2/Hz** across 30030 scored rows and 2 top-level groups. Groups, not individual dependent rows, define the scope of validation.

| Model | Confirmation MAE |
|---|---:|
| Selected: Thermal Lorentzian plus dispersion | 0.00297729 |
| Constant response | 0.0108667 |
| Polynomial field-temperature response | 0.00338083 |
| Symmetric thermal Lorentzian | 0.00297917 |

The lowest observed confirmation error among all frozen models is 0.0029663 for Common frequency background. This is a diagnostic comparison; it does not replace the development-selected reference.

Additional diagnostic figure: [Confirmation evidence](evidence/confirmation.png).

## Failures, limitations and value

Extra temperature-dependent linewidth and nonlinear-amplitude terms lack transfer evidence. Their development errors exceed the simpler thermal family; source termination heating must not be silently interpreted as film heating. All attempts and unfavorable results remain traceable in research history. Parameter vectors, group errors and all predictions are supplied; population confidence claims are not justified by this small or single-system campaign.

The useful contribution is an executable, auditable test of the stated response and its alternatives. No independent experiment, exhaustive novelty adjudication, validated deployment benefit or new universal physical law is claimed. Source-author analyses are prior art. Current outcomes are exposed and cannot become a fresh holdout by renaming this task.

## Reproduce or evaluate another finding

Run `python run.py` in this folder to verify integrity and reproduce saved predictions and metrics. `python run.py --input INPUT.csv --output predictions.csv` applies all frozen equations to a compatible input table. `task_spec.json` defines allowed inputs, calibration, units and grouping; use the shared Principia-100 evaluator for comparable prediction submissions. A different endpoint or information budget requires a separate frozen task.

The numerical score is equal-group MAE, supplemented by group RMSE, bias, error quantiles and applicable physical checks. Predictive accuracy and mechanistic/novelty review are separate; abstention and valid alternative discoveries remain admissible.

## Source and prior art

[Primary source study](https://arxiv.org/html/2404.17327v1); [authoritative dataset](https://kondata.uni-konstanz.de/radar/en/dataset/iRRYHMPwMObNsUOM). See `SOURCE_MANIFEST.json` for byte-level provenance and research history for the native-semantics audit, exclusions and literature record.
