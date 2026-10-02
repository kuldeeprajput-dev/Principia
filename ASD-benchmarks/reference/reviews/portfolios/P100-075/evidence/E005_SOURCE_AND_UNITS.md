# Source and measurement semantics

The RDS contains author-aligned raw gene counts for 24 libraries: four donors by two shear levels by three substrate stiffnesses. The source CSV labels stiffness as `pressure`; the source article identifies 30, 200 and 1000 kPa as substrate stiffness, not fluid pressure. HSS and LSS are 10 and 4 dyn/cm². VCAM1 is Entrez gene 7412, confirmed against NCBI.

Response: log2(1 + 10^6 VCAM1 counts / total counts in that library). This conventional count-depth transform is not absolute transcript concentration. The calibration measurement is the same donor at LSS/30 kPa. Five remaining conditions per donor are targets; calibration is explicitly permitted and equally available to every comparator. This diagnostic requires destructive gene-expression measurements of calibration cultures and is not real-time sensing.

Counts were not printed before the protocol/split freeze. Library count matrix normalization is per sample; no target across donors informs inputs. Biological replicates are donors, not genes or condition rows. Published VCAM1 stiffness/shear findings make mechanosensing reproduction prior art.
