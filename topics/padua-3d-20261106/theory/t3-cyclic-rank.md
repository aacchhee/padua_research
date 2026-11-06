# PD-T?padua-3d-codex-T3-01 — Exact cyclic cosine rank reduction

ID kind: PD-T.
Aliases: phase-weighted sign-orbit dictionary; odd cyclic half-grid matrix;
actual-node cyclotomic lift.
Split from: none; prerequisite for T2/T3, not a conjunct of the OPEN target.
Split into: none. Known-mechanism tool; no historical novelty claim.

## Statement

Let d>=1, M>=1, z in Z^d, phi in R^d and I a finite subset of N_0^d.
Write omega=exp(2*pi*i/M), theta_j(k)=phi_j+2*pi*k*z_j/M and
x(k)=(cos(theta_j(k)))_j, 0<=k<M. Let V have rows k and columns alpha in I,
with entries product_j T_(alpha_j)(x_j(k)). Define the M by |I| matrix

    B[r,alpha] = sum_{epsilon in {+1,-1}^d,
                      epsilon dot (alpha*z) = r (mod M)}
                 exp(i sum_j epsilon_j alpha_j phi_j),  0<=r<M.

The sum is over sign choices, with repetitions retained when alpha_j=0.
Then

    V = 2^(-d) F B,   F[k,r]=omega^(k*r),             (1)
    rank_R(V) = rank_C(B).                           (2)

Deleting duplicate node rows preserves rank. For I={alpha:|alpha|_1<=n},
evaluation on the distinct set X={x(k)} is injective on Pi_n iff B has
full column rank; it is unisolvent iff also |X|=binom(n+d,d).

For phi=0 put R=floor(M/2), f(s)=min(s mod M,(-s) mod M) and

    D[r,alpha]=#{epsilon in {+1,-1}^d:f(epsilon dot (alpha*z))=r},
    C[k,r]=cos(2*pi*k*r/M),       0<=k,r<=R.

On the parameter representatives 0<=k<=R,

    V_half=2^(-d) C D,   C invertible over R,         (3)
    rank_R(V_half)=rank_Q(D).                        (4)

Every full-orbit node occurs on these representatives. Extra coincidences
may occur for general z; if one z_j is a unit modulo M, there are exactly
R+1 distinct nodes. In particular T2's odd M=2N-1 and z_1=1 give exactly N
nodes, and Pi_n unisolvence is equivalent to det(D)!=0 when |I|=N.

For the integer D, full column rank modulo any prime implies full column
rank over Q and hence actual real-node injectivity. A nonzero rational
vector in ker(D) proves actual noninjectivity. Modular rank deficiency
alone has no converse implication.

## Definitions and assumptions

T_0=1, T_1=x, T_(a+1)=2xT_a-T_(a-1); thus T_a(cos t)=cos(at).
The product Chebyshev polynomials with |alpha|_1<=n form a basis of Pi_n
by nonzero triangular leading coefficients. All real/complex ranks in
the statement are exact. No positive cubature or tensor-cosine
orthogonality is assumed. Had the sign choices been deduplicated at
zero indices, (1) and (3) would have the wrong scaling.

## Status by part

Overall status: **PROVED** by the analytic proof below.

| Mathematical part | Status | Evidence / limit |
|---|---|---|
| General phase coefficient map and equality of kernels | PROVED | Product-to-sum and invertible Fourier matrix |
| Unshifted integer folded map | PROVED | Explicit cosine transform factorization |
| Modular implications and actual-node lifting | PROVED | Determinant reduction, including cyclotomic argument below |

Disposition: retained prerequisite, known-mechanism variant. No D2 survivor
is asserted and no Lebesgue or all-degree family result follows.

## Depends on

Only elementary polynomial leading terms, geometric sums, and determinant
reduction, proved as used below. PD-T106 is the closest local nodal-alias
predecessor; PD-T109 does not provide a rank or Lebesgue estimate here.
PD-T090 supplies the comparison with generic rational-axis witnesses,
whose conclusion must not be substituted for this prescribed-node claim.

## Proof

Expand each cosine into its two exponentials. Multiplying yields (1)
with exactly 2^d summands, even for zero alpha components. The geometric
sum identity gives F*F=M I (where * is conjugate transpose), so F is
invertible. Real matrices have the same real and complex rank; this gives
(2). Coincident nodes have identical polynomial-evaluation rows, hence
row deduplication changes neither rank nor kernel.

For zero phase, global sign reversal pairs each frequency with its
negative. Summing the paired exponentials gives precisely the folded
cosine expansion in (3). Residues 0 and M/2 (the latter only for even M)
are handled once as folded classes; multiplicities remain in D. Since
T_r(cos(2*pi*k/M))=C[k,r], C is a univariate polynomial evaluation matrix
of degrees 0,...,R at the distinct points cos(2*pi*k/M), 0<=k<=R. Their
angles belong to [0,pi], where cosine is strictly decreasing. A nonzero
polynomial of degree <=R has at most R roots, proving invertibility.
Integer-matrix rank is unchanged on extending Q to R, proving (4).

All coordinates are unchanged by k -> M-k at zero phase, so the chosen
half includes the full node image. If z_j is a unit and x_j(k)=x_j(l),
then z_j*k=+/-z_j*l modulo M; hence k=+/-l modulo M. For representatives
0<=k,l<=R this forces k=l. Thus their number is exactly R+1.

