# Cycling dynamics after a causal measurement-clock repair

## Scenario and task

BikeZ records 28 recurring riders in one controlled circular-track session. The older task used author RTS-smoothed instantaneous speeds. This version instead uses pre-final-Kalman, manually assisted position annotations acquired from the author repository at commit `ea1f8029c08949d7da019d12bc4a729ce4778ee6`: 27 files, 5.38 MB. Source labels, homography and human annotation assistance remain; this is not an end-to-end online visual system.

The distinct task `P100-096-forward-arc-actual-clock-v2` predicts the direction-projected mean angular-arc speed over the next approximately one-second observation interval. Its target and inputs differ from the old task, so their MAEs must not be compared. Small negative projected targets caused by reverse/noisy displacement are retained.

Two narrow-lane blocks form development: videos 0003–0005 train and 0007–0009 validate. All of wide-lane videos 0010–0012 form one connected diagnostic block; video 0010 is removed from fitting despite being in the old development partition. The diagnostic contains 5,833 observations. There are no independent new sessions or held-out riders.

## Solid measurement finding

Manual positions often arrive every 10 frames at 25 Hz, whereas nominal prediction samples are every 25 frames. Previous-observation holding therefore produces alternating **0.8/1.2-second observation windows**. Dividing every displacement by one nominal second produces a spurious negative acceleration response: the nominal-clock fit selects coefficient **−0.9283**, almost persistence of the previous interval. That behavior must not be interpreted as cyclists systematically reversing acceleration.

The repaired secant divides by its actual observed duration:

$$
v_t=\frac{\left|\Delta\theta_t\right|\bar{r}_t}{\Delta f_t/25}.
$$

Here theta is unwrapped angle, r-bar the average observed radius in metres, Delta-f the actual frame difference, and v is in m/s. This absolute secant is the current input. The future target uses the direction determined from the past window:

$$
y_t=d_t\,\Delta\theta_{t,+}\,\overline{r}_{t,+}/(\Delta f_{t,+}/25),\qquad d_t=\mathrm{sign}_{+}(\Delta\theta_{t,-}).
$$

The function sign-plus returns +1 for a nonnegative past angular increment and -1 otherwise. The future increment may reverse that past direction, so negative targets are retained. Annotation frames are the latest available at or before each nominal sample; permitted age is at most five frames (0.2 s). All inputs use observations at or before the decision frame. No future interpolation or RTS smoothing enters predictors; neighbor availability depends only on current/past observations, not future target availability. Future positions define targets only.

After clock repair, previous-interval persistence and fixed positive acceleration are both worse than current-interval persistence in development. This is a reproducible metrology correction, not a new behavioral law.

## Scoped leader-response candidate

The strongest compact development candidate is

$$
\widehat{v}_{t+}=\max\left[0,v_t+\frac{\beta(v_{L,t}-v_t)}{1+g_t/(5\,\mathrm{m})}\right],\qquad \beta=0.3801850775.
$$

The leader is nearest in the causal observed riding direction, with compatible direction and radial separation at most 1 m. g is centre-to-centre angular-arc spacing, not verified bumper clearance. The positive dimensionless response fraction is attenuated with spacing. It is task-specific, not an identified continuous-time relaxation constant.

Development MAE is **0.259050 m/s** versus **0.274505 m/s** for persistence. The exposed connected wide-lane block gives **0.262045 m/s** versus **0.271980 m/s**: **3.65%** lower error. Matched, identically gated reverse-direction and shuffled-neighbor controls give **0.271691** and **0.271195 m/s**. Their weak gains support directional specificity within this task, while shared perturbations and annotation noise remain competing explanations.

Thirteen actual-clock tests and five adaptive scale/simplification/falsifier tests were completed. A fitted 2 m spacing scale slightly improves development error, but the fixed 5 m, one-coefficient rule was selected by the preregistered simplicity criterion. It was not replaced by a diagnostic winner. The nominal-clock campaign is preserved as a falsified measurement version.

## Meaning, limits and next evidence

Relative-speed relaxation and spacing effects are established traffic-model ideas. This candidate is a small, physically plausible within-session association, not a new traffic law, collision-prevention claim or deployed safety result. One development validation block and one connected diagnostic block do not justify a population confidence interval. Rider recurrence, manual annotation, radial lane approximation, irregular intervals and direction uncertainty near stopping restrict interpretation.

The useful advance is to separate a clock artifact from a modest, correctly gated leader response. Fresh sessions with causally available detections, independent riders, controlled perturbations and stronger same-information bicycle-following models are necessary before promotion.

## Sources and use

[Author repository](https://github.com/DerKevinRiehl/mass_cycling_experiment), [BikeZ source methods](https://www.nature.com/articles/s41597-026-07247-7), and [prior bicycle-following study](https://doi.org/10.3390/su13063487). Run `python run.py` for frozen replay. This package's evaluator uses the repaired task and cannot score the old RTS-speed task interchangeably. All outcomes are exposed research diagnostics.
