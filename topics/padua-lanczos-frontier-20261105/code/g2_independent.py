#!/usr/bin/env python3
"""Independent finite G2 W pulse check; no R trace or asymptotic inference.
Only the pinned exact baseline builder is shared with the producer.
"""
import argparse, hashlib, json, pathlib, platform, sys, time
import flint
from flint import fmpq as Q, fmpq_mat as Mat
ROOT=pathlib.Path(__file__).resolve().parents[3]
BASE=ROOT/'tracks/bivariate-lanczos/code/drift/e1_exact.py'
PIN='19ce7b774e5a6fa56108eebca3b2ef81f5237328e518d95225adf9f8835e060f'

def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def qhash(q): return hashlib.sha256(str(q).encode()).hexdigest()
def dot(u,v): return (u*v.transpose())[0,0]
def mul(u,x): return Mat([[u[0,i]*x[i] for i in range(len(x))]])
def row(A,k): return Mat([[A[k,i] for i in range(A.ncols())]])
def rows(v): return Mat([[u[0,i] for i in range(u.ncols())] for u in v])
def block(A,count): return Mat([[A[k,i] for i in range(A.ncols())] for k in range(count)])
def diag(vals):
    A=Mat(len(vals),len(vals))
    for i,v in enumerate(vals): A[i,i]=v
    return A

def normal(v,b,d):
    out=v
    for z,dk in zip(b,d): out=out-dot(v,z)/dk*z
    return out

def projector(B,d): return B.transpose()*diag([1/z for z in d])*B

def projector_derivative(B,d,W):
    # Differentiate B^T (B B^T)^(-1) B before simplifying any term.
    Di=diag([1/z for z in d]); dGram=W*B.transpose()+B*W.transpose()
    return W.transpose()*Di*B+B.transpose()*Di*W-B.transpose()*Di*dGram*Di*B

def derivative_run(coords, b, rec, inputs, vary):
    M=len(coords[0]); out=[Mat(1,M)]
    for k in range(1,len(b)):
        axis,parent,alpha,_=rec[k]
        v=mul(out[parent],coords[axis])+inputs[k]
        for l,c in enumerate(alpha): v=v-c*out[l]
        # h_k=-b_k-b_0 is simultaneously a permissible beta derivative
        # and a c_(k,0) derivative, in the fixed monic conversion.
        if vary: v=v-b[k]-b[0]
        out.append(v)
    return out

def small_controls(ex, check_trace=False):
    points=[(Q(x),Q(y)) for x in (-1,0,1) for y in (-1,0,1)]
    xy,b,d,rec,meta=ex.build(points,2,'bj'); M,N=9,6
    F=[Mat(1,M)]+[Mat([[Q((k+2*i)%7-3,5) for i in range(M)]]) for k in range(1,N)]
    w=derivative_run(xy,b,rec,F,False); alt=derivative_run(xy,b,rec,F,True)
    X=diag(xy[0]); I=diag([Q(1)]*M); checks=[]
    for s in (0,1):
        ns=(s+1)*(s+2)//2; nt=(s+2)*(s+3)//2
        Bs=rows(b[:ns]); Bt=rows(b[:nt]); ds=d[:ns]; dt=d[:nt]
        Ps=projector(Bs,ds); Pt=projector(Bt,dt); R=I-Pt
        assert Ps*Ps==Ps and Pt*Pt==Pt and R*X*Ps==Mat(M,M)
        dPs=projector_derivative(Bs,ds,rows(w[:ns])); dPt=projector_derivative(Bt,dt,rows(w[:nt]))
        aPs=projector_derivative(Bs,ds,rows(alt[:ns])); aPt=projector_derivative(Bt,dt,rows(alt[:nt]))
        assert dPs==aPs and dPt==aPt
        for k in range(nt): assert normal(alt[k]-w[k],b[:nt],dt)==Mat(1,M)
        direct=-dPt*X*Ps+R*X*dPs
        C=diag([1/z for z in dt])*Bt*X*Bs.transpose()
        monic=R*(X*rows(w[:ns]).transpose()-rows(w[:nt]).transpose()*C)
        reconstructed=monic*diag([1/z for z in ds])*Bs
        assert direct==reconstructed
        assert direct==-aPt*X*Ps+R*X*aPs
        if s==1:
            # Meaningful malformed derivative controls: each missing projector
            # term changes this fixed nontrivial test instance.
            assert direct!=R*X*dPs
            assert direct!=-dPt*X*Ps
            assert direct!=dPt*X*Ps+R*X*dPs
        checks.append({'stage':s,'direct_projector_derivative_equal':True,'alternative_beta_and_coefficient_derivatives_equal':True})
    trace_control=None
    if check_trace:
        # Brute-force all45 monic source/node directions in the small model.
        # Differentiate full projectors, independently of the omega trace.
        brute=Q(0); formula=Q(0)
        for h in range(1,N):
            gh=selected_response(xy,rec,h)
            for s in (0,1):
                ns=(s+1)*(s+2)//2; nt=(s+2)*(s+3)//2
                Bs=rows(b[:ns]); Bt=rows(b[:nt]); ds=d[:ns]; dt=d[:nt]
                Ps=projector(Bs,ds); Pt=projector(Bt,dt); R=I-Pt
                C=diag([1/z for z in dt])*Bt*X*Bs.transpose()
                Om=rows([mul(z,xy[0]) for z in gh[:ns]])-C.transpose()*rows(gh[:nt])
                for i in range(M):
                    inputs=[Mat(1,M) for _ in range(N)]; inputs[h][0,i]=1
                    z=derivative_run(xy,b,rec,inputs,False)
                    p1=projector_derivative(Bs,ds,rows(z[:ns])); p2=projector_derivative(Bt,dt,rows(z[:nt]))
                    derivative=-p2*X*Ps+R*X*p1
                    brute+=rec[h][3]*sum((derivative[j,k]**2 for j in range(M) for k in range(M)),Q(0))
                    formula+=rec[h][3]*R[i,i]*sum((Om[j,i]**2/d[j] for j in range(ns)),Q(0))
        assert brute==formula and brute>0
        expected=brute/((N-1)*M*max(x*x for x in xy[0]))
        trace_control={'all_source_node_directions':(N-1)*M,'all_stages':[0,1],'dense_projector_trace_equals_omega_trace':True,'expectation_exact':str(expected),'global_denominator':(N-1)*M,'not_a_degree12_result':True}
    return {'small_full_trace_control':trace_control,'grid':'3x3 rational product' ,'degree':2,'stages':checks,'rejected_controls':['omit next-projector derivative','omit current-projector derivative','reverse next-projector sign'],'scope':'exact finite derivative controls; no n12 threshold decision'}