A full-column-rank integer minor nonzero mod p is nonzero in Z. Its
rational determinant is therefore nonzero. Conversely a displayed
rational kernel vector is a nonzero polynomial coefficient vector in
the Chebyshev basis and (3) makes its nodal values zero. Divisibility of
a nonzero determinant by p explains why a deficient modular rank does
not reverse the positive implication.

### Rational phases and direct root-of-unity rank certificates

Suppose phi_j=2*pi*a_j/L with integer a_j and M|L. Let zeta be a primitive
Lth root of unity. All entries of 2^d V and B lie in A=Z[zeta], and V
lies in A[1/2]. For an odd prime p with L|(p-1), choose rho in F_p with
**exact** order L. The factorization t^L-1=product_(e|L) Phi_e(t), whose
roots are disjoint because p does not divide L, implies Phi_L(rho)=0.
Consequently zeta -> rho defines a ring homomorphism A[1/2] -> F_p.
A minor with nonzero image was nonzero in A[1/2], hence at the prescribed
complex root and therefore at the prescribed real cosine nodes. This is
actual algebraic lifting, not the generic-axis conclusion of PD-T090.
A modularly deficient image does not establish a zero cyclotomic minor.

For phi=0 and M|(p-1), the finite-field counterpart of C is invertible
provided p is odd and rho has exact order M. Indeed the values
u_k=(rho^k+rho^(-k))/2 are distinct on 0<=k<=R: equality of u_k,u_l
implies (rho^k-rho^l)(rho^(k+l)-1)=0, hence k=+/-l modulo M. The leading
coefficient of T_r is a power of two and remains nonzero. Thus the same
polynomial root argument applies. These root/order hypotheses are needed
for a direct finite-field cosine evaluation, but **not** when lifting
full rank of the integer D itself.

### Frequency collisions versus basis injectivity

If the nonzero columns of B have pairwise disjoint supports, they are
independent. Injectivity of the frequency map on the distinct signed
indices {epsilon*alpha:alpha in I} is one stronger sufficient condition
(the repeated zero-index sign choices are not distinct signed indices).
Neither condition is necessary for full rank of B or D. Shared support
is an overlap of some summands, not an equality of entire cosine-product
columns.

For example d=2, n=2, M=11, z=(1,3), I=(00,10,01,20,11,02). The six
polynomials restrict to

    1, cos t, cos 3t, cos 2t,
    (cos 4t+cos 2t)/2, cos 6t.

On the Mth roots, cos 6t=cos 5t. Their folded-frequency coefficient
matrix has full rank: modes 0,1,3,2,4,5 give a triangular elimination.
The 20 and 11 columns share frequency 2. This warning is an elementary
example attached to the sufficient criterion, not a new interpolation
family or a separate rejected mechanism.

For a genuinely shifted coset global sign reversal need not preserve the
sample and B[-r,alpha] need not equal B[r,alpha]. One must use the full
phase-weighted B (or a separately justified phase-specific reduction).
Truncating to half the k rows merely because M is odd is unjustified.

## Checks

Analytic proof does not depend on computation. Developer sanity command:

`python topics/padua-3d-20261106/code/t3_checks.py --output topics/padua-3d-20261106/evidence/t3-checks.json`

The receipt records actual execution and code hash. It checks finite
field phase factorization, folded-rank agreement, zero-index factors and
the shared-frequency example. Independent replay remains to be performed;
no computer-assisted family claim is accepted by this prerequisite alone.

## Sources and scope

No fresh external fulltext was used. Existing relevant source-reading
limits are in [literature-T3](../literature-T3.md). This is a local proof
of a standard character reduction; no novelty/priority claim, universal
rank-one obstruction, good conditioning or Lebesgue growth is inferred.

## Open items

A D2-surviving explicit family, its all-degree determinant/injectivity
proof, and a quantitative inverse/kernel bound remain OPEN. For a shifted
half-grid chosen as a new definition rather than a full coset image, its
row-selection map must be analyzed separately.

## History

2026-11-06, Codex T3, assigned model `gpt-6.1-sol` xhigh (resolved runtime metadata not
exposed), pinned rules ccd9e905. Gate and candidate records preceded this
derivation; T2 supplied its explicit unshifted cyclic definition. No
shared-file changes or Git mutations.

## Supplementary check addendum — 2026-11-06

[Distinct Astra high check](../independent-checks-computation.md) completed
within its stated scope, including actual separate execution. Earlier
pending-check wording records the development state. Required Claude
substantive audit remains due; this addendum changes no mathematical claim.


## Completed-audit process addendum — 2026-11-06 — m5

[Claude audit-01](../audit-01.md) completed the substantive independent audit
of candidate f1a5b0936d8fb2b033c69af59a6366550f170999, including the recorded
independent executions, after the supplementary Astra checks. Its accepted
mathematical scopes supersede earlier “audit/replay/rerun pending” and
“planned, no run claimed” process descriptions where those refer to that
completed work. This addendum changes no mathematical statement or status;
MEASURED observations remain MEASURED and OPEN targets remain OPEN. The
new response dispositions/ID-kind/evidence changes require focused re-audit,
not another approval of the unchanged accepted mathematics.
