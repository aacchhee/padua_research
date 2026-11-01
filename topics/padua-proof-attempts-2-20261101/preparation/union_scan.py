"""Mechanical fresh-ID union scan; no Git mutation or assignment."""
import hashlib, json, re, subprocess
from pathlib import Path

P=Path(__file__).resolve().parent
R=P.parents[2]
REFS={'main':'67bd07c0867d8d49eb104942237d7f51a7d9f77d','PR12':'f4c5c9e783d2a57253142877cf6845635aaac50f'}
def git(*a):return subprocess.check_output(['git',*a],cwd=R)
prs=json.loads((P/'pr-snapshot.json').read_text())
assert {p['number'] for p in prs if p['state']=='open'}=={12}
assert not [p for p in prs if p['state']=='closed' and p['merged_at'] is None]
maxima={ns:0 for ns in ['PD-T','PD-N','IDEA-','LIT-']}
heads={}
for label,ref in REFS.items():
    ledgers=[p for p in git('ls-tree','-r','--name-only',ref).decode().splitlines() if p.endswith('/ALLOCATIONS.md')]
    rows=[]
    for path in ['PROOF_STATUS.md','state/IDEAS.md','literature/INDEX.md','ID_CROSSWALK.md']+ledgers:
        data=git('show',ref+':'+path);s=data.decode()
        rows.append({'path':path,'blob':git('rev-parse',ref+':'+path).decode().strip(),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
        # Complete ledger ranges include unused permanent headroom. Standalone
        # 'next unreserved' prose is a boundary, not a reservation.
        if path in ledgers:
            for ns,lo,hi in re.findall(r'(PD-T|PD-N|IDEA-|LIT-)(\d{3})[–-](?:(?:PD-T|PD-N|IDEA-|LIT-))?(\d{3})(?!\d)',s):
                maxima[ns]=max(maxima[ns],int(lo),int(hi))
        # Canonical first-column definitions and crosswalk's final-ID column.
        for line in s.splitlines():
            if not line.startswith('|'):continue
            cells=line.split('|')[1:3]
            for cell in cells:
                m=re.match(r'\s*\**(PD-T|PD-N|IDEA-|LIT-)(\d{3})(?!\d)',cell)
                if m:maxima[m[1]]=max(maxima[m[1]],int(m[2]))
    heads[label]={'sha':ref,'all_ledgers':ledgers,'files':rows}
assert maxima=={'PD-T':155,'PD-N':71,'IDEA-':285,'LIT-':459},maxima
result={'purpose':'fresh final-ID reservation union; no assignment','heads':heads,'PR_snapshot':'pr-snapshot.json','closed_unmerged':[],'max_used_or_reserved':maxima,'boundary_prose_is_not_allocation':True,'reservation':{'PD-T':[156,205,50,42],'PD-N':[72,77,6,2],'IDEA':[286,315,30],'LIT':'no range; reuse312/379/388'},'passed':True}
(P/'reservation-scan.json').write_text(json.dumps(result,indent=1)+'\n')
print(json.dumps({'passed':True,'maxima':maxima,'ledgers':{k:v['all_ledgers'] for k,v in heads.items()}}))
