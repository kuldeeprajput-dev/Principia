"""Predict from portable frozen models, never from stored prediction values."""
import numpy as np
from . import current, adaptive, followups, transport, falsifiers
from . import previous_pilot, previous_cho, previous_mech, previous_bio
ENGINES={m.__name__.rsplit('.',1)[-1]:m for m in (current,adaptive,followups,transport,falsifiers,previous_pilot,previous_cho,previous_mech,previous_bio)}
def predict_one(state,data):
 result=np.asarray(ENGINES[state['engine']].predict(state['model'],data),float)
 if result.shape!=(len(data),) or not np.isfinite(result).all():raise ValueError('Invalid model prediction')
 return result
def predict(model,data):
 """OOF reproduction by sample identity; deployment requires explicit mode."""
 mode=model.get('mode','oof')
 if mode=='deployment':return predict_one(model['deployment'],data)
 if mode!='oof':raise ValueError('mode must be oof or deployment')
 if 'sample_id' not in data or data.sample_id.isna().any() or data.sample_id.duplicated().any():raise ValueError('Unique nonmissing sample_id required')
 ids=data.sample_id.astype(str);mapping=model['validation_fold_by_sample_id'];missing=set(ids)-set(mapping)
 if missing:raise ValueError('Unknown OOF samples: deployment must be requested explicitly')
 folds=ids.map(mapping);out=np.zeros(len(data),float)
 for fold in folds.unique():
  rows=np.flatnonzero(folds.to_numpy()==fold);state=model['folds'][fold];out[rows]=predict_one(state,data.iloc[rows].reset_index(drop=True))
 return out
