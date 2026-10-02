# Ten new ASD portfolios: results and limits

Completed locally on 1 October 2026. Principia-100 now has **35 explored scenarios and 65 pending scenarios**, with 64 versioned local tasks. This campaign contributes **57 substantive attempts, 100 frozen model comparisons, 26 finding records and 20 separate computational/scientific reviews**. Finding records include reproductions, failures and abstentions; they are not 26 new laws.

All ten cases use existing native assets from the original corpus. Candidate 62 was excluded before fitting because two linked permeation traces did not support the proposed independent-group task; case 54 replaced it. No new source acquisition or publication occurred.

## What the experiments support

Errors below are equally weighted group mean absolute errors in physical units. They are not percentage accuracies. Lower is better. A development-selected reference remains selected even when a rejected alternative later scores better on confirmation.

| Case and reader package | Attempts | Main result | Evidence and practical scope |
|---|---:|---|---|
| [13 — Encapsulant cure](../cases/P100-013/final_results/FINDINGS.md) | 5 | Two Arrhenius channels: 0.05895 conversion MAE, versus 0.07528 first-order and 0.08360 flexible controls | Predictive extension on the reserved 20 K/min heating trace. One formulation; channels are not identified chemical species. |
| [21 — Josephson junctions](../cases/P100-021/final_results/FINDINGS.md) | 5 | Inverse nominal area remains selected: 766.27 recorded-channel ohms, versus 975.58 constant and 1237.10 flexible | Five reserved dies. Established geometry scaling; no supported new edge or wafer law. Unknown response gain and extreme devices constrain use. |
| [51 — Heterostructure FETs](../cases/P100-051/final_results/FINDINGS.md) | 7 | Calibration-dependent curvature: 0.016304 microampere, versus 0.017657 training-template control | Three same-device current anchors, nine reserved devices; 7.7% lower error and wins on 7/9 devices. Sparse characterization, not uncalibrated prediction or identified transport physics. |
| [54 — Microfracture](../cases/P100-054/final_results/FINDINGS.md) | 7 | LEFM geometry with bridge correction: 0.017316 mN, versus 0.026690 domain and 0.019077 flexible | 22 reserved specimens. Beats controls on 20/22 and 17/22 specimens respectively. Geometry may be measured after fracture; apparent response is not intrinsic toughness. |
| [56 — Composite beams](../cases/P100-056/final_results/FINDINGS.md) | 5 | Capped response: 5.281 kN, versus 14.737 elastic and 8.735 flexible | Two reserved beams after an early loading calibration. Saturation helps, but the simpler common cap scores 4.754 kN; material-specific superiority fails. |
| [64 — Stretchable optical cells](../cases/P100-064/final_results/FINDINGS.md) | 5 | Early persistence remains selected: 15.979 nA | Four reserved devices with unequal eligible lengths. No robust new optical transfer law. The endpoint is signed photodiode current; timing restrictions exclude slow-cadence runs. |
| [74 — Src biosensor](../cases/P100-074/final_results/FINDINGS.md) | 8 | Early-curvature extension fails: 130.233 fluorescence units versus 82.729 concentration-law control | Two reserved dose curves, no biological replicate IDs. Development improvement did not transfer; preserve the failure. |
| [85 — Yeast co-feeding](../cases/P100-085/final_results/FINDINGS.md) | 5 | Unit-mass recovery remains selected: 0.945 g/L; flexible comparator 0.3793 g/L | Retrospective diagnostic with one reserved condition. All four evaluation targets were visible during schema inspection. Duplicate bioreactor files prevent the intended feeding comparison. |
| [87 — Public-goods decisions](../cases/P100-087/final_results/FINDINGS.md) | 5 | One-step persistence: 0.36465 tokens, versus 0.42298 lag-two mean and 0.60194 flexible | 55 whole reserved pairs. All proposed mechanisms fail the simple control. Source-defined coordination events also receive pair-level precision/recall/F1 and specificity. |
| [91 — Private 5G](../cases/P100-091/final_results/FINDINGS.md) | 5 | Selected operating-point correction: 2.1956 ms, versus 3.0181 queue and 1.9165 flexible | Two reserved locations. Improvement over a queue model does not beat the strong flexible control. Same-run throughput makes this an after-run diagnostic. |

The clearest positive extensions are **13, 51 and 54**. Their practical value is a compact, reproducible conditional prediction rule within the measured system. None yet demonstrates an independently established physical law or deployed industrial savings. Case 56 supplies a useful saturation result with an explicitly failed material interaction. The remaining portfolios supply reproducible baselines, metrology boundaries and scientifically informative negative results.

## How to inspect and evaluate

Each case has a clean final_results folder: editable English reader note and two-page PDF, machine-readable findings, exact equations and coefficients, runnable frozen models, compact predictions/metrics and task/evaluator instructions. The research_history folder preserves every attempt, its hypothesis, development evidence, figures, frozen decisions and unfavorable results. Operational duplicates remain outside the release allowlist.

Use the shared [evaluation guide](../docs/EVALUATION.md) for a different equation under the same task. Every task declares permissible inputs, timing, calibration, groups, units, endpoint and source anchors. Prediction scoring executes no submitted code. Optional replay requires explicit trust. A different endpoint or information budget requires a new reviewed task contract.

Numerical checks include MAE, RMSE, bias, error quantiles, per-group errors, matched baselines, abstention and interval diagnostics. Case-specific checks add physical bounds, calibration windows, causal alignment, curve behavior or paired events where meaningful. Such checks do not automatically certify mechanism or novelty.

## Validation history and exposure

Complete physical groups were allocated before model fitting. Development selection and stopping preceded confirmation scoring. Previewed observations and source analyses are disclosed. Case 85 is wholly retrospective for its small evaluation cohort; other preview limitations are documented per case. All scores and outcomes are now exposed to future users.

Confirmation was not used to reselect later winners. This matters in cases 54, 56, 64, 74, 85 and 91. The reusable evaluator admits alternative future findings without requiring agreement with the reference equations, but their new validation claims require new independent evidence.

Separate computational and scientific-critical reviews are linked in the [review index](../reviews/README.md). These are agent reviews, not independent laboratory replication or definitive novelty adjudication. Prior-art checks are targeted; source papers and known fitted relationships are disclosed.

## Verification and continuation

See [current acceptance](ACCEPTANCE.md) for executed native reconstruction, replay, numerical parity, integrity and preservation checks. The [research handoff](../docs/ASD5_HANDOFF.md) records failure modes and lessons for the remaining 65 scenarios. Publication and new experiments remain separate actions.
