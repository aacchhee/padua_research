"""Small constructions explaining T208's two statement qualifications.

The QR example is a subspace-sensitivity construction, not a claim that a
particular QR library returns the perturbed subspace on the original input.
"""
import json
import numpy as np

u = np.finfo(float).epsneg
# x=0, y=(0,1,2), weights=1. Under T208(a) U(1) is not required.
X = np.zeros((3,3))
Pi0 = np.diag([1.,0.,0.])
Pi1 = np.eye(3)
delta = np.linalg.norm((np.eye(3)-Pi1)@X@Pi0, 2)
norm = np.linalg.norm(X,2)
assert delta == norm == 0
print(json.dumps(dict(case='zero_operator',delta=float(delta),operator_norm=float(norm),
                      normalized_quotient='undefined 0/0; unnormalised inequality true')))

eps = u/16
Q = np.array([[1.,1.],[0.,eps],[0.,0.]])
D = np.array([[0.,0.],[0.,0.],[0.,eps]])
V = np.linalg.qr(Q, mode='reduced')[0]
Vp = np.linalg.qr(Q+D, mode='reduced')[0]
projector_distance = np.linalg.norm(V@V.T-Vp@Vp.T,2)
relative_change = np.linalg.norm(D,2)/np.linalg.norm(Q,2)
assert relative_change < u
assert abs(projector_distance-1/np.sqrt(2)) < 1e-14
print(json.dumps(dict(case='QR_backward_error_does_not_give_uniform_subspace_error',
                      relative_input_change=float(relative_change),unit_roundoff=float(u),
                      condition=float(np.linalg.cond(Q)),projector_distance=float(projector_distance))))
