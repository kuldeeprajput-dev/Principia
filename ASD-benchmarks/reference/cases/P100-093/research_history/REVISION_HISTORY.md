# Technical correction

The first baseline process stopped after the control-copy diagnostic because pandas DataFrame.quantile is a method. Replaced dot access with explicit column indexing before any fitted baseline or ASD attempt completed. No outcome or protocol change; confirmation remains closed.
