# P100-072.round2.v2

Documentation correction of P100-072.round2.v1. Native data, coefficients, prepared values, group allocations and numerical evidence are byte-identical; only the contract identity and endpoint description are corrected. No new fitting or confirmation.

**Target.** Residual glucose plus fructose

**Units.** g/L

**Prediction time.** Predict future residual glucose plus fructose (g/L) at native sampling times >=96 h, using only glucose and fructose measured at 22 and 72 h in the same strain, monoculture/coculture and biological replicate. time_h is hours since inoculation; coculture is a protocol-known indicator derived from the native sample name. Whole strain, including both culture types, all replicates and times, remains in one fold. This task uses six original development strains and development OOF only; original reserved T73/D245 and unmatched CR85 monoculture are excluded. Native HPLC sheet columns D:E and exact row anchors define the target; no same-time sugar value is a predictor.

**Calibration.** G22/F22/G72/F72 are native HPLC concentrations in g/L; S22=G22+F22 and S72=G72+F72 are deterministic sums. Require both 22 h and 72 h measurements for the same strain, culture type and replicate; missing or ambiguous native sugar measurements are excluded by the parser, never imputed. Each model receives this identical prefix calibration; learned coefficients/scales come only from the applicable training folds. This is an assay-calibrated residual-sugar forecast, not a qPCR percentage or fitness estimate. Model-specific common/separate-clock and baseline equations remain frozen in the existing states and runtime.

**Primary metric.** mae; mean_group_error.

**Independent unit.** whole co-cultured strain including every replicate/time

**Limits.** Two reserved yeast strain labels, eighteen later author-derived qPCR percentages, same experiment campaign with audit-exposed targets; no blind validation or nutrient mechanism identification. Repeatedly exposed development out-of-fold cohort; not the original reserved cohort.

## Permitted inputs

| Input | Units |
|---|---|
| S22 | g/L; glucose + fructose at 22 h |
| S72 | g/L; glucose + fructose at 72 h |
| G22 | g/L glucose |
| G72 | g/L glucose |
| F22 | g/L fructose |
| F72 | g/L fructose |
| time_h | h since inoculation |
| coculture | binary indicator |

Current outcomes are exposed. Use the shared evaluator with task P100-072.round2.v2. Alternative valid equations are allowed; a different endpoint requires a separate reviewed task.
