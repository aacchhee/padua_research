#!/usr/bin/env python3
"""Frozen exact-cardinality cyclic cosine families. No inherited file mutations."""
import hashlib,itertools as it,json,math,platform,sys,time
from pathlib import Path
import numpy as np
import scipy,scipy.linalg as la
import sympy as sp
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'tracks/lattice-unisolvence/code'))
import c3_lebesgue as leb
import c3_rank as rk
TOP=ROOT/'topics/padua-3d-20261106'

def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def generator(name,n):
    return {'K':(1,n+1,(n+1)**2),'T':(1,n+1,(n+1)*(n+2)//2),'O':(1,2*n+1,2*n*n+2*n+1)}[name]
def dictionary(n,z):
    modes=rk.exponents(n); N=len(modes); M=2*N-1
    D=np.zeros((N,N),dtype=np.int64)
    for j,a in enumerate(modes):
        for signs in it.product([-1,1],repeat=3):
            r=sum(e*b*c for e,b,c in zip(signs,a,z))%M
            D[min(r,M-r),j]+=1
    return D

def root_check(n,z,D):
    N=len(D); M=2*N-1; p=M+1
    while p==2 or not sp.isprime(p): p+=M
    g=int(sp.primitive_root(p)); omega=pow(g,(p-1)//M,p)
    assert pow(omega,M,p)==1
    assert all(pow(omega,M//q,p)!=1 for q in sp.factorint(M))
    inv2=pow(2,-1,p); inv8=pow(8,-1,p)
    C=[[((pow(omega,k*r,p)+pow(omega,-k*r,p))*inv2)%p for r in range(N)] for k in range(N)]
    axes=[[(pow(omega,k*s,p)+pow(omega,-k*s,p))*inv2%p for s in z] for k in range(N)]
    def cheb(x,a):
        if a==0:return 1
        old,new=1,x
        for _ in range(1,a):old,new=new,(2*x*new-old)%p
        return new
    V=[[math.prod(cheb(x,a) for x,a in zip(pt,mode))%p for mode in rk.exponents(n)] for pt in axes]
    expected=np.array(C,dtype=np.int64)@D%p*inv8%p
    assert np.array_equal(expected,np.array(V))
    vr,vd=rk.rank_det(V,p)
    return {'prime':int(p),'primitive_root':g,'omega':omega,'order':M,'dictionary_identity':True,'direct_rank':vr,'direct_det':vd}

def controls(n,mesh,E):
    axis=leb.discrete_leja(leb.lobatto(n+1))
    lower=np.array([[axis[i],axis[j],axis[k]] for i,j,k in rk.exponents(n)])
    cand=np.array(list(it.product(leb.lobatto(2*n+1),repeat=3)))
    _,_,perm=la.qr(leb.basis(cand,n).T,pivoting=True,mode='economic')
    return {name:leb.diagnose(pts,n,mesh,E)['sampled_lebesgue'] for name,pts in [('Leja',lower),('QR',cand[perm[:len(lower)]]) ]}

def main():
    start=time.time(); mesh=np.array(list(it.product(leb.lobatto(21),repeat=3))); cache={}
    out={'schema':'t2-cyclic-screen-v1','rules_sha':'ccd9e905d19c0c625c196c4a3f3e707058ed042a','command':'OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/t2_screen.py','source_sha256':sha(__file__),'preregistration_sha256':sha(TOP/'preregistration-T2.md'),'inherited_sha256':{f:sha(ROOT/'tracks/lattice-unisolvence/code'/f) for f in ['c3_lebesgue.py','c3_rank.py']},'versions':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'sympy':sp.__version__},'mesh':{'axis_points':21,'total':len(mesh)},'families':[]}
    for name in ['K','T','O']:
        rows=[]; losses=0; killed=None
        for n in range(1,13):
            z=generator(name,n); D=dictionary(n,z); N=len(D); M=2*N-1
            assert len({min(k%M,(-k)%M) for k in range(N)})==N
            rank,det=rk.rank_det(D.tolist(),1000003)
            row={'n':n,'N':N,'M':M,'z':list(z),'cardinality_exact':N,'dictionary_sha256':hashlib.sha256(D.tobytes()).hexdigest(),'prime':1000003,'rank_mod_p':rank,'det_mod_p':det}
            if n<=4:row['root_check']=root_check(n,z,D)
            if rank<N:
                null=sp.Matrix(D.tolist()).nullspace()
                if null:
                    v=null[0]; den=sp.ilcm(*[x.q for x in v]); v=[int(x*den) for x in v]; divisor=math.gcd(*v); v=[x//divisor for x in v]
                    assert all(x==0 for x in sp.Matrix(D.tolist())*sp.Matrix(v))
                    row['rational_nullvector']=[[list(a),c] for a,c in zip(rk.exponents(n),v) if c]
                    row['nullvector_checked_exact']=True; killed='certified_dictionary_deficiency';rows.append(row);break
                row['rational_nullspace_empty']=True
            points=np.cos(2*np.pi*np.arange(N)[:,None]*np.array(z)[None,:]/M)
            if n not in cache:
                E=leb.basis(mesh,n); cache[n]=(E,controls(n,mesh,E))
            E,base=cache[n]; row['baselines']=base;row['quality']=leb.diagnose(points,n,mesh,E)
            value=row['quality']['sampled_lebesgue']
            if n>=6 and value is not None and value>base['Leja']:losses+=1
            else:losses=0
            rows.append(row)
            print(json.dumps({'family':name,'n':n,'rank':rank,'value':value}),flush=True)
            if losses==2:killed='two_consecutive_Leja_losses';break
        out['families'].append({'name':name,'rows':rows,'kill':killed,'fit':'INCONCLUSIVE: no surviving family with four n>=4 rows' if killed else 'pending'})
    out['elapsed_seconds']=round(time.time()-start,3)
    path=TOP/'evidence/t2-cyclic-screen.json';path.write_text(json.dumps(out,separators=(',',':'))+'\n'); assert path.stat().st_size<16384
    print(json.dumps({'output':str(path),'bytes':path.stat().st_size,'seconds':out['elapsed_seconds']}))
if __name__=='__main__':main()
