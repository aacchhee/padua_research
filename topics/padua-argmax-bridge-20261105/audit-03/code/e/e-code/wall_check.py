import json,sys,tarfile,statistics
P={}
with tarfile.open(sys.argv[1],'r|gz') as t:
  for m in t:
    if m.isfile() and m.name.endswith(('summary.json','final-accounting.json')) and '/jobs/' in m.name: P[m.name]=json.loads(t.extractfile(m).read())
for mode in ('produce','verify'):
  sw=[v['wall_seconds'] for k,v in P.items() if k.endswith('/'+mode+'/summary.json')]
  cpu=[(v['total_CPU_through_summary'],int(k.split('/')[3])) for k,v in P.items() if k.endswith('/'+mode+'/final-accounting.json')]
  print(mode, len(sw), round(sum(sw),6), max(sw), max(cpu), min(cpu))
