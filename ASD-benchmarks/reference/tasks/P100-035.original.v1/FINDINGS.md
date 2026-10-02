# Ungulate calls: transferable context prediction with a confounding warning

The source supplies3181 author-extracted calls from168 animals across seven ungulate species. Source Positive/Negative labels describe eliciting behavioral contexts; they are not direct measurements of subjective emotional state. Whole animals are held out within species:134 development animals and34 reserved animals, yielding475 reserved calls. Calls are weighted equally within each animal and animals equally overall.

## Selected equation

The selected compact model uses species, call duration $D$ in seconds and waveform root-mean-square amplitude $R$ relative to digital full scale:

$$\Pr(\mathrm{positive\ context})=\sigma(\alpha_{\mathrm{species}}-0.69376361\ln R-1.419715\ln(D/1\,\mathrm{s})).$$

Species intercepts are the intercept plus the corresponding indicator coefficient, with Cow as reference; the exact ordered values are in rules.json and EQUATIONS.md. The waveform amplitude is **not calibrated sound pressure**. Negative duration/amplitude coefficients characterize this dataset's recording/context structure; they are not universal emotional or physiological effects.

Five adaptive attempts compared arousal-related spectral/temporal summaries, tonality, envelope modulation, a recording-amplitude challenge and an amplitude-free spectrotemporal synthesis. The simpler duration/amplitude candidate was selected within the prespecified1% development-error tolerance. Filename context words, animal IDs and labels are excluded from predictors. Known species is available to every comparator.


## Frozen results

|Model|Development group error|Reserved group error|
|---|---:|---:|
|baseline_constant|0.2055007|0.2092979|
|baseline_species|0.1973187|0.2059766|
|baseline_flexible|0.187627|0.2016159|
|attempt_001_arousal|0.1833687|0.1900535|
|attempt_002_tonality|0.1982426|0.2013305|
|attempt_003_modulation|0.1828181|0.1897613|
|attempt_004_recording|0.1821831|0.1902146|
|attempt_005_spectrotemporal|0.1830023|0.1891998|

Selected before confirmation: **attempt_004_recording**. Primary error is animal/person/group-balanced Brier probability squared. All candidates are shown to preserve unfavorable results; a lower retrospective score does not change the selected reference.

Reserved animal-balanced Brier is0.190215 for the selected equation, versus0.209298 constant prevalence,0.205977 species prevalence and0.201616 flexible acoustics. Event precision/recall/F1 at a declared0.5 threshold, log loss and calibration bins are retained separately; that threshold is an equal-cost diagnostic, not a welfare decision boundary. The numerical transfer supports a reproducible context descriptor, but the ability of uncalibrated RMS and duration to match richer acoustics is a warning: call type, eliciting context, species, source study and recorder can remain confounded after animal holdout. The source already demonstrates machine learning of valence, so neither a new emotion law nor deployed welfare impact is established. Source labels WidlBoar and WildBoar are linked for the ten overlapping animalIDs, preventing an otherwise hidden split leak.

## Validation and reproducibility

After the complete author-extracted call. Predictors only waveform summaries and known species. File context words, animal ID, call label and source reference are never predictors. No held-animal labeled calibration. Fixed waveform summaries; any coefficients, centers or species normalization fitted only on training animals.

Seven ungulate species, source behavioral contexts and recording studies. Labels are experimental context-based valence annotations, not independently verified subjective emotion; held animals do not remove study/recording confounding. All outcomes are now exposed to later agents. Claims of new validation require fresh data or an explicitly retrospective designation. Source study and processing are disclosed in SOURCE_AND_UNITS and PRIOR_ART; this is computational confirmation, not independent experimental replication.

`python run.py` verifies the allowlisted package and reproduces all saved predictions. `rules.json` contains exact coefficients and all learned transforms; `EQUATIONS.md` names each feature and equation. The adjacent native adapter reconstructs source-hash-verified observations and predictors; `task_spec.json` declares input, timing, calibration and grouping budgets. Future proposals may use different equations under the same contract, or seek review of a genuinely different measured task.

Source: [Animal-group transfer of vocal context labels](https://zenodo.org/records/14636641); [primary source/prior art](https://doi.org/10.1016/j.isci.2025.111834). License recorded by source: CC BY4.0. Literature and semantics audited2 October2026.