def selected_response(coords, rec, h):
    N=len(rec); M=len(coords[0]); g=[Mat(1,M) for _ in range(N)]; g[h]=Mat([[1]*M])
    for k in range(h+1,N):
        axis,parent,alpha,_=rec[k]
        v=mul(g[parent],coords[axis])
        for l,c in enumerate(alpha):
            if c: v=v-c*g[l]
        g[k]=v
    return g

def pulse_direct(coords,b,d,rec,g,C,h,i,ell):
    """Actual two-projector derivative applied to every monic prefix column.
    Uses F_h=e_i first, then multiplies the squared gain by tau_h^2.
    This does not use omega or the diagonal projector formula.
    """
    N=len(b); ns=78; M=len(coords[0]); e=Mat(1,M); e[0,i]=1
    rs=normal(e,b[:ns],d[:ns]); rt=normal(e,b,d)
    ts=Mat(1,M); tt=Mat(1,M)
    for k in range(N):
        tt=tt+(g[k][0,i]/d[k])*b[k]
        if k<ns: ts=ts+(g[k][0,i]/d[k])*b[k]
    # Pdot = r*t^T+t*r^T in column notation.
    Rxrs=normal(mul(rs,coords[0]),b,d); Rxts=normal(mul(ts,coords[0]),b,d)
    total=Q(0); minus_nonzero=False; plus_nonzero=False
    for j in range(ns):
        xb=mul(b[j],coords[0])
        minus=-dot(tt,xb)*rt-dot(rt,xb)*tt
        plus=dot(ts,b[j])*Rxrs+dot(rs,b[j])*Rxts
        out=minus+plus
        minus_nonzero |= minus!=Mat(1,M); plus_nonzero |= plus!=Mat(1,M)
        # Separate direct frozen closure evaluation, with full expansion.
        direct=mul(e,coords[0])*g[j][0,i]
        for k in range(N):
            if C[k,j]: direct=direct-C[k,j]*g[k][0,i]*e
        direct=normal(direct,b,d)
        assert out==direct
        total+=dot(out,out)/d[j]
    tau=rec[h][3]
    assert tau*total==ell
    assert dot(rt,rt)==rt[0,i] and dot(rs,rs)==rs[0,i]
    # f_h=sigma_h e_i has total relative source norm exactly1 over all90;
    # F_h=tau_h e_i. Square roots need not be rounded or stored.
    parent=rec[h][1]; sigma2=dot(mul(b[parent],coords[rec[h][0]]),mul(b[parent],coords[rec[h][0]]))/d[parent]
    assert sigma2==tau/d[parent] and sigma2>0 and (d[parent]*sigma2)/tau==1
    return {'actual_two_projector_derivative_squared_equal':True,'direct_frozen_closure_squared_equal':True,'current_projector_term_nonzero':bool(plus_nonzero),'next_projector_term_nonzero':bool(minus_nonzero),'global_source_count':90,'nonzero_source_count':1,'source_budget_squared_exact':'1','sigma_squared_sha256':qhash(sigma2),'tau_squared_sha256':qhash(tau)}

