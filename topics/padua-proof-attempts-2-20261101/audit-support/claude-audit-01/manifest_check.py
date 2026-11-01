import json, subprocess, hashlib, sys, os, collections
C='4265bb94f987ce77d89cd5e15a8c435cbd1411d0'
T='topics/padua-proof-attempts-2-20261101'
m=json.loads(subprocess.check_output(['git','show',f'{C}:{T}/evidence-manifest.json']))
def show(commit,path):
    return subprocess.run(['git','show',f'{commit}:{path}'],capture_output=True).stdout
def blob(commit,path):
    r=subprocess.run(['git','rev-parse',f'{commit}:{path}'],capture_output=True,text=True); return r.stdout.strip()
res=collections.Counter(); bad=[]
for r in m['inputs']:
    b=show(r['commit'],r['path'])
    ok = hashlib.sha256(b).hexdigest()==r['sha256'] and len(b)==r['bytes'] and blob(r['commit'],r['path'])==r['git_blob']
    res['in_ok' if ok else 'in_bad']+=1
    if not ok: bad.append(('in',r['path'],r['commit']))
    pin=m['pins'].get(r['source'])
    if pin!=r['commit']: bad.append(('pinmismatch',r['path'],r['source']))
for c in m['changed_compared_inputs']:
    pass
outs={r['path']:r for r in m['outputs']}
for p,r in outs.items():
    b=show(C,p)
    ok= hashlib.sha256(b).hexdigest()==r['sha256'] and len(b)==r['bytes']
    if 'git_blob' in r: ok = ok and blob(C,p)==r['git_blob']
    res['out_ok' if ok else 'out_bad']+=1
    if not ok: bad.append(('out',p))
# coverage: every file in topic at C except exclusions
files=subprocess.check_output(['git','ls-tree','-r','--name-only',C,T],text=True).split()
missing=[f for f in files if f not in outs]
print(res, 'bad', bad[:20])
print('topic files',len(files),'outputs',len(outs),'not in manifest:',missing)
print('exclusions',m['exclusions'])
# size limits: generated files = outputs/ ?
sizes=[(r['bytes'],p) for p,r in outs.items() if '/outputs/' in p]
print('outputs/ files',len(sizes),'total',sum(s for s,_ in sizes),'max',max(sizes))
print('changed_compared', json.dumps(m['changed_compared_inputs'])[:1500])
print('pins', json.dumps(m['pins'],indent=0))
