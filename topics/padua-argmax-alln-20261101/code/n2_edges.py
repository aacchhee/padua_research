"""4001-point scan of lambda_2 along each edge (float64, MEASURED)."""
import numpy as np
from maj import setup, lam
S = setup(2)
t = np.linspace(0, np.pi, 4001)
for nm, X, Y in [('x=+1', 0*t, t), ('x=-1', 0*t+np.pi, t), ('y=+1', t, 0*t), ('y=-1', t, 0*t+np.pi)]:
    l = lam(2, X, Y, S)[0]
    i = l.argmax()
    print(nm, 'max %.12f at %.4f*pi' % (l[i], t[i]/np.pi), 'count>=3-1e-9:', (l > 3-1e-9).sum())
