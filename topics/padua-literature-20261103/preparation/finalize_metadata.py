"""Install PR21 administrative registration after apply_records.py.

Run from a reconciled checkout; no Git operations or scientific claim changes.
"""
import argparse
import json
import re
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument('--repo', type=Path, default=Path('.'))
a = ap.parse_args()
root = a.repo.resolve()
topic = 'topics/padua-literature-20261103'
p = root / topic
m = json.loads((p/'preparation/final-id-map.json').read_text())
mapping = m['mapping']

def append(path, marker, text):
    f = root/path
    old = f.read_text()
    if marker not in old:
        f.write_text(old.rstrip()+'\n\n'+text.strip()+'\n')

source_files = set()
for token in mapping:
    for f in (root/'literature/records').glob('*.md'):
        # This campaign's new records carry their own canonical aliases.
        if token in f.read_text() and '2026-11-05 PR21 final registration' not in f.read_text():
            source_files.add(f)
for f in sorted(source_files):
    s = f.read_text()
    tokens = sorted(set(re.findall(r'LIT\?padua-literature-claude-\d{2}(?!\d)', s)))
    if not tokens:
        continue
    first, rest = s.split('\n', 1)
    ids = ', '.join(sorted({mapping[x] for x in tokens}, key=lambda x:int(x[4:])))
    notice = ('\n\nRegistration (2026-11-05 PR21 final registration): '+ids+
              '. Original provisional aliases remain below; '
              '[exact map](../../'+topic+'/preparation/final-id-map.json). '
              'Source statements, versions, reader attribution and reading limits are unchanged. '
              'Developer-only source checks remain qualified by audit02/03; no independent auditor page-image verification is inferred.\n')
    # Only labels change: preserve the original alias in each statement heading.
    rest = re.sub(r'(?m)^(#{2,4}) (LIT\?padua-literature-claude-\d{2})(?!\d)',
                  lambda x: x[1]+' '+mapping[x[2]]+' ('+x[2]+')', rest)
    f.write_text(first+notice+rest)

# Compact current outcome; the full chronological working history stays in LOG.
results = '''# padua-literature-20261103 — audited literature registration

Audited source footing for the Padua Lebesgue function, Clenshaw–Curtis/Padua MZ constants, bivariate Lanczos/V+A and Leuven IEP/MOP line. This is literature attribution and bounded source reading, with no new local mathematical proof or PD status change.

- **Registration:** 58 provisional statement aliases reconciled. 31 new statement IDs LIT-482–512; 27 aliases reuse accepted IDs. LIT-513–561 remain permanent unused gaps. [Exact map](../topics/padua-literature-20261103/preparation/final-id-map.json), [deduplication](../topics/padua-literature-20261103/preparation/literature-dedup.md), [ledger](../topics/padua-literature-20261103/ALLOCATIONS.md). Existing PR22 source identities/coverage, including both distinct halves of LIT-420, are preserved.
- **P1:** the Padua vertex maximum was conjectured in the 2008 poster and observed in De Marchi2022. KL2021 supplies the published global coefficient4/π² and hence the corner upper estimate; no unchecked transfer of its noncorner lower estimate to the corner is asserted. Exact-corner/second-term and proof comparisons retain their documented search limits. [Comparison](../topics/padua-literature-20261103/p1-comparison.md).
- **P2:** signed cubature existence/exactness is attributed to SVZ2008; the reported journal normalization misprint is qualified by its source-reading provenance. Mastroianni–Russo's powered weight hypothesis and excluded CC/A2 endpoint are recorded; the missing borderline-MZ decay estimate is distinguished from its polynomial approximation-error rates. [Comparison](../topics/padua-literature-20261103/p2-comparison.md).
- **P3:** the full-sequence Favard/commuting machinery is classical; finite/truncated/words/manifold claims keep their distinct comparison scopes. Greenbaum branches, exact-section versus actual-run quantities, and revised V+A locators are separated. [Comparison](../topics/padua-literature-20261103/p3-comparison.md).
- **P4:** source authorship, RQ/QR, finite stability observations, Laurie author-awareness and future-work wording are corrected. Proposed joint questions remain unregistered and require their own future novelty gate; classical downdating is distinguished. [Memo](../topics/padua-literature-20261103/p4-memo.md).
- **Search scope:** AC's dated MathSciNet zero result is an indexed-query outcome, not publication absence. Title/review-only triage is not full-text exclusion. No exhaustive priority or manuscript/submission readiness is certified.
- **Audit:** audit01 F1–F6 resolved in audit02; F7 resolved in audit03. Inaccessible journal/image/NTNU/Crossref checks remain developer-verified only; acceptance does not promote them to independent auditor verification. [Audit02](../topics/padua-literature-20261103/audit-02.md), [audit03](../topics/padua-literature-20261103/audit-03.md).
- **Preparation:** main includes merged PR25/26/22; audited proposals are applied with explicit ID/alias mapping and preserved foreign records. Verification, rehearsal and independent preparation review are recorded in [preparation/record.md](../topics/padua-literature-20261103/preparation/record.md).
- **Remaining reading:** print-only and version/coverage gaps stay in [DOWNLOADS](../topics/padua-literature-20261103/DOWNLOADS.md) and the source records. They qualify this bounded literature registration; no new source campaign is assigned here.

The scientific statuses mentioned in historical comparison memos are those of their input scope. Current PROOF_STATUS.md and the separately accepted newer campaigns are authoritative, including the signed-Padua supersessions; this literature PR changes none of them. Only AC merges.
'''
(root/'results/padua-literature-20261103.md').write_text(results)
merged = root/'RESULTS.md'
marker = '## padua-literature-20261103\n'
assert marker not in merged.read_text(), 'Existing own section must be reconciled explicitly'
merged.write_text(merged.read_text().rstrip()+'\n\n'+marker+'\n'+results.split('\n',1)[1].lstrip().replace('(../topics/', '(topics/'))

