import json,re,subprocess,sys,difflib
T='topics/padua-mz-sharp-constants-20261106/'
fm=json.load(open(T+'final-id-map.json'))
m={}
for r in fm['records']:
    m[r['provisional_id']]=r['final_id']
    for a in r['provisional_aliases']: m[a]=r['final_id']
keys=sorted(m,key=len,reverse=True)
rx=re.compile('|'.join(re.escape(k) for k in keys))
def norm(t): return rx.sub(lambda x:m[x.group(0)],t)
def show(rev,p):
    return subprocess.run(['git','show',f'{rev}:{p}'],capture_output=True,text=True).stdout
def sections(t):
    out={};cur='_pre'
    for l in t.splitlines():
        if l.startswith('## '): cur=l.strip()
        out.setdefault(cur,[]).append(l)
    return out
files=subprocess.run(['git','diff','--name-only','95d0b30','7322d4c','--',T+'theory/',T+'ideas/',T+'literature/'],capture_output=True,text=True).stdout.split()
for p in files:
    a=sections(norm(show('95d0b30',p))); b=sections(show('7322d4c',p))
    for k in sorted(set(a)|set(b)):
        if a.get(k)!=b.get(k):
            sa,sb=a.get(k,[]),b.get(k,[])
            d=[l for l in difflib.unified_diff(sa,sb,lineterm='',n=0) if l[:1] in '+-' and not l.startswith(('+++','---'))]
            print('##',p.split('/')[-2]+'/'+p.split('/')[-1],'|',k[:50],'|',len(d),'lines')
            for l in d: print('    ',l[:260])
