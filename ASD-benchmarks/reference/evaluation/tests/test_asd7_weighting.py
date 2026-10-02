"""Hand-calculated tests for the additive survey-weighted estimand."""
import unittest
import numpy as np
import pandas as pd
from metrics import weights,score,event_metrics,interval_metrics

class SurveyWeights(unittest.TestCase):
 def setUp(self):
  self.d=pd.DataFrame({'group':['a','a','b'],'target':[0.,4.,2.],'sample_weight':[3.,1.,8.]})
  self.t={'aggregation':{'hierarchy':['group'],'within_group_weight':'sample_weight'},'metric_kind':'mae','primary_units':'unit','error_units':'unit','target_units':'unit'}
 def test_hand_computed_mae_and_group_risk(self):
  self.assertTrue(np.allclose(weights(self.d,self.t),[.375,.125,.5]))
  z,g=score(self.d,[0.,0.,0.],self.t)
  self.assertAlmostEqual(z['primary_error'],1.5)
  self.assertAlmostEqual(z['group_balanced_mae'],1.5)
  self.assertEqual([a['mae']for a in g],[1.,2.])
 def test_unweighted_unchanged(self):
  t=dict(self.t,aggregation={'hierarchy':['group']})
  self.assertTrue(np.allclose(weights(self.d,t),[.25,.25,.5]))
  self.assertAlmostEqual(score(self.d,[0.,0.,0.],t)[0]['primary_error'],2.)
 def test_scale_invariance_within_each_group(self):
  d=self.d.copy();d.loc[d.group=='a','sample_weight']*=100
  self.assertTrue(np.allclose(weights(d,self.t),weights(self.d,self.t)))
 def test_extreme_finite_weights_no_denominator_overflow(self):
  d=pd.DataFrame({'group':['a','b'],'target':[0.,1.],'sample_weight':[1e308,1e308]})
  self.assertTrue(np.allclose(weights(d,self.t),[.5,.5]))
 def test_invalid_weights(self):
  for v in [0.,-1.,float('inf'),float('nan')]:
   d=self.d.copy();d.loc[0,'sample_weight']=v
   with self.assertRaises(ValueError):weights(d,self.t)
 def test_missing_declared_weight(self):
  with self.assertRaises(ValueError):weights(self.d.drop(columns='sample_weight'),self.t)
 def test_hierarchy_is_not_silently_changed(self):
  t=dict(self.t,aggregation={'hierarchy':['group','particle'],'within_group_weight':'sample_weight'})
  with self.assertRaises(ValueError):weights(self.d,t)
 def test_f1_complete_failure(self):
  d=self.d.copy();d.target=[0.,1.,1.];r=event_metrics(d,[1.,0.,0.],self.t,.5)
  self.assertEqual(r['f1'],0.)
 def test_zero_event_undefined(self):
  d=self.d.copy();d.target=0.;r=event_metrics(d,[0.,0.,0.],self.t,.5)
  self.assertIsNone(r['f1']);self.assertIsNotNone(r['undefined_reasons']['f1'])
 def test_weighted_interval_coverage(self):
  r=interval_metrics(self.d,np.zeros(3),np.zeros(3),np.ones(3)*2,.9,self.t)
  self.assertAlmostEqual(r['group_balanced_coverage'],.875)
 def test_conditional_coverage_reweights_same_observations(self):
  d=self.d.iloc[[0,2]];self.assertTrue(np.allclose(weights(d,self.t),[.5,.5]))

if __name__=='__main__':unittest.main()
