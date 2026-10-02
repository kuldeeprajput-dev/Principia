# P100-060.original.v1

**Target.** Post-trigger peak absolute receiver voltage

**Units.** V

**Error units.** V

**Primary metric.** mae

**Primary metric units.** V

**Cohort.** P100-060.original.v1.cohort-1

**Prediction time.** Target is maximum absolute receiver voltage across all t>=0 samples, subtracting each trace mean over t<0. No response-selected time window or denoising. Ten actual waveform columns kept per file.

**Independent unit.** whole width block across sensor/distance; six correlated files

**Hierarchy.** group

**Calibration and history.** w is pulse width in microseconds; f is nominal resonance in cycles per microsecond (kHz/1000). The effective damping time12us was selected on development widths. Six calibrated gains in V are12.271204,0.941597,0.00302123,0.000609934,0.00227582,0.000462384 for(d0,f110),(d0,f500),(d20,f110),(d20,f500),(d50,f110),(d50,f500). The maximum accounts for an initial pulse edge before the second edge; it is a phenomenological peak approximation. Sensor type is confounded with nominal resonance.

**Limits.** Six condition files at one reserved5us width, not six independent reserved width experiments. Gain is concentrated in zero-distance110kHz contact; air and500kHz sensor counterexamples remain.

**Historical exposure record.** All packaged targets are now exposed; future scoring is retrospective. Only numerical schema/sample metadata were inspected before fitting. The reserved pulse width is allocated by metadata hash. No final performance inspected.

**Current exposure.** All outcomes exposed; future scoring is retrospective.

**Source scope.** original_corpus

**Source.** https://zenodo.org/records/17266427

**Source terms.** cc-by-4.0

## Permitted prediction inputs

| Variable | Unit / interpretation |
|---|---|
| `condition` | calibrated distance/sensor label |
| `distance_mm` | mm |
| `resonance_kHz` | kHz; confounded with sensor type |
| `width_us` | us |

Identifiers and source locators are alignment metadata. They may route documented frozen calibration states; they are not a license to look up a scored target. Additional columns outside this list are not predictors.

## Reproduction and comparison

`run.py` and `rules.json` contain executable frozen equations and every coefficient. `evidence/metrics.csv` and `evidence/predictions.csv.gz` preserve the historical comparisons. The shared evaluator recalculates them and compares submitted predictions on identical covered observations. Model IDs are local to this task and are distinct from finding IDs.

Primary aggregation and eligible observations are frozen. Excluded/nonpositive log targets are reported separately from physical-unit error. Uncertainty is described at independent-group level; no row bootstrap is used. The raw adapter emits native anchors, eligibility, calibration and group records. Preparation does not fit or tune a model.

Default reference: `reference`. Comparator models: `reference`, `challenger`, `baseline_linear_width`, `baseline_mean`, `baseline_rbf`, `baseline_residual_rbf`.

Use `python evaluation/benchmark.py example --task P100-060.original.v1 --output NEW_FOLDER` from the benchmark root. Historical development/confirmation separation cannot be reused as a fresh holdout after exposure.
