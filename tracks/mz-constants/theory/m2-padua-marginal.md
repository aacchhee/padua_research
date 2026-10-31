# PD-T?mz-constants-codex-28 — exact Padua marginal and spectral domination

ID kind: PD-T.
Aliases: factor-two x-marginal; univariate compression of the Padua Gram matrix.
Split from: supplied Padua marginal source fact, reconstructed independently.
Split into: none. The genuine two-dimensional upper-spectrum and minimum-eigenvalue asymptotics remain separate OPEN targets.

## Statement

Let N≥2. Suppose a real-weight cubature rule Q_N^P on [-1,1]² is supported at the Padua set

    P_N={(cos(jπ/N),cos(kπ/(N+1))): 0≤j≤N,0≤k≤N+1,j+k even},

and is exact for unnormalized Lebesgue integration on all bivariate polynomials of total degree≤N. Then its weights W_jk satisfy

    Σ_(k:j+k even) W_jk=2w_j^CC,   j=0,…,N,            (1)

where w_j^CC are the N+1-node CC weights. For every 0≤n≤N, define the real symmetric Gram matrices on Π_n and on bivariate total-degree P_n in Lebesgue-orthonormal bases. Their extreme eigenvalues and deviations satisfy

    λ_min(G_N,n^P)≤λ_min(G_N,n^CC),
    λ_max(G_N,n^P)≥λ_max(G_N,n^CC),
    ||I−G_N,n^P||₂≥||I−G_N,n^CC||₂.                   (2)

In particular at n=N−1, liminf_(N→∞)||I−G_N,N−1^P||₂≥1, using PD-T?mz-constants-codex-22. At N=512,n=511 the deviation is >3/4, using PD-N?mz-constants-codex-24.

## Definitions

The CC weights integrate degree-N cardinal polynomials on the x coordinates. The Padua weights in this theorem may have either sign; only the explicitly stated exactness is assumed. An interpolatory Lebesgue Padua rule, when defined by integrating its degree-N interpolation basis or by solving its exact moment equations, has precisely this exactness. The theorem applies to any such solution and does not assume a separate positivity claim.

λ_min/max are the usual real symmetric eigenvalues even when weights have both signs. The identity in each deviation acts on its corresponding finite-dimensional orthonormal coefficient space.

## Assumptions

The support, real weights, total-degree exactness, measure and parameter ranges in the statement. Neither weight positivity, an upper MZ bound nor a two-dimensional Schur estimate is assumed. Existence or uniqueness of the full bivariate interpolation rule is not needed to prove this implication for any weights satisfying these explicit moment conditions.

## Status by part

Overall status: PROVED (development; independent audit and acceptance pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Exact factor-two marginal | PROVED | Univariate interpolation uniqueness |
| Compression and extreme/deviation domination | PROVED | Isometric embedding, signed weights allowed |
| Stated liminf and finite consequences | PROVED | Exact domination and split CC dependencies |

Candidate / claim disposition: equivalent to the supplied marginal mechanism; independently reconstructed for its correct normalization, not claimed novel.

## Depends on

Univariate Vandermonde interpolation and finite-dimensional symmetric variational principle. Only the asymptotic consequence uses PD-T?mz-constants-codex-22, and only the finite consequence uses PD-N?mz-constants-codex-24. The algebraic identities and domination (1)–(2) are independent of those results.

## Checks

Rules/base d36722823441dc40c6e19d69a174459348dd309c. Source `padua_marginal_cc.py` read in full; no source run is claimed. No numerical execution is required by this analytic reconstruction. Its printed first difference mixes wx with wCC; the separately printed `wx−2*wcc` is the correct marginal diagnostic. Independent proof audit is needed; any existing root numerical reproduction is separate evidence, not inherited here.

## Sources

Supplied `topics/mz-constants/sources/padua_mz_inputs/code/padua_marginal_cc.py`; local reconstruction, no third-party theorem imported. Source hash is in the M2 Padua foundation record. No novelty/priority claim.

## Proof or evidence

Let a_j=Σ_k W_jk. For every univariate polynomial q of degree≤N, bivariate exactness applied to q(x) gives

    Σ_j a_j q(x_j)=∫[-1,1]²q(x)dxdy=2∫[-1,1]q(x)dx
                  =Σ_j2w_j^CC q(x_j).

Taking q to be each degree-N univariate cardinal polynomial shows a_j=2w_j^CC. This proves (1) with no positivity assumption.

Now map q(x) to Jq(x,y)=q(x)/√2. This map sends Π_n into bivariate P_n and is an isometry because ∫∫(q/√2)²=∫q². The grouped marginal identity implies, for any p,q∈Π_n,

    Q_N^P[(Jp)(Jq)]=(1/2)Σ_j a_j p(x_j)q(x_j)
                   =Q_N^CC(pq).

This uses (1), so it remains valid even when deg(pq)>N; no extra cubature exactness is being silently assumed. Thus in orthonormal coefficient coordinates, J*G_N,n^P J=G_N,n^CC and J*J=I. Symmetric Rayleigh quotients on the embedded subspace prove the two eigenvalue inequalities. Likewise

    I−G_N,n^CC=J*(I−G_N,n^P)J,

and operator-norm contraction under an isometric compression proves the deviation inequality. This argument is valid for signed cubature weights.

At n=N−1, λ_min(CC,N−1)→0 by the split upper theorem. Therefore

    ||I−G_N,N−1^P||₂≥||I−G_N,N−1^CC||₂
                     ≥1−λ_min(CC,N−1)→1,

which proves the liminf conclusion only. The finite counterexample transfers by the same norm domination.

## Scope

The result establishes the exact marginal and a one-sided compression comparison. Signed weights do not establish positivity of G^P. No upper bound for the Padua deviation, convergence of that deviation to1, positive lower Padua eigenvalue, or matching two-dimensional asymptotic order is asserted.

## Open items

Independent acceptance. Genuine Padua upper-spectrum and two-sided endpoint questions remain OPEN, with no new two-dimensional mechanism launched by this foundational reconstruction.

## History

2026-10-31, Codex gpt-6.1-sol xhigh (explicit orchestrator assignment), rules/base SHA above. Requested by root after completing M2 development, as source-fact reconstruction rather than a third substantive exploration. Normalization 2 is retained explicitly through the isometry.
