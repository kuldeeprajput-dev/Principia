from pathlib import Path
import hashlib,json
import pandas as pd
import pydicom
HERE=Path(__file__).resolve().parent
def prepare(root):
 rows=[]
 for a in json.loads((HERE/'SOURCE_MANIFEST.json').read_text())['assets']:
  p=Path(root)/a['path']
  if not p.is_file() or p.stat().st_size!=a['bytes'] or hashlib.sha256(p.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Missing or checksum-mismatched native DICOM: '+a['path'])
  h=pydicom.dcmread(p,stop_before_pixels=True)
  rows.append(dict(sample_id=str(h.SOPInstanceUID),group=str(h.PatientID),modality=str(h.Modality),series=str(h.SeriesInstanceUID),frame=str(getattr(h,'FrameOfReferenceUID','')),rows=int(h.Rows),columns=int(h.Columns),echo_time_ms=float(h.EchoTime) if hasattr(h,'EchoTime') else None,repetition_time_ms=float(h.RepetitionTime) if hasattr(h,'RepetitionTime') else None,series_description=str(getattr(h,'SeriesDescription','')),view=str(getattr(h,'ViewPosition','')),source_anchor=a['path']))
 d=pd.DataFrame(rows)
 if d.sample_id.duplicated().any():raise ValueError('Duplicate SOP instance')
 return d
