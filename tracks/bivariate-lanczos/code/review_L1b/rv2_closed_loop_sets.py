"""dot64 closed-loop mode of rv2_closed_loop.py on the six IDEA?...-120 checkerboards (convention-free verdict).
Usage: python3 -I -u rv2_closed_loop_sets.py > logs_L1b/closed_loop_sets.log"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'review_L1'))
import numpy as np
import rv_core as C
import rv2_checkerboard as CB
import rv2_open_loop            # installs the extended abscissae families into rv2_checkerboard
from rv2_closed_loop import bj_mode
ld = np.longdouble
degs = (12, 16, 20, 24)
print('# rv2_closed_loop_sets.py: C(n) = loss with only the window dot products in IEEE double (rest long double); L(n) = double BJ')
for fam, m in (('cubic', 30), ('equi', 30), ('quad', 30), ('quart', 30), ('cubic', 36), ('lobatto', 30)):
    if fam == 'equi':
        CB.abscissae = lambda f, n: np.linspace(-1, 1, n, dtype=ld)
    else:
        CB.abscissae = rv2_open_loop.abscissae
    P, w, _, _ = CB.checkerboard(fam, m)
    Qd, _ = C.window_rec(P[:, 0].astype(float), P[:, 1].astype(float), w.astype(float), 24, 'dev', 'block', 'cgs')
    L = [CB.gram_defect(Qd.astype(ld), n) for n in degs]
    Cn = [CB.gram_defect(bj_mode(P, w, 24, 'dot64'), n) for n in degs]
    print(f'{fam:7s} m={m}: L = ' + ' '.join(f'{v:.1e}' for v in L) + ' | C = ' + ' '.join(f'{v:.1e}' for v in Cn)
          + ' | C/L = ' + ' '.join(f'{c / l:.2f}' for c, l in zip(Cn, L)))
    sys.stdout.flush()
