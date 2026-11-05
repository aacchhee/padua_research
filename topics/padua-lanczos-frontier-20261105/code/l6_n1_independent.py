"""Exact independent IEEE-word reconstruction of the frozen L6 n1 contract.

No producer module or floating-point arithmetic is used by the interpreter.
Rational matrix bounds are conservative certificates, not float SVD values.
"""
import argparse, base64, hashlib, json, math, pathlib, platform, resource, signal, sys, time, zlib
from fractions import Fraction as F

SIGN=1<<63
MAXFINITE=0x7fefffffffffffff
ONE=0x3ff0000000000000
THREE=0x4008000000000000
TOP=pathlib.Path(__file__).resolve().parents[1]

def word(x): return f'{x:016x}'
def rational(bits):
    sign=-1 if bits&SIGN else 1
    e=(bits>>52)&2047; m=bits&((1<<52)-1)
    assert e!=2047, 'nonfinite word'
    if e:
        m+=1<<52; power=e-1023-52
    else: power=-1074
    return sign*(F(m<<power) if power>=0 else F(m,1<<(-power)))

def adjacent(value,squared=False):
    """Largest nonnegative finite encoding <=value (or square <=value)."""
    lo,hi=0,MAXFINITE
    while lo<hi:
        mid=(lo+hi+1)//2; a=rational(mid)
        if (a*a if squared else a)<=value:lo=mid
        else:hi=mid-1
    return lo

def nearest(value,negative_zero=False):
    if not value:return SIGN if negative_zero else 0
    sign=SIGN if value<0 else 0; value=abs(value)
    lo=adjacent(value); assert lo<MAXFINITE
    a,b=rational(lo),rational(lo+1)
    midpoint=(a+b)/2
    ans=lo if value<midpoint or (value==midpoint and lo%2==0) else lo+1
    return sign|ans

def root(bits):
    x=rational(bits);assert x>=0
    if x==0:return bits
    lo=adjacent(x,True);a,b=rational(lo),rational(lo+1);threshold=((a+b)/2)**2
    return lo if x<threshold or (x==threshold and lo%2==0) else lo+1

class Machine:
    def __init__(self):self.trace=[];self.states=[]
    def state(self,label,value):
        def encode(x):return [encode(z) for z in x] if isinstance(x,list) else word(x)
        self.states.append(dict(label=label,words=encode(value)))
    def op(self,kind,*values):
        x=[rational(v) for v in values]
        if kind=='sqrt':out=root(values[0])
        else:
            if kind=='add':
                exact=x[0]+x[1];negative=(values[0]&SIGN and values[1]&SIGN)
            elif kind=='sub':
                exact=x[0]-x[1];negative=(values[0]&SIGN and not values[1]&SIGN)
            elif kind=='mul':exact=x[0]*x[1];negative=bool((values[0]^values[1])&SIGN)
            elif kind=='div':
                assert x[1]!=0;exact=x[0]/x[1];negative=bool((values[0]^values[1])&SIGN)
            else:raise ValueError(kind)
            out=nearest(exact,bool(negative))
        self.trace.append((kind,[word(v) for v in values],word(out)))
        return out
    def dot(self,x,y):
        s=0
        for a,b in zip(x,y):s=self.op('add',s,self.op('mul',a,b))
        return s
    def norm(self,x):return self.op('sqrt',self.dot(x,x))
    def product(self,axis,q,label):
        diagonal=[0,ONE,0] if axis==0 else [0,0,ONE]
        v=[self.op('mul',a,b) for a,b in zip(diagonal,q)];self.state(label,v);return v
    def cgs(self,v,basis,label):
        self.state(label+'.input',v)
        passes=[]
        for stage in range(2):
            h=[self.dot(q,v) for q in basis];new=[]
            for r in range(3):
                s=0
                for j,q in enumerate(basis):s=self.op('add',s,self.op('mul',q[r],h[j]))
                new.append(self.op('sub',v[r],s))
            self.state(label+'.b'+str(stage+1),h);self.state(label+'.w'+str(stage+1),new)
            v=new;passes.append(h)
        coeff=[self.op('add',a,b) for a,b in zip(*passes)]
        self.state(label+'.h',coeff)
        return v,coeff

