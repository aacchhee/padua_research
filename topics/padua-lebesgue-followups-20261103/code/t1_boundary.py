"""Frozen N8 edge predicates with native exact corner sums and edge checkpoints.

The frozen source is never modified. The edge-loop AST is copied verbatim, with
one persistence callback inserted after each finished edge. Corner evaluation
uses the same all-active strict inward tests, evaluating native ANP coefficients.
"""
if not __debug__:
    raise RuntimeError('T1 boundary producer refuses optimized Python')
import argparse, ast, hashlib, json, os, sys, tempfile, time
from pathlib import Path
FROZEN = Path(__file__).resolve().parents[2] / 'padua-proof-attempts-2-20261101' / 'code'
sys.path.insert(0,str(FROZEN))
import a5_n8_boundary as old
BASE_SHA='6088db34cce2952332bd22e560c8b02e90446236f994dc2bac79b33717e769cb'

def atomic(path,value):
    path=Path(path); data=json.dumps(value,separators=(',',':'),sort_keys=True).encode()
    with tempfile.NamedTemporaryFile(dir=path.parent,prefix=path.name+'.',delete=False) as f:
        name=f.name; f.write(data); f.flush(); os.fsync(f.fileno())
    os.replace(name,path)

def native_at(p,u,v):
    return sum((c*u**i*v**j for(i,j),c in p.rep.to_dict().items()),old.K.zero)

def corners_native(L):
    corners=[]; cid=0; unresolved=[]
    derivatives=[(p.diff(old.x),p.diff(old.y))for p in L]
    for u,v in((-1,-1),(-1,1),(1,-1),(1,1)):
        vals=[native_at(p,u,v)for p in L]; row={'point':[u,v]}
        if vals.count(old.K.one)==1 and vals.count(old.K.zero)==44:
            row['kind']='node'
        else:
            zeros=[i for i,c in enumerate(vals)if c==old.K.zero]
            sg=[1 if old.ksign(c)>0 else -1 for c in vals]; ok=True
            du=[-u*native_at(p,u,v)for p,q in derivatives]
            dv=[-v*native_at(q,u,v)for p,q in derivatives]
            for bits in range(1<<len(zeros)):
                signsv=sg[:]
                for j,b in enumerate(zeros):signsv[b]=1 if bits>>j&1 else -1
                inward=[sum((signsv[i]*d[i]for i in range(45)),old.K.zero)for d in(du,dv)]
                if any(old.ksign(d)>=0 for d in inward):ok=False
            row['zeros']=zeros
            if ok:row.update(kind='max',id=cid);cid+=1
            else:row['kind']='unresolved';unresolved.append(row)
        corners.append(row)
    return corners,cid,unresolved

def build(checkpoint):
    raw=Path(old.__file__).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==BASE_SHA
    module=ast.parse(raw); source=next(n for n in module.body if isinstance(n,ast.FunctionDef)and n.name=='boundaries')
    body=source.body; start=next(i for i,n in enumerate(body)if isinstance(n,ast.Assign)and any(isinstance(t,ast.Name)and t.id=='corners'for t in n.targets))
    # Keep the frozen construction and entire edge loop; omit its slow corners.
    edge_loop=next(n for n in body[:start]if isinstance(n,ast.For))
    frozen_ast=ast.dump(edge_loop,include_attributes=False)
    callback=ast.parse('checkpoint(edges,dict(stats),list(unresolved),eid,time.time()-t0)').body[0]
    edge_loop.body.append(callback)
    assert ast.dump(ast.For(target=edge_loop.target,iter=edge_loop.iter,body=edge_loop.body[:-1],orelse=edge_loop.orelse,type_comment=None),include_attributes=False)==frozen_ast
    tail=ast.parse('corners,cid,cu=corners_native(L)\nunresolved.extend(cu)\nreturn edges,corners,{"edge":eid,"corner":cid,"counts":dict(stats),"unresolved":len(unresolved),"complete":edge_limit==4 and not unresolved,"seconds":time.time()-t0},unresolved').body
    source.body=body[:start]+tail
    namespace=dict(vars(old));namespace.update(checkpoint=checkpoint,corners_native=corners_native)
    exec(compile(ast.fix_missing_locations(ast.Module(body=[source],type_ignores=[])),'<frozen-n8-edges/native-corners>','exec'),namespace)
    return namespace['boundaries']

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True);parser.add_argument('--edge-limit',type=int,choices=range(1,5),default=4)
    args=parser.parse_args(); own=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    def checkpoint(edges,stats,unresolved,eid,seconds):
        atomic(args.output+'.edges-checkpoint.json',dict(edges=edges,stats=stats,unresolved=unresolved,edge=eid,seconds=seconds,complete=False,source_sha256=own,frozen_boundary_sha256=BASE_SHA))
    edges,corners,summary,unresolved=build(checkpoint)(edge_limit=args.edge_limit)
    assert hashlib.sha256(Path(old.__file__).read_bytes()).hexdigest()==BASE_SHA
    assert hashlib.sha256(Path(__file__).read_bytes()).hexdigest()==own
    atomic(args.output,dict(edges=edges,corners=corners,summary=summary,unresolved=unresolved,metadata=dict(source_sha256=own,frozen_boundary_sha256=BASE_SHA)))
    print(json.dumps(summary),flush=True)
if __name__=='__main__':main()
