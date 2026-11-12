# PD-N?padua-3d-20261106-codex-T8-r06-03 — even subgroup unions retain the trace obstruction

ID kind: PD-N. Aliases: common half-period union action; U2/U3 degree-six
failure. Split from: none. Split into: none.

## Statement

Let H=<z/M> have even order M, let a_1,...,a_r be arbitrary real phases,
and suppose the cosine images of their r full cosets form exactly rM=N
distinct nodes, where N=binom(n+3,3). Write t for the number of odd
coordinates of z. For n>=1, Pi_n-unisolvence requires n odd and t=2.
In particular at n6,N84 every 2-coset common cyclic order42 union and
every 3-coset common cyclic order28 union satisfying the no-fold count
fails Pi_6 injectivity, for all phases and all generators. The examples
selected by U2/U3 have exactly rank82, by the written upper bound and
their finite-field rank82 certificates.

## Assumptions, definitions and status

Overall status **PROVED** for the all-phase obstruction, by the analytic
argument below. The rank82 equalities have exact certificates but remain
**MEASURED** until independent rerun. Candidate dispositions: U2 and U3
as all-degrees-in-their-frozen-domain constructions REJECTED: failed
already at n6; their separate later D2 kills remain measured outcomes.
No rejection of general unions, different subgroup orders, folding, or
degree sequences that omit n6. U4 at n6 uses odd M21 and is not excluded.

## Negative scope and proof

The full rM distinct-node hypothesis makes (coset label,k) a bijective
parameterization. On every coset k->k+M/2 has the same physical sign
action R(x)_j=(-1)^z_j x_j, regardless of phase. It is free on the
whole union. At least one coordinate is odd because H has order M.
Thus the nodal trace is zero and the polynomial trace is D_t(n) from
PD-T?padua-3d-20261106-codex-T8-r06-01. Its complete formulas show
that equality is possible only for odd n,t2. More precisely rank is
at most N-|D_t(n)|/2, by summing the minima of the plus and minus
eigenspace dimensions. At n6,t2, D_2(6)=4 and rank<=82.
The two selected generators have t2, while the receipts show rank82
modulo two verified splitting primes, giving a matching exact lower bound.

## D3, sources, checks and limitations

The general trace argument admits 2D Padua, whose folded nodal involution
has fixed points matching its polynomial trace. The free no-fold rM count
is the hypothesis that differs here. All eight sign patterns are covered
analytically; there is no unenumerated phase class in this obstruction.
Checker/source: code/t8_r06_routes.py; evidence/t8-r06-union2.json and
union3.json, n6 rows. No external theorem is a proof dependency. Independent
rerun of the new finite rank equalities remains required.

Broader cyclic unions and arbitrary finite-group unions remain OPEN;
the common even-order/no-fold assumptions are essential. 2026-11-06,
Codex assigned gpt-6.1-sol xhigh, rules 7afa6a54, after the frozen U2/U3/U4
quality runs. This explains their finite degree-six deficiency without
replacing a modular lower bound by an unsupported exact upper bound.
