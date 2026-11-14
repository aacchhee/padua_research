"""Data-only census of authenticated complete inputs and regenerated records."""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import worker

def sha(b): return hashlib.sha256(b).hexdigest()
def main():
    p=argparse.ArgumentParser(); p.add_argument('--freeze',required=True); p.add_argument('--full',required=True); p.add_argument('--output',required=True); a=p.parse_args()
    freeze=json.loads(Path(a.freeze).read_bytes()); base=Path(a.full)
    data={}; identities={}
    for n,mode,name,b,d in worker.archive_inputs('local-output/argmax-bridge-20261105/actual-return-20261107/return.tar.gz'):
        data[n,mode]=d; identities[n,mode]=sha(b)
    inv=Path(freeze['inventory']); raw=inv.read_bytes()
    if sha(raw)!=freeze['inventory_sha256']: raise ValueError('inventory identity')
    for row in json.loads(raw)['files']:
        path=Path(freeze['additional_dir'])/row['name']; b=path.read_bytes()
        if sha(b)!=row['sha256'] or len(b)!=row['bytes']: raise ValueError('input identity')
        n,mode=row['name'][1:-5].split('-'); key=int(n),mode
        if key in data: raise ValueError('duplicate input')
        data[key]=json.loads(b); identities[key]=sha(b)
    expected={(n,mode) for n in range(41,512) for mode in ['produce','verify']}
    if set(data)!=expected: raise ValueError('input scope')
    rows={}; control_counts=[]; runtime=[]
    for j in range(4):
        directory=base/('worker-'+str(j))
        for row in json.loads((directory/'inputs.json').read_bytes())['inputs']:
            if identities[row['n'],row['pass']]!=row['sha256']: raise ValueError('executed input differs')
        control_counts.append(json.loads((directory/'summary.json').read_bytes()))
        runtime.append(json.loads((directory/'runtime-probes.json').read_bytes()))
        for line in (directory/'observations.jsonl').read_text().splitlines():
            r=json.loads(line); key=r['n'],r['pass']
            if key in rows or not r['accepted']: raise ValueError('duplicate/rejected record')
            rows[key]=r
    if set(rows)!=expected: raise ValueError('result scope')
    fields=['format','status','n','tree','pi_bracket','S_upper_columns','S_upper_rows','origin_lower_hex','lambda_upper_columns','lambda_upper_rows','norm','floor','corner','analytic_far']
    for n in range(41,512):
        if any(data[n,'produce'][k]!=data[n,'verify'][k] for k in fields): raise ValueError('primary/fresh scientific mismatch '+str(n))
        if {k:v for k,v in rows[n,'produce'].items() if k not in ['pass','CPU_seconds']}!={k:v for k,v in rows[n,'verify'].items() if k not in ['pass','CPU_seconds']}: raise ValueError('independent pair mismatch '+str(n))
    census=Counter()
    for n in range(320,511):
        t=data[n,'produce']['tree']['preorder']; census[len(t),sum(c not in 'ab' for c in t),t.count('f'),data[n,'produce']['norm']['method']]+=1
    minima={}
    for field in ['near_min','far_min','corner_gap','floor_min','M']:
        values=[(Fraction(r[field]),r['n'],r['pass']) for r in rows.values() if r[field] not in [None,'None']]
        m=min(v[0] for v in values); minima[field]={'exact':str(m),'degrees':sorted({n for v,n,mode in values if v==m})}
    result={'certificates':len(rows),'degrees':471,'new_range_tree_node_leaf_census':[{'nodes':nodes,'leaves':leaves,'analytic_far_leaves':far,'norm_method':method,'degrees':count} for (nodes,leaves,far,method),count in sorted(census.items())],
            'primary_fresh_scientific_pairs_equal':471,'independent_primary_fresh_pairs_equal':471,'minima':minima,
            'S_checks':sum(r['S_keys'] for r in rows.values()),'distinct_S_keys':sum(r['S_keys'] for (n,m),r in rows.items() if m=='produce'),
            'actual_lambda_checks':sum(r['lambda_keys'] for r in rows.values()),'distinct_actual_lambda_keys':sum(r['lambda_keys'] for (n,m),r in rows.items() if m=='produce'),
            'native_S_uppers_contained':sum(r['native_S_upper_contained'] for r in rows.values()),'native_S_uppers_total':sum(r['native_S_upper_total'] for r in rows.values()),
            'native_lowers_contained':sum(r['native_lower_contained'] for r in rows.values()),'M_max':str(max(Fraction(r['M']) for r in rows.values())),
            'worker_summaries':control_counts,'runtime_probes':runtime,'outer_observation':json.loads((base/'outer-observation.json').read_bytes()),
            'source_freeze_sha256':sha(Path(a.freeze).read_bytes()),'all_native_endpoints_validated':False}
    with Path(a.output).open('x') as f: json.dump(result,f,indent=2); f.write('\n')
    print(json.dumps(result))
if __name__=='__main__': main()
