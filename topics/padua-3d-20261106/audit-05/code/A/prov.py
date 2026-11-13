import json,glob,os,re,subprocess,hashlib,sys
top='topics/padua-3d-20261106'
commits=subprocess.check_output(['git','rev-list','04ef28b..ec5c089']).decode().split()+['04ef28b']
# map sha256 -> (path, commits) for all code files across batch commits
index={}
for c in commits:
    files=subprocess.check_output(['git','ls-tree','-r','--name-only',c,'--',top+'/code','tracks/lattice-unisolvence/code']).decode().split()
    for f in files:
        b=subprocess.check_output(['git','show',f'{c}:{f}'])
        h=hashlib.sha256(b).hexdigest()
        index.setdefault(h,set()).add((f.split('/')[-1],c[:7]))
new=subprocess.check_output(['git','diff','--name-only','--diff-filter=A','04ef28b','ec5c089','--',top+'/evidence']).decode().split()
for f in new:
    d=json.loads(subprocess.check_output(['git','show','ec5c089:'+f]))
    found=[]
    def walk(o,key=''):
        if isinstance(o,dict):
            p=o.get('path'); h=o.get('sha256')
            if isinstance(p,str) and isinstance(h,str) and p.endswith(('.py','.cpp')):
                found.append((os.path.basename(p),h))
            for k,v in o.items():
                if k in ('source_sha256','code_sha256','checker_sha256','producer_sha256') and isinstance(v,str): found.append((k,v))
                elif k in ('code_sha256',) and isinstance(v,dict):
                    for kk,vv in v.items(): found.append((kk,vv))
                walk(v,k)
        elif isinstance(o,list):
            for v in o: walk(v,key)
    walk(d)
    out=[]
    for name,h in found:
        m=index.get(h)
        cur = any(c=='ec5c089' for _,c in m) if m else False
        out.append(f"{name}:{'CUR' if cur else ('OLD:'+','.join(sorted(c for _,c in m)) if m else 'NOMATCH')}")
    print(os.path.basename(f), ' '.join(sorted(set(out))))
