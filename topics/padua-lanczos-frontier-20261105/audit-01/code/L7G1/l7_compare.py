import json, sys, itertools, pathlib
S=pathlib.Path(sys.argv[1]); REPO=pathlib.Path(sys.argv[2])
D=REPO/'topics/padua-lanczos-frontier-20261105'
summ=json.load(open(D/'evidence/l7-suite-summary.json'))
ind=json.load(open(D/'evidence/l7-independent.json'))
rows={}
for p in S.glob('*/*-202611050[12].json'):
    r=json.loads(p.read_text()); rows[r['domain'],r['seed']]=r
refs={(r['domain'],r['seed'],r['degree']):r for r in summ['references']}
indc={(r['domain'],r['seed'],r['n']):r for r in ind['cases']}
print('== reference screen comparison (mine vs committed summary)')
for (d,s),r in sorted(rows.items()):
    for c in r['cases']:
        a=c['reference']; b=refs[d,s,c['n']]
        rel=lambda k: abs(a[k]-b[k])/max(abs(b[k]),1e-300)
        mrep=max(m['training_replay_max'] for m in c['methods'].values())
        print(d,s,c['n'],'trusted',a['trusted'],b['trusted'],'kappa relerr %.2e'%rel('kappa'),'rank',a['rank'],b['rank'],
              'spangap %.3e vs %.3e'%(a['double_ld_span_gap'],b['double_ld_span_gap']),'LDgram %.2e vs %.2e'%(a['longdouble_gram_max'],b['longdouble_gram_max']),
              'replaymax %.6g vs indep %.6g'%(mrep,indc[d,s,c['n']]['replay_max']))
    print(' own/L2 Q max', max(v.get('old_Q_entry_max',0.) for v in r['checks'].values() if isinstance(v,dict)),
          'yx-dev', r['checks']['upstream_yx_vs_dev_entry_max'],'adapt full/window parent diffs', r['checks']['adaptive_full_window_parent_differences'])
print('== resolved losses (accepted reference only)')
losses=[]
for (d,s),r in sorted(rows.items()):
    for c in r['cases']:
        if not c['reference']['trusted']: continue
        for tn,t in c['targets'].items():
            for lab,m in t['methods'].items():
                for dist in ('uniform','boundary'):
                    if m[dist]['resolved_loss']: losses.append((d,s,c['n'],tn,lab,dist,m[dist]['rel_l2'],t['reference'][dist]['rel_l2'],m[dist]['difference_vs_reference']))
for l in losses: print(' ',l[:6],'err %.4e ref %.4e diff %.4e'%l[6:])
print(' count',len(losses))
# recompute flags from stored numbers independently of stored boolean
eps=2.0**-52
mism=0; cells=0; near=[]
for (d,s),r in sorted(rows.items()):
    for c in r['cases']:
        kap=c['reference']['kappa']; tr=c['reference']['trusted']
        for tn,t in c['targets'].items():
            for lab,m in t['methods'].items():
                for dist in ('uniform','boundary'):
                    e=m[dist]['rel_l2']; re=t['reference'][dist]['rel_l2']; df=m[dist]['difference_vs_reference']
                    flag=bool(tr and e>2*re and df>max(1e-10,100*eps*kap)); cells+=1
                    if flag!=m[dist]['resolved_loss']: mism+=1
                    if tr:
                        # margin to thresholds
                        mr=min(abs(e/(2*re)-1), abs(df/max(1e-10,100*eps*kap)-1))
                        near.append((mr,d,s,c['n'],tn,lab,dist,e/(2*re),df/max(1e-10,100*eps*kap)))
print(' recomputed-flag mismatches',mism,'of',cells)
near.sort(); print(' closest-to-threshold accepted cells:'); [print('  ',x) for x in near[:8]]
print('== paired directions (both seeds) where both seeds present')
groups=[['upstream_xy','upstream_yx','dev_full','mirror_full','alt_full','adapt_full'],['dev_window','mirror_window','alt_window','adapt_window']]
allm=groups[0]+groups[1]
for d in sorted({d for d,s in rows}):
    if (d,2026110501) not in rows or (d,2026110502) not in rows: continue
    for c1,c2 in zip(rows[d,2026110501]['cases'],rows[d,2026110502]['cases']):
        if not(c1['reference']['trusted'] and c2['reference']['trusted']): continue
        for tn in c1['targets']:
            for dist in ('uniform','boundary'):
                for a,b in itertools.combinations(allm,2):
                    ra=[c['targets'][tn]['methods'][a][dist]['rel_l2']/c['targets'][tn]['methods'][b][dist]['rel_l2'] for c in (c1,c2)]
                    w=b if min(ra)>2 else a if max(ra)<.5 else None
                    same=any(a in g and b in g for g in groups)
                    if w: print(' ',d,c1['n'],tn,dist,a,'/',b,'winner',w,'ratios(comparator/winner) %.4f;%.4f'%tuple((x if w==b else 1/x) for x in ra),'SAME-GROUP' if same else 'cross-group')
