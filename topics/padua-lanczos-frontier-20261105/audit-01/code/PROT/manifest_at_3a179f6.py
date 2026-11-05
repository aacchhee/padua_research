# Recompute check_manifest.py's inventory from the committed tree of 3a179f6 (git show), read-only.
import hashlib, json, subprocess
root='/home/user/padua_research'; rev='3a179f68ecbed20dc7e15862da842ed6116aa375'
topic='topics/padua-lanczos-frontier-20261105/'
names=subprocess.check_output(['git','ls-tree','-r','--name-only',rev],cwd=root,text=True).splitlines()
files={}
for name in sorted(names):
    if not(name.startswith(topic) or name=='results/padua-lanczos-frontier-20261105.md'):continue
    rel=name[len(topic):] if name.startswith(topic) else None
    if name==topic+'evidence-manifest.json' or name==topic+'LOG.md' or '/handoffs/' in '/'+name or '__pycache__' in name: continue
    b=subprocess.check_output(['git','show',rev+':'+name],cwd=root)
    key=rel if rel is not None else '@'+name
    files[key]=[len(b),hashlib.sha256(b).hexdigest()]
b=(json.dumps({'files':files},sort_keys=True,separators=(',',':'))+'\n').encode()
m=json.loads(subprocess.check_output(['git','show',rev+':'+topic+'evidence-manifest.json'],cwd=root))
print(len(files), len(b), hashlib.sha256(b).hexdigest(), 'expected', m['inventory']['files'], m['inventory']['bytes'], m['inventory']['sha256'])
print('MATCH' if hashlib.sha256(b).hexdigest()==m['inventory']['sha256'] else 'MISMATCH')