def fixed_check(cert, grid, M, xnorm, record, value, partial):
    assert cert['frozen_source_sha256']==PIN
    theorem=ROOT/'topics/padua-lanczos-frontier-20261105/theory/l2-smooth-rule-closure-reduction.md'
    assert cert['analytic_reduction_sha256']==sha(theorem)
    assert cert['saved_predicates']['W_squared_threshold']==65536
    assert cert['saved_predicates']['R_threshold']==16
    cases=[c for c in cert['cases'] if c['set']==grid]; assert len(cases)==1
    c=cases[0]
    for key,expected in [('degree',12),('rule','bj'),('stage',11),('source',6),('source_degree_index',[3,0]),('global_source_count',90),('global_node_count',M),('R_partial_node_coverage',M)]:
        assert c[key]==expected
    assert c['W_fixed_node']==record['node'] and c['W_fixed_point']==record['point']
    assert Q(c['Xnorm_squared_exact'])==xnorm
    assert Q(c['R_global_denominator_exact'])==90*M*xnorm
    lo=c['W_squared_lower_integer_floor']; lr=c['R_partial_expectation_lower_integer_floor']
    assert isinstance(lo,int) and isinstance(lr,int)
    assert lo<=value<lo+1 and lr<=partial<lr+1
    assert lo>=65536 and lr>=16
    return True

