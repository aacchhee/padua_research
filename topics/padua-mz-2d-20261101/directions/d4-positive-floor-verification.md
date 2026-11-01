# D4 positive-floor application — verification-only archive

Record kind: **verification/application only; no new mathematical claim or
PD-N allocation**. Date: 2026-11-01. Codex `/root/d4_ratio`, requested
`gpt-6.1-sol` xhigh. No Git authority.

Canonical result: [PD-N?mz2d-codex-10, proof §3](../../../tracks/mz-constants/theory/mz2d-upper-sign-obstruction.md).
Application: [IDEA?mz2d-codex-41](../ideas-d4.md), the attempted positive
sample-energy conversion after the M3 Schur step.

Supplementary Astra's duplicate finding is accepted. The negative-weight
witness and arbitrary-data consequence below were already established in
D2's canonical N10 §3. Candidate 41 is retained as an **equivalent known
obstruction applied to D4**; the positive-floor transfer fails, but this
record is verification and application, not a second negative result.
Historical provisional **PD-N?mz2d-codex-41 maps to PD-N?mz2d-codex-10**.
Root owns the global crosswalk. No duplicate mechanism is pursued after
consolidation. Restricted-degree signed coercivity remains OPEN.

The root verified with `git ls-files --error-unmatch` that the actual
source file was untracked/uncommitted and authorized its removal after
preservation. Its exact path was
`tracks/mz-constants/theory/mz2d-fixed-ratio-energy-conversion-obstruction.md`,
not `mz2d-fixed-ratio-positive-obstruction.md`.

The original body follows **byte for byte**, with its historical heading
and status language preserved as provenance only. Those archived labels
do not allocate or reactivate a result. Exclude this frozen body from
provisional-ID replacement; resolve N41 through the crosswalk instead.
The frozen [D2 peer report](../independent-math-d2.md) remains a verification
of the original bytes; its hashes and historical claims are not rewritten.
Diamond T40 and rectangular N40 proof bytes are unchanged.

Recovery metadata:

- Encoding: UTF-8; byte offsets count from zero.
- Prefix byte count / original-body starting offset: 2255.
- Original-body byte count: 4450.
- Original-body SHA-256: `bcecd47698bea9679f6b734a26f8afb0fd85874a51b414ad75cf9ac650e98903`.
- Recover the archived body as `Path(this_file).read_bytes()[2255:]`.
  Hashing those bytes must reproduce the value above.

---

# PD-N?mz2d-codex-41 — no positive pointwise Padua weight floor

ID kind: PD-N. Aliases: direct signed M3 energy-conversion obstruction;
negative m3 corner. Split from: none. Split into: none.

## Statement

For the campaign's even-checkerboard signed Lebesgue rule at m=3, the
weight at `(1,1)` equals `-1/18`. Consequently no strictly positive nodal
reference weights `v_z>0` and constant `c>0` can satisfy either

\[
 w_z\ge c v_z\quad\hbox{at all Padua nodes},        \tag{1}
\]

or, equivalently for arbitrary real nodal data a,

\[
 \sum_z w_z a_z^2\ge c\sum_z v_z a_z^2.             \tag{2}
\]

This rejects only the pointwise/arbitrary-data conversion step of the
positive M3 proof. It does **not** reject any restricted-degree signed
sampling inequality on `Pi_2`, nor a fixed-ratio eta target.

## Definitions and assumptions

The campaign node, measure and signed interpolatory weight conventions
are those of `topics/padua-mz-2d-20261101/definitions.md`. In particular
the weight of a node is the unnormalized `dx dy` integral of its degree-m
cardinal polynomial. The data vector in (2) is arbitrary; this quantifier
is essential. The regularized angular-product reference weights used by
a putative weighted Schur transfer are strictly positive even at corners.

## Status and negative-result scope

Overall status: **PROVED** in development; independent mathematical audit
pending. Candidate IDEA?mz2d-codex-41: **REJECTED: failed**, for positive
pointwise/arbitrary-data conversion. No theorem about signed low-degree
coercivity is rejected.

Parameter range: the exact m=3 rule suffices to refute a mechanism asserted
for every m. D3 separately develops an all-m negative-corner formula;
that stronger statement is not duplicated here or required by this proof.

## Depends on

The integrated cardinal convention and degree-three unisolvence. Accepted
PD-T101's elementary cardinal formula is an inspected predecessor, but
the explicit node check below proves the local formula without depending
on its general kernel calculation. No audit-pending A2 statement is used.

## Proof

Write `T_r` for the ordinary Chebyshev polynomials. At m=3 the cardinal
polynomial of z=`(1,1)` is

\[
 L_z(x,y)=\frac1{24}\big[
 1+2x+2y+2T_2(x)+2T_2(y)+T_3(x)+2T_3(y)
 +4xy+4T_2(x)y+4xT_2(y)\big].                    \tag{3}
\]

This is the corrected product-Chebyshev cardinal formula at the corner:
the corner Chebyshev weight is `1/24`, and the exceptional `T_3(x)` term
has coefficient one instead of two. It can be checked without importing
the general formula. At x=1, the bracket is
`6+10y+6T_2(y)+2T_3(y)`, giving 24,0,0 at the retained levels y=1,0,-1.
At x=-1/2 it is `2T_3(y)-2y`, giving zero at those same three levels.
At x=1/2 it is `2y+4T_2(y)+2T_3(y)`, giving zero at retained levels
`y=+-1/sqrt(2)`, since `T_2(y)=0,T_3(y)=-y` there.
At x=-1 the bracket is `2y-2T_2(y)+2T_3(y)`, which also vanishes at
those two retained levels. These are all ten Padua nodes for m=3.
Equation (3) has degree three, so unisolvence identifies it as L_z.

Odd moments vanish, while `h_0=2,h_2=-2/3`. Integrating (3) gives

\[
 w_z=\frac1{24}\left[4+2h_2h_0+2h_0h_2\right]
 =\frac1{24}\left(4-\frac83-\frac83\right)
 =-\frac1{18}.                                  \tag{4}
\]

Since `cv_z>0`, equation (4) contradicts (1). For (2), set a_z=1 at
this corner and zero at all other nodes. Conversely (1) summed against
`a_z^2` would imply (2), so the two mechanism formulations are equivalent.
The arbitrary-data vector is realized by L_z in `Pi_3`; it is not claimed
to be realized by a polynomial in `Pi_2`. ∎

## Checks, sources, scope and open items

The formal test was exact symbolic evaluation and integration as written;
no program was executed. Candidate/kill records are in `ideas-d4.md`.
M3/PD-T023 uses a positive nodal floor for the actual CC weights. That
step cannot simply be reused for signed Padua weights. Source reports
of negativity were motivation, not the proof of (4).

A useful fixed-ratio successor must estimate the signed energy **on the
admissible polynomial value subspace**, or compare the negative part with
a positive restricted form. The result here supplies no sign conclusion
on that subspace. Independent audit and the full fixed-ratio target remain.

## History

2026-11-01, Codex `/root/d4_ratio`, requested gpt-6.1-sol xhigh, rules read
at supplied main `806cc7b4509fd93bae652f9545d32d95529f8281`. No Git mutation.
