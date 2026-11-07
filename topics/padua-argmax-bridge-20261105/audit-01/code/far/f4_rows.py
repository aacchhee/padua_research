# MEASURED binary64 spot check of N1-07 (2)/(4): sum over first/last R rows of |R_r/(nm)-ell_r| vs e_rows bound.
import numpy as np, time
t0 = time.process_time()
def G(n, u, v):
    cu, cv = np.cos(u), np.cos(v)
    Pu = np.cos((n+1)*u) + np.cos(n*u); Pv = np.cos((n+1)*v) + np.cos(n*v)
    return (Pu - Pv)/(cu - cv) - np.cos(n*u)
def ell(r, al, b):
    a = (np.cos(al)+np.cos(b))/2; w = r*np.pi + b
    j = np.arange(-r+1, r, 2)
    return np.sin(b)/w + 8*a*np.sum(1/(w**2-(j*np.pi+al)**2))
def rowsum(n, r, al, b):
    m = n+1; dr = (1-r) % 2
    # j = dr mod 2 with -pi <= (j pi+al)/n < pi
    jlo = int(np.ceil((-n*np.pi - al)/np.pi)); jhi = int(np.floor((n*np.pi - al)/np.pi - 1e-15))
    j = np.arange(jlo, jhi+1); j = j[(j - dr) % 2 == 0]
    j = j[((j*np.pi+al)/n >= -np.pi) & ((j*np.pi+al)/n < np.pi)]
    assert len(j) == n, (len(j), n)
    return np.sum(np.abs(G(n, (j*np.pi+al)/n, (r*np.pi+b)/m)))/2
n = 50000; R = 64; m = n+1
H = np.sum(1/np.arange(1, n+1))
erow = (10*R+33+6*H)/n + 200*(R+2)*(R+1)**2/n**2
erows = (3+H)/n + (2*R-1)*erow
for al, be in [(0.25,0.25),(1.0,0.7),(0.1,2.9),(2.0,0.3),(0.37,0.0)]:
    tot = 0.0; mx = 0.0
    b = be
    e0 = abs(rowsum(n, 0, al, be)/(n*m) - (np.sin(be)/be if be else 1.0))
    tot += e0
    for r in range(1, R):
        e = abs(rowsum(n, r, al, be)/(n*m) - ell(r, al, be)); tot += e; mx = max(mx, e)
    for r in range(1, R+1):
        e = abs(rowsum(n, r, al, -be)/(n*m) - ell(r, al, -be)); tot += e; mx = max(mx, e)
    print("al=%.2f be=%.2f  r0 err=%.2e (bound %.2e)  max row err=%.2e (bound e_row %.2e)  total=%.3e (bound e_rows %.3e)" % (al, be, e0, (3+H)/n, mx, erow, tot, erows))
print("cpu", time.process_time()-t0)
