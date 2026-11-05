# PD-T?lanczos-frontier-codex-L2-05 — the saved full-sign X-closure expectation target holds on every SH_n

ID kind: PD-T.
Aliases: SH_n full-law Frobenius closure growth; final-degree isotropic source block.
Split from: saved R target in attempts/L2.md; W has its own L2-04 record.
Split into: none.

## Statement

For every integer n>=2 on exactly the frozen SH_n family, with H=N_n-1
and M=(n+2)², let all H*M signs xi_hi be independent and uniform in
{-1,+1}, and set, in weighted represented Euclidean coordinates,

    f_h(i)=sigma_h xi_hi/sqrt(H M).

For the saved smooth exact-base BJ class and original Frobenius-closure
observable,

    E_n=inf_R E[sum_(s<n)||D_X,s(R,xi)||_F²]/||X||²,

we have

    E_n >= (4^n-1)/(6 n(n+2) cos²(pi/(n+3)))
         >= 2^(n-8).                                      (1)

This proves exactly the saved R growth target under the unchanged full
law. The lower uses one source block's contribution after expectation;
it is neither the exact full E_n nor an expectation under a new one-source
or normal-direction random law.

## Definitions and assumptions

The family, weights, represented orthonormal basis, BJ order and saved
class are exactly those of L2-04 and attempts/L2.md. D_X,s is the actual
closure-frame derivative, equivalently the full projector-closure
derivative for its Frobenius norm, as proved in L2-01/03. The maximum
stage for W and the sum for R are not interchanged.

Positive weights, injectivity, exact starting vector and fixed nodes/
weights/parents; smooth exact-base coefficient and normalization rules.
There are H=N_n-1 global source positions. The signs are on Euclidean
represented-vector node coordinates, not unweighted polynomial values;
there is no added sqrt(w_i) in their covariance. No independence of
computed scalar roundoff or actual IEEE realization is assumed.

## Status by part

Overall status: PROVED, analytic complete proof below; distinct
supplementary mathematical check accepted; required Claude audit pending.

| Part | Status | Evidence |
|---|---|---|
| Full-law selected-block trace lower in (1) | PROVED | Common linear closure map, original covariance and rank of R_n |
| Original R target for all n>=2 | PROVED | Exact family dimensions and elementary exponential comparison |

## Depends on

L2-03 for positive-weight rule invariance and the exact global sign
covariance/trace reduction; L2-04 for its independently checkable exact
closure action of source h=(n,0), equation(2). L1a supplies the checked
family dimensions, orthogonality and source scale. No span lower is
used as a closure lower. Actual G2 passes preceded this proof as the
required protocol gate, without extrapolating a finite computation.

## Checks and sources

Analytic development only; no new experiment was executed by this worker.
The prospective original R statement and scope are in attempts/L2.md.
Closest source/observable distinctions are retained in the L2 gate.
No new primary literature or historical-priority claim. A distinct
reviewer reconstructed and accepted the full initial draft SHA256
`6a96b9e001e1e359aca4be418bb799f4bd284c3e39c1688014fe69c129b0e045`,
including removal of cross terms only after expectation, the original
isotropic covariance, exact rank factor and all-n constants. Its separate
review is independent-checks-l1-l2.md; no mathematical finding was reported.

## Proof

For every saved rule the closure derivative is the same **linear** map
of all normalized aggregate sources, by the weighted quotient theorem.
Decompose each stage response as a sum of source-block responses. Under
the complete original independent-sign law, blocks are independent and
centered, so all cross-block terms in each squared Frobenius norm have
zero expectation. The expected sum of squares is a sum of nonnegative
block contributions. We may therefore retain only stage n-1 and source
h=(n,0). This is done after expectation; realized block outputs need
not obey any pointwise lower because cancellation is possible.

The exact source-block action from L2-04 is

    D_X,n-1(:,(n-1-j,j))=-(-2)^j R_n f_h,
                            j=0,...,n-1,

with all other columns zero. Consequently its squared Frobenius norm
is `(4^n-1)||R_n f_h||²/3`.

The actual full-law covariance of this selected block is

    E[f_h f_h^T]=sigma_h² I_M/(H M)=I_M/(2 H M),

because h=(n,0) has raw-source scale sigma_h²=1/2 for n>=2.
Hence, using R_n²=R_n and exact weighted-space rank N_n,

    E||R_n f_h||²=tr(R_n E[f_h f_h^T])
                 =(M-N_n)/(2 H M).                         (2)

Only this second-moment identity is used. We do not rotate the
Rademacher distribution or assert that it is rotation invariant, and
we do not replace covariance I by diag(w).

Every saved rule therefore has

    E[sum_(s<n)||D_X,s||_F²]/||X||²
       >= (4^n-1)(M-N_n)/(6 H M ||X||²).                    (3)

Taking their infimum preserves this common lower. For this exact family

    M-N_n=(n+2)(n+3)/2,
    H=n(n+3)/2,
    (M-N_n)/(H M)=1/[n(n+2)],
    ||X||=cos(pi/(n+3)).

Substitution proves the first bound in (1).

For the original target, the elementary inequality
`2^n>=n(n+2)/2` holds for n>=2: equality at n=2, and the induction
step follows from
`2n(n+2)-(n+1)(n+3)=n²-3>=0`. Also
`4^n-1>=(3/4)4^n` for n>=1, and ||X||²<1. Thus the displayed
lower in (1) is at least

    (3/4)4^n/[6 n(n+2)] >= 2^n/16 >= 2^n/256=2^(n-8).

The stronger intermediate inequality proves the original frozen
threshold; it does not redefine the target or random law.

## Scope and open items

This is a formal full-law expectation over every represented node and
global source coordinate, for each finite n in the n-dependent family.
It gives no deterministic lower for each sign realization, high-probability
bound, exact full E_n, actual IEEE activation, uniform finite-epsilon
radius or unrestricted working-precision PD-T055 resolution. The source-
block lower is valid because the complete expectation has nonnegative
trace contributions; omitted sources were not removed from the law.
Independent mathematical reconstruction is accepted. Required Claude
scientific/protocol review remains pending, with the earlier campaign
timing deviation preserved.

## History

- 2026-11-05: Codex, configured gpt-6.1-sol xhigh. Saved R target, full
  sign law and selected-source-block expectation route were stated
  prospectively after actual independent G2 acceptance. Weighted bridge
  and actual closure action precede this separate complete proof. No
  numerical extrapolation, law change, pointwise block lower or IEEE
  claim is made; distinct mathematical review requested.
- 2026-11-05: Verification metadata updated after distinct reconstruction
  accepted the complete initial draft. Statement, law and proof are
  unchanged; required Claude audit remains pending.
