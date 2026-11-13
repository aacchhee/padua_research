"""Consistency only: relate my integer-scaled det to the developer's reported residue 318086 mod 1000037."""
import sys, json
sys.path.insert(0, sys.argv[2])
import b2_exact as B
d = json.load(open(sys.argv[1]))
by = B.b85dec(d["coordinates_base85"])
pts = [tuple(B.f64(by[24*i+8*j:24*i+8*j+8]) for j in range(3)) for i in range(455)]
exps = [(a, b, c) for a in range(13) for b in range(13) for c in range(13) if a+b+c <= 12]
rows = []; S = 0
for p in pts:
    k = max(q.denominator.bit_length()-1 for q in p); D = 1 << k; S += 12*k
    n = [q.numerator*(D//q.denominator) for q in p]
    rows.append([n[0]**a*n[1]**b*n[2]**c*D**(12-a-b-c) for a, b, c in exps])
p = 1000037
dm, rk = B.det_mod(rows, p)
unscaled = dm*pow(pow(2, S, p), p-2, p) % p
print({"p": p, "scaled_det": dm, "sum_scale_exp": S, "implied_unscaled_det": unscaled, "developer_reported": 318086, "match": unscaled == 318086})
