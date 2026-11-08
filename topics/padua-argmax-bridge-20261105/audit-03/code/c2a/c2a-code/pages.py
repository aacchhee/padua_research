import sys, re
txt = open(sys.argv[1], encoding='utf-8', errors='replace').read().split('\f')
phr = [l.strip() for l in open(sys.argv[2]) if l.strip()]
for p in phr:
    key = re.sub(r'\s+', ' ', p)
    hits = [i+1 for i, pg in enumerate(txt) if key in re.sub(r'\s+', ' ', pg)]
    print('%-55s pages %s' % (p[:55], hits[:6]))
