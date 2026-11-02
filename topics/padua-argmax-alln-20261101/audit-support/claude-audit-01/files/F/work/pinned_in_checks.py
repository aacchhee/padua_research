import re,hashlib,subprocess,glob,os
repo='/home/user/padua_research'; T='topics/padua-argmax-alln-20261101'
def blob(p):
    r=subprocess.run(['git','-C',repo,'show','HEAD:'+p],capture_output=True)
    return r.stdout if r.returncode==0 else None
tree=[l for l in subprocess.run(['git','-C',repo,'ls-tree','-r','--name-only','HEAD'],capture_output=True,text=True).stdout.split('\n') if l.startswith(T+'/') or l.startswith('results/')]
hashes={}
for p in tree:
    b=blob(p); hashes.setdefault(hashlib.sha256(b).hexdigest(),[]).append(p)
docs=sorted(glob.glob(repo+'/'+T+'/gated/checks/*.md'))+[repo+'/'+T+'/independent-checks-part3.md',repo+'/'+T+'/independent-checks-pairing.md',repo+'/'+T+'/independent-checks-claude-records.md',repo+'/'+T+'/independent-checks-claude-observations-audit.md']
for d in docs:
    txt=open(d).read()
    rows=re.findall(r'`([^`]+)`[^\n]*?`?([0-9a-f]{64})`?',txt)
    stale=[];ok=0;unk=[]
    for path,h in rows:
        cand=[q for q in tree if q.endswith(path.lstrip('./'))]
        if h in hashes: ok+=1; continue
        if cand:
            cur=hashlib.sha256(blob(cand[0])).hexdigest()
            stale.append((path,h[:12],'now',cur[:12]))
        else: unk.append((path,h[:12]))
    print('==',os.path.basename(d),'rows',len(rows),'match-current',ok,'differs-from-current',len(stale),'no-local-path',len(unk))
    for s in stale: print('   DIFF',s)
