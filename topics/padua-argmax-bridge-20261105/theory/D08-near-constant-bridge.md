# PD-T?argmax-bridge-codex-D08-bridge — Limiting constant bridge from the frozen near model

ID kind: PD-T. Aliases: old near model used only at infinity; exact
log-coefficient matching; uniform finite-part transfer.
Split from: D08 near comparison. Split into: none.

## Statement

On the full closed signed near domain |alpha|+|beta|<=1/2, let
C_infty be precisely D02's completed primitive constant and let T
be exactly the phase-only limiting function defined in
C02-near-explicit-onset.md equation(3). It retains the OLD near
model's R128,delta1/1000,J4096 and jump constants. Set

    eta0=12989329736187619160983471/
                         38345245772322816000000000000<1/1000.

Then uniformly in that domain,

    |C_infty(phi)-T(phi)|<=eta0,
    C_infty(phi)-C_infty(0)
                          <=T(phi)-T(0)+2eta0.        (1)

Status: **PROVED**, analytic limiting consequence, distinct review
pending. This makes NO finite-n assertion about M_near below its
old degree floors. No near model term/correction or cutoff is changed.

## Dependencies and proof

N1-16's exact coefficient extraction gives the old near model
M_near=B_M L^2+b_M L+R_n, with B_M=4a/pi^2. Its proof equation(8)
identifies b_M=2D0+integral(f_L+f_R)/pi. The full-domain coefficient
integration of C06/D07-global-mesh has EXACTLY the same identity for
b_full. Equivalently their explicit U0/trigonometric formulas agree.
Thus B_M=B0 and b_M=b_full on this phase domain, without an
asymptotic matching assumption.

D02-far-uniform-limit.md proves that
S_n-B0 L^2-b_full L tends uniformly to C_infty. The accepted C02
degree-limit proof gives, for n>=1e6,

    |R_n-T|<2000000(L+1)/n,

so the old near residual tends uniformly to T. Finally C13-near-
representation.md's accepted proof equation(12) gives
|S_n-M_near|<eta0 for every n>=500000 on this exact near domain.
Use these statements ONLY along n->infinity through their overlapping
valid domain n>=1e6. Coefficient equality cancels both growing terms;
the difference tends uniformly to C_infty-T. Taking the limit gives
the non-strict first inequality in(1); applying it at phi and0 gives
the second.

No old finite representation, Q_n error, H8 approximation or fixed-strip
geometry is applied at40000 or50000. Fixed tail biases are permitted:
their possible limiting discrepancy is exactly the retained eta0.
In particular replacing <=eta0 by equality or zero is not justified.
Separate absolute phases are the exact inherited symmetry; the
unequal coordinate meshes are not interchanged.

## Checks and history

Pure analytic proof; no numerical execution is a premise. The old
fixed near-model phase function T and its C04 phase-only upper bound
are used in D08-near-comparison.md only after this constant bridge.
All original finite degree statements and their statuses remain intact.
2026-11-06, Codex Sol xhigh at parent request, input
`cbfdb044e184731984e3bf8be487008a86e68c37`. New split supporting
claim for the prospective D08 assembly; no historical novelty claim.


### Supplementary review closure — 2026-11-06

The preceding developer-frozen text is retained unchanged. Distinct Astra
xhigh reconstruction ACCEPTED this scope with no unresolved findings;
[independent-checks-D08-global.md](../independent-checks-D08-global.md),
audited report SHA256 `c3ceac020dd1654b8b5be8340c2436b343ab740ba24253be3eab1837f17c9316`.
The independently executed scalar check confirms the failed40000 and
passed50000 budgets. This closes the earlier pending supplementary review;
final Claude audit remains pending and no theorem scope changes here.
