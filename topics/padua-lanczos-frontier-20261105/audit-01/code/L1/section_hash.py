import hashlib, itertools, sys
p = sys.argv[1]
txt = open(p, encoding='utf-8').read()
lines = txt.split('\n')
# split into sections by '## ' headings (level 2 only)
secs = {}
order = []
cur = None
buf = []
for ln in lines:
    if ln.startswith('## '):
        if cur is not None:
            secs[cur] = buf
        cur = ln[3:].strip(); order.append(cur); buf = [ln]
    else:
        if cur is not None:
            buf.append(ln)
secs[cur] = buf
print(order)
target = '13325943c81b8f21760a2ed79f77ddf442bdf42609007aa108f4e4589bb7ac05'
names_sets = {
 'seven': ['Statement','Definitions','Assumptions','Depends on','Sources','Proof or evidence','Scope'],
 'six_noSources': ['Statement','Definitions','Assumptions','Depends on','Proof or evidence','Scope'],
}
found = False
for key, names in names_sets.items():
    for incl_head in (True, False):
        for strip in ('none','rstrip','strip'):
            for sep in ('\n', '\n\n', ''):
                for trail in ('', '\n'):
                    parts = []
                    for nm in names:
                        b = secs[nm] if incl_head else secs[nm][1:]
                        s = '\n'.join(b)
                        if strip == 'rstrip': s = s.rstrip('\n')
                        elif strip == 'strip': s = s.strip('\n')
                        parts.append(s)
                    data = sep.join(parts) + trail
                    h = hashlib.sha256(data.encode()).hexdigest()
                    if h == target:
                        print('MATCH', key, incl_head, strip, repr(sep), repr(trail)); found = True
print('found' if found else 'no match among variants')
