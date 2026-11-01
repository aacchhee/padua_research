import numpy as np, sys
from scipy.ndimage import maximum_filter
sys.path.insert(0,'.')
from gen4_tests15 import leb
for n in (6,8):
    for m,uni in ((641,False),(1281,False),(1281,True),(2001,True)):
        lam,GX,GY=leb(n,m,uni)
        for size in (3,5):
            mx=(maximum_filter(lam,size=size,mode='nearest')==lam); inter=mx.copy(); inter[0,:]=inter[-1,:]=inter[:,0]=inter[:,-1]=False
            # strict: also require > all neighbours except itself (exclude plateaus): use lam > maximum_filter of lam with centre removed
            print('n',n,'mesh',m,'uniform' if uni else 'cheb','filter',size,'interior',int(inter.sum()),'total',int(mx.sum()))
