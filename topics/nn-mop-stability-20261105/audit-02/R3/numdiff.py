import re,subprocess,sys,collections
files=subprocess.check_output(['git','diff','--name-only','4e87fc0','d6760d7','--','topics/nn-mop-stability-20261105','results']).decode().split()
pat=re.compile(r'(?<![A-Za-z0-9_])[-+]?\d+(?:\.\d+)?(?:e[-+]?\d+)?(?:/\d+)?')
for f in files:
    if f.endswith('.json') : continue
    d=subprocess.check_output(['git','diff','-U0','4e87fc0','d6760d7','--',f]).decode()
    rem=collections.Counter();add=collections.Counter()
    for l in d.splitlines():
        if l.startswith('---') or l.startswith('+++'):continue
        if l.startswith('-'): rem.update(pat.findall(l[1:]))
        elif l.startswith('+'): add.update(pat.findall(l[1:]))
    gone=[k for k in rem if k not in add]
    new=[k for k in add if k not in rem]
    if gone or new:
        print('==',f); print('  removed-only:',gone); print('  added-only:',new[:80])
