"""Independent arithmetic and interpretation check of frozen L7 raw outputs.

No developer or upstream numerical helper is imported. Saved Q/recurrences
are inputs; the separate full algorithm rerun is identified explicitly.
"""
import argparse, hashlib, itertools, json, math, os, pathlib, platform, sys, time
import numpy as np
import scipy
from scipy.linalg import qr, svdvals

LD = np.longdouble
EPS = np.finfo(float).eps
TOP = pathlib.Path(__file__).resolve().parents[1]
DOMAINS = ('disk', 'lshape', 'triangle', 'sector')
SEEDS = (2026110501, 2026110502)

def sha(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()

def manifest(p):
    return dict(path=str(p), sha256=sha(p), bytes=pathlib.Path(p).stat().st_size)

def sample(domain, seed, count, band=False):
    rng = np.random.default_rng(seed)
    result = []
    while sum(len(a) for a in result) < count:
        a = rng.uniform(-1, 1, size=(4096, 2))
        x, y = a.T
        radius = np.hypot(x, y)
        if domain == 'disk':
            keep = radius <= 1
            distance = 1-radius
        elif domain == 'triangle':
            keep = x+y <= 0
            distance = np.minimum(np.minimum(x+1, y+1), -(x+y)/np.sqrt(2))
        elif domain == 'lshape':
            keep = (x <= 0) | (y <= 0)
            distance = np.minimum.reduce([x+1, y+1, 1-x, 1-y,
                np.hypot(x-np.clip(x, 0, 1), y), np.hypot(x, y-np.clip(y, 0, 1))])
        else:
            keep = (radius >= .4) & (radius <= 1) & (np.mod(np.arctan2(y,x), 2*np.pi) <= 1.5*np.pi)
            distance = np.minimum.reduce([radius-.4, 1-radius,
                np.hypot(x-np.clip(x,.4,1),y), np.hypot(x,y-np.clip(y,-1,-.4))])
        if band:
            keep &= distance <= .05
        result.append(a[keep])
    return np.concatenate(result)[:count]

def chebyshev(x, n):
    c = np.empty((len(x), n+1), dtype=LD)
    c[:,0] = 1
    c[:,1] = x
    for k in range(1,n):
        c[:,k+1] = 2*x*c[:,k]-c[:,k-1]
    return c

def jacobi(x, n, alpha):
    # Three-term recurrence with separately formed rational coefficients.
    p = np.ones_like(x)
    if n == 0:
        return p
    q = (LD(alpha)+(alpha+2)*x)/2
    for j in range(1,n):
        h = LD(2*j+alpha)
        den = 2*(j+1)*(j+alpha+1)*h
        A = (h+1)*h*(h+2)/den
        B = (h+1)*LD(alpha*alpha)/den
        C = 2*(j+alpha)*j*(h+2)/den
        p,q = q,(A*x+B)*q-C*p
    return q

def matrix(points, domain):
    x,y = points.astype(LD).T
    if domain != 'triangle':
        cx,cy = chebyshev(x,24),chebyshev(y,24)
        return np.column_stack([cx[:,t-j]*cy[:,j] for t in range(25) for j in range(t+1)])
    height = (1-y)/2
    horizontal = (x+1)/height-1
    return np.column_stack([jacobi(horizontal,t-j,0)*height**(t-j)*jacobi(y,j,2*(t-j)+1)
                            for t in range(25) for j in range(t+1)])

def target(points):
    x,y = points.T
    return dict(rational=1/(1+25*(x*x+y*y)), tanh=np.tanh(10*(x+y-.3)),
                absolute=np.abs(x-y), entire=np.exp(x)*np.cos(2*y)+np.sin(3*x*y))

def replay(points, raw, method):
    # Recover upstream parent by earliest admissible predecessor, independently
    # of upstream _update_rule. Own sparse recorded windows remain unchanged.
    n = raw[method+'_Q'].shape[1]
    E = np.zeros((len(points),n))
    path = [None]
    if method.startswith('upstream'):
        H,idx = raw[method+'_H'],raw[method+'_index']
        coords = points if method.endswith('xy') else points[:,[1,0]]
        E[:,0] = 1/H[0,0]
        for k in range(1,n):
            choices = [(j,a) for j in range(k) for a in range(2)
                       if np.array_equal(idx[j]+np.eye(2,dtype=int)[a],idx[k])]
            parent,axis = min(choices)
            path.append([axis,parent])
            v = coords[:,axis]*E[:,parent]
            v -= E[:,:k]@H[:k,k]
            E[:,k] = v/H[k,k]
    else:
        E[:,0] = 1/np.sqrt(len(raw['P']))
        for k in range(1,n):
            axis,parent,start = map(int,raw[method+'_parents'][k])
            path.append(['X' if axis==0 else 'Y',parent])
            window = np.arange(start,k)
            E[:,k] = (points[:,axis]*E[:,parent]-E[:,window]@raw[method+'_coeff'][window,k])/raw[method+'_beta'][k]
    return E,path

def errs(a,b):
    return dict(rel_l2=float(np.linalg.norm(a-b)/np.linalg.norm(b)),
                rel_max=float(np.max(np.abs(a-b))/np.max(np.abs(b))))

def check(args):
    start = time.time()
    rows = {}
    cases = []
    inputs = []
    max_metric_scaled = 0.
    max_metric_absolute = 0.
    max_reference_reconstruction = 0.
    losses = []
    independent_errors = {}
    def compare(a,b):
        nonlocal max_metric_scaled,max_metric_absolute
        delta = abs(float(a)-float(b))
        max_metric_absolute = max(max_metric_absolute,delta)
        scaled = delta/(1e-11+1e-7*abs(float(b)))
        max_metric_scaled = max(max_metric_scaled,scaled)
        assert scaled <= 1, (a,b,scaled)
    for domain in DOMAINS:
        for seed in SEEDS:
            found = list(pathlib.Path(args.raw_root).glob(f'*/*/{domain}-{seed}.json'))
            assert len(found)==1,found
            p = found[0]; folder=p.parent
            row=json.loads(p.read_text()); rows[domain,seed]=row
            meta=json.loads((folder/'metadata.json').read_text())
            assert meta['code_sha256']==sha(TOP/'code/l7_natural.py')
            assert meta['prereg_sha256']==sha(TOP/'l7-preregistration.md')
            for name,h in meta['source_sha256'].items():
                assert sha(pathlib.Path(args.external)/'polyrat'/name)==h
            inp_path=folder/f'{domain}-{seed}-inputs.npz'
            raw_path=folder/f'{domain}-{seed}-raw.npz'
            for f in (p,folder/'metadata.json',inp_path,raw_path): inputs.append(manifest(f))
            with np.load(inp_path) as inp, np.load(raw_path) as raw:
                P=sample(domain,seed,1600)
                S=[sample(domain,seed+100,2000),sample(domain,seed+200,2000,True)]
                for name,value in zip(('training','uniform','boundary'),(P,*S)):
                    assert np.array_equal(inp[name],value),(domain,seed,name)
                T=np.vstack(S); allpoints=np.vstack((P,T))
                assert np.array_equal(P,raw['P']) and np.array_equal(T,raw['T'])
                V=matrix(P,domain); V/=np.sqrt(np.sum(V*V,axis=0))
                Eref=matrix(T,domain)/raw['reference_scale']
                U=raw['reference_Q']; R=raw['reference_R']
                reconstruction=float(np.max(np.abs(V-U@R)))
                max_reference_reconstruction=max(max_reference_reconstruction,reconstruction)
                assert reconstruction<1e-14,(domain,reconstruction)
                train=target(P); truth=target(T)
                F=np.column_stack(list(train.values()))
                evals={}; paths={}
                for method in row['cases'][0]['methods']:
                    evals[method],paths[method]=replay(allpoints,raw,method)
                for c in row['cases']:
                    n=c['n']; k=(n+1)*(n+2)//2
                    s=svdvals(np.asarray(V[:,:k],float)); cond=float(s[0]/s[-1])
                    rank=int(np.sum(s>s[0]*max(1600,k)*EPS))
                    Ud=qr(np.asarray(V[:,:k],float),mode='economic')[0]
                    Un=np.asarray(U[:,:k],float)
                    gap=float(svdvals(Un-Ud@(Ud.T@Un))[0])
                    gram=float(np.max(abs(U[:,:k].T@U[:,:k]-np.eye(k,dtype=LD))))
                    trusted=rank==k and cond<1e8 and gram<1e-12 and gap<1e-7 and np.finfo(LD).nmant>np.finfo(float).nmant
                    assert trusted==c['reference']['trusted']
                    refpred={}
                    for name,f in train.items():
                        coeff=U[:,:k].T@f.astype(LD)
                        a=coeff.copy()
                        for j in range(k-1,-1,-1):
                            a[j]=(a[j]-R[j,j+1:k]@a[j+1:])/R[j,j]
                        refpred[name]=np.asarray(Eref[:,:k]@a,float)
                    replay_max=0.
                    for method,metrics in c['methods'].items():
                        Q=raw[method+'_Q'][:,:k]; E=evals[method][:,:k]
                        replay_error=float(np.max(abs(E[:1600]-Q)));replay_max=max(replay_max,replay_error)
                        compare(replay_error,metrics['training_replay_max'])
                        assert hashlib.sha256(json.dumps(paths[method][:k]).encode()).hexdigest()==metrics['parent_path_sha256']
                        W=qr(Q,mode='economic')[0]; G=Q.T@Q-np.eye(k)
                        compare(float(svdvals(Un-W@(W.T@Un))[0]),metrics['gap_raw'])
                        compare(float(svdvals(G)[0]),metrics['gram_2'])
                        compare(float(np.max(abs(G))),metrics['gram_max'])
                        uq,sq,vq=np.linalg.svd(Q,full_matrices=False)
                        use=sq>sq[0]*max(Q.shape)*EPS
                        C=vq[use].T@((uq[:,use].T@F)/sq[use,None])
                        pred=E[1600:]@C
                        for j,name in enumerate(train):
                            saved=c['targets'][name]['methods'][method]
                            assert int(np.sum(use))==saved['fit_rank']
                            for dist,sl in [('uniform',slice(0,2000)),('boundary',slice(2000,4000))]:
                                e=errs(pred[sl,j],truth[name][sl])
                                re=errs(refpred[name][sl],truth[name][sl])
                                diff=float(np.linalg.norm(pred[sl,j]-refpred[name][sl])/np.linalg.norm(truth[name][sl]))
                                for key in e: compare(e[key],saved[dist][key])
                                compare(diff,saved[dist]['difference_vs_reference'])
                                detected=bool(trusted and e['rel_l2']>2*re['rel_l2'] and diff>max(1e-10,100*EPS*cond))
                                assert detected==saved[dist]['resolved_loss'],(domain,seed,n,name,method,dist)
                                key=(domain,seed,n,name,method,dist)
                                independent_errors[key]=e['rel_l2']
                                if detected: losses.append(dict(domain=domain,seed=seed,n=n,target=name,method=method,distribution=dist))
                    cases.append(dict(domain=domain,seed=seed,n=n,trusted=bool(trusted),kappa=cond,span_gap=gap,gram_max=gram,replay_max=replay_max))
            print(domain,seed,'checked',flush=True)
    pairs=[]
    groups=[['upstream_xy','upstream_yx','dev_full','mirror_full','alt_full','adapt_full'],['dev_window','mirror_window','alt_window','adapt_window']]
    for d in DOMAINS:
        for n in (8,16,24):
            if not all(next(c for c in rows[d,s]['cases'] if c['n']==n)['reference']['trusted'] for s in SEEDS):continue
            for name,dist,group in itertools.product(train,('uniform','boundary'),groups):
                for a,b in itertools.combinations(group,2):
                    ratio=[independent_errors[d,s,n,name,a,dist]/independent_errors[d,s,n,name,b,dist] for s in SEEDS]
                    winner=b if min(ratio)>2 else a if max(ratio)<.5 else None
                    if winner:pairs.append(dict(domain=d,n=n,target=name,distribution=dist,a=a,b=b,winner=winner,ratios=ratio))
    # The distinct rerun must have identical actual algorithm arrays and metrics.
    original=next(pathlib.Path(args.raw_root).glob('*/triangle-2026110501/triangle-2026110501-raw.npz'))
    repeated=pathlib.Path(args.rerun)/'triangle-2026110501-raw.npz'
    with np.load(original) as a,np.load(repeated) as b:
        assert a.files==b.files
        assert all(np.array_equal(a[k],b[k]) for k in a.files)
        rerun_arrays=len(a.files)
    inputs.extend([manifest(repeated),manifest(pathlib.Path(args.rerun)/'metadata.json')])
    detail=dict(inputs=inputs,cases=cases,losses=losses,paired_advantages=pairs)
    detailpath=pathlib.Path(args.detail);detailpath.write_text(json.dumps(detail,indent=1)+'\n')
    receipt=dict(status='PASS; finite numerical independent arithmetic and one distinct actual algorithm rerun',
        source=manifest(__file__),command=sys.argv,python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,
        openblas_threads=os.getenv('OPENBLAS_NUM_THREADS'),longdouble_nmant=np.finfo(LD).nmant,
        elapsed_seconds=time.time()-start,detail=manifest(detailpath),cases=cases,
        accepted_reference_cases=sum(c['trusted'] for c in cases),resolved_losses=len(losses),paired_advantages=pairs,
        max_metric_comparison_scaled=max_metric_scaled,max_metric_comparison_absolute=max_metric_absolute,
        max_reference_reconstruction_entry=max_reference_reconstruction,
        algorithm_rerun=dict(domain='triangle',seed=2026110501,identical_arrays=rerun_arrays,
            command=['python','-B',str(TOP/'code/l7_natural.py'),'--external',args.external,'--output-dir',args.rerun,'--domains','triangle','--seeds','2026110501']),
        limits='Saved longdouble reference is numerical, not enclosed. Raw Q/H checked as inputs; only triangle seed1 is an independently executed algorithm rerun. End-to-end loss does not isolate span versus recurrence evaluation causation.')
    pathlib.Path(args.receipt).write_text(json.dumps(receipt,separators=(',',':'))+'\n')

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--raw-root',required=True);ap.add_argument('--external',required=True)
    ap.add_argument('--rerun',required=True);ap.add_argument('--detail',required=True);ap.add_argument('--receipt',required=True)
    check(ap.parse_args())
