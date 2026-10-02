# P100-056 — Calibrated timber-concrete beam response

## Scenario and task

Three native workbooks contain six composite-beam summary curves, interface-slip summaries and detailed strain records for one beam. This task uses all eligible late summary-curve points from normal-weight and lightweight concrete beams A/B/C. Post-damage force drops are retained; native source bytes are unchanged.

## Experimental and validation design

The target is applied force F in kN conditional on imposed deflection d in mm. Each beam provides a calibration prefix ending before its first deflection above 10 mm. F0 and d0 are its final calibration point, k0=F0/d0. Later force, failure load and future calibration are forbidden. Four A/B beams support complete-beam development folds; two C beams provide 45 reserved late points. Two beams are insufficient for population confidence claims.

At least five adaptive attempts preceded a code-and-state freeze; confirmation was then evaluated without fitting or reselection. Source publications and supplied analyses are known. All packaged outcomes are now exposed to later users.

## Frozen equation and interpretation

Define $u=d-d_0$, $k_0=F_0/d_0$, and $m=1$ for lightweight concrete ($m=0$ for normal-weight concrete). The frozen selected reference is

$$
\widehat F=\min\{F_0+k_0u,\ C_0+C_1m\},
\qquad C_0=60.247645\,\mathrm{kN},\quad C_1=-5.080368\,\mathrm{kN}.
$$

The elastic component uses only the initial calibration prefix. The cap approximates loss of composite-action stiffness; it is not a design resistance. Exact coefficients and all competing states are in rules.json.

## Evidence and limitations

The primary metric is the equally weighted mean of within-group mean absolute errors in kN; sample counts do not create independent replicates.

| Model | Development MAE | Confirmation MAE |
|---|---:|---:|
| baseline-domain | 22.3328 | 14.7367 |
| baseline-flexible | 5.64735 | 8.73499 |
| attempt-001 | 4.81833 | 9.67599 |
| attempt-002 | 3.72692 | 4.75397 |
| attempt-003 | 3.6113 | 5.28109 |
| attempt-004 | 3.72897 | 5.13079 |
| attempt-005 | 4.9214 | 9.28458 |


Selected-reference group errors: P-LWC-C: 5.52815; P-NWC-C: 5.03402.

The main supported conclusion is protection against unrestricted elastic continuation. Concrete-specific advantage is not confirmed: the simpler common cap achieves4.75397kN, better than the preselected5.28109kN. The reference is not replaced after seeing this. Progressive rational compliance and the recent-stiffness variant achieve9.67599and9.28458kN, respectively; their favorable development fit fails to transfer to both C beams. Abrupt force drops and specimen variability remain important counterexamples.

## Practical meaning and reproducibility

Saturation protects against gross elastic extrapolation and gives a compact calibrated-response benchmark. It is not a structural design limit: the fitted cap is neither measured characteristic strength nor a safety-rated allowable load. The task needs initial beam loading and does not predict ultimate strength from virgin material specifications.

Run `python run.py` to check hashes and reproduce every saved equation, prediction and metric. `rules.json` holds all coefficients, parameter names and fit scope; `findings.json` separates supported claims, failed hypotheses and abstentions. The shared benchmark evaluator accepts alternative equations under this same information budget; exact agreement with this reference is not required.

## Sources

- https://documentserver.uhasselt.be/bitstream/1942/41406/1/069179-0410open.pdf
- https://www.sciencedirect.com/science/article/pii/S0141029624000737
- https://zenodo.org/records/17967735
