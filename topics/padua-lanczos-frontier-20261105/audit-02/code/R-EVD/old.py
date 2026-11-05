import re,subprocess
D='topics/padua-lanczos-frontier-20261105'
t=open(D+'/registry-proposals-response-01.md').read()
secs=re.split(r'^## ',t,flags=re.M)[1:]
res=[]
for s in secs:
    head=s.splitlines()[0]; f=head.split(' — ')[0].strip()
    m=re.search(r'^OLD[^\n]*:\n+```[^\n]*\n(.*?)\n```',s,re.M|re.S)
    if not m: res.append((head,'no OLD fence')); continue
    old=m.group(1)
    out=[]
    for ref in ['330fab8','9322fba']:
        try: b=subprocess.check_output(['git','show',f'{ref}:{f}'],text=True,stderr=subprocess.DEVNULL)
        except Exception: out.append('nofile'); continue
        out.append(old in b or (old.strip()=='' ))
    res.append((head,out))
for r in res: print(r)
