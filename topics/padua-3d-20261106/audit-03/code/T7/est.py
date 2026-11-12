import sys, numpy as np, math
sys.path.insert(0,'.')
from aud_groups import groups, points
G=0;S=0;W=0;orbit_total=0;prime=0;m10=0
for m in range(10,81):
    for g in groups(m):
        P=points(g); mj=[len(np.unique(P[:,j])) for j in range(3)]
        if min(mj)<=2 or max(mj)>20: continue
        G+=1; s=math.prod(x+1 for x in mj); S+=s; W+=s*m
print(G,S,W)
