# Source and units audit

The selected native source is the36FET transfer-curve table for Fig2e. It contains one gate column and36current columns,201gate voltages from-20to20V. These are transistor measurements, not the simulated scaled-memory curves elsewhere in the source. The primary paper identifies a common10umchannel length and nominal50mVdrain bias. Native current values are in A; analysis converts to uA, keeping exact source row/column anchors.

This is a **calibrated sparse-characterization task**. Three native currents per device at gate-20,0,20V are supplied to every predictor; the remaining198points are targets. This is an offline reconstruction task, not an online forward sweep forecast or uncalibrated device transfer. Complete devices are split;9confirmation and27development devices. No coordinates, fabrication-batch IDs or random independent lots can be inferred from column order.

Source analyses already report uniformity, device yield, mobility, thermally activated transport and contact improvements. These are not new discoveries here. Near-quadratic shape in the selected low-drain-bias measurements cannot by itself establish MOSFET saturation physics; mobility/contact/trap contributions are not uniquely identified.

Current values at the first gate point were incidentally visible during header inspection; they are one of the declared calibration anchors, never scored. All other reserved curve values remain unread by development analysis until freeze.
