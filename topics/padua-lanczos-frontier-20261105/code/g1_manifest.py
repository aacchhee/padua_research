#!/usr/bin/env python3
"""Compact exact-scan inventory; refuses fits/gate judgments and reports gaps."""
import argparse,hashlib,json,pathlib,sys

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ident(p):return {'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)}
def main():
 p=argparse.ArgumentParser();p.add_argument('--receipt-dir',required=True);p.add_argument('--prefix',default='overlap');p.add_argument('--output',required=True);a=p.parse_args();base=pathlib.Path(a.receipt_dir);cases=[];missing=[];completed=0
 for s in ['triangle','rotated']:
  for rule in ['bj','mirror','alt','pivot']:
   f=base/f'{a.prefix}-{s}-{rule}.json'
   if not f.exists():missing.append({'set':s,'rule':rule});continue
   r=json.loads(f.read_text());case={'set':s,'rule':rule,'receipt':ident(f),'result':r['result'],'max_degree':r['max_degree']}
   if 'endpoint_file' in r:
    ep=pathlib.Path(r['endpoint_file']['path']);assert ident(ep)==r['endpoint_file'];rows=json.loads(ep.read_text())['runs'];completed+=len(rows)
    case.update({'endpoint_file':r['endpoint_file'],'basis_recurrence':r['basis_recurrence'],'completed_degrees':r['completed_degrees'],'all_2_through_12_overlap_pass':r['all_2_through_12_overlap_pass'],'pivot_ties':r['pivot_ties'],'independent_degree_controls':r['independent_degree_controls'],'elapsed_seconds':r['runtime']['elapsed_seconds'],'final_displays':{x:rows[-1][x]['float'] for x in ['Knode_squared','KHS_squared','Urow_squared','upper_squared']}})
   else:case['partial_state']=r.get('state')
   cases.append(case)
 result={'label':'EXACT_G1_PRODUCER_INVENTORY_NO_FIT_OR_GATE_VERDICT','phase':a.prefix,'full_required_scope':{'sets':['triangle','rotated'],'rules':['bj','mirror','alt','pivot'],'degrees':[2,20],'source_class':'all','expected_rows':152},'phase_completed_rows':completed,'missing_cases':missing,'cases':cases,'manifest_code_sha256':sha(pathlib.Path(__file__)),'command':[sys.executable,'-B',str(pathlib.Path(__file__).resolve()),*sys.argv[1:]],'limits':['This receipt inventories actual completed producer work; pending degrees/cases are not completed.','No descriptive fitting until the full152-row scope is complete.','Exact finite endpoints give no all-degree conclusion; independent port/checking remains separate.','Bulk exact endpoints/recurrence arrays remain external temporary evidence with archive/delivery pending.']}
 pathlib.Path(a.output).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'completed_rows':completed,'cases':len(cases),'missing':missing}))
if __name__=='__main__':main()
