# T4 numerical preregistration — before T4 execution

2026-11-06; rules `ccd9e905d19c0c625c196c4a3f3e707058ed042a`.

For every n>=1 use Pad_m={(cos(i*pi/m),cos(j*pi/(m+1))):i+j even},
m=n-k on plane k=0..n. Pad_0={(1,1)}. Heights permute h_j=cos(j*pi/n).
The three registered orderings are:

1. M: monotone indices 0,1,...,n. Ascending is a cube-reflection equivalent
   and is not a separate tested family.
2. A: alternating extremes 0,n,1,n-1,2,n-2,..., stopping without repetition.
3. L: greedy discrete-Leja indices, starting at0, then maximizing
   product_{previous i}|h_j-h_i| over unused j; ties choose smallest index.
   Family code uses high precision for the greedy comparison and records the
   permutation. The all-n theorem works for every permutation, so no floating
   ordering comparison is a proof dependency.

Primary degrees are1..12. Evaluate degree by degree and stop a family at
D2 KILL: sampled value above the inherited Leja lower-set value at two
consecutive n>=6. Any extension through n20 requires survival of this screen
and a separately recorded resource decision, never a retrospective pass.

Mesh: the identical21^3 tensor Chebyshev-Lobatto mesh from c3_lebesgue.py.
Basis: inherited total-degree product Chebyshev ordering. Controls at each
executed degree: the exact inherited discrete-Leja lower-set construction and
pivoted-QR approximate Fekete extraction from the (2n+1)^3 Lobatto cube mesh.
The latter is the inherited tensor-mesh reference, not a claim about the
literature's Lissajous-specific extraction.

Record node counts, condition2, singular extrema, numerical rank threshold
1e-12, sampled maximum and location, solve residual against V^T C=E^T and
nodal cardinality residual. If condition2>=1e12, suppress the ordinary double
value and label the solve unreliable; analytic unisolvence remains separate.
Use finite residual diagnostics to flag accuracy, not prove a Lebesgue bound.
Evaluate the analytic Newton recursion separately at small degrees and compare
its cardinals with direct solves before relying on implementation agreement.

Promising requires all D2 original conjuncts. If an ordering survives to20,
fit log Lambda = log C + k log log(n+1), k in{3,4}, and
log Lambda=log C+alpha log(n+1), alpha>=1, on every available n>=4,
using least-squares SSE on logarithms; lower SSE wins (tie inconclusive).
A family killed early gets no growth-model verdict. Analytic all-n
unisolvence can replace redundant finite rank certification for this baseline,
but does not waive either measured comparison conjunct or establish quality.

Limits: all sampled values/conditioning/fits are MEASURED; no continuous
upper bound or asymptotic law follows from them. No seeds are used. Store
small receipts under evidence/t4-*.json; large arrays under the supplied
/tmp/padua-3d-20261106/ location. Primary command will be recorded in its
receipt. Independent replay/audit is pending.
