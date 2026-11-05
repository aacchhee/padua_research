#!/usr/bin/env python3
"""Supplementary binary64 checks of N2-01; no fit or proof certificate."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import platform
import subprocess

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
TOPIC = Path(__file__).resolve().parents[1]


def direct_q(n: int, alpha: float, beta: float):
    m = n + 1
    js, rs = np.meshgrid(np.arange(2*n), np.arange(2*m), indexing="ij")
    odd = (js + rs) % 2 == 1
    j, r = js[odd], rs[odd]
    u, v = (j*math.pi+alpha)/n, (r*math.pi+beta)/m
    value = np.zeros_like(u)
    for a in range(n+1):
        for b in range(n+1-a):
            coefficient = (1 if a == 0 else 2) * (1 if b == 0 else 2)
            value += coefficient*np.cos(a*u)*np.cos(b*v)
    value -= np.cos(n*u)
    return j, r, u, v, ((-1.0)**j)*value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT/"local-output/argmax-bridge-20261105/N2/rows.json")
    parser.add_argument("--receipt", type=Path, default=TOPIC/"evidence/n2-rows.json")
    args = parser.parse_args()
    maxima = dict(row=0.0, global_signed=0.0, cotangent=0.0,
                  collision=0.0, absolute_rows=0.0, boundary=0.0,
                  vertex=0.0, crt=0.0)
    counts = dict(cases=0, generic_cases=0, collision_entries=0,
                  regular_entries=0, sign_disagreements=0,
                  boundary_cases=0, vertex_cases=0)
    records = []
    degrees = [2, 3, 4, 5, 8, 13, 16]
    for n in degrees:
        m, N = n+1, n*(n+1)
        phases = [(0.0, 0.0), (.17, .23), (.41, .07),
                  (0.0, .33), (.9, 1.2), (.2, 2.8)]
        for t in [.13, .5, .87]:
            for sa, sb in [(1,1),(-1,1),(1,-1),(-1,-1)]:
                phases.append((sa*math.pi*t, sb*math.pi*(1-t)))
        phases += [(math.pi,0),(-math.pi,0),(0,math.pi),(0,-math.pi)]
        # Construct both equal-angle and opposite-angle collisions. These
        # cases are evaluated with the direct finite polynomial, not a
        # quotient whose poles have been patched by numerical interpolation.
        beta = math.pi/7
        for epsilon in [1, -1]:
            candidates = []
            for r in range(2*m):
                v = (r*math.pi+beta)/m
                chosen_u = v if epsilon == 1 else 2*math.pi-v
                for j in range(2*n):
                    if (j+r) % 2 == 0:
                        continue
                    alpha = n*chosen_u-j*math.pi
                    if 0 < alpha < math.pi-beta:
                        candidates.append((alpha,beta))
            phases += candidates[:3]
        # Preserve insertion order and deduplicate literal numerical cases.
        phases = list(dict.fromkeys(phases))
        for alpha, beta in phases:
            j,r,u,v,Q = direct_q(n, alpha, beta)
            S = float(np.sum(np.abs(Q))/(2*N))
            signed_error = abs(float(np.sum(Q)/(2*N))-math.cos(alpha))
            maxima["global_signed"] = max(maxima["global_signed"], signed_error)
            counts["cases"] += 1
            row = dict(n=n,alpha=alpha,beta=beta,S=S,signed_error=signed_error)
            is_generic = alpha >= 0 and 0 < beta < math.pi and alpha+beta <= math.pi+1e-14
            if is_generic:
                counts["generic_cases"] += 1
                A,p,q = math.cos(alpha)+math.cos(beta), math.sin(alpha), math.sin(beta)
                collision = np.abs(np.cos(u)-np.cos(v)) < 2e-12
                reconstructed = 0.0
                for rr in range(2*m):
                    take = r == rr
                    vv = float(v[take][0])
                    uu, QQ = u[take],Q[take]
                    cc = collision[take]
                    cm = (p-q-A/math.tan(vv/2))/2
                    cp = (p+q+A/math.tan(vv/2))/2
                    expected_signed = n*(A-q/math.tan(vv/2))
                    maxima["row"] = max(maxima["row"],abs(float(np.sum(QQ))-expected_signed))
                    regular = ~cc
                    uq = uu[regular]
                    reconstructed_q = cm/np.tan((uq-vv)/2)+cp/np.tan((uq+vv)/2)
                    if len(uq):
                        maxima["cotangent"] = max(maxima["cotangent"],float(np.max(np.abs(reconstructed_q-QQ[regular]))))
                    W = A*(1+math.cos(vv))+q*math.sin(vv)
                    E = np.logical_xor(np.cos(uq)<math.cos(vv), W-p*np.sin(uq)<0)
                    significant = np.abs(QQ[regular])>2e-9
                    counts["sign_disagreements"] += int(np.count_nonzero((E != (QQ[regular]<0)) & significant))
                    counts["regular_entries"] += int(np.count_nonzero(regular))
                    collision_q = []
                    for uv, qv in zip(uu[cc],QQ[cc]):
                        epsilon = 1 if abs(math.sin(uv)-math.sin(vv))<1e-10 else -1
                        expected = (epsilon*n*p-m*q)/math.sin(vv)-math.cos(alpha)
                        maxima["collision"] = max(maxima["collision"],abs(float(qv)-expected))
                        collision_q.append(expected)
                        counts["collision_entries"] += 1
                    reconstructed += expected_signed-2*float(np.sum(reconstructed_q[E]))+2*sum(max(-x,0) for x in collision_q)
                maxima["absolute_rows"] = max(maxima["absolute_rows"],abs(reconstructed/(2*N)-S))
                # Check the odd-board CRT csc/cot identity away from its
                # individual singular factors, preserving their signs.
                k = (m*j+n*r) % (2*N)
                ss = (math.pi*k+m*alpha+n*beta)/(2*N)
                tt = (math.pi*(2*n+1)*k+m*alpha-n*beta)/(2*N)
                regular_crt = (np.abs(np.sin(ss))>1e-8) & (np.abs(np.sin(tt))>1e-8)
                sx,tx = ss[regular_crt],tt[regular_crt]
                crt = A/2*(1/(np.sin(sx)*np.sin(tx))-1/(np.tan(sx)*np.tan(tx))-1)
                crt += (p-q)/(2*np.tan(tx))+(p+q)/(2*np.tan(sx))
                if len(crt):
                    maxima["crt"] = max(maxima["crt"],float(np.max(np.abs(crt-Q[regular_crt]))))
            if abs(abs(alpha)+abs(beta)-math.pi)<1e-13:
                if min(abs(alpha),abs(beta))<1e-14:
                    maxima["vertex"] = max(maxima["vertex"],abs(S-1))
                    counts["vertex_cases"] += 1
                else:
                    t = abs(alpha)/math.pi
                    kk = np.arange(2*N)
                    expected = math.sin(math.pi*t)*float(np.sum(np.abs(1/np.tan(math.pi*(kk+t)/(2*N)))))/(2*N)
                    maxima["boundary"] = max(maxima["boundary"],abs(S-expected))
                    counts["boundary_cases"] += 1
            records.append(row)
    if counts["sign_disagreements"]:
        raise AssertionError(counts)
    if any(value>2e-7 for value in maxima.values()):
        raise AssertionError(maxima)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    payload = dict(status="MEASURED supplementary developer sanity check",degrees=degrees,
                   counts=counts,max_absolute_errors=maxima,records=records)
    args.output.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
    sources = [Path(__file__).resolve(), TOPIC/"theory/N2-row-decomposition.md",
               ROOT/"topics/padua-argmax-alln-20261101/theory/gated-codex-02-two-phase-global-bound.md",
               ROOT/"topics/padua-argmax-alln-20261101/theory/gated-codex-12-row-primitive-identity.md",
               ROOT/"topics/padua-argmax-effective-2-20261105/theory/profile-boundary-cotangent.md"]
    def identity(path):
        content = path.read_bytes()
        return dict(path=str(path.relative_to(ROOT)),bytes=len(content),sha256=hashlib.sha256(content).hexdigest())
    receipt = dict(status=payload["status"],command="python topics/padua-argmax-bridge-20261105/code/n2_rows.py",
                   input_head=subprocess.check_output(["git","rev-parse","HEAD"],cwd=ROOT,text=True).strip(),
                   python=platform.python_version(),numpy=np.__version__,degrees=degrees,
                   counts=counts,max_absolute_errors=maxima,sources=[identity(x) for x in sources],
                   raw=identity(args.output),independent_rerun="PENDING",fit="NONE",
                   limits="Binary64 checks only; no rigorous rounding bound, continuum claim, profile fit, B3 pass or proof dependency. Cold-storage archival pending.")
    args.receipt.write_text(json.dumps(receipt,indent=2,sort_keys=True)+"\n")
    print(json.dumps({k:receipt[k] for k in ["status","counts","max_absolute_errors","raw"]},indent=2))


if __name__ == "__main__":
    main()
