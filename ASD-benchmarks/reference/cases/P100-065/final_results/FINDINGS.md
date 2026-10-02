# P100-065: Injection-ratio laser noise transfer

## What the scenario contains

The −30 and −15 dB spectra were developed with four complete log-frequency-band folds; the entire −20 dB spectrum was reserved. Both ratio conditions remain in each development training fold. Confirmation therefore adds ratio interpolation beyond the spectral-band validation used for selection. The endpoint is log frequency-noise spectral density, reported in dB re 1 Hz^2/Hz. Native files remain unchanged; preparation is deterministic and hash-verified.

## Supported result and its interpretation

A compact sum of feedback-sensitive and common noise contributions predicts the reserved injection ratio, but the selected extension loses to the simpler fixed-exponent domain control. This supports bounded reproduction and model ambiguity, not a new laser-noise law.

**Admission:** partially supported; **classification:** reproduction.

Let $q=f/(10^4\,\mathrm{Hz})$ and $r=10^{R/10}$, where $R$ is the injection ratio in dB. The selected frozen spectrum is


$$
\widehat S_\nu(f,R)=A/r+B/q^{\alpha}+C,\qquad\widehat y=10\log_{10}\!\left[\frac{\widehat S_\nu}{1\,\mathrm{Hz}^2/\mathrm{Hz}}\right].
$$


$A,B,C$ are nonnegative noise-density coefficients in Hz$^2$/Hz; $\alpha$ is dimensionless. This separates feedback-sensitive and shared contributions phenomenologically. With two development ratios, a common white floor and a changed feedback exponent are competing, nearly indistinguishable explanations.

| Coefficient | Value | Unit |
|---|---:|---|
| `log10(A)` | -2.94428 | log10 relative to 1 Hz^2/Hz |
| `log10(B)` | -0.87677569 | log10 relative to 1 Hz^2/Hz |
| `alpha` | 2.0179107 | dimensionless |
| `log10(C)` | -1.0358948 | log10 relative to 1 Hz^2/Hz |

## Validation and performance

The selected reference was fixed after 5 substantive development attempts. Whole-group development MAE was **3.865**; reserved-group MAE was **3.04917 dB** across 401 scored rows and 1 top-level groups. Groups, not individual dependent rows, define the scope of validation.

| Model | Confirmation MAE |
|---|---:|
| Selected: Shared white floor plus feedback | 3.04917 |
| Constant response | 11.6166 |
| Cubic spectral surface | 3.16575 |
| Inverse-feedback floor plus f^-2 noise | 3.01527 |

The lowest observed confirmation error among all frozen models is 2.9116 for Two fixed colored-noise components. This is a diagnostic comparison; it does not replace the development-selected reference.

Additional diagnostic figure: [Confirmation evidence](evidence/confirmation.png).

## Failures, limitations and value

Extra spectral components are not automatically better than the fixed physical comparator. The chosen shared-floor extension loses to the fixed f^-2/inverse-feedback control; a later-looking best confirmation candidate is explicitly not promoted. All attempts and unfavorable results remain traceable in research history. Parameter vectors, group errors and all predictions are supplied; population confidence claims are not justified by this small or single-system campaign.

The useful contribution is an executable, auditable test of the stated response and its alternatives. No independent experiment, exhaustive novelty adjudication, validated deployment benefit or new universal physical law is claimed. Source-author analyses are prior art. Current outcomes are exposed and cannot become a fresh holdout by renaming this task.

## Reproduce or evaluate another finding

Run `python run.py` in this folder to verify integrity and reproduce saved predictions and metrics. `python run.py --input INPUT.csv --output predictions.csv` applies all frozen equations to a compatible input table. `task_spec.json` defines allowed inputs, calibration, units and grouping; use the shared Principia-100 evaluator for comparable prediction submissions. A different endpoint or information budget requires a separate frozen task.

The numerical score is equal-group MAE, supplemented by group RMSE, bias, error quantiles and applicable physical checks. Predictive accuracy and mechanistic/novelty review are separate; abstention and valid alternative discoveries remain admissible.

## Source and prior art

[Primary source study](https://eprints.soton.ac.uk/507397/1/prj-13-3-611.pdf); [authoritative dataset](https://eprints.soton.ac.uk/497413/). See `SOURCE_MANIFEST.json` for byte-level provenance and research history for the native-semantics audit, exclusions and literature record.
