#!/usr/bin/env python3
"""Portable exact certificate check from fresh arrays and committed fixed vectors.
Historical developer artifacts, receipts, extraction paths and proposal vectors
are deliberately never opened. Independently rerun approved producers first.
"""
import argparse, gzip, hashlib, json, pathlib, platform, sys, time
import flint
from flint import fmpq as Q, fmpq_mat as Mat
ROOT=pathlib.Path(__file__).resolve().parents[3]
SOURCES={'e1_exact.py':'19ce7b774e5a6fa56108eebca3b2ef81f5237328e518d95225adf9f8835e060f','e1_cgs2.py':'426630eb916e13bb14409f6f7b8ea310eaeb1bf7949de10866d163aad31c7b4b'}
FROZEN={'e1-scalar-cgs2.json':'e215556a01f9e169163b228dfe1b984d28e0cebd7f78e0d858f9a61a0de878c8','e1-multinode-certificates.json':'fae9c8743c78230ef0aa82c185d1efe0eee37be066982a37d39d920af95719f0'}
UPPER_CODE='0da27e69ddd3cff5ca23e3fcac764f53891ad164ffab20324540fd67d2faf901'
LOWER_CODE='9f56bf92aa5883aaf6895327044406b7fdccb57e3c26199391fcaf61d873d2cf'
def check(value,why):
    if not value:raise ValueError(why)
