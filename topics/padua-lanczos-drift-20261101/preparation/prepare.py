"""PR-preparation assignment for padua-lanczos-drift-20261101 (handoff 11).

Performs only approved mechanical work: final-ID substitution in current developer
prose, the 15 literal approved OLD/NEW blocks (+ one History anchor) from
proposed-record-changes.md, removal of the withdrawn record-14 tombstone, and
append-only registry sections. No Git operations. Dry run by default;
--apply writes files and the receipt preparation/prepare-receipt.json.
"""
import argparse, datetime, hashlib, json, pathlib, re, sys

R = pathlib.Path('.')
T = R / 'topics/padua-lanczos-drift-20261101'
P = T / 'preparation'
TH = R / 'tracks/bivariate-lanczos/theory'
PREPARER = 'Claude PR preparation (configured claude-opus-5-5, high)'
TS = '2026-11-01'
MARK = '## Padua Lanczos drift campaign — PR15 final registration'

MAP = json.loads((P / 'final-id-map.json').read_text())
mapping = MAP['mapping']                       # provisional -> final
decl = MAP['declarations']                     # provisional -> {path,title,kind}
PAT = re.compile('|'.join(re.escape(k) for k in sorted(mapping, key=len, reverse=True)))


def sha(b): return hashlib.sha256(b).hexdigest()
def cell(s): return re.sub(r'\s+', ' ', s).strip().replace('|', '\\|')


def substitute(s):
    """Replace provisional IDs with final IDs outside «...» quotations (quoted
    original wording is preserved verbatim)."""
    out, i = [], 0
    for m in re.finditer(r'«.*?»', s, re.S):
        out.append(PAT.sub(lambda x: mapping[x.group()], s[i:m.start()]))
        out.append(m.group())
        i = m.end()
    out.append(PAT.sub(lambda x: mapping[x.group()], s[i:]))
    return ''.join(out)


def literal_blocks():
    """The approved OLD/NEW pairs, in file order, with their targets."""
    s = (T / 'proposed-record-changes.md').read_text()
    pairs = re.findall(r'\nOLD\n```text\n(.*?)\n```\n+NEW[^\n]*\n```text\n(.*?)\n```', s, re.S)
    targets = (['bj-universal-reorthogonalization-obstruction-open.md',
                'condition-C-staircase-selections-acyclic-sections.md',
                'bivariate-lanczos-claude-300-l3q1-backward-interpretation-target.md']
               + ['bivariate-lanczos-claude-319-padua-obstruction-radius-uniformity.md'] * 3
               + ['reorthogonalization-does-not-restore-graded-spaces.md',
                  'one-relation-selections-do-not-keep-spans-near-Sn.md']
               + ['bivariate-lanczos-claude-319-padua-obstruction-radius-uniformity.md'] * 4
               + ['bivariate-lanczos-claude-313-padua-turan-certificate-all-n.md'] * 2
               + ['bivariate-lanczos-claude-305-three-node-square-case-sqrt-rate.md'])
    assert len(pairs) == 15 == len(targets), len(pairs)
    blocks = [(t, o, n) for t, (o, n) in zip(targets, pairs)]
    # Block 7 History anchor (written in prose in the proposal).
    anchor = '2026-10-31, Claude Opus 5.5 (xhigh, requested), L3 developer, base 2d8c3ab: created in round R01.'
    hist = (anchor + '\n- <prep-ts>, <preparer>: Open item cross-referenced to the explicit instance '
            'PD-T?drift-codex-31; statement and status unchanged. Original wording: «Explicit constants.».')
    blocks.append(('bivariate-lanczos-claude-305-three-node-square-case-sqrt-rate.md', anchor, hist))
    return blocks


def fill(s):
    return substitute(s.replace('<prep-ts>', TS).replace('<preparer>', PREPARER))


