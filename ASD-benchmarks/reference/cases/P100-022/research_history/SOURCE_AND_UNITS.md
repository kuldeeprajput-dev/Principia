# Source and units audit: P100-022

First-forming current across perovskite devices. Native bytes are hash-verified by native.py. Primary publication: https://advanced.onlinelibrary.wiley.com/doi/10.1002/admt.202502152.

Endpoint: Initial positive forming-sweep current, microampere. Inputs: voltage_V (V), bromine_rich (indicator).

Complete device, both compositions; all duplicate device traces linked. No future current or state permitted.

None. First100 voltage rows of each device, V>=0.05V; no measured current allowed as predictor.

Public source-aware corpus; source plots and published analyses known. Schema previews exposed first rows only. Case30 speeds>=13.9mm/s previewed; scored0.28–10mm/s unviewed. Case22 initial~0.006V row previewed; targetV>=0.05V unviewed. Case65 10Hz first rows previewed; scoref>=100Hz. Reserved response distributions and scores unopened.

## Native semantics, prior processing and limitations

The primary article identifies Figure3a/d as first-forming sweeps across50 I-rich and50 Br-rich cells. The release has50 column pairs in each workbook; one Br-rich pair is exactly duplicated in both voltage and current, yielding99 distinct released traces, not an invented100th independent sample. Complete traces are deduplicated conservatively and all states/directions remain linked. Only the first100 increasing-voltage samples, V>=0.05V, are targets. Units are native V andA, converted exactly to microampere. The source states1mA compliance, while the development exports repeatedly plateau at1.15mA; treat the fitted ceiling as instrument/circuit-limited response, not intrinsic material saturation. A population turn-on curve predicts ensemble current across devices; it is not a calibrated switching law for an individual cell. The source already reports lower forming voltages in Br-rich films, filament interpretations, Gaussian statistics and CALM dynamics. CALM pertains to repeated hysteresis; first-forming profiles are a distinct endpoint. No clamping-force/retention/neuromorphic benefit is measured here. Some files named by README (Figure5,S6,S7) are absent; no missing file is fabricated.
