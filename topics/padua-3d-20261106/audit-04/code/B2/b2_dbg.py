import sys, numpy as np, json, base64
sys.argv = ['x', sys.argv[1], '12', '9', '3', '/dev/null']
CODE = open(sys.argv[0] if False else __file__.replace('b2_dbg.py','b2_leb.py')).read()
# exec only the definitions part
cut = CODE.index("rep = {'source'")
exec(CODE[:cut])
cut2 = CODE.index('def negf'); cut3 = CODE.index('order = np.argsort')
exec(CODE[cut2:cut3])
y = np.array([-1.0, 0.9238795325112867, 0.38268343236508984])
f, g = negf(y)
print('val', -f, 'lam', lam(y.reshape(1,3)))
h = 1e-6
for k in range(3):
    e = np.zeros(3); e[k] = h
    print(k, g[k], (negf(np.clip(y+e,-1,1))[0]-negf(np.clip(y-e,-1,1))[0])/(2*h) if k else (negf(y+e)[0]-negf(y)[0])/h)
from scipy.optimize import minimize
r = minimize(negf, y, jac=True, method='L-BFGS-B', bounds=[(-1,1)]*3)
print(r.x, -r.fun, r.message)
r = minimize(negf, y, jac=True, method='L-BFGS-B', bounds=[(-1, 1)] * 3, options={'maxiter': 200})
print('lbfgs maxiter200', -r.fun, r.x)
r2 = minimize(lambda q: negf(np.clip(q, -1, 1))[0], np.clip(r.x, -1, 1), method='Powell',
              bounds=[(-1, 1)] * 3, options={'xtol': 1e-10, 'ftol': 1e-13, 'maxfev': 4000})
print('powell', -r2.fun, r2.x, r2.message, lam(np.clip(r2.x,-1,1).reshape(1,3)))
