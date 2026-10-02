# Source and units

Zenodo16033764 and ScientificReports DOI10.1038/s41598-025-24666-5. The RAR contains31 raw `noisy_s` traces and pairedGHKSS noise-reduced representations. NativeMATLABPSDcode explicitly labels `noisy_s` as voltage. The paper and code disagree on velocityconversion; this task usesV and doesnot inferphysicalmechanicalcoefficients.

Archive extraction uses systembsdtar `tar -xOf` for a manifest-listed member, neverunpacksarbitrarypaths. Rawtime vectors are verified at0.5ms except1172at1ms. No authornoise-reducedsignal enters predictors or targets.
