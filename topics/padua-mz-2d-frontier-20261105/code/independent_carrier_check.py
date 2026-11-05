#!/usr/bin/env python3
"""Exact finite Fourier/DCT carrier identities, plus measured fixed-node slopes."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,sys,time,platform
import numpy as np

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def conv(a,b):
    out={}
    for i,x in a.items():
        for j,y in b.items():out[i+j]=out.get(i+j,F(0))+x*y
    return {k:v for k,v in out.items() if v}
def mean(c,m,alternating=False):
    target=m if alternating else 0
    return sum(v for k,v in c.items() if k%(2*m)==target)
def fixed_weight(m,j,k):
    R=m//2;a=np.arange(R+1);t=np.empty(R+1)
    t[0]=2;t[1:]=-4/(4*a[1:]**2-1)
    xs=t*np.cos(2*a*j*np.pi/m)
    ys=t*np.cos(2*a*k*np.pi/(m+1))
    triangular=xs@np.cumsum(ys)[::-1]
    d=triangular-4/(1-m*m)*((-1)**j)
    eps=.5 if j==0 or j==m else 1.
    eta=.5 if k==0 or k==m+1 else 1.
    return 2*eps*eta*d/(m*(m+1))
def main():
    tick=time.monotonic();count=0
    for m in range(8,65,2):
        for r in range(1,(m-1)//4+1):
            f={l:1-F(abs(l),r+1) for l in range(-r,r+1)}
            f2=conv(f,f)
            c0=F(2*r*r+4*r+3,3*(r+1))
            assert f2[0]==c0 and f2[2*r]==F(1,(r+1)**2)
            neg=conv(f,{m//2:F(1,2),-m//2:F(1,2)})
            # sin(m*t/2) sin(r*t)=(cos((m/2-r)t)-cos((m/2+r)t))/2.
            carrier={m//2-r:F(1,4),-m//2+r:F(1,4),m//2+r:F(-1,4),-m//2-r:F(-1,4)}
            pos=conv(f,carrier)
            neg2=conv(neg,neg);pos2=conv(pos,pos)
            h0=c0/2-F(1,2*(r+1)**2)
            assert mean(neg2,m)==c0/2 and mean(neg2,m,True)==c0/2
            assert mean(pos2,m)==h0/2 and mean(pos2,m,True)==-h0/2
            assert mean(f2,m+1,True)==0
            count+=1
    rows=[]
    for j,k in [(0,0),(0,2),(1,1),(2,0),(2,2),(3,1),(4,0)]:
        values=[(m,m**4*fixed_weight(m,j,k)) for m in [128,256,512,1024,2048,4096,8192]]
        target=-16*(.5 if j==0 else 1)*(.5 if k==0 else 1)*(-1)**j
        slopes=[(values[i][1]-values[i-1][1])/np.log(2) for i in range(1,len(values))]
        rows.append({'j':j,'k':k,'predicted_log_coefficient':target,'m4_weight':values,'doubling_slopes_float':slopes})
    root=Path(__file__).resolve().parents[3];topic=Path(__file__).resolve().parent.parent
    inputs=[Path(__file__).resolve(),topic/'theory/f12-local-weight-asymptotic.md']
    out={'pass':True,'status':'Exact finite carrier regression; separate MEASURED fixed-node slope probes',
        'rules_input_sha':'83cf6f1ee244f2e72057332a7ec04ee74db1f0de',
        'command':sys.argv,'python':sys.version,'numpy':np.__version__,'platform':platform.platform(),
        'inputs':{str(p.relative_to(root)):sha(p) for p in inputs},
        'exact_scope':'even m=8..64; every integer 1<=r with 4r<m','exact_cases':count,
        'measured_fixed_node_scope':rows,'seconds':time.monotonic()-tick}
    Path(sys.argv[1]).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'pass':True,'exact_cases':count,'seconds':out['seconds'],'last_slopes':[(x['j'],x['k'],x['doubling_slopes_float'][-1]) for x in rows]}))
if __name__=='__main__':main()
