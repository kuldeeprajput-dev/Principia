# Mobile-network latency: a scoped ASD reference
> Principia-100 | Case 100 | Scoped latency forecast extension; small aggregate gain and run counterexamples

## 1. Scenario and measured quantities

Zenodo 14635635, Vigo/Málaga 6G-MOBKPI on 6G-SANDBOX platform. Nov 20-22, 2024; releaseJan 2025. The pilot target is **Next successful ICMP probe RTT** in **ms**, with 5965 development and 2943 reserved prepared observations. Source bytes remain unchanged; prepared target/predictor transformations are labeled analysis products.

## 2. Experimental design

Six complete PING runs develop the models; three complete runs are reserved, one per route. Five previous completed probes and radio observations asof the previous completion are permitted. The current response timestamp, sequence phase and cumulative target averages are excluded. 6 substantive attempts tested competing physical or process explanations. Baseline reproduction is excluded from that count. All scales, coefficients and tuning are trained inside applicable development folds. Direct and residual Gaussian-kernel comparators share the same available information. Candidate selection and stopping were frozen before the separate final scoring process; no final-score-driven revision occurred.

## 3. Executable equation and interpretation

$$
\widehat r_{n+1}=\max[0,r_n+c_q+0.675521(\overline{r}_5-r_n)+0.085666(r_n-55)_+-0.662004(r_n-r_{n-1})]
$$

r_n and r_(n−1) are completed previous RTTs in milliseconds; rbar 5 averages the last five completed probes. c_q in ms is−0.002897 for indoor random,−0.069945 for indoor rectangle and−0.049676 for outdoor rectangle. The 55 ms breakpoint was selected using nested development groups. Payload and causal radio measurements are available to comparators, but the selected equation uses history and the calibrated route offset only. It predicts a conditional successful next response, not a missing lost-packet RTT.

<!-- pagebreak -->

## 4. Findings, accuracy and counterexamples

| Frozen model | Final MAE (ms) |
|---|---:|
| reference | 2.070016 |
| challenger | 3.351972 |
| baseline_persistence | 13.071518 |
| baseline_rbf | 2.479101 |
| baseline_residual_rbf | 2.105397 |
| baseline_rolling | 8.094475 |
| baseline_static | 8.024929 |

Reference equal-run MAE is 2.070016 ms versus residual-kernel 2.105397 ms, a1.68 percent aggregate reduction. It loses to that comparator on two of three runs, and persistence wins the indoor rectangle run 2.310924 versus 2.430185 ms. A large gain over trailing-mean and persistence establishes information in short latency history, not a causal queue or scheduler mechanism. One lost packet has no RTT target; 2942 of 2943 assigned rows are scored.

## 5. Applicability, practical value and limits

Three complete PING runs, one per calibrated route, one platform; online previous-probe calibration. No new-network or packet-loss reliability prediction. The equation and preserved falsifications provide an auditable test of whether an ASD agent can produce a useful conditional numerical relationship. They do not establish industrial savings, causal mechanism or universal transfer. The source-aware corpus contains known physics and previously analyzed observations; no previously unknown physical law is admitted. Individual group errors are reported, without row-level confidence intervals that treat repeated samples as independent.

## 6. Reproduction and scientific status

run.py checks package hashes and reproduces all predictions/metrics without fitting. rules.json contains full precision coefficients and calibration. The evaluator accepts alternative equations and abstention, scores common rows fairly and keeps scientific review separate from numerical scoring. All targets are now exposed. Fresh confirmation of a later method requires new reserved experimental groups. Computational review is a separate checking phase by the same operator, not independent experimental replication or human adjudication.

Source: [Authoritative release](https://zenodo.org/records/14635635); [Source platform and measured KPI release](https://zenodo.org/records/14635635). Evidence: `evidence/metrics.csv`, `by_group.csv`, `sample_anchors.csv.gz` and the source/units audit. Rejected hypotheses remain in research history.
