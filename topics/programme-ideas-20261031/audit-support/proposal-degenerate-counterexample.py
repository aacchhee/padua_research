"""Test the local implication used by degenerate_max, not a Padua counterexample.
Four polynomials sum to one near the origin, and their sum of absolute values is
2-x^2-y^2+eps*abs(x), which has two strict maxima at (+/-eps/2,0).
They are not claimed to be a complete Lagrange basis; the point is that the local
jet inequalities alone do not imply the claimed one-maximum conclusion.
"""
import pathlib,sys,json
import numpy as np
root=pathlib.Path(__file__).resolve().parents[1]
sys.path[:0]=[str(root/'checks/code/decisive/gen4-2'),str(root/'checks/code/gen4')]
from t3_certify import Certifier
eps=1e-12
class Local:
    n=2
    MB=np.array([10.,10.,10.,10.])
d={k:np.zeros((1,4)) for k in ('L','Lt','Lp','Ltt','Ltp','Lpp')}
d['L'][0]=[1.5,-.5,0.,0.]
d['Lt'][0]=[0.,0.,eps/2,-eps/2]
d['Ltt'][0]=[-1.,1.,0.,0.]
d['Lpp'][0]=[-1.,1.,0.,0.]
got=Certifier.degenerate_max(Local(),np.zeros(2),np.array([2,3]),d)
out=dict(returned=got,epsilon=eps,exact_number_of_maxima_in_returned_disc=2,
         exact_maxima_x=[-eps/2,eps/2],scope='local certificate implication, not a Padua count refutation')
print(out)
(root/'audit-support/proposal-degenerate-counterexample.json').write_text(json.dumps(out,indent=2))
