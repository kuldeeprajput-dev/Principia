# Source and units audit: P100-065

Injection-ratio laser noise transfer. Native bytes are hash-verified by native.py. Primary publication: https://eprints.soton.ac.uk/507397/1/prj-13-3-611.pdf.

Endpoint: Log frequency-noise spectral density, dB re 1 Hz^2/Hz. Inputs: frequency_Hz (Hz), injection_dB (dB).

Complete injection ratio; one laser/resonator setup. Development validation blocks complete log-frequency bands across two ratios.

No held-ratio calibration. Log10 target transform fixed; measuredPSD only and100<=f<=1e6Hz.

Public source-aware corpus; source plots and published analyses known. Schema previews exposed first rows only. Case30 speeds>=13.9mm/s previewed; scored0.28–10mm/s unviewed. Case22 initial~0.006V row previewed; targetV>=0.05V unviewed. Case65 10Hz first rows previewed; scoref>=100Hz. Reserved response distributions and scores unopened.

## Native semantics, prior processing and limitations

Figure8 contains frequency/PSD pairs ordered -30,-20,-15dB; the -15dB trace duplicates Figure7/9and is read onlyonce. Institutional sourcePDF and Figure9's measuredpair provenance identify these curves. SimulatedFigure2andFigure9 columns andmanufacturer Allan-deviation references are excluded. Target y=10log10(Snu/(1Hz^2/Hz)), dB re1Hz^2/Hz; this fixed transform matches multidecade spectral-error interpretation. Raw-PSD error is complementary. Score100Hz<=f<=1MHz; first10Hzrows were schema-exposed and are excluded by the statedband. Entire -20dBcurve is reserved; development -30/-15dB uses four full log-frequency bands with both ratios in each fold. This tests spectral interpolation during selection and ratio interpolation during confirmation, not independent laser transfer. Source already reports inverse-feedback suppression, environmental noise below1kHz, linewidth0.2Hzandnoise floor differences; these cannot be new discoveries. Onlyoneapparatus andone reservedcondition exist. Measurement September–December2024; repositorycoverage2022–2024is broaderandnotassumedthecampaign.
