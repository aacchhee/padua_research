# D1 R4 reconstruction and mandatory consistency controls

2026-11-12, Codex assigned gpt-6.1-sol xhigh. Prospective R4 published/pushed at `f7caf42`; root GO preceded this reconstruction. This is developer reconstruction, not the assigned independent audit. No new numerical run.

## Proof-chain challenge

| Potential gap | Reconstruction and disposition |
|---|---|
| Boundary signs/collisions | Each cosine fiber is exactly one sign orbit; stabilizers have equal multiplicity. Weights are divided by distinct orbit size; different cube nodes have disjoint orbits. No assumption of eight images at a boundary node. |
| Critical lifted count | Rank gives m<=M; orbit size gives M<=8N; N/D->1 and m~8D squeeze M/m->1. No boundary equidistribution is assumed in the Chebyshev proof. |
| Deleting low leverage | Bad count <=(M-m)/epsilon=o(m), with epsilon=sqrt((M-m)/m)+1/n. Good count/m->1. |
| Pairwise rather than aggregate orthogonality | Each nonnegative row-sum term is bounded by the row sum. Cancellation yields |D/m|^2<=epsilon/(1-epsilon). |
| Uniform separation | Uniform compact Riemann-sum convergence makes F_n bounded below near zero. It applies to periodic copies because exp(2pi i k.z)=1. Same-atom copies are distance >=n. |
| Vague limit loses points/intensity | Deterministic limits can lose density. Random shifts give an exact expectation for every compact test; separation uniformly bounds compact-window counts, making that expectation continuous under weak convergence of laws. |
| Compactness/stationarity | X_b includes the empty measure. Distance-function diagonal compactness gives configuration compactness; continuous translations preserve weak limits of exactly stationary laws. No ergodicity is required. |
| Pairwise orthogonality in law | Continuous nonnegative local pair functionals converge uniformly to zero; a countable sequence of cutoffs covers every pair. Same-atom periodic copies are at least n apart, so for n greater than a fixed cutoff's diameter no such pair occurs in its H_f sum; all remaining pairs are covered by the distinct-atom row estimate. This makes the supplemental review's optional clarity note explicit without changing the R2 proof. |
| Tail escaping before completeness | No finite tail identity is passed to the limit. The limiting mean counting measure integrates |F|^2 by monotone convergence/Tonelli. |
| Incorrect Fourier factor | Coordinates lambda=n theta/(2pi); normalized F=(1/|O|)FT(1_O). Plancherel gives integral |F|^2=1/|O|. Intensity |O| makes the mean Bessel sum exactly one. |
| Uncountable probability intersection | Equality is first imposed for y in Q^3 only. Hilbert projection and continuity/Fourier uniqueness imply completeness for that single full-probability event. |
| Critical density alone | Not used. The mean-intensity identity plus exact orthogonality is stronger and is the actual hypothesis of D1-03. |
| Uniform excess quantifier | Negating existence of gamma,n0 gives n_r>=r and N_r<(1+1/r)D_r. Positivity gives the opposite N_r>=D_r, forcing ratio->1. |
| Nonspectral source application | O is a full-dimensional convex polytope with a triangular facet. GL1.1's complete-spectrum/Lebesgue normalization is exactly the output of D1-03. |

No unresolved Chebyshev local-limit/completeness gap was found in this reconstruction. The separate independent audit may still identify one; source proofs are not inherited. General doubling is OPEN at H1/H2 in general-weight-open.md.

## Exact 2-D Padua calibration

For d=2 let O_2={|x_1|+|x_2|<=1}. With

    B=[[1,1],[1,-1]],  O_2=B[-1/2,1/2]^2,
    Lambda=B^(-T)Z^2=(1/2)[[1,1],[1,-1]]Z^2,

the ordinary tensor Fourier basis on the square transports to a complete orthogonal exponential basis on O_2. Its intensity is |det B|=2=|O_2|. Thus D1-01/02/03 consistently allow a spectral diamond; the 3-D triangular-facet contradiction has no 2-D counterpart.

