# PD-N?padua-xu-lebesgue-20261114-claude-30 — no vertex value of the Morrow–Patterson Lebesgue function equals (n+1)(n+2)/2

ID kind: PD-N.
Aliases: X2-N30; target T4(c) of round X2-2; flag F1 of `lit-notes/X2-sources.md`.
Split from: none.
Split into: none.

## Statement

Let d_n := (n+1)(n+2)/2 = dim Π_n. For every even n ≥ 2 and the Morrow–Patterson points MP_n (interpolation in Π_n):

(i) λ_n(1, −1) = λ_n(−1, −1) = n + 1 < d_n;
(ii) λ_n(1, 1) = λ_n(−1, 1) < d_n for n ∈ {2, 4}, and λ_n(1, 1) = λ_n(−1, 1) > d_n for every even n ≥ 6;
(iii) λ_n(±1, 1)/d_n → 2c* = 1.0339073… as n → ∞ (c* of X2-25); more precisely λ_n(±1,1) = 2c*·d_n + (2c* − 1)(n + 1) + 9c*/4 + R_n with −(0.4053 log²(n+2) + 2.9833 log(n+2) + 15.82) ≤ R_n ≤ 7.66.

So the reported identity "the computed corner values are (n+1)(n+2)/2" (BBDM, Constr. Approx. 63 (2026) §7 p. 63) holds at **no** vertex for **any** even n ≥ 2. What is true is (i)–(iii): the two lower vertex values are exactly n + 1, and the two upper vertex values are asymptotically 3.39% larger than d_n, crossing d_n between n = 4 and n = 6 (λ_2 = 5.8456 < 6, λ_4 = 14.8408 < 15, λ_6 = 28.0250 > 28).

## Definitions

As in X2-21, X2-25.

## Assumptions

n even, n ≥ 2; BBDM's node set.

## Status by part

Overall status: PROVED (analytic for (i), (iii) and for (ii) with n ≥ 42; computer-assisted by rigorous ball arithmetic for (ii) with n ≤ 40; independent rerun of the finite part pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (i) | PROVED | X2-22; n + 1 < (n+1)(n+2)/2 for n ≥ 1 |
| (ii), even n ≥ 42 | PROVED | X2-25 lower bound + monotonicity below |
| (ii), n ∈ {2, 4} and even 6 ≤ n ≤ 40 | PROVED, computer-assisted | ball-arithmetic enclosures of the closed form X2-23 (a) (`x2_corner_arb.py`); for n ≤ 30 also the independent path-A enclosures |
| (iii) | PROVED | X2-25 |

Candidate / claim disposition: REJECTED (the published numerical report of the corner values).
Rejection reason: refuted for every even n ≥ 2 at every vertex.

## Negative-result scope (PD-N only)

Attempted mechanism: the statement "λ_n(v) = (n+1)(n+2)/2 at the vertices v of the square" (numerical report in BBDM §7; `leb_mp_true` reference curve in their code).
Parameter range: every even n ≥ 2, all four vertices.

Not refuted: that (n+1)(n+2)/2 is a good *approximation* of λ_n(±1, 1) for moderate n (relative deviation −2.6% at n = 2, +1.4% at n = 10, +2.9% at n = 30, tending to +3.39%); BBDM's plotted comparison for n ≤ 30 ("almost overlapping") is consistent with this.

## Depends on

- X2-22, X2-23 (a), X2-25 (two-sided bound and enclosure of c*), X2-21 part 4.

## Checks

- `python3 code/mp/research/x2_corner_arb.py --nmax 60` (2026-11-14): `lt_dim_n2_n4: true`; `gt_dim_n>=6: true` for every even 6 ≤ n ≤ 60; λ_n(1,1) − d_n = −0.15444077, −0.15916453, +0.025027606, +0.38784525, +0.91845198, +1.6088138 for n = 2, …, 12 and +26.736967 at n = 40; `threshold_f(44)>0: true` (f(42) = −0.8918 < 0, so the analytic range starts at M = 44, n = 42).
- Path-A certificate `evidence/mp-cmp-certificate.json`: `claim_lam(1,1)_gt_(n+1)(n+2)/2` false for n = 2, 4 and true for n = 6, with enclosures of width 2e−45 (independent code path).
- Agreement with the published table CDMV 2005, Table 4 (values 649, 1264, 2082, 3102 at n = 34, 48, 62, 76; d_n = 630, 1225, 2016, 3003): LITERATURE, reproduced as upper-vertex values by the literature subagent (`lit-notes/X2-sources.md` §6.2); these published values already exceed d_n.
- Independent rerun: pending (auditor).

## Sources

- LITERATURE: BBDM, Constr. Approx. 63 (2026), §7 p. 63 and Fig. 4; Caliari–De Marchi–Vianello, Appl. Math. Comput. 165 (2005), Table 4 p. 271 (`lit-notes/X2-sources.md` §3).

## Proof or evidence

(i) is X2-22. (iii): by X2-25, λ_n(1,1) = c*(n+5/2)² − (n+1) + R_n, and (n+5/2)² = (n+1)(n+2) + 2(n+1) + 9/4, so c*(n+5/2)² = 2c*d_n + 2c*(n+1) + 9c*/4; divide by d_n.

(ii) Let M = n + 2, ℓ(M) = 0.4053 log²M + 2.9833 log M + 15.82. By X2-25, λ_n(1,1) − d_n ≥ c*(M+½)² − (M−1) − ℓ(M) − M(M−1)/2 = (c* − ½)M² + (c* − ½)M + c*/4 + 1 − ℓ(M) ≥ f(M) := 0.01695 M² + 0.01695 M + 0.51695/4 + 1 − ℓ(M), using c* ≥ 0.51695. f'(M) = 0.0339 M + 0.01695 − (0.8106 log M + 2.9833)/M, which at M = 44 is 1.371 > 0 and is increasing in M; f(44) > 0 by ball arithmetic (f(44) ≈ 1.78). Hence λ_n(1,1) > d_n for every even n ≥ 42. For n ∈ {2, 4} (λ_n < d_n) and for even 6 ≤ n ≤ 40 (λ_n > d_n) the strict inequalities are verified by rigorous enclosures of the closed form X2-23 (a). λ_n(−1,1) = λ_n(1,1) by X2-21 part 4. ∎

## Scope

Vertex values only, every even n ≥ 2.

## Open items

- Independent rerun of the finite range (auditor).

## History

- 2026-11-14, Claude Fable 5.2 (xhigh), researcher subagent of round X2-2; uncommitted at writing. First version.
