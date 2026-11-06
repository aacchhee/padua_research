# Supplementary mathematical check: S2 uniform bound and MZ deficit

Date: 2026-11-06. Codex independent supplementary checker, requested
`gpt-6-astra high`; actual runtime model/effort metadata is unexposed.
Rules/source corpus: `2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861`.
This supplements, and does not replace, the required Claude audit.

**PASS for the mathematical statements and proofs below.** No unresolved
BLOCKING, MAJOR or MINOR finding within this declared scope. The explicit
all-N upper bound and the deficit corollary are supported analytically.
No numerical experiment is used or claimed for this mathematical check.

## Audited statements and exact identities

The developer explicitly froze the uniform-bound file before review.
The separately added corollary was read after it was declared ready.

| Record | Audited SHA-256 |
|---|---|
| [S2-uniform-upper.md](theory/S2-uniform-upper.md) | `3a45f40aad550a50da4871ab2d3554adb60b41513b08b2427e10b203408b9e6b` |
| [S2-eta-deficit.md](theory/S2-eta-deficit.md) | `72f70e50aa67d5c7f3a262cf789984ed4a0283f05eeb11e47a98ef1f0a637a33` |

The first states Q_N(p²)<=5/3 integral p² for every N>=2 and every
real p in Pi_(N−1), with strict positive Q_N(p²) for nonzero p.
The second states the explicit two-sided deficit bounds using K_N from
PD-T017 and 128000/(log N)² from PD-T018, and therefore
1−eta_N has order (1+log N)^−2 and eta_N tends to1. Neither asserts
existence or value of either sharp spectral limit.

Read both target files in full, PD-T013/015/017/018 in full, the S2
candidate and novelty-gate records, PD-N104 in full, and the full
IDEA386 predecessor entry. The latter was read from the historical local
corpus only after its whole-file Git blob matched the developer's pinned
input identity `997bb5d0808b8d8557b3dc3eddc6fe8309ae4479`.

This supplementary assignment is proof-validity and dependency-scope
review only. It does not approve novelty, priority, the campaign-wide
candidate coverage or registry dispositions. The full state/IDEAS.md
was not read: a bounded initial read/search was followed by the relevant
full predecessor and obstruction records. The novelty/full-registry
audit remains in the required Claude handoff. No new mechanism or
candidate is proposed by this report.

## Independent reconstruction of the uniform bound

1. **Sign and normalization.** For s=i+j>N even, exact CC aliasing gives
   (M−R)_ij=1/((2N−s)²−1)−1/(s²−1). For s<=N the difference is zero;
   for odd s both moments vanish. Thus R=M−H+K with precisely the
   displayed entries. There is no missing factor2: it cancels against
   the product-to-sum factor1/2 in the mass matrices.

2. **Positive reflected core.** For i,j of the same parity, put
   r=2N−i−j. Then

       (1/2) integral_0^1 x^(r−2)(1−x²) dx
           = (1/2)(1/(r−1)−1/(r+1)) = 1/(r²−1).

   The two same-parity sums of squares give exactly H, without mixed
   parity terms. All exponents N−1−i are nonnegative, r>=2, and
   integration is over [0,1] with nonnegative weight. There is no
   singular endpoint or convergence qualification. Hence H is PSD.
   This does not assume PSD of the truncated defect M−R.

3. **Parity-dependent remainder.** A nonzero entry of K has even
   denominator index u=max(s,2N−s), so u>=N when N is even and u>=N+1
   when N is odd. Each parity block has at most ceil(N/2) indices.
   The nonnegative entry and row-sum estimates therefore give
   a^T K a <= ceil(N/2)/(L_N²−1) ||a||². K need not be PSD.

4. **Mass metric.** Reconstructed PD-T015's nonpositive off-diagonal
   argument: with b_0=1/2 and b_i=1, the telescoping residual is
   (Mb)_0=1/k_0 and (Mb)_i=k_i/(k_i²−i²), where i<k_i<=N.
   Its weighted quadratic identity gives M>=diag(2,1,...,1)/N.
   In particular ||a||²<=N a^T M a with the original signed vector a.
   Combining this with the preceding row estimate yields

       beta_N = N²/[2(N²−1)]       (even N),
                (N+1)/[2(N+2)]     (odd N).

   The first is <=2/3 for even N>=2; the second is <1/2 for odd N>=3.
   Therefore R<=M+K<=(1+beta_N)M<=(5/3)M.

5. **Boundary and positivity.** At N=2 every sum s<=2=N, so K=H
   and R=M exactly; the proof's loose beta_2=2/3 remains valid.
   At N=3 the only aliased even sum is4, with reflected index2;
   its K denominator is4²−1 as required. Positive CC weights and
   N+1 distinct nodes imply strict positivity for a nonzero polynomial
   of degree <=N−1. No claim is transferred to degree N.

6. **Obstruction scope.** The absolute values in the upper row bound
   concern K alone. The proof does not replace the original vector by
   its absolute values inside 2M−R or inside its continuous-mass
   denominator. Thus the specific intermediary refuted by PD-N104 is
   not invoked. The mathematical missing inequality in IDEA386,
   K<=beta M with a uniform beta<1, is supplied here. This observation
   does not constitute a historical novelty determination.

The additional limsup lambda_max<=3/2 statement follows directly from
the displayed beta_N formulas, each tending1/2. No spectral convergence
is required for that limsup conclusion. The sharp-limit question stays
OPEN.

## Independent check of the deficit corollary

The continuous orthonormal basis makes G_N real symmetric and positive
definite. For its spectral endpoints,

    eta_N=max(1−lambda_min,lambda_max−1),
    1−eta_N=min(lambda_min,2−lambda_max).

These identities are exact. The constant polynomial has quotient1,
so lambda_min<=1<=lambda_max. Applying the accepted all-N inequalities
PD-T017, PD-T018 and the newly checked upper gap gives exactly

    min(1/K_N,1/3) <= 1−eta_N
                    <= min(1,128000/(log N)²).

The K_N formula matches PD-T017, including both harmonic-number indices
and the factor4*pi²*(pi+1)². Since K_N<=C(1+log N)², the left side
is bounded below by c(1+log N)^−2: choose c<=min(1/C,1/3), using
(1+log N)^−2<=1. For N>=2, log N is uniformly comparable with
1+log N, so the right side supplies the upper order. Its convergence
to0 proves eta_N→1 together with positivity of the deficit.
At N=2, G_N=I and the deficit equals1, consistent with both displayed
bounds. No hidden finite-size onset or sharp coefficient is implied.

## Remaining scope

These proofs are analytic, not computer-assisted. Their supporting
identities were reconstructed above; the corollary retains explicit
dependencies on the established PD-T017/018 bounds. No numerical
evidence, extrapolation, imported asymptotic theorem or new model
prediction is a proof premise. Sharp upper-limit existence/value,
sharp lower constant, full historical coverage and final registry
classification remain outside this supplementary approval.
