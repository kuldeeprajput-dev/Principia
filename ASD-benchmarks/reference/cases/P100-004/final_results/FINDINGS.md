# P100-004: Recoil and activity in reconstructed missing momentum

## Scenario and question

The native 2015 ATLAS four-lepton educational skim contains six complete run periods. Four periods support development; H and J are reserved. The endpoint is reconstructed missing transverse momentum magnitude from same-event lepton and jet kinematics.

How much of observed MET magnitude is explained by recoil geometry versus scalar activity?

## Experimental contract

Diagnostic event reconstruction from lepton and jet kinematics; met_phi/met_mpx/met_mpy and truth fields forbidden. Inputs are measured same-event objects, not a pre-collision forecast. Training events only; no held-period target calibration.

The campaign completed 5 substantive hypotheses. Native bytes and exact sample anchors are preserved. Model selection uses whole-group development error and a 1% simplicity tolerance; selection and stopping were frozen before the separate no-fitting confirmation process. All outcomes are now exposed for future users.

## Main result and interpretation

A quadrature combination of coherent recoil, activity-dependent resolution and a positive floor improves held-period prediction over scalar activity alone and the constrained nonlinear control. A Rician-mean revision and separate subsystem variances do not justify their extra structure in development.

$$
\widehat M=\sqrt{(kR)^2+a^2H+c^2}
$$

The exact executable expression is: MET_hat=sqrt((k*R)^2+a^2*H+c^2).

Parameters: b[0] = 0.2885606463; b[1] = 1.695287619; b[2] = 23.00800315. Coefficient ordering follows run.py and rules.json.

Here R is the magnitude of measured transverse object recoil and H is summed object transverse momentum, both in GeV; k is dimensionless, a has units sqrt(GeV), and c is in GeV.

## Performance and adverse evidence

| Model | Development MAE | Confirmation MAE |
|---|---:|---:|
| attempt 003 | 19.9341 | 20.9421 |
| constant | 22.1749 | 23.4594 |
| rbf | 21.1163 | 21.8207 |

MAE is averaged within each complete group and then equally over the 2 reserved groups (87854 observations). Errors are in GeV. Per-group RMSE, bias and failures are available in evidence/by_group.csv; small or dependent group counts do not support population confidence claims.

The lowest retrospective confirmation error belongs to attempt 003. It did not change the frozen selection. Replacing the quadrature response by a Rician mean or separately fitted lepton/jet variances does not provide a material development gain under the 1% simplicity rule.

## Value, limits and evaluation

The equation is an interpretable reconstruction diagnostic. Its components resemble established detector-resolution models, but shared reconstruction inputs prevent treating its predictive agreement as independent discovery of momentum conservation or new particle physics. The source is a selected four-lepton sample without the Monte Carlo/control samples needed to identify background, missing particles or detector-resolution components causally.

Alternative agents can submit any predictor under this task's information budget. The shared evaluator reports task-unit errors, whole-group and worst-group results, coverage, abstention, optional intervals and meaningful event diagnostics. A different endpoint requires an independently reviewed new-task contract. Numerical success alone does not certify mechanism, novelty or deployed impact.

## Reproducibility and source

Run `python run.py` for the frozen reference replay. `rules.json` contains every fitted value; `task_spec.json` defines units and access; `evidence/` contains compact predictions and numerical evidence. Research history preserves all hypotheses, failed candidates, technical corrections and the first confirmation receipt.

Authoritative source: https://opendata.cern.ch/record/93918. Redistribution terms: CC0 1.0. Primary-source prior-art searches and limitations are recorded in PRIOR_ART.json.
