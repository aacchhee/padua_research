"""Smooth-target companion to E6 post-hoc adversarial polynomial benchmark."""
import argparse,json,pathlib
import numpy as np
from e6_benchmark import load_upstream,L2

def main():
    p=argparse.ArgumentParser();p.add_argument('--external',default='/workspace/padua-drift-external/polyrat');p.add_argument('--output',required=True);a=p.parse_args();up=load_upstream(a.external)
    result={'status':'MEASURED','target':'exp(x+y), independently fixed analytic target','cases':[]}
    for name in L2.BENCH:
        P,w,n=L2.benchmark(name);test=(P[:128]+P[-128:])/2
        target=np.exp(P.sum(axis=1))*np.sqrt(w);truth=np.exp(test.sum(axis=1));out={'name':name,'n':n,'methods':{}}
        for label,order in [('upstream_xy',[0,1]),('upstream_yx',[1,0])]:
            Q,H,idx=up.vandermonde_arnoldi_CGS(P[:,order],n,weight=np.sqrt(w))
            c=np.linalg.lstsq(Q,target,rcond=None)[0]
            pred=up.vandermonde_arnoldi_eval(test[:,order],H,idx)@c
            out['methods'][label]={'weighted_training_relative_residual':float(np.linalg.norm(Q@c-target)/np.linalg.norm(target)), 'test_relative_error':float(np.linalg.norm(pred-truth)/np.linalg.norm(truth))}
        result['cases'].append(out)
        pathlib.Path(a.output).write_text(json.dumps(result,indent=2)+'\n')
        print(name,out['methods'],flush=True)
if __name__=='__main__':main()
