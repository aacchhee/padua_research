import sys
t=open('/tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/audit4/build/text/companion.txt').read()
pages=t.split('\f')
for q in sys.argv[1:]:
    hits=[i+1 for i,p in enumerate(pages) if q in p.replace('\n',' ')]
    print(repr(q),hits[:8])
