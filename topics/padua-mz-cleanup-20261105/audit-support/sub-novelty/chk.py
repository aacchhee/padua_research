import re
p=open('topics/padua-mz-cleanup-20261105/proposed-record-changes.md').read()
blocks=re.findall(r'```markdown\n(.*?)```',p,flags=re.S)
files=['PAPER_MAP.md','PAPER_MAP.md','state/CURRENT.md','state/CURRENT.md','tracks/mz-constants/README.md','tracks/mz-constants/README.md']
for i,(b,f) in enumerate(zip(blocks,files)):
    txt=open(f).read()
    print(f,'old' if i%2==0 else 'new','occurs',txt.count(b))
    if i%2==0 and txt.count(b)==0:
        for j,l in enumerate(b.split('\n')):
            if l and l not in txt: print('  missing line',j,l[:120])
