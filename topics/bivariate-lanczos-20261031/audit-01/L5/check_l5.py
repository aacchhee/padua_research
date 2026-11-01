"""Independent audit driver; source copied to /tmp, all outputs in owned audit directory.

Run OPENBLAS_NUM_THREADS=1 python3 -I .../check_l5.py setup|analysis|rules|kill|small
This reruns committed implementations, not a new implementation of Algorithm 1.
"""
from pathlib import Path
import hashlib, json, os, platform, shutil, subprocess, sys, tempfile, time
import numpy as np
import scipy

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]
SRC = ROOT / 'tracks/bivariate-lanczos/code'
WORK = Path('/tmp/padua-l5-audit-3a9063b')
def emit(rec):
    print(json.dumps(rec, allow_nan=False), flush=True)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def setup():
    WORK.mkdir(exist_ok=True)
    sources = []
    for sub in ('L5', 'inputs', 'review_L5'):
        dest = WORK / sub; dest.mkdir(exist_ok=True)
        for p in sorted((SRC / sub).iterdir()):
            if p.suffix not in ('.py', '.c'): continue
            shutil.copy2(p, dest / p.name)
            sources.append(dict(path=str(p.relative_to(ROOT)), sha256=sha(p), bytes=p.stat().st_size))
    builds = [('L5/givens_core.c', 'L5/libgivens_core.so', []),
              ('L5/givens_core.c', 'L5/libgivens_core2.so', []),
              ('L5/givens_dual.c', 'L5/libgivens_dual.so', []),
              ('review_L5/agivens.c', 'review_L5/libagivens.so', []),
              ('review_L5/agivens.c', 'review_L5/libagivens_ld.so', ['-DAG_LD'])]
    commands=[]
    for src, dst, flags in builds:
        cmd=['gcc','-O2','-ffp-contract=off',*flags,'-shared','-fPIC','-o',str(WORK/dst),str(WORK/src),'-lm']
        subprocess.run(cmd,check=True); commands.append(cmd)
    prov=dict(head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
              python=sys.version, numpy=np.__version__, scipy=scipy.__version__, platform=platform.platform(),
              compiler=subprocess.check_output(['gcc','--version'],text=True).splitlines()[0],
              longdouble_mantissa=int(np.finfo(np.longdouble).nmant), threads=os.environ.get('OPENBLAS_NUM_THREADS'),
              sources=sources, build_commands=commands)
    (OUT/'source_manifest.json').write_text(json.dumps(prov,indent=2)+'\n')
    emit(dict(setup='ok', sources=len(sources), workspace=str(WORK)))
def libraries():
    sys.path.insert(0,str(WORK/'L5')); sys.path.insert(0,str(WORK/'review_L5'))
    os.environ['AG_BUILD']=str(WORK/'review_L5')
    import l5_lib as L, prefix as P, alib as A, exp_r03 as E
    return L,P,A,E
def rules():
    L,P,A,E=libraries()
    for n in (20,30):
        pts,wc,Qc=P.padua_orthogonal_basis(n); N=len(pts)
        for wn,w in [('cub',wc),('rand',np.random.default_rng(1000+n).uniform(.1,1,N))]:
            rx,ry=L.reference_H(pts[:,0].copy(),pts[:,1].copy(),np.sqrt(w),N)
            for lab,perm in [('given',np.arange(N)),('sortx',np.lexsort((pts[:,1],pts[:,0])))]:
                x,y,v=pts[perm,0].copy(),pts[perm,1].copy(),np.sqrt(w[perm])
                rec=dict(mode='rules',n=n,weights=wn,order=lab)
                for name,(kind,rule,kappa) in E.RULES.items():
                    if kind=='c': hx,hy,st=L.givens_c(x,y,v,rule=['scheme','largest'][rule])
                    else: hx,hy,st=L.givens_c2(x,y,v,rule,kappa)
                    rec[name]=E.to_err(hx,hy,N,rx,ry); rec['alternatives_'+name]=int(st[2])
                emit(rec)
                # Original finite failure demonstrated on n=20; n=30 FIFO is costly.
                if n==20:
                    for tau in (1e-8,1e-3):
                        t=time.monotonic(); hx,hy,info=E.defer_run(x,y,v,tau)
                        emit(dict(mode='fifo',n=n,weights=wn,order=lab,tau=tau,
                                  error=E.to_err(hx,hy,N,rx,ry), **info, seconds=time.monotonic()-t))
