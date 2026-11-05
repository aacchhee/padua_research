"""Independent final boundary producer guard-only source review controls."""
import ast
import hashlib
import json
from pathlib import Path
import subprocess
import sys


def main():
    topic = Path(__file__).resolve().parents[1]
    change = topic / 'evidence/t1-boundary-optimization-guard-delta.json'
    proposal = json.loads(change.read_text())
    path = topic / 'code/t1_boundary.py'
    old = Path(proposal['old_source_copy']).read_bytes()
    new = path.read_bytes()
    sha = lambda b: hashlib.sha256(b).hexdigest()
    assert old == subprocess.check_output(['git', 'cat-file', 'blob', proposal['old_git_blob']])
    assert sha(old) == proposal['old_sha256']
    assert sha(new) == proposal['new_sha256']
    tree = ast.parse(new)
    guard = tree.body.pop(1)
    expected = ast.parse("if not __debug__:\n    raise RuntimeError('T1 boundary producer refuses optimized Python')\n").body[0]
    assert ast.dump(guard, include_attributes=False) == ast.dump(expected, include_attributes=False)
    assert ast.dump(tree, include_attributes=False) == ast.dump(ast.parse(old), include_attributes=False)
    lines = new.splitlines(keepends=True)
    assert b''.join(lines[:guard.lineno-1] + lines[guard.end_lineno:]) == old
    cases = []
    for flag in ('-O', '-OO'):
        result = subprocess.run([sys.executable, '-B', flag, str(path)], capture_output=True, text=True, timeout=20)
        assert result.returncode == 1
        assert 'RuntimeError: T1 boundary producer refuses optimized Python' in result.stderr
        cases.append(dict(flag=flag, exit_code=result.returncode, refused_before_imports=True))
    assert path.read_bytes() == new
    output = dict(all_controls_passed=True, count_certified=False,
                  scope='exact final guard-only byte/AST delta and pre-import optimized-mode refusals; executed scientific artifact keeps old source identity',
                  control_sha256=sha(Path(__file__).read_bytes()), development_delta_sha256=sha(change.read_bytes()),
                  old_sha256=sha(old), new_sha256=sha(new), old_git_blob=proposal['old_git_blob'],
                  original_bytes_restored_by_removing_only_guard=True, original_ast_unchanged=True, controls=cases)
    destination = topic / 'evidence/t1-independent-boundary-guard-controls.json'
    destination.write_text(json.dumps(output, indent=2, sort_keys=True) + '\n')
    print(json.dumps(output, sort_keys=True))


if __name__ == '__main__':
    main()
