import re,sys
log=sys.argv[1]; eps=float(sys.argv[2])
blk=None; rows=[]
for line in open(log):
    if not line.startswith(" "):
        blk=line.strip(); continue
    m=re.search(r"deg\s+(\d+) N=\s*(\d+)\s+max\|Q\^TQ-I\|=([\d.e+-]+)\s+min Ritz residual=([\d.e+-]+)",line)
    if m:
        d,N,loss,res=int(m[1]),int(m[2]),float(m[3]),float(m[4])
        rows.append((blk,d,N,loss,res,loss/(eps/res)))
for r in rows: print(f"{r[0]:38s} deg{r[1]:3d} N={r[2]:4d} loss={r[3]:.1e} res={r[4]:.1e} u/res={eps/r[4]:.1e} ratio={r[5]:.2f}")
