"""Second, independent code path for the record -06 lattice witnesses, plus compact evidence.

Reads the full output of pdn_lattice_witness.py. For each n and each exactness tag
(E = 2n-2, 2n-1) with a witness basis A (integer, columns = basis vectors) it checks:
  (1) index: |det A| equals the reported index (exact integers);
  (2) avoidance: no nonzero k in Z^3 with |k|_1 <= E lies in A Z^3.
Membership test: k in A Z^3  <=>  adj(A) k = 0 (mod det A), exact int64 arithmetic
(|entries| stay far below 2^63 in the tested range; asserted).  The l1 ball is
enumerated directly, slice by slice in k_1 (no coefficient-box bound is used, so this
is independent of the witness search's exhaustiveness argument).
Writes compact evidence: rows [n, 8P, index_E2n-1, covered, basis(9 ints, row-major
of A), index_E2n-2, covered] and the list of n checked.

Usage: python3 -B pdn_check_ball.py --full witness-final.json --out evidence/pdn-lattice-witness.json
"""
import argparse, hashlib, json, sys
import numpy as np


def det3(A):
    return (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
        - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
        + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))


def adj3(A):
    C = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            m = [[A[r][c] for c in range(3) if c != j] for r in range(3) if r != i]
            C[j][i] = (-1) ** (i + j) * (m[0][0] * m[1][1] - m[0][1] * m[1][0])
    return C


def avoids(A, E):
    d = det3(A)
    adj = np.array(adj3(A), dtype=np.int64)
    assert int(np.abs(adj).max()) * 3 * E < 2 ** 62
    for k1 in range(-E, E + 1):
        r = E - abs(k1)
        k2 = np.arange(-r, r + 1)
        rows = []
        for v in k2:
            rr = r - abs(int(v))
            k3 = np.arange(-rr, rr + 1)
            rows.append(np.stack([np.full_like(k3, k1), np.full_like(k3, v), k3], axis=1))
        K = np.concatenate(rows).astype(np.int64)
        R = (K @ adj.T) % abs(d)
        hit = np.all(R == 0, axis=1) & np.any(K != 0, axis=1)
        if hit.any():
            return False
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--full", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    full = json.load(open(a.full))
    rows, bad = [], []
    for r in full["rows"]:
        n = r["n"]
        out = [n, r["8P"]]
        for tag, E in (("E=2n-1", 2 * n - 1), ("E=2n-2", 2 * n - 2)):
            w = r[tag]
            A = w["basis_columns"]
            ok = abs(det3(A)) == w["index"] and avoids(A, E)
            if not ok:
                bad.append([n, tag])
            if tag == "E=2n-1":
                out += [w["index"], bool(w["covered"] and ok), [x for row in A for x in row]]
            else:
                out += [w["index"], bool(w["covered"] and ok)]
        rows.append(out)
        print(n, out[2], out[3], out[5], out[6], flush=True)
    cov1 = [x[0] for x in rows if x[3]]
    cov2 = [x[0] for x in rows if x[6]]
    res = {"checker": "pdn_check_ball.py (direct l1-ball enumeration, adjugate membership)",
           "checker_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
           "search_script_sha256": full["script_sha256"],
           "search_full_output_sha256": hashlib.sha256(open(a.full, "rb").read()).hexdigest(),
           "python": sys.version.split()[0], "numpy": np.__version__,
           "columns": ["n", "8*binom(n+3,3)", "index (min l1 >= 2n)", "covered E=2n-1",
                       "basis A row-major (columns = basis vectors)", "index (min l1 >= 2n-1)", "covered E=2n-2"],
           "check_failures": bad, "covered_E2n-1": cov1, "covered_E2n-2": cov2, "rows": rows}
    s = json.dumps(res, separators=(",", ":"))
    open(a.out, "w").write(s)
    print("bytes", len(s), "failures", bad)


if __name__ == "__main__":
    main()
