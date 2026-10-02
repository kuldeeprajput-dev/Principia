# Native source and units audit

Twenty healthy participants; three complete trials linked. Forecasts assess device/airway signal continuity under rapid occlusion, not separately identified lung compliance or clinical accuracy.

Endpoint: gauge_pressure_200ms_future (cmH2O).

Calibration: Source fixed ADC-to-cmH2O conversion; no target-participant fitted coefficients. All history at or before forecast origin.

Timing: At each fixed1s origin predict native gauge pressure0.20s later using only present/past pressure and differential-pressure signals.

Source: https://physionet.org/content/respiratory-heartrate-dataset/1.0.0/
Primary study: https://doi.org/10.1016/j.ifacol.2023.10.1107

Native bytes remain unchanged; deterministic adapters emit explicit source and calibration anchors. Publisher-calculated measurements remain labeled author-processed. No global normalization, model fitting or future-outcome features occur in preparation.
