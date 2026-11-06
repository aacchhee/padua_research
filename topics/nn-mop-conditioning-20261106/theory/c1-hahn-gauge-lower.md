# PD-T?nn-mop-cond-codex-C1-07 — all-N Hahn lower survives diagonal gauges

ID kind: PD-T. Aliases: Hahn invariant diagonal lower; base-two gauge
corollary; fixed-mass terminal witness.
Split from: none. Split into: none.

## Statement

For the exact Hahn pair alpha1=1, alpha2=3/2, gamma=1 of
`c2-hahn-normality.md`, N>=2 nodes z_k=2k/(N-1)-1 and M=N-1, let
K_fix,N and K_dep,N be the full-NN fieldwise infima defined in
`c1-gauge-invariants.md`. Then both satisfy

    K_dep,N <= K_fix,N,
    K_dep,N >= 2^(M+1)
      /[M(2M+3) binom(M+4,4) (M+1)(2M+1)].

Consequently each infimum has Nth-root liminf at least2. The same
inequality holds for node scale one, natural-spacing node scale2/M,
componentwise-node scale |z_k|, separately fixed-mass weight tangents,
and natural log weights. The base2 is explicitly nonsharp. No balanced
step-line Hahn all-N rate follows from this terminal-index witness.

## Assumptions and status

Overall status: PROVED, direct corollary with no new mechanism.
The six rescaled NN fields, field-sup scales, frozen positive gauges and
local positive C1 sections are precisely those of C1-01. Normality and
positive field scales for every N>=2 come from C2-02; this is not an
inference from positivity alone. The result concerns unrestricted local
input perturbations rather than perturbations confined to Hahn parameters.

## Dependencies and proof

The separate written theorem `PD-T?nn-mop-cond-codex-C2-03` in
`c2-hahn-lower.md`, using the all-N normality result C2-02, constructs a
mass-zero relative-weight perturbation of the second measure, with no
node change, at nu=(M-1,1). Its terminal b2 response divided by the
upper field scale2M+3 is at least the displayed lower bound.

For every fixed gauge and every input-dependent C1 section, the whole
b2 field is the identical input function. Its derivative and field-sup
scale therefore agree with the monic values, by C1-01. The C2 witness
thus gives the same lower for every admissible gauge, hence for either
infimum. Its weight direction preserves mass and changes no nodes, so
it remains admissible in every listed restricted node box. Natural log
weights have the same first-order relative-weight tangent. Fixed gauges
form a subset of smooth sections, proving the order of the infima.
Finally, the denominator is polynomial in N, so its Nth root tends to
one and the displayed exponential term has Nth-root limit2.

## Checks, sources and scope

No numerical premise or new external source is imported. The producer
and supplementary checks of the C2 normality and witness identities are
recorded in their own files; this corollary neither reproduces nor
independently approves those proofs. C1's gauge algebra has a separate
supplementary review. The Hahn sharp base, a matching upper, exact finite
gauge optimizer, finite-error radius and algorithm stability remain open.

## History

2026-11-06, Codex gpt-6.1-sol xhigh, rules/input snapshot
`b4a04981d42c7cd872957facf5e3995e4096ca67`. Added within productive
round3 after reading the completed C2 all-N normality and lower proofs;
no additional numerical sweep or independent candidate mechanism.
