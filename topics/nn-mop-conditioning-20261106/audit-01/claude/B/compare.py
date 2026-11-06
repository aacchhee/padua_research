import json,sys
IGN={'elapsed_seconds','python','mpmath'}
def strip(o):
    if isinstance(o,dict): return {k:strip(v) for k,v in o.items() if k not in IGN}
    if isinstance(o,list): return [strip(v) for v in o]
    return o
T='/workspace/padua_research/topics/nn-mop-conditioning-20261106/'
B=sys.argv[1]
for mine,theirs in [('c2-hahn-checks.json','c2-hahn-checks.json'),('c2-hahn-terminal.json','c2-hahn-terminal.json'),('independent-hahn-rate-receipt.json','independent-hahn-rate-receipt.json'),('c2-hahn-upper-search.json','c2-hahn-upper-search.json')]:
    a=json.load(open(B+'/'+mine)); b=json.load(open(T+theirs))
    sa,sb=strip(a),strip(b)
    print(mine, 'IDENTICAL(after ignoring timing/version)' if sa==sb else 'DIFF')
    if sa!=sb:
        for k in set(sa)|set(sb):
            if sa.get(k)!=sb.get(k): print('  key',k, str(sa.get(k))[:200],'|',str(sb.get(k))[:200])
    print('  ignored committed:',{k:b.get(k) for k in IGN if k in b}, 'mine:',{k:a.get(k) for k in IGN if k in a})
