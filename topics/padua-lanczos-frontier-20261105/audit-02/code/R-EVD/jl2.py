import os,re,subprocess,urllib.parse
D='topics/padua-lanczos-frontier-20261105'
ch=subprocess.check_output(['git','diff','--name-only','45646d7','HEAD','--',D,'results/'],text=True).split()
lk=re.compile(r'\[[^\]]*\]\(([^)\s]+)\)')
out={'ok':0,'fenced_or_quoted':0,'broken':[]}
for f in ch:
    if not f.endswith('.md'): continue
    fence=False
    for i,line in enumerate(open(f),1):
        if line.lstrip().startswith('```') or line.lstrip().startswith('~~~'): fence=not fence; continue
        for m in lk.finditer(line):
            t=m.group(1)
            if re.match(r'[a-z]+:',t) or t.startswith('#'): continue
            path=urllib.parse.unquote(t.partition('#')[0])
            p=os.path.normpath(os.path.join(os.path.dirname(f),path))
            if os.path.exists(p): out['ok']+=1; continue
            if fence or line.startswith('>') or line.startswith('    '): out['fenced_or_quoted']+=1; continue
            out['broken'].append((f,i,t))
print(out['ok'],out['fenced_or_quoted'],len(out['broken']))
for b in out['broken'][:10]: print(b)
