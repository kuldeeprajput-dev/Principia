"""Endpoint, threshold-provenance and explicit-calibration regression fixtures."""
from pathlib import Path
import sys,unittest,json
import numpy as np,pandas as pd
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import metrics,batch7_checks,common
from preparation import calibration_records
class Contracts(unittest.TestCase):
 def setUp(self):
  self.y=pd.DataFrame({'group':['a','b'],'target':[0.,1.]});self.x=pd.DataFrame({'group':['a','b']});self.t={'case_number':90,'metric_kind':'mae','aggregation':{'hierarchy':['group']},'scope_limits':'test','target_units':'unit','error_units':'unit','primary_units':'unit'}
 def test_conventional_threshold_is_not_preregistered(self):
  t=dict(self.t,metric_kind='brier');v=metrics.probability_metrics(self.y,[.2,.8],t)['binary_events'];self.assertFalse(v['threshold_registered_before_outcomes']);self.assertEqual(v['status'],'conventional_descriptive_threshold')
 def test_explicit_threshold_requires_provenance(self):
  for d,expected in [({'value':.5,'frozen_before_confirmation':True},False),({'value':.5,'frozen_before_confirmation':True,'provenance':'frozen/threshold.json'},True)]:
   v=metrics.probability_metrics(self.y,[.2,.8],dict(self.t,binary_decision_threshold=d))['binary_events'];self.assertEqual(v['threshold_registered_before_outcomes'],expected)
 def test_invalid_threshold_rejected(self):
  with self.assertRaises(ValueError):metrics.probability_metrics(self.y,[.2,.8],dict(self.t,binary_decision_threshold={'value':0.}))
 def test_rotation_bound(self):
  r=batch7_checks.checks(self.t,self.y,[2.,-1.1],self.x);z=next(x for x in r['tests']if x['test']=='normalized_rotation_bounds');self.assertEqual(z['violations'],2);self.assertTrue(r['diagnostic_only'])
 def test_frechet_bounds(self):
  x=self.x.assign(green=[.8,.1],red=[.7,.9]);r=batch7_checks.checks(dict(self.t,case_number=77),self.y,[40.,11.],x);self.assertEqual(next(z for z in r['tests']if z['test']=='joint_event_frechet_bounds')['violations'],2)
 def test_valid_joint_bounds(self):
  x=self.x.assign(green=[.8,.1],red=[.7,.9]);r=batch7_checks.checks(dict(self.t,case_number=77),self.y,[60.,10.],x);self.assertEqual(next(z for z in r['tests']if z['test']=='joint_event_frechet_bounds')['violations'],0)
 def test_explicit_calibration_preserves_anchor(self):
  d=pd.DataFrame({'sample_id':['s'],'group':['g'],'pilot_seconds':[2.],'input_anchor':['source::circuit']});t={'case_number':31,'calibration_columns':['pilot_seconds'],'calibration':'per-instance pilot'};r=calibration_records(t,d);self.assertIn('input_anchor',r);self.assertEqual(r.pilot_seconds.iloc[0],2.)
 def test_missing_calibration_is_error(self):
  with self.assertRaises(ValueError):calibration_records({'case_number':12,'calibration_columns':['I0'],'calibration':'five points'},self.x)
 def test_explicit_no_calibration_is_empty(self):
  d=pd.DataFrame({'sample_id':['s'],'group':['g'],'target':[1.]});r=calibration_records({'case_number':4,'calibration_columns':[],'calibration':'none'},d);self.assertEqual(len(r),0);self.assertNotIn('target',r)
 def test_stellar_future_timestamp_is_forbidden(self):
  t,p,x,y,r=common.context('P100-002.original.v1');self.assertNotIn('delta_h',t['permitted_inputs']);self.assertNotIn('delta_h',x);self.assertEqual(t['protocol_version'],'P100-002-asd7-native-v1.1')
 def test_risk_unannounced_feedback_mask(self):
  t,p,x,y,r=common.context('P100-088.original.v1');self.assertTrue((x.loc[x.feedback_known==0,'complete']==0).all());self.assertEqual(t['protocol_version'],'P100-088-asd7-native-v1.1')
 def test_adequacy_not_fabricated_prediction(self):
  r=common.registry();c=next(c for c in r['cases']if c['case_id']=='P100-008');self.assertIsNone(c['default_task']);self.assertEqual(c['task_ids'],[]);self.assertFalse(c['predictive_evaluator_ready']);self.assertEqual(len([a for a in r['assessments']if a['case_id']==c['case_id']]),1)
if __name__=='__main__':unittest.main()
