"""Execute a committed control harness unchanged except that its single receipt write
is redirected outside the repository (auditor wrapper; no repo file is modified)."""
import sys, runpy
src_path, old_rel, new_path = sys.argv[1], sys.argv[2], sys.argv[3]
src = open(src_path).read()
target = "(p/'outputs/part3/%s')" % old_rel
assert src.count(target) == 1, "unexpected write target"
src = src.replace(target, "(__import__('pathlib').Path(%r))" % new_path)
sys.dont_write_bytecode = True
code = compile(src, src_path, "exec")
g = {"__file__": src_path, "__name__": "__main__"}
exec(code, g)
