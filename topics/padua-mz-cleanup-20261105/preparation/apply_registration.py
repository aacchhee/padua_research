#!/usr/bin/env python3
"""Apply the audited cleanup registration once, failing on changed old blocks."""
import hashlib
import json
from pathlib import Path
import re


def main():
    topic=Path(__file__).resolve().parents[1]
    root=topic.parents[1]
    data=json.loads((topic/'preparation/final-id-map.json').read_text())
    aliases=data['aliases']
    def final(text):
        text=text.replace('PD-T?mz-cleanup-codex-02/03',
                          'PD-T?mz-cleanup-codex-02/PD-T?mz-cleanup-codex-03')
        for old,new in aliases.items():text=text.replace(old,new)
        return text
    proposal=(topic/'proposed-record-changes.md').read_text()
    pairs=re.findall(r'Old:\n\n```markdown\n(.*?)```\s*New:\n\n```markdown\n(.*?)```',proposal,re.S)
    paths=['PAPER_MAP.md','state/CURRENT.md','tracks/mz-constants/README.md',
           'state/IDEAS.md','state/IDEAS.md','PROOF_STATUS.md',
           'PROOF_STATUS.md','PROOF_STATUS.md']
    if len(pairs)!=len(paths):raise ValueError('unexpected literal proposal structure')
    original={};changed={}
    def read(name):
        if name not in original:
            original[name]=(root/name).read_text();changed[name]=original[name]
        return changed[name]
    for name,(old,new) in zip(paths,pairs):
        text=read(name)
        if text.count(old.rstrip())!=1:raise ValueError('old block not unique: '+name)
        new=final(new.rstrip())
        if name=='PAPER_MAP.md':
            new=new.replace(' (replace provisional aliases by final IDs at preparation)','')
            new=new.replace('response/preparation pending','response resolved; preparation checks recorded separately')
        if name=='state/CURRENT.md':
            summary=('PD-T376 certifies finite negative trial directions at m=1101,1240,1600;\n'
                     'PD-T377 supplies the odd-m weight limit and PD-T378 the all-integer\n'
                     'spectral divergence above half-exactness. PD-T379 gives exact continuous\n'
                     'carrier norms and explicit normalized one-sided bounds. PD-T380 keeps\n'
                     'the 23 scans/fits MEASURED; PD-T381 retains the original sharp-growth\n'
                     'target OPEN, with PD-T379 as separate support, not a proved conjunct.\n\n')
            new=new.replace('Claude [cleanup audit-01]',summary+'Claude [cleanup audit-01]')
            new=new.replace('accepts the new mathematics at its stated scope; response and preparation\nare separate.',
                'accepts the new mathematics at its stated scope; the response resolves\nits record findings. Registration/verification details live in the\n[preparation record](../topics/padua-mz-cleanup-20261105/preparation/record.md),\nrather than a continuing initialization task.')
        changed[name]=text.replace(old.rstrip(),new)
    blocks=re.findall(r'```markdown\n(.*?)```',proposal,re.S)
    proof=next(b for b in blocks if b.startswith('## Signed Padua MZ cleanup — 2026-11-05'))
    ideas=next(b for b in blocks if b.startswith('## Signed Padua MZ cleanup — retained candidate records'))
    for name,addition in [('PROOF_STATUS.md',proof),('state/IDEAS.md',ideas)]:
        text=read(name)
        if '| PD-T376 |' in text or '| IDEA-466;' in text:raise ValueError('already registered')
        addition=final(addition)
        if name=='state/IDEAS.md':
            addition=addition.replace('retained bounded implementation variant;', 'active (PROVED outcome), bounded implementation variant;')
            addition=addition.replace('retained parity variant;', 'active (PROVED outcome), parity variant;')
            addition=addition.replace('retained quantitative variant;', 'active (PROVED outcome), quantitative variant;')
        changed[name]=text.rstrip()+'\n\n'+addition.rstrip()+'\n'
    name='ID_CROSSWALK.md';text=read(name)
    table='\n\n## Signed Padua MZ cleanup — final mapping and preserved target\n\n'
    table+='Reservation first published ee490356ce51d5e2f4a84f2c45e6ccb98a19bd90, [PR26](https://github.com/aacchhee/padua_research/pull/26). '
    table+='[Live union check](topics/padua-mz-cleanup-20261105/preparation/reservation-check.md); '
    table+='[exact map](topics/padua-mz-cleanup-20261105/preparation/final-id-map.json); '
    table+='[batch ledger](topics/padua-batch-20261031/ALLOCATIONS.md). No accepted ID is renumbered.\n\n'
    table+='| Provisional alias | Final ID | Durable record / disposition |\n|---|---|---|\n'
    for row in data['theory']:
        table+=f"| {row['alias']} | {row['final']} | [record](topics/padua-mz-cleanup-20261105/{row['path']}); {row['status']} |\n"
    for row in data['ideas']:
        table+=f"| {row['alias']} | {row['final']} | [candidate](topics/padua-mz-cleanup-20261105/{row['path']}); {row['disposition']} |\n"
    table+='\nOriginal C3 target PD-T381 remains OPEN; split/support PD-T379 is PROVED. '
    table+='These supporting bounds are not a proved conjunct of the target and do not make it PARTIAL. '
    table+='PD-T377/378 extend PD-T295/PD-N105–107 without splitting or narrowing accepted statements. '
    table+='Permanent unused gaps: T382–391, N138–145, IDEA472–489; no LIT assignment.\n'
    changed[name]=text.rstrip()+table
    # Validate every old block before any writes; the branch mutation is one-shot.
    for name,text in changed.items():(root/name).write_text(text)
    rows=[[name,hashlib.sha256(original[name].encode()).hexdigest(),
           hashlib.sha256(text.encode()).hexdigest()] for name,text in changed.items()]
    (topic/'preparation/shared-registration.json').write_text(json.dumps(dict(
        source='a930f32fbf4568fbc431ddcf0b0fd689f5fa8201',
        method='8 exact old/new blocks plus audited theory/IDEA append sections and complete crosswalk',
        columns=['path','before_sha256','after_sha256'],files=rows),separators=(',',':'))+'\n')
    print(f'Applied {len(pairs)} checked replacements and registered six theory/six IDEA records')


if __name__=='__main__':main()
