#!/usr/bin/env python3
"""Check the final sign quadratic form by an explicit normal projection.

This independently formulates the final projection calculation, but trusts
the recorded target capacities. Recomputing them requires the multinode
generator. This developer check is not an independent-agent rerun.
"""
import argparse
import contextlib
import hashlib
import io
import json
from pathlib import Path
from e1_exact import Q, Mat, build, dot, points


def check(path):
    record=json.loads(Path(path).read_text())
    with contextlib.redirect_stdout(io.StringIO()):
        _,b,d,_,_=build(points(record['set']),record['degree'],record['rule'])
    capacity=list(map(Q,record['target_capacity_exact']));signs=record['node_signs'];target=record['target_column']
    v=Mat([[c*s for c,s in zip(capacity,signs)]])
    normal=v
    for q,dq in zip(b,d):normal=normal-dot(v,q)/dq*q
    explicit=dot(normal,normal)/d[target]
    diagonal=Q(0)
    for i,c in enumerate(capacity):
        Rii=1-sum((q[0,i]**2/dq for q,dq in zip(b,d)),Q(0))
        diagonal+=Rii*c*c/d[target]
    assert explicit==Q(record['explicit_greedy_sign_lower_squared']['exact'])
    assert diagonal==Q(record['expected_random_sign_lower_squared']['exact'])
    assert explicit>=diagonal
    assert set(signs)<={-1,1}
    return {'set':record['set'],'degree':record['degree'],'rule':record['rule'],'result':'PASS','checks':['explicit final normal projection squared norm','random-sign diagonal expectation','explicit>=expected','all node signs unit magnitude'],'trust_limit':'Target capacities are trusted input to this checker; independent generator rerun needed to check source propagation.','input_sha256':hashlib.sha256(Path(path).read_bytes()).hexdigest()}


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',required=True);a=p.parse_args();r=check(a.input)
    Path(a.output).write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
