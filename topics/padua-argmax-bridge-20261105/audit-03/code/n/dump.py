import csv, collections, sys
doc = sys.argv[1]; keys = sys.argv[2:]
rows = list(csv.DictReader(open(f'out/definitions-{doc}.tsv'), delimiter='\t'))
by = collections.defaultdict(list)
for r in rows: by[r['key']].append(r)
for k in (keys or sorted(by, key=lambda k: -len(by[k]))):
    v = by.get(k, [])
    print(f"## {k} ({len(v)})")
    for r in v:
        print(f"   {r['unit']:4} {r['full']:14} {r['file'].split('/')[-1][:12]}:{r['line']} p{r['page']} eq[{r['eq']}] = {r['rhs'][:50]}")
