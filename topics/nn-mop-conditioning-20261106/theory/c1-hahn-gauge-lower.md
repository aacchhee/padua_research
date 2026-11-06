# PD-T?nn-mop-cond-codex-C1-07 — all-N Hahn lower survives diagonal gauges

ID kind: PD-T. Aliases: Hahn invariant diagonal lower; base-two gauge
corollary; fixed-mass terminal witness; algebraic terminal-row gauge lower.
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

### Stronger dated corollary — 2026-11-06

The subsequent terminal parity-row theorem C2-04 in
`c2-hahn-terminal-rate.md` strengthens the lower root base for both gauge
infima to

    liminf_(N->infinity) K_dep,N^(1/N) >= rho_H,
    liminf_(N->infinity) K_fix,N^(1/N) >= rho_H,
    rho_H=(7+3sqrt(3)+sqrt((7+3sqrt(3))^2-4))/2
          =12.1136005841... .

The radical is the exact value; the decimal is rounded. The same
quantifiers over positive frozen gauges and local positive C1 sections,
field scales, and listed node/log-weight input variants apply. This
stronger lower base also holds for separately fixed masses.

More explicitly, for N>=3 and the positive integer A_M defined in C2-04,
every gauge has condition at least A_M/[27M(2M+3)] with independent
relative weights, and at least A_M/[54M(2M+3)] with fixed masses.
These are also lower bounds for the corresponding infima. The original
base-two inequality above remains a valid simpler bound, including N2.
This corollary supplies no matching full-map upper or equality of a
full-map rate, and makes no step-line conditioning claim.

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

For the stronger dated corollary, C2-04 uses the balanced terminal index
nu=(ceil(M/2),floor(M/2)) and the second relative-weight parity direction
eta_k=(-1)^k, with nodes and first weights fixed. It proves that this
single terminal b2 row has response at least A_M/[27M(2M+3)] in the
declared fieldwise metric, with A_M^(1/M)->rho_H. The b2 function,
derivative and scale remain identical in every C1 gauge, so the same
response bounds each gauge's condition and therefore its infimum.

For fixed masses the C2-04 direction subtracts its weighted mean c0 and
divides by 1+|c0|<=2. A constant relative-weight direction is a null
direction of b2, irrespective of the gauge. The adjusted direction thus
has zero mass and input norm at most one, losing at most a factor two
in this row response. This argument does not require other fields of an
input-dependent gauge to be null in the constant direction. No node
changes are used, and natural log weights give the same first-order
relative-weight tangent. Finally M=N-1 and all denominator and factor-two
losses have Nth root tending to one, proving both stated liminf bounds.

## Checks, sources and scope

No numerical premise or new external source is imported. The producer
and supplementary checks of the C2 normality and witness identities are
recorded in their own files; this corollary neither reproduces nor
independently approves those proofs. C1's gauge algebra has a separate
supplementary review. For the stronger corollary, read the complete
C2-04 proof and `independent-checks-02.md`: that check independently
reconstructs the all-M row comparison, both parities, fixed-mass transfer
and coefficient-root argument, with exact finite checks supporting its
identities. No numerical rerun is needed for this invariant-field
inference. Historical pre-response scope: the full Hahn map's sharp base,
a matching upper, exact finite gauge optimizer, finite-error radius and
algorithm stability remained open; the dated addendum below updates only
the b-dominant benchmark gauge optimizer.

## History

2026-11-06, Codex gpt-6.1-sol xhigh, rules/input snapshot
`b4a04981d42c7cd872957facf5e3995e4096ca67`. Added within productive
round3 after reading the completed C2 all-N normality and lower proofs;
no additional numerical sweep or independent candidate mechanism.

2026-11-06 continuation: after C2-04 and its focused independent check
were finalized, appended the stronger rho_H gauge-infimum lower as a
direct consequence of the same invariant b2 field. Preserved the earlier
base-two bound and its provenance; no other C1 file, numerical output,
shared record or Git state was changed in this continuation.

2026-11-06 audit-02 addendum: [response-gauge-infimum.md](response-gauge-infimum.md) proves finite positive attainment of the exact b-field lower for both b-dominant benchmarks, for all N>=2 in all six stated input models. The generic non-dominant optimizer problem remains OPEN.
