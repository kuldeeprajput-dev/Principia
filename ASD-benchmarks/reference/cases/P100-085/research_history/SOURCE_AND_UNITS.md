# Native source and information audit

Flask glycolic-acid recovery from independent HPLC substrate measurements

Diagnostic contemporaneous assay: initial and current independently measured EG and current pH, known medium and elapsed time. No GA calibration. Not an online forecast or replacement of HPLC.

Complete flask conditions; three development conditions and one metadata-hash confirmation condition; leave-one-condition-out folds keep all replicates together.

Native CSV previews exposed several GA observations in all four flask conditions before task freezing; explicitly retrospective; no confirmation metrics used in model selection.

- Only one held-out condition and two replicate curves; no precise population confidence.
- Bioreactor filenames imply opposing feed regimes but members are byte-identical: both excluded.
- Measured EG depletion can be negative from measurement error; preserve sign, do not impute.
- Native early rows for most conditions were seen at schema audit: confirmation is outcome-exposed retrospective transfer, not fresh experimental confirmation.

All consumed source hashes are in SOURCE_MANIFEST.json. Source instrument exports are author-calibrated/processed; no original bytes are changed. Native anchors and eligibility reasons accompany every observation. Repetitions and calibration measurements are not additional independent groups.
