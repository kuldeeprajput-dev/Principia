# NVD annotation coverage: a rare-event non-discovery benchmark

This snapshot does not support a transferable waiting-time or source-load law for NVD-authored CVSS coverage. The predeclared complexity rule selected a constant probability; no positive discrimination is established in the held sources.

## Data and evaluation

A frozen August23,2026 recent NVD feed contributes4425non-rejected CVEs:3037development records in71assigning sources and1388confirmation records in17sources. Entire sources stay linked. The reserved sources contain no positive NVD-authoredCVSSv3.1 annotations, so sensitivity/recall cannot be validated.

Target: **NVD-authored CVSSv3.1 assessment present in current snapshot**, measured as binary source=nvd@nist.gov in cvssMetricV31. Primary error: squared probability (Brier). All covariates are snapshot-available contemporaneous metadata. Source-day count and CNA assessment may be added after initial disclosure. This is current coverage diagnostics, not prediction of future NVD action or security exploitation.

CVE records nested in complete assigning sources; duplicated JSON/gzip representations linked. Source-day batches dependent. Whole CNA/source group folds and held sources; no held-source target calibration.

## Findings and equations

**P100-010-F01 — informative_falsification (supported).** Age, publication-batch and CNA-availability hypotheses do not establish a transferable annotation-coverage mechanism in this snapshot.

p_reference=logistic(a)

NIST April2026 changed duplicate scoring priorities. These metadata are contemporaneous policy/process proxies, not exploitation signals.

Falsifying evidence and limits: All held sources lack the positive endpoint; rare-event calibration alone cannot validate detection, waiting-time hazard or operational triage.

**P100-010-F02 — unsupported_hypothesis (unsupported).** The proposed age/batch hazard equation identifies NVD enrichment dynamics.

Attempts001–004 and006 test age,conditional link andbatchpressure.

A single recent snapshot cannot identify event waiting times, staffing or actual backlog process.

Falsifying evidence and limits: Negligible age gains, unstable flexible transfer, binary-link equivalence005/007 and no heldpositiveclass; hypothesis notadmitted.

Selected executable model: `constant`. Selected p=logistic(a), a=[-5.4463586440393055]. Endpoint is exact NVD-authoredCVSSv3.1 presence, not CVSS severity. All age,source-batch andCNA-conditioned equations remain executable negative comparisons.

All coefficients, input definitions, training groups and transformations are in `rules.json`; the runnable reference performs no fitting.

## Compact numerical evidence

Errors are computed within declared complete groups (with final survey weights when supplied), then averaged equally across groups.

| Frozen model | Development error | Confirmation error | Worst confirmation group |
|---|---:|---:|---:|
| reference | 0.004277048 | 1.843384e-05 | 1.843384e-05 |
| constant | 0.004277048 | 1.843384e-05 | 1.843384e-05 |
| domain | 0.004279076 | 1.913509e-05 | 3.250403e-05 |
| flexible | 0.007502287 | 0.003068499 | 0.04629555 |

Confirmation contains 1388 scored observations in 17 groups. Individual-group scores and every attempted model remain available. Confirmation Brier is about0.000018 for the prevalence reference, versus0.003068 flexible. This apparent low error is driven by zero positive outcomes; it is not evidence of industrial vulnerability prioritization. No positive-class recall or meaningful AUROC can be inferred.

## Interpretation, limitations and use

August23,2026 recent-feed snapshot only. Source status code is excluded; CVSS score formula and severity are not predicted. NIST policy deprioritizes duplicate scoring, so absence is not unsafe analysis failure. Whole-group errors/ranges; no row bootstrap or manufactured independent-population confidence. Confirmation becomes exposed after freeze.

A useful counterexample for ASD: low error, rare labels and policy-driven administrative processes do not establish a new law. Future evaluation must report class support and accept abstention from hazard/discrimination claims.

## Reproducibility and prior art

Run `python run.py` to verify hashes and replay every frozen equation. Predictions use declared input columns only. The shared benchmark evaluator can score alternative equations under the same task; numerical agreement with these coefficients is not required. Public source-aware confirmation is now exposed. No independent experimental replication or certified novelty is claimed.

- [NIST changed CVE enrichment priorities and stopped routinely duplicating CNA scores; modified/deferred status interpretations changed. Any negative CNA availability relationship is policy-consistent reproduction, not new physics.](https://www.nist.gov/news-events/news/2026/04/nist-updates-nvd-operations-address-record-cve-growth) (checked 2026-10-02).
- [Official source metadata; recent feed is a changing snapshot, preserved native hashes.](https://nvd.nist.gov/vuln/data-feeds) (checked 2026-10-02).
