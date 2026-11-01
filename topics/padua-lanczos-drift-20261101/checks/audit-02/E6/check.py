"""Independent audit-02 E6 checks; no developer/upstream files are changed.

The producer is imported only on the comparison side. Sampling, support tests,
long-double polynomial evaluation, triangular solve and norms below are auditor
implementations. This is numerical corroboration, not a certified enclosure.
"""
import argparse
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import traceback

ROOT = Path(__file__).resolve().parents[5]
TOPIC = ROOT / 'topics/padua-lanczos-drift-20261101'
CODE = ROOT / 'tracks/bivariate-lanczos/code/drift'
EXTERNAL = Path('/workspace/padua-drift-external/polyrat')
CANDIDATE = 'cef79d66321a93d93d53e53efcb7e6744c387481'
RULES_HEAD = '2fd5456066de08094a35542f2ff6443c27d8c149'
sys.path.insert(0, str(CODE))
import numpy as np
import scipy
from scipy.linalg import qr, svd, solve_triangular
import e6_offsample as prod

LD = np.longdouble


def digest(data):
    return hashlib.sha256(data).hexdigest()


def pin(path):
    data = Path(path).read_bytes()
    return {'bytes': len(data), 'sha256': digest(data)}


def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args], text=True).strip()


def compare(a, b, ignored=()):
    """Compare every leaf, not rounded summaries. Float equality is exact here."""
    rows = []
    structural = []
    def walk(x, y, path):
        if path in ignored:
            return
        if isinstance(x, dict) and isinstance(y, dict):
            if set(x) != set(y):
                structural.append({'path': path, 'keys': [list(x), list(y)]})
            for k in x.keys() & y.keys():
                walk(x[k], y[k], path + '/' + k)
        elif isinstance(x, list) and isinstance(y, list):
            if len(x) != len(y):
                structural.append({'path': path, 'lengths': [len(x), len(y)]})
            for i, (u, v) in enumerate(zip(x, y)):
                walk(u, v, path + '/' + str(i))
        else:
            row = {'path': path, 'actual': x, 'committed': y, 'equal': x == y}
            if isinstance(x, (int, float)) and not isinstance(x, bool) and isinstance(y, (int, float)):
                row['absolute_difference'] = abs(x-y)
            rows.append(row)
    walk(a, b, '')
    return {'ignored_paths': list(ignored), 'leaf_count': len(rows),
            'numeric_leaf_count': sum('absolute_difference' in r for r in rows),
            'all_equal': not structural and all(r['equal'] for r in rows),
            'structural_differences': structural, 'leaves': rows}


def rotate(z, inverse=False):
    c, s = np.cos(np.pi/4), np.sin(np.pi/4)
    if inverse:
        s = -s
    return np.column_stack((c*z[:,0]-s*z[:,1], s*z[:,0]+c*z[:,1]))


def training_nodes(name):
    rng = np.random.default_rng(11)
    square = rng.uniform(-1, 1, (1681, 2))
    accepted = 0
    while accepted < 1681:
        p = rng.uniform(-1, 1, 2)
        accepted += p @ p <= 1
    triangle = []
    while len(triangle) < 1681:
        p = rng.uniform(0, 1, 2)
        if p[0] + p[1] <= 1:
            triangle.append(2*p-1)
    # Matrix multiplication preserves the benchmark's declared rounded inputs.
    c, s = np.cos(np.pi/4), np.sin(np.pi/4)
    return (square @ np.array([[c,s],[-s,c]]) if name == 'rotpi4'
            else np.array(triangle)), np.ones(1681)


def in_support(z, name, tol=1e-12):
    return ((np.abs(z) <= 1+tol).all(axis=1) if name == 'rotpi4'
            else ((z >= -1-tol).all(axis=1) & (z.sum(axis=1) <= tol)))


def boundary(name, rng, count):
    lengths = np.array([2., 2., 2., 2.] if name == 'rotpi4' else [2., np.sqrt(8.), 2.])
    vertices = (np.array([[-1.,-1.],[1.,-1.],[1.,1.],[-1.,1.]]) if name == 'rotpi4'
                else np.array([[-1.,-1.],[1.,-1.],[-1.,1.]]))
    distances = rng.uniform(0, lengths.sum(), count)
    ends = np.cumsum(lengths)
    edge = np.sum(distances[:,None] >= ends[None,:], axis=1)
    starts = np.r_[0., ends[:-1]]
    out, normals = [], []
    for dist, e in zip(distances, edge):
        a, b = vertices[e], vertices[(e+1) % len(vertices)]
        d = b-a
        out.append(a+(dist-starts[e])/lengths[e]*d)
        normals.append(np.array([-d[1],d[0]])/lengths[e])
    return np.array(out), np.array(normals), vertices, edge, lengths


