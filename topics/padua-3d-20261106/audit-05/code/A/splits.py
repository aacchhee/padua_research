import re,sys,pathlib
top=pathlib.Path(sys.argv[1])
files=[p for p in top.rglob('*.md') if 'audit' not in p.parts[-2] and not p.name.startswith('audit')]
idre=re.compile(r'(PD-[TN]\?[A-Za-z0-9-]+)')
recs={}
for p in files:
    t=p.read_text(errors='replace')
    m=re.match(r'#\s*(PD-[TN]\?[A-Za-z0-9-]+)',t)
    if not m: continue
    recs[m.group(1)]=(p,t)
def field(t,name):
    out=[]
    for m in re.finditer(name+r'\s*:?\s*(.{0,600})',t,re.S):
        s=m.group(1)
        # stop at next field or blank line
        s=re.split(r'\n\s*\n|Split into|Split from|Overall status|Status:',s)[0]
        out.append(s)
    return out
suffix={i.split('-',)[0]:i for i in recs}
def resolve(token):
    if token in recs: return token
    for i in recs:
        if i.endswith('-'+token) : return i
    return None
issues=[]
for cid,(p,t) in sorted(recs.items()):
    for s in field(t,'Split from'):
        if re.match(r'\s*none',s): continue
        ids=idre.findall(s)
        if not ids:
            # alias token
            tok=re.match(r'\s*([A-Za-z0-9-]+)',s)
            r=resolve(tok.group(1)) if tok else None
            ids=[r] if r else []
            if r: issues.append(f'ALIAS-ONLY parent ref in {p.relative_to(top)}: "{s.strip()[:80]}" -> {r}')
            else: issues.append(f'UNRESOLVED parent ref in {p.relative_to(top)}: "{s.strip()[:120]}"')
        for pid in ids:
            pid=pid.rstrip('.,;)')
            if pid not in recs:
                issues.append(f'parent {pid} not found (child {cid})'); continue
            pp,pt=recs[pid]
            into=' '.join(field(pt,'Split into'))
            if cid not in into and p.name not in into:
                issues.append(f'NONRECIPROCAL: child {cid} ({p.relative_to(top)}) says from {pid} ({pp.relative_to(top)}), parent Split into: "{into.strip()[:150]}"')
    for s in field(t,'Split into'):
        if re.match(r'\s*none',s): continue
        for kid in idre.findall(s):
            kid=kid.rstrip('.,;)')
            if kid not in recs: issues.append(f'child {kid} not found (parent {cid})'); continue
            kp,kt=recs[kid]
            fr=' '.join(field(kt,'Split from'))
            if cid not in fr and p.name not in fr and cid.split('codex-')[-1] not in fr:
                issues.append(f'NONRECIPROCAL-INTO: parent {cid} lists {kid} but child Split from: "{fr.strip()[:150]}"')
print(len(recs),'records')
print('\n'.join(issues))
