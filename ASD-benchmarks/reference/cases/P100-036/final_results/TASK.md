# P100-036.original.v1

**Target.** Author QY_max

**Target units.** dimensionless quantum yield

**Metric kind.** mae

**Timing contract.** Contemporaneous imaging diagnostic: source NPQ_Lss, Rfd_Lss, NGRDI, morphology and known cultivar/treatment predict separately reported maximum quantum yield. No QY_max-derived feature or future plant measurement is supplied.

**Calibration.** No per-plant target calibration. Learned feature normalization or flexible centers are fitted on development training plants only.

**Independent unit.** Plant; repeated sampling remains linked

**Scope limits.** Two dwarf cultivars under this controlled stress protocol. Source-extracted contemporaneous fluorescence/RGB traits; no independently measured hydration or new photosynthetic law.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| npq | dimensionless author NPQ_Lss |
| rfd | dimensionless author Rfd_Lss |
| ngrdi | dimensionless RGB index |
| area | source AREA_MM scale; only relative/log descriptor used |
| tiny | cultivar indicator |
| salt | salt-treatment indicator |
| drought | drought-treatment indicator |
| high_stress | source second stress-level indicator; no invented dose units |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-036.original.v1 --output NEW_SUBMISSION; then score --task P100-036.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