def generation():
    m=Machine();m.state('Xdiag',[0,ONE,0]);m.state('Ydiag',[0,0,ONE])
    s=m.op('sqrt',THREE);a=m.op('div',ONE,s);basis=[[a]*3];m.state('startup.s',s);m.state('q0',basis[0])
    v,g=m.cgs(m.product(1,basis[0],'Yq0'),basis,'q1.cgs');b1=m.norm(v)
    basis.append([m.op('div',z,b1) for z in v]);m.state('q1.beta',b1);m.state('q1.q',basis[1])
    v,h=m.cgs(m.product(0,basis[0],'Xq0'),basis,'q2.cgs');b2=m.norm(v)
    basis.append([m.op('div',z,b2) for z in v]);m.state('q2.beta',b2);m.state('q2.q',basis[2])
    hxcols=[[h[0],h[1],b2]];terminal=[]
    for j in (1,2):
        v,c=m.cgs(m.product(0,basis[j],'Xq'+str(j)),basis,'Xcol'+str(j));hxcols.append(c);terminal.append(v)
    v,j1=m.cgs(m.product(1,basis[1],'Yq1'),basis,'Ycol1');terminal.append(v)
    j0=[g[0],b1,0]
    for label,value in [('Q',transpose(basis)),('Hx',transpose(hxcols)),('j0',j0),('j1',j1)]:m.state(label,value)
    return m.trace,basis,hxcols,j0,j1,terminal,m.states

