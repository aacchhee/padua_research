"""M6: numbered display/statement blocks changed ad908acb->8937d3b, and paper/companion equality."""
import re, sys
R, T = sys.argv[1], 'topics/padua-argmax-bridge-20261105'
ENV = r'(equation|align|gather|multline|flalign|theorem|lemma|proposition|corollary|remark)'
pat = re.compile(r'\\begin\{' + ENV + r'\}(.*?)\\end\{\1\}', re.S)
files = ['introduction', 'preliminaries', 'corner-unified', 'localization-unified', 'comparison-unified', 'certification-unified']
def blocks(tree, prod):
    out = []
    for f in files:
        s = open(f'{R}/{tree}/{T}/{prod}/sections/{f}.tex').read()
        s = re.sub(r'(?m)%.*$', '', s)
        for m in pat.finditer(s):
            body = m.group(2)
            lab = re.findall(r'\\label\{([^}]*)\}', body)
            key = lab[0] if lab else f'{f}:{m.group(1)}:nolabel:{body[:40]!r}'
            out.append((key, m.group(1), re.sub(r'\s+', ' ', body).strip()))
    return out
res = {}
for tree in ('old', 'new'):
    for prod in ('paper', 'companion-paper'):
        res[tree, prod] = blocks(tree, prod)
for prod in ('paper', 'companion-paper'):
    print(prod, 'old blocks', len(res['old', prod]), 'new blocks', len(res['new', prod]))
newp = dict((k, (e, b)) for k, e, b in res['new', 'paper'])
newc = dict((k, (e, b)) for k, e, b in res['new', 'companion-paper'])
oldp = dict((k, (e, b)) for k, e, b in res['old', 'paper'])
oldc = dict((k, (e, b)) for k, e, b in res['old', 'companion-paper'])
labeled = [k for k, e, b in res['new', 'paper'] if ':nolabel:' not in k]
print('labelled paper blocks', len(labeled), 'companion', len([k for k in newc if ':nolabel:' not in k]))
print('labels only in one text:', sorted(set(k for k in newp if ':nolabel:' not in k) ^ set(k for k in newc if ':nolabel:' not in k)))
changed = []
for k in labeled:
    if k not in newc: continue
    cp = oldp.get(k, (None, None))[1] != newp[k][1]
    cc = oldc.get(k, (None, None))[1] != newc[k][1]
    same = newp[k][1] == newc[k][1]
    if cp or cc or not same:
        changed.append((k, cp, cc, same))
for k, cp, cc, same in changed:
    print(f'  {k:32s} paper_changed={cp!s:5} companion_changed={cc!s:5} identical_now={same}')
# unlabelled statement blocks (e.g. remark) comparisons
