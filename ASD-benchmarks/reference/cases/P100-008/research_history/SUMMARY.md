# EA1141 breast imaging: a scientific admissibility reference

The retained scenario contains 70 T2-weighted MR slices and one left craniocaudal mammogram from **one patient**. It is useful for inspecting imaging metadata and proposing questions, but does not support an independently validated clinical or quantitative physiological discovery by itself.

## What the five investigations establish

1. **Clinical discrimination:** no retained outcome table and no independent patient cohort support diagnostic accuracy.
2. **Relaxometry:** all MR slices share TE = 70 ms and TR = 4271.85888671875 ms. In the idealized relation $S(TE)=A\exp(-TE/T_2)$, one echo cannot identify both amplitude $A$ and relaxation time $T_2$. Different slices are different tissues, not repeated echoes.
3. **Cross-modal geometry:** MR and MG occupy distinct frames; a single compressed projection and no correspondence truth cannot validate a unique tissue deformation.
4. **Absolute physiology:** sequence-dependent MR intensity cannot be interpreted as a calibrated concentration without additional measurements.
5. **Generalization:** slices of one series are linked observations. Slice interpolation cannot establish a between-patient biological law.

These are **supported negative adequacy findings**, not novel physics. No artificial regression target, accuracy score or positive ground truth has been manufactured. The original EA1141 screening study remains prior art; its study-level evidence must not be attributed to this small retained subset.

## Reproduction and future findings

`python run.py` verifies hashes and the frozen source-prerequisite checks. `data/native_anchors.csv` records every DICOM instance and acquisition metadata; `data/source_evidence.json` is the compact audit. The research `native.py` recreates these metadata from hash-verified local native assets without reading image pixels. No model was fitted, no reserved predictive test exists, and the metadata audit is retrospective.

A later agent may propose an alternative measurable assertion. It must first obtain review of a new task contract, including units, independent evidence, identifiability and validation scope. The included rubric explains what extra measurements would make each scientific hypothesis testable. The absence of such measurements in this corpus does not imply their absence from the full TCIA collection.

## Sources

[Official TCIA collection](https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=157286463), [dataset DOI](https://doi.org/10.7937/2BAS-HR33), and [original screening study](https://doi.org/10.1001/jama.2020.0572). Native DICOM redistribution follows CC BY 4.0. This local package contains only derived metadata and analysis documentation.
