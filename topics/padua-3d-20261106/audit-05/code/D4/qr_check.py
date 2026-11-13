# Check the 13 QR payloads: identity, N, distinctness, cube, membership in the float (2n+1)^3 grid,
# and (MEASURED) whether an own re-implementation of the stated QR recipe reproduces them here.
import json,base64,hashlib,math,sys,itertools
import numpy as np, scipy
from scipy.linalg import qr
S=sys.argv[1]
qr_rec={r['n']:r for r in json.load(open(S+'/evidence/fd4-qr.json'))['rows']}
def idx(n): return [(a,b,c) for a in range(n+1) for b in range(n+1-a) for c in range(n+1-a-b)]
def V(x,n):
    T=[np.polynomial.chebyshev.chebvander(x[:,j],n) for j in range(3)]
    return np.stack([T[0][:,a]*T[1][:,b]*T[2][:,c] for a,b,c in idx(n)],axis=1)
print('numpy',np.__version__,'scipy',scipy.__version__)
for n in range(4,17):
    p=f'{S}/evidence/fd4-qr-n{n}-nodes.json'; raw_file=open(p,'rb').read(); d=json.loads(raw_file)
    raw=base64.b85decode(d['coordinates_base85']); sha=hashlib.sha256(raw).hexdigest(); x=np.frombuffer(raw,'<f8').reshape(-1,3)
    N=math.comb(n+3,3)
    g=np.cos(np.linspace(0,np.pi,2*n+1)); gs=set(g.tolist())
    ingrid=all(v in gs for v in x.flatten().tolist())
    ok=(sha==d['coordinates_sha256']==qr_rec[n]['coordinates_sha256'] and d['N']==N==len(x) and len({tuple(r) for r in x.tolist()})==N and np.abs(x).max()<=1 and ingrid
        and hashlib.sha256(raw_file).hexdigest()==qr_rec[n]['essential_payload']['sha256'] and len(raw_file)==qr_rec[n]['essential_payload']['bytes'])
    cand=np.array(list(itertools.product(g,repeat=3))); piv=qr(V(cand,n).T,pivoting=True,mode='economic')[2]
    regen=cand[piv[:N]]; same=hashlib.sha256(regen.astype('<f8').tobytes()).hexdigest()==sha
    print(n,N,'payload_ok',ok,'ingrid',ingrid,'file_bytes',len(raw_file),'regen_same_hash',same, 'same_set', {tuple(r) for r in regen.tolist()}=={tuple(r) for r in x.tolist()})
