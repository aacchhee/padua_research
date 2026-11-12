# PD-T?padua-3d-20261106-codex-D1-05 — fixed inverse-polynomial weight changes

ID kind: PD-T. Aliases: D1 fixed Christoffel reweighting.
Split from: a bounded subclass of the separately OPEN general-weight target.
Split into: none.

## Statement, definitions and assumptions

Let mu be normalized product Chebyshev measure on [-1,1]^3. Fix a real polynomial p that is strictly positive everywhere on the closed cube, write k=deg p, and normalize nu=c mu/p to a probability measure, c=(integral (1/p) dmu)^(-1). There exist gamma_p>0 and n_p such that every positive degree-(2n-1) rule for nu with all nodes in the closed cube [-1,1]^3, n>=n_p, has

    N >= (1+gamma_p) binom(n+2,3).

These measures have full cube support, positive density almost everywhere, and are doubling relative to Euclidean balls intersected with the cube. This is a bounded subclass, not the general doubling conclusion.

## Status and dependencies

Overall status: **PROVED with explicit LITERATURE dependency**, inherited explicitly through D1-04 and its Greenfeld–Lev dependency. The transfer itself is elementary and exact. No new local universality theorem or mechanism is imported. This is the routine polynomial measure-change variant of D1, not a novelty claim.

## Proof

For a positive nu-rule with all nodes x_i in the closed cube [-1,1]^3 and masses w_i, set v_i=p(x_i)w_i/c>0. Exactness gives

    sum v_i q(x_i)=integral q dmu

for every polynomial q of degree <=2n-1-k. Thus, for r=n-ceil(k/2)>=1, the same nodes with masses v_i form a positive Chebyshev rule exact through 2r-1. The masses sum to one by q=1. D1-04 gives N>=(1+gamma)binom(r+2,3) once r>=n0. Since k is fixed, binom(r+2,3)/binom(n+2,3)->1. For all sufficiently large n this lower bound is at least (1+gamma/2)binom(n+2,3). Take gamma_p=gamma/2 and enlarge n_p. The constants remain non-effective because those in D1-04 are.

For the doubling statement, the 1-D arcsine mass of [x-r,x+r] intersected with [-1,1] is comparable, uniformly in x and 0<r<=2, to r/sqrt(1-|x|+r). This follows by integrating the endpoint-comparable density (1-|t|)^(-1/2); near an endpoint its integral is a difference of square roots, and away from endpoints the density is comparable on the interval. This expression changes by a bounded factor under r->2r. Products are doubling on coordinate boxes. Euclidean balls lie between coordinate boxes of radii r/sqrt(3) and r, so the product is doubling on intersected balls as well, by a finite number of box doublings. Finally min p>0 and max p<infinity make nu and mu boundedly comparable; bounded positive density changes preserve a doubling constant. QED.

## Limitations and history

No arbitrary continuous multiplier, Jacobi parameter class, vanishing-density class or general doubling family is claimed. The broad extension remains OPEN in general-weight-open.md. No numerical work. This routine exact reweighting corollary was developed in the authorized R4 general-weight attempt after publication `f7caf42` and root GO, Codex assigned gpt-6.1-sol xhigh, 2026-11-12.

2026-11-12, response-05, Codex assigned gpt-6.1-sol high: made all-node membership in the closed cube explicit in the statement and transfer setup (H1; audit-05 D1a-F1). Previously it was implicit in "rule for nu". Positivity of p is assumed only on that cube, and the same nodes pass to D1-04. This statement clarification preserves the fixed-p hypothesis, exactness loss, proof and status and is submitted for focused re-audit.
