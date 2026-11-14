import difflib,sys
c=open(sys.argv[1]).read().split('\n')
p=open(sys.argv[2]).read().split('\n')
sm=difflib.SequenceMatcher(None,p,c,autojunk=False)
orig=set()
for a,b,size in sm.get_matching_blocks():
    for i in range(size): orig.add(b+i)
lo,hi=int(sys.argv[3]),int(sys.argv[4])
out=open(sys.argv[5],'w')
for i in range(lo-1,hi):
    out.write(('O ' if i in orig else '+ ')+'%4d '%(i+1)+c[i]+'\n')
