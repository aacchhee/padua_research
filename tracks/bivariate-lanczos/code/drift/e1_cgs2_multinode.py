#!/usr/bin/env python3
"""Exact many-node formal scalar-error sign witness for one output column.

The initial target is selected by the prior one-node witness. At every node
all scalar errors align to this column. Greedy node signs keep each newly
fixed off-diagonal term nonnegative, so their normal-column norm is at least
the independent random-sign expected squared norm.
"""
import argparse
import hashlib
import json
import time
from pathlib import Path
from e1_exact import Q, Mat, build, multiply, points, scalar


def run(witness_path):
    start=time.monotonic();prior=json.loads(Path(witness_path).read_text())
    name,n,rule=prior['set'],prior['degree'],prior['rule'];xy=points(name)
    coords,b,d,rec,_=build(xy,n,rule);M,N=len(xy),len(b)
    selected=max(prior['selected_nodes'],key=lambda r:Q(r['rank_one_output_squared']['exact']))
    target=selected['target_column'];capacity=[Q(0)]*M
    for h in range(1,target+1):
        axis,parent,alpha,_=rec[h];u=multiply(b[parent],coords[axis])
        rho=[]
        for i in range(M):
            val=abs(u[0,i])+3*abs(b[h][0,i]);partial=Q(0)
            for l,c in enumerate(alpha):
                term=c*b[l][0,i];val+=abs(term);partial+=term
                if l>=1:val+=abs(partial)
            rho.append(val)
        g=[None]*(target+1);g[h]=Mat([[1]*M])
        for k in range(h+1,target+1):
            a,p,coefficients,_=rec[k]
            v=multiply(g[p],coords[a]) if p>=h else Mat(1,M)
            for l in range(h,k):
                if coefficients[l]:v=v-coefficients[l]*g[l]
            g[k]=v
        for i in range(M):capacity[i]+=abs(g[target][0,i])*rho[i]
        print(json.dumps({'event':'capacity_source','source':h,'target':target,'elapsed':time.monotonic()-start}),flush=True)
    diagonal=[1-sum((b[l][0,i]**2/d[l] for l in range(N)),Q(0)) for i in range(M)]
    expected=sum((diagonal[i]*capacity[i]**2 for i in range(M)),Q(0))/d[target]
    c=[Q(0)]*N;signs=[]
    for i in range(M):
        score=-sum((b[l][0,i]*c[l]/d[l] for l in range(N)),Q(0))
        sign=1 if score>=0 else -1;signs.append(sign)
        for l in range(N):c[l]+=b[l][0,i]*capacity[i]*sign
    exact=(sum((v*v for v in capacity),Q(0))-sum((v*v/dl for v,dl in zip(c,d)),Q(0)))/d[target]
    assert exact>=expected>=0
    return {'status':'MEASURED exact explicit formal scalar-CGS2 many-node witness','set':name,'degree':n,'rule':rule,'target_column':target,'expected_random_sign_lower_squared':scalar(expected),'explicit_greedy_sign_lower_squared':scalar(exact),'input_norm':'all formal relative scalar errors l-infinity<=1','operation_sign_rule':'delta_hio = node_sign_i * sign(g_target,h(zi)*m_hio), all h<=target; other errors0','node_signs':signs,'target_capacity_exact':[str(v) for v in capacity],'greedy_rule':'node order0..M-1; c_l=sum_previous b_l(i)S_i sign_i; sign_i=sign(-sum_l b_l(i)c_l/dl), zero chooses+1','limitation':'Declared dense-matvec CGS2 formal standard-model capacity, not actualIEEE realizability. A lower bound only; no exact operator norm claimed.','elapsed_seconds':time.monotonic()-start,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'prior_witness_path':str(witness_path),'prior_witness_sha256':hashlib.sha256(Path(witness_path).read_bytes()).hexdigest(),'aggregate_code_sha256':hashlib.sha256(Path(__file__).with_name('e1_exact.py').read_bytes()).hexdigest()}


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--witness',required=True);p.add_argument('--output',required=True);a=p.parse_args()
    result=run(a.witness);result['command']=' '.join(__import__('sys').argv)
    Path(a.output).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'event':'complete','lower_squared':result['explicit_greedy_sign_lower_squared']['float'],'elapsed':result['elapsed_seconds']}))
