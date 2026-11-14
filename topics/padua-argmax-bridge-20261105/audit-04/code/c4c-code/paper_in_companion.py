import sys, difflib
P='/home/user/padua_research/topics/padua-argmax-bridge-20261105/paper/sections/comparison-unified.tex'
C='/home/user/padua_research/topics/padua-argmax-bridge-20261105/companion-paper/sections/comparison-unified.tex'
p=open(P).read().split('\n'); c=open(C).read().split('\n')
# companion range 1990..4020 -> find paper lines in that region
cs=set(l.strip() for l in c[1989:4020])
call='\n'.join(c)
lo,hi=int(sys.argv[1]),int(sys.argv[2])
miss=[]
for i in range(lo-1,hi):
    s=p[i].strip()
    if not s: continue
    if s in cs: continue
    # try substring match in companion range
    if s in '\n'.join(c[1989:4020]): continue
    miss.append((i+1,s))
for i,s in miss: print(i,s)
print('missing',len(miss))
