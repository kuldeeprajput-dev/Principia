# Targeted audit of eight earlier portfolios

Targeted scientific-quality audit of eight preserved existing portfolios. No source data, model states, historical scores, or reference selections were changed. Source acquisition and new fitting were outside scope.

All evaluation outcomes are exposed. Each comparison below retains its own task version and cohort. A lower retrospective candidate score is not a reference promotion.

## P100-083

A modest, calibrated one-hour hive-temperature forecast is supported; thermal conductance, biological setpoints and thermoregulation are not identified. Physically signed passive and weather-increment challengers fail stronger flexible controls.

| Task/cohort | Primary metric | Selected reference | Strongest control |
|---|---|---:|---:|
| P100-083.original.v1 / P100-083.original.v1.cohort-1 | RMSE (degC); 5 groups | reference: 0.204548276 | baseline_residual_rbf: 0.202102597 |
| P100-083.round2.v1 / P100-083.round2.v1.development-oof | RMSE (degC); 15 groups | current/cycle-001: 0.186824253 | previous/baseline-flex: 0.160961448 |

**Scope and input access.** Five sensor streams in one apiary are not independent colonies/sites. Species, sensor placement and season are confounded. Causal one-hour lag and target matching tolerances matter; original uses future dates while round2 is development OOF with an extra ambient lag. Negative ambient-gradient coefficient cannot be positive passive conductance; 35.72 degC derived coefficient combination is not a measured brood setpoint.

**Claim-quality issues.** Round2 calibration prose appends coefficients of the older reference after the training-scope description; future readers should use per-fold states, not treat those old coefficients as the round2 equation. The original reference loses to residual kernel; continuation loses13/15 blocks. These negative outcomes deserve equal prominence.

**Next improvements.**
- Add independent apiaries and colonies with sensor placement and response calibration; reserve complete seasons/sites.
- Obtain heat-flow or controlled perturbation evidence before interpreting conductance or active regulation.
- Keep statistical forecast quality separate from biological mechanism and verify timestamp tolerances in external submissions.

No new blocking numerical defect is established by this documentary audit. Exact inspected file hashes and complete versioned comparisons are in the companion JSON.

## P100-085

The unit mass-recovery equation is a transparent contemporaneous assay screening control, not a new stoichiometric law or a superior estimator. The duplicate bioreactor payloads cannot establish a feed-regime contrast.

| Task/cohort | Primary metric | Selected reference | Strongest control |
|---|---|---:|---:|
| P100-085.original.v1 / P100-085.original.v1.cohort-1 | MAE (g/L); 1 groups | reference: 0.945 | baseline_flexible: 0.379298538 |

**Scope and input access.** Only one reserved condition with four targets; all four targets were visible during schema preview, so evaluation is retrospective even historically. Current ethylene-glycol depletion and pH are measured inputs; the task is neither an online forecast nor replacement of laboratory GA assay. Mass recovery ratio1 differs from molecular stoichiometry, and cofeeding pathways are not isolated.

**Claim-quality issues.** The flexible control substantially beats the selected screening reference; preserve that adverse comparison. Failure of five mechanisms in development cannot universally falsify those mechanisms; several look better on the single exposed condition.

**Next improvements.**
- Obtain independently repeated medium/pH conditions with assay uncertainty and carbon-balance measurements.
- Resolve identical but oppositely named bioreactor files with the depositor before any feed-regime scientific claim.
- Test proposed kinetics with controlled substrate/cofeed experiments and a genuinely unexposed whole-condition cohort.

No new blocking numerical defect is established by this documentary audit. Exact inspected file hashes and complete versioned comparisons are in the companion JSON.

## P100-086

A multiscale causal-history ensemble improves six-hour potency forecasting relative to the secant under a declared assay-history budget. This is a conditional forecasting contribution, not an identified biochemical growth law or demonstrated online industrial benefit.

| Task/cohort | Primary metric | Selected reference | Strongest control |
|---|---|---:|---:|
| P100-086.continuation.v1 / P100-086.continuation.v1.cohort-1 | MAE (source potency unit (undocumented)); 81 groups | reference: 24.4844186 | ar: 33.9848216 |
| P100-086.original.v1 / P100-086.original.v1.cohort-1 | MAE (source potency unit (undocumented)); 81 groups | reference: 37.759076 | baseline_domain: 37.759076 |

**Scope and input access.** Native hx potency units and source assay receipt times remain undocumented; numerical source-clock causality is not proven production-time availability. Source smoothness audit reports92.646% of39,217 hourly triples with second differences <=1 native unit; interpolation lineage remains unresolved. Original and continuation have different information budgets. The latter admits1/3/6/12h history; both cohorts contain81 later batch IDs within a single production dataset.