def kill():
    L,P,A,E=libraries()
    for n in (30,50):
        pts,wc,Qc=P.padua_orthogonal_basis(n); N=len(pts); perm=P.gepp_order(Qc)
        # Independent polynomial construction (three-term Chebyshev, QR) on identical doubles.
        x,y=pts[:,0].copy(),pts[:,1].copy(); q=A.householder(x,y,wc,N)
        rx,ry=A.signfix_H(*A.H_from_Q(q,x,y),N)
        B=Qc[perm]; bounds=A.prefix_lu_bounds(B)
        lo,up,growth,resid=bounds
        # Normwise residual correction; factor/inverse rounding not rigorously enclosed.
        minlo=float(np.min(lo)); correction=N*resid
        rec=dict(mode='kill',n=n,N=N,order='developer_gepp',min_lu_lower_bound=minlo,
                 lu_max_entry_residual=resid, residual_corrected_lower=minlo-correction,
                 prefix_status='floating-point estimate, not exact certificate',
                 input_matrix_sha256=hashlib.sha256(B.tobytes()).hexdigest(),
                 permutation_sha256=hashlib.sha256(perm.tobytes()).hexdigest())
        xp,yp,v=x[perm].copy(),y[perm].copy(),np.sqrt(wc[perm])
        for rule in ('scheme','largest'):
            hx,hy,st=L.givens_c(xp,yp,v,rule=rule)
            fx,fy=A.signfix_H(hx,hy,N)
            rec[rule]=A.relerr(fx,fy,rx,ry); rec['rotations_'+rule]=int(st[0])
            ax,ay,w,qt,ast=A.givens(xp,yp,v,rule=rule,accQ=True)
            rec['reviewer_core_maxdiff_'+rule]=float(max(np.max(np.abs(ax-hx)),np.max(np.abs(ay-hy))))
            nh=np.sqrt(np.sum(x*x)+np.sum(y*y))
            rec['backward_residual_'+rule]=float(np.sqrt(np.sum((qt@(xp[:,None]*qt.T)-ax)**2)+np.sum((qt@(yp[:,None]*qt.T)-ay)**2))/nh)
            rec['first_column_'+rule]=float(np.linalg.norm(np.abs(qt[0])-v/np.linalg.norm(v)))
            pp,pc,ap,ac=A.pivot_tables(N); defect=0.
            for j in range(1,N-1):
                for part,col in ((pp[j],pc[j]),(ap[j],ac[j])):
                    if part<0: continue
                    defect=max(defect,float(np.max(np.abs((ax if part==1 else ay)[j+1:,col]))))
            rec['structure_defect_'+rule]=defect/(nh/np.sqrt(N))
        rec['catastrophe']=rec['largest']>=1e-10 and rec['largest']/rec['scheme']>=1e3
        emit(rec)
def small():
    L,P,A,E=libraries()
    for n in (6,10,14):
        pts,w,Q=P.padua_orthogonal_basis(n); N=len(pts)
        for lab,perm in [('given',np.arange(N)),('gepp',P.gepp_order(Q))]:
            x,y,v=pts[perm,0].copy(),pts[perm,1].copy(),np.sqrt(w[perm])
            for rule in ('scheme','largest'):
                hx,hy,st=L.givens_c(x,y,v,rule=rule)
                _,px,py=L.F.givens(x,y,v,N,pivot=rule)
                emit(dict(mode='port',n=n,order=lab,rule=rule,max_diff=float(max(np.max(np.abs(hx-px)),np.max(np.abs(hy-py))))))
        for lab,perm in [('given',np.arange(N)),('gepp',P.gepp_order(Q))]:
            # Direct exhaustive SVD independently validates the fast prefix classification.
            b=Q[perm]; fast=P.prefix_scan(b,use_comb=P.combinatorial_singular(pts[perm,0],pts[perm,1]))
            singular=np.array([np.linalg.svd(b[:k,:k],compute_uv=False)[-1] for k in range(1,N+1)])
            emit(dict(mode='prefix_svd',n=n,order=lab,min_sigma=float(singular.min()),
                      singular_prefixes=int((singular<1e-11).sum()),
                      mismatch=int(np.sum(fast['sing']!=(singular<1e-11)))))
    cmd=[sys.executable,'-I',str(WORK/'L5/exp_r02_dual.py'),str(OUT/'dual.jsonl'),'padua_cub','15','20']
    subprocess.run(cmd,check=True)
