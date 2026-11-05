#!/usr/bin/env python3
"""Pinned mechanical allocation inventory; writes only its compact receipt.

Run from the repository root. Every ledger and four registries is read in full.
Manual ledger-prose review is documented in reservation-check.md; this parser
is an inventory, not an automatic replacement for that review.
"""
import hashlib
import json
import re
import subprocess
from pathlib import Path

HEADS = {
    'main': '330fab835f43e5ba5b24e320c2d7e9647e6cbd60',
    'PR21': '3ed6c94246f21353350f82712b6628b39db6f65a',
    'PR24': '3a179f68ecbed20dc7e15862da842ed6116aa375',
    'own_integration': '5821c3f130ec0b1e33ad1d01620b67620e1f0be1',
}
REGISTRIES = ['PROOF_STATUS.md', 'state/IDEAS.md', 'literature/INDEX.md', 'ID_CROSSWALK.md']
OWN = 'topics/padua-argmax-effective-2-20261105/ALLOCATIONS.md'
PREFIXES = {'PD-T': r'(?:PD-)?T', 'PD-N': r'(?:PD-)?N', 'IDEA': 'IDEA-?', 'LIT': 'LIT-?'}
RESERVED = {'PD-T': [364,375], 'PD-N': [132,137], 'IDEA': [454,465], 'LIT': [594,597]}
PUBLICATION = 'ce17564ea1c185fea0be109b8ebb38efe25bceec'


def git(*args):
    return subprocess.check_output(['git', *args])


def maxima(text, ledger):
    result = {}
    for ns, prefix in PREFIXES.items():
        if not ledger and ns in ['PD-T','PD-N']: prefix = ns
        # Boundaries exclude foreign four-digit BTTB LIT aliases. Include an
        # omitted-prefix endpoint: T364–375, PD-T364–375, IDEA454–465, etc.
        pat = rf'(?<![A-Za-z0-9]){prefix}(\d{{3}})(?!\d)(?:[–−-](?:{prefix})?(\d{{3}})(?!\d))?'
        nums = [int(v) for pair in re.findall(pat, text) for v in pair if v]
        result[ns] = max(nums, default=0)
    if ledger:
        for line in text.splitlines():
            cells = [c.strip().strip('*') for c in line.split('|')]
            if len(cells)>2 and cells[1] in PREFIXES:
                nums = [int(x) for x in re.findall(r'(?<!\d)\d{3}(?!\d)', cells[2])]
                result[cells[1]] = max([result[cells[1]], *nums])
    return result


def main():
    files, blobs, head_indices, raw = [], {}, {}, []
    union = dict.fromkeys(PREFIXES,0)
    for label, head in HEADS.items():
        paths = git('ls-tree','-r','--name-only',head).decode().splitlines()
        paths = [p for p in paths if p.endswith('/ALLOCATIONS.md') or p in REGISTRIES]
        assert set(REGISTRIES) <= set(paths)
        head_indices[label] = []
        for path in paths:
            data = git('show', head+':'+path)
            blob = git('rev-parse', head+':'+path).decode().strip()
            mx = maxima(data.decode(),path.endswith('/ALLOCATIONS.md'))
            blobs[blob] = {'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),
                           'lines':len(data.splitlines()),'maxima':mx}
            row = [path,blob]
            if row not in files: files.append(row)
            head_indices[label].append(files.index(row))
            raw.append({'head':head,'path':path,'blob':blob,**blobs[blob]})
            for ns in union: union[ns] = max(union[ns],mx[ns])
    assert union == {'PD-T':391,'PD-N':145,'IDEA':489,'LIT':597}, union
    # Verify original publication and unchanged reservation at integration.
    for head in [PUBLICATION, HEADS['own_integration']]:
        text = git('show',head+':'+OWN).decode()
        for ns, (lo,hi) in RESERVED.items():
            prefix = ns+'-' if ns in ['IDEA','LIT'] else ns
            assert f'{prefix}{lo:03}–{prefix}{hi:03}' in text
    for label,head in HEADS.items():
        # No proposed own final ID is an existing registry row/token. Own
        # reservation acknowledgements occur only in ledgers/crosswalk prose.
        for path in REGISTRIES[:3]:
            text = git('show',head+':'+path).decode()
            for ns,(lo,hi) in RESERVED.items():
                prefix=PREFIXES[ns]
                for n in range(lo,hi+1):
                    assert not re.search(rf'(?<![A-Za-z0-9]){prefix}{n:03}(?!\d)',text),(label,path,ns,n)
    temp=Path('/tmp/argmax-prep-allocation');temp.mkdir(exist_ok=True)
    bulk=json.dumps(raw,sort_keys=True,separators=(',',':')).encode()+b'\n'
    (temp/'full-inventory.json').write_bytes(bulk)
    report={'format':'padua-allocation-union-v1','date':'2026-11-05',
      'rules_sha':HEADS['own_integration'],'worker':'Codex gpt-6.1-sol medium',
      'scope':'Mechanical full-file inventory; no scientific claim, new reservation, assignment or Git mutation.',
      'heads':HEADS,'own_remote_pr25':'22e8540cf90278dad2eba3eb51f129ca10a9dd9e',
      'population':{'source':'pr-population.json supplied from orchestrator live all-state connector search; no independent network query','open':[21,24,25],'closed_merged':22,'closed_unmerged':[]},
      'method':'Full bytes of every ledger and four registries per head; complete unique ledger prose reviewed separately. Qualified three-digit tokens, abbreviated namespace prefixes/endpoints and namespace table bare ranges included. Four-digit foreign BTTB aliases excluded; historical next-free prose not a reservation.',
      'copies_read':len(raw),'ledger_copies':sum(r['path'].endswith('/ALLOCATIONS.md') for r in raw),
      'distinct_ledger_blobs':len({r['blob'] for r in raw if r['path'].endswith('/ALLOCATIONS.md')}),
      'distinct_blobs':len(blobs),'files_columns':['path','git_blob'],'files':files,'head_file_indices':head_indices,'blobs':blobs,
      'union_maxima':union,'own_reservation':RESERVED,'first_publication':PUBLICATION,
      'proposed_only':{'PD-T':{'T01':364,'T03':365,'T04':366,'T05':367,'T06':368,'T07':369,'T08':370},'PD-N':{'N01':132},'IDEA':{'IDEA01-08':[454,461]},'T02':'unregistered','LIT':'none'},
      'own_unused_permanent_after_proposal':{'PD-T':[371,375],'PD-N':[133,137],'IDEA':[462,465],'LIT':[594,597]},
      'result':'PASS','conflicts':[],'accepted_id_renumbering':False,'no_assignment_performed':True,
      'bulk_inventory':{'path':str(temp/'full-inventory.json'),'bytes':len(bulk),'sha256':hashlib.sha256(bulk).hexdigest(),'retention':'Temporary convenience; regenerate from pinned Git file identities.'}}
    encoded=json.dumps(report,separators=(',',':')).encode()+b'\n'
    assert len(encoded)<16384,len(encoded)
    Path(__file__).with_name('reservation-scan.json').write_bytes(encoded)
    print(json.dumps({k:report[k] for k in ['result','copies_read','ledger_copies','distinct_ledger_blobs','distinct_blobs','union_maxima']}))
    print('receipt_bytes',len(encoded))

if __name__=='__main__': main()
