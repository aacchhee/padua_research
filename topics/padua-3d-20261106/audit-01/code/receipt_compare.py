import json,subprocess,sys
def flat(o,p=""):
    if isinstance(o,dict):
        for k,v in o.items(): yield from flat(v,p+"/"+k)
    elif isinstance(o,list):
        for i,v in enumerate(o): yield from flat(v,p+f"[{i}]")
    else: yield p,o
def load(t):
    try: return json.loads(t)
    except Exception: return [json.loads(l) for l in t.splitlines() if l.strip()]
for f in sys.argv[1:]:
    old=load(subprocess.check_output(["git","show","HEAD:"+f]).decode()); new=load(open(f).read())
    a=dict(flat(old)); b=dict(flat(new))
    diff=[(k,a.get(k),b.get(k)) for k in sorted(set(a)|set(b)) if a.get(k)!=b.get(k)]
    num=[d for d in diff if isinstance(d[1],float) and isinstance(d[2],float)]
    big=[d for d in num if abs(d[1]-d[2])>1e-9*max(1,abs(d[1]))]
    other=[d for d in diff if d not in num]
    print("==",f,"diffs",len(diff),"float",len(num),"float>1e-9rel",len(big))
    for d in other+big: print("  ",d[0],"|",str(d[1])[:90],"->",str(d[2])[:90])
