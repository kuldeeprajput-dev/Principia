# P100-046 source and units audit

Can double-adiabatic or polytropic electron-temperature closures explain local evolution beyond lag persistence?

**target:** Electron perpendicular temperature

**target units:** eV

**timing contract:** Diagnostic closure using current electron density and magnetic-field magnitude plus electron temperature/density/field measured at least60s earlier; current temperature and tensor-derived equivalents forbidden.

**calibration:** Causal60-second-old electron state, same information for every model. Magnetic matching backward only.

**independent unit:** Contiguous20-minute blocks in one MMS1 passage, not independent spacecraft or experiments

**scope limits:** One2-hour MMS1 interval. All ion moments have qualityflag66 (saturation plus highMach); ion targets excluded before any fit. Electron flags0 and FGMflags0 retained. Moment errors and unmeasured heat flux/geometry limit CGL interpretation.

**exposure:** Source-aware public data. Limited schema/header and first-row previews recorded before task freeze; any inspected examples remain explicitly exposed. Confirmation performance withheld until selection and stopping freeze.

Source data stay byte-identical. Exact consumed rows/members and transformations are in native.py. All outputs record native source anchors.
