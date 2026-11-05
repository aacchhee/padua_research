#!/usr/bin/env python3
"""Even-m carrier-times-Fejer finite floating probe requested after original gates."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import time
import numpy as np
from scipy.special import roots_legendre
from g1_spectral import weights_dct
from g1_fejer import fejer,mass


def xmass(m,b,r,extra):
    order=m//2+b+r+1+extra;x,w=roots_legendre(order);angle=np.arccos(x)
    v=np.sin(m*angle/2)*np.sin(b*angle)*fejer(angle,r)
    return float(w@(v*v))


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--m',type=int,nargs='+',default=[100,400,1000,2000]);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
    out=dict(status='MEASURED',rigorous_enclosures=False,command=sys.argv,
        code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),results=[])
    for m in args.m:
        assert m%2==0;tick=time.monotonic();b=int(.10*m);r=s=int(.15*m)
        w=weights_dct(m);alpha=np.pi*np.arange(m+1)/m;beta=np.pi*np.arange(m+2)/(m+1)
        # sin(j*pi/2)^2 is exactly zero on even j, exactly one on odd j.
        fx2=(np.arange(m+1)%2)*np.sin(b*alpha)**2*fejer(alpha,r)**2
        fy2=fejer(beta,s)**2;q=float(fx2@w@fy2)
        den=xmass(m,b,r,0)*mass(s);den2=xmass(m,b,r,8)*mass(s,8)
        nodes=[]
        for j,k in [(0,0),(0,2),(1,1),(1,3),(2,0),(2,2),(3,1),(3,3)]:
            eps=.5 if j==0 else 1.;eta=.5 if k==0 else 1.
            nodes.append(dict(j=j,k=k,weight=float(w[j,k]),m4w_over_log=float(m**4*w[j,k]/np.log(m)),
                proposed_limit=-16*eps*eta*(-1)**j))
        row=dict(m=m,b=b,r=r,s=s,total_degree=m//2+b+r+s,Q_p_squared=q,
            integral_p_squared=den,rayleigh=q/den,mass_relative_refinement_error=abs(den2/den-1),
            proposed_log_scaled_rayleigh=q/den/np.log(m),nodes=nodes,seconds=time.monotonic()-tick)
        out['results'].append(row);args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n')
        print(m,row['rayleigh'],row['mass_relative_refinement_error'],flush=True)

if __name__=='__main__':main()
