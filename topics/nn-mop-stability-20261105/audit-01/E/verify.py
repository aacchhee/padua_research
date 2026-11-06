import json, hashlib, subprocess, sys, os
R='/home/user/padua_research'
T=R+'/topics/nn-mop-stability-20261105'
def blobinfo(commit, path):
    try:
        data=subprocess.check_output(['git','-C',R,'show',f'{commit}:{path}'],stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        return None
    blob=subprocess.check_output(['git','-C',R,'rev-parse',f'{commit}:{path}']).decode().strip()
    return hashlib.sha256(data).hexdigest(), blob, len(data)
def check_rows(name, rows, cols, commits):
    print('=== ',name, len(rows), 'rows; cols', cols)
    bad=0
    for r in rows:
        if isinstance(r,dict):
            d=r
        else:
            d=dict(zip(cols,r))
        path=d.get('repository_path') or d.get('path') or d.get('source_path')
        sha=d.get('sha256'); blob=d.get('git_blob'); by=d.get('bytes')
        ok=False; res=None
        for c in commits:
            res=blobinfo(c,path) if path else None
            if res and res[0]==sha:
                ok=True; break
        if not ok:
            bad+=1
            print('MISMATCH/absent', name, d, 'actual', res)
        else:
            if blob and res[1]!=blob: print('BLOB MISMATCH',path,blob,res[1]); bad+=1
            if by is not None and res[2]!=by: print('SIZE MISMATCH',path,by,res[2]); bad+=1
    print(name,'bad',bad)
em=json.load(open(T+'/evidence-manifest.json'))
check_rows('evidence-manifest', em['files'], em['columns'], ['ff783d5','HEAD'])
print('input_inventory', em['input_inventory'], blobinfo('ff783d5', em['input_inventory'][0]))
cs=json.load(open(T+'/cold-storage.json'))
print('cold keys', cs['format'], cs['delivered'], cs.get('destination'))
print('cold source_inventory', cs['source_inventory'])
print('cold columns', cs['columns'])
print('cold rows', len(cs['files']))
for r in cs['files'][:3]: print(r)
ins=json.load(open(T+'/input-snapshot.json'))
print('snapshot', ins['source_commit'], ins['base_commit'], ins.get('reconciled_main'))
print(type(ins['files']), (ins['files'][:2] if isinstance(ins['files'],list) else list(ins['files'].items())[:2]))
print('supp', ins['supplemental_source_files'] if len(str(ins['supplemental_source_files']))<3000 else str(ins['supplemental_source_files'])[:3000])
