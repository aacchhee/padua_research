# PD-T?proof-attempts-2-codex-91 — A coalescent structural witness for pole-only generic rank

ID kind: PD-T.
Aliases: B1 generic generation; coalescent projective polynomial flag; fixed-data offset discriminant.
Split from: programme `OPEN_TARGETS.md` B1, reverse-inclusion/generic-rank obligation.
Split into: none. Detection is record 90; the combined class theorem is record 92.

## Statement

Fix any `T>=3`, any `M` real nodes in `[-1,1]^2` injective for `Pi_(T+1)`, and any positive weights. All node/weight data are held fixed. For offsets `a=(a_1,...,a_(T+1))` in `Omega=(2,infinity)^(T+1)`, use the rational flags, `C_t` and `R_t` of record 90.

1. At every coalescent tuple `a_1=...=a_(T+1)=c>2`,
   `R_t=W_(t+1) direct-sum W_(t-2)` and `dim R_t=2t+1` for every `2<=t<=T`.
2. There are explicit polynomial expressions `p_t(a)`, depending on these fixed nodes/weights, positive at every such coalescent tuple, for which `p_t(a)!=0` implies `dim R_t=2t+1`.
3. With `Delta(a)=prod_(i<j)(a_i-a_j)`, the polynomial
   `F(a)=Delta(a)^2 prod_(t=2)^T p_t(a)`
   is not identically zero. Hence `E={a:F(a)=0}` is a proper real algebraic subset of the **pole-offset parameter space alone**. For `a in Omega\E`, all poles are distinct and all displayed ranks hold simultaneously. Such tuples exist in every sufficiently small coalescent neighbourhood, including strictly ordered tuples.

There is no generic-node or generic-weight quantifier in this statement.

## Definitions and assumptions

All notation and finite-sampling assumptions are as in record 90. `P_V` and `P_W` are weighted orthogonal projectors; the diagonal matrices of original coordinates are denoted `D_x,D_y`. Repeated poles are permitted in the auxiliary coalescent witness, not in the final distinct-pole class. They have nonzero denominators and full flag dimensions, so all witness projectors are defined. Coalescence is used to prove a polynomial is nonzero, not asserted to lie outside the final collision exceptional set.

## Status by part

Overall status: **PROVED**. Complete written proof and actual supplementary full-file inspections are recorded below. No finite numerical or exact computation is required; Part 2 Claude audit remains PENDING.

| Mathematical part | Status / verification obligation |
| --- | --- |
| Coalescent rank, rational projectors and proper pole-only exception | PROVED; written structural proof below and actual independent full-file candidate inspections |

Candidate / claim disposition: retained exact completion route; no novelty claim.

## Depends on

Record `PD-T?proof-attempts-2-codex-90`, universal bound `dim R_t<=2t+1`. Other ingredients are proved below by polynomial degree, positive inner-product duality and finite matrix algebra. No external rational recurrence or unproved source generic-rank assertion is used.

## Checks and sources

The parent, primary checker and top-form agent ACTUALLY read the complete frozen candidate proof and found no blocker. Exact reviewed hashes and scopes are in `../independent-checks-b1.md` and `../independent-checks-b1-topform.md`. Status/verification metadata only changed on promotion; the matching before/after proof-body hashes are in `../outputs/b1_status_metadata.json`. No computation or computational rerun is claimed. Part 2 Claude audit remains PENDING. Source target/provenance is programme B1 and `../attempts/T-B1.md` at input head `ec05862985460ed18d6756b2bd9b4c5266b39df2`.

## Proof

### 1. Coalescence converts the entire flag to a polynomial flag

Set `L=x+y-c`, `X=x/L`, `Y=y/L`, and `A=1/L`. Then

`A=(X+Y-1)/c`.

At coalescence `pi_j=L^j`. For every `j<=T+1`, the evaluated space `V_j` equals the polynomial space `Pi_j(X,Y)`. Indeed

`x^u y^v/L^j = X^u Y^v A^(j-u-v)` for `u+v<=j`,

which proves one inclusion, while

`X^u Y^v = x^u y^v L^(j-u-v)/L^j`

proves the other. Thus transformed evaluation has full polynomial dimensions: its `dim Pi_j` monomial columns span the already full-dimensional space `V_j`. The fixed positive inner product is unchanged. The `W_j` are therefore ordinary orthogonal degree blocks in these transformed coordinates.

For such a polynomial flag, multiplication by any affine polynomial sends `W_j` into `W_(j-1)+W_j+W_(j+1)`. It has degree at most `j+1`, and its pairing with any degree at most `j-2` test polynomial vanishes after moving the real affine multiplier to that test vector, now of degree at most `j-1`.

Here

`C_t=A W_(t-1)+A W_t+X W_t+Y W_t`.

Because `X+Y-cA=1`, this space contains `W_t` and equals

`A W_(t-1)+W_t+X W_t+Y W_t`.

Consequently projection off `W_t` and `W_(t-1)` leaves only `W_(t+1)+W_(t-2)`.

### 2. Both surviving blocks are fully generated

The top homogeneous-form map on an ordinary degree block `W_j` is an isomorphism to `H_j`: a vector whose polynomial degree is lower belongs to `V_(j-1)` and is orthogonal to itself; dimensions then give surjectivity. The top forms of `X W_t+Y W_t` span

`X H_t+Y H_t=H_(t+1)`.

Hence projection of these products onto `W_(t+1)` is onto. Their only other blocks are precisely the two being removed, so `W_(t+1) subset R_t`.

For the other block put `k=t-2`. Consider

