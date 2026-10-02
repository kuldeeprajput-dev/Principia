# PPG native representation and independent target

The3888 ten-second PPG recordings cover50 people, with simultaneous ECG reference heart-rate annotations. The first3 recordingIDdigits identify a person. SourceQuality flags are retained, not predictors or good-only filters. HR must be finite/positive to be an observed reference.

The initial48 recordings use a surprising WFDB representation:300 signal channels and one frame, with each original time sample represented by its own gain and baseline. The remaining3840 recordings contain300 frames by3 explicit RGB channels; the adapter selects PPG_R to retain a common red-channel measurement across source versions. Digital values may all be zero; discarding gains would erase the waveform. The adapter reconstructs each sample as(digital-baseline)/gain, concatenates source order, and uses the declared30Hz sampling frequency. No ECG or qrs file enters a feature. Source PPG is extracted from smartphone video and temporally segmented by authors; it is not raw optical voltage.

A fixed linear detrend and Hann periodogram describe each complete PPG window. Fixed0.5–4Hz(30–240bpm) candidate domain and autocorrelation lags are not adjusted to HR values. Negative source waveform orientation is preserved before detrending; power/autocorrelation are sign-invariant. Motion is a known acquisition condition; ear/finger is a source binary code with no invented remapping.

Autocorrelation searches only interior local maxima in the fixed lag domain; when no interior maximum exists, its declared fallback is the Fourier estimate. The discarded boundary-max implementation and its development outcomes are preserved as a technical failure.
