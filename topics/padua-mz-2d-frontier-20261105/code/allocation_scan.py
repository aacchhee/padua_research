#!/usr/bin/env python3
"""Record pinned registry/ledger identities; conservative mention maxima."""
import hashlib,json,re,subprocess
from pathlib import Path
refs=['origin/main','origin/codex/padua-argmax-effective-20261103','origin/codex/padua-lebesgue-followups-20261103','origin/claude/padua-literature-20261103','origin/codex/nn-mop-iep-20261103','origin/codex/padua-lanczos-frontier-20261105']
namespaces={'PD-T':r'PD-T(\d{3})\b','PD-N':r'PD-N(\d{3})\b','IDEA':r'IDEA-?(\d{3})\b','LIT':r'LIT-?(\d{3})\b'}
rows=[]
for ref in refs:
    head=subprocess.check_output(['git','rev-parse',ref],text=True).strip()
    paths=subprocess.check_output(['git','ls-tree','-r','--name-only',head],text=True).splitlines()
    paths=[p for p in paths if p.endswith('ALLOCATIONS.md') or p in ['PROOF_STATUS.md','state/IDEAS.md','literature/INDEX.md','ID_CROSSWALK.md']]
    for p in paths:
        data=subprocess.check_output(['git','show',head+':'+p]);s=data.decode()
        maxima={ns:max([int(x) for x in re.findall(pat,s)] or [0]) for ns,pat in namespaces.items()}
        # A bare range in a namespace table is still a reservation.
        for line in s.splitlines():
            cells=[v.strip() for v in line.split('|')]
            if len(cells)>2 and cells[1] in namespaces and 'ALLOCATIONS' in p:
                nums=[int(x) for x in re.findall(r'(?<!\d)\d{3}(?!\d)',cells[2])]
                if nums:maxima[cells[1]]=max(maxima[cells[1]],max(nums))
        rows.append({'ref':ref,'head':head,'path':p,'sha256':hashlib.sha256(data).hexdigest(),'maxima':maxima})
report={'date':'2026-11-05','method':'Read complete files at pinned Git heads; qualified three-digit mentions plus bare namespace reservation ranges. Foreign four-digit BTTB LIT aliases excluded; historical next-free prose may conservatively overestimate and is manually checked.','prs':{'open':[19,20,21,22],'closed_unmerged':[],'all_returned_closed_are_merged':True},'files':rows,'union_maxima':{ns:max(r['maxima'][ns] for r in rows) for ns in namespaces}}
out=Path(__file__).resolve().parents[1]/'allocation-scan.json';out.write_text(json.dumps(report,separators=(',',':'))+'\n')
print(json.dumps({'files':len(rows),'union_maxima':report['union_maxima'],'bytes':out.stat().st_size}))
