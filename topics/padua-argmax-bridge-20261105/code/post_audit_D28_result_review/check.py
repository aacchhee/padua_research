"""Independent exact D28 result reconstruction; no author code imports."""
import resource
resource.setrlimit(resource.RLIMIT_CPU,(1,2))
import hashlib
import json
import math
import sys
import time
from fractions import Fraction as F
from pathlib import Path

HERE=Path(__file__).resolve().parent
TOPIC=HERE.parents[1]
ROOT=TOPIC.parents[1]
RAW=ROOT/'local-output/argmax-bridge-20261105/post-audit-D28/static'
OUT=HERE/'result'
STATIC=TOPIC/'code/post_audit_D28_static'
CACHE={}

def identity(p):
    p=Path(p).resolve()
    if p not in CACHE:
        raw=p.read_bytes()
        CACHE[p]={'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
    return CACHE[p]

def read(p):
    def pairs(items):
        d={}
        for k,v in items:
            assert k not in d
            d[k]=v
        return d
    return json.loads(Path(p).read_text(),object_pairs_hook=pairs,
        parse_constant=lambda x:(_ for _ in ()).throw(ValueError(x)))

def cpu():
    r=resource.getrusage(resource.RUSAGE_SELF)
    return r.ru_utime+r.ru_stime

def save(name,obj):
    data=(json.dumps(obj,sort_keys=True,indent=2,allow_nan=False)+'\n').encode()
    assert len(data)<16384
    with (OUT/name).open('xb') as h:h.write(data)
    return {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}

def verify_id(obj):
    p=Path(obj['path'])
    if not p.is_absolute():p=ROOT/p
    actual=identity(p)
    assert actual['bytes']==obj['bytes'] and actual['sha256']==obj['sha256'],str(p)

def identity_tree(value):
    if isinstance(value,dict):
        if {'path','bytes','sha256'}<=set(value):verify_id(value)
        for v in value.values():identity_tree(v)
    elif isinstance(value,list):
        for v in value:identity_tree(v)

def binary(s):
    assert type(s) is str
    value=float.fromhex(s)
    assert math.isfinite(value) and value.hex()==s
    return F.from_float(value)

def main(receipt_sha,final_sha,exit_chunk):
    pins={
        STATIC/'FREEZE.json':'4769e50fbedcdfc54ce771a60f2870e725db71a04ea8933c9c0d6bd1655cf150',
        STATIC/'SPEC.md':'da0bce3a45248f2ecc825eb564e45c626d8763e3f14c3c24a5944566236e6e84',
        STATIC/'SOURCE.md':'d76247be408a85f7c524f0e80f1eb68f190e77c1bb5665ae6af7096d9108b0be',
        TOPIC/'independent-checks-D28-static-source.md':'15b80aa2f052b4fc51584a08570dd44d58eb42c42afaddc701d6208bb6643044',
        RAW/'essential-receipt.json':receipt_sha,RAW/'final-accounting.json':final_sha}
    for p,sha in pins.items():assert identity(p)['sha256']==sha
    freeze=read(STATIC/'FREEZE.json')
    assert len(freeze['code_data'])==14
    for row in freeze['code_data']:verify_id(row)
    doc=read(RAW/'essential-receipt.json');final=read(RAW/'final-accounting.json')
    assert doc['format']=='D28-static-allrow-v1' and doc['n']==6912
    assert final['result']=='INDEPENDENT_CHEAP_STATIC_REPLAY_ACCEPTED_PENDING_RESULT_REVIEW'
    assert final['complete'] is True and final['first_failure'] is None
    assert final['hard_aggregate_cap']==200 and final['total_CPU_through_summary']<200
    limit=final['final_self_limit']
    assert limit['no_live_children'] is True and limit['waited_child_CPU']+limit['absolute_self_CPU_hard']<=199
    assert type(exit_chunk) is str and exit_chunk
    save('identities.json',{'inputs':[identity(p) for p in pins],
        'own_source':identity(Path(__file__).resolve()),'own_SPEC':identity(HERE/'SPEC.md'),
        'frozen_entries':len(freeze['code_data']),'observed_controller_exit_code':0,
        'observed_controller_exit_tool_chunk':exit_chunk,'before_exact_certificate_arithmetic':True})
    tree=read(TOPIC/'evidence/d19-pruned-tree.json')
    assert set(tree)=={'format','n','preorder'} and tree['format']=='D19-midpoint-v1' and type(tree['n']) is int and tree['n']==2048
    tokens=tree['preorder'];assert type(tokens) is str and len(tokens)==61
    pending=[(F(0),F(1),F(0),F(1))];leaves=[]
    for index,token in enumerate(tokens):
        assert pending
        box=pending.pop();a,A,b,B=box
        if token=='.':leaves.append((index,box));continue
        if token=='a':
            mid=(a+A)/2; children=((a,mid,b,B),(mid,A,b,B))
        else:
            assert token=='b';mid=(b+B)/2;children=((a,A,b,mid),(a,A,mid,B))
        pending.extend(reversed(children))
    assert not pending and len(leaves)==31
    def canon(a,b):
        orbit=set()
        for sa in (-1,1):
            for sb in (-1,1):
                for p in range(-2,3):
                    for q in range(-2,3):
                        if (p+q)%2:continue
                        x,y=sa*a+p,sb*b+q
                        if x>=0 and y>=0 and x+y<=1:orbit.add((x,y))
        assert orbit
        return min(orbit)
    corners={}
    for ident,(a,A,b,B) in leaves:
        if a+b<=1:corners[ident]={canon(x,y) for x in (a,A) for y in (b,B)}
    required=set().union(*corners.values())
    assert len(required)==41 and (F(0),F(0)) in required
    def rows(document):
        assert document['n']==6912 and len(document['rows'])==41
        assert document['columns']==['api','a','b','lower_hex','upper_hex','radius_hex','counts','CPU']
        out={}
        for row in document['rows']:
            api,a,b,lo,hi,rad,costs,cost=row
            key=(F(a),F(b));assert api=='S' and key not in out and key in required
            assert tuple(map(str,key))==(a,b)
            lo,hi,rad=map(binary,(lo,hi,rad));assert 0<=lo<=hi and rad>=0
            assert len(costs)==6 and all(type(x) is int and x>=0 for x in costs)
            if key[0]==1 or key[1]==1:assert costs==[0]*6 and lo==hi==1
            else:
                r,d,c,md,mc,o=costs
                assert r==4*6912 and o==2*6913-4 and md<=5 and mc<=24 and d<=5*o and c<=24*o
            assert type(cost) in (int,float) and math.isfinite(cost) and 0<=cost
            out[key]=(lo,hi,costs,cost)
        assert set(out)==required
        return out
    fresh=rows(doc);old=rows(read(TOPIC/'evidence/d21-static6912.json'))
    assert [tuple(map(F,row[1:3])) for row in doc['rows']]==sorted(required)
    assert all(row[3]<=15 for row in fresh.values())
    widths=[];oldwidths=[];gaps=[]
    for key,(lo,hi,counts,cost) in fresh.items():
        ol,oh,oc,ot=old[key]
        assert counts==oc and max(lo,ol)<=min(hi,oh)
        assert hi-lo<=F(1,50000) and hi-ol<=F(1,50000)
        widths.append(hi-lo);oldwidths.append(oh-ol);gaps.append(hi-ol)
    L=fresh[(F(0),F(0))][0];assert L>0
    data={}
    for ident,box in leaves:
        if ident not in corners:continue
        a,A,b,B=box
        theta=F(22,7)**2*((A-a)**2+F(6912,6913)**2*(B-b)**2)/8
        assert 0<=theta<1
        V=max(fresh[k][1] for k in corners[ident])
        data[ident]=(theta,V,V/(1-theta))
    R=max(t[2] for t in data.values());M=F((R.numerator+R.denominator-1)//R.denominator)
    assert M>0
    active=[i for i,(_,_,r) in data.items() if r==R]
    bounds=[];counts={};margins={}
    for ident,(a,A,b,B) in leaves:
        if ident not in data:tag='OUTSIDE';upper=None;requirements=[]
        else:
            theta,V,_=data[ident];upper=V+theta*M;low=a+b;high=min(A+B,F(1))
            if upper<L:tag='FAR';requirements=[('FAR',L-upper)]
            elif 2*F(22,7)*high<=1 and upper-F(1,16)<L:
                tag='NEAR';requirements=[('NEAR',L-upper+F(1,16))]
            else:
                tag='SPLIT';requirements=[]
                if low<=F(25,157):requirements.append(('SPLIT_NEAR',L-upper+F(1,16)))
                if high>=F(7,44):requirements.append(('SPLIT_FAR',L-upper))
                assert requirements
            for label,gap in requirements:
                assert gap>0
                margins[label]=min(margins.get(label,gap),gap)
        counts[tag]=counts.get(tag,0)+1
        bounds.append([ident,tag,None if upper is None else str(upper)])
    own={'n':6912,'nodes':61,'vertices':len(required),'L':str(L),
        'norm':{'R':str(R),'Mceil':str(M),'active_norm_leaf_ids':active},
        'leaf_counts':counts,'minimum_strict_margins':{k:str(v) for k,v in margins.items()},'leaf_bounds':bounds}
    for k,v in own.items():assert doc['verification'][k]==v,k
    comp=doc['comparison']
    assert comp['rows']==41 and comp['all_overlap'] is True and comp['all_counters_equal'] is True
    for key,value in [('maximum_new_endpoint_width',max(widths)),('maximum_D21_endpoint_width',max(oldwidths)),('maximum_new_upper_minus_D21_lower',max(gaps))]:assert F(comp[key])==value
    for stage in doc['CPU_stages']:
        assert stage['complete'] is True and stage['accounting_complete'] is True and stage['returncode']==0 and stage['stop'] is None and stage['first_failure'] is None
        assert stage['inclusive_CPU_with_supervision']<=(2 if stage['stage']=='controls' else 180)
    identity_tree(doc)
    raw=read(RAW/'checker-checkpoint.json')
    assert raw['status']=='COMPLETE' and raw['active_call'] is None and len(raw['completed_calls'])==41
    for call,row in zip(raw['completed_calls'],doc['rows']):
        assert call['n']==6912 and call['native']['returncode']==0
        assert [call['api'],*call['key'],*call['native']['raw_hex'],call['native']['counts'],call['cpu_seconds']]==row
    build=read(RAW/'checker-build.json');identity_tree(build)
    before=read(RAW/'checker-runtime-before.json');after=read(RAW/'checker-runtime-after.json')
    assert before['loaded']==after['loaded'] and before['all_file_mappings']==after['all_file_mappings']
    identity_tree(before);identity_tree(after)
    for stage in ('controls','checker'):
        reap=read(RAW/(stage+'-descendants.json'));assert reap['complete'] is True
    assert not list(RAW.glob('*first-failure*'))
    oldfinal=read(TOPIC/'evidence/d21-static6912-final-accounting.json')
    result={'status':'ACCEPT_INDEPENDENT_D28_RESULT','observed_native_exit_code':0,'observed_native_exit_tool_chunk':exit_chunk,
        'native_receipt':identity(RAW/'essential-receipt.json'),'final_account':identity(RAW/'final-accounting.json'),
        'exact_certificate':own,'retained_leaves':len(data),'tangent_leaves':sum(a+b==1 for _,(a,A,b,B) in leaves),
        'all41_overlaps_and_counters':True,'maximum_new_width':str(max(widths)),'maximum_old_width':str(max(oldwidths)),
        'maximum_upper_minus_old_lower':str(max(gaps)),'unique_hashed_artifacts':len(CACHE),
        'fresh_point_CPU_sum':sum(x[3] for x in fresh.values()),'fresh_point_CPU_max':max(x[3] for x in fresh.values()),
        'D21_point_CPU_sum':sum(x[3] for x in old.values()),'D21_point_CPU_max':max(x[3] for x in old.values()),
        'D28_final_CPU_checkpoint':final['total_CPU_through_summary'],'D21_final_CPU_checkpoint':oldfinal['total_CPU_through_summary'],
        'fresh_build_CPU':build['inclusive_build_CPU'],'comparison_predicates_CPU':comp['comparison_predicates_CPU'],
        'review_CPU_before_serialization':cpu(),'review_CPU_hard_cap':2,'children':0,
        'own_source':identity(Path(__file__).resolve()),'own_SPEC':identity(HERE/'SPEC.md')}
    output=save('review.json',result)
    print(json.dumps({'status':result['status'],'review_CPU_before_serialization':result['review_CPU_before_serialization'],
        'M':str(M),'L':str(L),'leaf_counts':counts,'artifacts':len(CACHE),**output}),flush=True)
    assert cpu()<2

if __name__=='__main__':
    assert len(sys.argv)==5 and sys.argv[1]=='--run-once'
    OUT.mkdir(parents=True,exist_ok=False)
    try:main(*sys.argv[2:])
    except BaseException as error:
        save('first-failure.json',{'error':repr(error),'CPU_checkpoint':cpu(),'retry':False})
        raise
