# N5-02 — Explicit actual-edge margin on a wider central phase window

2026-11-05. Developer: Codex, gpt-6.1-sol xhigh (assigned metadata).
Input/rules head: `714f3cad18859c07cd13f31561f2a185f9591a7f`.
Provisional theory label: `PD-T?argmax-bridge-codex-N5-02`.
Status at preregistration: OPEN. Current theory status: PROVED developer
claim, distinct review pending. Disposition: retained quantitative variant.

## Exact candidate

For every n>=32, m=n+1, vertical endpoint epsilon in {-1,1}, and
complementary center beta=q*pi/m with epsilon^n*(-1)^q=-1, put
phi=beta+s/m. Require phi in [11pi/24,13pi/24] and |s|<=r<=1/2.
The inherited exact identity is lambda_n(epsilon,cos phi)=S_n(s)-Delta.
Prove

`Delta >= d_n(r) = [c(r)/32](1-8/n)(1-8/m)`,
`c(r)=1/5-5r/16-r^2/20`.

Thus d_n(1/2)>1/2048 and d_n(1/4)>1/512. Combine with N1's frozen
primitive model error to give an explicit finite-n actual-lambda upper
bound in terms of a one-dimensional cotangent model. This candidate does
not assert corner dominance, whole-cell E-C, or a full R_cen gap.

## Closest entries and distinction

T185/T191 provide the two-half-kernel exact defect identity. T186 concerns
the exact complementary grid. T187–192 give the limiting central gap;
T192 has no explicit onset. T222's finite positive block covers phase
radius 1/8 and n>=48. T224/T366 handle all noncorner centers at smaller
radii. This is a **quantitative domain/constants variant** of their
existing mechanism, with no historical novelty claim. It restricts the
physical location to a central strip but widens the phase window to 1/2,
lowers the onset to n=32, and supplies a directly usable actual-lambda
margin after the fourth-order model error.

## Cheapest decisive gate and intended proof

Use physical second angles b in [pi/8,pi/4] and reflected first angles
u in the **open** interval (phi-pi/8,phi+pi/8). Both halves then have
opposite, nonzero denominators. Bound both numerators below by c(r),
count physical rows and the correct first-grid parity, and retain the
two-copy normalization exactly. Kill the candidate if the resulting
bound loses the asserted radius, effective onset or constants, or if
only the primitive S is bounded. No finite ordering scan is a test.

The constants above were proposed after reading the predecessors and an
informal central-rectangle calculation, before a new proof file or
numerical experiment. This is an informed preregistration, not a blind
prediction. Verification will test finite algebra/counts and representative
direct polynomial values, without inferring an all-degree result from
samples. Independent review belongs to the parent.

## Considered routes and dispositions

| Route | Disposition and scoped reason |
|---|---|
| Actual-lambda partial fractions after combining H+ and H- | deferred: the numerator is quadratic in cos u, so sign blocks look tractable, but no useful constant or ordering consequence has been derived. N1 owns primitive full-profile compactification. Resume only with a comparison advantage over that model. |
| Swapped vertical primitive rows and zero signed interior-row sums | deferred interface sent to N1; an identity alone does not meet the round's new-information criterion. |
| Stronger central two-copy defect for radius 1/4 only | consolidated into the parameterized radius <=1/2 candidate; its sharper 1/512 floor is retained as a corollary. |
| Transfer of unread classical endpoint-ordering proof | deferred unchanged: source records are reports, not fulltext read by N5. No external proof is imported. |
| Equal-phase E-P continuation | excluded by N080; its counterexample does not reject E-C. |

## Limits and next obligation

Outside this phase window the actual-edge comparison remains OPEN.
Even within it, a corner comparison still requires the one-dimensional
model's excess to be less than the explicit remaining defect margin.
The parent must publish this round before any new N5 round.

## Gate outcome and verification

The analytic proof survived the stated gate, including the entire radius
1/2 window, n=32 onset, both reflected endpoint parities, open collision-free
bands and exact physical weights. It is written in
`../theory/N5-central-edge-defect.md`. Applying the N1/N5 model error gives
actual lambda<M_n(0,s)-31/65536 on |s|<=1/2, with the sharper subtraction
127/65536 on |s|<=1/4. The fixed-rectangle obstruction beyond the window is
preserved in that file; no larger theorem is rejected.

Six supplementary 80-digit finite-polynomial cases passed, at n=32,33,48,64
and both endpoints/phase signs. A separate odd-periodic-board evaluation
agreed with the physical two-copy primitive to less than 1e-77. Exact
rational assertions checked the floor/error constants. These diagnostics
do not establish corner dominance or whole-cell order. The short evidence
receipt is `../evidence/n5-central-edge-defect.json`; full case values stay
in the parent's specified local-output area. An initial diagnostic failed
because Python converted interior physical weights to binary floats;
making those weights mpmath values fixed that implementation error before
the passing run. This did not change the written analytic claim.
