"""Reproducible bounded G2/G3/G4 finite screens. No universal extrema claims."""
import argparse, hashlib, json, os, platform, time
from pathlib import Path
import numpy as np
from evaluator import Evaluator

DEGREES=[17,18,24,25,48,49,96,97,192,199,200]

def g2(n):
    e=Evaluator(n); out=[]
    # Avoid subtracting O(10) quantities at rho=1/1024 for large n.
    radii=[1/64,1/256,1/1024] if n<=200 else [1/64,1/128]
    fs=np.linspace(0,1,9 if n<=200 else 5)
    for J,K in e.corner():
        t,p=J*np.pi/n,K*np.pi/(n+1); sx=1 if J==0 else -1; sy=1 if K==0 else -1
        lc=e.point(t,p)[0]; best=(-1e99,None); deficits=[]
        for rho in radii:
            for f in fs:
                a,b=f*rho,(1-f)*rho
                l=e.point(t+sx*a/n,p+sy*b/(n+1))[0]
                val=(l-(np.cos(a)+np.cos(b))*lc/2)/(rho*rho*np.log(n+1))
                if val>best[0]: best=(val,[rho,float(f)])
                deficits.append(lc-l)
        # Sampled validity is a censored local radial screen, not largest radius.
        validity=[]
        for f in [0.,.5,1.]:
            gaps=[lc-e.point(t+sx*f*r/n,p+sy*(1-f)*r/(n+1))[0] for r in [.03125,.0625,.125,.25,.5,1.,2.,np.pi]]
            validity.append({'fraction':f,'minimum_sampled_gap':min(gaps),'all_strict_to_pi':min(gaps)>0})
        out.append({'corner':[J,K],'Lc':lc,'K_sample_max':best[0],'arg':best[1], 'axis_budget':lc/(4*np.log(n+1)), 'minimum_gap_local':min(deficits),'validity':validity})
    return {'n':n,'radii':radii,'direction_count':len(fs),'corners':out}

def g3(n):
    e=Evaluator(n); J,K=e.corner()[0]; t,p=J*np.pi/n,K*np.pi/(n+1); lc=e.point(t,p)[0]
    # Original 61x61 pilot grid retained for comparable far-margin samples.
    count=61
    points={(float(a),float(b)) for a in np.linspace(-np.pi,np.pi,count) for b in np.linspace(-np.pi,np.pi,count) if abs(a)+abs(b)<=np.pi+1e-12}
    points.update([(np.pi/2,-np.pi/2),(-np.pi/2,np.pi/2),(0.,0.)])
    vals=[]
    for a,b in sorted(points):
        s=e.point(t+a/n,p+b/(n+1))[1]
        vals.append((a,b,s-lc,(s-(np.cos(a)+np.cos(b))*lc/2)/np.log(n+1)))
    best=max(vals,key=lambda x:x[3]); margins={str(r):-max(x[2] for x in vals if abs(x[0])+abs(x[1])>=r) for r in [.125,.25,.5,1.]}
    return {'n':n,'grid_count_axis':count,'points':len(vals),'C_sample_max':best[3],'arg':best[:2],'max_S_minus_Lc':max(x[2] for x in vals),'far_margin':margins}

def g4(n):
    e=Evaluator(n); lc=e.point(*[v*np.pi/d for v,d in zip(e.corner()[0],(n,n+1))])[0]
    # All physical edge odd centers, first-four-strip classes at 7 representative
    # macroscopic positions, 7x7 representative interior positions. Every odd
    # coset is sampled for n<=25. Perturbations cover both phase signs and axes.
    if n<=25: centers={(j,k) for j in range(n+1) for k in range(n+2) if (j+k)%2}
    else:
        jj=sorted(set([0,1,2,3,4,n-4,n-3,n-2,n-1,n]+[round(n*f) for f in [.1,.25,.5,.75,.9]]))
        kk=sorted(set([0,1,2,3,4,n-3,n-2,n-1,n,n+1]+[round((n+1)*f) for f in [.1,.25,.5,.75,.9]]))
        centers={(j,k) for j in jj for k in kk if (j+k)%2}
        # Avoid parity holes when rounded macroscopic fractions all land even.
        for f in [.1,.25,.5,.75,.9]:
            for h in [.1,.25,.5,.75,.9]:
                j,k=round(n*f),round((n+1)*h)
                if (j+k)%2==0: k+=1
                centers.add((j,k))
        centers.update((j,k) for j in (0,n) for k in range(n+2) if (j+k)%2)
        centers.update((j,k) for k in (0,n+1) for j in range(n+1) if (j+k)%2)
    centers-=set(e.corner())
    groups={}; total=0
    phases=[(0.,0.),(1/64,0.),(-1/64,0.),(0.,1/64),(0.,-1/64),(1/128,1/128),(-1/128,-1/128),(1/128,-1/128),(-1/128,1/128)]
    for j,k in sorted(centers):
        dj=min(j,n-j); dk=min(k,n+1-k)
        cls='edge' if min(dj,dk)==0 else ('strip_1_4' if min(dj,dk)<=4 else 'interior')
        # Retain directional distinction in records.
        cls+= '_vertical' if dj<dk else ('_horizontal' if dk<dj else '_diagonal')
        rec=groups.setdefault(cls,{'centers':0,'samples':0,'min_gap':1e99,'min_Delta':1e99})
        rec['centers']+=1
        for a,b in phases:
            if not (0<=j*np.pi+a<=n*np.pi and 0<=k*np.pi+b<=(n+1)*np.pi): continue
            l,s=e.point((j*np.pi+a)/n,(k*np.pi+b)/(n+1)); gap=lc-l; delta=s-l
            rec['samples']+=1; total+=1
            if gap<rec['min_gap']: rec['min_gap']=gap;rec['gap_arg']=[j,k,a,b]
            if delta<rec['min_Delta']: rec['min_Delta']=delta;rec['Delta_arg']=[j,k,a,b]
    return {'n':n,'centers':len(centers),'samples':total,'all_centers':n<=25,'classes':groups}

def main():
    p=argparse.ArgumentParser();p.add_argument('gate',choices=['g2','g3','g4']);p.add_argument('--output',required=True);args=p.parse_args()
    degrees=DEGREES+([255,256,511,512,999,1000] if args.gate=='g2' else [])
    result={'gate':args.gate,'status':'MEASURED','python':platform.python_version(),'numpy':np.__version__,'rows':[]}
    start=time.monotonic()
    for n in degrees:
        t=time.monotonic(); row=globals()[args.gate](n);row['seconds']=time.monotonic()-t
        result['rows'].append(row); result['seconds']=time.monotonic()-start
        Path(args.output).write_text(json.dumps(result,indent=2)+'\n');print(args.gate,n,row['seconds'],flush=True)
if __name__=='__main__':main()
