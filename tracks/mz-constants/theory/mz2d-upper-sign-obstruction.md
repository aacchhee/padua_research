# PD-N045 — coefficient sign comparison fails for Padua

Provisional alias: `PD-N?mz2d-codex-10`. Final ID assigned at PR preparation, 2026-11-01; required Claude audit PENDING.

ID kind: PD-N.
Aliases: signed-Padua Z-matrix obstruction; frustrated coefficient triangle;
two-dimensional absolute-coefficient transfer.
Split from: IDEA-212, the direct transfer of the one-dimensional
proof of PD-T014/022 to the signed Padua endpoint space; and IDEA-225,
the strictly positive pointwise nodal-floor transfer.
Split into: none. The upper target is retained OPEN in
[PD-T110](mz2d-upper-open.md).

## Statement

For every integer `m>=3`, let `H,R` be the continuous and signed Padua
mass matrices on the product-Chebyshev basis of `Pi_(m-1)`, with the
fixed even-checkerboard, unnormalized `dx dy` conventions of
[definitions.md](../../../topics/padua-mz-2d-20261101/definitions.md).
Set `A=2H-R`. There is **no** diagonal matrix `S` with diagonal entries
in `{−1,1}` such that all off-diagonal entries of `S A S` are nonpositive.

Moreover, at `m=4` the defect `H-R` has entries of both signs. Thus
neither of the two entrywise sign hypotheses used in the one-dimensional
absolute-coefficient proof transfers in the stated basis.

At `m=3`, the weight at `(1,1)` is `w_(1,1)=−1/18`, so there is no
strictly positive pointwise nodal floor. For bounded nodal data equal to
one at that node and zero elsewhere, `Q_3(f²)=−1/18`. The expression
`Q(f²)^(1/2)` in positive-weight Cauchy–Schwarz therefore cannot be used
on arbitrary nodal data. This elementary witness checks the missing
hypothesis; it does not decide the restricted signed polynomial form on
`Pi_(m-1)`.

## Definitions

The row indexed by `(i,j)` represents `T_i(x)T_j(y)`; `H` is its
continuous Gram matrix, and `R` its signed-quadrature Gram matrix.
A real matrix with nonpositive off-diagonal entries is called a Z-matrix.
The allowed `S` changes coefficient signs but does not change the basis
by an arbitrary linear transformation.

## Assumptions

The fixed signed Padua rule, total degree `m−1`, real coefficients and
the product-Chebyshev basis. The first assertion covers every `m>=3`;
the mixed-defect-sign example is at `m=4` only. No assertion excludes
other bases, block comparisons, or a direct proof that `A` is positive.

## Status by part

Overall status: **PROVED** in development; independent audit pending.
Both entrywise sign obstructions are proved analytically below.

Candidate / claim disposition: **REJECTED: failed**, restricted to the
specified coefficient-sign transfer. The spectral upper target is OPEN,
not rejected. The obstruction is not caused solely by negative nodal
weights: the tensor continuous mass matrix already contains the sign
cycle that prevents this one-dimensional argument.

## Negative-result scope

Attempted mechanism: IDEA-212, requiring `2H-R` to be a
Z-matrix after diagonal sign switching, and a nonnegative entrywise
defect as in IDEA-062/073.
Parameter range: switchability fails for all `m>=3`; both defect signs
are exhibited at `m=4`.

Second attempted mechanism: IDEA-225, requiring a strictly positive
pointwise nodal floor and the positive-weight Cauchy–Schwarz step on
arbitrary nodal data. Parameter range: `m=3`, where `w_(1,1)=−1/18`.
For bounded nodal data equal to one at that node and zero elsewhere,
`Q_3(f²)=−1/18`. The expression `Q(f²)^(1/2)` in positive-weight
Cauchy–Schwarz therefore cannot be used on arbitrary nodal data.
This elementary witness checks the missing hypothesis; it does not
decide the restricted signed polynomial form on `Pi_(m-1)`.

## Depends on

Only degree-`m` exactness, elementary Chebyshev integrals, and the nodal
alias identities of [PD-T106](mz2d-aliasing.md). The aliases
used here can also be checked directly at the stated nodes.
PD-T014/022 identify the attempted predecessor mechanism, not a proof
dependency for the obstruction.

## Checks

No computation is necessary for this analytic proof. The three-mode
cycle and the two mixed entries were the prewritten cheapest tests in
[ideas-d2.md](../../../topics/padua-mz-2d-20261101/ideas-d2.md).
Separate finite spectra do not enter this result.

## Sources

Local predecessor IDEA-062/073 and PD-T014/022, read in full. No external
theorem, unread primary-source statement, or historical novelty claim.

## Proof or evidence

