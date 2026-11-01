"""Cross-check of the rhombus Dirichlet L1 norm: brute-force lattice sum vs product identity vs the gen4_tests16 formula.
Model run: claude-fable-5-1 (adversary gen4-2), 2026-11-01. MEASURED."""
import numpy as np, sys
sys.path.insert(0,'/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/adv/gen4-2')
from adv_rhombus_L1 import rhombus_L1, dirichlet
def brute(n, M):
    th=(np.arange(M)+0.5)*2*np.pi/M
    TH,PH=np.meshgrid(th,th,indexing='ij')
    D=np.zeros_like(TH)
    for i in range(-n,n+1):
        for j in range(-n,n+1):
            if abs(i)+abs(j)<=n: D+=np.cos(i*TH+j*PH)
    return np.mean(np.abs(D))
def gen4_formula(n, M=None):
    M = M or 8*n+9
    th=(np.arange(M)+0.5)*2*np.pi/M; J=np.arange(-n,n+1)
    E=np.exp(1j*np.outer(th,J)); ph=th
    Dk=np.array([np.sum(np.cos(np.outer(ph,np.arange(1,k+1))),axis=1)*2+1 if k>0 else np.ones(M) for k in range(n+1)])
    D=E@Dk[np.abs(J)]
    return np.mean(np.abs(D))
for n in (3,5,10,20):
    M=16*n+8
    print('n',n,'brute(M=%d) %.5f'%(M,brute(n,M)),'product-identity %.5f'%rhombus_L1(n,M),'gen4_tests16 formula (same M) %.5f'%gen4_formula(n,M),'gen4 default M=8n+9: %.5f'%gen4_formula(n))
