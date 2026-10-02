# Source and units audit — P100-094

Source: https://zenodo.org/records/17530624. Redistribution: CC-BY-4.0. Native bytes are hash-checked and never modified.

Target: Calibrated CDOM fluorescence channel (ppb). Inputs: pressure [dbar]; temperature [degC]; salinity [psu].

Contemporaneous calibrated CDOM fluorescence diagnostic using pressure,T1,S1; no other optical or oxygen response input. Good T/S flags0, pump on,5–500dbar. CDOM has no independent QC column.

Entire station casts02,06,08 development (cast04 has no eligible good-QC observations) leave-one-cast-out; casts10 and12 confirmation. Same expedition/instrument, spatial transfer not independent sensor calibration.

CDOM ppb is the publisher-calibrated fluorescence channel, not chemically measured DOC concentration. Quality control does not establish a universal conservative-mixing relationship. No target-based outlier removal.

Exposure: Schema inspection printed first CSV row from all six casts. These shallow pump-off rows are excluded by prefit5dbar/pump rule; confirmation groups partially schema-exposed, numerical eligible outcomes not inspected.

Every output retains exact native row or NetCDF profile/level anchors. Missing/invalid measurements are excluded explicitly; none are imputed. Quality-screening defines the task, not claimed population coverage. No scientific source values are rewritten.