def main(apply):
    before, writes, deletes = {}, {}, []

    def read(p):
        p = pathlib.Path(p)
        if p not in before:
            before[p] = p.read_bytes() if p.exists() else None
        return (writes.get(p) or before[p] or b'').decode()

    def write(p, s):
        p = pathlib.Path(p); read(p); writes[p] = s.encode()

    def append(p, s):
        old = read(p); assert MARK not in old, p
        write(p, old.rstrip('\n') + '\n\n' + s.strip('\n') + '\n')

    # 1. Literal approved proposals into inherited theory (sequential, unique).
    applied = []
    for t, o, n in literal_blocks():
        p = TH / t; s = read(p)
        assert s.count(o) == 1, (t, s.count(o), o[:80])
        nn = fill(n)
        write(p, s.replace(o, nn))
        applied.append({'target': str(p), 'old_sha256': sha(o.encode()), 'new_sha256': sha(nn.encode())})

    # 2. Final IDs in current developer prose + canonical alias line in records.
    prose = [pathlib.Path(x['path']) for k, x in decl.items() if x['kind'] in ('PD-T', 'PD-N')]
    prose += [T / f for f in ['ideas-e1.md', 'ideas-e3-e4.md', 'ideas-e5.md', 'ideas-e6.md', 'report.md', 'plan.md',
                              'proposed-record-changes.md', 'independent-checks.md', 'external-code.md']]
    prose += sorted((T / 'directions').glob('E[0-9].md'))
    prose += [R / 'results/padua-lanczos-drift-20261101.md', R / 'tracks/bivariate-lanczos/code/drift/README.md']
    impact = []
    for p in prose:
        s = read(p); new = substitute(s)
        ident = next((k for k, x in decl.items() if x['path'] == str(p) and x['kind'] in ('PD-T', 'PD-N')), None)
        if ident:
            lines = new.splitlines(keepends=True)
            assert lines[0].startswith('# ' + mapping[ident] + ' '), (p, lines[0][:60])
            lines.insert(1, '\nProvisional alias: `' + ident + '`. Final ID assigned at PR preparation, ' + TS +
                         ' (handoff 11, after Codex audit-04 acceptance).\n')
            new = ''.join(lines)
        write(p, new)
        impact.append({'path': str(p), 'id_substitution_only': True, 'alias_line_added': bool(ident)})

    # 3. Withdrawn record-14 tombstone.
    tomb = TH / 'drift-codex-e4-14-noiseless-quantifier-refutation.md'
    assert tomb.exists(); read(tomb); deletes.append(tomb)

    # 4. Registries (append-only sections; three named in-place row updates).
    rows = []
    for ident, x in sorted(decl.items(), key=lambda v: mapping[v[0]]):
        if x['kind'] not in ('PD-T', 'PD-N'): continue
        s = read(x['path'])
        st = re.search(r'Overall status:\s*\**(PROVED|PARTIAL|CONDITIONAL|MEASURED|OPEN)', s)
        assert st, ident
        rows.append((mapping[ident], ident, x, st.group(1)))
    ps = (MARK + '\n\nStage **PR**. Codex [audit-04](topics/padua-lanczos-drift-20261101/audit-04.md) accepted the final '
          'response; earlier audits: Claude [audit-01](topics/padua-lanczos-drift-20261101/audit-01.md), Codex '
          '[audit-02](topics/padua-lanczos-drift-20261101/audit-02.md)/[03](topics/padua-lanczos-drift-20261101/audit-03.md). '
          'Final IDs from the PR15 reservation (first published `6920ba6`). Exact statements, quantifiers and part '
          'tables are in the linked records; summaries below do not broaden them. No actual-IEEE, all-degree, general '
          'staircase, PD-T055, PD-T075(U2) or PD-T056(G) claim follows.\n\n'
          '| ID | Claim | Status | Evidence | Disposition / reason | Depends on | Record | Audit |\n'
          '|---|---|---|---|---|---|---|---|\n')
    for final, ident, x, st in rows:
        ps += '| ' + ' | '.join([final + ' (' + ident + ')', cell(x['title']), st, cell(x['evidence']),
                                 cell(x['disposition']), ', '.join(x['depends_on']) or 'elementary; see record',
                                 '[record](' + x['path'] + ')', 'Claude audit-01; Codex audits 02–04 (accepted)']) + ' |\n'
        if final == 'PD-T140':
            ps += ('| PD-T140 (target part) | Factor-ten target K_BJ > 10 min(K_alt, K_pivot) on T24 and on rotQ24 '
                   '(formal scalar-CGS2 model, degree 12) | PARTIAL | T24 conjunct PROVED in PD-T141(c); rotQ24 conjunct '
                   'OPEN (certificate ratio 62.09 < 100) | Separately labelled claim inside PD-T140; the experiment row '
                   'above stays MEASURED and the both-grid sufficient test INCONCLUSIVE | PD-T141 | '
                   '[record](' + x['path'] + ') | Codex audit-03 accepted PARTIAL |\n')
    append('PROOF_STATUS.md', ps)
    pf = read('PROOF_STATUS.md')
    old75 = [l for l in pf.split('\n') if l.startswith('| PD-T075 |')]
    assert len(old75) == 1
    new75 = ('| PD-T075 | PARTIAL ((U1) PROVED in PD-T144; (U2) OPEN): dependence on n of the Padua obstruction radius '
             '(does the positivity radius of P_n tend to 0? is there an obstruction radius uniform in n?) | PARTIAL | '
             '(U1) ρ_n → 0: PROVED, split to PD-T144 (ρ_n = O(n^-5)); (U2) inf_n δ_obs(n) > 0: OPEN | split into PD-T144 '
             '(U1) | PD-T058, PD-T059, PD-T069, PD-N020, PD-N022 | '
             '[bivariate-lanczos-claude-319-padua-obstruction-radius-uniformity.md](tracks/bivariate-lanczos/theory/'
             'bivariate-lanczos-claude-319-padua-obstruction-radius-uniformity.md) | bivariate-lanczos audits 01–03 '
             '(Codex); U1 split at PR15 preparation (padua-lanczos-drift-20261101 audits 01–04) |')
    write('PROOF_STATUS.md', pf.replace(old75[0], new75))

    ideas = (MARK + '\n\nAll 22 candidates, including failed, equivalent, rejected and deferred routes, are retained in '
             'full at the linked canonical files (topic `padua-lanczos-drift-20261101`). The withdrawn draft '
             '`PD-N?drift-codex-14` is IDEA-253 only; it has no PD-N. Disposition summaries below do not broaden '
             'their scopes.\n\n| ID | Provisional alias | Candidate | Disposition / scope | Full record |\n'
             '|---|---|---|---|---|\n')
    for ident, x in sorted(decl.items(), key=lambda v: mapping[v[0]]):
        if x['kind'] != 'IDEA': continue
        s = read(x['path'])
        h = re.search(r'^## ' + re.escape(mapping[ident]) + r' — [^\n]*\n(.*?)(?=^## |\Z)', s, re.M | re.S)
        assert h, ident
        d = re.search(r'^- (?:Candidate )?[Dd]isposition[^:\n]*:\s*(.*?)(?=\n- |\n\n|\Z)', h.group(1), re.M | re.S)
        disp = cell(d.group(1)) if d else 'see full candidate'
        ideas += '| ' + ' | '.join([mapping[ident], ident, cell(x['title']), disp,
                                    '[full candidate](../' + x['path'] + ')']) + ' |\n'
    append('state/IDEAS.md', ideas)
    si = read('state/IDEAS.md')
    r151 = [l for l in si.split('\n') if l.startswith('| IDEA-151 |')]
    assert len(r151) == 1 and r151[0].endswith(' |')
    n151 = r151[0][:-2].rstrip() + ' Polynomial span-drift form of the safety question registered as OPEN in PD-T054\'s open item; sufficient criterion in PD-T142/PD-T143 (padua-lanczos-drift-20261101). |'
    write('state/IDEAS.md', si.replace(r151[0], n151))

    cw = read('ID_CROSSWALK.md')
    sec = re.search(r'## Lanczos drift reservation \(no final assignment\)\n.*?(?=\n## |\Z)', cw, re.S)
    assert sec
    crow = ('## Lanczos drift reservation and PR15 final registration\n\nReservation PD-T136–155, PD-N062–071, '
            'IDEA-246–285, LIT-445–459, first published `6920ba632843597c37e1493d077c1df2e89f54cb` in the '
            '[shared batch ledger](topics/padua-batch-20261031/ALLOCATIONS.md), kept unchanged through the PR14-first '
            'merge of main `e0d9e3d`. Final map: [final-id-map.json](topics/padua-lanczos-drift-20261101/preparation/'
            'final-id-map.json). Assigned at PR preparation, ' + TS + ', after Codex audit-04 acceptance. No accepted ID '
            'is renumbered.\n\n| Provisional ID | Final ID | Origin | Durable record | Audit / provenance |\n'
            '|---|---|---|---|---|\n')
    for ident, final in sorted(mapping.items(), key=lambda v: v[1]):
        crow += '| ' + ' | '.join([ident, final, 'codex/padua-lanczos-drift-20261101',
                                   '[record](' + decl[ident]['path'] + ')',
                                   'Claude audit-01; Codex audits 02–04; development by Codex, responses by Claude']) + ' |\n'
    crow += ('| PD-N?drift-codex-14 | none (IDEA-253) | codex/padua-lanczos-drift-20261101 | withdrawn; content in '
             '[IDEA-253](topics/padua-lanczos-drift-20261101/ideas-e3-e4.md) | Converted in response-01 (audit-01 E34-F3); '
             'tombstone removed at preparation; no PD-N allocated |\n')
    crow += ('\nOriginal-to-split relations: PD-T140 (formerly carrying the finite inequalities) → **PD-T141** (finite '
             'computer-assisted PROVED, formal scalar model); PD-T140 keeps the MEASURED experiment, the INCONCLUSIVE '
             'both-grid sufficient test and its separately labelled factor-ten target, PARTIAL (T24 conjunct PROVED in '
             'PD-T141, rotQ24 conjunct OPEN). **PD-T075(U1) → PD-T144** (ρ_n = O(n^-5) for the named certificate); '
             'PD-T075 becomes PARTIAL with (U2) OPEN. PD-N062 is the generalized fixed-degree closure lemma and exact '
             'instance of PD-T055\'s recorded heuristic; PD-T055 stays OPEN. PD-N063 records three scoped failed '
             'negative-witness mechanisms. Permanent unused gaps: PD-T147–155, PD-N064–071, IDEA-268–285, LIT-445–459.\n')
    write('ID_CROSSWALK.md', cw[:sec.start()] + crow.rstrip('\n') + cw[sec.end():])

    led = 'topics/padua-batch-20261031/ALLOCATIONS.md'
    append(led, MARK + '\n\nOwn reservation unchanged (first published `6920ba632843597c37e1493d077c1df2e89f54cb`): '
           'assigned **PD-T136–146 (11), PD-N062–063 (2), IDEA-246–267 (22)**, no LIT. Permanent unused headroom: '
           '**PD-T147–155, PD-N064–071, IDEA-268–285, LIT-445–459**. No range shifts, shrinks or reuses another topic\'s '
           'IDs; PR14\'s assignments and gaps above are preserved. [Map](../padua-lanczos-drift-20261101/preparation/'
           'final-id-map.json); [fresh union scan](../padua-lanczos-drift-20261101/preparation/union-scan.json).')
    append('state/CURRENT.md', MARK + '\n\nFinite-precision bivariate Lanczos span drift (draft PR15, stage PR after '
           'Codex audit-04 acceptance): normal-quotient span derivative and rational certificates (PD-T136/137), '
           'formal scalar-CGS2 normal map (PD-T138), finite aggregate and scalar separations (PD-T139, PD-T141), '
           'MEASURED scalar experiment with PARTIAL factor-ten target (PD-T140), computed-polynomial span certificate '
           'and fixed-degree selection criterion (PD-T142/143), fixed-degree closure lemma (PD-N062), Padua radius '
           'ρ_n = O(n^-5) (PD-T144, splitting PD-T075(U1)), square √ε family (PD-T145), failed witness paths (PD-N063), '
           'MEASURED public polyrat drift (PD-T146). OPEN: all-degree drift (E2), general staircase safety, PD-T055, '
           'PD-T075(U2), PD-T056(G). [Report](../topics/padua-lanczos-drift-20261101/report.md), '
           '[results](../results/padua-lanczos-drift-20261101.md).')
    append('PAPER_MAP.md', MARK + '\n\n| Brief | Question | Support | Remaining gaps | Readiness |\n|---|---|---|---|---|\n'
           '| [Lanczos drift campaign](topics/padua-lanczos-drift-20261101/report.md) | Span drift of computed '
           'bivariate Lanczos bases; Padua obstruction radius rate | PD-T136–146; PD-N062–063 at their individual '
           'statuses | All-degree drift, staircase safety, PD-T055, PD-T075(U2), PD-T056(G) OPEN; formal-model results '
           'imply no IEEE claim | PR prepared after Codex audit-04; draft PR15, AC decision pending; no manuscript claim |')
    append('topics/README.md', MARK + '\n\n[padua-lanczos-drift-20261101](padua-lanczos-drift-20261101/LOG.md): '
           'finite-precision bivariate Lanczos span drift; PD-T136–146, PD-N062–063, IDEA-246–267. Stage PR; Codex '
           'audit-04 accepted; draft PR15, AC merge decision pending.')
    append('tracks/bivariate-lanczos/README.md', MARK + '\n\nSpan-drift development (topic padua-lanczos-drift-20261101) '
           'is registered as PD-T136–146 and PD-N062–063 with individual statuses; IDEA-246–267 retain all candidates. '
           'Code: `code/drift/` ([README](code/drift/README.md)). PD-T075 is now PARTIAL ((U1) PROVED in PD-T144).')

    # 5. Write.
    changes = [{'path': str(p), 'before_sha256': sha(before[p]) if before[p] is not None else None,
                'after_sha256': sha(b), 'bytes': len(b)} for p, b in writes.items() if before[p] != b]
    receipt = {'apply': apply, 'preparer': PREPARER, 'date': TS, 'literal_blocks_applied': applied,
               'prose_impact': impact, 'deleted': [str(p) for p in deletes], 'changed_files': changes,
               'counts': {k: sum(1 for x in decl.values() if x['kind'] == k) for k in ('PD-T', 'PD-N', 'IDEA')}}
    if apply:
        for p, b in writes.items():
            cur = p.read_bytes() if p.exists() else None
            assert cur == before[p], ('concurrent modification', str(p))
        for p, b in writes.items():
            p.write_bytes(b)
        for p in deletes:
            p.unlink()
        (P / 'prepare-receipt.json').write_text(json.dumps(receipt, indent=1, ensure_ascii=False) + '\n')
    print(json.dumps({'apply': apply, 'changed': len(changes), 'deleted': len(deletes),
                      'literal_blocks': len(applied), 'counts': receipt['counts']}))


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('--apply', action='store_true')
    main(ap.parse_args().apply)
