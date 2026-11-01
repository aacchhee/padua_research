import json,sys
def load(p): return json.load(open(p))
def flat(d,pre=''):
    out={}
    if isinstance(d,dict):
        for k,v in d.items(): out.update(flat(v,pre+'/'+k))
    elif isinstance(d,list):
        for i,v in enumerate(d): out.update(flat(v,pre+f'[{i}]'))
    else: out[pre]=d
    return out
a,b=flat(load(sys.argv[1])),flat(load(sys.argv[2]))
diff=sorted(k for k in set(a)|set(b) if a.get(k,'<missing>')!=b.get(k,'<missing>'))
print(len(a),len(b),'differing keys:',diff)
for k in ['/count_certified','/total_maxima','/interior','/edge','/corner','/global_argmax_verified','/accepted']:
    if k in a: print(k,a[k])
