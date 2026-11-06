# Regenerate ONLY the binary64 raw targets with developer native/C4 code on this platform,
# compare to committed hex (platform-dependence probe; not an independent formulation).
import sys, json, importlib.util, platform
from pathlib import Path
CODE=Path('/home/user/padua_research/topics/nn-mop-stability-20261105/code')
sys.path.insert(0,str(CODE))
spec=importlib.util.spec_from_file_location('nm',CODE/'native_mixed.py'); nm=importlib.util.module_from_spec(spec); spec.loader.exec_module(nm)
ref=json.load(open(sys.argv[1]))
print(platform.python_version(), nm.np.__version__, nm.scipy.__version__)
F=('a1','a2','b1','b2')
for c in ref['cases']:
    N,fam,m=c['N'],c['family'],c['method']
    raw=nm.c4.compute(N,fam)[0] if m=='c4' else nm.compute(N,fam,m)[0]
    diff=0; maxrel=0
    for row in c['raw_coefficients']:
        nu=tuple(row['nu'])
        for f in F:
            a=float(raw[nu][f]); b=float.fromhex(row[f])
            if a.hex()!=row[f]:
                diff+=1; maxrel=max(maxrel,abs(a-b)/max(abs(b),1e-300))
    print(fam,N,m,'differing_entries=%d/%d'%(diff,4*len(c['raw_coefficients'])),'maxrel=%.3g'%maxrel)
