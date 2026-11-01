#!/usr/bin/env python3
"""Exact rational frozen-recurrence normal-sensitivity bounds.

Requires python-flint (external dependency, not vendored). Every source block
is included by default; --sources degree2 is a restricted-input screen only.
Output intervals bound squared spectral-output operator norm, not equality.
"""
import argparse
import hashlib
import json
import math
import platform
import time
from pathlib import Path
import flint
from flint import fmpq as Q, fmpq_mat as Mat


def dot(a, b):
    return (a * b.transpose())[0, 0]


def multiply(a, x):
    return Mat([[a[0, i] * z for i, z in enumerate(x)]])


def sqrt_bounds(v, places=12):
    scale = 10 ** places
    h = math.isqrt((int(v.numerator) * scale * scale) // int(v.denominator))
    return [str(Q(h, scale)), str(Q(h + 1, scale))]


def scalar(v):
    return {"exact": str(v), "float": float(v), "sqrt_rational_interval": sqrt_bounds(v)}


def points(name):
    if name == "triangle":
        return [(Q(i, 12)-1, Q(j, 12)-1) for i in range(25) for j in range(25-i)]
    out = []
    for i in range(25):
        for j in range(25):
            x, y = Q(i, 12)-1, Q(j, 12)-1
            out.append(((3*x-4*y)/5, (4*x+3*y)/5))
    return out


def build(xy, degree, rule):
    coords = [[p[a] for p in xy] for a in (0, 1)]
    b = [Mat([[1]*len(xy)])]
    d = [Q(len(xy))]
    rec = [None]
    index = {(0, 0): 0}
    metadata = [(0, 0)]
    for t in range(1, degree+1):
        for j in range(t+1):
            candidates = []
            axes = [a for a in (0, 1) if (a == 0 and j<t) or (a == 1 and j>0)]
            if rule != "pivot":
                wanted = 0 if ((rule == "bj" and j == 0) or
                               (rule == "mirror" and j != t) or
                               (rule == "alt" and 2*j<t)) else 1
                axes = [wanted if wanted in axes else axes[0]]
            for a in axes:
                parent = index[(t-1, j-(a == 1))]
                u = multiply(b[parent], coords[a])
                sigma = dot(u, u)
                alpha = [dot(v, u)/dv for v, dv in zip(b, d)]
                residual = u
                for c, v in zip(alpha, b):
                    if c:
                        residual = residual-c*v
                dk = dot(residual, residual)
                if not dk or not sigma:
                    raise ArithmeticError("breakdown")
                candidates.append((dk/sigma, a, parent, alpha, sigma, residual, dk))
            # X wins exact ties. All comparisons are rational.
            chosen = max(candidates, key=lambda c: (c[0], -c[1]))
            _, a, parent, alpha, sigma, residual, dk = chosen
            index[(t, j)] = len(b)
            metadata.append((t, j))
            b.append(residual)
            d.append(dk)
            rec.append((a, parent, alpha, sigma))
        print(json.dumps({"event":"basis_degree", "degree":t,"rule":rule}), flush=True)
    return coords, b, d, rec, metadata


def bounds(xy, degree, rule, sources):
    start = time.monotonic()
    coords, b, d, rec, metadata = build(xy, degree, rule)
    M, N = len(xy), len(b)
    # Normal projector's diagonal, without constructing its dense matrix.
    normal = [1-sum((v[0,i]**2/dk for v,dk in zip(b,d)), Q(0)) for i in range(M)]
    if min(normal) < 0:
        raise ArithmeticError("negative normal projector diagonal")
    maximum, total, witness = Q(0), Q(0), None
    row_total = [Q(0)]*M
    selected = [j for j in range(1,N) if sources == "all" or metadata[j][0] == 2]
    for source in selected:
        g = [None]*N
        g[source] = Mat([[1]*M])
        energy = [Q(1)/d[source]]*M
        for k in range(source+1,N):
            axis, parent, alpha, _ = rec[k]
            v = multiply(g[parent],coords[axis]) if parent>=source else Mat(1,M)
            for l in range(source,k):
                if alpha[l]:
                    v = v-alpha[l]*g[l]
            g[k] = v
            for i in range(M):
                energy[i] += v[0,i]**2/d[k]
        sigma = rec[source][3]
        for i in range(M):
            row_total[i] += sigma*energy[i]
            term = sigma*normal[i]*energy[i]
            total += term
            if term>maximum:
                maximum, witness = term, {"source":source,"source_degree_index":metadata[source],"node":i,"point":[str(q) for q in xy[i]]}
        print(json.dumps({"event":"source", "source":source,"count":len(selected),"elapsed":time.monotonic()-start}),flush=True)
    return {"degree":degree,"rule":rule,"sources":sources,"source_count":len(selected),"point_count":M,"basis_count":N,"Knode_squared":scalar(maximum),"KHS_squared":scalar(total),"Urow_squared":scalar(max(row_total)),"upper_squared":scalar(min(total,max(row_total))),"witness":witness,"elapsed_seconds":time.monotonic()-start,"normal_trace_exact":str(sum(normal)),"expected_normal_trace":M-N,"pivot_choices":["XY"[r[0]] for r in rec[1:]],"basis_orthogonality":"exact full projection by construction; projector diagonal nonnegative checked"}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--set",choices=["triangle","rotated"],required=True)
    parser.add_argument("--degree",type=int,required=True)
    parser.add_argument("--rule",choices=["bj","mirror","alt","pivot"],required=True)
    parser.add_argument("--sources",choices=["all","degree2"],default="all")
    parser.add_argument("--output",required=True)
    args=parser.parse_args()
    if not 2<=args.degree<=12:
        parser.error("frozen scope is degree 2..12")
    result=bounds(points(args.set),args.degree,args.rule,args.sources)
    result.update({"set":args.set,"status":"MEASURED exact rational finite bounds; no automatic spectral verdict","python":platform.python_version(),"python_flint":flint.__version__,"code_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),"rules_base_sha":"806cc7b4509fd93bae652f9545d32d95529f8281","command":" ".join(__import__('sys').argv)})
    Path(args.output).write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"event":"complete","output":args.output,"elapsed":result["elapsed_seconds"]}),flush=True)


if __name__ == "__main__":
    main()
