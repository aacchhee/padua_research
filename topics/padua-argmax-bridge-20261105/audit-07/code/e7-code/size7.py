import subprocess, sys
SRC = ('.py', '.sh', '.c', '.cpp', '.h', '.tex', '.bib', '.diff')
R='/home/user/padua_research'
def inv(ref):
    out = subprocess.check_output(['git','-C',R,'ls-tree','-rl',ref], text=True)
    rows = {}
    for line in out.splitlines():
        meta, path = line.split('\t', 1)
        mode, typ, blob, size = meta.split()
        if typ != 'blob': continue
        base = path.rsplit('/', 1)[-1]
        if base == '.gitignore' or path.endswith(SRC): continue
        if path.endswith('.md') and base != 'COLD_STORAGE.md': continue
        rows[path] = (blob, int(size))
    return rows
main=inv('99a9b1d161e41a80c4fd425b63022c681fbe8779'); head=inv('HEAD'); old=inv('f4e8d8d')
tm=sum(s for _,s in main.values()); th=sum(s for _,s in head.values())
P='topics/padua-argmax-bridge-20261105/'
topic_head=sum(s for p,(_,s) in head.items() if p.startswith(P))
res_head=sum(s for p,(_,s) in head.items() if p.startswith('results/padua-argmax-bridge'))
topic_main=sum(s for p,(_,s) in main.items() if p.startswith(P))
print('main_total',tm,'head_total',th,'head-main',th-tm)
print('topic_dir_head',topic_head,'topic_dir_main',topic_main,'results_file_head',res_head)
only_head=sum(s for p,(b,s) in head.items() if p not in main); diff_blob=[(p,s,main[p][1]) for p,(b,s) in head.items() if p in main and main[p][0]!=b]
print('head paths not in main',only_head, 'changed-blob paths',len(diff_blob), sum(s-m for p,s,m in diff_blob))
only_main=[(p,s) for p,(b,s) in main.items() if p not in head]
print('main paths not in head',len(only_main),sum(s for p,s in only_main))
pos=sum(s for p,(b,s) in head.items() if p not in main)+sum(max(0,s-m) for p,s,m in diff_blob)
print('positive deltas head vs main',pos,'main+pos',tm+pos,'+2087',tm+pos+2087)
print('union(main + topic share)',tm+topic_head,'+2087',tm+topic_head+2087)
# versus f4e8d8d
posf=sum(s for p,(b,s) in head.items() if p not in old)+sum(max(0,s-old[p][1]) for p,(b,s) in head.items() if p in old and old[p][0]!=b)
print('f4e8d8d total',sum(s for _,s in old.values()),'pos deltas f4e8->HEAD',posf)
for p,s,m in diff_blob: print(' changed',p,m,'->',s)
