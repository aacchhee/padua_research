# PD-T?argmax-bridge-codex-C1 — Near-edge comparison reduces to the fixed-count model

ID kind: PD-T. Aliases: near-edge model budget; finite-model comparison
criterion. Split from: the unresolved full all-degree argmax comparison.
Split into: none. This is direct assembly of the already stated N1/N5
results, not a new mechanism, novelty or priority claim.

## Statement and definitions

Let n>=10^6 be an integer, m=n+1. Let J be0 or n and
1<=q<=m-1 satisfy J+q odd. Use inward alpha>=0 and signed beta
with alpha+|beta|<=1/2. Define

    x=cos(alpha/n) if J=0, and x=-cos(alpha/n) if J=n,
    y=cos((q*pi+beta)/m).

Let M_near(alpha,|beta|,log n) be exactly the fixed-count model of
N1-15, with its finite-h/collision convention and R128,delta1/1000.
Then at every such point,

    lambda_n(x,y) < M_near(alpha,|beta|,log n)-491/1792000
                  < M_near(alpha,|beta|,log n)-1/4096.  (1)

In particular the model inequality

    M_near(alpha,|beta|,log n)<=Lambda_c(n)+1/4096      (2)

implies the strict comparison

    lambda_n(x,y)<Lambda_c(n)-107/3584000.             (3)

If (2) is verified uniformly over the displayed phase domain and all
integers n>=n0>=10^6, (3) therefore holds for every interior
complementary vertical-edge class at every such degree. Uniform (2)
is an OPEN comparison obligation, not a conclusion of this record.

## Status and dependencies

Overall status: **PROVED**, elementary corollary of the written N1-15
model error and N5-04 two-phase defect. Their stated hypotheses are
explicit premises here; their independent review records retain their
exact source identities. No fit, numerical maximum or external theorem
is used. This does not assert an effective argmax onset, full B3 PASS,
far-phase comparison or exclusion for other center classes.

The normalizations coincide: both use the corrected even-checkerboard
PD-T101 kernel, exceptional cos(alpha) mode and the same periodic
primitive S_n(alpha,beta). Reindexing the periodic grid by a complementary
center J+q odd leaves this S_n unchanged; separate phase evenness gives
S_n(alpha,beta)=S_n(alpha,|beta|). The physical class/parity/inward
conventions are exactly N5-two-phase-defect.md.

## Proof

N5-04 gives lambda<S_n-1/2048 for n>=64 on this domain.
N1-15 gives |S_n-M_near|<3/14000 for n>=10^6. Thus

    lambda < S_n-1/2048
           < M_near+3/14000-1/2048
           = M_near-491/1792000.

The exact positive difference491/1792000-1/4096=107/3584000
proves (1); inserting (2) proves (3). No additional model approximation
or the separate finite-cotangent N5 model is charged again.

## Scope, checks and next step

The coefficient evaluation count of M_near is independent of degree.
A validated implementation and proof of (2) over its phase/log-degree
parameters are future work. Neither values sampled at large n nor
small-error control alone establishes (2). True-corner treatment, other
noncorner classes, far phases and an effective onset for the full square
remain separate obligations. The finite bootstrap energy proof2..128
is not extrapolated to the analytic range n>=10^6.

2026-11-06, Codex coordinator assembly. Exact Fraction arithmetic checks
491/1792000 and107/3584000; no numerical optimization or fit. Source
N1-15 SHA ca3b98dc209a27fde2924ac9f4112111fe5be7b4e520d8b68ed0c8b20b50ea63,
N5-04 SHA de47e7d806f6c4d5107148516c7bec6686ba27c60b1d872572564ec94b7e0646.
Supplementary final assembly review is requested separately. Required
Claude audit remains separate.
