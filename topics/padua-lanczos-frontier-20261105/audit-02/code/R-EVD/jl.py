import json,os,re,subprocess,sys,urllib.parse
D='topics/padua-lanczos-frontier-20261105'
ch=subprocess.check_output(['git','diff','--name-only','45646d7','HEAD','--',D,'results/'],text=True).split()
allj=[f for f in subprocess.check_output(['git','ls-files',D],text=True).split() if f.endswith('.json')]
big=[];bad=[]
for f in allj:
    b=open(f,'rb').read()
    try: json.loads(b)
    except Exception as e: bad.append((f,str(e)))
    if len(b)>=16384: big.append((f,len(b)))
print('tracked json',len(allj),'parse-fail',bad,'>=16KiB',big)
print('changed json',[ (f,os.path.getsize(f)) for f in ch if f.endswith('.json')])
tot=sum(os.path.getsize(f) for f in allj); print('total json bytes',tot)
# links
lk=re.compile(r'\[[^\]]*\]\(([^)\s]+)\)')
broken=[];n=0
for f in ch:
    if not f.endswith('.md') or not os.path.exists(f): continue
    for m in lk.finditer(open(f).read()):
        t=m.group(1)
        if re.match(r'[a-z]+:',t) or t.startswith('#'): continue
        path,_,frag=t.partition('#'); path=urllib.parse.unquote(path)
        p=os.path.normpath(os.path.join(os.path.dirname(f),path)); n+=1
        if not os.path.exists(p): broken.append((f,t)); continue
        tracked=subprocess.run(['git','ls-files','--error-unmatch',p],capture_output=True).returncode==0 or os.path.isdir(p)
        if not tracked: broken.append((f,t,'UNTRACKED'))
print('links checked',n,'broken',broken)
