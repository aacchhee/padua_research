#!/usr/bin/env python3
"""Pinned read-only reservation/registry union scan before mechanical assignment."""
import argparse,hashlib,json,re,subprocess
from pathlib import Path
R=Path(__file__).resolve().parents[1]
def git(*a):return subprocess.check_output(['git',*a],text=True)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('snapshot',type=Path);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
 prs=json.loads(a.snapshot.read_text());assert not any(x['state']=='closed' and not x['merged'] for x in prs),'recover closed-unmerged ledger first'
 heads={'main':git('rev-parse','origin/main').strip()}
 for x in prs:
  if x['state']=='open':
   assert git('rev-parse','origin/'+x['head']).strip()==x['head_sha'],x
   heads['PR'+str(x['number'])]=x['head_sha']
 rows=[];maxima={ns:0 for ns in ['PD-T','PD-N','IDEA','LIT']};owner_rows={}
 for label,head in heads.items():
  paths=git('ls-tree','-r','--name-only',head).splitlines()
  for p in paths:
   if not(p.endswith('ALLOCATIONS.md') or p in ('PROOF_STATUS.md','state/IDEAS.md','literature/INDEX.md','ID_CROSSWALK.md')):continue
   raw=git('show',head+':'+p);local={}
   for ns,pat in {'PD-T':r'PD-T(\d{3})(?!\d)','PD-N':r'PD-N(\d{3})(?!\d)','IDEA':r'IDEA-?(\d{3})(?!\d)','LIT':r'LIT-?(\d{3})(?!\d)'}.items():
    values=[int(v) for v in re.findall(pat,raw)]
    local[ns]=max(values or [0])
   if p.endswith('ALLOCATIONS.md'):
    for line in raw.splitlines():
     c=[x.strip() for x in line.split('|')]
     if len(c)>2 and c[1] in maxima:
      nums=[int(n) for n in re.findall(r'(?<!\d)\d{3}(?!\d)',c[2])]
      if nums:local[c[1]]=max(local[c[1]],max(nums))
    if p not in ('topics/padua-batch-20261031/ALLOCATIONS.md',):owner_rows[label+':'+p]=[x for x in raw.splitlines() if any(k in x for k in ('| PD-T |','| PD-N |','| IDEA |','| LIT |'))]
   for ns,v in local.items():maxima[ns]=max(maxima[ns],v)
   rows.append([label,p,hashlib.sha256(raw.encode()).hexdigest(),local])
 out={'date':'2026-11-05','heads':heads,'prs':prs,'closed_unmerged':[],'method':'Complete ledger and four-registry reads at pinned heads; three-digit local IDs and namespace table ranges; foreign four-digit BTTB LIT aliases excluded. Historical next-free mentions are conservative maxima, not reservations. Own unchanged reservation is assigned, not re-reserved.','files':rows,'qualified_maxima':maxima,'topic_reservation':{'PD-T':[294,323],'PD-N':[104,115],'IDEA':[384,413],'LIT':[574,581]}}
 a.output.write_text(json.dumps(out,separators=(',',':'))+'\n')
 print(json.dumps({'heads':heads,'files':len(rows),'qualified_maxima':maxima,'bytes':a.output.stat().st_size,'owner_rows':owner_rows},indent=1))
if __name__=='__main__':main()