cross = '''## Padua literature campaign — PR21 final source-statement mapping

Owner `claude/padua-literature-20261103`; permanent LIT-482–561 first published `fe946c9701916dce042af48c0e2705eac9d87db9`. [Topic ledger](topics/padua-literature-20261103/ALLOCATIONS.md); [shared batch ledger](topics/padua-batch-20261031/ALLOCATIONS.md); [fresh union](topics/padua-literature-20261103/preparation/allocation-scan.json); [deduplication](topics/padua-literature-20261103/preparation/literature-dedup.md). No accepted ID is renumbered. New statement IDs482–512; unused513–561 permanent. Existing broad/overlapping IDs117/118/348,119/347,346,420 and the other reused statements remain distinct where historically registered; coverage addenda do not erase earlier provenance or become independent source verification.

| Provisional alias | Final statement ID | Decision |
|---|---|---|
'''
new = set(range(482, 513))
for token, fid in sorted(mapping.items()):
    cross += '| '+token+' | '+fid+' | '+('new within own reservation' if int(fid[4:]) in new else 'same-statement reuse; coverage addendum')+' |\n'
append('ID_CROSSWALK.md','## Padua literature campaign — PR21 final source-statement mapping',cross)

ledger = '''## PR21 audited literature registration — 2026-11-05

Unchanged reservation LIT-482–561 (80), owner claude/padua-literature-20261103, first published fe946c9701916dce042af48c0e2705eac9d87db9. [Topic ledger](../padua-literature-20261103/ALLOCATIONS.md), [fresh union](../padua-literature-20261103/preparation/allocation-scan.json), [exact map](../padua-literature-20261103/preparation/final-id-map.json). Main9322fba and open PR21/24 checked, including every inherited/retired ledger and four canonical registries; all returned closed PRs merged. New31 statement IDs482–512;27 aliases reuse accepted statements. LIT513–561 remain permanent gaps. No PD-T/PD-N/IDEA range or assignment. Other topics' reservations and final assignments remain intact; no source-verification upgrade or mathematical status change.
'''
append('topics/padua-batch-20261031/ALLOCATIONS.md','## PR21 audited literature registration — 2026-11-05',ledger)
append(topic+'/ALLOCATIONS.md','## Final assignment — 2026-11-05', '''## Final assignment — 2026-11-05

Fresh union at main9322fba and open PR21/24: [receipt](preparation/allocation-scan.json). Assigned31 new statement IDs LIT-482–512;27 provisional aliases reuse existing statement IDs. [Exact58-alias map](preparation/final-id-map.json), [deduplication](preparation/literature-dedup.md). Permanent unused gaps LIT-513–561. No new reservation, no renumbering and no PD-T/PD-N/IDEA assignment. Original first-publication priority is unchanged. Earlier “no final IDs” prose is historical and superseded only by this preparation entry.
''')