def samples(name):
    rng = np.random.default_rng(2026110101)
    if name == 'rotpi4':
        uniform = rng.uniform(-1, 1, (4000,2))
    else:
        candidate = 2*rng.random((24000,2))-1
        uniform = candidate[candidate[:,0]+candidate[:,1] <= 0][:4000]
    rng = np.random.default_rng(2026110102)
    edge, _, vertices, edge_ids, lengths = boundary(name,rng,1000)
    on = np.vstack((edge, vertices))
    near, normals, _, _, _ = boundary(name,rng,4000)
    distances = np.power(10.,rng.uniform(-6,-1,4000))
    near += distances[:,None]*normals
    mask = in_support(near,name)
    near = near[mask][:1000]
    stats = {'native_mean_uniform': uniform.mean(axis=0).tolist(),
             'native_covariance_uniform': np.cov(uniform.T,bias=True).tolist(),
             'expected_mean': [0,0] if name == 'rotpi4' else [-1/3,-1/3],
             'expected_covariance': [[1/3,0],[0,1/3]] if name == 'rotpi4' else [[2/9,-1/9],[-1/9,2/9]],
             'uniform_all_inside': bool(in_support(uniform,name).all()),
             'on_all_inside': bool(in_support(on,name).all()),
             'near_all_inside': bool(in_support(near,name).all()),
             'edge_counts': np.bincount(edge_ids,minlength=len(vertices)).tolist(),
             'expected_edge_probabilities': (lengths/lengths.sum()).tolist(),
             'near_candidates_rejected': int((~mask).sum()),
             'accepted_normal_offset_min': float(distances[mask][:1000].min()),
             'accepted_normal_offset_max': float(distances[mask][:1000].max())}
    if name == 'rotpi4':
        uniform,on,near = map(rotate,(uniform,on,near))
    return {'uniform_interior':uniform,'boundary_on_edges':on,'boundary_near_edges':near}, stats


def jacobi(n,a,b,x):
    if n == 0:
        return np.ones_like(x)
    prev = np.ones_like(x)
    cur = (LD(a-b)+LD(a+b+2)*x)/2
    for k in range(2,n+1):
        t = LD(2*k+a+b)
        nex = ((t-1)*(t*(t-2)*x+a*a-b*b)*cur
               -2*LD(k+a-1)*(k+b-1)*t*prev)/(2*LD(k)*(k+a+b)*(t-2))
        prev,cur = cur,nex
    return cur


def reference_values(points,n,name,training):
    """No scipy.special/np.chebvander/producer basis used in this branch."""
    z, train = points.astype(LD),training.astype(LD)
    if name == 'rotpi4':
        z, train = rotate(z,True), rotate(train,True)
        center = (train.max(axis=0)+train.min(axis=0))/2
        radius = (train.max(axis=0)-train.min(axis=0))/2
        z = (z-center)/radius
        tx,ty = [np.ones(len(z),dtype=LD)],[np.ones(len(z),dtype=LD)]
        tx.append(z[:,0]);ty.append(z[:,1])
        for k in range(2,n+1):
            tx.append(2*z[:,0]*tx[-1]-tx[-2]);ty.append(2*z[:,1]*ty[-1]-ty[-2])
        return np.column_stack([tx[t-j]*ty[j] for t in range(n+1) for j in range(t+1)])
    xi,eta = (z[:,0]+1)/2,(z[:,1]+1)/2
    h=1-eta; u=2*xi-h
    hom=[np.ones(len(z),dtype=LD),u]
    for k in range(2,n+1):
        hom.append(((2*k-1)*u*hom[-1]-(k-1)*h*h*hom[-2])/k)
    return np.column_stack([hom[t-j]*jacobi(j,2*(t-j)+1,0,2*eta-1)
                            for t in range(n+1) for j in range(t+1)])


