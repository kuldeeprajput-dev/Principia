# P100-054 — Geometry-conditioned bridge failure load

## Scenario and task

The native archive contains microcantilever force-depth traces and an author analysis workbook. The task uses the measured second-bridge failure force Pb2 and measured geometry from 107 records representing 103 linked specimens. Author-computed toughness, fitted correction factors and crack-arrest labels are excluded from predictors.

## Experimental and validation design

The response is force P in mN; cantilever width B, thickness W, length L, notch depth a and notch width b are in micrometres. Repeated specimen labels are linked. Development holds out entire C/D/E specimen-ID families in turn; confirmation contains 22 specimens and 23 records allocated using only IDs. Some geometry comes from post-test imaging: this is a conditional response reconstruction, not a prospective failure-control rule. All specimens originate from one wafer/campaign.

At least five adaptive attempts preceded a code-and-state freeze; confirmation was then evaluated without fitting or reselection. Source publications and supplied analyses are known. All packaged outcomes are now exposed to later users.

## Frozen equation and interpretation

With $x=a/W$ and $r=1-b/B$, the source-declared cantilever geometry factor is

$$
f(x)=1.46+24.36x-47.21x^2+75.18x^3,
\qquad \widehat P=\frac{BW^{3/2}}{L f(x)}(K_0+c r).
$$

Here K0=0.636134MPa sqrt(m) and c=5.430604MPa sqrt(m); geometry in micrometres yields force in mN. Full precision is in rules.json. These coefficients describe apparent geometric response at bridge failure; neither is claimed to be intrinsic silicon toughness.

## Evidence and limitations

The primary metric is the equally weighted mean of within-group mean absolute errors in mN; sample counts do not create independent replicates.

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


Selected-reference group errors: C16: 0.000177068; C25: 0.00503408; C27: 0.0238396; C44: 0.0189243; C45: 0.0340114; D16: 0.0159339; D19: 0.0129144; D28: 0.0304222; D45: 0.0100224; E17: 0.0114722; E20: 0.00933404; E21: 0.0208402; E25: 0.0287463; E26: 0.0188464; E27: 0.00899972; E37: 0.0207901; E38: 0.0261877; E41: 0.0210864; E43: 0.00106995; E6: 0.0362713; E8: 0.00803985; E9: 0.0179835.

The notch-only alternative worsens development MAE to0.02596mN and confirmation to0.02860mN, so relative notch depth alone does not replace bridge width in this task. A bounded regime model happens to score0.015961mN after opening confirmation, but its development error was worse and one boundary parameter was at its bound; it remains a diagnostic alternative rather than replacing the preselected reference. This disagreement is useful evidence for future independent experiments.

## Practical meaning and reproducibility

A two-parameter correction transfers better than constant apparent toughness and the constrained quadratic control. It can support screening of geometric response models and diagnose why apparent toughness varies with bridges. It does not establish intrinsic material toughness, causal bridge manipulation, safe loading limits or cross-wafer transfer.

Run `python run.py` to check hashes and reproduce every saved equation, prediction and metric. `rules.json` holds all coefficients, parameter names and fit scope; `findings.json` separates supported claims, failed hypotheses and abstentions. The shared benchmark evaluator accepts alternative equations under this same information budget; exact agreement with this reference is not required.

## Sources

- https://doi.org/10.1016/j.msea.2025.148479
- https://zenodo.org/records/15581944
