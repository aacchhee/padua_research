"""Preparation checker for PR15 (padua-lanczos-drift-20261101, handoff 11).

Works on committed Git objects only: --base is the pre-preparation commit, --head the
prepared commit. Checks the exact allowed edits and their preservation:
final-ID map, record headers, literal approved proposals, ID-only prose
substitution (with declared administrative edits listed separately), append-only
or named in-place registry changes, protected files, relative links, registry row
counts, a disposable squash rehearsal onto main and merge-tree checks against
other open PRs.
Usage: python3 validate.py --base <sha> --head <sha> --main <sha> [--pr PR12=<sha>] --output <json>
"""
import argparse, datetime, hashlib, importlib.util, json, os, re, subprocess, sys, tempfile


def git(*a, check=True):
    r = subprocess.run(['git', *a], capture_output=True, text=True)
    if check and r.returncode:
        raise SystemExit(f'git {a} failed: {r.stderr}')
    return r.stdout


def show(ref, path):
    r = subprocess.run(['git', 'show', f'{ref}:{path}'], capture_output=True)
    return r.stdout.decode() if r.returncode == 0 else None


T = 'topics/padua-lanczos-drift-20261101/'
TH = 'tracks/bivariate-lanczos/theory/'
MARK = '## Padua Lanczos drift campaign — PR15 final registration'
ADMIN = {T + 'report.md', T + 'plan.md', T + 'proposed-record-changes.md', T + 'directions/E4.md',
         'results/padua-lanczos-drift-20261101.md'}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--base', required=True); ap.add_argument('--head', required=True)
    ap.add_argument('--main', required=True); ap.add_argument('--pr', action='append', default=[])
    ap.add_argument('--output', required=True)
    a = ap.parse_args()
    base, head, mainsha = (git('rev-parse', x).strip() for x in (a.base, a.head, a.main))
    out = {'generated_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'),
           'code_sha256': hashlib.sha256(open(__file__, 'rb').read()).hexdigest(),
           'base': base, 'head': head, 'main': mainsha, 'checks': {}}
    c = out['checks']
    # Load the preparation module (substitution and literal blocks) from the HEAD bytes.
    spec_src = show(head, T + 'preparation/prepare.py')
    mod = type(sys)('prep'); mod.__dict__['__file__'] = 'prepare.py'
    cwd = os.getcwd()
    with tempfile.TemporaryDirectory() as td:
        os.makedirs(os.path.join(td, T, 'preparation'))
        open(os.path.join(td, T, 'preparation/final-id-map.json'), 'w').write(show(head, T + 'preparation/final-id-map.json'))
        open(os.path.join(td, T, 'proposed-record-changes.md'), 'w').write(show(base, T + 'proposed-record-changes.md'))
        os.chdir(td)
        try:
            exec(compile(spec_src, 'prepare.py', 'exec'), mod.__dict__)
            blocks = mod.literal_blocks()
        finally:
            os.chdir(cwd)
    M = json.loads(show(head, T + 'preparation/final-id-map.json'))
    mapping, decl = M['mapping'], M['declarations']
    # 1. Map.
    finals = list(mapping.values())
    def inr(f):
        m = re.match(r'(PD-T|PD-N|IDEA-|LIT-)(\d+)$', f); n = int(m.group(2))
        return {'PD-T': 136 <= n <= 155, 'PD-N': 62 <= n <= 71, 'IDEA-': 246 <= n <= 285, 'LIT-': 445 <= n <= 459}[m.group(1)]
    c['map'] = {'unique': len(set(finals)) == len(finals), 'all_in_own_reservation': all(inr(f) for f in finals),
                'counts': {k: sum(1 for x in decl.values() if x['kind'] == k) for k in ('PD-T', 'PD-N', 'IDEA')},
                'record14_unmapped': 'PD-N?drift-codex-14' not in mapping}
    c['map']['pass'] = c['map']['unique'] and c['map']['all_in_own_reservation'] and c['map']['counts'] == {'PD-T': 11, 'PD-N': 2, 'IDEA': 22} and c['map']['record14_unmapped']
    # 2. Records.
    rec = {}
    for ident, x in decl.items():
        if x['kind'] not in ('PD-T', 'PD-N'): continue
        s = show(head, x['path']); lines = s.split('\n')
        rec[ident] = lines[0].startswith('# ' + mapping[ident] + ' — ') and lines[2].startswith('Provisional alias: `' + ident + '`')
    c['records'] = {'headers_and_alias': all(rec.values()), 'record14_deleted': show(head, TH + 'drift-codex-e4-14-noiseless-quantifier-refutation.md') is None}
    c['records']['pass'] = c['records']['headers_and_alias'] and c['records']['record14_deleted']
    # 3. Literal proposals: recompute every inherited target from base.
    exp = {}
    for t, o, n in blocks:
        p = TH + t; s = exp.get(p, show(base, p)); assert s.count(o) == 1, t
        exp[p] = s.replace(o, mod.fill(n))
    c['literal'] = {'targets': {p: show(head, p) == v for p, v in exp.items()}, 'blocks': len(blocks)}
    others = [p for p in git('ls-tree', '-r', '--name-only', mainsha, TH).split() if 'drift-codex-' not in p and p not in exp]
    c['literal']['other_inherited_theory_identical_to_main'] = not git('diff', '--name-only', mainsha, head, '--', *others).strip()
    c['literal']['other_inherited_count'] = len(others)
    c['literal']['pass'] = all(c['literal']['targets'].values()) and c['literal']['other_inherited_theory_identical_to_main'] and len(blocks) == 16
    # 4. Prose: ID-only substitution, except declared administrative files.
    prose = sorted({x['path'] for x in decl.values()} | {T + f for f in ['report.md', 'plan.md', 'proposed-record-changes.md', 'independent-checks.md', 'external-code.md']}
                   | {T + 'directions/E%d.md' % i for i in range(1, 7)} | {'results/padua-lanczos-drift-20261101.md', 'tracks/bivariate-lanczos/code/drift/README.md'})
    imp = {}
    for p in prose:
        b, h = show(base, p), show(head, p)
        e = mod.substitute(b)
        ident = next((k for k, x in decl.items() if x['path'] == p and x['kind'] in ('PD-T', 'PD-N')), None)
        if ident:
            ls = e.splitlines(keepends=True)
            ls.insert(1, '\nProvisional alias: `' + ident + '`. Final ID assigned at PR preparation, 2026-11-01 (handoff 11, after Codex audit-04 acceptance).\n')
            e = ''.join(ls)
        if h == e:
            imp[p] = 'ID substitution only' + (' + alias line' if ident else '')
        else:
            el, hl = e.split('\n'), h.split('\n')
            changed = [l for l in hl if l not in el]
            imp[p] = {'declared_administrative': p in ADMIN, 'lines_not_from_substitution': len(changed)}
    c['prose_impact'] = imp
    c['prose_pass'] = all(isinstance(v, str) or v['declared_administrative'] for v in imp.values())
    # 5. Registries.
    reg = {}
    for f in ['state/CURRENT.md', 'PAPER_MAP.md', 'topics/README.md', 'tracks/bivariate-lanczos/README.md',
              'topics/padua-batch-20261031/ALLOCATIONS.md', 'RESULTS.md']:
        b, h = show(base, f), show(head, f)
        reg[f] = h.startswith(b.rstrip('\n')) and (MARK in h or f == 'RESULTS.md')
    ps_b, ps_h = show(base, 'PROOF_STATUS.md'), show(head, 'PROOF_STATUS.md')
    o75 = [l for l in ps_b.split('\n') if l.startswith('| PD-T075 |')][0]; n75 = [l for l in ps_h.split('\n') if l.startswith('| PD-T075 |')][0]
    reg['PROOF_STATUS.md'] = ps_h.replace(n75, o75).startswith(ps_b.rstrip('\n')) and 'PARTIAL' in n75.split('|')[3]
    id_b, id_h = show(base, 'state/IDEAS.md'), show(head, 'state/IDEAS.md')
    o151 = [l for l in id_b.split('\n') if l.startswith('| IDEA-151 |')][0]; n151 = [l for l in id_h.split('\n') if l.startswith('| IDEA-151 |')][0]
    reg['state/IDEAS.md'] = id_h.replace(n151, o151).startswith(id_b.rstrip('\n')) and n151.startswith(o151[:-2].rstrip())
    cw_b, cw_h = show(base, 'ID_CROSSWALK.md'), show(head, 'ID_CROSSWALK.md')
    pre_b = cw_b[:cw_b.index('## Lanczos drift reservation (no final assignment)')]
    reg['ID_CROSSWALK.md'] = cw_h.startswith(pre_b) and '## Lanczos drift reservation and PR15 final registration' in cw_h
    rb, rh = show(base, 'RESULTS.md'), show(head, 'RESULTS.md')
    reg['RESULTS_other_sections_preserved'] = rh.startswith(rb.rstrip('\n')) and rh.count('\n## padua-lanczos-drift-20261101') == 1
    c['registries'] = reg
    def rows(text, start):
        sec = text[text.index(start):]; nxt = re.search(r'\n## ', sec[3:])
        sec = sec[:nxt.start() + 3] if nxt else sec
        return sum(1 for l in sec.split('\n') if re.match(r'\| (PD-[TN]\d{3}|IDEA-\d{3}|PD-[TN]\?|IDEA\?)', l))
    c['registry_row_counts'] = {'PROOF_STATUS': rows(ps_h, MARK), 'IDEAS': rows(id_h, MARK),
                                'CROSSWALK': rows(cw_h, '## Lanczos drift reservation and PR15 final registration')}
    c['registry_counts_pass'] = c['registry_row_counts'] == {'PROOF_STATUS': 14, 'IDEAS': 22, 'CROSSWALK': 36}
    # 6. Protected files unchanged between base and head.
    names = git('diff', '--name-only', base, head).split()
    prot_rx = re.compile(r'^(' + re.escape(T) + r'(audit-0\d|response-0\d|checks/|evidence/|handoffs/0[0-9]|handoffs/10|COLD_STORAGE|local-results-entry|external-code)|tracks/bivariate-lanczos/code/drift/.*\.py$|\.github/|AGENTS\.md|agents/|templates/)')
    bad = [n for n in names if prot_rx.match(n) and n != T + 'external-code.md']
    c['protected_unchanged'] = not bad; c['protected_violations'] = bad
    # 7. Relative links in changed markdown files resolve at head.
    tree = set(git('ls-tree', '-r', '--name-only', head).split()); dirs = {os.path.dirname(p) for p in tree}
    broken = []
    for p in names:
        if not p.endswith('.md'): continue
        s = show(head, p)
        if s is None: continue
        s = re.sub(r'«.*?»', '', s, flags=re.S)  # quoted original wording is history, not a live link
        for m in re.finditer(r'\]\(([^)#\s]+)(?:#[^)]*)?\)', s):
            u = m.group(1)
            if re.match(r'[a-z]+:', u): continue
            q = os.path.normpath(os.path.join(os.path.dirname(p), u))
            if q not in tree and q not in dirs and q.rstrip('/') not in dirs: broken.append((p, u))
    c['broken_links'] = broken[:50]; c['links_pass'] = not broken
    # 8. Squash rehearsal and merge-tree.
    with tempfile.TemporaryDirectory() as td:
        wt = os.path.join(td, 'wt'); git('worktree', 'add', '--detach', wt, mainsha)
        try:
            r = subprocess.run(['git', '-C', wt, 'merge', '--squash', head], capture_output=True, text=True)
            tree_sq = subprocess.run(['git', '-C', wt, 'write-tree'], capture_output=True, text=True).stdout.strip()
            c['squash'] = {'rc': r.returncode, 'tree_equals_head': tree_sq == git('rev-parse', head + '^{tree}').strip(),
                           'main_is_ancestor': subprocess.run(['git', 'merge-base', '--is-ancestor', mainsha, head]).returncode == 0}
        finally:
            git('worktree', 'remove', '--force', wt)
    mt = {}
    for spec in a.pr:
        k, v = spec.split('=')
        r = subprocess.run(['git', 'merge-tree', '--write-tree', '--name-only', head, v], capture_output=True, text=True)
        mt[k] = {'ref': git('rev-parse', v).strip(), 'clean': r.returncode == 0,
                 'conflicts': [l for l in r.stdout.splitlines()[1:] if l and not l.startswith(('Auto-merging', 'CONFLICT'))]}
    c['merge_tree'] = mt
    ok = (c['map']['pass'] and c['records']['pass'] and c['literal']['pass'] and c['prose_pass'] and all(reg.values())
          and c['registry_counts_pass'] and c['protected_unchanged'] and c['links_pass'] and c['squash']['rc'] == 0
          and c['squash']['tree_equals_head'] and c['squash']['main_is_ancestor'] and all(v['clean'] for v in mt.values()))
    out['result'] = 'PASS' if ok else 'FAIL'
    json.dump(out, open(a.output, 'w'), indent=1, ensure_ascii=False); print(out['result'])


if __name__ == '__main__':
    main()
