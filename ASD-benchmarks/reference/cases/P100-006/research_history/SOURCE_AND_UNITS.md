# Source and units audit: P100-006

Rydberg ionization spectral transfer. Native bytes are hash-verified by native.py. Primary publication: https://arxiv.org/html/2509.15463v1.

Endpoint: Ion-readout amplitude, arbitrary units. Inputs: detuning_MHz (MHz), rabi_MHz (MHz).

Entire contiguous probe-Rabi blocks; one vapor cell. No independent atomic-cell replication.

None. Inputdetuning/Rabi only. Fixed43D5/2 neighborhood abs(detuning)<=60MHz.

Public source-aware corpus; source plots and published analyses known. Schema previews exposed first rows only. Case30 speeds>=13.9mm/s previewed; scored0.28–10mm/s unviewed. Case22 initial~0.006V row previewed; targetV>=0.05V unviewed. Case65 10Hz first rows previewed; scoref>=100Hz. Reserved response distributions and scores unopened.

## Native semantics, prior processing and limitations

The source reports cesium ion collection, EIT and thermal/electrical noise comparisons. Peak reversal and double-Lorentzian fits are prior art. We use only Figure3b's author-released gridded ion-readout map, not its fitted linewidth/amplitude tables or sensitivity fits. The 300 equally spaced Rabi coordinates are source-defined conditions, not independent cell replicates. Interpolation/averaging lineage is not fully specified; adjacent points must not be treated as independent experiments. The fixed detuning neighborhood ±60MHz targets the calibrated43D5/2 feature. Broader43D3/2 data and optical traces are outside this task. Source README incorrectly calls the ion amplitude EIT in one format description; CSV header and figure define it as ion readout. The amplitude is arbitrary units, not calibrated current. Unknown measurement dates; published2025, source web manuscript date later modified. Collected spectral line shapes cannot identify a microscopic ionization pathway by themselves.