def analysis():
    logs=ROOT/'topics/bivariate-lanczos-20261031/directions/L5/logs'
    subprocess.run([sys.executable,'-I',str(WORK/'L5/analyze_r01c.py'),str(logs)],check=True)
def diagnostics():
    from scipy.stats import linregress, t
    from collections import defaultdict
    import mpmath as mp
    L,P,A,E=libraries()
    logs=ROOT/'topics/bivariate-lanczos-20261031/directions/L5/logs'
    for family in ('padua_cub','padua_rand','random','random_cheb'):
        rows=[json.loads(s) for s in (logs/f'r01_{family}.jsonl').read_text().splitlines()]
        rows=[r for r in rows if not r.get('meta')]
        for other in ('hl','cgs2','hh'):
            by=defaultdict(list)
            for r in rows: by[r['M']].append(np.log10(r['givens-scheme']/r[other]))
            sizes=sorted(by); fit=linregress(np.log10(sizes),[np.mean(by[k]) for k in sizes])
            width=t.ppf(.975,len(sizes)-2)*fit.stderr
            emit(dict(mode='paired_difference',family=family,comparator=other,
                      slope=float(fit.slope),ci95=[float(fit.slope-width),float(fit.slope+width)],df=len(sizes)-2))
    rows=[json.loads(s) for s in (logs/'r02_dual.jsonl').read_text().splitlines()]
    for r in rows:
        if r.get('order')!='gepp': continue
        drops=[dict(i0=r['ckpt'][k],i1=r['ckpt'][k+1],before=v,after=r['relfro'][k+1])
               for k,v in enumerate(r['relfro'][:-1]) if r['relfro'][k+1]<v]
        emit(dict(mode='monotonicity',n=r['size'],decreases=drops))
    mp.mp.dps=80
    for n in (10,30,50,62):
        pts,w,q=P.padua_orthogonal_basis(n); N=len(pts)
        ij=[(j,k) for j in range(n+1) for k in range(n+2) if (j+k)%2==0]
        ld=np.longdouble; pi=ld('3.1415926535897932384626433832795028841971693993751')
        jj=np.array([j for j,k in ij],dtype=ld); kk=np.array([k for j,k in ij],dtype=ld)
        tx=np.cos(jj[:,None]*np.arange(n+1)*pi/n)
        ty=np.cos(kk[:,None]*np.arange(n+1)*pi/(n+1))
        exactish=np.empty_like(q,dtype=ld)
        weights=np.array([ld(2)*(ld('.5') if j in (0,n) else 1)*(ld('.5') if k in (0,n+1) else 1)/ld(n*(n+1)) for j,k in ij])
        for col,(a,b) in enumerate(A.monomials(N)):
            factor=np.sqrt(ld(2))**int(a>0)*np.sqrt(ld(2))**int(b>0)
            if (a,b)==(n,0):factor/=np.sqrt(ld(2))
            exactish[:,col]=np.sqrt(weights)*factor*tx[:,a]*ty[:,b]
        row,col=np.unravel_index(np.argmax(np.abs(q.astype(ld)-exactish)),q.shape)
        j,k=ij[row];a,b=A.monomials(N)[col]
        ww=mp.mpf(2)*(mp.mpf('.5') if j in (0,n) else 1)*(mp.mpf('.5') if k in (0,n+1) else 1)/(n*(n+1))
        factor=mp.sqrt(2)**int(a>0)*mp.sqrt(2)**int(b>0)/(mp.sqrt(2) if (a,b)==(n,0) else 1)
        ideal=mp.sqrt(ww)*factor*mp.cos(mp.pi*j*a/n)*mp.cos(mp.pi*k*b/(n+1))
        err=abs(mp.mpf(float(q[row,col]))-ideal)
        def cheb_mp(z,degree):
            z=mp.mpf(float(z)); prev,cur=mp.mpf(1),z
            if degree==0:return prev
            for _ in range(1,degree):prev,cur=cur,2*z*cur-prev
            return cur
        vals=[cheb_mp(xx,a)*cheb_mp(yy,b) for xx,yy in pts]
        norm=mp.sqrt(mp.fsum(mp.mpf(float(ww))*vv*vv for ww,vv in zip(w,vals)))
        same_input=mp.sqrt(mp.mpf(float(w[row])))*vals[row]/norm
        same_error=abs(mp.mpf(float(q[row,col]))-same_input)
        emit(dict(mode='entry_rounding',n=n,row=int(row),col=int(col),j=j,k=k,a=a,b=b,
                  error=str(err),error_in_u=str(err/(mp.mpf(2)**-53)),mpmath_dps=mp.mp.dps,
                  same_stored_input_error_in_u=str(same_error/(mp.mpf(2)**-53)),
                  target='exact Padua angles and exact cubature weights, analytic column norms'))
