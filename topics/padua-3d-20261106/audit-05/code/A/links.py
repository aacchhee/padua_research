import re,sys,os,subprocess,unicodedata
root=sys.argv[1]
files=subprocess.check_output(['git','diff','--name-only','--diff-filter=AM','04ef28b','ec5c089']).decode().split()
files=[f for f in files if f.endswith('.md')]
def slug(h):
    h=h.strip().lower()
    h=re.sub(r'[^\w\- ]','',h)  # keep word chars, hyphen, space
    return h.replace(' ','-')
anchors={}
def get_anchors(p):
    if p in anchors: return anchors[p]
    s=set(); counts={}
    try:
        for line in open(p,encoding='utf-8'):
            m=re.match(r'^(#{1,6})\s+(.*?)\s*#*\s*$',line)
            if m:
                b=slug(m.group(2));
                if b in counts: counts[b]+=1; b2=f'{b}-{counts[b]}'
                else: counts[b]=0; b2=b
                s.add(b2)
    except FileNotFoundError: pass
    anchors[p]=s; return s
bad=0; total=0
for f in files:
    p=os.path.join(root,f)
    txt=open(p,encoding='utf-8').read()
    txt=re.sub(r'`[^`\n]*`','',txt)
    for m in re.finditer(r'\]\(([^)\s]+)\)',txt):
        t=m.group(1)
        if re.match(r'[a-z]+:',t): continue
        total+=1
        path,_,anc=t.partition('#')
        tp=os.path.normpath(os.path.join(os.path.dirname(p),path)) if path else p
        if not os.path.exists(tp):
            bad+=1; print('MISSING',f,t); continue
        if anc and tp.endswith('.md'):
            if anc not in get_anchors(tp):
                bad+=1; print('ANCHOR',f,t)
print('files',len(files),'links',total,'bad',bad)
