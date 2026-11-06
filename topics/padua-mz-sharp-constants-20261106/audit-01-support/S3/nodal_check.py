import numpy as np, importlib.util
spec=importlib.util.spec_from_file_location('g1','/home/user/padua_research/topics/padua-mz-2d-frontier-20261105/code/g1_spectral.py');g1=importlib.util.module_from_spec(spec);spec.loader.exec_module(g1)
from lm_spectra import L_weights
def t(a): return 2. if a==0 else -4./(4*a*a-1)
for m in [4,5,6,7,10,11,40,41,200,201,1000,1001]:
    M=m+1;R=m//2
    th=np.pi*np.arange(m+1)/m; ph=np.pi*np.arange(M+1)/M
    tv=np.array([t(a) for a in range(R+1)])
    CX=np.cos(2*np.outer(np.arange(R+1),th)); CY=np.cos(2*np.outer(np.arange(R+1),ph))
    mask=(np.add.outer(np.arange(R+1),np.arange(R+1))<=R)*np.outer(tv,tv)
    S=CX.T@mask@CY
    hm=2/(1-m*m) if m%2==0 else 0.
    j=np.arange(m+1)[:,None];k=np.arange(M+1)[None,:]
    eps=np.where((j==0)|(j==m),.5,1.);eta=np.where((k==0)|(k==M),.5,1.)
    w=2*eps*eta/(m*M)*(S-2*hm*np.cos(m*th)[:,None]); w[(j+k)%2!=0]=0
    wd=g1.weights_dct(m)
    d=np.minimum(j,m-j);e=np.minimum(k,M-k);D=(1+d)*(1+e)
    err=np.abs(wd-np.log(R)*L_weights(m))
    ratio=(err/(eps*eta*D/(m*M*R*R)))[(j+k)%2==0].max()
    print(m,'formula-vs-frozen',float(np.abs(w-wd).max()),'max err/(eps eta D/(mMR^2))',round(float(ratio),3),'(proved <=134)')
