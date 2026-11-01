import json,sys
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
R=sys.argv[1]
ev=json.load(open('topics/padua-lanczos-drift-20261101/evidence/e1-full-sweep.json'))
def find(obj,setn,rule):
    # search the sweep for degree 12 record
    out=[]
    def walk(o):
        if isinstance(o,dict):
            if o.get('degree')==12 and o.get('rule')==rule and (o.get('set')==setn or setn in json.dumps(o.get('set',''))):
                out.append(o)
            for v in o.values(): walk(v)
        elif isinstance(o,list):
            for v in o: walk(v)
    walk(obj); return out
runs={}
for s,r,f in [('triangle','bj','audit-T24-bj'),('triangle','pivot','audit-T24-pivot'),('rotated','bj','audit-rotQ24-bj'),('rotated','alt','audit-rotQ24-alt')]:
    a=json.load(open(f'{R}/{f}.json')); runs[(s,r)]=a
    c=find(ev,s,r)
    keys=['Knode_squared','KHS_squared','Urow_squared','upper_squared']
    if c:
        eq={k:(a[k]['exact']==c[0][k]['exact']) if k in c[0] else None for k in keys}
    else: eq='no committed match found'
    print(s,r,'match committed:',eq)
X=lambda s,r,k:F(runs[(s,r)][k]['exact'])
t=X('triangle','bj','Knode_squared')/X('triangle','pivot','upper_squared')
print('T24 bj Knode^2 / pivot upper^2 =',float(t),' >1126^2?',t>1126**2)
u=X('rotated','bj','Knode_squared')/X('rotated','alt','Urow_squared')
print('rot bj Knode^2 / alt Urow^2 =',float(u),' >11.72^2?',u>F(1172,100)**2, ' >100?',u>100)
k=X('rotated','bj','Knode_squared')/X('rotated','alt','KHS_squared')
print('rot bj Knode^2 / alt KHS^2 =',float(k),' <100?',k<100)
print('rot alt upper==min(KHS,Urow)?', X('rotated','alt','upper_squared')==min(X('rotated','alt','KHS_squared'),X('rotated','alt','Urow_squared')))
print('tri pivot upper==min?', X('triangle','pivot','upper_squared')==min(X('triangle','pivot','KHS_squared'),X('triangle','pivot','Urow_squared')))