**Claim-quality issues.** The original development-selected secant remains reference even though several exposed diagnostic models score lower. Continuation gain is substantial but no contract-matched comparison to author MASTER exists, and artificial delay sensitivity exposes operational risk. Use native potency units; never relabel asmg/L orU/mL.

**Next improvements.**
- Obtain laboratory timestamp, receipt delay, interpolation lineage and physical unit metadata before claiming online deployment.
- Benchmark delay-aware histories with real assay arrival times, then reserve later production campaigns.
- Measure production decision utility under prespecified costs, constraints and matched source-model access.

No new blocking numerical defect is established by this documentary audit. Exact inspected file hashes and complete versioned comparisons are in the companion JSON.

## P100-087

Previous own contribution is the strongest tested next-round forecast in the retained first-session games; five richer behavioral responses provide informative negative evidence, not new behavioral laws.

| Task/cohort | Primary metric | Selected reference | Strongest control |
|---|---|---:|---:|
| P100-087.original.v1 / P100-087.original.v1.cohort-1 | MAE (experimental tokens); 55 groups | reference: 0.364646465 | baseline_persistence: 0.364646465 |

**Scope and input access.** Complete interacting pairs are held together;55 held pairs remain from one university laboratory sample. Strictly previous own/peer actions and announced rules are permitted, including earlier held-pair actions as online history. This is not a fixed-horizon unseen-pair trajectory prediction. Type2 duplicates and session2 participant reuse are excluded; treatment associations are not causal policy effects.

**Claim-quality issues.** No fitted behavioral extension beats persistence on the declared objective. Rare changes can be obscured by MAE even when average persistence is strong. Threshold success is a rule identity; predicting contributions is the independent target.

**Next improvements.**
- Prespecify a change-event task with scientifically meaningful token thresholds and report precision, recall, calibration and per-treatment errors alongside MAE.
- Test whole-session/laboratory/treatment transfer on fresh pairs without repurposing exposed outcomes.
- Separate descriptive forecasts from causal reciprocity or incentive-effect hypotheses requiring randomized contrasts.

No new blocking numerical defect is established by this documentary audit. Exact inspected file hashes and complete versioned comparisons are in the companion JSON.

## P100-091

A finite offered-rate rule with achieved-throughput correction improves a regularized queue curve but loses to the matched flexible control. The data do not identify network capacity or packet loss from a fitted pole/throughput difference.

| Task/cohort | Primary metric | Selected reference | Strongest control |
|---|---|---:|---:|
| P100-091.original.v1 / P100-091.original.v1.cohort-1 | MAE (ms); 2 groups | reference: 2.19555683 | baseline_rbf: 1.91645742 |

**Scope and input access.** Contemporaneous achieved throughput is measured after the60-second trial; this is conditional latency reconstruction, not prospective offered-load prediction. Only two held locations in a single seven-location installation; all offered rates and repetitions stay linked. Endpoint is mean one-way end-to-end UDP latency, not pure radio latency; source clock/synchronization and complete-stack contributions limit mechanisms.

**Claim-quality issues.** Reference MAE improves a queue comparator but RMSE4.4458ms is worse than flexible2.9480ms; mean-error claims should include tail degradation. Six offered-rate offsets are calibration parameters, so no unseen-rate extrapolation is established. Neither offered-minus-achieved throughput nor an unstable fitted queue pole is an independent physical loss/capacity measurement.

**Next improvements.**
- Preserve flexible and finite-rate lookup baselines under identical same-run input access.
- Add fresh locations/installations and controlled offered-rate/interference experiments with synchronized packet-level latency/loss logs.
- If prospective control is desired, freeze a new task without same-run achieved throughput; use tail quantiles and operational limits justified externally.

No new blocking numerical defect is established by this documentary audit. Exact inspected file hashes and complete versioned comparisons are in the companion JSON.

## P100-092

Compact contrast or positive-power corrections offer a readable calibration-drift description, but do not beat flexible prediction and do not establish propagation physics or reduced calibration cost.

| Task/cohort | Primary metric | Selected reference | Strongest control |
|---|---|---:|---:|
| P100-092.original.v1 / P100-092.original.v1.cohort-1 | MAE (dB); 3 groups | compact: 3.68956429 | flexible: 3.65548184 |
| P100-092.round2.v1 / P100-092.round2.v1.development-oof | MAE (dB); 3 groups | current/cycle-001: 3.57649332 | current/baseline-hgb: 3.33980226 |

