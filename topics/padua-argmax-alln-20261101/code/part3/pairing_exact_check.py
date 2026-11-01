"""Independent-form rational checker for the O-Lt n4 witness.
Uses supplied rational angular boxes; no numerical inverse trig, optimizer,
NumPy, or imports from pairing_screens. Inherits the accepted n4 certificate.
"""
import argparse, gzip, hashlib, json, math
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]

def arctan_enclosure(q):
    s=sum(F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(30))
    return s,s+F(1,61*q**61)

def pi_enclosure():
    a,b=arctan_enclosure(5);c,d=arctan_enclosure(239)
    return 16*a-4*d,16*b-4*c

def cosine_enclosure(t):
    s=F(1);term=F(1)
    for k in range(1,31):
        term=-term*t*t/((2*k-1)*(2*k));s+=term
    error=t**62/math.factorial(62)
    return s-error,s+error

def verify_qbox(X,q,m,pi):
    lo,hi=map(F,X);a,b=map(F,q)
    assert 0<a<b<m
    assert cosine_enclosure(a*pi[1]/m)[0]>hi
    assert cosine_enclosure(b*pi[0]/m)[1]<lo
    return a,b

def max_abs(q,c):return max(abs(q[0]-c),abs(q[1]-c))
def dist(a,c):return sum((x-y)**2 for x,y in zip(a,c))

def check(evidence):
    base=ROOT/'topics/padua-proof-attempts-2-20261101/outputs'
    cp=base/'a5_n4_certificate.json.gz';gp=base/'a5_n4_global.json'
    raw=cp.read_bytes();cert=json.loads(gzip.decompress(raw));glob=json.loads(gp.read_bytes())
    cs=hashlib.sha256(raw).hexdigest();gs=hashlib.sha256(gp.read_bytes()).hexdigest()
    assert cs==glob['certificate_sha256']==evidence['certificate_sha256']
    assert gs==evidence['global_sha256']
    roots={r['id']:r for r in cert['interior_roots']}
    values={r['id']:list(map(F,r['enclosure'])) for r in glob['interior_values']}
    assert len(roots)==len(evidence['rows'])==13
    assert set(roots)=={r['id'] for r in evidence['rows']}
    pi=pi_enclosure();groups={}
    for r in evidence['rows']:
        i=r['id'];assert r['R']==roots[i]['R']
        Q=[verify_qbox(roots[i]['R'][a],r['qbox'][a],4+a,pi) for a in range(2)]
        a=tuple(r['cell']);assert (sum(a)%2)==1
        assert max_abs(Q[0],a[0])+max_abs(Q[1],a[1])<1
        assert list(map(F,r['value']))==values[i]
        groups.setdefault(a,[]).append(i)
    a,b,c=(3,2),(2,1),(4,5)
    assert set(groups[a])=={5} and set(groups[b])=={6,7,11}
    assert tuple(b[i]-a[i] for i in range(2))==(-1,-1)
    assert dist(b,c)>dist(a,c)
    C=[(0,5),(4,5)]
    assert dist(a,c)==min(dist(a,z) for z in C)
    assert dist(b,c)==min(dist(b,z) for z in C)
    lower=max(values[i][0] for i in groups[b])-max(values[i][1] for i in groups[a])
    assert lower==F(5008831434656004615594354983,79228162514264337593543950336)>0
    return {'check':'PASS','status':'exact rational inference from inherited accepted n4 coordinate/value certificates','certificate_sha256':cs,'global_sha256':gs,'groups_checked':len(groups),'roots_checked':13,'a':a,'b':b,'corner':c,'reversal_lower':str(lower),'independent_full_n4_certificate_replay':False}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('evidence');p.add_argument('--output');a=p.parse_args()
    evidence=json.loads(Path(a.evidence).read_text())
    out=check(evidence['certified_list'] if 'certified_list' in evidence else evidence)
    line=json.dumps(out,sort_keys=True)+'\n'
    if a.output:Path(a.output).write_text(line)
    print(line,end='')