def fresh_analysis():
    from scipy.stats import linregress,t
    from collections import defaultdict
    rows=[json.loads(s) for s in (OUT/'random-rerun.jsonl').read_text().splitlines()]
    rows=[r for r in rows if not r.get('meta')]
    expected={66,136,231,496,861,1326,2016}
    assert len(rows)==35 and {r['M'] for r in rows}==expected
    for M in expected:assert {r['order'] for r in rows if r['M']==M}=={f'seed{k}' for k in range(1,6)}
    for method in ('givens-scheme','givens-largest','hl','bj','cgs2','hh'):
        for lo in (0,496):
            by=defaultdict(list)
            for r in rows:
                if r['M']>=lo:by[r['M']].append(np.log10(r[method]))
            sizes=sorted(by); f=linregress(np.log10(sizes),[np.mean(by[M]) for M in sizes])
            h=t.ppf(.975,len(sizes)-2)*f.stderr
            emit(dict(mode='fresh_size_fit',family='random',method=method,min_M=lo,rows=sum(map(len,by.values())),
                      slope=float(f.slope),ci95=[float(f.slope-h),float(f.slope+h)],df=len(sizes)-2))
def manifest():
    files=[]
    for p in sorted(OUT.iterdir()):
        if not p.is_file() or p.name=='evidence_manifest.json':continue
        files.append(dict(path=str(p.relative_to(ROOT)),bytes=p.stat().st_size,sha256=sha(p)))
    data=dict(audited_head='3a9063b84d14ca0a5998378371e27643fde50a29',
              candidate='5ccfac223f466a9105450365d8c6c3781ff7d922',files=files,
              total_bytes=sum(f['bytes'] for f in files),
              retention='Small necessary audit evidence intended for Git; copied sources and binaries remain ephemeral in /tmp. No cold-storage destination selected or invented.',
              commands='Exact producer commands, seeds and observed results are recorded in ../L5.md and source_manifest.json. check_l5.py setup reconstructs the /tmp workspace from tracked sources.',
              checker='Recompute SHA-256 and byte length for each path; fresh_analysis asserts all 35 size/seed rows are present.',
              classification='All numerical calculations are MEASURED; no computer-assisted proof claimed.')
    assert data['total_bytes']<1_000_000
    (OUT/'evidence_manifest.json').write_text(json.dumps(data,indent=2)+'\n')
    emit(dict(manifest='ok',files=len(files),total_bytes=data['total_bytes']))
if __name__=='__main__':
    {'setup':setup,'analysis':analysis,'rules':rules,'kill':kill,'small':small,'diagnostics':diagnostics,
     'fresh_analysis':fresh_analysis,'manifest':manifest}[sys.argv[1]]()
