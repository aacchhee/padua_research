# PD-T?padua-3d-20261106-codex-D1-06 — general doubling-weight extension

ID kind: PD-T. Aliases: frontier S2 I2; D1 general weights.
Split from: C1's optional general-doubling extension, kept separate from the solved Chebyshev target.
Split into: D1-05 proves only the fixed inverse-polynomial Chebyshev subclass.

## Statement retained and interpretation

Target: for a fixed probability weight nu on the full cube, positive almost everywhere and doubling, prove that there are gamma_nu>0 and n_nu such that every positive degree-(2n-1) nu-rule has N>=(1+gamma_nu)binom(n+2,3) for n>=n_nu.

Here doubling means nu(B(x,2r) intersect cube)<=C nu(B(x,r) intersect cube) for every x in the cube and r>0. Full cube support and polynomial positive definiteness are explicit. Neither the meaning 'doubling only for centers in support' nor arbitrary singular measures is silently substituted.

## Status, dependencies and outcome

Overall status: **OPEN**. Supporting exact defect identity D1-01 holds for any polynomial-positive-definite nu. D1-05 closes a bounded subclass. These supporting results do not turn this undecomposed general target PARTIAL. No universal negative theorem and no rejected general-weight candidate are claimed. R4 stops at the named missing local-limit obligations below.

## Actual bounded attempt

For a hypothetical nearcritical sequence, the polynomial projection still has q_i=w_i K_nu(x_i,x_i), sum(1-q_i)=N-dim Pi_(n-1), and good normalized polynomial kernels become pairwise nearly orthogonal by the same projection row identity. The exact torus step now fails: independent sign averaging gives Chebyshev products, but their nu-integrals need not be Haar Fourier moments. Thus the full-frequency Fourier matrix used in D1-01 is not an isometry. Doubling alone is not a replacement proof of that identity.

A precise sufficient replacement would be the following pair of obligations, for every hypothetical nearcritical sequence of nu-rules. These are unverified hypotheses, not conclusions:

**H1 (retained bulk count).** There exist rho_n->0 with n rho_n->infinity such that all but o(n^3) of its high-leverage nodes have angular coordinates theta=arccos x in [rho_n,pi-rho_n]^3.

**H2 (uniform normalized angular kernel limit).** For every fixed R, uniformly for centers theta in that retained angular bulk and u,v in B_R, the normalized nu-kernel at cos(theta+2pi u/n), cos(theta+2pi v/n) tends to

    F(u-v)=|O|^(-1) integral_O exp(2pi i (u-v).xi) dxi.

Only pairs with both arguments in the cube are required; n rho_n->infinity makes that automatic on fixed windows. The kernel is normalized by the square root of its two diagonal values, and degree is n-1. An x-dependent non-octahedral limit does not meet H2.

With H1/H2, remove bad/boundary nodes, reflect the remaining angles, and periodize after scaling by n/(2pi). There are 8(1+o(1))dim Pi_(n-1) points per period cell. Reflections of an individual bulk node are far apart at this scale; close pairs from distinct nodes inherit the projection near-orthogonality and H2. The separation/local-orthogonality and stationary mean-count proof of D1-02 then applies, followed by D1-03 and GL1.1. This is a **CONDITIONAL route on H1/H2**; neither H1 nor H2 has been established here from the stated doubling assumption. In particular a pointwise fixed-center universality citation would not by itself verify the uniform moving-center H2 or the boundary count H1.

The cheapest successful bounded test was exact polynomial reweighting: it proves D1-05 for nu=c mu_Cheb/p, p fixed positive polynomial. A proposed approximate reweighting/near-Parseval continuation for more general multipliers was considered and deferred; it would need its own complete Gram/defect error analysis. No such analysis or further mechanism run was started.

## Cheap assumption checks

If 'general doubling' means any measure doubling on its support without positive definiteness/full support, the literal universal extension is false: a point mass is doubling with constant one and has an exact one-node positive rule in every degree. Its polynomial inner product is degenerate, so D1-01's hypothesis fails. This is an interpretation check, not a refutation of the full-support target above.

Polynomial positive definiteness alone also does not force full cube support. For example the uniform parameter measure on

    t -> (t/2, exp(t-1)/2, exp(sqrt(2)(t-1))/2),   0<=t<=1,

is supported on a bi-Lipschitz curve inside the cube and is doubling on that support. Every nonzero polynomial has positive squared integral: its restriction is a finite sum of polynomial-in-t coefficients times exp((j+sqrt(2)k)t), with distinct real exponents. Such functions are linearly independent (analytic continuation and elimination of the largest exponent at t->infinity prove this), so the restriction is not identically zero. This example only disproves an implicit support inference; it is not claimed to violate the cubature lower bound. It cannot supply H2's 3-D angular bulk limit merely from the word doubling.

Li–Xu's exact Gaussian families on the A3 orbit-space domain are another reason to state the domain. D5 read the actual nonlinear domain/weight formulas but no doubling premise; they are therefore not asserted as a doubling counterexample on the cube.

## Sources, next unresolved step and history

AMO's weighted-ball kernel theorem and its cited Kroo–Lubinsky universality are coverage-qualified in sources.md; neither is a cube theorem. No source establishes H1/H2 here. Next step, only if separately authorized: prove both obligations for a precisely specified cube weight class, or develop the separately preregistered approximate reweighting variant. No computation. R4 after `f7caf42`/root GO, Codex assigned gpt-6.1-sol xhigh, 2026-11-12.