`B:W_(t-1) -> W_k`, `Bv=P_(W_k)(A v)`.

Its adjoint is `B*:W_k -> W_(t-1)`, `B*q=P_(W_(t-1))(Aq)`. This adjoint is injective: a nonzero `q in W_k` has a nonzero homogeneous degree-`k` form. The linear part of `A` is `(X+Y)/c`, a nonzero polynomial. Their product is nonzero in the polynomial ring, so `Aq` has degree `k+1=t-1`. Injective transformed evaluation prevents it from becoming a lower-degree polynomial on the nodes. Therefore its degree-`t-1` block is nonzero. Finite-dimensional positive inner-product duality makes `B` onto.

The other blocks of `A W_(t-1)` are removed by the projection. Thus `W_k subset R_t`. Both inclusions and the preceding containment prove

`R_t=W_(t+1) direct-sum W_k`, of dimension `2t+1`.

This proof includes `t=2`: the backward map is onto the constant block, since multiplication of a nonzero constant by the nonconstant affine `A` has nonzero degree-one part.

### 3. Explicit rational matrices for fixed data

For each `0<=j<=T+1`, let `A_j(a)` be the `M` by `N_j` evaluated matrix of all monomials of degree at most `j`, divided at row `i` by `pi_j(z_i)`, where `N_j=(j+1)(j+2)/2`. Let `W=diag(w_i)`. These matrices have full column rank everywhere on `Omega`, and

`P_j=A_j (A_j^T W A_j)^(-1) A_j^T W`

is the weighted projector onto `V_j`. Put `P_(-1)=0`, `Q_j=P_j-P_(j-1)`, the projector onto `W_j`, and `D_(t+1)=diag(ell_(t+1)(z_i))`.

The following `M` by `4M` rational matrix has image exactly `R_t`:

`M_t=(I-Q_t-Q_(t-1)) D_(t+1)^(-1) [Q_(t-1), Q_t, D_x Q_t, D_y Q_t]`.

Thus all rank conditions concern rational functions of the offsets alone; the nodes and positive weights remain fixed coefficients.

### 4. Clearing denominators without a hidden generic-data assumption

An explicit common polynomial denominator can be given. Let

`h_j(a)=prod_(i=1)^M pi_j(z_i)`, `B_j(a)=h_j(a) A_j(a)`,
`g_j(a)=det(B_j^T W B_j)`, `G(a)=prod_(j=0)^(T+1) g_j(a)`.

Each entry of `B_j` is polynomial in the offsets: its row denominator is cancelled by the corresponding factor in `h_j`. Since `h_j` is nonzero on `Omega`, `B_j` has full column rank there and `g_j>0` there. Computing `P_j` with `B_j` gives the same projector; its entries have denominators dividing `g_j` by the adjugate formula. Hence entries of `Q_j` have common denominator `G`.

For each `t` define

`q_t(a)=G(a)^2 prod_(i=1)^M ell_(t+1)(z_i)`.

This is nonzero on `Omega`, and `K_t=q_t M_t` is a polynomial matrix: a term has at most two projector factors and one diagonal inverse, all cleared by the displayed factors.

Let `r_t=2t+1` and define the finite polynomial

`p_t(a)=sum_(|I|=|J|=r_t) det(K_t[I,J])^2`,

where `I` ranges over row subsets and `J` over column subsets. There are enough rows since `M>=N_(T+1)>r_t`. Real sums of squares vanish exactly when every such minor vanishes. At the coalescent tuple, parts 1–2 give rank `r_t`; its denominator `q_t` is nonzero, so `p_t>0` there. This is a structural nonzero witness for **every** fixed admissible sampled measure, not a computed numerical rank and not a witness obtained by varying the nodes/weights.

If `p_t(a)!=0`, rank is at least `r_t`; record 90 bounds it above by `r_t`. Thus it equals `r_t`. The finite product `prod_(t=2)^T p_t` is positive at any common coalescent tuple. Multiplying it by the nonzero collision polynomial squared produces a nonzero polynomial `F`: the real polynomial ring has no zero divisors. Its zero set is proper.

For clarity, although the collision factor vanishes at the witness, this does not make `F` identically zero. Alternatively, all `p_t` stay positive in some neighbourhood of the coalescent tuple by continuity, and that neighbourhood contains distinct strictly ordered offsets, for example `a_j=c+j*epsilon` for sufficiently small positive `epsilon`. Thus each prescribed strict ordering also has admissible offsets outside the exception. No numerical choice or computed bound on `epsilon` is required for this existence argument.

## Scope

The exceptional polynomial may depend on the fixed nodes, weights and finite ceiling `T`. No uniform exceptional set independent of all sampled measures is asserted. This is the free-offset real parallel diagonal class underlying the source's `Ldiag`; it does not yet prove that a particular fixed tapered sequence from its numerical experiments avoids the exceptional set. That is a separate specialization question. No unbounded-degree claim on a fixed finite node set or numerical-stability theorem follows.

## Open items

Supplementary full-file candidate inspections are complete; Part 2 Claude audit remains PENDING. Record 92 combines this generic rank with record 90's exact detector to obtain the equality. The pole classes `Ppt`, `Pbhh`, `Pdiag` and unrestricted real directions remain outside this class result.

## History

2026-11-01, Codex `gpt-6.1-sol xhigh`, within the original B1 box. Coalescent projective witness independently reconstructed by the lead, primary checker, top-form agent and parent; this wording records reconstruction rather than asserting separate origination. Source skew-form ranks are not inherited. Full structural proof supplies the user's nonzero-witness alternative without executing mathematical code.