This calibration also matches the actual Padua torus groups. For the cyclic order 2n(n+1), angular generator (pi/n,pi/(n+1)), the full periodic scaled lift nH/(2pi)+nZ^2 has lattice basis

    (1,0), (1/2, n/(2(n+1))).

The first basis vector is obtained by 2(n+1) generator steps and subtracting the period (n,n); these vectors generate a lattice with exactly 2n(n+1) points per period cell, so they generate the whole lift. Its basis tends to (1,0),(1/2,1/2), a basis of Lambda above. Its density tends to two. In particular the local limit is admissible, not just a case left unexamined.

At finite n the polynomial defect sum is N-dim Pi_(n-1)=n+1; the torus sum is M-|A_n|=4n-1. The seven-case exact controls reproduce n2/3/4 Padua values 3/4/5 and 7/11/15, respectively. Root actually reran all seven rows separately and reported exact row agreement. These finite controls do not prove the asymptotic theorem.

## Disk and sphere primary consistency

**Disk/ball.** D1 directly read AMO arXiv2101.08064v1 §3.4, Theorem14/proof pp15–16. Its weighted-ball result excludes sequences of exact orthogonal reproducing-kernel bases; the proof takes a ball-kernel scaling limit and invokes nonexistence of infinite orthogonal ball exponentials. This is consistent with D1 and is close prior art, not a consequence of the cube proof. AMO's remark (p16) extends AMO's obstruction to an orthogonal nonbasis family when enough local points are present (the p15 sphere/tight-design remark is also AMO's; see the supplemental audit); it does not give our nearcritical positive-frame statement.

**Sphere.** D1 directly read Marzo's arXiv:math/0611503v1 pp1–4: the finite harmonic spaces, MZ/interpolation definitions, density Theorem1.6 and complete-interpolation Theorem1.7. The latter excludes p!=2 only. Therefore it cannot be used to assert an L2 spherical cubature gap, or to prove/contradict D1's claim. A uniformly stable Riesz sampling/interpolation family is not an orthogonal exponential spectrum. Positive tight spherical cubature would have a projection defect identity, but our exact Chebyshev reflection-to-Haar step is absent there. No new sphere/disk cubature theorem or 'all local bodies must tile' principle is asserted. The actual source comparison finds no contradiction with the cube theorem; a universal sphere extension remains unproved here.

**Other domains.** Li–Xu's all-dimensional Padua/Gaussian families live on a nonlinear A_d orbit-space domain. Their domain and polynomial-frequency dictionary differ; their existence does not meet the cube theorem's hypotheses. D5 checked the exact domain/weight formulas and reported no doubling premise. They are not recast as cube rules.

**Local-density predecessor.** D1 also directly read Kuperberg arXiv:math/0405366 §3 Proposition3.1/Theorem3.2 (printed p5) and §6 Theorem6.1/Corollary6.2/Scholium6.5 (printed pp11–14). They give lattice-design/packing equivalences and local net/density requirements for positive uniform-simplex/simple-polytope cubature. They do not state the product-Chebyshev fixed relative excess proved here. These are additional substantive precedents, with different measures and conclusions; no theorem or numerical constant is transferred.

On the supplemental reviewer's further lead, D1 actually read §7's continuous Fourier-cubature paragraph (versioned math/0405366v2, printed p14). Periodic weighted continuous density minimization is therefore also established prior framing. This reinforces the bounded novelty language and introduces no proof premise or mechanism reopening.

## Novelty and disposition

The source gate now includes actual AMO and Kolountzakis compactness proofs at the stated coverage. Kernel blow-up, density compactness and the spectral obstruction are prior mechanisms. The retained distinction is arbitrary nearcritical positive Chebyshev frames: defect pruning, stationary local-law intensity preservation and Bessel saturation complete the inherited C1 sketch. No historical-priority assertion is made. The root-supplied stationary translation lead is credited in the proof files.

Outcome: Chebyshev D1-04 and the bounded reweighting corollary D1-05 retain **PROVED with explicit LITERATURE dependency**; local D1-01/02/03 retain PROVED. General full-support doubling D1-06 remains OPEN with a conditional H1/H2 route. Stop successfully after four research rounds; no reason to consume rounds5/6, and no claim that the broader programme is exhausted.
