#!/usr/bin/env python3
"""Independent L4 artifact/Gram checker; no imports from the proposed producer.
Full source regeneration is a separate, recorded invocation, not this checker.
"""
import argparse, gzip, hashlib, json, pathlib, platform, sys, time
import flint
from flint import fmpq as Q, fmpq_mat as Mat
PRODUCER='0da27e69ddd3cff5ca23e3fcac764f53891ad164ffab20324540fd67d2faf901'
PINS={'e1-scalar-cgs2.json':'e215556a01f9e169163b228dfe1b984d28e0cebd7f78e0d858f9a61a0de878c8','e1-multinode-certificates.json':'fae9c8743c78230ef0aa82c185d1efe0eee37be066982a37d39d920af95719f0'}
def require(value, message):
    if not value: raise ValueError(message)
def sha(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for chunk in iter(lambda:f.read(1048576),b''):h.update(chunk)
    return h.hexdigest()
def identity(p):
    p=pathlib.Path(p);return {'path':str(p.resolve()),'bytes':p.stat().st_size,'sha256':sha(p)}
def artifact(a):
    p=pathlib.Path(a['path']);require(p.stat().st_size==a['bytes'] and sha(p)==a['sha256'],'artifact identity');return p
def header(h):
    require(h['schema']=='full-envelope-v1' and h['rows']==91 and h['nodes']==625,'dimensions/schema')
    require(h['sources']==list(range(1,91)),'all 90 sources required')
    d=list(map(Q,h['d']));require(len(d)==91 and all(x>0 for x in d),'positive norms');return d
def rowcheck(row,k):
    require(row['k']==k and len(row['values'])==625,'ordered full rows')
    values=list(map(Q,row['values']));require(all(x>=0 for x in values),'nonnegative envelope')
    if k==0:require(not any(values),'constant row zero')
    return values
def positive(v):require(len(v)==625 and all(type(x)==int and x>0 for x in v),'strictly positive full vector')
def bounded(z,v,B):require(all(z[i]<=B*v[i] for i in range(625)),'component upper inequality')
def witness_check(ownpath,devpath,lower,B,fixedpath):
    own=json.loads(pathlib.Path(ownpath).read_text());dev=json.loads(pathlib.Path(devpath).read_text())
    pin='9f56bf92aa5883aaf6895327044406b7fdccb57e3c26199391fcaf61d873d2cf'
    for r in [own,dev]:require(r['code_sha256']==pin and r['fixed_comparator_upper_integer']==B,'full witness source and comparator pins')
    bs=[];vs=[]
    with gzip.open(artifact(own['raw_full_witness']),'rt') as f,gzip.open(artifact(dev['raw_full_witness']),'rt') as g:
        h=json.loads(next(f));require(h==json.loads(next(g)),'full witness header regeneration')
        require(h['schema']=='full-old-witness-v1' and h['M']==625 and h['N']==91 and h['sources']==list(range(1,91)) and h['target']==90,'full witness scope')
        require(h['node_signs']==lower['node_signs'],'unchanged old node signs')
        d=list(map(Q,h['d']));require(len(d)==91 and all(x>0 for x in d),'witness norms')
        for k in range(91):
            r=json.loads(next(f));require(r==json.loads(next(g)),'full witness entry regeneration')
            require(r['k']==k and len(r['b'])==len(r['V'])==625,'full witness ordered dimensions')
            bs.append(list(map(Q,r['b'])));vs.append(list(map(Q,r['V'])))
        require(not f.read() and not g.read(),'all full witness rows')
    require(not any(vs[0]),'constant witness zero')
    # Certify the projection data themselves: exact orthogonality and all norms.
    BM=Mat(bs);gram=BM*BM.transpose()
    require(all(gram[i,j]==(d[i] if i==j else 0) for i in range(91) for j in range(91)),'exact basis Gram diagonal')
    def projected_gain(t):
        require(len(t)==91 and t[0]==0 and any(t[1:]),'nonzero nonconstant readout')
        y=[sum((Q(tk)*row[i] for tk,row in zip(t,vs) if tk),Q(0)) for i in range(625)]
        # Orthogonal subtraction of energies is independent of producer's projected-vector norm.
        energy=sum((x*x for x in y),Q(0))
        removed=sum((sum((x*b for x,b in zip(y,row)),Q(0))**2/dk for row,dk in zip(bs,d)),Q(0))
        den=sum((dk*tk*tk for dk,tk in zip(d,t)),Q(0));num=energy-removed
        require(den>0 and num>=0,'projected quotient signs')
        return num/den,den
    control,den=projected_gain([0]*90+[1]);G=Q(lower['explicit_greedy_sign_lower_squared']['exact']);require(control==G,'old target exact control')
    results=[];trials=dev['readouts'];require(1<=len(trials)<=3,'bounded full witness proposals')
    require([r['scale'] for r in trials]==[10**6,10**9,10**12][:len(trials)],'registered quantization order')
    for r in trials:
        c=json.loads(artifact(r['artifact']).read_text())
        t=c['monic_coefficients'];require(all(type(x)==int for x in t),'integer readout')
        gain,den=projected_gain(t);floor=int(gain.numerator)//int(gain.denominator)
        require(gain==Q(c['lower_exact']) and den==Q(c['denominator_exact']) and floor==c['lower_integer_floor'],'exact full witness gain')
        passed=bool(gain>100*B);require(passed==c['pass_exact'] and bool(floor>100*B)==c['pass_integer_floor'],'full witness strict comparison')
        results.append({'scale':c['scale'],'gain_display':float(gain),'floor':floor,'exact_gain_sha256':hashlib.sha256(str(gain).encode()).hexdigest(),'exact_pass':passed,'integer_floor_pass':bool(floor>100*B)})
    fixed=json.loads(pathlib.Path(fixedpath).read_text())
    require(fixed['producer_code_sha256']==pin and fixed['comparator_upper_integer_B']==B,'fixed certificate scope')
    require(fixed['frozen_node_sign_source']['sha256']==PINS['e1-multinode-certificates.json'],'fixed frozen sign source')
    require(hashlib.sha256(json.dumps(lower['node_signs'],separators=(',',':')).encode()).hexdigest()==fixed['node_signs_canonical_json_sha256'],'fixed node sign identity')
    recorded=json.loads(artifact(fixed['extracted_from']).read_text());require(fixed['monic_coefficients']==recorded['monic_coefficients'],'faithful fixed vector extraction')
    require(artifact(fixed['original_producer_receipt']).resolve()==pathlib.Path(devpath).resolve(),'fixed original producer receipt')
    require(all(type(x)==int for x in fixed['monic_coefficients']),'fixed integer vector')
    fixed_gain,_=projected_gain(fixed['monic_coefficients']);L=fixed['readout_lower_integer_floor_L']
    require(L<=fixed_gain<L+1 and L>100*B,'fixed exact lower certificate')
    require(hashlib.sha256(str(fixed_gain).encode()).hexdigest()==fixed['exact_readout_value_sha256'],'fixed exact quotient hash')
    controls=[]
    for name,fn in [('zero full-output readout',lambda:projected_gain([0]*91)),('nonzero constant readout',lambda:projected_gain([1]+[0]*89+[1])),('inflated attained lower',lambda:require(Q(trials[-1]['lower_integer_floor'])+1<=gain,'outward lower'))]:
        try:fn()
        except ValueError:controls.append({'name':name,'result':'REJECTED'})
        else:raise RuntimeError('witness malformed control accepted: '+name)
    return {'result':'INDEPENDENT_FULL_OUTPUT_CERTIFICATE_PASSES' if any(r['exact_pass'] for r in results) else 'INDEPENDENT_FULL_OUTPUT_INCONCLUSIVE','producer_sha256':pin,'regeneration_receipt':identity(ownpath),'developer_receipt':identity(devpath),'raw_full_witness':own['raw_full_witness'],'exact_full_witness_matches_developer':True,'exact_basis_Gram_diagonal':True,'exact_old_target_projection_reproduced':True,'independent_projection_formula':'||Vt||^2 - sum_l (b_l dot Vt)^2/d_l; denominator sum_k d_k t_k^2','fixed_readout_certificate':identity(fixedpath),'fixed_vector_checked_independently_of_new_float_proposal':True,'fixed_lower_integer_L':L,'fixed_exact_L_le_Q_lt_L_plus_one':True,'fixed_exact_L_gt_100B':True,'fixed_alt_upper_B':B,'strict_squared_threshold':100*B,'readouts':results,'malformed_controls':controls,'scope':'Same frozen formal scalar witness, all90sources/outputs; no new delta sign search or actual IEEE assertion.'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--regeneration',required=True);ap.add_argument('--developer',required=True);ap.add_argument('--frozen-evidence',required=True);ap.add_argument('--bj-reproduction',required=True);ap.add_argument('--output',required=True);ap.add_argument('--witness-regeneration');ap.add_argument('--witness-developer');ap.add_argument('--fixed-certificate');a=ap.parse_args();start=time.monotonic()
    own=json.loads(pathlib.Path(a.regeneration).read_text());dev=json.loads(pathlib.Path(a.developer).read_text())
    for r in [own,dev]:require(r['code_sha256']==PRODUCER,'producer source pin')
    ev=pathlib.Path(a.frozen_evidence)
    for name,h in PINS.items():require(sha(ev/name)==h,'frozen evidence pin')
    old=json.loads((ev/'e1-scalar-cgs2.json').read_text());low=json.loads((ev/'e1-multinode-certificates.json').read_text())
    oldrow=next(r for r in old['full_graph_upper_runs'] if r['set']=='rotated' and r['rule']=='alt')
    lower=next(r for r in low['witnesses'] if r['set']=='rotated' and r['rule']=='bj')
    require(oldrow['degree']==lower['degree']==12 and oldrow['source_count']==90,'frozen scope')
    T=Q(oldrow['upper_squared']['exact']);G=Q(lower['explicit_greedy_sign_lower_squared']['exact'])
    p=artifact(own['envelope']);dp=artifact(dev['envelope']);S=[];streamhash=hashlib.sha256()
    with gzip.open(p,'rt') as f,gzip.open(dp,'rt') as g:
        h=json.loads(next(f));dh=json.loads(next(g));require(h==dh,'regenerated header equality');d=header(h)
        streamhash.update(json.dumps(h,sort_keys=True,separators=(',',':')).encode())
        for k in range(91):
            r=json.loads(next(f));dr=json.loads(next(g));require(r==dr,'regenerated envelope row equality')
            S.append(rowcheck(r,k));streamhash.update(json.dumps(r,sort_keys=True,separators=(',',':')).encode())
        require(not f.read() and not g.read(),'no omitted or extra rows')
    trace=sum((sum((x*x for x in row),Q(0))/dk for row,dk in zip(S,d)),Q(0));require(trace==T,'full frozen Frobenius equality')
    bj=json.loads(pathlib.Path(a.bj_reproduction).read_text())
    require(bj['result']=='PASS' and bj['set']=='rotated' and bj['explicit_projection_check']['result']=='PASS','fresh BJ reproduction')
    require(bj['certificate_sha256']==PINS['e1-multinode-certificates.json'] and bj['source_record_sha256']==PINS['e1-scalar-cgs2.json'],'BJ frozen pins')
    require(bj['generator_sha256']==lower['code_sha256'],'BJ generator pin')
    # Check every proposed vector using exact products; never trust receipt booleans.
    M=Mat(S);MT=M.transpose();results=[];best=None;proposal_equalities=[]
    require([r['step'] for r in own['candidates']]==list(range(9)),'nine bounded proposals')
    require(len(dev['candidates'])==9,'developer proposal count')
    for rec,devrec in zip(own['candidates'],dev['candidates']):
        newproposal=json.loads(artifact(rec['candidate']).read_text());cert=json.loads(artifact(devrec['candidate']).read_text())
        proposal_equalities.append(newproposal==cert);v=cert['v'];positive(v)
        w=M*Mat([[x] for x in v]);zm=MT*Mat([[w[k,0]/d[k]] for k in range(91)]);z=[zm[i,0] for i in range(625)]
        U=max(z[i]/v[i] for i in range(625));B=-((-int(U.numerator))//int(U.denominator))
        require(U==Q(cert['U_exact']) and B==cert['U_integer_upper'],'exact proposed bound');bounded(z,v,B)
        require(z[cert['maximizing_node']]/v[cert['maximizing_node']]==U,'maximum attained')
        passed=bool(100*U<G);rounded=bool(100*B<G)
        require(passed==devrec['pass_exact_100U_lt_G'] and rounded==cert['pass_100_integer_upper_lt_G'],'honest comparison')
        results.append({'step':cert['step'],'B':B,'U_sha256':hashlib.sha256(str(U).encode()).hexdigest(),'exact_100U_lt_G':passed,'exact_100B_lt_G':rounded})
        if best is None or U<best[0]:best=(U,B,v,z,cert['step'])
    U,B,v,z,step=best
    # A distinct scalar-loop formulation verifies the consequential best Gram product.
    sw=[sum((s*x for s,x in zip(row,v)),Q(0))/dk for row,dk in zip(S,d)]
    sz=[sum((S[k][i]*sw[k] for k in range(91)),Q(0)) for i in range(625)]
    require(sz==z,'independent scalar-loop Gram product')
    rayleigh=sum((Q(x)*y for x,y in zip(v,z)),Q(0))/sum(x*x for x in v)
    rayleigh_floor=int(rayleigh.numerator)//int(rayleigh.denominator)
    require(rayleigh_floor<=rayleigh<rayleigh_floor+1 and 100*rayleigh_floor>=G,'compact exact Rayleigh obstruction')
    controls=[]
    def reject(name,fn):
        try:fn()
        except (ValueError,KeyError,IndexError):controls.append({'name':name,'result':'REJECTED'});return
        raise RuntimeError('malformed control accepted: '+name)
    reject('missing source despite valid dimensions',lambda:header(dict(h,sources=h['sources'][:-1])))
    bad_d=list(h['d']);bad_d[1]='0';reject('zero norm',lambda:header(dict(h,d=bad_d)))
    reject('negative envelope entry',lambda:rowcheck({'k':1,'values':['-1']+['0']*624},1))
    reject('nonzero constant response',lambda:rowcheck({'k':0,'values':['1']+['0']*624},0))
    reject('missing response row',lambda:rowcheck({'k':2,'values':['0']*625},1))
    reject('zero vector coordinate',lambda:positive([0]+v[1:]))
    reject('one unit underestimated outward bound',lambda:bounded(z,v,B-1))
    reject('false factor ten acceptance',lambda:require(100*B<G,'strict comparison'))
    k,i=next((k,i) for k,row in enumerate(S) for i,x in enumerate(row) if x>0)
    omitted_trace=trace-S[k][i]**2/d[k]
    reject('omitted positive envelope entry with full-source header',lambda:require(omitted_trace==T,'frozen trace'))
    bad_art=dict(own['envelope'],sha256='0'*64);reject('artifact hash mismatch',lambda:artifact(bad_art))
    result={'result':'INDEPENDENTLY_VERIFIED_INCONCLUSIVE','scope':{'set':'rotated Q24','degree':12,'rule':'alt','nodes':625,'columns':91,'full_sources':90,'model':'PD-T138 full formal scalar relative-error CGS2'},'producer_sha256':PRODUCER,'independent_checker':identity(__file__),'regeneration_receipt':identity(a.regeneration),'developer_receipt':identity(a.developer),'regenerated_envelope':own['envelope'],'canonical_envelope_sha256':streamhash.hexdigest(),'exact_full_envelope_matches_developer':True,'regenerated_power_proposal_equality_diagnostic':proposal_equalities,'saved_rational_upper_vectors_verified_independently_of_new_float_proposals':True,'exact_old_frobenius_reproduced':True,'old_frobenius_display':float(T),'G_R_display':float(G),'old_G_over_trace_display':float(G/T),'fresh_BJ_reproduction':identity(a.bj_reproduction),'BJ_checks':bj,'candidates':results,'best_step':step,'best_B':B,'best_U_display':float(U),'best_Gram_product_scalar_loop_agrees':True,'rayleigh_diagnostic':{'value_display':float(rayleigh),'exact_integer_floor':rayleigh_floor,'exact_floor_le_R_lt_floor_plus_one':True,'exact_100_floor_ge_G_R':bool(100*rayleigh_floor>=G),'exact_value_sha256':hashlib.sha256(str(rayleigh).encode()).hexdigest(),'exact_100_Rayleigh_gt_G_R':bool(100*rayleigh>G),'scope':'Obstruction only to this fixed absolute envelope with this frozen BJ lower; not to true scalar capacities or the target.'},'malformed_controls':controls,'command':[sys.executable,'-B',str(pathlib.Path(__file__).resolve()),*sys.argv[1:]],'runtime':{'python':platform.python_version(),'flint':flint.__version__,'elapsed_seconds':time.monotonic()-start},'limitations':['Same approved producer independently executed; checker is a separately written implementation, not a second derivation of the inherited scalar graph.','Exact arithmetic trusts Python/FLINT and inherited proved reduction.','L4a with old BJ lower and the original PD-T140 experiment remain inconclusive; L4b is an additive result.','Large external artifacts are temporary and require archival or regeneration.','Separate Claude scientific/protocol audit remains pending.']}
    require(not any(r['exact_100U_lt_G'] for r in results),'unexpected positive certificate requires new review')
    if a.witness_regeneration or a.witness_developer:
        require(bool(a.witness_regeneration and a.witness_developer and a.fixed_certificate),'both witness receipts and fixed certificate required')
        result['L4a_result']=result['result']
        result['L4b']=witness_check(a.witness_regeneration,a.witness_developer,lower,B,a.fixed_certificate)
        if result['L4b']['result']=='INDEPENDENT_FULL_OUTPUT_CERTIFICATE_PASSES':result['result']='INDEPENDENT_FINITE_FACTOR_TEN_PASSES'
        result['runtime']['elapsed_seconds']=time.monotonic()-start
    pathlib.Path(a.output).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'result':result['result'],'best_B':B,'rayleigh_obstruction':bool(100*rayleigh>G),'controls':len(controls),'elapsed':time.monotonic()-start}))
if __name__=='__main__':main()