append('topics/README.md','## Padua literature campaign — audited PR21 registration','''## Padua literature campaign — audited PR21 registration

[Report](padua-literature-20261103/report.md), [final source map](padua-literature-20261103/preparation/final-id-map.json), [results](../results/padua-literature-20261103.md). Source attribution/coverage campaign completed at its bounded audited scope; no new mathematical claim or source-proof status.31 new LIT482–512,27 reused aliases;513–561 permanent gaps. Preparation/readiness evidence in the topic record; only AC merges. Source gaps remain disclosed, not a queued new campaign.
''')
append('state/CURRENT.md','## Literature footing — PR21 audited registration','''## Literature footing — PR21 audited registration

The [literature report](../topics/padua-literature-20261103/report.md) and [source map](../topics/padua-literature-20261103/preparation/final-id-map.json) register the accepted bounded P1–P4 comparisons and corrections:31 new source-statement IDs482–512 and27 reused aliases. Completed preparation replaces the earlier initialization/download-list task at this scope. Source gaps, search-negative limits and developer-only journal/image/NTNU/Crossref checks remain explicit; no further source campaign or manuscript is assigned here. No mathematical frontier, PD status or accepted PR25/26 result is changed. Only AC merges.
''')
append('PAPER_MAP.md','## Audited literature footing — PR21','''## Audited literature footing — PR21

The [P1–P4 report](topics/padua-literature-20261103/report.md), [comparisons](topics/padua-literature-20261103/p1-comparison.md) and [final source map](topics/padua-literature-20261103/preparation/final-id-map.json) supply bounded literature attribution for later manuscript revisions. They distinguish historical conjectures, global versus corner estimates, classical signed cubature/Favard machinery and scoped Leuven proposals. Inaccessible source checks remain developer-verified; no exhaustive novelty, local source-theorem proof, manuscript acceptance or submission readiness follows. Mathematical source statuses and newer accepted scientific campaigns remain authoritative and unchanged.
''')

report = p/'report.md'
s = report.read_text()
s = s.replace('# Report — padua-literature-20261103 (WORK complete; audit pending)', '# Report — padua-literature-20261103 (audited literature registration)')
notice = '''
Final preparation note (2026-11-05): audit01–03 resolved F1–F7 at the recorded bounded scopes. The [58-alias final map](preparation/final-id-map.json) assigns31 new LIT482–512 and reuses27 accepted statements;513–561 remain permanent gaps. Shared source records are reconciled with main including merged PR25/26. Source-reading VERIFIED labels credit the developer; audit02/03 retain developer-only journal/image/NTNU/Crossref limits and nonexhaustive priority scope. Current PROOF_STATUS.md supersedes historical mathematical-status language below; this literature registration changes no PD status. Preparation checks and readiness are recorded in [preparation/record.md](preparation/record.md).
'''
if 'Final preparation note (2026-11-05)' not in s:
    first, rest = s.split('\n',1)
    s = first+'\n'+notice+rest
s = s.replace('## Audit request\n\nCodex (gpt-6-astra high) audits this Claude development; see handoff 02.', '## Audit and preparation\n\nAudits01–03 accepted the corrected bounded literary statements. Source-verification limits remain explicit. Final mechanical registration and checks are recorded in preparation/record.md; only AC merges.')
report.write_text(s)