def backsolve(r,v):
    r=r.astype(LD);v=v.astype(LD);x=np.empty(len(v),dtype=LD)
    for j in range(len(v)-1,-1,-1):
        x[j]=(v[j]-np.sum(r[j,j+1:]*x[j+1:],dtype=LD))/r[j,j]
    return x


def norm(x):
    x=np.asarray(x,dtype=LD)
    return np.sqrt(np.sum(x*x,dtype=LD))


def errors(a,b):
    a,b=np.asarray(a,dtype=LD),np.asarray(b,dtype=LD)
    return {'rel_l2':float(norm(a-b)/norm(b)),
            'rel_max':float(np.max(np.abs(a-b))/np.max(np.abs(b)))}


def independent_case(up,name,n):
    p,w=training_nodes(name)
    pp,ww,_=prod.L2.benchmark(name)
    own_samples,geometry=samples(name)
    produced_samples=prod.make_samples(name)
    geometry['independent_vs_producer_max_abs']={k:float(np.max(np.abs(v-produced_samples[k]))) for k,v in own_samples.items()}
    sets={'midpoint':(p[:128]+p[-128:])/2,
          'uniform_interior':produced_samples['uniform_interior'],
          'boundary':np.vstack((produced_samples['boundary_on_edges'],produced_samples['boundary_near_edges'])),
          'boundary_on_edges':produced_samples['boundary_on_edges'],
          'boundary_near_edges':produced_samples['boundary_near_edges']}
    allpts=np.vstack(list(sets.values())); sizes=[len(v) for v in sets.values()]
    offsets=np.cumsum([0]+sizes)
    u,r,vtest,kappa,smin,rank=prod.reference(p,w,n,name,allpts)
    q,h,idx=up.vandermonde_arnoldi_CGS(p[:,[1,0]],n,weight=np.sqrt(w))
    met,_,v=prod.metrics(q,u)
    f=u@v;truth=vtest@solve_triangular(r,v)
    prediction=up.vandermonde_arnoldi_eval(allpts[:,[1,0]],h,idx)@np.linalg.lstsq(q,f,rcond=None)[0]
    rebuilt={k:errors(prediction[offsets[j]:offsets[j+1]],truth[offsets[j]:offsets[j+1]]) for j,k in enumerate(sets)}
    committed=json.loads((TOPIC/'evidence/response-01-e6-offsample.json').read_text())
    crow=next(c for c in committed['cases'] if c['name']==name)['targets']['adversarial']['upstream_yx']
    norm_comparison={k:{metric:{'independent':value,'committed':crow[k][metric],
                               'absolute_difference':abs(value-crow[k][metric])}
                        for metric,value in values.items()} for k,values in rebuilt.items()}
    lo,hi=offsets[1:3]
    uniform_error=(prediction[lo:hi]-truth[lo:hi])**2
    worst=int(np.argmax(uniform_error))
    verts=(rotate(np.array([[-1.,-1.],[1.,-1.],[1.,1.],[-1.,1.]])) if name=='rotpi4'
           else np.array([[-1.,-1.],[1.,-1.],[-1.,1.]]))
    vertex_dist=np.linalg.norm(allpts[lo:hi,None,:]-verts[None,:,:],axis=2).min(axis=1)
    vertex_probe={'worst_uniform_point':allpts[lo+worst].tolist(),
                  'worst_point_distance_to_nearest_vertex':float(vertex_dist[worst]),
                  'largest_ten_points_fraction_of_squared_error':float(np.sort(uniform_error)[-10:].sum()/uniform_error.sum()),
                  'nearest_200_to_vertices_fraction_of_squared_error':float(uniform_error[np.argsort(vertex_dist)[:200]].sum()/uniform_error.sum())}
    # Include endpoints, every sample kind, and the worst-error point of each kind.
    chosen=set()
    for j in range(len(sets)):
        start,stop=offsets[j:j+2]
        chosen.update([int(start),int(start+1),int(stop-1),int(start+(stop-start)//2),int(start+np.argmax(np.abs(prediction[start:stop]-truth[start:stop])))])
    chosen.update(range(int(offsets[3]+1000),int(offsets[3]+1000+(4 if name=='rotpi4' else 3))))
    chosen=sorted(chosen)
    rawtrain=reference_values(p,n,name,p)
    scales=np.sqrt(np.sum(rawtrain*rawtrain,axis=0,dtype=LD))
    rawtest=reference_values(allpts[chosen],n,name,p)
    independent_eval=rawtest/scales
    independent_truth=independent_eval@backsolve(r,v)
    # Different evaluator, independently normalized, independently QR'd.
    independent_u=qr(np.asarray(rawtrain/scales,dtype=float),mode='economic')[0]
    wq=qr(q,mode='economic')[0]
    gap=float(svd(independent_u-wq@(wq.T@independent_u),compute_uv=False)[0])
    truth_difference=errors(independent_truth,truth[chosen])
    normalized_basis_difference=float(np.max(np.abs(independent_eval-vtest[chosen])))
    targets={}
    zl=allpts[chosen].astype(LD)
    for target,expected in [('exp_xpy',np.exp(zl[:,0]+zl[:,1])),('generic',np.exp(zl[:,0])*np.cos(2*zl[:,1])+np.sin(3*zl[:,0]*zl[:,1]))]:
        actual=(prod.target_exp if target=='exp_xpy' else prod.target_generic)(allpts[chosen])
        targets[target]=errors(actual,expected)
    return {'name':name,'n':n,'M':len(p),'N':len(r),
            'input_sha256':digest(p.tobytes()+w.tobytes()),
            'independent_training_bytes_equal':bool(np.array_equal(p,pp) and np.array_equal(w,ww)),
            'sample_hashes':{k:digest(z.tobytes()) for k,z in sets.items()},
            'geometry':geometry,'independent_norm_adversarial_errors':rebuilt,
            'independent_norm_comparison':norm_comparison,'vertex_dominance_probe':vertex_probe,
            'producer_gap':met['gap'],'independent_evaluator_QR_gap':gap,
            'gap_absolute_difference':abs(gap-met['gap']),
            'independent_truth_vs_producer':truth_difference,
            'normalized_basis_max_abs_difference':normalized_basis_difference,
            'selected_point_indices':chosen,'selected_points':allpts[chosen].tolist(),
            'selected_reference_truth':truth[chosen].tolist(),
            'selected_independent_reference_truth':[float(x) for x in independent_truth],
            'smooth_target_evaluation_difference':targets,
            'diagnostic_tolerances':{'gap_abs':1e-11,'reference_truth_rel_l2':1e-10,'basis_abs':1e-10,'sample_coordinate_abs':1e-14},
            'diagnostic_pass':bool(abs(gap-met['gap'])<1e-11 and truth_difference['rel_l2']<1e-10 and normalized_basis_difference<1e-10 and max(geometry['independent_vs_producer_max_abs'].values())<1e-14 and max(z['absolute_difference'] for a in norm_comparison.values() for z in a.values())<1e-15)}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--work',required=True);ap.add_argument('--output',required=True);ap.add_argument('--compat',action='store_true');args=ap.parse_args()
    work=Path(args.work); up=prod.load_upstream(str(EXTERNAL))
    if args.compat:
        result={'numpy':np.__version__,'python':platform.python_version(),'numpy_path':np.__file__,'upstream_path':up.__file__,'upstream_sha256':pin(up.__file__)['sha256'],'probe':'vandermonde_arnoldi_CGS(default_rng(21).uniform(-1,1,(20,2)),2)'}
        try:
            up.vandermonde_arnoldi_CGS(np.random.default_rng(21).uniform(-1,1,(20,2)),2)
            result['result']='PASS'
        except Exception as error:
            result.update(result='FAIL',exception_type=type(error).__name__,message=str(error),traceback=traceback.format_exc())
        Path(args.output).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result));return
    rerun=json.loads((work/'offsample-rerun.json').read_text())
    committed=json.loads((TOPIC/'evidence/response-01-e6-offsample.json').read_text())
    grids=json.loads((work/'grids16-rerun.json').read_text())
    oldgrids=json.loads((TOPIC/'evidence/e6-frozen-grids.json').read_text())
    files=['AGENTS.md','agents/WORKFLOW.md','agents/codex/CODEX.md','state/IDEAS.md','literature/INDEX.md',
           'tracks/bivariate-lanczos/theory/drift-codex-e6-50-public-va-drift-measured.md',
           'tracks/bivariate-lanczos/code/drift/e6_offsample.py','tracks/bivariate-lanczos/code/drift/e6_benchmark.py',
           'tracks/bivariate-lanczos/code/drift/e6_smooth.py','tracks/bivariate-lanczos/code/L2/l2_core.py',
           'tracks/bivariate-lanczos/code/L1/l1_recurrence.py']
    files += [str(p.relative_to(ROOT)) for p in [TOPIC/'ideas-e6.md',TOPIC/'directions/E6.md',TOPIC/'external-code.md',TOPIC/'response-01.md',TOPIC/'checks/response-01/E6-developer-report.md',TOPIC/'evidence/response-01-e6-offsample.json',TOPIC/'evidence/response-01-manifest.json',TOPIC/'evidence/e6-frozen-grids.json']]
    pins={}
    for name in files:
        snap=subprocess.check_output(['git','-C',str(ROOT),'show',CANDIDATE+':'+name])
        pins[name]={**pin(ROOT/name),'candidate_sha256':digest(snap),'matches_candidate':digest(snap)==pin(ROOT/name)['sha256']}
    result={'auditor':'Codex independent E6 reviewer; requested gpt-6-astra xhigh; serving variant not independently exposed',
            'rules_read_head':RULES_HEAD,'updated_workflow_read_head':'1776029bdd6613d186abf0aa149a4216ba45073a','candidate':CANDIDATE,'head_at_check':git('rev-parse','HEAD'),
            'command':' '.join(sys.argv),'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,
            'OPENBLAS_NUM_THREADS':os.getenv('OPENBLAS_NUM_THREADS'),'longdouble_eps':str(np.finfo(LD).eps),
            'dependency_backports_cached_property':importlib.metadata.version('backports.cached-property'),
            'numpy_build':np.__config__.show(mode='dicts'),
            'source_pins':pins,'checker_pin':pin(__file__),
            'upstream_head':subprocess.check_output(['git','-C',str(EXTERNAL),'rev-parse','HEAD'],text=True).strip(),
            'upstream_status':subprocess.check_output(['git','-C',str(EXTERNAL),'status','--porcelain'],text=True),
            'upstream_pins':{name:pin(EXTERNAL/'polyrat'/name) for name in ['arnoldi.py','index.py','basis.py','version.py','__init__.py']},
            'output_pins':{name:pin(work/name) for name in ['offsample-rerun.json','grids16-rerun.json','numpy240-probe.json','numpy241-probe.json','numpy240-install.json','numpy241-install.json']},
            'BNT_source':{'path':'/workspace/padua-drift-external/chebfun-examples/linalg/VandermondeArnoldi.m',
                          'pin':pin('/workspace/padua-drift-external/chebfun-examples/linalg/VandermondeArnoldi.m'),
                          'commit':subprocess.check_output(['git','-C','/workspace/padua-drift-external/chebfun-examples','rev-parse','HEAD'],text=True).strip(),
                          'reading':'Full 186-line source read, univariate MGS; not executed'},
            'response_comparison':compare(rerun,committed,('/command','/python','/elapsed_seconds')),
            'grids16_comparison':compare(grids,oldgrids,('/python',)),
            'selection_check':__import__('e6_benchmark').selection_check(up,47),
            'independent_cases':[],
            'scope':{'response_cases':['rotpi4 n24','triangle n20'],'new_reruns':['T24 n16','Q24 n16'],
                     'other_twelve_suite_rerun_in_this_audit':False,'papers_read':False,'BNT_executed':False,'ZN_executed':False,
                     'reference_is_certified':False,'producer_imported_on_comparison_side':True}}
    for name,n in [('rotpi4',24),('triangle',20)]:
        result['independent_cases'].append(independent_case(up,name,n))
    result['compatibility']={v:json.loads((work/('numpy'+v+'-probe.json')).read_text()) for v in ['240','241']}
    result['all_numerical_checks_pass']=result['response_comparison']['all_equal'] and result['grids16_comparison']['all_equal'] and all(c['diagnostic_pass'] for c in result['independent_cases'])
    Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'all_numerical_checks_pass':result['all_numerical_checks_pass'],'response_leaves':result['response_comparison']['leaf_count'],'grids16_leaves':result['grids16_comparison']['leaf_count'],'independent_cases':[{k:c[k] for k in ['name','gap_absolute_difference','normalized_basis_max_abs_difference','independent_truth_vs_producer','diagnostic_pass']} for c in result['independent_cases']]}))


if __name__=='__main__':
    main()