### 1. A sign cycle invariant under every allowed switch

Use the three distinct modes `u=1`, `v=T_2(x)`, `z=T_2(y)`, all in
`Pi_(m-1)` when `m>=3`. Since `h_0=2` and `h_2=−2/3`, degree-two
exactness gives

\[
 A_{uv}=H_{uv}=-4/3,\qquad A_{uz}=H_{uz}=-4/3.
\]

For `m>=4`, degree-four exactness also gives

\[
 A_{vz}=H_{vz}=h_2^2=4/9>0.
\]

For `m=3`, the complementary nodal alias for `T_2(x)T_2(y)` is
`T_1(x)T_2(y)`, of degree three. Its integral vanishes, so `R_vz=0`
and `A_vz=2h_2^2=8/9>0`. Therefore in every claimed degree

\[
 A_{uv}A_{vz}A_{zu}>0.                                      \tag{1}
\]

Under a diagonal sign switch, this product is multiplied by
`(s_u s_v)(s_v s_z)(s_z s_u)=1`. If all three switched entries were
nonpositive, they would in fact be negative because none is zero,
and their product would be negative. This contradicts (1).

This also rules out replacing sign switching by nonzero real diagonal
scalings for the purpose of changing this sign pattern. At `m=2`, the
quadratic products in `Pi_1` are exact and this cycle is absent; the
statement deliberately does not include that case.

### 2. The signed Padua defect has no inherited entrywise sign

At `m=4`, put `v=T_2(x)`, `z=T_3(y)`, and `t=T_2(x)T_1(y)`.
All three have total degree at most three. The nodal representatives
of the required product modes are

\[
 T_2(x)T_3(y)\longleftrightarrow T_2(x)T_2(y),\qquad
 T_4(x)T_1(y)\longleftrightarrow T_0(x)T_4(y).
\]

Their representative degrees are four. Exactness and odd moments give

\[
 (H-R)_{v,z}=0-h_2h_2=-4/9,
\]
\[
 Q_4(vt)=\tfrac12 Q_4((T_4(x)+1)T_1(y))
 =\tfrac12 h_0h_4=-2/15,
 \qquad (H-R)_{v,t}=2/15.
\]

The two opposite signs disprove either universal entrywise sign choice
for this defect in the unmodified product basis. They do not prove that
the defect is indefinite, nor is such an assertion needed here.

### 3. The separate positive-nodal-weight hypothesis fails exactly

For clarity about the other old proof step, a small exact signed-weight
witness can be verified without a numerical weight solve. At `m=3`,
the cardinal polynomial for the retained node `(1,1)` is

\[
 L(x,y)=\frac{4x^3+8x^2y+4x^2+8xy^2+4xy-5x
                 +8y^3+4y^2-8y-3}{24}.
\]

The x levels are `1,1/2,−1/2,−1`. At the first and third levels the
retained y values are `1,0,−1`; at the other two they are `±1/sqrt(2)`.
The four restrictions of `L`, in that x order, are

\[
 \frac{y(2y+1)(y+1)}6,\quad
 \frac{(y+1)(2y^2-1)}6,\quad
 \frac{y(y^2-1)}3,\quad
 \frac{(2y-1)(2y^2-1)}{12}.
\]

These values are one at `(1,1)` and zero at the other retained nodes.
Thus the weight at `(1,1)` equals the integral of `L`. Odd monomials
integrate to zero, and

\[
 w_{00}=\frac{4(4/3)+4(4/3)-3(4)}{24}=-1/18.
\]

For bounded nodal data equal to one at that node and zero elsewhere,
`Q_3(f²)=−1/18`. The expression `Q(f²)^(1/2)` in positive-weight
Cauchy–Schwarz therefore cannot be used on arbitrary nodal data.
This elementary witness checks the missing hypothesis; it does not
imply a negative polynomial Gram eigenvalue on `Pi_2`.

## Scope

Two exact sign hypotheses of the one-dimensional route fail. A
Z-matrix sufficient criterion is not necessary for positive definiteness.
Neither the target `lambda_+<2` nor a block/operator approach is refuted.
Likewise a negative nodal weight does not decide the restricted signed
polynomial form on `Pi_(m-1)`.

## Open items

Independent audit of the written algebra. A successful successor must
control complementary modes while retaining two-coordinate cancellation,
or use a different basis with a separately proved comparison.

## History

2026-11-01, Codex, requested gpt-6.1-sol xhigh, rules
`cf89b140530d5838bdb208a8c28f3e7aa676ace3`, unchanged after campaign
merge of `806cc7b4509fd93bae652f9545d32d95529f8281`.
D1 PASS was received before this bounded D2 round. No Git operation,
final-ID assignment, or computer-assisted proof claim by this worker.
