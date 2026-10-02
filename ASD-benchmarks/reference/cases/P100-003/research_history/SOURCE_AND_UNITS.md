# P100-003 source and units audit

Is local strain-band noise stationary, mean reverting or driven by coupled bands?

**target:** Next nonoverlapping16-second 30–80Hz strain RMS

**target units:** 10^-21 strain

**timing contract:** Only earlier16-second strain summaries used. Quality masks applied to entire predictor and target windows; no centered filters or future PSD.

**calibration:** Four preceding16-second windows; training-only global coefficients.

**independent unit:** Contiguous512-second block in one detector segment; blocks not independent experiments

**scope limits:** Single4096-second H1 segment; this is detector-noise monitoring, not GW detection or source parameter inference. Conditional on supplied quality mask.

**exposure:** Source-aware public data. Limited schema/header and first-row previews recorded before task freeze; any inspected examples remain explicitly exposed. Confirmation performance withheld until selection and stopping freeze.

Source data stay byte-identical. Exact consumed rows/members and transformations are in native.py. All outputs record native source anchors.


**Pre-fit quality correction.** Single4096-second H1 segment; this is detector-noise monitoring, not GW detection or source parameter inference. Conditional on supplied quality mask. The entire source has injectionmask23: a continuous-wave hardware injection is present. This study concerns recorded strain-band power including possible injected contribution, NOT uncontaminated detector noise or astrophysical inference. No-cbc/burst/detchar/stochastic injections required; CW status retained.