def transpose(a):return list(map(list,zip(*a)))
def matmul(a,b):return [[sum((x*y for x,y in zip(row,col)),F(0)) for col in zip(*b)] for row in a]
def minus(a,b):return [[x-y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def det(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            +a[0][1]*(a[1][2]*a[2][0]-a[1][0]*a[2][2])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))
def sqrt_bounds(x,bits=160):
    assert x>=0
    scale=1<<bits;k=math.isqrt((x.numerator<<(2*bits))//x.denominator)
    lo=F(k,scale);hi=lo if lo*lo==x else F(k+1,scale)
    assert lo*lo<=x<=hi*hi
    return lo,hi
def norm_bounds(a):
    column_squares=[sum((z*z for z in c),F(0)) for c in zip(*a)]
    return sqrt_bounds(max(column_squares))[0],sqrt_bounds(sum(column_squares,F(0)))[1]
def serial(a):
    if isinstance(a,F):return str(a)
    if isinstance(a,list) or isinstance(a,tuple):return [serial(z) for z in a]
    if isinstance(a,dict):return {k:serial(v) for k,v in a.items()}
    return a
def matrix_analysis(basis,hxcols,j0,j1):
    q=transpose([[rational(z) for z in b] for b in basis])
    hx=transpose([[rational(z) for z in c] for c in hxcols]);y0=list(map(rational,j0));y1=list(map(rational,j1))
    z=matmul(hx,[[v] for v in y0]);h0,h1,beta=[row[0] for row in hx]
    y2=[(z[r][0]-h0*y0[r]-h1*y1[r])/beta for r in range(3)];hy=transpose([y0,y1,y2])
    X=[[F(int(i==j==1)) for j in range(3)] for i in range(3)]
    Y=[[F(int(i==j==2)) for j in range(3)] for i in range(3)]
    fx=minus(matmul(X,q),matmul(q,hx));fy=minus(matmul(Y,q),matmul(q,hy))
    I=[[F(int(i==j)) for j in range(3)] for i in range(3)]
    gram=minus(matmul(transpose(q),q),I);gup=max(sum(map(abs,row),F(0)) for row in gram)
    glow=max(abs(v) for row in gram for v in row)
    assert det(q)!=0 and gup<F(1,2)
    qmin=sqrt_bounds(1-gup)[0];qmax=sqrt_bounds(1+gup)[1]
    fxb,fyb=norm_bounds(fx),norm_bounds(fy);budget=F(64,1<<53)*qmin
    budget_pass=fxb[1]<=budget and fyb[1]<=budget
    comm=minus(matmul(hx,hy),matmul(hy,hx));assert all(row[0]==0 for row in comm)
    asymx=minus(hx,transpose(hx));asymy=minus(hy,transpose(hy))
    witnesses=[dict(matrix=name,row=i,col=j,value=str(a[i][j])) for name,a in [('Hx',asymx),('Hy',asymy)] for i in range(3) for j in range(i+1,3) if a[i][j]]
    return dict(Q=q,Hx=hx,Hy=hy,Fx=fx,Fy=fy,Gram=gram,detQ=det(q),
        gram_norm=[glow,gup],Q_norm=[qmin,qmax],sigma_min_Q=[qmin,qmax],
        Fx_norm=fxb,Fy_norm=fyb,Fx_column_norms=[sqrt_bounds(sum((v*v for v in c),F(0))) for c in zip(*fx)],
        Fy_column_norms=[sqrt_bounds(sum((v*v for v in c),F(0))) for c in zip(*fy)],
        full_residual_64u_budget_pass=budget_pass,necessary_symmetry_failures=witnesses,
        raw_branch='INCONSISTENT' if witnesses else 'NECESSARY_SYMMETRY_PASSED_ONLY')

def identity(p):
    p=pathlib.Path(p);return dict(path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size)

PRODUCER='d001e22e4ed8713721c6af429d5089d6c462afef60f9835e3802f79f03738be5'
CONTRACT='9d857e30146be3e2f8963f20cf89a4441fa72b1b542a5dcb79245384198e3a35'

def validate_norm(a,certificate):
    column=[sum((v*v for v in col),F(0)) for col in zip(*a)]
    lower,upper=map(F,certificate['spectral'])
    assert 0<=lower<=upper and lower*lower<=max(column) and upper*upper>=sum(column,F(0))
    for square,interval in zip(column,certificate['column_euclidean']):
        lo,hi=map(F,interval);assert 0<=lo<=hi and lo*lo<=square<=hi*hi

def verify(trace,producer,analysis,expected):
    etrace,basis,hxcols,j0,j1,terminals,states,result=expected
    assert producer['source_sha256']==PRODUCER
    assert producer['status']=='FROZEN n1 actual run completed; independent verification PENDING'
    assert len(trace['primitives'])==len(etrace)==producer['trace']['primitive_count']
    for i,(actual,wanted) in enumerate(zip(trace['primitives'],etrace)):
        assert actual['seq']==i
        assert (actual['op'],actual['args'],actual['out'])==wanted,(i,actual,wanted)
        values=[rational(int(v,16)) for v in actual['args']]
        target=(values[0] if actual['op']=='sqrt' else
                values[0]+values[1] if actual['op']=='add' else
                values[0]-values[1] if actual['op']=='sub' else
                values[0]*values[1] if actual['op']=='mul' else values[0]/values[1])
        assert F(actual['exact'])==target and actual['RN'] is True
        bits=int(actual['out'],16)
        assert actual['subnormal']==(((bits>>52)&2047)==0 and bool(bits&((1<<52)-1)))
    encode=lambda x:[encode(t) for t in x] if isinstance(x,list) else word(x)
    raw=producer['raw_words']
    assert raw['Q']==encode(transpose(basis)) and raw['Hx']==encode(transpose(hxcols))
    assert raw['j0']==encode(j0) and raw['j1']==encode(j1) and raw['stored_D_scalars']==14
    assert raw['terminals']==dict(zip(('X1','X2','Y1'),map(encode,terminals)))
    for actual_key,key in [('Q','Q'),('raw_Hx','Hx'),('completed_Hy','Hy'),('Fx','Fx'),('Fy','Fy'),('Gram_loss','Gram'),('detQ','detQ')]:
        assert analysis[actual_key]==serial(result[key]),actual_key
    assert analysis['C1_j2']==serial([row[2] for row in result['Hy']])
    assert analysis['omitted_Y_column']==serial([row[2] for row in result['Fy']])
    assert producer['C1_j2']==analysis['C1_j2'] and producer['completed_Hy']==analysis['completed_Hy']
    for key,mat in [('Gram_loss','Gram'),('Fx','Fx'),('Fy','Fy')]:validate_norm(result[mat],producer['norm_bounds'][key])
    eta=F(producer['norm_bounds']['Gram_loss']['spectral'][1])
    for key in ('Q_spectral','sigma_min_Q'):
        lo,hi=map(F,producer['norm_bounds'][key]);assert lo>=0 and lo*lo<=1-eta and hi*hi>=1+eta
    witnesses=[dict(matrix=w['matrix'],i=w['row'],j=w['col'],exact_difference=w['value']) for w in result['necessary_symmetry_failures']]
    assert witnesses==producer['symmetry_witnesses']==analysis['consistency']['asymmetry_witnesses']
    assert witnesses,'This checker is scoped to a raw necessary-condition failure; do not accept consistency from symmetry alone.'
    assert producer['consistency_status']==analysis['consistency']['status']=='INCONSISTENT raw exact data; STOP'
    assert analysis['consistency']['symmetry'] is False
    comm=minus(matmul(result['Hx'],result['Hy']),matmul(result['Hy'],result['Hx']))
    assert analysis['consistency']['commutator']==serial(comm)
    interior=all(comm[i][0]==0 and comm[0][i]==0 for i in range(3))
    assert analysis['consistency']['interior_commutator_row_col0_zero']==interior
    assert result['full_residual_64u_budget_pass'] and all(v=='PASS' for v in producer['budget_gates'].values())
    # Named stored states are redundant trace diagnostics; independently check
    # their final data and require every scalar state word to be a literal
    # input or a previously obtained exact-interpreter output.
    admissible={'0000000000000000','8000000000000000',word(ONE),word(THREE)}|{t[2] for t in etrace}
    def state_words(x):
        if isinstance(x,list):
            for z in x:yield from state_words(z)
        else:yield x
    assert len(trace['states'])==producer['trace']['state_count']
    assert trace['states']==states
    assert all(w in admissible for s in trace['states'] for w in state_words(s['words']))
    final={s['label']:s['words'] for s in trace['states']}
    for k in ('Q','Hx','j0','j1'):assert final[k]==raw[k]
    return True

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--producer-root',required=True)
    ap.add_argument('--out',required=True);ap.add_argument('--receipt',required=True);a=ap.parse_args()
    resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
    def expire(*_):raise TimeoutError('55 second independent cap')
    signal.signal(signal.SIGALRM,expire);signal.alarm(55);start=time.monotonic()
    out=pathlib.Path(a.out);out.mkdir(parents=True,exist_ok=False);rootpath=pathlib.Path(a.producer_root)
    assert identity(TOP/'theory/l6-02-actual-n1-implementation-contract.md')['sha256']==CONTRACT
    paths=[rootpath/'receipt.json',rootpath/'analysis.json',rootpath/'trace-packed.json']
    inputs=[identity(p) for p in paths]
    provenance=dict(command=[sys.executable,*sys.argv],source=identity(__file__),inputs=inputs,
                    contract=identity(TOP/'theory/l6-02-actual-n1-implementation-contract.md'),caps=dict(seconds=55,bytes=512*1024**2))
    (out/'start-provenance.json').write_text(json.dumps(provenance,indent=1)+'\n')
    producer=json.loads(paths[0].read_text());analysis=json.loads(paths[1].read_text());packed=json.loads(paths[2].read_text())
    data=zlib.decompress(base64.b64decode(packed['data']));assert len(data)==packed['uncompressed_bytes']
    assert hashlib.sha256(data).hexdigest()==packed['uncompressed_sha256']==producer['trace']['sha256']
    trace=json.loads(data)
    assert nearest(F(1)+F(1,1<<53))==ONE
    assert nearest(F(1)+F(3,1<<53))==ONE+2
    assert nearest(F(1,1<<1075))==0 and nearest(F(3,1<<1075))==2
    control=Machine();assert control.op('add',SIGN,0)==0 and control.op('sub',SIGN,0)==SIGN
    assert control.op('mul',SIGN,ONE)==SIGN and control.op('sqrt',SIGN)==SIGN
    etrace,basis,hxcols,j0,j1,terminals,states=generation();result=matrix_analysis(basis,hxcols,j0,j1)
    expected=(etrace,basis,hxcols,j0,j1,terminals,states,result);verify(trace,producer,analysis,expected)
    rejected=[]
    def mutation(label,where,change):
        t,p,b=json.loads(json.dumps(trace)),json.loads(json.dumps(producer)),json.loads(json.dumps(analysis))
        change({'trace':t,'producer':p,'analysis':b}[where])
        try:verify(t,p,b,expected)
        except AssertionError:rejected.append(label)
        else:raise AssertionError('Corruption accepted: '+label)
    mutation('changed operation result word','trace',lambda x:x['primitives'][0].update(out=word(ONE)))
    mutation('omitted operation','trace',lambda x:x['primitives'].pop())
    mutation('changed exact C1 column','analysis',lambda x:x['C1_j2'].__setitem__(0,str(F(x['C1_j2'][0])+1)))
    mutation('changed omitted Y residual','analysis',lambda x:x['omitted_Y_column'].__setitem__(0,'1'))
    mutation('invalid zero residual norm upper','producer',lambda x:x['norm_bounds']['Fx']['spectral'].__setitem__(1,'0'))
    verify(trace,producer,analysis,expected)
    detail=out/'independent-analysis.json';detail.write_text(json.dumps(serial(result),indent=1)+'\n')
    independent_trace=out/'independent-trace.json';independent_trace.write_text(json.dumps(etrace,separators=(',',':'))+'\n')
    receipt=dict(status='PASS exact independent frozen n1 trace; raw branch INCONSISTENT',
        source=identity(__file__),command=[sys.executable,*sys.argv],inputs=inputs,
        python=platform.python_version(),trace_operations=len(etrace),producer_source_sha256=PRODUCER,
        contract_sha256=CONTRACT,detail=identity(detail),trace=identity(independent_trace),
        elapsed_seconds=time.monotonic()-start,peak_rss_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        exact_primitive_controls='ties-even normal/subnormal and signed-zero add/sub/mul/sqrt pass',
        all_operation_operand_result_words_match=True,exact_C1_and_full_residuals_match=True,
        producer_norm_enclosures_validated=True,independent_norm_method='Exact Gram max-row bound; residual column lower/Frobenius upper; rational dyadic sqrt enclosures',
        independent_norm_bounds=serial({k:result[k] for k in ('gram_norm','Q_norm','sigma_min_Q','Fx_norm','Fy_norm')}),
        Gram_loss_le_half=True,full_residual_64u_budget_pass=result['full_residual_64u_budget_pass'],
        necessary_symmetry_failures=result['necessary_symmetry_failures'],malformed_controls_rejected=rejected,
        limits='One fixed binary64 n1 instance. Necessary exact symmetry fails, so no raw mass-one section functional/positive model is claimed. No correction branch, PD-T145 matching or general Greenbaum verdict.')
    pathlib.Path(a.receipt).write_text(json.dumps(receipt,indent=1)+'\n')
    signal.alarm(0);print(json.dumps({k:receipt[k] for k in ('status','trace_operations','elapsed_seconds','full_residual_64u_budget_pass','necessary_symmetry_failures')},indent=1))

if __name__=='__main__':main()
