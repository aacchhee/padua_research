import json,sys
def load(p):
    t=open(p).read()
    try: return json.loads(t)
    except Exception: return [json.loads(l) for l in t.splitlines() if l.strip()]
def flat(o,p=""):
    if isinstance(o,dict):
        for k,v in o.items(): yield from flat(v,p+"/"+k)
    elif isinstance(o,list):
        for i,v in enumerate(o): yield from flat(v,p+f"[{i}]")
    else: yield p,o
for a,b in zip(sys.argv[1::2],sys.argv[2::2]):
    A=dict(flat(load(a)));B=dict(flat(load(b)))
    d=[(k,A.get(k),B.get(k)) for k in sorted(set(A)|set(B)) if A.get(k)!=B.get(k)]
    big=[x for x in d if not(isinstance(x[1],float) and isinstance(x[2],float) and abs(x[1]-x[2])<=1e-9*max(1,abs(x[1])))]
    print("==",a.split('/')[-1],"vs",b.split('/')[-1],"diffs",len(d),"non-negligible",len(big))
    for x in big[:12]: print("   ",x[0],"|",str(x[1])[:70],"->",str(x[2])[:70])
