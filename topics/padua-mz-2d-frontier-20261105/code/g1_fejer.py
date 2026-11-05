#!/usr/bin/env python3
"""Signed-Q Rayleigh tests for prescribed tensor Fejer polynomials, floats only."""
import argparse
import hashlib
import json
from pathlib import Path
import resource
import sys
import time
import numpy as np
from scipy.special import roots_legendre
from g1_spectral import weights_dct


def fejer(angle, r):
    # np.sinc avoids the removable 0/0 at the selected endpoint.
    return (r+1)*(np.sinc((r+1)*angle/(2*np.pi))/np.sinc(angle/(2*np.pi)))**2


def mass(r, extra=0):
    x,w=roots_legendre(r+1+extra)
    f=fejer(np.arccos(x),r)
    return float(w@(f*f))


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--m',nargs='+',type=int,default=[100,400,1000,2000]);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
    report=dict(status='MEASURED',rigorous_enclosures=False,command=sys.argv,
                code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                weight_code_sha256=hashlib.sha256(Path(__file__).with_name('g1_spectral.py').read_bytes()).hexdigest(),results=[])
    for m in args.m:
        start=time.monotonic();w=weights_dct(m)
        alpha=np.pi*np.arange(m+1)/m;beta=np.pi*np.arange(m+2)/(m+1)
        for rx,ry in [(.65,.30),(.55,.40),(.75,.20)]:
            r,s=int(np.floor(rx*m)),int(np.floor(ry*m))
            fx=fejer(alpha,r);fy=fejer(beta,s)
            numerator=float((fx*fx)@w@(fy*fy))
            mx,my=mass(r),mass(s); mx2,my2=mass(r,8),mass(s,8)
            denominator=mx*my
            row=dict(m=m,r=r,s=s,total_degree=r+s,ratio=(r+s)/m,
                     requested_ratios=[rx,ry],Q_p_squared=numerator,integral_p_squared=denominator,
                     rayleigh=numerator/denominator,mass_quadrature_orders=[r+1,s+1],
                     mass_relative_refinement_error=abs(mx2*my2/denominator-1),
                     weight_sum=float(w.sum()),negative_weights_mass=float(-w[w<0].sum()),
                     seconds_since_m_start=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            report['results'].append(row);args.output.parent.mkdir(parents=True,exist_ok=True)
            args.output.write_text(json.dumps(report,indent=2)+'\n')
            print(m,r,s,row['rayleigh'],row['mass_relative_refinement_error'],flush=True)

if __name__=='__main__':main()
