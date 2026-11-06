# PD-N?argmax-bridge-codex-D01-far-01 — Unchanged far model has no uniform vanishing error

ID kind: PD-N. Aliases: D01 T1-c fixed-strip obstruction; no uniform
C(L+1)/n remainder; midpoint cutoff bias.
Split from: the post-audit P1 uniformly vanishing remainder proposal.
Split into: PD-T?argmax-bridge-codex-D01-far-identity, the substantive
exact midpoint finite-n identity and limiting residue, in its own file.

## Statement

For the unchanged C06 M_far with R=64, delta=1/100, there are no
finite constants C,n0 such that, for every integer n>=n0 and every
phase |alpha|+|beta|<=pi,

    |S_n(alpha,beta)-M_far(alpha,beta,log n)|
         <= C*(1+log n)/n.                                  (1)

This is a scoped negative statement about the vanishing error form (1).
It leaves C06's fixed positive error bound, every frozen C13 statement,
and an estimate with a separately charged residual allowance intact.

## Definitions and assumptions

Use exactly the corrected polynomial, odd board, normalization and
fixed-count formula of C06-far-compact-error.md. Exact h_R,g_R constants
and exact retained-interior quadrature define M_far. Its fixed R and
delta are unchanged. All mathematical arithmetic is exact real arithmetic.

## Status by part

Overall status: **PROVED**, by the standalone midpoint identity below.
Distinct supplementary review and formal Claude audit are publication
obligations. Candidate disposition: the full-diamond vanishing error
form (1) is **REJECTED: refuted**. The P1 route allowing a fixed residual
term remains OPEN; no comparison or effective onset is inferred.

## Negative-result scope

Attempted mechanism: infer a uniform C(L+1)/n remainder for the
unchanged fixed-delta C06 model, as the artifact-only interpretation of
audit01 P1 T1-c. Parameter range: all sufficiently large integer n and
the full closed phase diamond. A single exact midpoint phase disproves
that universal estimate. No claim about arbitrary models or errors with
an additional nonzero residual allowance is made.

## Depends on and proof

[PD-T?argmax-bridge-codex-D01-far-identity](D01-far-midpoint-identity.md)
proves for every integer n>=2 that

    S_n(pi/2,pi/2)-M_far(pi/2,pi/2,log n)
       =b_delta+(2/pi)*log(1+1/n)+e_n,
    |e_n|<=1/[4*n^2*(n+1)^2],

where, with eps=delta/(2*pi),

    b_delta=(4/pi)*[(gamma-log pi)*eps
       +sum_{k>=1}zeta(2k+1)*eps^(2k+1)/(2k+1)]<0.

The left side therefore tends to a nonzero constant. The right side
of (1) tends to zero for each finite C, a contradiction. QED.

## Checks and scope

The proof has no numerical premise. The requested twelve-case signed
diagnostic is separately MEASURED and defined in
[SPEC](../code/post_audit_D01_far/SPEC.md). Its exact telescope is a
routine add-and-subtract identity, not another substantive theory result.
At every requested degree delta*m/pi<R, so the first/last R rows reach
outside the strip and the high-degree N1-08 component estimates do not
apply. The signed telescope remains valid with that explicit geometry.

Tighter quadrature and g_R-tail controls are implementation verification;
they are not needed to establish the negative limit. The exact midpoint
has a linear-in-delta residue at its phase cusp, so an O(delta^2) residual
cannot be assumed uniformly. The whole limiting discrepancy at the
interior phase (1.45,1.45) is not proved by this boundary theorem.

## Open items

Keep a justified nonzero residual allowance in any later unchanged-model
comparison. A fixed-strip tail is one diagnostic source; fixed-R endpoint
or cancellation effects may also survive. No correction, validated cover,
new degree certificate or improved threshold follows here.

## History

2026-11-06, Codex math subagent, parent-requested D01 work at input
`4cf68980fa0538b53e2aea7174ed6e5782a34908`; serving model/effort metadata
not independently exposed. Fresh gate: ideas/D01-far.md. The parent
explicitly requested the PD-T/PD-N split before distinct review because
the exact midpoint identity will be reused. The original combined
boundary derivation is preserved in that PD-T file, not relabeled.
