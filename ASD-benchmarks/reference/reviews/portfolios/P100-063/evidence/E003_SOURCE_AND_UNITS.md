# Source and units audit: P100-063

Temperature-transfer magnon noise. Native bytes are hash-verified by native.py. Primary publication: https://arxiv.org/html/2404.17327v1.

Endpoint: Noise power spectral density, nV^2/Hz. Inputs: frequency_GHz (GHz), field_T (T), termination_K (K).

Entire termination temperature; magnetic-field traces nested. One74nm YIG film, frequencies dependent.

No held-condition calibration. Publisher background subtraction retained, not refitted.

Public source-aware corpus; source plots and published analyses known. Schema previews exposed first rows only. Case30 speeds>=13.9mm/s previewed; scored0.28–10mm/s unviewed. Case22 initial~0.006V row previewed; targetV>=0.05V unviewed. Case65 10Hz first rows previewed; scoref>=100Hz. Reserved response distributions and scores unopened.

## Native semantics, prior processing and limitations

The original HDF5Figure6 holds measured, author-processed noise spectra: fHz, BT, terminationTK, Sn nV^2/Hz. The film remains near293K; termination temperature is NOT film temperature. The source reports background-polynomial subtraction using equilibrium spectra, circuit attenuation, Lorentzian fits and Kittel dispersion; all are prior art. We retain source processing unchanged; source preprocessing used author-global information and is not an independently blind raw-detector analysis. No suppliedfit_result array is used. Native frequency bins are1001points perfield, nested in complete temperaturegroups (77,195,293,352,389K), all on one74nm YIGfilm. Confirmation195/352Kinterpolates between development temperatures; whole-temperature leave-out development includes harder extrapolation. A locally linear resonance relation over167–173mT is identifiable better than independently inferring both gyromagneticratio andmagnetization. Native parser requires h5py in addition to common dependencies. Screening substitution12→63 was approved beforefit: onlythree tabular SE wafermaps in12 gave weaker independent validation.
