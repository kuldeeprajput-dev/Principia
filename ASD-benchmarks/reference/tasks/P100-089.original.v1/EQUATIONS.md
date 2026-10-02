# Executable equations

The exact frozen coefficients and feature transformations are in `rules.json` and `run.py`. No coefficient is fitted during replay.

Selected equation: Pr(Choice=1 | available history) = 1 / (1 + exp(-beta dot phi)).

Let r=reward/2, p=the experimenter-specified probability, a=child, m=multi-option context, v=explicit-description context, h=the previous-choice running mean minus0.5, and l=the immediately previous choice minus0.5. The ordered vector phi is (1,r,p,r*p,r^2,p^2,a,m,v,a*m,a*v,r*a,p*a,r*m,p*m,r*v,p*v,h,l,h*a,h*m,trial_progress). The intercept is -3.302904, and the h and l coefficients are 2.629934 and 1.308668. Child/adult and context interactions alter those effects; an isolated coefficient is not a causal effect. The frozen coefficients already undo training feature-RMS scaling, so the displayed vector is used directly without standardization. Adult age is not included in this selected model.

| Coefficient index | Value |
|---|---:|
| 0 | -3.30290352626 |
| 1 | 1.47286345799 |
| 2 | -2.61575844098 |
| 3 | 3.58786851701 |
| 4 | -0.471636605786 |
| 5 | 0.312298418327 |
| 6 | 3.65230176388 |
| 7 | -3.80563362005 |
| 8 | -4.32171536934 |
| 9 | 0.812767687682 |
| 10 | 0.512742169467 |
| 11 | -0.954940765827 |
| 12 | -2.79792317724 |
| 13 | 1.15137185214 |
| 14 | 3.10887010172 |
| 15 | 1.01583503602 |
| 16 | 4.50866354376 |
| 17 | 2.62993406839 |
| 18 | 1.30866759121 |
| 19 | -1.16486480048 |
| 20 | 1.4772801405 |
| 21 | -0.206919560775 |

Each model is separate from the scientific finding and evaluation task. All alternative states remain available for numerical comparison.

For the selected flexible model let r=reward/2, p=probability, a=child, m=multi, v=description, h=history_mean-0.5, l=lag_choice-0.5. Its ordered vector is [1,r,p,r*p,r^2,p^2,a,m,v,a*m,a*v,r*a,p*a,r*m,p*m,r*v,p*v,h,l,h*a,h*m,trial_progress]. Predicted probability is sigmoid(beta dot vector). Coefficients are dimensionless.
