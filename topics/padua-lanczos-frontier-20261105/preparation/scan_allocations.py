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
    'main': 'b4d292eea5eed373002506d5e16a3761bd7ae10e',
    'PR27': '95366c19562e88c11138f88aab0a6617d6b15305',
    'PR24': '29a78ec132d94d253816fd103d6ffb574de25e3b',
    'own_integration': 'a3f03be58be6819d833523ef26ccff69f5bc184a',
}
REGISTRIES = ['PROOF_STATUS.md', 'state/IDEAS.md', 'literature/INDEX.md', 'ID_CROSSWALK.md']
OWN = 'topics/padua-lanczos-frontier-20261105/ALLOCATIONS.md'
PREFIXES = {'PD-T': r'(?:PD-)?T', 'PD-N': r'(?:PD-)?N', 'IDEA': 'IDEA-?', 'LIT': 'LIT-?'}
RESERVED = {'PD-T': [324,363], 'PD-N': [116,131], 'IDEA': [414,453], 'LIT': [582,593]}
PUBLICATION = '40b3eb645c1dc066a8e646b79c67eaa00f4fa181'


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
    population_path = Path(__file__).with_name('live-prs.json')
    population_bytes = population_path.read_bytes()
    population = json.loads(population_bytes)['prs']
    assert len(population) == 26
    assert sorted(p['number'] for p in population if p['state'] == 'open') == [24, 27]
    assert all(p['merged_at'] for p in population if p['state'] == 'closed')
    for p in population:
        if p['state'] == 'open':
            assert HEADS['PR'+str(p['number'])] == p['head']
    files, blobs, head_indices, raw = [], {}, {}, []
    union = dict.fromkeys(PREFIXES,0)
    for label, head in HEADS.items():
        paths = git('ls-tree','-r','--name-only',head).decode().splitlines()
        paths = [p for p in paths if p.endswith('/ALLOCATIONS.md') or p in REGISTRIES]
        assert set(REGISTRIES) <= set(paths)
        head_indices[label] = []
        for path in paths:
            data = git('show', head+':'+path)
            snapshot = Path('/tmp/padua-lanczos-frontier-preparation/raw') / head / path
            snapshot.parent.mkdir(parents=True, exist_ok=True)
            snapshot.write_bytes(data)
            blob = git('rev-parse', head+':'+path).decode().strip()
            mx = maxima(data.decode(),path.endswith('/ALLOCATIONS.md'))
            blobs[blob] = {'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),
                           'lines':len(data.splitlines()),'maxima':mx}
            row = [path,blob]
            if row not in files: files.append(row)
            head_indices[label].append(files.index(row))
            raw.append({'head':head,'path':path,'blob':blob,**blobs[blob]})
            for ns in union: union[ns] = max(union[ns],mx[ns])
    assert union == {'PD-T':431,'PD-N':161,'IDEA':529,'LIT':613}, union
    # Verify original publication and unchanged reservation at integration.
    for head in [PUBLICATION, HEADS['own_integration']]:
        text = git('show',head+':'+OWN).decode()
        for ns, (lo,hi) in RESERVED.items():
            prefix = ns+'-' if ns in ['IDEA','LIT'] else ns
            assert f'{prefix}{lo:03}–{prefix}{hi:03}' in text
    for label,head in HEADS.items():
        # No reserved own final ID is an existing registry row/token. Own
        # reservation acknowledgements occur only in ledgers/crosswalk prose.
        for path in REGISTRIES[:3]:
            text = git('show',head+':'+path).decode()
            for ns,(lo,hi) in RESERVED.items():
                prefix=PREFIXES[ns]
                for n in range(lo,hi+1):
                    assert not re.search(rf'(?<![A-Za-z0-9]){prefix}{n:03}(?!\d)',text),(label,path,ns,n)
    # The new foreign PR27 reservation is strictly above ours in all namespaces.
    bridge = {'PD-T':[392,431], 'PD-N':[146,161], 'IDEA':[490,529], 'LIT':[598,613]}
    bridge_text = git('show', HEADS['PR27']+':topics/padua-argmax-bridge-20261105/ALLOCATIONS.md').decode()
    for ns, (lo, hi) in bridge.items():
        prefix = ns+'-' if ns in ['IDEA','LIT'] else ns
        assert f'{prefix}{lo:03}–{prefix}{hi:03}' in bridge_text
        assert RESERVED[ns][1] < lo
    temp=Path('/tmp/padua-lanczos-frontier-preparation');temp.mkdir(exist_ok=True)
    bulk=json.dumps(raw,sort_keys=True,separators=(',',':')).encode()+b'\n'
    (temp/'full-inventory.json').write_bytes(bulk)
    report={'format':'padua-allocation-union-v1','date':'2026-11-05',
      'rules_sha':HEADS['own_integration'],'worker':'Codex gpt-6.1-sol medium',
      'scope':'Mechanical full-file inventory; no scientific claim, new reservation, assignment or Git mutation.',
      'heads':HEADS,'population_file':{'path':'live-prs.json','sha256':hashlib.sha256(population_bytes).hexdigest(),'bytes':len(population_bytes)},'own_remote_pr24':HEADS['PR24'],
      'population':{'source':'live-prs.json supplied from orchestrator all-state GET per_page=100; no independent network query','open':[24,27],'closed_merged':24,'closed_unmerged':[]},
      'method':'Full bytes of every ledger and four registries per head; complete unique ledger prose reviewed separately. Qualified three-digit tokens, abbreviated namespace prefixes/endpoints and namespace table bare ranges included. Four-digit foreign BTTB aliases excluded; historical next-free prose not a reservation.',
      'copies_read':len(raw),'ledger_copies':sum(r['path'].endswith('/ALLOCATIONS.md') for r in raw),
      'distinct_ledger_blobs':len({r['blob'] for r in raw if r['path'].endswith('/ALLOCATIONS.md')}),
      'distinct_blobs':len(blobs),'files_columns':['path','git_blob'],'files':files,'head_file_indices':head_indices,'blobs':blobs,
      'union_maxima':union,'own_reservation':RESERVED,'first_publication':PUBLICATION,'foreign_pr27_reservation':bridge,
      'result':'PASS','conflicts':[],'accepted_id_renumbering':False,'no_assignment_performed':True,
      'bulk_inventory':{'path':str(temp/'full-inventory.json'),'bytes':len(bulk),'sha256':hashlib.sha256(bulk).hexdigest(),'retention':'Temporary convenience; regenerate from pinned Git file identities.'}}
    encoded=json.dumps(report,separators=(',',':')).encode()+b'\n'
    assert len(encoded)<16384,len(encoded)
    Path(__file__).with_name('allocation-scan.json').write_bytes(encoded)
    print(json.dumps({k:report[k] for k in ['result','copies_read','ledger_copies','distinct_ledger_blobs','distinct_blobs','union_maxima']}))
    print('receipt_bytes',len(encoded))

if __name__=='__main__': main()
