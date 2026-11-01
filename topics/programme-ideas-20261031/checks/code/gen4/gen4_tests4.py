import numpy as np, sys
sys.path.insert(0,'.')
from gen4_tests import padua, cheb_basis
# Saturation test: s_k(B) = w_B * K_k^disc(B,B) in (0,1]; =1 iff node resolved at degree k. Where/how many nodes saturate as theta grows?
for weights in ('equal','cubature'):
  for n in (20,40,60):
    P,w = padua(n)
    if weights=='equal': w=np.ones(len(P))/len(P)
    for th in (0.5,0.7,0.8,0.9,0.95):
        k=int(round(th*n))
        V,idx=cheb_basis(P[:,0],P[:,1],k); Q,R=np.linalg.qr(np.sqrt(w)[:,None]*V)
        s = np.sum(Q**2,axis=1)   # = w_B K(B,B)
        bnd = (np.abs(P[:,0])>0.999)|(np.abs(P[:,1])>0.999)
        r = np.sqrt(P[:,0]**2+P[:,1]**2)
        print(weights,'n',n,'theta',th,'N_k/N %.3f'%(len(idx)/len(P)),'mean s %.3f'%s.mean(),'frac s>0.9 %.3f'%np.mean(s>0.9),'frac s>0.99 %.3f'%np.mean(s>0.99),'mean s boundary %.3f'%s[bnd].mean(),'mean s interior %.3f'%s[~bnd].mean(), 'mean s |x|<.5&|y|<.5 %.3f'%s[(np.abs(P[:,0])<.5)&(np.abs(P[:,1])<.5)].mean(), 'min s %.3f max s %.3f'%(s.min(),s.max()))
