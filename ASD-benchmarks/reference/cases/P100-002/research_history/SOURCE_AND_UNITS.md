# P100-002 source and units audit

Does a damped local dynamical model transfer between stars better than persistence?

**target:** Next hourly median systematics-corrected stellar flux

**target units:** relative flux (native normalization)

**timing contract:** Predict next disjoint hourly bin using preceding observed hourly medians only. The released light curve was author-corrected using full-sector information; this is a retrospective product-space forecast, not a raw real-time pipeline.

**calibration:** Causal observed flux history within each star; no fitted header period or future light curve values.

**independent unit:** Star; repeated hourly bins are dependent

**scope limits:** Eight selected stars in one TESS sector; no new planet, stellar period or universal rotation law. Missing per-cadence quality/error columns limit robustness.

**exposure:** Source-aware public data. Limited schema/header and first-row previews recorded before task freeze; any inspected examples remain explicitly exposed. Confirmation performance withheld until selection and stopping freeze.

Source data stay byte-identical. Exact consumed rows/members and transformations are in native.py. All outputs record native source anchors.
