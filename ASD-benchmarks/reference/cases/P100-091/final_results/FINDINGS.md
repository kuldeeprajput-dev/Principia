# Private 5G latency: what transfers across locations?

## Scenario and practical question

The TU Wien source contains 210 UDP trials: seven indoor locations, six configured rates and five repeats per setting. Each approximately 60-second iPerf run reports a mean one-way end-to-end delay. Three source-disclosed clock-wrap records are excluded without imputation, leaving 207 measured responses. The path includes campus routing, the 5G core/radio, customer equipment and a WiFi link.

We ask whether a compact equation reconstructs mean delay at a previously uncalibrated location using configured rate and achieved same-run throughput. This is an after-run diagnostic task. It is not a pre-run latency promise, radio-only model or causal congestion experiment. Native logs, units, exclusions and source anchors are audited in the retained research record.

## Method and frozen equation

Five complete locations supply 147 development trials. Q4 and Q5 supply 60 reserved trials. Development uses leave-one-location-out validation; kernel tuning is nested within its training locations. Whole-location grouping keeps rates and repetitions together. Every candidate was frozen before the two confirmation scores were opened. The primary error is the unweighted mean of location-specific MAE in milliseconds.

Five substantive attempts test global traffic deficit, finite-setting response, within-setting correction, a high-load hinge and monotonicity. Attempt 003 was selected by development error and remains the reference despite its later failure to beat the flexible control.

For configured rate $a$ and achieved rate $b$, both in Mbit/s, the equivalent centered equation is

$$
\widehat L=\max\{0,m_a+1.179\,(b-1.05a)\}\quad\mathrm{ms}.
$$

| Configured rate $a$ (Mbit/s) |1|10|50|100|200|500|
|---|---:|---:|---:|---:|---:|---:|
|$m_a$ (ms)|5.123|10.509|14.001|12.313|13.601|29.229|

The coefficient 1.179 has units ms/(Mbit/s). The dimensionless 1.05 is only an algebraic recentering for readability; the executable state stores the uncentered exact coefficients. No interpolation between the six settings is admitted. All coefficients are estimated from development locations, with no held-out latency calibration.

<!-- pagebreak -->

## Evidence and interpretation

| Model | Development group MAE (ms) | Confirmation group MAE (ms) |
|---|---:|---:|
| Selected operating-point plus throughput rule |1.5094|2.1956|
| Operating-point medians without throughput |1.5841|1.9458|
| Monotonic operating-point medians |1.6181|1.9171|
| Nested flexible RBF control |1.6108|1.9165|
| Regularized source-family queue control |2.3271|3.0181|
| Achieved-throughput affine control |2.4882|2.9530|

The selected rule improves the queue control by 27.3% on average, but is 14.6% worse than the flexible control. Its Q4/Q5 errors are 1.6631/2.7280 ms, compared with 1.7619/2.0710 ms for RBF. Thus the claimed gain from the within-setting slope fails overall confirmation. The later better controls remain comparators; they were not promoted after seeing confirmation.

The useful result is a bounded calibration recipe and an informative failure. Setting-specific response is more transferable here than a globally smooth queue approximation. However, adding a coefficient that looks like processing cost can improve development and degrade a new location. A 0.5 Mbit/s change in achieved-rate reporting changes the frozen equation by 0.5895 ms, making report precision relevant.

The difference$a-b$ is not measured packet loss: achieved rate is about 1.05-1.06 times configured rate in development. Neither that difference nor a fitted capacity pole identifies network physics. The source paper already studies queue-like delay and parameter identifiability. No new physical law or demonstrated operational benefit is claimed.

## Use, limitations and evaluation

`run.py` and `rules.json` reproduce every frozen model. `evidence/` contains predictions, aggregate metrics and both location results; `TASK.md` states the information budget and shared evaluator commands. Alternative equations are welcome under the same endpoint and cohort. Different endpoints require a separately reviewed task.

Only two reserved locations from one installation were tested. Clock synchronization is not independently verified; delay tails and independent deployment transfer remain unresolved. All current targets are now exposed, so future scoring is retrospective. The supported scope is an empirical reference with preserved counterexamples, not a universal communications law.

## Sources

Bodur et al., Measurement-Driven Modeling of End-to-End Latency in an Indoor Private Standalone 5G Network, Network 6(3), 78 (2026), DOI 10.3390/network6030078. Pinned data: DOI 10.48436/hja53-s8y18,v1.0.0. Data: CC BY 4.0; source code: MIT. iPerf 2 user manual supplies report semantics. The complete targeted literature record is retained in `PRIOR_ART.json`.
