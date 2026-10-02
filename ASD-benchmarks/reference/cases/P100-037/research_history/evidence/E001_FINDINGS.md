# Router power under changing traffic
> P100-037 | Scenario and findings | September 2026 reference results

The practical question is whether current traffic can predict electrical power with a compact, interpretable equation. The pilot supports workload-based prediction on two measured routers, but does not identify separate physical energy costs or establish a new power law.

## 1. Scenario and available measurements

The Telefónica/Universidad Politécnica de Madrid deposit contains 15 semicolon-delimited CSV runs: five router/traffic-protocol combinations, each repeated three times. The measurements include electrical power in watts, throughput in Gbit/s, packet size in bytes and native timestamps. The traffic patterns vary load, packet length and mixtures of flows. The supplied capacity is 200 Gbit/s; the packaged predictor covers packet sizes from 62 to 1,500 bytes.

The data mix experimental controls with measured responses. Packet rate is an algebraic proxy calculated from throughput and packet size, not an additional independent sensor. For mixed flows, the supplied mean packet size cannot resolve the underlying packet distribution. No temperature channel or instrument-repeatability estimate is available.

## 2. Experimental method

Repetitions 1 and 2 supplied ten development runs; repetition 3 supplied five complete reserved runs. Six substantive attempts compared bounded workload responses, interactions and causal memory. Development used whole-run validation. The selected equation and all comparators were fixed before confirmation. No row-wise random split was used.

The final static predictors use router identity, current throughput and current packet size. Measured power history and future traffic are excluded. All 27,692 reserved input rows remain represented; one missing power value leaves 27,691 scored responses. Power is neither imputed nor filtered according to prediction error.

## 3. Tested equation and physical interpretation

Let *B* denote throughput, *L* packet size, and *R* the effective packet rate in packets/s, obtained by converting *B* to bit/s and dividing by 8*L* bits per packet. Define dimensionless workload variables:

$$
u=\dfrac{B}{200\,\mathrm{Gbit}\,\mathrm{s}^{-1}},\qquad q=\dfrac{R}{10^8\,\mathrm{s}^{-1}},\qquad s=\dfrac{q}{0.03+q}.
$$

The selected compact model is:

$$
\widehat P=b_0+b_u u+b_s s+b_{us}us.
$$

The intercept represents baseline power; the saturating term describes a bounded packet-workload response, and its interaction with *u* allows that response to vary with byte load. These are interpretable model components, not independently measured energy mechanisms. Separate coefficients are fitted for each router; all coefficients below are in watts and are rounded for presentation.

| Router | *b*<sub>0</sub> | *b*<sub>u</sub> | *b*<sub>s</sub> | *b*<sub>us</sub> |
|---|---|---|---|---|
| A | 704.2433 | -18.0702 | 10.0829 | 39.1871 |
| B | 69.8802 | 6.4945 | 0.5501 | 6.4486 |

<!-- pagebreak -->

## 4. Findings and predictive performance

**Traffic composition improves on throughput alone, but the compact hypothesis is not the best predictor.** The compact model reduces mean run error by 6.17% relative to throughput-only prediction. The flexible workload model, which adds polynomial and log-packet-size terms, is still better: the compact model has 7.35% higher error and wins only one of five reserved runs.

| Frozen model | Mean run MAE (W) |
|---|---|
| Compact saturation model, selected before confirmation | 4.00588 |
| Flexible workload comparator | 3.73154 |
| Throughput-only comparator | 4.26914 |

For *G* complete runs, with *n* measured responses in each run, the primary measure is:

$$
E_{\mathrm{MAE}}=\dfrac{1}{G}\sum_{g=1}^{G}\dfrac{1}{n_g}\sum_{i=1}^{n_g}|\widehat P_{gi}-P_{gi}|,\qquad G=5.
$$

Each run receives equal weight. This reports typical absolute power error in watts; it is not classification accuracy or a guaranteed engineering tolerance. The compact model's run-specific MAEs range from 1.28 to 8.55 W, showing that the overall average masks substantial operating-condition variation.

**Component energy costs remain unidentified.** Router A's standalone throughput coefficient is negative. Although the total fitted response increases on the checked fixed-packet-size grid, individual terms cannot be read as independent positive processing costs. The historical memory models also lacked measured temperature evidence; one native clock inconsistency further limits a dynamic interpretation.

## 5. Practical value and limits

This case provides reproducible comparators for power estimation from readily available traffic telemetry. It shows why byte load and packet composition deserve separate attention, and quantifies the accuracy sacrificed by a compact equation. Such estimates could inform workload accounting or capacity studies after validation on the intended equipment; no energy-saving intervention was tested here.

The evidence concerns two calibrated routers and five reserved runs, not an independent population of devices. Hardware transfer, thermal causation and microscopic per-packet energy are unverified. The small, system-dependent group count is reported through individual run errors rather than a falsely precise population confidence interval.

## 6. Evidence and use

Reproduction: run `python run.py` from this folder. Exact coefficients are in `rules.json`; predictions, aggregate errors and run-level errors are in `evidence/`. The source rows and measured targets remain linked in `data/observations.csv.gz`.

Evaluation: `evaluator/README.md` defines submissions, scoring and optional executable replay. It accepts alternative equations, compares all frozen models on matched samples, and separates numerical performance from scientific review.

Status: this is scoped reference evidence, not an admitted new physical law. All confirmation targets are now exposed; subsequent revisions need new unexposed runs for fresh confirmation. No fitting or model selection was performed for this introduction.

Source: Lentisco and colleagues, Telefónica/UPM router experiments, [Zenodo record 17282065](https://zenodo.org/records/17282065), DOI 10.5281/zenodo.17282065. Source provenance and asset hashes are recorded in `rules.json`.
