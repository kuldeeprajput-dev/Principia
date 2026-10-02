# Native assay semantics

The nine Fig6H FCS wells represent three fold doses and named replicate blocks A/B/C, with one BOB negative control. The source paper describes triplicate dual-tagging experiments; no extra cell-line or instrument generalization is inferred. GFP 525.40(488nm)-A and mCherry 610.20(561nm)-A channels are explicit FCS metadata.

A reproducible minimally gated endpoint uses finite signals and positive FSC-A/SSC-A, then channel-wise negative-control99.5th-percentile thresholds. These are explicitly new deterministic gates, not the authors’ unavailable manual FlowJo gates. No editing-genotype conclusion follows solely from fluorescence; the source separately uses ddPCR. The fraction of events jointly exceeding thresholds is the target, in percentage points.

Marginal green/red positive fractions are contemporaneous inputs from the same well, not pre-treatment predictors. Their product is an independence baseline, not an identity. Frechet bounds max(0,p+q-1)<=joint<=min(p,q) constrain every model. Cell events are subsamples, not independent biological validation units. Complete replicate blocks remain together.
