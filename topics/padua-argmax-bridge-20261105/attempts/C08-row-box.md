# C08 — whole-box row interface attempt

Rules 4b728b0; 2026-11-06. Own only C08 idea/attempt/theory records.
No Git, shared file, old source, review, backend or cover changes.

Prospective full novelty gate and exact candidate:
[ideas/C08-row-box.md](../ideas/C08-row-box.md). The full current IDEAS
registry, all obstruction tables and PR30 additions were freshly re-read.
Classification is a technical interval-integration variant of N2/C02/C06.

C06 owner confirms native `c06_partial_arb(n,q,y,out)` already encloses
the entire interval y when both strict pole-distance guards hold. Its
LP64 degree guard is n<=2147483647. C07 accepts exact rational phase
points only and is under development, not a whole-box backend.

No numerical test or implementation has been run. The proof will first
derive fixed integer cores, closed ambiguous bands and the actual
O(n+sum B_r) work scope, then state when this becomes O(n).

## Frozen analytic outcome

The contract is `theory/C08-row-box-contract.md`, SHA-256
`7c29e35b509cefcb9bb01f88a078ca46822221afce54c2a7bcd8d5de8565602f`.
The separate scoped limitation is `theory/C08-row-box-obstruction.md`,
SHA-256 `283eca3471dc74953af5ef246c84d38200dca6a554432e2bcd938c213b443256`.
Both are developer PROVED, distinct review PENDING. No executable or
arithmetic diagnostic was run; computational CPU charged is zero.

The complete box contract keeps fixed integer labels, excludes closed
root bands (including exact boundary coincidences), retains cuts even
when a root band contains no integer, and calls C06 with interval offsets
for every fixed core. It proves the actual work O(n+sum_r |B_r|), with
at most12 blocks/channel. The C07 point-only maxdirect5 guard cannot be
silently reused; a conservative box count is7+3floor(d_I).

Collision index bands have exact width
`(w_alpha+n*w_beta/m)/(2pi)<1`, independent of degree. Numerator bands
have width `n*Delta_asin/(2pi)+w_alpha/(2pi)`. Transverse-root and tangent
estimates yield the respective O(1/n) and O(1/n^2) sufficient phase-width
scales for bounded per-row direct work under uniform nondegeneracy.
Every tail, including C06's separate w' tail, is charged over all rows.
The four retained rows and all direct samples carry full primitive balls.

The obstruction uses actual phase boxes beta0, alpha in
`[3pi/4,3pi/4+w]`, with0<w<=pi/16. At least m/3-1 ordinary rows have
g=cot(alpha/2)(1+cos v) and each numerator root sweeps at least
floor(n*w/(8pi)) integer indices. Thus the defined direct-enumeration
route has an Omega(n^2*w) fixed-width cost. A one-row actual tangent
example separately verifies square-root motion and is explicitly NOT
used to infer a total quadratic lower bound.

This limitation concerns the swept-index enumeration route only.
Coefficient relaxation, convexity, aggregate uncertain-band bounds and
other whole-box algorithms are not rejected. Unresolved p0/closed-axis
branches either use a proved special branch, a charged row enumeration,
the proved coarse row cap, or return failure for subdivision. No point
result is promoted to a box enclosure, gradient, corner orbit or defect.
