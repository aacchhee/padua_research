import json, sys
R='/home/user/padua_research/topics/padua-argmax-alln-20261101/outputs/gated/'
A='/tmp/claude-0/-home-user-padua-research/efec27fb-ede8-54e4-a9c8-12b8741cbbba/scratchpad/audit01/'
c=json.load(open(R+'d3_edge_certificate.json')); r=json.load(open(A+'padua_d3_claude_certificate.json'))
def diff(a,b,path=''):
    out=[]
    if isinstance(a,dict) and isinstance(b,dict):
        for k in sorted(set(a)|set(b)):
            if k not in a or k not in b: out.append((path+'/'+k,'missing')); continue
            out+=diff(a[k],b[k],path+'/'+k)
    elif isinstance(a,list) and isinstance(b,list):
        if len(a)!=len(b): out.append((path,'len %d vs %d'%(len(a),len(b))))
        for i,(x,y) in enumerate(zip(a,b)): out+=diff(x,y,path+'[%d]'%i)
    elif a!=b: out.append((path,(a,b)))
    return out
d=diff(c,r)
for p,v in d: print(p,v)
print('top keys',sorted(c))
print('n pairs',len(c['pairs']),'leaves',sum(len(p['leaves']) for p in c['pairs']),'witnesses',len(c['ep_exact_witnesses']))
for p in c['pairs']: print(p['n'],p['j'],p['source'],p['target'],[l['path'] for l in p['leaves']],p['pending'])
for w in c['ep_exact_witnesses']: print(w['n'],w['j'],w['source'],w['target'],w['phase'],w['reversal_lower']/2**192)
for name in ['padua_d3_claude_check.json','padua_d3_claude_check_regen.json']:
    k=json.load(open(A+name)); print(name,k['accepted'],k['certificate_sha256'],k['checker_sha256'],k['malformed_controls']['count'],k['malformed_controls']['malformed_cases_rejected'],k['count_n7'],k['count_n12'])
dev=json.load(open(R+'d3_edge_check.json'))
k=json.load(open(A+'padua_d3_claude_check.json'))
print('dev vs claude check diffs:',diff(dev,k))
k2=json.load(open(A+'padua_d3_claude_check_regen.json'))
print('dev vs regen check diffs:',diff(dev,k2))
