"""Scoped IDEA03 screens. Exact rational certificate-list grouping; float maxima.
The exact grouping checks inherited certificates, not their original producer.
"""
import argparse, gzip, hashlib, json, math, sys, time
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from scipy.optimize import minimize, minimize_scalar
from tests_common import Eval, Edge, validate
ROOT=Path(__file__).resolve().parents[4]
TOP=Path(__file__).resolve().parents[2]

def atan_bounds(q, m=30):
    terms=[(-1)**k*F(1,q**(2*k+1)*(2*k+1)) for k in range(m+1)]
    a=sum(terms[:-1]); b=a+terms[-1]
    return min(a,b),max(a,b)
def pi_bounds():
    a,b=atan_bounds(5);c,d=atan_bounds(239)
    return 16*a-4*d,16*b-4*c

def cos_bounds(a,b,K=30):
    def one(t):
        v=sum((-1)**k*t**(2*k)/math.factorial(2*k) for k in range(K+1))
        r=t**(2*K+2)/math.factorial(2*K+2)
        return v-r,v+r
    # monotonicity of cos on [0,pi]; both endpoint bounds are used.
    return one(b)[0],one(a)[1]

def qinterval(I,n):
    xlo,xhi=map(F,I);mid=(float(xlo)+float(xhi))/2
    q=math.acos(mid)*n/math.pi
    a,b=F(math.floor(q*10000)-1,10000),F(math.ceil(q*10000)+1,10000)
    pl,ph=pi_bounds()
    al,ah=cos_bounds(a*pl/n,a*ph/n)
    bl,bh=cos_bounds(b*pl/n,b*ph/n)
    assert al>xhi and bh<xlo
    return a,b

def absbounds(I,c):
    a,b=I[0]-c,I[1]-c
    return (0 if a<=0<=b else min(abs(a),abs(b))), max(abs(a),abs(b))

def assignment(Q,n):
    matches=[]
    for j in range(n+1):
        for k in range(n+2):
            if (j+k)%2==0:continue
            if absbounds(Q[0],j)[1]+absbounds(Q[1],k)[1]<1:matches.append((j,k))
    assert len(matches)==1, (Q,matches)
    return matches[0]

def corners(n):return [(j,k) for j in (0,n) for k in (0,n+1) if (j+k)%2]
def closest(a,n):
    ds=[sum((x-y)**2 for x,y in zip(a,c)) for c in corners(n)]
    return corners(n)[ds.index(min(ds))] if ds.count(min(ds))==1 else None

def pairs(cells,n,ties=False):
    for a in cells:
        c=closest(a,n)
        if ties:
            cc=[c for c in corners(n) if sum((x-y)**2 for x,y in zip(a,c))==min(sum((x-y)**2 for x,y in zip(a,z)) for z in corners(n))]
        else:cc=[] if c is None else [c]
        if not cc:continue
        for e in ((1,1),(1,-1),(-1,1),(-1,-1)):
            b=(a[0]+e[0],a[1]+e[1])
            if b not in cells:continue
            for c in cc:
                if ties:
                    if sum((x-y)**2 for x,y in zip(b,c))!=min(sum((x-y)**2 for x,y in zip(b,z)) for z in corners(n)):continue
                elif closest(b,n)!=c:continue
                if sum((x-y)**2 for x,y in zip(b,c))>sum((x-y)**2 for x,y in zip(a,c)):
                    yield a,b,c

def certified_list():
    base=ROOT/'topics/padua-proof-attempts-2-20261101/outputs'
    cp=base/'a5_n4_certificate.json.gz';gp=base/'a5_n4_global.json'
    raw=cp.read_bytes();cert=json.loads(gzip.decompress(raw));glob=json.loads(gp.read_bytes())
    assert hashlib.sha256(raw).hexdigest()==glob['certificate_sha256']
    vals={r['id']:tuple(map(F,r['enclosure'])) for r in glob['interior_values']}
    groups={};rows=[]
    for r in cert['interior_roots']:
        Q=[qinterval(r['R'][0],4),qinterval(r['R'][1],5)]
        a=assignment(Q,4);groups.setdefault(a,[]).append(r['id'])
        rows.append({'id':r['id'],'R':r['R'],'qbox':[[str(x) for x in I] for I in Q],'cell':a,'value':list(map(str,vals[r['id']]))})
    # Each group's exact max lies in the max of its lower and upper endpoints.
    maxima={a:(max(vals[i][0] for i in ids),max(vals[i][1] for i in ids)) for a,ids in groups.items()}
    comparisons=[]
    for a,b,c in pairs(maxima,4):
        diff=maxima[b][0]-maxima[a][1]
        comparisons.append({'a':a,'b':b,'corner':c,'a_ids':groups[a],'b_ids':groups[b],'reversal_lower':str(diff),'reversed':diff>0})
    tie_comparisons=[]
    for a,b,c in pairs(maxima,4,ties=True):
        diff=maxima[b][0]-maxima[a][1]
        tie_comparisons.append({'a':a,'b':b,'corner':c,'a_ids':groups[a],'b_ids':groups[b],'reversal_lower':str(diff),'reversed':diff>0})
    return {'tie_comparisons':tie_comparisons,'tie_violations':[r for r in tie_comparisons if r['reversed']], 'status':'exact rational inference from inherited PROVED certificate; independent check pending','certificate_sha256':hashlib.sha256(raw).hexdigest(),'global_sha256':hashlib.sha256(gp.read_bytes()).hexdigest(),'pi_bounds':list(map(str,pi_bounds())),'rows':rows,'comparisons':comparisons,'violations':[r for r in comparisons if r['reversed']]}

