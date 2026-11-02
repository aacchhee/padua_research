import re,os,glob,sys
repo='/home/user/padua_research'; T=repo+'/topics/padua-argmax-alln-20261101'
files=sorted(glob.glob(T+'/**/*.md',recursive=True))+[repo+'/results/padua-argmax-alln-20261101.md']
link=re.compile(r'\]\(([^)\s]+)\)')
total=0; broken=[]; external=0; anchors=0
for f in files:
    txt=open(f).read()
    # skip fenced code blocks
    txt_nc=re.sub(r'```.*?```','',txt,flags=re.S)
    for m in link.finditer(txt_nc):
        u=m.group(1)
        if u.startswith(('http://','https://','mailto:')): external+=1; continue
        if u.startswith('#'): anchors+=1; continue
        total+=1
        p=u.split('#')[0]
        tgt=os.path.normpath(os.path.join(os.path.dirname(f),p))
        if not os.path.exists(tgt): broken.append((os.path.relpath(f,repo),u))
print('md files',len(files),'relative links',total,'external',external,'anchor-only',anchors)
print('broken',len(broken))
for b in broken: print('  ',b)
# links inside fenced proposal blocks in proposed-record-changes.md, resolved as if placed at repo root
prc=open(T+'/proposed-record-changes.md').read()
blocks=re.findall(r'```\n(.*?)```',prc,flags=re.S)
print('proposal blocks',len(blocks))
for i,b in enumerate(blocks):
    for m in link.finditer(b):
        u=m.group(1)
        if u.startswith('http'): continue
        # determine base: RESULTS/PROOF_STATUS/ID_CROSSWALK at root; batch ledger in topics/padua-batch-20261031
        for base in ('', 'topics/padua-batch-20261031'):
            tgt=os.path.normpath(os.path.join(repo,base,u.split('#')[0]))
            print(f'  block{i} base={base or "root"} {u} -> {"OK" if os.path.exists(tgt) else "MISSING"}')
