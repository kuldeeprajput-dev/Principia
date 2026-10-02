# Stretchable LECs: a bounded negative result for optical transfer

## Scenario and task

The source contains paired device-current and photodiode-current traces for spray-coated light-emitting electrochemical cells with different polyurethane fractions. The 17 named devices include repeated voltage runs. Fifteen devices provide eligible data after a fixed 20-second calibration period; two devices do not satisfy the fixed calibration and timing rules. Duplicate featured traces are not counted twice.

The endpoint is **signed photodiode current in nanoamperes**, not luminance. The latter requires emissive area and optical corrections that are not fully linked to each timestamp. Complete strain schedules are also unavailable. Two embedded timestamp restarts are parsed explicitly. Electrical inputs use the latest reading at or before each optical timestamp, at most 2 seconds old; charge is integrated only through that reading.

Every predictor receives the first 20 seconds' median optical current and early electrical current, plus permitted current, time, voltage, polymer fraction and past charge. Eleven eligible complete devices were used for development, and four hash-selected devices for confirmation. Five attempts tested charge state, logarithmic aging, composition interactions, saturating current response and calibrated optical yield.

## What the evidence supports

The development-selected reference is the early optical persistence rule:

$$
\widehat P(t)=P_0,\qquad P_0=\mathrm{median}\{P(s):0\leq s\leq20\,\mathrm{s}\}.
$$

Here $P$ is signed photodiode current and prediction begins after 20 seconds. This rule is a transparent comparator, **not an accurate optical law**. Its role is to prevent flexible regressions from receiving credit merely for fitting repeated rows.

|Frozen model|Development MAE (nA)|Confirmation MAE (nA)|
|---|---:|---:|
|Preselected persistence|7.543|15.979|
|Current-change control|7.860|16.289|
|Charge-state attempt|7.765|16.055|
|Flexible control|38.870|46.107|
|Rejected calibrated-yield attempt|46.636|11.337|

The primary metric equally averages complete-device MAEs, irrespective of trace length. The four reference errors are 19.244, 1.439, 42.986 and 0.246 nA, from 2316, 37, 4 and 9136 eligible observations respectively. The fixed requirement for at least three early optical calibration points and electrical readings at most 2 seconds old excludes many slower-cadence runs. This is a restricted fast-sampling task: short eligible overlaps make two group estimates especially limited. Thousands of dependent time points do not establish thousands of independent replications.

**Main finding:** the tested richer electrical/history equations do not establish robust cross-device optical transfer under this information budget. The calibrated-yield model happens to win confirmation after failing development badly. It remains a diagnostic alternative; replacing the preselected reference would be confirmation-driven selection. Its favorable confirmation number alone does not validate its mechanism.

## Scientific and practical implications

The negative evidence is useful for designing subsequent experiments: record strain timing, emitting area and synchronized optical geometry, and add independent device repeats before claiming current-to-luminance conversion or material degradation physics. Composition, voltage, aging and unobserved deformation remain confounded. No new physical law, reliable luminance prediction, industrial intervention benefit or general device-failure detector is admitted here.

The source already reports stretchable emission. This portfolio supplies an explicit information budget, causal alignment, transferable evaluator and preserved failure cases. Alternative agents can test new equations fairly without matching this persistence rule. Executable states, all group errors and native anchors are retained; run `python run.py` for local verification. Packaged outcomes are now exposed.

Sources: Gellner et al., [Journal of Materials Chemistry C (2025)](https://pubs.rsc.org/en/content/articlelanding/2025/tc/d4tc05108d); [Figshare v 1](https://doi.org/10.6084/m9.figshare.29298161.v1), CC BY 4.0. Local source READMEs define the instrument channels and luminance calibration; publisher full-text HTML retrieval was unavailable during this check.
