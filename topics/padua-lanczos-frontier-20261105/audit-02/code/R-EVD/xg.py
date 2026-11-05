import json,re,sys
D=sys.argv[1]
X=json.load(open(D+'/evidence/l7-cross-group.json'))
txt=open(D+'/audit-01/code/L7G1/compare-l7run_haswell.txt').read()
aud={}
for m in re.finditer(r"tanh boundary (\S+) / (\S+) winner (\S+) ratios\(comparator/winner\) (\S+);(\S+) (\S+)",txt):
    a,b,w,r1,r2,g=m.groups(); aud[frozenset((a,b))]=(w,float(r1),float(r2),g)
print(len(aud), sum(v[3]=='cross-group' for v in aud.values()))
for d in X['directions']:
    k=frozenset((d['full'],d['window'])); w,r1,r2,g=aud[k]
    fw=d['full_over_window']
    comp_over_win=[x if d['winner']==d['window'] else 1/x for x in fw]
    print(d['full'],d['window'],d['winner']==w,g,[round(x,4) for x in comp_over_win],(r1,r2), all(abs(round(x,4)-y)<1.5e-4 for x,y in zip(comp_over_win,(r1,r2))))
# check worker pins equal summary manifest
S_=json.load(open(D+'/evidence/l7-suite-summary.json'))
print('worker pins == summary manifest', X['source_workers']==S_['worker_json_manifest'])
fulls=['upstream_xy','upstream_yx','dev_full','mirror_full','alt_full','adapt_full']; wins=['dev_window','mirror_window','alt_window','adapt_window']
print(len(fulls)*len(wins), 24*64)
same=S_['paired_seed_method_comparisons_same_reorth_group']; print('same-group pairs',len(same), sum(v['a_better_both']+v['b_better_both'] for v in same.values()), set(v['paired_cells'] for v in same.values()))
print(sorted({tuple(p.split(' / ')) for p in same} and {m for p in same for m in p.split(' / ')}))
