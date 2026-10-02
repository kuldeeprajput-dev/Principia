# Crowd rotation: short-horizon memory and heterogeneity

A compact aggregate-memory rule tests whether directional heterogeneity adds useful short-horizon information beyond current collective rotation. Its interpretation is phenomenological and limited to the released group experiments.

## Data and evaluation

Native trajectories cover 26 country/age/condition groups. All repetitions of a condition remain linked: 1,158 development origins in 21 conditions and 270 confirmation origins in five conditions. The singleton teenager condition is development-only. Japan and child coordinates are converted from source centimetres to metres. At each integer time, positions use only the last available sample at or before that time; velocity is backward one-second displacement. The target is the mean angular order at the next two seconds. Native author-supplied velocity/polarization fields are excluded because their causal derivative windows are unspecified.

Target: **Mean next-two-second signed angular polarization about instantaneous group centroid**, measured as dimensionless signed[-1,1]. Primary error: polarization units. Every predictor uses trajectory rows at/before origin t. Integer positions use previous observed sample only, at most1second stale; current tracked count uses prefix-present IDs, never full-trial future membership. No interpolation from future. Velocities derived by backward1s differences; supplied VX/VY/Pol forbidden because smoothing provenance can include future. Target uses t+1..t+2.

Whole country/experiment-condition group with all repetitions; participants may recur across conditions and identifiers do not resolve all dependence. One teen condition keptdevelopment, no heldteen generalization. First2seconds of each trial used as explicit calibration; no future held-group target fit. Whole condition/session A/C/D identifiers keep repetitions linked. Calibration baseline given same prefix access.

## Findings and equations

**P100-090-F01 — validated_extension (unsupported).** The proposed aggregate-memory and heterogeneity equation improves reserved-condition two-second rotation prediction over all matched controls.

See rules.json models.reference: Pfuture_hat=clip[Ppast+a(P0-Ppast)+c H Ppast,-1,1].

Memory and within-group directional spread provide a compact phenomenological description; coefficient signs do not identify participant-level causal mechanisms.

Falsifying evidence and limits: Limited conditions, possible repeated participants, author-publication exposure and short windows constrain generalization. Compare every held group and persistence before accepting the positive transfer claim.

**P100-090-F02 — informative_falsification (supported).** The campaign does not establish a new universal collective-rotation or individual-bias law.

Mean-field cubic002 and density/boundary003 models remain recorded; no causal individual-bias equation is admitted.

Aggregate trajectories and short forecast accuracy cannot independently separate intrinsic locomotor bias, social interactions and boundary effects.

Falsifying evidence and limits: No independent perturbation or new experiment; published source outcomes and the now-exposed confirmation cannot provide a novelty proof.

Selected executable model: `attempt_005`. For moving participant i, a_i=(r_x*v_y-r_y*v_x)/(|r|*|v|) about the current group centroid. P is its participant mean; H is the square root of its within-group variance. Let P0 be current order and Ppast the previous two-second mean. The selected rule is Pfuture_hat=clip[Ppast+a*(P0-Ppast)+c*H*Ppast,-1,1], with [a,c]=[0.828009503397648, -0.09191006303742405]. Prefix-derived tracked participants only are used; no future trajectory endpoints enter inputs.

All coefficients, input definitions, training groups and transformations are in `rules.json`; the runnable reference performs no fitting.

## Compact numerical evidence

Errors are computed within declared complete groups (with final survey weights when supplied), then averaged equally across groups.

| Frozen model | Development error | Confirmation error | Worst confirmation group |
|---|---:|---:|---:|
| reference | 0.06946779 | 0.06595787 | 0.09504082 |
| calibration | 0.1588337 | 0.1835706 | 0.2250237 |
| constant | 0.2039894 | 0.2243616 | 0.5518001 |
| current | 0.07054484 | 0.06571862 | 0.09364152 |
| flexible | 0.08384881 | 0.06474652 | 0.09632542 |
| persistence | 0.07350839 | 0.07354352 | 0.1120237 |

Confirmation contains 270 scored observations in 5 groups. Individual-group scores and every attempted model remain available. Confirmation MAE is 0.065958 in signed angular-order units versus current-order persistence 0.065719, past-order persistence 0.073544, and the flexible control 0.064747. Individual conditions and every alternative are retained. The development-selected simpler005 omits initial-drift calibration even though004 had slightly lower development error.

## Interpretation, limitations and use

Within-source group-rotation temporal dynamics after observed prefix. Centroid-based XY-derived order differs from authors supplied Pol; no arithmetic identity predicted at same time. Source published conditionmeans already known; confirmation not unseen-world evidence. No novel biological handedness or safety intervention law. Whole-group errors/ranges; no row bootstrap or manufactured independent-population confidence. Confirmation becomes exposed after freeze.

The heterogeneity term damps an existing signed collective rotation. It is compatible with dephasing, but does not establish an individual motor bias, social coupling strength or biological law. Source published condition-level outcomes were already visible during the semantics audit. Participant reuse is unresolved and five held conditions are not five independent populations. The two-second horizon is chosen to retain short child experiments.

## Reproducibility and prior art

Run `python run.py` to verify hashes and replay every frozen equation. Predictions use declared input columns only. The shared benchmark evaluator can score alternative equations under the same task; numerical agreement with these coefficients is not required. Public source-aware confirmation is now exposed. No independent experimental replication or certified novelty is claimed.

- [Source article attributes counterclockwise tendency to individual locomotor bias, with experiments across populations; recovering mean rotation is prior-art reproduction, not new collective mechanism.](https://www.nature.com/articles/s41467-026-73713-w) (checked 2026-10-02).
- [Preserved experimental trajectory record; supplied derivatives/order are not used to avoid unknown future smoothing.](https://zenodo.org/records/19592341) (checked 2026-10-02).
