import re
P='/home/user/padua_research/topics/padua-argmax-bridge-20261105/paper/sections/comparison-unified.tex'
C='/home/user/padua_research/topics/padua-argmax-bridge-20261105/companion-paper/sections/comparison-unified.tex'
def envs(path):
    t=open(path).read()
    out={}
    for m in re.finditer(r'\\begin\{(equation|align|corollary|theorem|lemma)\}(\[[^\]]*\])?\\label\{([^}]*)\}(.*?)\\end\{\1\}',t,re.S):
        out[m.group(3)]=re.sub(r'\s+',' ',m.group(4)).strip()
    return out
p=envs(P); c=envs(C)
for k in ['uc:reference-match','uc:ordinary-variation','uc:phase-allowance','uc:absolute-components','uc:sinc-row','uc:origin-variation','uc:relative-components','uc:signed-outer','uc:absolute-gate','uc:absolute-gate-formula','ul:outer-exclusion','uc:relative-gate','ul:radial-quadratic','ul:wide-polynomial','uc:relative-gate-bounds','uc:constants','uc:uniform-allowance','uc:finite-bounds']:
    a=p.get(k); b=c.get(k)
    print(k, 'SAME' if a==b else ('MISSING' if a is None or b is None else 'DIFF'))
    if a!=b and a and b:
        import difflib
        for d in difflib.ndiff([a],[b]):
            print('   ',d[:400])
