"""Check the post-run guard-only edit against preserved executed Git blobs."""
import ast
import hashlib
import json
from pathlib import Path
import subprocess
import sys


def main():
    root = Path(__file__).resolve().parents[1]
    source = root / 'evidence/t1-optimization-guard-delta.json'
    proposal = json.loads(source.read_text())
    sha = lambda b: hashlib.sha256(b).hexdigest()
    results = []
    for entry in proposal['changes']:
        path = Path(entry['path'])
        old = Path(entry['preserved_byte_blob']).read_bytes()
        new = path.read_bytes()
        git = subprocess.check_output(['git', 'cat-file', 'blob', entry['old_git_blob']])
        assert old == git
        assert sha(old) == entry['executed_before_sha256']
        assert sha(new) == entry['after_sha256']
        old_ast, new_ast = ast.parse(old), ast.parse(new)
        index = 1 if isinstance(new_ast.body[0], ast.Expr) and isinstance(new_ast.body[0].value, ast.Constant) and isinstance(new_ast.body[0].value.value, str) else 0
        guard = new_ast.body.pop(index)
        expected = ast.parse("if not __debug__:\n    raise RuntimeError('T1 refuses optimized Python: " + path.name + "')\n").body[0]
        assert ast.dump(guard, include_attributes=False) == ast.dump(expected, include_attributes=False)
        assert ast.dump(new_ast, include_attributes=False) == ast.dump(old_ast, include_attributes=False)
        # Stronger textual check: deleting exactly the added statement restores every byte.
        lines = new.splitlines(keepends=True)
        assert b''.join(lines[:guard.lineno-1] + lines[guard.end_lineno:]) == old
        refusals = []
        for flag in ('-O', '-OO'):
            done = subprocess.run([sys.executable, '-B', flag, str(path)], capture_output=True, text=True, timeout=20)
            assert done.returncode == 1
            assert 'RuntimeError: T1 refuses optimized Python: ' + path.name in done.stderr
            refusals.append(dict(flag=flag, exit_code=done.returncode))
        assert path.read_bytes() == new
        results.append(dict(path=str(path), old_sha256=sha(old), new_sha256=sha(new), old_git_blob=entry['old_git_blob'], exact_guard_only_bytes=True, original_ast_unchanged=True, optimization_refusals=refusals))
    result = dict(all_controls_passed=True, count_certified=False, scope='guard-only source delta and actual pre-import optimized-mode refusals; no mathematical replay', control_sha256=sha(Path(__file__).read_bytes()), development_delta_sha256=sha(source.read_bytes()), changes=results)
    output = root / 'evidence/t1-independent-optimization-guard-controls.json'
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
