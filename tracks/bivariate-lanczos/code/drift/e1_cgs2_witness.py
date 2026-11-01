#!/usr/bin/env python3
"""Exact formal-l-infinity sign witness at selected scalar-source nodes.

All scalar operation errors at one node align with one output column. The
full rank-one normal output is then evaluated, not merely that column.
"""
import argparse
import hashlib
import json
import time
from pathlib import Path
from e1_exact import Q, build, points, scalar


def run(source_path):
    start=time.monotonic();source=json.loads(Path(source_path).read_text())
    name,n,rule=source['set'],source['degree'],source['rule'];xy=points(name)
    coords,b,d,rec,_=build(xy,n,rule);N=len(b)
    nodes=sorted({v['witness']['node'] for v in source['metrics'].values()})
    results=[]
    for i in nodes:
        rho=[Q(0)]*N
        G=[[Q(0)]*N for _ in range(N)]
        for h in range(1,N):
            axis,parent,alpha,_=rec[h]
            partial=Q(0);rho[h]=abs(coords[axis][i]*b[parent][0,i])+3*abs(b[h][0,i])
            for l,c in enumerate(alpha):
                product=c*b[l][0,i];partial+=product;rho[h]+=abs(product)
                if l>=1:
                    rho[h]+=abs(partial)
            G[h][h]=Q(1)
            for k in range(h+1,N):
                a,p,coefficients,_=rec[k]
                G[k][h]=coords[a][i]*G[p][h]-sum((coefficients[l]*G[l][h] for l in range(h,k)),Q(0))
        Rii=1-sum((b[k][0,i]**2/d[k] for k in range(N)),Q(0))
        columns=[Rii*sum((abs(G[k][h])*rho[h] for h in range(1,k+1)),Q(0))**2/d[k] for k in range(1,N)]
        target=max(range(1,N),key=lambda k:columns[k-1])
        sign=lambda v: int(v>0)-int(v<0)
        aggregate=[rho[h]*sign(G[target][h]) for h in range(N)]
        values=[sum((G[k][h]*aggregate[h] for h in range(1,k+1)),Q(0)) for k in range(N)]
        norm=Rii*sum((values[k]**2/d[k] for k in range(1,N)),Q(0))
        assert norm>=columns[target-1]
        results.append({'node':i,'point_exact':[str(z) for z in xy[i]],'target_column':target,'normal_projector_diagonal_exact':str(Rii),'target_column_lower_squared':scalar(columns[target-1]),'rank_one_output_squared':scalar(norm),'aggregate_source_values_exact':[str(v) for v in aggregate]})
    best=max(results,key=lambda r:Q(r['rank_one_output_squared']['exact']))
    return {'status':'MEASURED exact sign witness for declared formal scalar-CGS2 graph','set':name,'degree':n,'rule':rule,'input_norm':'formal relative scalar errors l-infinity<=1','sign_rule':'At chosen node i, each local scalar operation o at source h has delta_hio=sign(g_target,h(zi)*m_hio); all errors at other nodes are zero.','lower_squared':best['rank_one_output_squared'],'selected_nodes':results,'limitation':'Formal standard model capacity only, not actual IEEE error realizability. Depends on theorem03 quotient reduction and declared dense-matvec CGS2 operation order.','elapsed_seconds':time.monotonic()-start,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scalar_source_path':str(source_path),'scalar_source_sha256':hashlib.sha256(Path(source_path).read_bytes()).hexdigest(),'aggregate_code_sha256':hashlib.sha256(Path(__file__).with_name('e1_exact.py').read_bytes()).hexdigest()}


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--scalar-source',required=True);p.add_argument('--output',required=True);a=p.parse_args()
    result=run(a.scalar_source);result['command']=' '.join(__import__('sys').argv)
    Path(a.output).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'event':'complete','lower_squared':result['lower_squared']['float'],'elapsed':result['elapsed_seconds']}))
