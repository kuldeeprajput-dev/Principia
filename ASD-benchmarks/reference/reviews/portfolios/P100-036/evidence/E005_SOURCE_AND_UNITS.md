# Source semantics and pre-fit endpoint revision

The native integrated workbook has347 source-derived imaging/laboratory rows and81 plantIDs; metadata associate each plant with one cultivar/treatment. Main and metadata row orders differ. We join cultivar/treatment by exact PlantID, never by row order. Entire plants remain in one partition.

The source calls QY_max maximum quantum yield, a dimensionless fluorescence readout. NPQ_Lss/Rfd_Lss and NGRDI are separate source-extracted dimensionless measures; they can share underlying fluorescence measurements, so this is a contemporaneous readout diagnostic rather than independent hydration or molecular confirmation. AREA_MM is retained in its source scale and used only as a relative log descriptor; no area-unit conversion or heat flux is inferred.

Before any fit, RWC was dropped because its normalization/percent convention was not explicitly documented. The main workbook defines DAS as days after sowing; author code README defines it as days after stress. Both source files remain untouched, and all age variables are excluded. Source publication metadata and author code are primary references; the author repository still uses a manuscript DOI placeholder. No full article-specific novelty review is claimed.
