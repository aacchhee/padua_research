import hashlib, json, subprocess, sys, os
repo='/home/user/padua_research'
T='topics/padua-argmax-alln-20261101'
def git(*a): return subprocess.run(['git','-C',repo]+list(a),capture_output=True).stdout
man=json.loads(git('show','HEAD:'+T+'/evidence-manifest.json'))
bad=[]; n=0
paths=set()
for f in man['files']:
    n+=1; paths.add(f['path'])
    blob=git('show','HEAD:'+f['path'])
    if len(blob)!=f['bytes'] or hashlib.sha256(blob).hexdigest()!=f['sha256']:
        bad.append(f['path'])
    # also compare working tree
    wt=open(os.path.join(repo,f['path']),'rb').read()
    if wt!=blob: bad.append('WORKTREE-DIFF '+f['path'])
print('manifest entries',n,'mismatches',bad)
# files at HEAD in topic not in manifest
tree=[l for l in git('ls-tree','-r','--name-only','HEAD').decode().split('\n') if l.startswith(T+'/')]
notin=[p for p in tree if p not in paths]
print('topic files at HEAD not in manifest:',notin)
print('manifest paths not at HEAD:',[p for p in paths if p not in tree and not p.startswith('results/')])
# pinned hashes
pins={'d3 certificate':(T+'/outputs/gated/d3_edge_certificate.json','0d660fc70e9db06624d6f8bd82371602c9f6d540b01124824e264624de0385b7'),
 'd3 checker':(T+'/code/gated/d3_edge_check.py','5f43f69a427c415542848f8ae9e337c69b3a5b8f822e78db38e095a0a2c9a358'),
 'd3 report':(T+'/gated/checks/d3-r01.md','f6733e2af13d2bd12f207d9876139ec58efdde958ee895401a1288bc9adbfad3'),
 'd3 receipt':(T+'/outputs/gated/check_d3_r01_receipt.json','d77ee6d68926d3b19eaf663a6837a5fcc9d9115fec0db36f26076cd37bf539b'),
 'manifest':(T+'/evidence-manifest.json','16eb0708715c3abb5b7ab7011cd9675ab8bcb12b9f371aef927edb1faf19d038')}
for k,(p,h) in pins.items():
    blob=git('show','HEAD:'+p)
    print(k,p,len(blob),'MATCH' if hashlib.sha256(blob).hexdigest()==h else 'MISMATCH '+hashlib.sha256(blob).hexdigest())
# sizes
outs=[(len(git('show','HEAD:'+p)),p) for p in tree if '/outputs/' in p]
rec=T+'/outputs/part3/packaging-validation.json'
print('outputs/ files',len(outs),'total',sum(s for s,_ in outs),'excl receipt',sum(s for s,p in outs if p!=rec),'largest',max(outs))
print('any >1MB:',[x for x in outs if x[0]>1_000_000])
