#!/usr/bin/env python3
"""Mechanical final-ID substitution in root-owned live records only."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
M=json.loads((R/'preparation/final-id-map.json').read_text())
ALIASES={x['provisional']:x['final'] for x in M['records']+M['ideas']}
ALIASES.update({'PD-N?...-13':'PD-N105','PD-N?...-14':'PD-N106','PD-T?...-12':'PD-T295','PD-T…12':'PD-T295','PD-N…13':'PD-N105','PD-N…14':'PD-N106','PD-N…f3-01':'PD-N107','PD-T…f3-01':'PD-T296','PD-T…f4-01':'PD-T297','PD-N…10':'PD-N104','PD-T…11':'PD-T294','PD-T…90/91':'PD-T298/299'})
def substitute(s):
 for a,b in sorted(ALIASES.items(),key=lambda x:-len(x[0])):s=s.replace(a,b)
 return s
for rec in M['records']:
 p=R/rec['path']
 if not p.exists():continue
 before=p.read_text()
 if before.startswith('# '+rec['final']+' '):continue
 after=substitute(before);lines=after.splitlines(keepends=True)
 lines.insert(2,'Development alias: `'+rec['provisional']+'`. Final ID assigned during audited preparation; [mapping](../preparation/final-id-map.json).\n\n')
 p.write_text(''.join(lines)+'\n2026-11-05: mechanical final-ID registration after accepted Claude audit-01 and response-01. The earlier audited source/receipt identities are historical; proof content changes only by ID substitution.\n')
for p in list((R/'attempts').glob('*.md'))+[R/'report.md',R/'gates.md']:
 p.write_text(substitute(p.read_text()))
