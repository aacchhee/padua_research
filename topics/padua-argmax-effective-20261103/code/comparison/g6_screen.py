"""Finite floating G6 E-C and I-B0 screens. No certificates or universal claims."""
import argparse, hashlib, json, platform, sys, time
from pathlib import Path
import numpy as np
import scipy
from scipy.optimize import minimize, minimize_scalar
SOURCE=Path(__file__).resolve().parents[3]/'padua-argmax-alln-20261101'/'code'/'part3'
sys.path.insert(0,str(SOURCE))
from tests_common import Eval, Edge, validate

def edge_max(e,name,k):
    n=e.n; ts=np.linspace((k-1)*np.pi/(n+1),(k+1)*np.pi/(n+1),65)
    ys=np.array([e.one(name,t) for t in ts]); candidates=[(float(ys[0]),float(ts[0])),(float(ys[-1]),float(ts[-1]))]
    for i in range(1,64):
        if ys[i]>=ys[i-1] and ys[i]>=ys[i+1]:
            r=minimize_scalar(lambda t:-e.one(name,t),bounds=(ts[i-1],ts[i+1]),method='bounded',options={'xatol':1e-13})
            candidates.extend([(float(ys[i]),float(ts[i])),(-float(r.fun),float(r.x))])
    val,arg=max(candidates)
    return val,arg*(n+1)/np.pi,len(candidates)

def rectangle(e,j,k,edge_value,edge_arg):
    n=e.n; bounds=[(0.,1.) if j==0 else (n-1.,float(n)),(k-1.,k+1.)]
    def f(z):return -e.one(z[0]*np.pi/n,z[1]*np.pi/(n+1))[0]
    grid=[np.array([u,v]) for u in np.linspace(*bounds[0],9) for v in np.linspace(*bounds[1],17)]
    vals=sorted([(f(z),z) for z in grid],key=lambda z:z[0]);best=(-edge_value,np.array([j,edge_arg])); successes=[]
    # Best three distinct grid points and the optimized edge point.
    starts=[z for _,z in vals[:3]]+[np.array([float(j),edge_arg])]
    for x,z in vals[:1]:
        if x<best[0]:best=(x,z)
    for z in starts:
        r=minimize(f,z,method='Nelder-Mead',bounds=bounds,options={'maxiter':180,'xatol':1e-8,'fatol':1e-10})
        successes.append(bool(r.success))
        if r.fun<best[0]:best=(float(r.fun),r.x)
    return {'value':-best[0],'arg':best[1].tolist(),'excess':-best[0]-edge_value,'optimizer_success':successes}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--degrees',type=int,nargs='*',default=list(range(13,61)));ap.add_argument('--ib-degrees',type=int,nargs='*',default=[13,17,24,32,48,60]);ap.add_argument('--output',required=True);a=ap.parse_args()
    start=time.monotonic(); result={'status':'MEASURED','python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'validation':validate(),'invocation':sys.argv,'source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),SOURCE/'tests_common.py',SOURCE.parent/'maj.py']},'rows':[]}
    for n in a.degrees:
        t=time.monotonic();edge=Edge(n);ev=Eval(n) if n in a.ib_degrees else None; comps=[]; ib=[]
        for j,name in [(0,'v+'),(n,'v-')]:
            centers=[k for k in range(2,n) if (j+k)%2];vs={k:edge_max(edge,name,k) for k in centers}
            for k in centers:
                kk=k+2 if k<(n+1)/2 else k-2
                if kk in vs and abs(kk-(n+1)/2)<abs(k-(n+1)/2):
                    comps.append({'edge':name,'source':k,'target':kk,'difference':vs[kk][0]-vs[k][0],'source_value':vs[k][0],'source_arg':vs[k][1],'target_value':vs[kk][0],'target_arg':vs[kk][1]})
                if ev is not None:
                    r=rectangle(ev,j,k,vs[k][0],vs[k][1]);r.update({'edge':name,'center':k,'edge_value':vs[k][0],'edge_arg':vs[k][1]});ib.append(r)
        row={'n':n,'E_C_comparisons':comps,'I_B_rectangles':ib,'E_C_count':len(comps),'E_C_min_difference':min((r['difference'] for r in comps),default=None),'E_C_reversals':[r for r in comps if r['difference']< -1e-6],'I_B_count':len(ib),'I_B_max_excess':max((r['excess'] for r in ib),default=None),'I_B_reversals':[r for r in ib if r['excess']>1e-6],'I_B_optimizer_failed_count':sum(not all(r['optimizer_success']) for r in ib),'seconds':time.monotonic()-t}
        result['rows'].append(row);result['seconds']=time.monotonic()-start
        Path(a.output).write_text(json.dumps(result,indent=2)+'\n');print(n,row['seconds'],row['E_C_min_difference'],row['I_B_max_excess'],flush=True)
if __name__=='__main__':main()
