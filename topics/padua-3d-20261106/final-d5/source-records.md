# D5 R1 — primary and coverage-labelled literature records

2026-11-12. Reader: Codex, assigned gpt-6.1-sol xhigh; internal runtime metadata unexposed. Rules/input `04ef28b6139ad15b8cfc31f865c7bb9ba0d56d9b`; registered R1 authorized after root published `f9ab1c6`. Exact E4 imports have their separate [verification](e4-verification.md). All source facts below are **LITERATURE**, not locally proved source theorems. No final IDs or shared records allocated.

Access: actual web connector PDF text was inspected at the locators below. Local curl failed at sandbox proxy and approved retry403; no local PDF artifact, PDF byte identity, or cold-storage delivery is claimed. Web snapshots are identified by durable URL/version and inspected page/theorem. Screenshots were attempted for ORSV and failed. The record contains authored paraphrases, not downloaded third-party text. The root LOG is the canonical timing disclosure for early source reconnaissance.

## LIT?padua-3d-20261106-codex-D5-04 — Li–Sun–Xu2009

[*Cubature formula and interpolation on the cubic domain*](https://arxiv.org/pdf/0808.0180v2), NMTMA2(2009),119–152, DOI10.4208/nmtma.2009.v2n2.p119. Actual coverage: intro pp1–3, §4 node definition/count and cubature pp14–16, Thm4.10–4.11 pp25–26, Cor4.12 p26. Preprint/journal versions not compared.

Cor4.12 gives `||Ln||<=C(log n)^3` for interpolation on Γn, roughly n³/4 nodes. Thm4.11 identifies its space as Π*n, the rhombic-dodecahedron positive-octant monomial space (pairwise degree sums at most n); it contains Πn and reaches total degree about3n/2. Thus the cube already has explicit polylog interpolation in a superspace, at asymptotic ratio3/2 to `dim Πn`.

The intro conjectures at least `n³/4+O(n²)` nodes for degree2n−1 cube cubature, in the surrounding product-Chebyshev setting. It leaves the n³/6 leading count as a question. This is not a proved node lower bound and is not an interpolation impossibility theorem. The intro allows real nonzero cubature weights; do not silently replace its conjecture with a verified positivity-only theorem. The construction is related to DMVX, which it cites as previously publishing/testing its cubature.

## LIT?padua-3d-20261106-codex-D5-05 — Li–Xu2010

[*Discrete Fourier analysis on fundamental domain of A_d lattice and on simplex in d-variables*](https://arxiv.org/pdf/0809.1079v1), JFAA16(2010),383–433. Actual coverage: §4.2 count(4.10) p26, Thms4.7–4.8 p28, §5 definitions, Thm5.10–5.11 pp36–37 and closing interpolation remark; Gaussian Thm5.8 statement. External proofs and journal version not checked.

On the orbit domain Δ*, with weight w^(−1/2), Thm5.10 gives degree2n−1 cubature on Yn of `binom(n+d,d)` nodes, including boundary. The closing remark identifies unique Πn interpolation there with Thm4.7's trigonometric interpolant; Thm4.8 gives the O(log^d n) norm. The variables are generalized elementary-symmetric exponential coordinates, not the original cube coordinates. Thm5.8 separately concerns Gaussian cubature for w^(1/2).

This is strong prior art for higher-dimensional Padua analogues on other domains; the note's target is specifically ordinary total degree on the cube. No transfer of this package to that target is proved by a change of terminology or a nonlinear coordinate map.

## LIT?padua-3d-20261106-codex-D5-06 — Wang–Wang–Wang2014

[*On the norm of the hyperinterpolation operator on the d-dimensional cube*](https://doi.org/10.1016/j.camwa.2014.07.009), Comput.Math.Appl.68(5),632–638. Author names reported in other bibliographies: Heping Wang, Kai Wang, Xiaoli Wang. Publisher URL `https://www.sciencedirect.com/science/article/pii/S0898122114003150` returned403. Exact-title/DOI/regularity/fulltext searches found metadata and snippets, no inspected theorem.

**Coverage: publisher search metadata/snippets only; exact theorem, positivity/exactness/regularity hypotheses and application unverified.** Prior source reports and Bos–De Marchi–Vianello describe a log^d hyperinterpolation norm result. It is a close attribution lead for T10, but this reading cannot identify T10's anisotropic rank-one-corrected least-squares projection with its operator or discharge a new dependency through it. T10 already has the independently checked Kolomoitsev–Lomako application. Obtain this paper before saying that this particular T10 operator is literally its theorem.

## LIT?padua-3d-20261106-codex-D5-07 — Gunzburger–Teckentrup

[*Optimal Point Sets for Total Degree Polynomial Interpolation in Moderate Dimensions*](https://arxiv.org/pdf/1407.3291v1). Actual coverage: intro, §2 definitions/conjecture, §4.1/Table1 p9. This is a numerical optimization study, not a proof of global optimality. For d=3 and n=1..5 the table reports 2.00,2.95,4.05,5.09,6.40. Use these as external **optimized numerical benchmarks**, not certified optima. Their log^d growth suggestion is conjectural. It is wrong to frame the topic's n4 value5.54 as the strongest external numerical benchmark; the source reports5.09.

## LIT?padua-3d-20261106-codex-D5-08 — Krieg–Pozharska–M.Ullrich–T.Ullrich

[*Sampling projections in the uniform norm*](https://arxiv.org/pdf/2401.02220v2), actual coverage pp1–3, Thms1–2, Remarks4–5 and Remark7. Every N-dimensional subspace of bounded functions on a set admits a sampling projection using2N evaluations with norm at most C√N. A fixed oversampling factor greater than1 is possible with its stated factor-dependent constant. The same order cannot be improved uniformly over arbitrary function spaces; exactly N samples can require linear order. This worst-case statement does not prove a √N lower barrier for cube polynomials. The intermediate N+N^α question remains open in their formulation. Neither their LS theorem nor the topic's pruning measurements supplies exact-N polylog interpolation.

## LIT?padua-3d-20261106-codex-D5-09 — Dolbeault–Chkifa

[*Randomized least-squares with minimal oversampling and interpolation in general spaces*](https://arxiv.org/pdf/2306.07435v2), SINUM62(4)(2024). Actual coverage intro/Cor1.2–1.4 pp1–4 and proof's optimal-measure discussion pp14–15.

Cor1.4, using an optimal design measure on compact X, yields N nodes with interpolation **operator norm at most2N√N**; `1+2N√N` is the near-best error factor, not the Lebesgue constant. The text expressly says that finding that optimal measure can be as difficult as Fekete optimization. For a polynomial lower set and tensor arcsine measure it gives `Λ<=2N min(2^(d/2)√N,N^(log3/log4))`. At d=3 this is O(N^(3/2)) with specified polynomial greedy machinery. It is not a nested closed-form family and its optimal-measure case is not automatically a cheap algorithm. Both bounds improve the topic's known O(N³) R-Leja guarantee as cardinality orders. Classical Fekete gives Λ<=N (local proof below).

## Fekete baseline (known elementary argument; no new source ID)

For a compact cube and Πn, maximize absolute Vandermonde determinant over N-tuples. A nonzero tuple exists because the cube is polynomially determining, and compactness attains the maximum. Replacing node j by any x shows `|ell_j(x)|<=1`. Therefore `Λ<=N`. This proves existence, not a practical closed formula. It is the proper general comparison for the explicit nested R-Leja bound, whose value is computability/nesting rather than the best norm order.

## LIT?padua-3d-20261106-codex-D5-10 — Golomb–Welch

[*Perfect Codes in the Lee Metric and the Packing of Polyominoes*](https://epubs.siam.org/doi/10.1137/0118025), SIAM J.Appl.Math.18(2)(1970),302–317. Actual coverage: primary publisher metadata/reference page; mathematical article behind Get Access, no theorem inspected. The1968 antecedent is *Algebraic Coding and the Lee Metric*, cited separately in later references; the1970 journal article must not be dated1968.

The historical packing mechanism is a close predecessor. The exact large-radius theorem/proof and its relation to the local constants remain **unverified against the original**, so this record grants no priority claim or new proof dependency. Betke–Henk's actual18/19 statement separately supports the existing packing consequence. A historical analogy with Golomb–Welch does not make the local folded-cardinality theorem new or identical without the folding and support hypotheses.

## LIT?padua-3d-20261106-codex-D5-11 — Horak–AlBdaiwi

[*Diameter Perfect Lee Codes*](https://arxiv.org/pdf/1109.3475v3), IEEE IT58(2012),5490–5499. Actual coverage: pp1–2 definitions/anticode discussion; Thm6 and proof p4; Thm10 p5. Thm6 gives lattice tiling of Z^d by finite V iff a finite abelian group G of order|V| admits a homomorphism Z^d→G bijective on V. Thm10 extends this to arbitrary ambient lattices. The source attributes the determinant lower bound for anticodes to Etzion and the double-sphere maximal-anticode assertion to earlier work; those original proofs were not read.

Application: injective reduction of the integer l1 frequency ball modulo L with quotient size equal to that ball makes it a complete set of coset representatives, hence a lattice tiling. This concerns full trigonometric frequencies. Cosine folding and exact `dim Πn` counts are different; no cosine impossibility is obtained solely by quoting the tiling theorem. D4's direct anticode-injectivity argument can prove its own bound without importing maximum-anticode optimality.

## LIT?padua-3d-20261106-codex-D5-12 — Gravier–Mollard–Payan

[*On the Non-existence of 3-Dimensional Tiling in the Lee Metric*](https://doi.org/10.1006/eujc.1998.0211), European J.Combin.19(5)(1998),567–572. Actual coverage: primary publisher search abstract, which states nonexistence of tilings by Lee spheres of radius>=2 in dimension3. Publisher fulltext URL `https://www.sciencedirect.com/science/article/pii/S0195669898902116` returned403. Exact tile model and theorem proof remain unread. The abstract supports the attributed claim, but combining it with a discrete quotient argument as a formally verified theorem requires the original definitions. The paper note can cite it as a coverage-labelled context result; no local cosine theorem depends on it.

## LIT?padua-3d-20261106-codex-D5-13 — Bel-Afia–Meroni–Telen

[*Chebyshev Varieties*](https://arxiv.org/pdf/2401.12140v1). Actual coverage: §3.1 Thm3.3 pp6–7, Thm3.5 p7; §3.2 Thm3.9 p9; §5 Prop5.6/Remark5.7 and surface discussion pp18–19. Thm3.3 identifies nodal singularities of coprime Chebyshev plane curves with the interior parity-grid points. This explains the interior Padua connection, not every boundary Padua point. Thm3.9 gives smooth space curves when three entries are pairwise coprime. Prop5.6 describes a containment for the singular locus of rational cosine varieties; the specialized two-parameter surface discussion gives curves and cube vertices. Do not promote the examples/containment into a theorem about every algebraic surface, every parametrization or every possible non-lattice construction. No interpolation-quality estimate is imported.

## LIT?padua-3d-20261106-codex-D5-14/15 — spectral-set sources

[Greenfeld–Lev1602.08854v2](https://arxiv.org/pdf/1602.08854v2), pp1–3: Thm1.1 says that every facet of a spectral convex polytope is centrally symmetric; Thm1.2 gives translational tiling for spectral convex3-polytopes. [Lev–Matolcsi1904.12262v4](https://arxiv.org/pdf/1904.12262v4), pp1–2: Thm1.1 says that a spectral convex body is a polytope and tiles face-to-face along a lattice. Both define spectrality using a **complete orthogonal** system of `exp(2pi i<lambda,x>)` in Lebesgue L2. The unit octahedron has triangular facets, so Greenfeld–Lev directly excludes its spectrality. This implication is scale-invariant. Full external proofs were not checked.

D1 must separately construct the complete orthogonal limiting system. Small trace deficit, density alone, a maximal orthogonal set or a Riesz basis is not automatically such a spectrum. The sources themselves prove no cubature bound.

## Supplemental primary leads sent to D1/D2/D4

- [Antezana–Marzo–Ortega-Cerdà2101.08064v1](https://arxiv.org/pdf/2101.08064v1), §1 and Thm14/proof pp15–16: excludes sequences of orthogonal reproducing-kernel bases for ball polynomials with weight `(1-|x|²)^(a-1/2)`, a>=0, via a scaled Bessel-kernel limit. This is a close existing spectral-limit mechanism; it does not state a fixed positive excess for asymptotically minimal cubature. R2 actually reread the entire Thm14 proof; its cited universality theorem remains unread.
- [Marzo math/0611503v1](https://arxiv.org/pdf/math/0611503v1), Thms1.6–1.7 and §5: necessary spherical MZ/interpolation densities; no complete interpolation families for p≠2. The p=2 exception is essential and gives no desired positive cubature gap by itself.
- [Białas-Cież–Kenne–Sommariva–Vianello2311.18656v1](https://arxiv.org/pdf/2311.18656v1), Lemma1/Prop1 and proof pp3–4 (2026-11-12 audit05 note: 2311.18656v1 states Lemma1 without proof, citing Piazzon–Vianello, Optim. Lett. 12 (2018) 63–71, following Bos (DRNA 10, 2017); Proposition1's proof is pp3–4. Lemma1's proof is therefore located in that cited source, not locally verified.): degree<=n product Chebyshev mesh C_mn in each coordinate, roots or Lobatto extrema, gives meshΛ<=Λ<=sec(pi/(2m))meshΛ, dimension independent. It applies to interpolation and determining positive-weight LS. At m=3 the upper/mesh factor is1.1547; the midpoint relative half-width is about7.18%. Floating mesh evaluation still needs rigorous arithmetic for a numerical certificate.
- [Ottem–Ranestad–Sturmfels–Vinzant1311.3675v2](https://arxiv.org/pdf/1311.3675v2), Thm1.1 p3 and §2 pp6–7: quartic4×4 pencils with all10 corank-two nodes real exist, with explicit integer matrices. Those matrices were sent directly to D2. This is topic n=2 only; no all-real5×5/6×6 theorem follows. No numerical experiment was executed by D5.

## Acquisition queries and remaining gaps

Actual queries included exact titles/DOIs for Wang–Wang–Wang, Golomb–Welch and Gravier–Mollard–Payan, plus `regularity`, `pdf`, `Lee spheres`, `complete interpolation`, and sphere/cubature. Direct arXiv PDFs above succeeded; the two ScienceDirect bodies failed403, SIAM supplied metadata only. The exact Wang theorem/application, original Golomb–Welch packing proof and GMP tile definitions remain named fulltext gaps. Fulltext novelty comparisons are R2, not established by R1 metadata searches.

## R2 primary coverage supplement — 2026-11-12

The following provisional IDs refer to the actual statement/section comparisons in [novelty-gate.md](novelty-gate.md). These are authored coverage records, not copies of third-party texts. No local PDF bytes/hashes are claimed.

| Provisional literature ID suffix | Primary identity and actual read coverage |
|---|---|
| D5-16 | Cools–Lyness2001, DOI10.1090/S0025-5718-01-01326-6; author-uploaded fulltext recovered through ResearchGate. §1 bounds, §2 eq2.2/Thms2.4–2.5/Def2.7, §4 all3D rows of Tables1/3, §5 limitations. AMS/CiteSeer failed. |
| D5-17 | Poppe–Cools *In search for good Chebyshev lattices*, UNSW-hosted author preprint15pp. §1.2–1.3, §2.2, §3–§6, result tables and captions. Cools–Poppe2011 BIT predecessor remains abstract/metadata-only despite fulltext search. |
| D5-18 | Dencker–Erb arXiv1511.04564v2,30pp. Intro, §2.1–2.3 including frequency space2.19, Thms2.7–2.8, Remark2.13; §3 lead. |
| D5-19 | De Marchi–Vianello–Xu arXiv0805.3529v1,20pp. Intro and §2 including Thm2.2 and its proof. |
| D5-20 | Carnicer–Sauer arXiv1610.01850v2,18pp. Intro, §2 and §3 Thm3.1/cardinal formulas/proof pp4–6. Original Berzolari/Radon papers unread. |
| D5-21 | Kolountzakis arXiv1606.02452 (web-served PDF14pp). §1.1 spectral packing/tiling identities; density/weak-convergence definitions; entire §2 Thm1 and Lemmas1–5/proofs pp5–9. |
| D5-22 | Kuperberg arXivmath/0405366v2,15pp. post-R2 follow-through (committed after R3 preregistration): §3 Prop3.1/Thm3.2 and explanation p5; §6 Thm6.1/Cor6.2 pp11–13; Scholium6.5 statement/sketch p14. Uniform simplex/simple-polytope local-density result is context, not a verified transfer to Chebyshev measure. |

Additional Li–Xu coverage for D1's general-weight boundary: pp32–34 eq5.11–5.13, Lemma5.5 and definition of Δ*. Here `w(x(t))=∏_(μ<ν)sin²π(tμ−tν)`, the Jacobian is constant×√w, and Δ* is the orbit-coordinate image of the A_d simplex. The read weighted inner products are normalized `w^α dx`, α=±1/2, on that curvilinear full-dimensional domain. No general doubling theorem or cube universality premise was read or asserted.

Source-dependent imports remain governed by the exact-statement/normalization/application criterion; full external proof inheritance is not claimed. In particular the log3 import uses KL independently of unread Wang–Wang–Wang, and D1's final nonspectrality uses primary-read GL1.1 independently of the broader LM corroboration.
