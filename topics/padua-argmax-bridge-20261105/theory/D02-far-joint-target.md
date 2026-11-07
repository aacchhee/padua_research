# PD-T?argmax-bridge-codex-D02-far-target — Practical joint finite-h error

ID kind: PD-T. Aliases: phase-local far error; bias-retaining small-degree
contract; signed geometry cancellation. Split from: none; original D02
objective. Split into: D02-far-bias, D02-far-limit and D02-far-boundary are
separate supporting results, not conjuncts of this target.

## Exact target and status

**OPEN.** For the corrected odd-board primitive on the full closed signed
phase diamond and the unchanged R64,delta=.01 M_far, establish explicit
phase-box constants C(B), C2(B) and a useful small N such that

    |S_n(phi)-M_far(phi,log n)-beta_(64,.01)(phi)|
        <=C(B)(1+log n)/n+C2(B)/n^2,
    every phi in B, every integer n>=N, both parities.        (1)

The exact beta is the signed functional in D02-far-bias-identity.md.
An equally acceptable form bounds S_n-M_infty, where the newly declared
M_infty includes that bias. No extra correction of the near model is
allowed or needed in this statement. The relevant practical far goal is
N around 10^2–10^3 with an error below the rigorously validated phase
margin, not merely an unspecified finite constant or asymptotic order.
A phase-relative form may directly bound

    [S_n(phi)-S_n(0)]-[M_infty(phi,log n)-M_infty(0,log n)],

retaining both signs and allowing S_n(0)=Lambda_c. Its constant and degree
quantifiers still require proof. No sampled error is such a bound.

## What is proved and what remains

The separate bias identity proves an exact continuous full-phase constant
and its cutoff representation. D02-far-uniform-limit identifies it as the
true uniform constant and supplies a fully explicit auxiliary-parameter
bound valid under its actual degree floor. D02-far-boundary-identity gives
(1) on the entire a=0 boundary with C=2sin(alpha)/pi and an O(n^-4) remainder.
These are supporting results. They do not resolve the open interior rate
or yield a practical onset, so the present target is OPEN, not PARTIAL.

The parameter-bound proof still charges the row cancellation by
2a/(R-1), the finite endpoint rows by R^2(1+L)/n+R^4/n^2 and the strip
residual by Q(P,delta). It cannot be presented as a joint C(1+L)/n estimate
by simply choosing fixed R,delta: its positive bounds then have floors.
This is an incompleteness of that bound, not a new negative theorem about
the true residual or the possibility of a joint estimate.

The next decisive obligation is a normalized comparison joining the
actual endpoint rows, ordinary cancellation quadrature and continuous
endpoint finite part before taking absolute values. At finite n its
special/collision rows and moving zeros must be retained exactly. A
prospective bounded check may subtract the now proved beta from D01's
existing twelve values, but cannot establish (1), a uniform constant or
any additional degree certificate. P1's validated margin run still lacks
the sharp error-side premise. P2 h-Taylor and P5 analytic first-order
coefficient routes remain deferred alternatives; no fit is adopted.

## Assumptions, checks and history

Use the exact definitions and dependencies in the three proved support
files; all old C06/C13/N1-15 bytes and their quantifiers remain unchanged.
No historical novelty claim, numerical proof or new argmax range follows.
No CPU diagnostic is a premise. Distinct supplementary review and later
formal Claude audit are pending tasks, not approval by this developer.

2026-11-06, rules/input 084a64f6465956f9c75b5538f83752c30318f151;
Codex parent-requested Astra ultra with prospective LOG justification,
serving metadata unexposed. Candidate and alternatives retained in
ideas/D02-far-joint.md.
