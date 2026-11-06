import sys
sys.argv=[sys.argv[0]]+sys.argv[1:]
import bf_cosets as b
M=int(sys.argv[1]); degs=tuple(int(x) for x in sys.argv[2].split(","))
stats,hits,ex,classif=b.run(M,"all",degs)
print(stats); print(hits)
import math
cap=8*max(math.comb(n+3,3) for n in degs)
bad=[]
divs=[d for d in range(1,M+1) if M%d==0]
import itertools
for m in itertools.product(divs,repeat=3):
    pred=sorted(c for c,sz in b.predicted(m) if sz<=cap)
    if sorted(classif.get(m,[]))!=pred: bad.append((m,classif.get(m),pred))
# also orders absent from classif but predicted nonempty (subject to size cap)
print("orders seen",len(classif),"mismatch vs classification",bad)
for n,e in ex.items():
    for x in e[:2]: print("EX n=%d"%n,x)
