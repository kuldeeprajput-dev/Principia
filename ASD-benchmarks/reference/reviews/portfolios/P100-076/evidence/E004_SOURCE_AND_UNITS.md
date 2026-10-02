# Native source and units audit

DIV7 cells only; complete dishes linked, final recording date reserved. Culture/animal provenance may share latent batches; do not treat cells or dishes as independent donor replications.

Endpoint: evoked_spike_count (spikes per stimulus).

Calibration: Per-cell spike counts at applied current<=10pA; later currents>10pA forecast. Source manual FI eligibility preserved.

Timing: Predict higher-current evoked spike counts after the lower-current prefix for that cell. No future rheobase or peak-response calibration.

Source: https://zenodo.org/records/12802682
Primary study: https://doi.org/10.1038/s41467-025-64810-3

Native bytes remain unchanged; deterministic adapters emit explicit source and calibration anchors. Publisher-calculated measurements remain labeled author-processed. No global normalization, model fitting or future-outcome features occur in preparation.


Three cell IDs each have two distinct native ABF filenames. Calibration is scoped to the filename-specific sweep series; both series remain linked by complete dish/date. File+sweep identifies an observation, not cell+sweep. All manual y eligibility flags retained.
