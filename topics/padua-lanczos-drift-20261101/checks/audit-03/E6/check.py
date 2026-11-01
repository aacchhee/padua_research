"""Audit-03 E6: independent JSON/pin checks and exact midpoint geometry.

The production off-sample run and reused audit-02 compatibility probes must be
executed first. This script does not write any frozen developer evidence.
"""
import argparse
import ast
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform
import subprocess

ROOT = Path(__file__).resolve().parents[5]
TOPIC = ROOT / 'topics/padua-lanczos-drift-20261101'
CANDIDATE = 'ea829d92d509f79326a1cc037844a1bac3b4de13'
RULES_HEAD = 'c8849a89a601e0a56342d3d568086ab8abdbc4c0'
BEFORE = '1df5f89fe52f62c49d5addd58dcfea7246c5a688'
EXTERNAL = Path('/workspace/padua-drift-external/polyrat')


def pin(p):
    raw = Path(p).read_bytes()
    return {'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}


def flatten(value, path=''):
    if isinstance(value, dict):
        return {k: v for key, child in value.items()
                for k, v in flatten(child, path + '/' + key).items()}
    if isinstance(value, list):
        return {k: v for i, child in enumerate(value)
                for k, v in flatten(child, path + '/' + str(i)).items()}
    return {path: value}


def compare(left, right, masks):
    a, b = json.loads(Path(left).read_text()), json.loads(Path(right).read_text())
    a.pop('response02_comparison_to_response01', None)
    b.pop('response02_comparison_to_response01', None)
    a, b = flatten(a), flatten(b)
    assert a.keys() == b.keys()
    keys = sorted(a.keys() - set(masks))
    unequal = [k for k in keys if type(a[k]) is not type(b[k]) or a[k] != b[k]]
    assert not unequal, unequal
    return {'left': str(left), 'left_pin': pin(left), 'right': str(right),
            'right_pin': pin(right), 'leaf_count': len(a),
            'compared_leaves': len(keys),
            'numeric_leaves': sum(type(a[k]) in (int, float) for k in keys),
            'masked': {k: [a[k], b[k]] for k in masks}, 'unequal': unequal,
            'tolerance': 0, 'pass': True}


def clip(poly, a, b, c):
    """Exact polygon intersection with a*x+b*y <= c."""
    out = []
    for p, q in zip(poly, poly[1:] + poly[:1]):
        fp, fq = a*p[0]+b*p[1]-c, a*q[0]+b*q[1]-c
        if fp <= 0:
            out.append(p)
        if (fp < 0 < fq) or (fq < 0 < fp):
            t = fp/(fp-fq)
            out.append(tuple(p[i]+t*(q[i]-p[i]) for i in range(2)))
    return out


def triangle_density(x, y):
    poly = [(F(-1), F(-1)), (F(1), F(-1)), (F(-1), F(1))]
    # p in T and 2z-p in T. Since area(T)=2, the Jacobian 4 cancels area(T)^2.
    for a, b, c in [(1, 0, 2*x+1), (0, 1, 2*y+1), (-1, -1, -2*(x+y))]:
        poly = clip(poly, a, b, c)
    return abs(sum(p[0]*q[1]-p[1]*q[0]
                   for p, q in zip(poly, poly[1:]+poly[:1])))/2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--rerun', required=True)
    ap.add_argument('--numpy235', required=True)
    ap.add_argument('--numpy241', required=True)
    ap.add_argument('--output', required=True)
    args = ap.parse_args()
    old = TOPIC/'evidence/response-01-e6-offsample.json'
    new = TOPIC/'evidence/response-02-e6-offsample-rerun.json'
    masks = ['/command', '/python', '/elapsed_seconds']
    result = {'status': 'PASS', 'audit': 'E6 audit-03',
              'candidate': CANDIDATE, 'rules_head': RULES_HEAD,
              'executed_at_utc': datetime.now(timezone.utc).isoformat(),
              'checker_python': platform.python_version(),
              'comparisons': [compare(old, new, masks+['/code_sha256/e6_offsample.py']),
                              compare(new, args.rerun, masks),
                              compare(old, args.rerun, masks+['/code_sha256/e6_offsample.py'])]}
    script = 'tracks/bivariate-lanczos/code/drift/e6_offsample.py'
    before = ast.parse(subprocess.check_output(['git', '-C', str(ROOT), 'show', BEFORE+':'+script]))
    after = ast.parse((ROOT/script).read_text())
    assert isinstance(before.body[0], ast.Expr) and isinstance(after.body[0], ast.Expr)
    before.body = before.body[1:]
    after.body = after.body[1:]
    assert ast.dump(before) == ast.dump(after)
    result['offsample_executable_ast_unchanged'] = True
    result['numpy_probes'] = [json.loads(Path(p).read_text()) for p in [args.numpy235, args.numpy241]]
    assert result['numpy_probes'][0]['numpy'] == '2.3.5'
    assert result['numpy_probes'][0]['result'] == 'PASS'
    assert result['numpy_probes'][1]['numpy'] == '2.4.1'
    assert result['numpy_probes'][1]['result'] == 'FAIL'
    assert result['numpy_probes'][1]['exception_type'] == 'TypeError'
    assert 'arnoldi.py\", line 12' in result['numpy_probes'][1]['traceback']
    result['midpoint_exact_geometry'] = []
    for t in [F(1,16), F(1,8), F(1,4), F(1,3), F(1,2)]:
        density = triangle_density(-1+t, -1+t)
        assert density == 4*t*t
        result['midpoint_exact_geometry'].append({'t': str(t), 'area': str(density), 'pass': True})
    # The all-z density and its normalization are derived analytically in E6.md.
    result['upstream_head'] = subprocess.check_output(['git', '-C', str(EXTERNAL), 'rev-parse', 'HEAD'], text=True).strip()
    assert result['upstream_head'] == '6903d7af9995c9d88e661fb229626696e00fdfba'
    result['upstream_status'] = subprocess.check_output(['git', '-C', str(EXTERNAL), 'status', '--porcelain'], text=True)
    assert result['upstream_status'] == ''
    result['upstream_pins'] = {f: pin(EXTERNAL/'polyrat'/f) for f in ['arnoldi.py', 'index.py', 'basis.py', 'version.py']}
    names = ['AGENTS.md', 'agents/WORKFLOW.md', 'agents/codex/CODEX.md',
             'state/IDEAS.md', 'literature/INDEX.md', script,
             'tracks/bivariate-lanczos/code/drift/e6_offsample_compare.py',
             'tracks/bivariate-lanczos/code/drift/e6_benchmark.py',
             'tracks/bivariate-lanczos/code/drift/e6_smooth.py',
             'tracks/bivariate-lanczos/code/drift/README.md',
             'tracks/bivariate-lanczos/theory/drift-codex-e6-50-public-va-drift-measured.md',
             'topics/padua-lanczos-drift-20261101/ideas-e6.md',
             'topics/padua-lanczos-drift-20261101/directions/E6.md',
             'topics/padua-lanczos-drift-20261101/external-code.md',
             'topics/padua-lanczos-drift-20261101/checks/audit-02/E6/check.py']
    result['candidate_pins'] = {}
    for name in names:
        raw = subprocess.check_output(['git', '-C', str(ROOT), 'show', CANDIDATE+':'+name])
        item = pin(ROOT/name)
        item['candidate_sha256'] = hashlib.sha256(raw).hexdigest()
        assert item['sha256'] == item['candidate_sha256']
        result['candidate_pins'][name] = item
    result['checker_pin'] = pin(__file__)
    Path(args.output).write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'counts': [c['compared_leaves'] for c in result['comparisons']],
                      'numeric': [c['numeric_leaves'] for c in result['comparisons']], 'output_pin': pin(args.output)}))


if __name__ == '__main__':
    main()
