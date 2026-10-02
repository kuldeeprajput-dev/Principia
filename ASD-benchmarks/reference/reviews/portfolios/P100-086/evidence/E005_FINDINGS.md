# Stronger history controls for industrial fermentation

## Scenario and methods

The source contains hourly erythromycin-production exports from 406 batches at one facility. The source-defined `hx` chemical potency has undocumented physical units. The task predicts potency six hours ahead, conditional on a current potency assay and its strictly earlier history. It is not an assay-free inline sensor.

Training remains restricted to the original 324 usable development batches. Four forward chronological folds fit earlier batches and score complete later batches; the earliest block only trains. The exposed diagnostic cohort contains 81 later batches and 9,132 observations. The whole-batch mean absolute error (MAE) is averaged equally over batches. No diagnostic result changed candidate selection.

Eight substantive tests compare the six-hour secant, multiscale lags, acceleration, age interactions, exponentially weighted memory, potency feedback, growth/loss asymmetry and a fixed flexible control. Every fold state, failure and coefficient is retained. Features use past values only; duplicate native hours have identical potency values and are documented.

## Findings and equations

A stronger causal-history control challenges the earlier compact hypotheses. The fixed 120-tree histogram-boosting control predicts

$$
\widehat{c}(t+6)=\max\left[0,c(t)+b_0+\sum_{m=1}^{120} f_m(X_t)\right].
$$

Here c is potency in its native unit, t is hours, and X(t) contains the clock, current assay, causal 1/3/6/12-hour slopes, backward curvature, causal weighted slopes and prior-rate variability. Every raw-threshold tree and the intercept is frozen in `rules.json`; `run.py` requires only NumPy and pandas. Portable predictions were checked against the fitting implementation.

The numerical reference's development MAE is **27.360290** and exposed later-batch MAE is **24.484419**, versus **37.759076** for the calibrated six-hour secant: **35.16%** lower diagnostic error. This is a predictive baseline improvement, not an interpretable biochemical law or a comparison with every published forecasting system. Compact multiscale, memory and feedback proposals remain scored; none matched the stronger control in development.

The compact secant remains useful:

$$
\widehat{c}(t+6)=c(t)+6\beta s_6(t),\qquad s_6(t)=\frac{c(t)-c(t-6)}{6}.
$$

The full-development fitted beta is 0.98065907. The source study already models multiscale trends and phases, so these families have established prior art.

## Assay timing and scientific limits

A preregistered development-only stress test keeps the same 26,271 eligible observations across artificial 0/2/6-hour assay delays. The causal latency-aware secant uses the latest assay c(t-lag) and extrapolates by 6+lag hours. Its MAEs are **39.5545**, **58.1412** and **95.5388**; naively reusing the six-hour equation at delayed assay times gives **39.5545**, **154.6205** and **439.5077**. No model was refitted for this audit. These are assumed-delay sensitivities, not measured laboratory turnaround or optimized delay-specific models. Actual receipt timestamps are needed before online operational claims.

In development, **92.646% of 39,217 consecutive hourly triples** have absolute second differences at most one native unit. Such smooth integer ramps are compatible with biological smoothness or upstream interpolation/processing; they do not identify either cause. The released loader does not resolve assay interpolation or true assay times. Source units and upstream processing remain important identification boundaries.

The reference improves historical numerical forecasting and raises the benchmark's comparator standard. It does not establish a new physical law, a causal phase mechanism, independent-facility transfer or deployed production benefit. Individual batch errors, tails and unfavorable regimes remain in `evidence/by_group.csv`. Stop further local mechanism promotion until independent assay timestamps, unit definitions and an unexposed facility/campaign are available.

## Sources and use

Source: [Zenodo 14619074](https://zenodo.org/records/14619074). Prior analysis: [MASTER paper](https://doi.org/10.1016/j.neucom.2025.131701) and [author code](https://github.com/YifeiSunEcust/MASTER), pinned to commit `5d939be43c1faf995e96dd767a3b57c1de92cc11`. The author loader's original scaling/partition conventions differ from this chronological contract; no claim of superiority to MASTER is made.

Run `python run.py` to verify frozen prediction replay. The evaluator supports alternative findings under this information budget; all packaged targets are exposed. Novelty and scientific admission require separate review.
