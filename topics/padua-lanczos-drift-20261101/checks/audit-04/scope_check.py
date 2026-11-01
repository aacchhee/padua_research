"""Bounded audit04: exact logical examples and preservation checks; no imports from development."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import subprocess
import sys

BASE = '3cca9b929ac006a5ed4295b3beba909dfd602271'
CANDIDATE = '02bd97b892ed409ec64e9b281130c71a85e914e9'
READ_HEAD = '39b3c5d8690566ce461e6e3a0a628e772a695dbc'
TOPIC = Path('topics/padua-lanczos-drift-20261101')
IDEAS = str(TOPIC / 'ideas-e3-e4.md')
RECORD = 'tracks/bivariate-lanczos/theory/drift-codex-e1-05-finite-scalar-cgs2-capacities.md'
pins = {}
for path in ['state/IDEAS.md', IDEAS, RECORD]:
    data = subprocess.check_output(['git', 'show', CANDIDATE + ':' + path])
    assert data == Path(path).read_bytes()
    pins[path] = {'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}
for path, prefix in [(IDEAS, '- Separation criterion vs closest entry (and observation that falsifies it): R17b'),
                     (RECORD, '| Factor-ten target, rotQ24 conjunct')]:
    old = subprocess.check_output(['git', 'show', BASE + ':' + path]).decode().splitlines()
    new = Path(path).read_text().splitlines()
    def preserved(lines):
        return [s for s in lines if not s.startswith(prefix)
                and not s.startswith('- 2026-11-01 (Claude response-03,')]
    assert preserved(old) == preserved(new)

dot = lambda a, b: sum(x*y for x, y in zip(a, b))
r0, r1 = (F(1), F(0), F(0)), (F(0), F(1), F(0))
models = []
for c, s in [(F(3, 5), F(4, 5)), (F(9999, 10001), F(200, 10001))]:
    q = (F(0), c, s)
    Q = [r0, q, (F(0), s, -c)]
    assert all(dot(a, b) == int(i == j) for i, a in enumerate(Q) for j, b in enumerate(Q))
    assert c >= F(1, 2)
    raw = (F(0), c, F(0))
    pre = tuple(x-y for x, y in zip(raw, q))
    delta = tuple(x-y for x, y in zip(r1, q))
    def project(v):
        return tuple(sum(dot(col, v)*col[i] for col in Q) for i in range(3))
    assert project(pre) == pre and project(delta) == delta and pre != delta
    assert raw == tuple(c*x for x in r1)
    models.append({'gamma': str(c), 'pre_normalization_correction': list(map(str, pre)),
                   'normalized_difference': list(map(str, delta)), 'both_normal_components_zero': True})
bj, alt, pivot = F(9), F(1), F(1, 10)
assert bj*bj <= 100*alt*alt and bj > 10*min(alt, pivot)
assert not (bj*bj <= 100*min(alt*alt, pivot*pivot))
bj, alt, pivot = F(10), F(1), F(2)
assert bj*bj == 100*min(alt*alt, pivot*pivot) and not bj > 10*min(alt, pivot)
out = {'auditor': 'Codex independent scope subagent; configured gpt-6-astra high; resolved serving metadata unexposed',
       'read_head': READ_HEAD, 'candidate': CANDIDATE, 'previous_published': BASE,
       'command': 'python3 -B ' + str(Path(__file__).relative_to(Path.cwd())),
       'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'python': sys.version.split()[0], 'inputs': pins,
       'checks': {'unchanged_idea_content_except_separation_and_history': True,
                  'unchanged_record05_except_rotated_row_and_history': True,
                  'alt_only_countermodel': True, 'strict_target_equality_refutation': True,
                  'reference_countermodels': models}, 'all_pass': True,
       'limits': 'Exact elementary scope checks only; no experiment, scalar regeneration, IEEE realization or novelty claim.'}
(TOPIC / 'evidence/audit-04-scope.json').write_text(json.dumps(out, indent=2) + '\n')
print('PASS: preservation, scalar countermodel/equality, two rational reference examples')
