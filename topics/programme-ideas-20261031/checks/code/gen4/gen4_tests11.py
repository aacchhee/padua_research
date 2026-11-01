import numpy as np, sys, time
sys.path.insert(0,'.')
from gen4_tests9 import lam_at
def leb1d(nodes, x):
    L=np.ones(len(nodes))
    for i,xi in enumerate(nodes):
        for j,xj in enumerate(nodes):
            if i!=j: L[i]*= (x-xj)/(xi-xj)
    return np.sum(np.abs(L))
def leb1d_max(nodes, m=4001):
    g=np.cos(np.linspace(0,np.pi,m)); return max(leb1d(nodes,x) for x in g[::max(1,m//400)]) 
for n in (10,20,40,80,160):
    cheb = np.cos((2*np.arange(n+1)+1)*np.pi/(2*(n+1)))        # n+1 Chebyshev zeros
    lob_n = np.cos(np.arange(n+1)*np.pi/n)                       # n+1 Chebyshev-Lobatto (extrema), as Padua x-grid
    lob_n1 = np.cos(np.arange(n+2)*np.pi/(n+1))                  # n+2, Padua y-grid
    Lc = leb1d(cheb,1.0); Ll_n = max(leb1d(lob_n,x) for x in np.cos(np.linspace(0,np.pi,801))); Ll_n1=max(leb1d(lob_n1,x) for x in np.cos(np.linspace(0,np.pi,801)))
    Lpad = lam_at(n,1,-1)
    asym = (2/np.pi)*np.log(n)+(2/np.pi)*(np.euler_gamma+np.log(8/np.pi))
    print('n',n,'Pad %.4f'%Lpad,'| cheb1D %.4f lob_n %.4f lob_n1 %.4f asym %.4f'%(Lc,Ll_n,Ll_n1,asym),'| Pad-cheb^2 %.4f Pad-lob_n*lob_n1 %.4f Pad-lob_n^2 %.4f Pad-asym^2 %.4f'%(Lpad-Lc**2,Lpad-Ll_n*Ll_n1,Lpad-Ll_n**2,Lpad-asym**2))
