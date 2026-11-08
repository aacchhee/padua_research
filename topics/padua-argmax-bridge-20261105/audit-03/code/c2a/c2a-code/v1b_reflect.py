import math
from scipy import integrate
import numpy as np
pi = math.pi
def I(C, D, e):
    g = lambda t: abs(C/math.tan(t)+D/math.tan(t+e))-abs(C/math.tan(t))-abs(D/math.tan(t+e))
    ts = np.linspace(1e-9, pi-1e-9, 200001)
    h = np.abs(C/np.tan(ts))-np.abs(D/np.tan(ts+e))
    br = list(ts[1:][np.sign(h[1:]) != np.sign(h[:-1])])
    pts = sorted(set([pi/2-e, pi/2, pi-e] + br))
    pts = [p for p in pts if 0 < p < pi]
    return integrate.quad(g, 0, pi, points=pts, limit=2000, epsabs=1e-13)[0]
for (C, D, e) in [(0.3, -1.1, 0.9), (1.0, 0.4, 0.3), (-0.7, 0.2, 1.3)]:
    print(C, D, e, I(C, D, e), I(C, D, pi-e), I(D, C, e))
