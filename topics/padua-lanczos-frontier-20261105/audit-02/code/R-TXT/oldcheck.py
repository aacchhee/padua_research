import re,sys
S=sys.argv[1]
t=open(sys.argv[2]).read()
secs=re.split(r'\n(?=## )',t)
for s in secs:
    title=s.split('\n',1)[0]
    m=re.search(r'OLD[^\n]*:\s*\n+```text\n(.*?)\n```',s,re.S)
    n=re.search(r'NEW[^\n]*:\s*\n+```text\n(.*?)\n```',s,re.S)
    if not m: print('NO-OLD',title); continue
    old=m.group(1); new=n.group(1) if n else None
    fname=None
    for f in ['PROOF_STATUS.md','state/IDEAS.md','state/CURRENT.md','ID_CROSSWALK.md','RESULTS.md']:
        if f in title: fname=f
    res=[]
    for r in ['330fab8','origin_main','HEAD']:
        body=open(f'{S}/reg/{r}/{fname}').read()
        c=body.count(old); cn=body.count(new) if new else -1
        res.append(f'{r}:old={c},new={cn}')
    print(title[:60].ljust(60),' '.join(res), 'same' if old==new else '')
