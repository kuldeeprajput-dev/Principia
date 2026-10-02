# Pre-fit layout and unit corrections

Before any fit or score, schema audit found Japan/Kids coordinates in centimetres and the singleton Teenagers CSV one directory level shallower. Native adapter now converts explicit centimetre headers to metres and admits the teen singleton as development only. Preliminary preparation is preserved; no candidate or confirmation score was inspected or used.

A second pre-fit time audit found nonzero recording origins and short child clips. Set per-trial integer grid fromceil(minimum native time), a2-second calibration/target horizon, and origins>=4relative seconds. This admits all protocol groups without filling missing outcomes. The preliminary5-second absolute-clock draft excluded children/teenagers and is preserved; no model was fit.

Prefix audit before any fit replaced full-trial ID count with currently observed tracked IDs and removed dependence on each track future endtime. A pastsample<=1secondold is eligible. This fixes an information-availability defect without reading future target scores; preliminary preparation is preserved.
