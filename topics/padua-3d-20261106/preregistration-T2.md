# T2 preregistration — immutable first screen

2026-11-06; written before first T2 mechanism run. D0/D1 PASS inherited from evidence/replay.json. Rules SHA ccd9e905d19c0c625c196c4a3f3e707058ed042a.

Let N=binom(n+3,3), M=2N-1 and k=0,...,N-1. Nodes are x_k=(cos(2πkz1/M),cos(2πkz2/M),cos(2πkz3/M)). Frozen families, admissible all integers n≥1:

- K: z=(1,n+1,(n+1)^2).
- T: z=(1,n+1,(n+1)(n+2)/2).
- O: z=(1,2n+1,2n^2+2n+1).

No generator search or adjustment after outcomes. Ascending n=1,...,12 for exact dictionary ranks; stop each family at first certified deficiency. Optional n=13,...,20 only for families surviving12, conditional on feasible dense cost; report truncation. Rational nullvector is required to certify deficiency; a zero modular determinant alone is insufficient. Positive witnesses use integer dictionary determinant mod p=1000003, with one direct root-of-unity check at p odd and p≡1 mod M for each tested n≤4. Root order verified by all prime divisors of M. This certifies the actual Chebyshev specialization.

Exact node count comes first: first-coordinate monotonicity on 0≤2πk/M<π proves all N nodes distinct. Integer residues also explicitly checked. Basis: products T_a(x)T_b(y)T_c(z), a+b+c≤n. Dictionary reduction written separately before interpreting rank.

Quality: inherited c3_lebesgue.py imported immutable, 21^3 tensor Chebyshev–Lobatto mesh (21 points per axis including endpoints). Same-degree controls: discrete-Leja ordering of n+1 Lobatto axis, total-degree lower set; QR approximate Fekete from (2n+1)^3 tensor Lobatto candidates, pivoted QR of transposed product-Chebyshev evaluation. Use inherited condition<10^12 guard. Mesh maxima are MEASURED sampled values, no true maximum certification.

D2 kill unchanged: certified deficiency at any admissible n; or sampled value above Leja at two consecutive n≥6. Stop fixed family at kill. Promising requires exact unisolvence at every tested admissible n≤12 (or explicit feasible cutoff), sampled value below QR at every tested n≥4, and fit preference below. A bounded survivor is not an infinite-degree theorem.

Fits only if ≥4 quality degrees n≥4 survive: log(response)=log C+k log(log n), k∈{1,2,3,4}, versus log(response)=log C+α log n, α≥1. Fit intercept separately by least squares, optimize α constrained≥1; compare log-scale SSE, choose polylog only if its SSE is strictly smaller than best polynomial SSE. Equal SSE is INCONCLUSIVE. Record all models. With fewer than4 degrees, fit INCONCLUSIVE, no fitting to killed-family prefixes to rescue them. All bounded n≤20 fits are diagnostics only, never asymptotic evidence.

Compute bound: three explicit formulas, no unbounded parameter search. Evidence compact<16KiB, large scratch only /tmp/padua-3d-20261106/. Independent replay required before any finite computer-assisted PROVED rank verdict.

## Round 2 preregistration — exhaustive normalized generator screen

2026-11-06, after round1 fixed K/T/O kills; before any exhaustive run.
For each n=2,3,4, N=binom(n+3,3), M=2N-1, enumerate every integer generator z=(1,b,c) with 1≤b<c≤N-1. There are respectively36,171,561 rows, including b=1 (repeated first generator) and excluding c=b. Equal b=c gives identical y,z and immediate linear deficiency; signs of b,c are equivalent under cosine, and interchange of b,c is a cube symmetry. The slice z1=1 is explicit: not every generator can be normalized to1 if no coordinate is a unit modulo M. Even with a unit coordinate, multiplying the parameter by its inverse gives a group reparameterization and thus identical full folded node set. This is a finite degree screen, no all-n conclusion.

Compute integer dictionary as above, modular rank at1000003, then rational RREF for every deficient modular matrix; save exact rational rank and primitive integer nullvector, checking Dv=0. For full modular rank, integer determinant is nonzero and no rational RREF needed. Report each degree's rank distribution, maximum rank, number fullrank, and first fullrank generator in lex order. Large per-generator witness catalogue only in /tmp/padua-3d-20261106/; compact summary and hashes committed. First-generator normalization still guarantees exact N nodes before rank or quality. No Lebesgue runs in the exhaustive stage. This is class diagnosis after killed fixed families, not a continuation of them.

If any fullrank generators survive at the largest screened degree, preregister the prospective rule separately before larger-degree evaluation; default lex-first fullrank is a candidate rule, not an outcome-dependent formula silently frozen here. No prose hash is an acceptance dependency; code/data hashes identify computation. Independent replay remains required.

## Round2b preregistration — finite survivor quality

Before quality runs: evaluate every modular-fullrank generator from the complete n2,n4 screen: n2 (1,3,7),(1,4,6),(1,5,8),(1,7,8); n4 (1,11,15),(1,15,19),(1,21,29),(1,25,30). Same inherited21³ mesh/evaluator and same-degree QR/Leja controls. Select finite best by minimum measured mesh value, ties lexicographic. This selects a finite representative only, not a rule for higher degrees. These two degrees supply fewer than4 n≥4 observations, so growth fit INCONCLUSIVE. Direct root-of-unity rank checks for all8, with order and good prime data, independent of dictionary prime. No D2 PASS possible at this stage.
