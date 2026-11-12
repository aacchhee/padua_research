# D1 primary-source coverage — 2026-11-12

Codex, assigned gpt-6.1-sol xhigh. Repository gate at input `04ef28b6139ad15b8cfc31f865c7bb9ba0d56d9b` preceded opening these PDFs. Sources remain **LITERATURE**, not locally checked source proofs. Exact versioned URLs identify artifacts; the web reader exposed parsed PDF text/page counts, not downloadable PDF bytes, so full-PDF SHA256/byte sizes are unavailable. No hash is fabricated. D5 owns consolidation into the topic source ledger.

## LIT?padua-3d-20261106-codex-D1-GL — Greenfeld–Lev

[arXiv1602.08854v2](https://arxiv.org/pdf/1602.08854v2), dated 1 June 2017, 39 PDF pages; *Fuglede's spectral set conjecture for convex polytopes*, Analysis & PDE 10 (2017), 1497–1538 (journal metadata supplied by D5; journal PDF not independently compared here).

Actually read: opening definition and Theorems 1.1/1.2, printed pp1–3. Spectrum means a countable complete orthogonal system exp(2pi i lambda.x) in Lebesgue L2(Omega). Theorem1.1 requires every facet of a spectral convex polytope in R^d to be centrally symmetric. Theorem1.2 makes a spectral convex polytope in R^3 a translational tile. Source proofs and later sections were not checked.

Application checked locally: O={|x|_1<=1} is a full-dimensional bounded convex polytope. Its facet with nonnegative coordinates is conv(e1,e2,e3), a triangle. A centrally symmetric polygon pairs distinct vertices under a half-turn, hence has an even number of vertices; this triangle is not centrally symmetric. Therefore GL1.1 alone implies O is not spectral. Completeness must first be established by the local D1 argument; mere orthogonality does not meet the theorem's hypothesis.

## LIT?padua-3d-20261106-codex-D1-LM — Lev–Matolcsi

[arXiv1904.12262v4](https://arxiv.org/pdf/1904.12262v4), dated 2 July 2022, 29 PDF pages; *The Fuglede conjecture for convex domains is true in all dimensions*, Acta Mathematica 228 (2022),385–420 (journal PDF not compared).

Actually read: definition, Theorem1.1 and geometric conditions in the introduction, printed pp1–3. With the same exponential/Lebesgue normalization, a spectral convex body must be a convex polytope admitting a lattice face-to-face translational tiling. The introduction also states the Venkov–McMullen facet condition. This independently corroborates the obstruction; GL1.1 is the shorter load-bearing import, so D1 need not import the tiling classification as an additional theorem. No LM proof is inherited.

## LIT?padua-3d-20261106-codex-D1-K — closest compactness precedent

[Kolountzakis, arXiv1606.02452](https://arxiv.org/pdf/1606.02452), 14 PDF pages. Actually read: packing/weak-convergence definitions and §2, Theorem1 and Lemmas1–5/proof, printed pp5–9. Theorem1 turns arbitrarily near-unit upper-density exact packings of a nonnegative integrable function of integral one into an exact tiling, under a positive-measure >1/2 condition. Its proof includes separation, compactness and integrated tail control. Our finite configurations are only asymptotically orthogonal, so this theorem cannot simply be applied to them. The density-to-completeness compactness principle is prior art; no novelty for that principle is claimed.

## LIT?padua-3d-20261106-codex-D1-AMO — closest kernel-limit precedent / disk control

[Antezana–Marzo–Ortega-Cerdà, arXiv2101.08064v1](https://arxiv.org/pdf/2101.08064v1), 17 PDF pages. Actually read: §3.4 context and Theorem14/proof, printed pp12–16; references for its kernel limit and ball obstruction. It excludes sequences of orthogonal reproducing-kernel bases on the unit ball in dimension >1 for the weights (1-|x|^2)^(a-1/2)dV, a>=0 in the surrounding setup. The proof rescales kernels, obtains an infinite orthogonal exponential set for a Euclidean ball, then invokes Fuglede's ball theorem. This is direct prior art for the blow-up mechanism. D1 differs by almost-critical redundant positive frames, and by exact Chebyshev torus unfolding; AMO supplies neither that extension nor general doubling-weight universality. Its cited source theorems are not locally checked here.

## Searches and limits

Additional actual primary reading during R4: [Marzo, arXiv:math/0611503v1](https://arxiv.org/pdf/math/0611503v1), parsed PDF25 pages, pp1–4: sphere harmonic/MZ/interpolation definitions, Theorems1.6/1.7. The density theorem is a necessary condition; the nonexistence statement explicitly excludes p=2. No spherical L2 cubature excess is imported. The served text carries both the arXiv2006 header and an internal August2021 date; no journal/version comparison was made.

[Kuperberg, arXiv:math/0405366](https://arxiv.org/pdf/math/0405366), parsed PDF15 pages: §3 Proposition3.1/Theorem3.2 p5, and §6 Theorem6.1/Corollary6.2/Scholium6.5 pp11–14, including the positive-island argument and local-density discussion. These are lattice and positive-cubature local-density precedents on their stated torus/simplex/uniform-polytope settings. No product-Chebyshev fixed-excess theorem was located in those statements; no source proof/constant is inherited. D5 owns bibliography consolidation.

Additional primary follow-through, on the supplemental reviewer's lead: versioned [math/0405366v2](https://arxiv.org/pdf/math/0405366v2), §7 printed p14, continuous Fourier-cubature paragraph. It explicitly formulates density minimization for periodic weighted Euclidean Fourier cubature and asks whether nonlattice rules improve lattice ones. This is close prior framing for a continuous limit; it does not state D1's Chebyshev fixed-excess conclusion. No new mechanism or additional research round follows.

Actual web queries: `cubature positive asymptotically Gaussian spectral sets Fuglede octahedron`; `orthogonal exponentials stationary point process critical density spectral set cubature`; `Marzo Ortega Cerda Pridhnani complete interpolation cubature asymptotic ball`; exact Kolountzakis title/arxiv; `cubature spectral Fuglede positive`; `orthogonal exponentials density spectral Kolountzakis compactness`. These bounded searches found the precedents above and the maximal-incomplete warning arXiv2410.12387 (search/abstract only, not a dependency). They do not establish priority or exhaustive literature absence. Sphere-specific coverage is coordinated with D5; a sphere/disk theorem is not imported into the cube proof.