**Scope and input access.** The full3120-cell initial RSSI map remains required; three held dates test temporal transfer at calibrated positions, not localization/unseen-position prediction. Whole dates contain correlated positions/channels/antenna ports in one installation. Original held-date metrics and round2 development OOF metrics are different cohorts and must remain separate.

**Claim-quality issues.** Original compact reference loses to flexible on2/3 dates; local redistribution loses on all three development dates. The round2 task scope inherits mention of the original reserved days before explicitly saying OOF; reader navigation should show the actual three development dates first. Three fitted power-mixing coefficients are not total model complexity when the3120-cell measured map is required.

**Next improvements.**
- Measure calibration acquisition cost explicitly and evaluate sparse-map budgets as separately registered tasks.
- Reserve entire rooms/installations and positions for spatial claims; collect independent antenna/geometry controls for mechanistic power transfer.
- Report date-group uncertainty, worst-date performance and unchanged-map/flexible baselines under equal calibration access.

No new blocking numerical defect is established by this documentary audit. Exact inspected file hashes and complete versioned comparisons are in the companion JSON.

## P100-096

The most substantive contribution is correcting observation timing and demonstrating a modest scoped directional-leader relation under matched wrong-neighbor controls. The original author-smoothed speed result alone is nearly tied with persistence.

| Task/cohort | Primary metric | Selected reference | Strongest control |
|---|---|---:|---:|
| P100-096.continuation.v1 / P100-096.continuation.v1.cohort-1 | MAE (m/s); 1 groups | reference: 0.262045361 | geometry: 0.270299766 |
| P100-096.original.v1 / P100-096.original.v1.cohort-1 | MAE (m/s); 2 groups | reference: 0.261642382 | baseline_persistence: 0.265822819 |

**Scope and input access.** Original source Kalman/RTS speeds may incorporate future smoothing, so timestamp-only predictor causality does not establish online measurement availability. Supplemental manual-position trajectories use actual0.8/1.2s windows and form a distinct optional source/task; negative projected targets remain eligible. All28 riders recur in one session. Connected videos0010–0012 are one exposed diagnostic block; no independent rider or safety transfer.

**Claim-quality issues.** A nominal-clock acceleration coefficient near-0.9283 was a timing artifact, not behavior. Supplemental leader-only diagnostic improvement is modest and some exposed parameter variants score slightly better; do not promote them as fresh confirmation. Keep original and supplemental endpoints, units of backward speed difference, source manifests and source availability distinct.

**Next improvements.**
- Collect independent sessions/riders and genuinely causal raw/manual tracking with explicit frame timing and annotation latency.
- Repeat matched reverse-direction, shuffled-neighbor and persistence controls on new groups before physical car-following interpretation.
- Use signed target validation and actual duration everywhere; no automatic nonnegative filtering of projected motion.

No new blocking numerical defect is established by this documentary audit. Exact inspected file hashes and complete versioned comparisons are in the companion JSON.

## P100-100

Lag-two persistence is the mandatory recurrence control; adding it overturns a weak earlier improvement claim. This is a useful benchmark correction and negative mechanism test, not identification of a scheduler or queue.

| Task/cohort | Primary metric | Selected reference | Strongest control |
|---|---|---:|---:|
| P100-100.original.v1 / P100-100.original.v1.cohort-1 | MAE (ms); 3 groups | reference: 2.07001603 | baseline_residual_rbf: 2.10539685 |
| P100-100.round2.v1 / P100-100.round2.v1.development-oof | MAE (ms); 6 groups | current/cycle-001: 2.69166704 | previous/baseline-lag2: 2.422715 |

**Scope and input access.** Complete route/run groups and only prior completed probes are allowed; radio is as-of previous completion with<=0.5s age. Original has2942 measured RTTs among2943 assigned observations; one lost response has no RTT and cannot be imputed. Round2 has5938/5965. Successful-response conditioning excludes a packet-loss outcome; three original held runs and six development runs do not establish network-wide reliability.

**Claim-quality issues.** Original compact average gain versus residual kernel loses on2/3 runs and omitted a stronger simple lag-two control. Parity-filter assumptions of equal-variance independent noise and stationary alternating means are not measured. A50ms decision threshold is illustrative absent an externally justified service constraint; event metrics require declared provenance.

**Next improvements.**
- Require lag-one, lag-two, rolling and flexible history baselines in every new proposal with equivalent input availability.
- Register loss/timeout and tail-RTT tasks separately, preserving missing targets and identical eligibility denominators.
- Reserve fresh operators/routes/time periods and measure relevant scheduling/queue state before a mechanism claim.

No new blocking numerical defect is established by this documentary audit. Exact inspected file hashes and complete versioned comparisons are in the companion JSON.

