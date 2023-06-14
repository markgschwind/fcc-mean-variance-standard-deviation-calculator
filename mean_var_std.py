import numpy as np

def calculate(list):
  if len(list) < 9:
    raise ValueError('List must contain nine numbers.')  
  else:
    nrs = np.array(list).reshape((3,3))
    calculations = {
      'mean': [nrs.mean(axis=0).tolist(), nrs.mean(axis=1).tolist(), nrs.flatten().mean()],
  'variance': [nrs.var(axis=0).tolist(), nrs.var(axis=1).tolist(), nrs.flatten().var()],
  'standard deviation': [nrs.std(axis=0).tolist(), nrs.std(axis=1).tolist(), nrs.flatten().std()],
  'max': [nrs.max(axis=0).tolist(), nrs.max(axis=1).tolist(), nrs.flatten().max()],
  'min': [nrs.min(axis=0).tolist(), nrs.min(axis=1).tolist(), nrs.flatten().min()],
  'sum': [nrs.sum(axis=0).tolist(), nrs.sum(axis=1).tolist(), nrs.flatten().sum()]
}
    return calculations
