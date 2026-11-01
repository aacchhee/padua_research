# PD-T?lattice-c1-codex-01 — Complete six-node quadratic criterion with a mixed-axis residual

ID kind: PD-T. Aliases: rowwise two-root sums; adjacent-mod4 n2 criterion.
Split from: none. Split into: pure-axis-product failure PD-N?lattice-c1-codex-01 is a separate negative statement.

## Statement

Let K be any field. Let x0,x1,x2 be distinct, and let each row r contain two distinct y values u_r,v_r. Order the six points `(x0,u0),(x0,v0),(x1,u1),(x1,v1),(x2,u2),(x2,v2)`, with columns `1,x,x²,y,xy,y²`. Put s_r=u_r+v_r, ΔX=product_(r<t)(x_t-x_r), and R=det of the3x3 matrix with rows `(1,x_r,s_r)`. Then

`det V = -ΔX * product_(r=0)^2(v_r-u_r) * R`.

Consequently the six nodes are unisolvent for Pi_2 if and only if the three root sums are not the values of an affine function of x. The identity and iff hold over every field, including characteristic2. In the phase0 mod4 union, `(u0,v0)=(y0,y1)`, `(u1,v1)=(y0,y3)`, `(u2,v2)=(y2,y3)` for four distinct y labels. The generic determinant is a nonzero polynomial over every field; over any infinite field the unisolvent specializations form a nonempty Zariski-open set.

For shifted adjacent unions at n2 the same identity holds with the selected pairs, ordered by increasing y index: phase1 has pairs `(y1,y2),(y0,y1),(y0,y3)`; phase3 has pairs `(y0,y3),(y2,y3),(y1,y2)`. Phase2 has pairs `(y2,y3),(y1,y2),(y0,y1)`. These are applications of the same theorem, not new generic mechanisms.

## Definitions and assumptions

Pi_2 is the full6-dimensional total-degree<=2 polynomial space. Cross-axis coordinate coincidences are allowed. Within each row distinct roots and distinct x are the exact nonzero-factor hypotheses; no real order or positivity is assumed. In the mod4 application all y labels are distinct. Generic means formal nonvanishing, and nonempty open specializations over an infinite field; this is not a claim that every finite field has enough suitable rational labels.

## Status by part

Overall status: PROVED (developer-written proof; independent Astra reconstruction pending; no self-acceptance).

| Part | Status | Evidence |
|---|---|---|
| Determinant and complete iff | PROVED | Row elimination and independent kernel argument below |
| Generic formal nonvanishing | PROVED | Explicit polynomial coefficients below |

## Depends on

Elementary determinant row operations and univariate interpolation at3distinct x values; no charter or published theorem is imported.

## Proof

Subtract each first row of a pair from its second row and divide the latter by v_r-u_r. The latter becomes `(0,0,0,1,x_r,s_r)`. Move these three rows after the three first rows. The permutation has3inversions, so determinant sign is-1, in every characteristic. The resulting block-upper-triangular matrix has top-left block `(1,x_r,x_r²)` and lower-right block `(1,x_r,s_r)`. Undoing the extracted factors proves the formula, since the first block determinant is ΔX. All extracted factors are nonzero under the hypotheses, proving the iff.

For a direct kernel check write `f=A*y²+(B*x+C)*y+q(x)` with deg q<=2. Vanishing at both row roots forces `B*x_r+C=-A*s_r` and `q(x_r)=A*u_r*v_r`. If A=0, three distinct x values force B=C=0 and then q=0. Thus a nonzero kernel requires A!=0, and its first condition is exactly that s is affine in x. Conversely, if s is affine, choose A=1 and B,C accordingly, then interpolate the three root products by the unique quadratic q; the resulting nonzero f vanishes at all six points.

For phase0, R expands as

`R=(x1-x0)*(y2+y3-y0-y1)-(x2-x0)*(y3-y1)`.

This polynomial has, for example, coefficient1 at x1*y2, so remains nonzero over every field. The factors ΔX and the three root differences are also nonzero polynomials. Their product is nonzero in the polynomial ring over any field. Its complement, intersected with all within-axis distinctness conditions, is a nonempty Zariski-open set over any infinite field: a finite product of nonzero polynomials does not vanish at every point of an infinite field, by induction on the number of variables. Shifted n2 pairs are obtained by permuting y labels and row labels, so have the same generic conclusion.

## Checks

`code/c1_mod4.py` verifies the exact sign/formula at four crossed rational examples and50seeded distinct integer-axis draws using Fraction Gaussian elimination. Those are supplementary finite checks, not the proof. Full commands/hashes in C1/rounds.md. The frozen row/column order and hypotheses were written in C1/frozen-scope.md before derivation. Independent Astra reconstruction pending.

## Sources and scope

Closest registry IDEA-012; primary inspection limits and pending Floater/DU/Camargo comparisons are in literature/lattice-unisolvence/candidate-screen.md. This is an elementary structural example, no novelty claim. Property(a) mod4 character-union periodic yes; property(b) complete mixed-axis criterion yes at n2, pure axis product disproved separately; property(c) no asymptotic Lebesgue result. General n is not proved by this rowwise quadratic argument.

## Open items and history

Independent reconstruction and finite checker rerun pending. A larger-n extension requires a degree-appropriate row-root/matrix criterion, stated separately.2026-10-31, Codex assigned gpt-6.1-sol xhigh, rules/source e949ef06895acd5463cdf8df7e0e5f795218f70f. Shifted phases added after root's explicit continuation and frozen before their numerical execution.

## Audit history addendum — 2026-11-01

The pre-acceptance pending wording above is historical. Supplementary [Astra reconstruction](../../../topics/lattice-unisolvence-20261031/independent/report.md) completed, and [Claude audit-01](../../../topics/lattice-unisolvence-20261031/audit-01.md) accepted this exact existing statement and epistemic status. [Response-01](../../../topics/lattice-unisolvence-20261031/response-01.md) changes audit/integration metadata only; no proof, hypothesis, status or finite observation is upgraded. Literature/novelty gaps remain unresolved where stated. Codex administrative response, requested gpt-6.1-sol high; runtime metadata unexposed.
