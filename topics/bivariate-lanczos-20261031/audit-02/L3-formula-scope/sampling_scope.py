"""Focused floating check of the new T313/T319 sampling attribution.
No interval-certificate rerun; no source imports; no claim of exact sign.
"""
import numpy as np
from numpy.polynomial.chebyshev import chebval

print('NumPy', np.__version__, 'MEASURED only', flush=True)
radii = []
for n in range(4, 13):
    def T(k, z):
        a = np.zeros(k+1)
        a[k] = 1
        return chebval(z, a)

    def P(x, y):
        g = [T(n-m, x)*T(m, y)-T(m, x)*T(n+1-m, y) for m in range(4)]
        return 9*(g[1]**2-.5*g[0]*g[2])+g[2]**2-g[1]*g[3]

    a = np.linspace(0, 2*np.pi, 720, endpoint=False)
    u, v = np.cos(a), np.sin(a)
    found = False
    for r in np.geomspace(1e-4, .5, 200):
        for j, k in [(j, k) for j in range(n+1) for k in range(n+2) if (j+k)%2 == 0]:
            values = P(np.cos(j*np.pi/n)+r*u, np.cos(k*np.pi/(n+1))+r*v)
            if values.min() < 0:
                radii.append(r)
                print(f'n={n}: first r={r:.12g}, first node(j,k)={(j,k)}, '
                      f'min P={values.min():.12g}', flush=True)
                assert (j, k) == (1, 1)
                found = True
                break
        if found:
            break
    assert found
lower = np.array([5.6302e-4, 1.0225e-4, 2.3627e-5, 6.6062e-6, 2.1471e-6,
                  7.8710e-7, 3.1825e-7, 1.3955e-7, 6.5495e-8])
print('Descriptive slopes from nine finite values: sampled',
      np.polyfit(np.log(np.arange(4, 13)), np.log(radii), 1)[0], 'lower bounds',
      np.polyfit(np.log(np.arange(4, 13)), np.log(lower), 1)[0])
print('PASS attribution (1,1); no asymptotic or certified-upper-bound conclusion')
