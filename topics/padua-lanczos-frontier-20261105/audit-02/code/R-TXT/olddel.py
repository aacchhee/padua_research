import re,sys,difflib
t=open(sys.argv[1]).read()
for s in re.split(r'\n(?=## )',t):
    title=s.split('\n',1)[0]
    m=re.search(r'OLD[^\n]*:\s*\n+```text\n(.*?)\n```',s,re.S)
    n=re.search(r'NEW[^\n]*:\s*\n+```text\n(.*?)\n```',s,re.S)
    if not (m and n): continue
    a=m.group(1).split(' '); b=n.group(1).split(' ')
    sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
    dels=[(tag,' '.join(a[i1:i2]),' '.join(b[j1:j2])[:200]) for tag,i1,i2,j1,j2 in sm.get_opcodes() if tag in('delete','replace')]
    print(title[:50], 'removed/replaced spans:',len(dels))
    for d in dels: print('   ',d[0],'OLD:',d[1][:200],'| NEW:',d[2][:120])
