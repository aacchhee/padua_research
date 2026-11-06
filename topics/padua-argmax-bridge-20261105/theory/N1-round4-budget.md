# PD-N?argmax-bridge-codex-N1-01 — Floor of the unmodified error certificate

ID kind: PD-N. Aliases: independent-error assembly floor; R-balancing
obstruction. Split from: the budget test in IDEA?argmax-bridge-codex-N1-04.
Split into: none.

## Exact negative statement

Consider the proposed certificate that adds N1-02's error E_(n,R) to
N1-08's endpoint error e4, without any cancellation between their error
estimates. Other errors, if included, are nonnegative. For every
admissible n,R with n<=10^6, at alpha=beta=0 this **upper-bound formula**
is strictly greater than 3/50. Consequently it cannot certify the B3
half-margin requirement for a comparison margin gamma<=3/25, regardless
of how R is chosen, even if every other error were zero.

This is not a lower bound on the true model error. It does not refute
H4, the logarithmic profile, or a comparison with a separately proved
larger margin. Its scope is exactly the unchanged sum of the two stated
error estimates and the indicated numerical budget.

## Status, assumptions and dependencies

Overall status: **PROVED**, elementary analytic budget obstruction.
Candidate disposition: **REJECTED: failed** only for this unmodified
certificate at gamma<=3/25 through degree 10^6. The broader N1 target
remains OPEN. Dependencies: the explicit nonnegative error formulas in
N1-02, N1-07 and N1-08. No measurement or source theorem is a premise.

## Proof

At alpha=beta=0, a=1 and P=0. N1-02's stated error is
2(n+1)/(n(R-1))>2/R. N1-07's stated e_rows, a nonnegative component of
N1-08's e4, is at least (2R-1)*10R/n>=15R^2/n for R>=2. Hence the
unchanged sum of upper bounds is at least

    2/R+15R^2/n >=3*(15/n)^(1/3)>6/n^(1/3)>=3/50.

The middle inequality is arithmetic-geometric mean applied to
1/R,1/R,15R^2/n; the last uses n<=10^6. If gamma<=3/25 then
gamma/2<=3/50, proving the stated certificate failure. The inequalities
hold for every admissible R, including choices depending on n.

## Consequence and limits

More precision, a different R, further phase samples or completion of
the currently missing nonnegative error terms cannot repair this scoped
failure. A viable continuation must improve at least one of these two
estimates jointly, or prove a comparison margin exceeding this budget.
One retained repair is an explicit pole-jump/sawtooth correction to the
coarse cancellation quadrature before adding the finite-row remainder.
That repair is unproved and untested here; it must be gated and defined
before further development. The original one-correction limit remains.

The comparison margin for the eventual full model is not established by
this record. Sparse conservative B1 margins are diagnostics, and the
larger projected class margin is also not promoted to a proof. Thus this
scoped obstruction is not an unconditional whole-campaign B3 verdict.
No effective onset or B4 release follows.

## Checks and history

No mathematical computation, optimization or fit was run. This exact
calculation is the preregistered budget test after the H4 proof, not a
new mechanism search. Distinct review is pending. 2026-11-06, round 4
after bda45a4; Codex requested gpt-6-astra ultra.