def fixed_controls(cert, grid, M, xnorm, record, value, partial):
    assert fixed_check(cert,grid,M,xnorm,record,value,partial)
    tests=[('global_source_count',1),('R_global_denominator_exact',str(M*xnorm)),('W_fixed_node',(record['node']+1)%M)]
    original=next(c for c in cert['cases'] if c['set']==grid)
    tests += [('W_squared_lower_integer_floor',original['W_squared_lower_integer_floor']+1),('R_partial_expectation_lower_integer_floor',original['R_partial_expectation_lower_integer_floor']+1)]
    rejected=[]
    for key,badvalue in tests:
        bad=json.loads(json.dumps(cert)); next(c for c in bad['cases'] if c['set']==grid)[key]=badvalue
        try: fixed_check(bad,grid,M,xnorm,record,value,partial)
        except AssertionError: rejected.append(key)
        else: raise AssertionError('malformed fixed certificate accepted: '+key)
    # Metadata describing historic receipts is unnecessary for mathematics.
    stripped={k:v for k,v in cert.items() if k in ['frozen_source_sha256','analytic_reduction_sha256','saved_predicates','cases']}
    assert fixed_check(stripped,grid,M,xnorm,record,value,partial)
    return {'fixed_mathematical_data_verified':True,'malformed_fixed_fields_rejected':rejected,'historical_top_level_lineage_removed_successfully':True}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--set',choices=['triangle','rotated'],required=True); ap.add_argument('--output',required=True); ap.add_argument('--exact-output',required=True); ap.add_argument('--fixed-certificate'); ap.add_argument('--partial-r',action='store_true',help='prospectively recorded h6/s11 lower for unchanged full sign law'); args=ap.parse_args()
    started=time.monotonic(); assert sha(BASE)==PIN
    sys.path.insert(0,str(BASE.parent)); import e1_exact as ex
    controls=small_controls(ex,args.partial_r)
    points=ex.points(args.set); coords,b,d,rec,metadata=ex.build(points,12,'bj'); M=len(points); N=len(b); ns=78
    assert N==91 and M==({'triangle':325,'rotated':625}[args.set]) and len(rec)==N and all(z>0 for z in d)
    B=rows(b); Gram=B*B.transpose(); assert Gram==diag(d)
    XB=rows([mul(z,coords[0]) for z in b[:ns]])
    C=diag([1/z for z in d])*B*XB.transpose()
    assert B.transpose()*C==XB.transpose()
    xnorm=max(x*x for x in coords[0]); assert xnorm==({'triangle':Q(1),'rotated':Q(49,25)}[args.set])
    rd=[Q(1)-sum((b[k][0,i]**2/d[k] for k in range(N)),Q(0)) for i in range(M)]
    assert min(rd)>=0 and max(rd)<=1 and sum(rd)==M-N
    print(json.dumps({'event':'independent_basis_controls','set':args.set,'seconds':time.monotonic()-started}),flush=True)
    screens=[]; winning=None; partial_r=None; partial_value=None; fixed=None
    assert not args.fixed_certificate or args.partial_r
    for h in (6,4,3,5):
        g=selected_response(coords,rec,h)
        # Construct the entire closure-response matrix by exact multiplication;
        # node columns are independent. No producer omega routine is imported.
        Xg=rows([mul(z,coords[0]) for z in g[:ns]])
        Omega=Xg-C.transpose()*rows(g)
        gains=[]
        for i in range(M):
            gains.append(rec[h][3]*rd[i]*sum((Omega[j,i]**2/d[j] for j in range(ns)),Q(0)))
        if args.partial_r and h==6:
            partial_value=sum(gains,Q(0))/(90*M*xnorm)
            partial_r={'stage':11,'source':6,'all_nodes':M,'global_source_count':90,'global_variance_denominator':90*M,'xnorm_squared_exact':str(xnorm),'partial_lower_floor':int(partial_value.numerator)//int(partial_value.denominator),'partial_lower_sha256':qhash(partial_value),'threshold':16,'result':'EXACT_R_LOWER_PASSES' if partial_value>=16 else 'INCONCLUSIVE_LOWER','full_expectation_computed':False,'omitted_trace_terms_nonnegative':True}
        i=max(range(M),key=lambda k:gains[k]); ell=gains[i]; value=ell/xnorm
        record={'stage':11,'source':h,'node':i,'point':[str(z) for z in points[i]],'all_node_count':M,'squared_capacity_lower_floor':int(value.numerator)//int(value.denominator),'exact_lower_sha256':qhash(value),'threshold_squared':65536,'passes':bool(value>=65536)}
        screens.append(record); print(json.dumps({'event':'independent_screen',**record,'seconds':time.monotonic()-started}),flush=True)
        if record['passes']:
            direct=pulse_direct(coords,b,d,rec,g,C,h,i,ell)
            if args.fixed_certificate:
                cert=json.loads(pathlib.Path(args.fixed_certificate).read_text())
                fixed=fixed_controls(cert,args.set,M,xnorm,record,value,partial_value)
                fixed['certificate_sha256']=sha(args.fixed_certificate)
            exact={'set':args.set,'stage':11,'source':h,'node':i,'ell_exact':str(ell),'xnorm_squared_exact':str(xnorm),'normalized_lower_squared_exact':str(value),'normal_diagonal_exact':str(rd[i]),'tau_squared_exact':str(rec[h][3]),'omega_at_node':[str(Omega[j,i]) for j in range(ns)],'d_prefix':[str(z) for z in d[:ns]],'partial_R_lower_exact':str(partial_value) if partial_value is not None else None,'all_node_ell':[str(z) for z in gains] if args.partial_r and h==6 else None}
            exactpath=pathlib.Path(args.exact_output); exactpath.parent.mkdir(parents=True,exist_ok=True); exactpath.write_text(json.dumps(exact,indent=2)+'\n')
            winning={'screen':record,'direct_controls':direct,'exact_artifact':{'path':str(exactpath),'bytes':exactpath.stat().st_size,'sha256':sha(exactpath)}}
            break
    receipt={'schema':'g2-independent-W-pulse-v1','code_sha256':sha(__file__),'baseline_builder_sha256':PIN,'model':'saved R_smooth aggregate normalized raw sources; finite uniform-grid reduction','set':args.set,'degree':12,'M':M,'N':N,'global_source_columns':list(range(1,91)),'screen_order':[6,4,3,5],'result':'EXACT_W_LOWER_PASSES' if winning else 'INCONCLUSIVE_SCREEN','winning':winning,'screens':screens,'basis_controls':{'full_Gram_exact':True,'full_X_expansion_exact':True,'normal_trace_exact':str(sum(rd)),'positive_pivots':True,'positive_source_scales':all(r[3]>0 for r in rec[1:])},'small_degree_controls':controls,'fixed_certificate_controls':fixed,'R_partial_lower':partial_r,'R_status':'PARTIAL LOWER ONLY; full expectation not computed' if args.partial_r else 'NOT COMPUTED','limits':['One exact source pulse lower for W; no all-source upper. Optional R partial trace is only a lower for the unchanged full law.','No all-degree L2 result, SH_n extension, finite-epsilon or IEEE assertion.','Independent execution shares pinned baseline builder only; no producer import.'],'runtime':{'python':platform.python_version(),'python_flint':flint.__version__,'seconds':time.monotonic()-started},'command':[sys.executable,'-B',str(pathlib.Path(__file__).resolve()),*sys.argv[1:]]}
    out=pathlib.Path(args.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(receipt,indent=2)+'\n'); print(json.dumps({'event':'complete','result':receipt['result'],'seconds':time.monotonic()-started}),flush=True)
if __name__=='__main__': main()
