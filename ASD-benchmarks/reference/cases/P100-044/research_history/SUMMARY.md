# P100-044: scientific portfolio

capped elapsed solver resource consumption min(Total Runtime,7200s).

5 substantive attempts; reference selected before confirmation: **exp_size**.

| Candidate | Development MAE | Parameters | Confirmation MAE |
|---|---:|---:|---:|
| constant | 2948.466 | 1 | 4808.836 |
| exp_size | 629.7206 | 5 | 980.825 |
| form_median | 2364.617 | 3 | 4095.026 |
| rbf | 1614.099 | 37 | 1182.146 |
| attempt_001 | 2701.923 | 4 | 4088.67 |
| attempt_002 | 1742.769 | 4 | 1236.824 |
| attempt_003 | 759.787 | 5 | 1069.29 |
| attempt_004 | 767.2382 | 7 | 1111.63 |
| attempt_005 | 1182.693 | 4 | 556.2756 |

Units: seconds. All final results are exposed; confirmation alternatives did not change selection.

Attempts004 and005 fail to improve the established size-degree model in primary error, worst-group error or offline selection regret. The proposed occupancy/combinatorial/smooth-cap alternatives are not supported as better resource laws. Five substantive attempts retained; retain established baseline as reference.

One solver/hardware experiment,16 structural instances,three formulations,one run each. Consumption censored by a7200s resource cap; not latent solve time or general computational complexity. No deployed impact evidence.
