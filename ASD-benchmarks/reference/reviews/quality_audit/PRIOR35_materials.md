# Targeted scientific-quality audit: nine prior materials portfolios

This audit preserves existing source data, models, task histories and numerical results. It is a task-specific quality review, not a new ASD fit, independent experimental replication or novelty certification. All future scoring is retrospective. Original and expanded-input tasks are never pooled. Case54/56 were authored by this reviewer in the prior campaign; this maintenance audit is not a new independent scientific review of those cases.

## P100-054

A two-parameter bridge-width correction improves second-bridge force reconstruction within one wafer; notch-only correction fails. It is not intrinsic toughness or prospective safe-load control.

Twenty-two reserved specimen IDs/23 records, but only one wafer/campaign. Some SEM geometry is post-test; repeated labels stay linked. Author toughness outputs are excluded.

| Task | Metric | Frozen reference | Strongest named control |
|---|---|---:|---:|
| P100-054.original.v1 | mae (mN) | reference: 0.017315774 | baseline_flexible: 0.019076826 |

Quality findings: Post-test geometry must remain prominent in every task description. Stronger bounded-regime confirmation result is diagnostic, not a replacement reference.

Next evidence: Use pre-test geometry plus new-wafer specimens to test prospective transfer. Repeat geometric metrology to quantify errors-in-variables before intrinsic toughness claims.

## P100-055

Physical-law abstention is justified for the uncalibrated force task. Complete early-age curves enable a separate calibrated aging task, but the selected proportional gain is not best on the exposed two-mixture confirmation.

Unknown penetration-index cadence and incomplete probe geometry preclude material stress/time constants. Age0 and age30 represent distinct specimens; input histories change the task. Water, aggregate and additives covary.

| Task | Metric | Frozen reference | Strongest named control |
|---|---|---:|---:|
| P100-055.continuation.v1 | mae (N) | reference: 0.13632263 | baseline_kernel: 0.082818948 |
| P100-055.original.v1 | mae (N) | reference: 0.15009735 | baseline_rbf: 0.15009735 |

Quality findings: The continuation reference0.136323N loses to kernel0.082819N and several later diagnostics; development-selection success must never be presented as confirmed superiority.

Next evidence: Obtain penetration kinematics/geometry and independent batch replication. Fix mixture labels/masses using author context; pre-register prospective paired-age sampling before mechanistic aging inference.

## P100-056

Early-calibrated saturation prevents gross elastic extrapolation. The concrete-specific cap does not beat a simpler common cap on two held beams.

Four training beams and two C-beam confirmation curves. Every predictor sees only<=10mm calibration, but task is conditional on later imposed displacement. Post-damage drops retained; no virgin-material strength or safety certification.

| Task | Metric | Frozen reference | Strongest named control |
|---|---|---:|---:|
| P100-056.original.v1 | mae (kN) | reference: 5.281086 | attempt_002: 4.7539679 |

Quality findings: A cap estimates response, not characteristic design resistance. Material-specific superiority is already unsupported and must remain so.

Next evidence: Measure additional independent beams and connector-slip evolution; test damage-phase predictions separately under a prespecified task, retaining abrupt drops.

## P100-057

Known Arrhenius response is a compact repeat-test baseline. Causal earlier-temperature history defines a separate task; shear transport adds negligible useful evidence and does not identify equilibrium rheology.

Known formulations in one rheometer campaign; synthesis lots absent. Signed/extreme readings remain. Sequential heating confounds temperature and aging. History task contains40 development-OOF Test IDs, distinct from10 original reserved tests.

| Task | Metric | Frozen reference | Strongest named control |
|---|---|---:|---:|
| P100-057.original.v1 | mae (cP) | reference: 3291.1659 | baseline_rbf: 4575.9069 |
| P100-057.round2.v1 | mae (cP) | current/cycle-001: 3628.0281 | previous/baseline-old: 3637.3972 |

Quality findings: Round2 calibration prose incorrectly inherited original static Arrhenius amplitudes; exact documentation-onlyv2 corrections supplied. Extra histories explain changed information budget; static/history error differences are not an algorithm comparison.

Next evidence: Apply versioned task-card correction without touching v1 states. Seek instrument-status/torque-range evidence for negative/extreme readings and new synthesis batches; do not silently discard unfavorable values.

## P100-058

Maxwell/WLF storage transfer and unfitted loss response provide meaningful orthogonal checks. Recycled-PLA loss failure is a stronger limitation than storage fit alone; individual relaxation modes remain unidentified.

Core is one PDLLA batch; supplements are separately calibrated materials from same authors/instrument. OriginalT70/T80 and all PLA outcomes now exposed. Three negative original storage readings are excluded only from logarithmic, not physical error.

| Task | Metric | Frozen reference | Strongest named control |
|---|---|---:|---:|
| P100-058.continuation.v1 | log_mae (dimensionless natural-log ratio) | reference: 0.31113311 | arrhenius: 0.5114834 |
| P100-058.original.v1 | log_mae (dimensionless natural-log ratio) | reference: 0.40446148 | baseline_rbf: 1.2934495 |
| P100-058.supplemental-PLA3D850-loss.v1 | log_mae (dimensionless natural-log ratio) | reference: 0.46416856 | arrhenius: 0.78917837 |
| P100-058.supplemental-PLA3D850-storage.v1 | log_mae (dimensionless natural-log ratio) | reference: 0.70932423 | arrhenius: 1.1998153 |
| P100-058.supplemental-PLA_recycled-loss.v1 | log_mae (dimensionless natural-log ratio) | reference: 1.860375 | arrhenius: 2.047151 |
| P100-058.supplemental-PLA_recycled-storage.v1 | log_mae (dimensionless natural-log ratio) | reference: 0.37983623 | arrhenius: 0.80862066 |

