"""Audit wrapper: run unchanged T8 producers from an isolated extracted copy,
rebinding only the raw scratch directory (SCRATCH) to the auditor's dir."""
import sys, json, time, importlib
from pathlib import Path
RUN = Path(sys.argv[1]); RAW = Path(sys.argv[2]); which = sys.argv[3:]
code = RUN / 'topics/padua-3d-20261106/code'
sys.path.insert(0, str(code))
import t8_cyclic as core
core.SCRATCH = RAW
assert core.TOP == RUN / 'topics/padua-3d-20261106'
for w in which:
    t = time.time()
    if w == 'controls': core.controls()
    elif w.startswith('census'): core.census(int(w[-1]))
    elif w.startswith('odd'): core.odd(int(w[-1]))
    elif w == 'phases':
        import t8_phases; t8_phases.main()
    elif w == 'even':
        import t8_even_family; t8_even_family.main()
    print('DONE', w, round(time.time() - t, 2), flush=True)