def sha(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for chunk in iter(lambda:f.read(1048576),b''):h.update(chunk)
    return h.hexdigest()
def ident(path):
    p=pathlib.Path(path);return {'path':str(p.resolve()),'bytes':p.stat().st_size,'sha256':sha(p)}
def fresh_artifact(meta):
    p=pathlib.Path(meta['path']);check(p.stat().st_size==meta['bytes'] and sha(p)==meta['sha256'],'fresh artifact integrity');return p
def upper_vector(v):check(len(v)==625 and all(type(x)==int and x>0 for x in v),'positive625vector')
def lower_vector(t):check(len(t)==91 and all(type(x)==int for x in t) and t[0]==0 and any(t[1:]),'nonzero integer90readout')
def mathematical_certificate(c):
    # Only scientific data/pins are selected; lineage fields are not dependencies.
    upper_vector(c['upper_positive_vector']);lower_vector(c['lower_monic_coefficients'])
    check(type(c['upper_integer_B'])==type(c['lower_integer_floor_L'])==int,'integer endpoints')
    check(c['upper_integer_B']>0 and c['lower_integer_floor_L']>100*c['upper_integer_B'],'strict endpoint inequality')
    check(c['upper_producer_code_sha256']==UPPER_CODE and c['lower_producer_code_sha256']==LOWER_CODE,'approved producers')
    check(c['upper_producer_source_pins']==c['lower_producer_source_pins']==SOURCES and c['upper_frozen_evidence_pins']==FROZEN,'certificate source pins')
    return c['upper_positive_vector'],c['lower_monic_coefficients'],c['upper_integer_B'],c['lower_integer_floor_L']
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--certificate',required=True);ap.add_argument('--fresh-envelope-receipt',required=True);ap.add_argument('--fresh-witness-receipt',required=True);ap.add_argument('--frozen-evidence',required=True);ap.add_argument('--output',required=True);a=ap.parse_args();start=time.monotonic()
    c=json.loads(pathlib.Path(a.certificate).read_text());v,t,B,L=mathematical_certificate(c)
    er=json.loads(pathlib.Path(a.fresh_envelope_receipt).read_text());wr=json.loads(pathlib.Path(a.fresh_witness_receipt).read_text())
    check(er['code_sha256']==UPPER_CODE and wr['code_sha256']==LOWER_CODE,'fresh producer pins')
    check(er['source_sha256']==wr['source_sha256']==SOURCES and er['frozen_evidence_sha256']==FROZEN,'fresh input pins')
    check(er['scope']['rule']=='alt' and er['scope']['degree']==12 and wr['scope']['rule']=='bj' and wr['scope']['degree']==12,'fixed selections and degree')
    src=ROOT/'tracks/bivariate-lanczos/code/drift';ownsrc=pathlib.Path(__file__).parent
    for name,h in SOURCES.items():check(sha(src/name)==h,'current frozen code pin')
    for name,h in [('l4_envelope.py',UPPER_CODE),('l4_full_witness.py',LOWER_CODE)]:check(sha(ownsrc/name)==h,'approved current producer')
    ev=pathlib.Path(a.frozen_evidence)
    for name,h in FROZEN.items():check(sha(ev/name)==h,'actual frozen evidence pin')
    old=json.loads((ev/'e1-scalar-cgs2.json').read_text());low=json.loads((ev/'e1-multinode-certificates.json').read_text())
    orow=next(r for r in old['full_graph_upper_runs'] if r['set']=='rotated' and r['rule']=='alt')
    lrow=next(r for r in low['witnesses'] if r['set']=='rotated' and r['rule']=='bj')
    check(orow['degree']==lrow['degree']==12 and orow['source_count']==90 and lrow['target_column']==90,'frozen finite scope')
    G=Q(lrow['explicit_greedy_sign_lower_squared']['exact']);T=Q(orow['upper_squared']['exact']);check(G>0,'positive old lower')
    ep=fresh_artifact(er['envelope']);S=[]
    with gzip.open(ep,'rt') as f:
        h=json.loads(next(f));check(h['schema']=='full-envelope-v1' and h['rows']==91 and h['nodes']==625 and h['sources']==list(range(1,91)),'complete envelope schema')
        d=list(map(Q,h['d']));check(len(d)==91 and all(x>0 for x in d),'positive envelope norms')
        for k in range(91):
            row=json.loads(next(f));check(row['k']==k and len(row['values'])==625,'full envelope rows')
            values=list(map(Q,row['values']));check(all(x>=0 for x in values),'nonnegative envelope');S.append(values)
        check(not f.read() and not any(S[0]),'zero constant/no extra rows')
    trace=sum((sum((x*x for x in row),Q(0))/dk for row,dk in zip(S,d)),Q(0));check(trace==T,'old full Frobenius control')
    M=Mat(S);w=M*Mat([[x] for x in v]);zm=M.transpose()*Mat([[w[k,0]/d[k]] for k in range(91)]);z=[zm[i,0] for i in range(625)]
    def bound(b):check(all(zi<=b*vi for zi,vi in zip(z,v)),'exact upper component inequalities')
    bound(B)
    R=sum((zi*vi for zi,vi in zip(z,v)),Q(0))/sum(vi*vi for vi in v);rf=int(R.numerator)//int(R.denominator)
    check(rf==13462955378 and rf<=R<rf+1 and 100*rf>=G,'scoped exact Rayleigh floor')
    wp=fresh_artifact(wr['raw_full_witness']);bs=[];V=[]
    with gzip.open(wp,'rt') as f:
        h=json.loads(next(f));check(h['schema']=='full-old-witness-v1' and h['M']==625 and h['N']==91 and h['sources']==list(range(1,91)) and h['target']==90,'complete witness schema')
        check(h['node_signs']==lrow['node_signs'],'same frozen node signs')
        check(hashlib.sha256(json.dumps(h['node_signs'],separators=(',',':')).encode()).hexdigest()==c['node_signs_canonical_json_sha256'],'fixed sign hash')
        bd=list(map(Q,h['d']));check(len(bd)==91 and all(x>0 for x in bd),'positive witness norms')
        for k in range(91):
            row=json.loads(next(f));check(row['k']==k and len(row['b'])==len(row['V'])==625,'full witness rows')
            bs.append(list(map(Q,row['b'])));V.append(list(map(Q,row['V'])))
        check(not f.read() and not any(V[0]),'zero constant witness/no extra rows')
    BM=Mat(bs);gram=BM*BM.transpose();check(all(gram[i,j]==(bd[i] if i==j else 0) for i in range(91) for j in range(91)),'exact full basis Gram')
    def gain(x):
        lower_vector(x)
        y=[sum((Q(tk)*row[i] for tk,row in zip(x,V) if tk),Q(0)) for i in range(625)]
        energy=sum((yi*yi for yi in y),Q(0));removed=sum((sum((yi*bi for yi,bi in zip(y,row)),Q(0))**2/dk for row,dk in zip(bs,bd)),Q(0))
        den=sum((dk*tk*tk for dk,tk in zip(bd,x)),Q(0));check(energy>=removed and den>0,'projection quotient signs');return (energy-removed)/den
    check(gain([0]*90+[1])==G,'unchanged old target90 control');q=gain(t);check(L<=q<L+1 and L>100*B,'exact fixed lower and strict separation')
    # Proof acceptance depends on inequalities, not the original stored quotient hash.
    controls=[]
    def reject(name,fn):
        try:fn()
        except ValueError:controls.append({'name':name,'result':'REJECTED'});return
        raise RuntimeError('malformed fixed data accepted: '+name)
    reject('short upper vector',lambda:upper_vector(v[:-1]))
    reject('zero upper coordinate',lambda:upper_vector([0]+v[1:]))
    reject('underestimated upper B-1',lambda:bound(B-1))
    reject('zero lower readout',lambda:gain([0]*91))
    reject('nonzero constant readout',lambda:gain([1]+t[1:]))
    reject('inflated lower L+1',lambda:check(L+1<=q,'attained lower'))
    reject('equality instead of strict target',lambda:check(100*B>100*B,'strict inequality'))
    stripped={k:value for k,value in c.items() if not any(part in k for part in ['extracted_from','original_','exact_lower_readout','frozen_node_sign_source'])}
    check(mathematical_certificate(stripped)==(v,t,B,L),'lineage-free scientific certificate')
    result={'result':'PORTABLE_FIXED_CERTIFICATE_PASSES','checker':ident(__file__),'certificate':ident(a.certificate),'fresh_envelope_receipt':ident(a.fresh_envelope_receipt),'fresh_witness_receipt':ident(a.fresh_witness_receipt),'fresh_envelope':ident(ep),'fresh_witness':ident(wp),'source_sha256':SOURCES,'frozen_evidence_sha256':FROZEN,'full_source_count':90,'nodes':625,'columns':91,'full_Frobenius_exactly_reproduced':True,'all_Cv_le_Bv_exact':True,'B':B,'Rayleigh_integer_floor':rf,'exact_floor_le_R_lt_floor_plus_one':True,'exact_100_floor_ge_old_G':True,'exact_basis_Gram_diagonal':True,'old_target90_exactly_reproduced':True,'L':L,'exact_L_le_Q_lt_L_plus_one':True,'strict_L_gt_100B':True,'fixed_gain_sha256':hashlib.sha256(str(q).encode()).hexdigest(),'malformed_controls':controls,'lineage_fields_removed_control':'PASS; same mathematical certificate without historical artifact paths/identities','historical_artifacts_opened':False,'new_float_proposals_consulted':False,'command':[sys.executable,'-B',str(pathlib.Path(__file__).resolve()),*sys.argv[1:]],'runtime':{'python':platform.python_version(),'flint':flint.__version__,'elapsed_seconds':time.monotonic()-start},'trust_scope':['Fresh array generation uses approved exact producers; this checker verifies their outputs and fixed vectors, not a second source-graph implementation.','Executed using the already completed distinct independent full regenerations; no claim of another source rerun.','Fresh gzip/artifact hashes protect this execution only; historical compressed bytes are not acceptance inputs.','Only the frozen finite formal first-order scalar model; separate Claude audit remains pending.']}
    pathlib.Path(a.output).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'result':result['result'],'B':B,'L':L,'controls':len(controls),'elapsed':time.monotonic()-start}))
if __name__=='__main__':main()
