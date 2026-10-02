# Retrospective US inflation adjustment: compact forecasting evidence and limits

A two-term partial-adjustment equation improves on persistence in development and confirmation, but does not beat the training-only constant in the reserved recent period. The portfolio supports an interpretable scoped forecasting relationship, not a new structural inflation law.

## Data and evaluation

Six US seasonally adjusted CPI/CES series from the preserved BLS bulk snapshot. Development uses1990–2022, with forward five-year validation blocks from2000; confirmation uses2023–2025September,33months in11quarters. Complete-calendar eligibility excludes later months after a missing2025October CPI observation. The source snapshot extends into2026 but those later dates are not silently imputed.

Target: **Next-month seasonally adjusted all-items CPI log change**, measured as percentage points per month (100 natural log index ratio). Primary error: percentage points. Only calendar months through t-1 enter predictors for month t. This is a retrospectively revised and seasonally adjusted bulk snapshot, not an as-issued forecast archive. Calendar lags do not establish historical release availability; the nominal origin is after prior-month releases. No month-t prices/employment or CPI accounting decomposition enters inputs.

Whole calendar quarter; forward chronological development folds and2023-onward confirmation. One national economic system, overlapping lag windows and persistent macro shocks; quarters are not independent economies. All regression coefficients, centering/scales and flexible centers fit only preceding development blocks. No held-quarter target fitting.

## Findings and equations

**P100-016-F01 — reproduction (partially_supported).** Lagged partial adjustment provides an interpretable predictor better than persistence, with limited cross-period superiority.

p_hat=p12+a(p1-p12)+b[(h+m)/2-p1]

Partial persistence and sector-relative price adjustment are established forecasting motifs. The coefficient is phenomenological, not an identified causal relaxation constant.

Falsifying evidence and limits: Confirmation constant MAE0.105693 beats reference0.108585; uncertainty is group descriptive, no independent-quarter confidence.

**P100-016-F02 — informative_falsification (supported).** Adding employment pressure, shock asymmetry, robust fitting or acceleration does not establish a new stable inflation mechanism.

See frozen attempts003–006 and nested controls.

Employment improved a worst-quarter diagnostic while damaging mean transfer; asymmetry traded mean and worst-group performance.

Falsifying evidence and limits: No causal intervention, revision-free vintages, or independent economic systems; no structural law or demonstrated financial value.

Selected executable model: `attempt_002`. Let p1,p12 denote previous-month inflation and the trailing12-month mean, h,m previous housing and medical inflation. The selected equation is p_hat=p12+a(p1-p12)+b[(h+m)/2-p1], where a=0.6788581552753963, b=0.25333515480765123. Every term is in monthly log-change percentage points. This is a lagged adjustment representation; housing/medical averages are not an exact CPI decomposition.

All coefficients, input definitions, training groups and transformations are in `rules.json`; the runnable reference performs no fitting.

## Compact numerical evidence

Errors are computed within declared complete groups (with final survey weights when supplied), then averaged equally across groups.

| Frozen model | Development error | Confirmation error | Worst confirmation group |
|---|---:|---:|---:|
| reference | 0.2006199 | 0.1085852 | 0.2049382 |
| annual_mean | 0.224154 | 0.1167382 | 0.2012013 |
| constant | 0.2156496 | 0.1056932 | 0.177262 |
| flexible | 0.2260805 | 0.1132284 | 0.2328886 |
| persistence | 0.2295867 | 0.1289942 | 0.3072 |

Confirmation contains 33 scored observations in 11 groups. Individual-group scores and every attempted model remain available. Reference confirmation MAE0.108585percentagepoints versus persistence0.128994, annualmean0.116738, flexible0.113228 and constant0.105693. The constant is better, so universal predictive superiority is falsified. No post-confirmation reselection: attempt005/006 remain diagnostics despite some lower recent errors.

## Interpretation, limitations and use

1990–2026 US selected national seasonally adjusted series. Revised historical values and seasonal factors can incorporate later information. No causal Phillips-curve, policy intervention, operational financial-return or structural-inflation law claim. Quarter-group errors/ranges; no row bootstrap or independent-quarter population confidence. Confirmation will become exposed.

Useful as a compact source-aware retrospective forecasting reference and a test of avoiding policy/causal overclaim. Revised seasonal factors and benchmarked employment make this unsuitable as a proven real-time trading or monetary-policy model.

## Reproducibility and prior art

Run `python run.py` to verify hashes and replay every frozen equation. Predictions use declared input columns only. The shared benchmark evaluator can score alternative equations under the same task; numerical agreement with these coefficients is not required. Public source-aware confirmation is now exposed. No independent experimental replication or certified novelty is claimed.

- [Annual CPI seasonal re-estimation revises prior five years;2021–2025 recalculated in February2026.](https://www.bls.gov/cpi/seasonal-adjustment/) (checked True).
- [CES revisions reflect later responses and annual benchmarks; seasonal histories can change five years.](https://www.bls.gov/web/empsit/cesfaq.htm) (checked True).
