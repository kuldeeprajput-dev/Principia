# Campaign summary

Attempt005 improves worst-group robustness but not mean;006(square-root stress scaling) and007(notch-only ablation) fail to improve the established mean/worst Pareto envelope. Keep001 as primary mean-error choice and retain005 as a robustness alternative.

| Model | Development MAE | Confirmation MAE |
|---|---:|---:|
| baseline-domain | 0.0230178 | 0.02669 |
| baseline-flexible | 0.0185827 | 0.0190768 |
| attempt-001 | 0.0154339 | 0.0173158 |
| attempt-002 | 0.0155683 | 0.0178839 |
| attempt-003 | 0.0173592 | 0.0196951 |
| attempt-004 | 0.0172705 | 0.0159612 |
| attempt-005 | 0.0159668 | 0.0197531 |
| attempt-006 | 0.0156993 | 0.0172339 |
| attempt-007 | 0.025961 | 0.0286041 |


The notch-only alternative worsens development MAE to0.02596mN and confirmation to0.02860mN, so relative notch depth alone does not replace bridge width in this task. A bounded regime model happens to score0.015961mN after opening confirmation, but its development error was worse and one boundary parameter was at its bound; it remains a diagnostic alternative rather than replacing the preselected reference. This disagreement is useful evidence for future independent experiments.

No confirmation-driven revision occurred. Scientific failures are retained in attempts/.
