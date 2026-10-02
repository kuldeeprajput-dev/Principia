# Source and units audit

The Heidelberg deposit contains paired generator/response waveforms from two wafers. The depositor specifies design width in micrometres and generator voltage divided by100ohm as current. No amplifier-gain calibration, measurement-temperature specification or matched film-stress/device linkage is provided in the source description. Therefore the endpoint is **effective recorded-channel resistance**, not an absolute intrinsic tunnel-barrier resistance.

Each junction contributes one arithmetic mean of ordinary least-squares voltage/current slopes in the lower20% and upper20% current tails. These local regressions define the measurement endpoint and are not predictive fits. Quantiles are per-waveform operational endpoint extraction; they never create predictors from held-out responses. All32768/other native rows are used to determine tails. No correlation- or residual-based exclusion. The filename `1_0_2um_0_gen.csv` has ambiguous width and is excluded before any fitting.76 unambiguous junctions on19dies remain. Region/die names provide grouping; no fabricated spatial coordinates are assigned.

Inputs: nominal width(um), wafer-B indicator, outer-region-of-wafer-A indicator. Target and errors: ohm(V/A) in recorded-channel scale. Repeated time points are not independent validation units. Five hash-selected dies form confirmation;14development dies are leave-one-die-out. The schema audit explicitly exposed the1A13die and it was forced development.

A very large effective resistance in development is retained. It could reflect device failure, gain variation or other acquisition conditions; no such cause is assigned from regression alone. Native amplitudes and physical calibration require author clarification before absolute barrier-physics claims.