def diamond_max(e,a):
    n=e.n
    def f(z):
        q=np.array(a)+np.array([(z[0]+z[1])/2,(z[0]-z[1])/2])
        excess=np.maximum(-q,0).sum()+np.maximum(q-[n,n+1],0).sum()
        if excess>1e-12:return 1000+excess
        return -e.one(q[0]*np.pi/n,q[1]*np.pi/(n+1))[0]
    grid=[np.array([u,v]) for u in np.linspace(-1,1,5) for v in np.linspace(-1,1,5)]
    starts=sorted([(f(z),z) for z in grid],key=lambda r:r[0])[:3]
    best=min((x for x,z in starts))
    bestz=starts[0][1]
    for x,z in starts:
        r=minimize(f,z,method='Nelder-Mead',bounds=[(-1,1)]*2,options={'maxiter':180,'xatol':1e-8,'fatol':1e-10})
        if r.fun<best:best,bestz=r.fun,r.x
    return -best,(np.array(a)+[(bestz[0]+bestz[1])/2,(bestz[0]-bestz[1])/2]).tolist()

def edge_max(e,name,k):
    n=e.n;lo=(k-1)*np.pi/(n+1);hi=(k+1)*np.pi/(n+1)
    ts=np.linspace(lo,hi,65);ys=[e.one(name,t) for t in ts];i=int(np.argmax(ys))
    r=minimize_scalar(lambda t:-e.one(name,t),bounds=(ts[max(i-1,0)],ts[min(i+1,64)]),method='bounded',options={'xatol':1e-13})
    return max(ys[i],-r.fun),r.x*(n+1)/np.pi

def measured(ns):
    out=[]
    for n in ns:
        e=Eval(n);cells={}
        if n<=12:
            for j in range(n+1):
                for k in range(n+2):
                    if (j+k)%2:cells[j,k]=diamond_max(e,(j,k))
        comparisons=[{'a':a,'b':b,'corner':c,'a_value':cells[a][0],'b_value':cells[b][0],'difference':cells[b][0]-cells[a][0],'a_arg':cells[a][1],'b_arg':cells[b][1]} for a,b,c in pairs(cells,n)]
        edge=Edge(n);es=[]
        for j,name in ((0,'v+'),(n,'v-')):
            centers=[k for k in range(2,n) if (j+k)%2]
            vs={k:edge_max(edge,name,k) for k in centers}
            for k in centers:
                kk=k+2 if k<(n+1)/2 else k-2
                if kk in vs and abs(kk-(n+1)/2)<abs(k-(n+1)/2):
                    es.append({'edge':name,'source':k,'target':kk,'source_value':vs[k][0],'target_value':vs[kk][0],'difference':vs[kk][0]-vs[k][0]})
        out.append({'n':n,'lc':e.lc,'diamonds':[{'a':a,'value':v,'arg':z} for a,(v,z) in cells.items()],'O_R_violations':[r for r in comparisons if r['difference']>1e-6],'O_R_count':len(comparisons),'E_C_comparisons':es,'E_C_violations':[r for r in es if r['difference']< -1e-6]})
    return out

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--degrees',nargs='*',type=int,default=[4,7,12,24,50]);ap.add_argument('--output',required=True);a=ap.parse_args();start=time.monotonic()
    result={'status':'MEASURED screens plus exact rational inherited-certificate comparisons','validation':validate(),'certified_list':certified_list(),'measurements':measured(a.degrees),'seconds':time.monotonic()-start}
    Path(a.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'output':a.output,'seconds':result['seconds'],'list_violations':len(result['certified_list']['violations']),'summary':[{'n':r['n'],'O_R_violations':len(r['O_R_violations']),'E_C_violations':len(r['E_C_violations'])} for r in result['measurements']]}))
