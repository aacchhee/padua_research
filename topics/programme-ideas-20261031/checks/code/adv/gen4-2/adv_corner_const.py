"""Adversarial check (gen4-2): more digits of the constant c in Lambda_corner(Pad_n) = (4/pi^2) log^2 n + 2(2/pi)c1 log n + c + ...
using n = 2^k up to 2048 and a 7-term Euler-Maclaurin-type fit; then an inverse-symbolic attempt on c - c1^2 with mpmath.identify.
Model run: claude-fable-5-1 (adversary gen4-2), 2026-11-01. MEASURED (fit) / UNVERIFIED (any identification)."""
import sys, time, numpy as np
sys.path.insert(0,'/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/adv/gen4-2')
import importlib.util
spec = importlib.util.spec_from_file_location('cf', '/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/adv/gen4-2/adv_corner_fit.py')
# reuse lam_at without re-running the fit script: copy the function source
src = open('/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/adv/gen4-2/adv_corner_fit.py').read()
ns_ = {}
exec(src.split('t0 = time.time()')[0], ns_)
lam_at = ns_['lam_at']
t0=time.time()
a=4/np.pi**2; c1=(2/np.pi)*(np.euler_gamma+np.log(8/np.pi)); b=2*(2/np.pi)*c1
ns=[64,96,128,192,256,384,512,768,1024,1536,2048]
L=[]
for n in ns:
    L.append(lam_at(n,1,-1)); print(f'n={n} {L[-1]:.9f} [{time.time()-t0:.0f}s]', flush=True)
L=np.array(L); nn=np.array(ns,float); ln=np.log(nn)
y=L-a*ln**2-b*ln
for name,A in {
  'c + d log n/n + e/n + f/n^2': np.c_[1+0*ln, ln/nn, 1/nn, 1/nn**2],
  'c + d log n/n + e/n + f log n/n^2 + g/n^2': np.c_[1+0*ln, ln/nn, 1/nn, ln/nn**2, 1/nn**2],
  'c + d log n/n + e/n + f log^2 n/n^2 + g log n/n^2 + h/n^2': np.c_[1+0*ln, ln/nn, 1/nn, ln**2/nn**2, ln/nn**2, 1/nn**2],
  '... + i/n^3': np.c_[1+0*ln, ln/nn, 1/nn, ln**2/nn**2, ln/nn**2, 1/nn**2, 1/nn**3],
}.items():
    coef,*_=np.linalg.lstsq(A,y,rcond=None); r=y-A@coef
    print(f'{name}: c={coef[0]:.9f}  coefs={np.round(coef[1:],5)}  max resid {np.max(np.abs(r)):.1e}')
# also with b free, to confirm b
A=np.c_[ln,1+0*ln, ln/nn, 1/nn, ln**2/nn**2, ln/nn**2, 1/nn**2]; coef,*_=np.linalg.lstsq(A,L-a*ln**2,rcond=None)
print('b free (7-term): b=%.8f (2(2/pi)c1=%.8f) c=%.8f' % (coef[0], b, coef[1]))
c=coef[1]
print('c - c1^2 = %.8f ; c1^2 = %.8f ; c = %.8f' % (c-c1**2, c1**2, c))
try:
    import mpmath as mp
    mp.mp.dps=15
    for val,label in ((c,'c'),(c-c1**2,'c - c1^2'),(c*np.pi**2/4,'c*pi^2/4'),((c-c1**2)*np.pi**2/4,'(c-c1^2)*pi^2/4')):
        print(label, '=', val, ' identify:', mp.identify(mp.mpf(val), ['euler','log(2)','log(pi)','pi','pi**2','euler**2','log(2)**2','log(pi)**2','euler*log(2)','euler*log(pi)','log(2)*log(pi)'], tol=1e-6, maxcoeff=20))
except Exception as ex:
    print('identify failed', ex)
print('elapsed %.0f s'%(time.time()-t0))
