import sys,re
txt=open(sys.argv[1]).read().split('\f')
for q in sys.argv[2:]:
    hits=[i+1 for i,p in enumerate(txt) if q in re.sub(r'\s+',' ',p)]
    print(repr(q), hits[:8])
