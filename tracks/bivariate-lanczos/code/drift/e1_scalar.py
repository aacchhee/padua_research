#!/usr/bin/env python3
"""Exact sensitivity for two declared scalar-operation source families.

Each coordinate-product source is u_k(i)*delta_ki; each normalization-division
source is b_k(i)*epsilon_ki. Relative source parameters have joint unit l2
norm. These are SUBSET maps, NOT full implementation rounding maps. Their
lower bounds embed in any implementation admitting these scalar operations;
their upper bounds apply only to the declared source subset.
"""
import argparse
import hashlib
import json
import platform
import time
from pathlib import Path
import flint
from e1_exact import Q, Mat, build, dot, multiply, points, scalar


def run(name,degree,rule):
    start=time.monotonic();xy=points(name)
    coords,b,d,rec,metadata=build(xy,degree,rule)
    M,N=len(xy),len(b)
    R=[1-sum((v[0,i]**2/dk for v,dk in zip(b,d)),Q(0)) for i in range(M)]
    names=['coordinate_product','normalization_division','joint_subset']
    metrics={name:{'lower':Q(0),'HS':Q(0),'row':[Q(0)]*M,'witness':None,'active':0} for name in names}
    for source in range(1,N):
        axis,parent,_,_=rec[source]
        u=multiply(b[parent],coords[axis])
        g=[None]*N;g[source]=Mat([[1]*M]);energy=[Q(1)/d[source]]*M
        for k in range(source+1,N):
            a,p,alpha,_=rec[k]
            v=multiply(g[p],coords[a]) if p>=source else Mat(1,M)
            for l in range(source,k):
                if alpha[l]:
                    v=v-alpha[l]*g[l]
            g[k]=v
            for i in range(M):
                energy[i]+=v[0,i]**2/d[k]
        for i in range(M):
            for label,amplitude in [('coordinate_product',u[0,i]),('normalization_division',b[source][0,i])]:
                raw=amplitude**2*energy[i];term=R[i]*raw
                for target in [label,'joint_subset']:
                    m=metrics[target];m['HS']+=term;m['row'][i]+=raw;m['active']+=int(bool(amplitude))
                    if term>m['lower']:
                        m['lower']=term;m['witness']={'operation':label,'source':source,'degree_index':metadata[source],'node':i,'amplitude_exact':str(amplitude),'point_exact':[str(z) for z in xy[i]]}
        print(json.dumps({'event':'scalar_source','source':source,'elapsed':time.monotonic()-start}),flush=True)
    out={}
    for label,m in metrics.items():
        upper=min(m['HS'],max(m['row']))
        out[label]={'Knode_squared':scalar(m['lower']),'KHS_squared':scalar(m['HS']),'Urow_squared':scalar(max(m['row'])),'upper_squared':scalar(upper),'witness':m['witness'],'active_scalar_parameters':m['active'],'standard_linf_lower_squared':scalar(m['lower']),'standard_linf_coarse_upper_squared':scalar(m['active']*upper)}
    return {'status':'MEASURED exact scalar subset map; full implementation derivative OPEN','set':name,'degree':degree,'rule':rule,'source_count_each_family':N-1,'parameter_norm':'sum_ki delta_ki^2+epsilon_ki^2=1 for joint subset; one family for separate maps','output_norm':'spectral norm of orthonormal-basis final normal derivative','operation_interpretation':'coordinate product fl(a*qparent); normalization division fl(residual/beta), relative output errors with monic amplitudes A*bparent and b_k, respectively. Coefficients and norms differentiate but their normal contributions vanish under the aggregate-map reduction. No complete CGS2 arithmetic graph asserted.','limitation':'Upper certificates apply only to the stated subset and cannot compare full per-operation susceptibility across rules. Scalar lower witnesses may embed in a wider implementation model after its operation graph is fixed.','metrics':out,'elapsed_seconds':time.monotonic()-start,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'aggregate_code_sha256':hashlib.sha256(Path(__file__).with_name('e1_exact.py').read_bytes()).hexdigest(),'python':platform.python_version(),'python_flint':flint.__version__}


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--set',choices=['triangle','rotated'],required=True);p.add_argument('--degree',type=int,required=True);p.add_argument('--rule',choices=['bj','mirror','alt','pivot'],required=True);p.add_argument('--output',required=True);a=p.parse_args()
    result=run(a.set,a.degree,a.rule);result['command']=' '.join(__import__('sys').argv)
    Path(a.output).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'event':'complete','elapsed':result['elapsed_seconds']}))
