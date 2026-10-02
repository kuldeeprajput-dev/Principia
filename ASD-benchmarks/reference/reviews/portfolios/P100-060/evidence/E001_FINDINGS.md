# Ultrasonic transmission response: a scoped ASD reference
> Principia-100 | Case 60 | Conditional pulse-response reference; aggregate improvement with regime counterexamples

## 1. Scenario and measured quantities

Zenodo 17266427; TU Graz Jakob Harden, converted MATLABv 6 exports. Native embedded measurement timestamps in 2020; technical description 2023, MAT export 2025. Export date is not acquisition date.. The pilot target is **Post-trigger peak absolute receiver voltage** in **V**, with 300 development and 60 reserved prepared observations. Source bytes remain unchanged; prepared target/predictor transformations are labeled analysis products.

## 2. Experimental design

Five pulse widths develop the models; one 5 us width is reserved across all six distance/sensor conditions. All ten pulses per file stay together. Target preparation uses the whole post-trigger trace after pre-trigger mean subtraction. 6 substantive attempts tested competing physical or process explanations. Baseline reproduction is excluded from that count. All scales, coefficients and tuning are trained inside applicable development folds. Direct and residual Gaussian-kernel comparators share the same available information. Candidate selection and stopping were frozen before the separate final scoring process; no final-score-driven revision occurred.

## 3. Executable equation and interpretation

$$
\widehat{A}_{ds}=a_{ds}\max[1,\sqrt{1+e^{-2w/12}-2e^{-w/12}\cos(2\pi fw)}]
$$

w is pulse width in microseconds; f is nominal resonance in cycles per microsecond (kHz/1000). The effective damping time 12 us was selected on development widths. Six calibrated gains in V are 12.271204, 0.941597, 0.00302123, 0.000609934, 0.00227582, 0.000462384 for(d0,f110),(d0,f500),(d20,f110),(d20,f500),(d50,f110),(d50,f500). The maximum accounts for an initial pulse edge before the second edge; it is a phenomenological peak approximation. Sensor type is confounded with nominal resonance.

<!-- pagebreak -->

## 4. Findings, accuracy and counterexamples

| Frozen model | Final MAE (V) |
|---|---:|
| reference | 0.356202 |
| challenger | 0.863519 |
| baseline_linear_width | 2.180363 |
| baseline_mean | 0.780303 |
| baseline_rbf | 1.097194 |
| baseline_residual_rbf | 0.622043 |

Reference MAE is 0.356202 V versus 0.622043 V for the strongest fixed comparator, a42.74 percent aggregate reduction. Against constant gain, only zero-distance 110 kHz improves; all five other conditions worsen. Its contact 110 error is 1.478 V, contact 500 error 0.656 V; air errors are 0.000215-0.001453 V. The amplitude range makes aggregate gain contact-dominated. Treat this as a conditional instrument-response reference, not an air-propagation or universally useful pulse law.

## 5. Applicability, practical value and limits

Six condition files at one reserved 5 us width, not six independent reserved width experiments. Gain is concentrated in zero-distance 110 kHz contact; air and 500 kHz sensor counterexamples remain. The equation and preserved falsifications provide an auditable test of whether an ASD agent can produce a useful conditional numerical relationship. They do not establish industrial savings, causal mechanism or universal transfer. The source-aware corpus contains known physics and previously analyzed observations; no previously unknown physical law is admitted. Individual group errors are reported, without row-level confidence intervals that treat repeated samples as independent.

## 6. Reproduction and scientific status

run.py checks package hashes and reproduces all predictions/metrics without fitting. rules.json contains full precision coefficients and calibration. The evaluator accepts alternative equations and abstention, scores common rows fairly and keeps scientific review separate from numerical scoring. All targets are now exposed. Fresh confirmation of a later method requires new reserved experimental groups. Computational review is a separate checking phase by the same operator, not independent experimental replication or human adjudication.

Source: [Authoritative release](https://zenodo.org/records/17266427); [Author test-series 3 technical description](https://doi.org/10.3217/ph0jm-8ax76). Evidence: `evidence/metrics.csv`, `by_group.csv`, `sample_anchors.csv.gz` and the source/units audit. Rejected hypotheses remain in research history.
