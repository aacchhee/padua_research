"""Reference-conditioned finite summary; never attributes rejected-reference rows."""
import hashlib, itertools, json, pathlib
ROOT=pathlib.Path(__file__).resolve().parents[3]
TOP=pathlib.Path(__file__).resolve().parents[1]
RAW=pathlib.Path('/tmp/padua-lanczos-frontier-l7-suite')
def main():
 files=sorted(RAW.glob('*/*/*-202611050[12].json'))
 rows=[json.loads(p.read_text()) for p in files]
 by={(r['domain'],r['seed']):r for r in rows};table=[];losses=[];pairs={};max_replay=0.;max_qdiff=0.
 for r in rows:
  max_qdiff=max(max_qdiff,max(v.get('old_Q_entry_max',0.) for v in r['checks'].values() if isinstance(v,dict)))
  for c in r['cases']:
   ref=c['reference'];table.append({'domain':r['domain'],'seed':r['seed'],'degree':c['n'],**ref})
   max_replay=max(max_replay,max(m['training_replay_max'] for m in c['methods'].values()))
   if not ref['trusted']:continue
   for tn,t in c['targets'].items():
    for label,m in t['methods'].items():
     for dist in ['uniform','boundary']:
      if m[dist]['resolved_loss']:losses.append({'domain':r['domain'],'seed':r['seed'],'degree':c['n'],'target':tn,'method':label,'distribution':dist,'error':m[dist]['rel_l2'],'reference_error':t['reference'][dist]['rel_l2'],'prediction_difference':m[dist]['difference_vs_reference'],'gap':c['methods'][label]['gap_raw'],'gram_2':c['methods'][label]['gram_2']})
 for d in ['disk','lshape','triangle','sector']:
  if not all((d,s) in by for s in [2026110501,2026110502]):continue
  for c1,c2 in zip(by[d,2026110501]['cases'],by[d,2026110502]['cases']):
   if not(c1['reference']['trusted'] and c2['reference']['trusted']):continue
   for tn in c1['targets']:
    for dist in ['uniform','boundary']:
     for group in [['upstream_xy','upstream_yx','dev_full','mirror_full','alt_full','adapt_full'],['dev_window','mirror_window','alt_window','adapt_window']]:
      for a,b in itertools.combinations(group,2):
       ratios=[c['targets'][tn]['methods'][a][dist]['rel_l2']/c['targets'][tn]['methods'][b][dist]['rel_l2'] for c in [c1,c2]]
       # A direction is accepted only if both errors improve by strictly more than2.
       winner=b if min(ratios)>2 else a if max(ratios)<.5 else None
       key=f'{a} / {b}';entry=pairs.setdefault(key,{'paired_cells':0,'a_better_both':0,'b_better_both':0,'mixed_or_below_threshold':0,'examples':[]});entry['paired_cells']+=1
       if winner:
        entry['a_better_both' if winner==a else 'b_better_both']+=1
        if len(entry['examples'])<3:entry['examples'].append({'domain':d,'degree':c1['n'],'target':tn,'distribution':dist,'winner':winner,'a_over_b_ratios':ratios})
       else:entry['mixed_or_below_threshold']+=1
 out={'status':'MEASURED; finite reference-conditioned developer execution; independent review pending','scope':{'domain_seed_runs':len(rows),'degree_cases':len(table),'accepted_reference_cases':sum(r['trusted'] for r in table),'rejected_reference_cases':sum(not r['trusted'] for r in table),'methods':10,'targets':4,'test_distributions':2},'worker_elapsed_seconds_sum':sum(r['elapsed_seconds'] for r in rows),'maximum_own_L2_Q_entry_discrepancy':max_qdiff,'maximum_training_replay_all_raw_cases':max_replay,'references':table,'accepted_reference_resolved_losses':losses,'paired_seed_method_comparisons_same_reorth_group':pairs,'worker_json_manifest':[{'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files]}
 full=RAW/'aggregate-full.json';full.write_text(json.dumps(out,indent=1)+'\n')
 out['full_aggregate']={'path':str(full),'sha256':hashlib.sha256(full.read_bytes()).hexdigest(),'bytes':full.stat().st_size}
 grouped={}
 for row in losses:
  key=row['method']+' / '+row['distribution'];grouped[key]=grouped.get(key,0)+1
 out['accepted_reference_resolved_loss_count']=len(losses);out['resolved_losses_by_method_distribution']=grouped;out['accepted_reference_resolved_losses']=losses[:3]
 out['loss_examples_truncated']=len(losses)>3
 for item in pairs.values():item.pop('examples',None)
 (TOP/'evidence/l7-suite-summary.json').write_text(json.dumps(out,indent=1)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k in ['scope','worker_elapsed_seconds_sum','maximum_own_L2_Q_entry_discrepancy','maximum_training_replay_all_raw_cases']},indent=1));print('resolved losses',len(losses))
if __name__=='__main__':main()
