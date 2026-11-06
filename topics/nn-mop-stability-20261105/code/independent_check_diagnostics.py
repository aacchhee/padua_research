#!/usr/bin/env python3
"""Supplementary path-information traps and exact dictionary reconstruction."""
from fractions import Fraction as Q
import copy
import hashlib
import json
from pathlib import Path
import platform
import mpmath as mp
from independent_check_moments import direct, inputs, inverse, module

HERE = Path(__file__).resolve().parent


def path_trap():
    helper = module('independent_path',HERE/'path_recovery.py')
    N = 4
    x,w = inputs(N,'krawtchouk')
    c,_ = direct(x,w,False)
    with mp.workdps(100):
        convert = lambda a: mp.mpf(a.numerator)/a.denominator
        cf = {nu:{f:convert(a) for f,a in r.items()} for nu,r in c.items()}
        xx = list(map(convert,x))
        ww = [list(map(convert,r)) for r in w]
        plain = helper.recover(cf,N,xx,ww,100)
        changed = copy.deepcopy(cf)
        # Site (0,3) is entirely absent from the first-e1 alternating path.
        changed[0,3]['b1'] += 1
        hidden = helper.recover(changed,N,xx,ww,100)
        assert hidden == plain
        assert changed[0,3]['b1'] != changed[0,3]['b2']
        # b2_00 enters solely through the second-functional anchor d0.
        anchor = copy.deepcopy(cf)
        anchor[0,0]['b2'] += mp.mpf('0.01')
        oldd = cf[0,0]['b2']-cf[0,0]['b1']
        newd = anchor[0,0]['b2']-anchor[0,0]['b1']
        # Preserve the step-line gamma2 and delta2 while changing d0.
        anchor[1,1]['a1'] = cf[1,1]['a1']*oldd/newd
        anchor[1,1]['a2'] = cf[1,1]['a1']+cf[1,1]['a2']-anchor[1,1]['a1']
        moved = helper.recover(anchor,N,xx,ww,100)
        assert abs(moved['node_relative_sup']-plain['node_relative_sup']) < 1e-90
        assert moved['normalized_weight_relative_sup'] > .001
        return dict(exact_truth_path=plain,off_path_diagnostic_identical=True,
                    off_path_terminal_identity_violated=True,
                    anchor_changes_weights_not_nodes=True,anchor_result=moved)


def dictionary():
    x = list(map(Q,range(4)))
    w = [list(map(Q,(1,1,1,1))),list(map(Q,(1,2,4,8)))]
    A = [[sum(row),sum(a*b for a,b in zip(row,x))] for row in w]
    rhs = [-sum(a*b*b for a,b in zip(row,x)) for row in w]
    c = [sum(a*b for a,b in zip(row,rhs)) for row in inverse(A)]
    vals = [t*t+c[1]*t+c[0] for t in x]
    assert c == [Q(32,23),Q(-75,23)]
    assert sum(vals) == sum(a*b for a,b in zip(vals,w[1])) == 0
    assert sum(a*b for a,b in zip(vals,x)) == Q(-30,23)
    assert all(y*y-y == 0 for y in (Q(0),Q(1)))
    return dict(coefficients=list(map(str,c)),missing_x_moment='-30/23',
                selector_identity=True,two_sheet_annihilator=True)


if __name__=='__main__':
    paths = [Path(__file__),HERE/'independent_check_moments.py',HERE/'path_recovery.py']
    hashes = {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    out = dict(python=platform.python_version(),mpmath=mp.__version__,
               source_sha256=hashes,path=path_trap(),dictionary=dictionary(),
               scope='exact dictionary algebra; measured spectral path trap at N4 Krawtchouk')
    assert hashes == {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    print(json.dumps(out,indent=2,sort_keys=True,allow_nan=False))
