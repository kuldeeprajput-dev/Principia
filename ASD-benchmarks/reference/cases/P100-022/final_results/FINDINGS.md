# P100-022: First-forming current across perovskite devices

## What the scenario contains

A fixed SHA-256 allocation reserved ten complete devices per composition. Development used five hash-assigned device folds. Exact duplicate native traces were linked and deduplicated. The task predicts the initial positive forming branch from voltage and composition alone; no current calibration or later sweep is a predictor. The endpoint is initial positive forming-sweep current, reported in microampere. Native files remain unchanged; preparation is deterministic and hash-verified.

## Supported result and its interpretation

A compact composition-conditioned forming-current equation improves the logistic control and is essentially tied with a larger spline on reserved devices. Its negative I-rich precursor coefficient prevents admission as a new physical conduction law.

**Admission:** partially supported; **classification:** validated extension.

For composition $c\in\{\mathrm{I},\mathrm{Br}\}$, define $q_c(V)=[1+\exp(-(V-v_c)/w_c)]^{-1}$. The selected predictor is


$$
\widehat I(V,c)=[1-q_c(V)]g_c V+C_c q_c(V).
$$


$I$ is in microamperes, $V,v_c,w_c$ in volts, $g_c$ in microamperes per volt and $C_c$ in microamperes. The fitted turn-on describes an ensemble of different first-forming devices. It must not be confused with an individual device's deterministic switching threshold. The negative I-rich $g_c$ rules out interpreting both fitted precursor coefficients as physical Ohmic conductances.

| Coefficient | Value | Unit |
|---|---:|---|
| `C_I` | 1141.5889 | microampere |
| `v_I` | 0.70008043 | V |
| `w_I` | 0.056872858 | V |
| `g_I` | -17.001943 | microampere/V |
| `C_Br` | 1150.7323 | microampere |
| `v_Br` | 0.50504391 | V |
| `w_Br` | 0.051874973 | V |
| `g_Br` | 578.78751 | microampere/V |

## Validation and performance

The selected reference was fixed after 5 substantive development attempts. Whole-group development MAE was **89.2474**; reserved-group MAE was **74.9489 microampere** across 1900 scored rows and 20 top-level groups. Groups, not individual dependent rows, define the scope of validation.

| Model | Confirmation MAE |
|---|---:|
| Selected: Ohmic precursor plus turn-on | 74.9489 |
| Constant response | 481.943 |
| Composition-specific cubic spline | 74.8678 |
| Logistic forming distribution | 83.2743 |

The lowest observed confirmation error among all frozen models is 74.8678 for Composition-specific cubic spline. This is a diagnostic comparison; it does not replace the development-selected reference.

Additional diagnostic figure: [Confirmation evidence](evidence/confirmation.png).

## Failures, limitations and value

Treating every fitted precursor as a positive physical conductance is unsupported. The selected I-rich coefficient is negative; the model must remain an empirical ensemble surrogate, and a flexible control is marginally better in confirmation. All attempts and unfavorable results remain traceable in research history. Parameter vectors, group errors and all predictions are supplied; population confidence claims are not justified by this small or single-system campaign.

The useful contribution is an executable, auditable test of the stated response and its alternatives. No independent experiment, exhaustive novelty adjudication, validated deployment benefit or new universal physical law is claimed. Source-author analyses are prior art. Current outcomes are exposed and cannot become a fresh holdout by renaming this task.

## Reproduce or evaluate another finding

Run `python run.py` in this folder to verify integrity and reproduce saved predictions and metrics. `python run.py --input INPUT.csv --output predictions.csv` applies all frozen equations to a compatible input table. `task_spec.json` defines allowed inputs, calibration, units and grouping; use the shared Principia-100 evaluator for comparable prediction submissions. A different endpoint or information budget requires a separate frozen task.

The numerical score is equal-group MAE, supplemented by group RMSE, bias, error quantiles and applicable physical checks. Predictive accuracy and mechanistic/novelty review are separate; abstention and valid alternative discoveries remain admissible.

## Source and prior art

[Primary source study](https://advanced.onlinelibrary.wiley.com/doi/10.1002/admt.202502152); [authoritative dataset](https://zenodo.org/records/17278410). See `SOURCE_MANIFEST.json` for byte-level provenance and research history for the native-semantics audit, exclusions and literature record.
