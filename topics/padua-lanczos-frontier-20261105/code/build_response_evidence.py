import sys,json,pathlib,hashlib,importlib.util,itertools,argparse
from fractions import Fraction as F
T=pathlib.Path(__file__).resolve().parents[1]; C=T/'code'
ap=argparse.ArgumentParser(description='Package pinned pre-existing evidence only; no new fits or scans')
ap.add_argument('--output-dir',required=True);args=ap.parse_args();E=pathlib.Path(args.output_dir);E.mkdir(parents=True,exist_ok=False)
def ident(p):
 p=pathlib.Path(p);return dict(path=str(p),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest())
def pinned(p,h):
 assert ident(p)['sha256']==h,(str(p),ident(p));return pathlib.Path(p)
pinned(C/'g1_fit.py','18eea30277a3d2d58aab8ece2f15b33e83a1178d5b03e96180229b41a247aeac')
pinned(C/'l7_suite_summary.py','e6fe858208a36206a7bcf9a4e81412fd3b8920cd45dfde5835a26a3c8c363a01')
spec=importlib.util.spec_from_file_location('frozen',C/'g1_fit.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
manifest=pinned('/tmp/padua-lanczos-frontier-g1-check05/full-fit-input/manifest.json','8bd04bb6502762a61d53d5633f6737786315d743b6e408e689d647ac7998c144')
report=pinned('/tmp/padua-lanczos-frontier-g1-fit/actual/report.json','5211917f379060bfa5f477354bbe0cf29066dba76d85d428d43de34a6190176b')
data,man=m.load_manifest(manifest);scale=10**15
for g in m.GRIDS:
 rows=[]
 for s in range(2,21):
  for r in m.RULES:
   vals=[]
   for v in (data[g,r][s-2][0],data[g,r][s-2][3]):
    z=m.logq(v,144)/2;lo=z.a*scale;hi=z.b*scale
    vals.extend([lo.numerator//lo.denominator,-((-hi.numerator)//hi.denominator)])
   rows.append([s,r,*vals])
 obj=dict(schema='g1-compact-log-endpoints-v1',grid=g,scale=scale,columns=['degree','rule','logL_lower','logL_upper','logU_lower','logU_upper'],meaning='integer bounds / scale enclose log(L_squared)/2 and log(U_squared)/2; floor lower and ceil upper of exact 144-bit outward logarithms',source_manifest=ident(manifest),source_report=ident(report),frozen_log_code=ident(C/'g1_fit.py'),source_cases=[c for c in man['cases'] if c['grid']==g],rows=rows)
 p=E/f'g1-compact-{g}.json';p.write_text(json.dumps(obj,separators=(',',':'))+'\n');assert p.stat().st_size<16384;print(ident(p))
summary=json.loads((T/'evidence/l7-suite-summary.json').read_text());aggregate=pinned(summary['full_aggregate']['path'],summary['full_aggregate']['sha256']);a=json.loads(aggregate.read_text())
obj=dict(schema='l7-full-loss-list-v1',source_aggregate=ident(aggregate),aggregator=ident(C/'l7_suite_summary.py'),aggregator_command='python topics/padua-lanczos-frontier-20261105/code/l7_suite_summary.py',loss_count=20,losses=a['accepted_reference_resolved_losses']);assert len(obj['losses'])==20
p=E/'l7-full-loss-list.json';p.write_text(json.dumps(obj,separators=(',',':'))+'\n');assert p.stat().st_size<16384;print(ident(p))
# Cross-group computation uses pinned original worker JSON, no new fit.
raw=[]
for pin in summary['worker_json_manifest']:raw.append(json.loads(pinned(pin['path'],pin['sha256']).read_text()))
by={(x['domain'],x['seed']):x for x in raw};full=['upstream_xy','upstream_yx','dev_full','mirror_full','alt_full','adapt_full'];window=['dev_window','mirror_window','alt_window','adapt_window'];pairs=[];count=0
for d in ['disk','lshape','triangle','sector']:
 for c1,c2 in zip(by[d,2026110501]['cases'],by[d,2026110502]['cases']):
  if not(c1['reference']['trusted'] and c2['reference']['trusted']):continue
  for tn in c1['targets']:
   for dist in ['uniform','boundary']:
    for x,y in itertools.product(full,window):
     count+=1;rat=[c['targets'][tn]['methods'][x][dist]['rel_l2']/c['targets'][tn]['methods'][y][dist]['rel_l2'] for c in (c1,c2)]
     if min(rat)>2 or max(rat)<.5:pairs.append(dict(domain=d,degree=c1['n'],target=tn,distribution=dist,full=x,window=y,winner=y if min(rat)>2 else x,full_over_window=rat))
obj=dict(schema='l7-cross-group-v1',choice='Post-registration grouping disclosure; frozen >2 both-seeds rule unchanged',source_workers=summary['worker_json_manifest'],cross_group_method_pairs=24,matched_cells_per_pair=64,comparisons=count,qualifying_directions=len(pairs),directions=pairs)
p=E/'l7-cross-group.json';p.write_text(json.dumps(obj,separators=(',',':'))+'\n');print(ident(p));print('cross',len(pairs),pairs)