Quality findings: Keep six task IDs separate: original/continuation and four supplemental material-response tasks. Historical original metrics.csv labels35 scored rows although log eligibility is32; corrected current task scope explicitly states32. Do not overwrite historical receipts or represent35 as positive log targets.

Next evidence: Report primary-log and physical denominators side by side. Obtain independent complex-modulus/creep data and compliance calibration to distinguish elastic plateau/slow modes; do not retune recycled-loss response and claim fresh confirmation.

## P100-059

A conditional radiation/calendar surrogate transfers to one city. The continuation calendar control remains stronger than a compact equal-lag model; thermal derating is not identified.

One held city, plants sharing weather; weather provider, timezone and averaging provenance unresolved. Current weather is a contemporaneous diagnostic input, not a forecast. Native energy normalized by independent installed capacity.

| Task | Metric | Frozen reference | Strongest named control |
|---|---|---:|---:|
| P100-059.continuation.v1 | mae (kWh/kWp) | reference: 0.10073207 | ridge_calendar: 0.10073207 |
| P100-059.original.v1 | mae (kWh/kWp) | reference: 0.10969556 | baseline_rbf: 0.12991607 |

Quality findings: Positive or boundary-hitting thermal coefficients contradict a causal thermal-derating reading. Native-clock history cannot justify an inferred timestamp shift.

Next evidence: Resolve weather/timestamp provenance with authoritative records and test other cities/plant orientations. Pre-register a genuine forecast-information task separately.

## P100-060

Pulse-edge models predict conditional peak voltage, but aggregate physical gains are contact-dominated. Normalized OOF comparisons and spectral mismatch prevent fitted resonance from being treated as measured physics.

One setup, two sensor classes confounded with nominal frequency. Original one held5us width has six correlated condition files. Round2 covers five development widths/30files/300pulses with training-only condition normalizers.

| Task | Metric | Frozen reference | Strongest named control |
|---|---|---:|---:|
| P100-060.original.v1 | mae (V) | reference: 0.35620194 | baseline_residual_rbf: 0.62204268 |
| P100-060.round2.v1 | normalized_mae (condition-normalized MAE) | current/cycle-001: 0.18070677 | previous/baseline-global_edge: 0.19526332 |

Quality findings: Round2 scope/calibration inherited original5us cohort and one comparator coefficients; documentation-onlyv2 replacements supplied. Default round2 current/cycle001 is an anchor, not the best discovered candidate.

Next evidence: Apply versioned contract correction. Hold independent sensor/width regimes and validate time-domain response and measured spectral peaks before damping/resonance interpretation. Report normalized and physical errors together.

## P100-061

Physically bounded depletion/film models reproduce known transport constraints; the original compact model loses sharply to nested kernel. Later two-family film closure improves development OOF only, with no fresh independent confirmation.

Four calibrated specimens, two geometry families.64 pure-H2 measurements allowed at350/450C for all mixture candidates. Normal molar volume assumed22.414L/mol. Original400C holdout differs from round2 six gas-temperature OOF groups at350/450C.

| Task | Metric | Frozen reference | Strongest named control |
|---|---|---:|---:|
| P100-061.original.v1 | mae (mol s^-1 m^-2) | attempt-004: 0.012896336 | rbf_nested: 0.0016878248 |
| P100-061.round2.v1 | mae (mol m^-2 s^-1) | current/cycle-001: 0.0049059982 | previous/baselines/kernel_nested: 0.0046582048 |

Quality findings: Round2 independent_unit/scope incorrectly said reserved400C/60rows; exact documentation-onlyv2 corrections supplied. Full coefficient burden includes12pure-gas calibration parameters even when mixture parameters shrink to2.

Next evidence: Apply versioned contract correction. Match the published layered-model implementation before superiority claims. Vary geometry and gas/flow factorially with new calibrated specimens, and resolve normal-flow convention.

## P100-064

No robust optical transfer improvement is admitted beyond early optical persistence. Lack of area/strain/optical geometry linkage prevents luminance or material-degradation law claims.

Four held devices; two groups have only37 and4eligible overlaps, while another9136rows. Fixed<=2s electrical alignment and>=3early optical points define a fast-sampling restricted cohort. Signed photodiode current is retained.

| Task | Metric | Frozen reference | Strongest named control |
|---|---|---:|---:|
| P100-064.original.v1 | mae (nA) | reference: 15.978752 | persistence: 15.978752 |

Quality findings: Post-hoc calibrated-yield MAE11.3374 beats reference15.9788 after failing development; do not promote. Sparse groups and cadence eligibility are central limitations, already disclosed.

Next evidence: Collect synchronized strain/optical-area records and independent device repeats. Pre-register relaxed-cadence alignment as a different task if justified by timing uncertainty, not by desirable scores.

