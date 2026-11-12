# Positive-cubature and finite-coset obstructions for three-dimensional Padua analogues

Research-note draft, 2026-11-12. Rules/input `04ef28b6139ad15b8cfc31f865c7bb9ba0d56d9b`.
D5 RECORD R3 was published/pushed at `9cd34d7` before root GO. This draft synthesizes the stated local results and primary-source comparisons; it makes no historical-priority claim. New final-stage results retain their developer/supplemental-review status, with formal Claude review separate.

## Abstract

Let Π_n be ordinary total-degree polynomials on the cube. We study analogues of the bivariate Padua package: exactly dimΠ_n nodes, unisolvent interpolation, positive product-Chebyshev cubature through degree2n−1, and polylogarithmic Lebesgue growth. An analytic argument gives a non-effective fixed relative excess over dimΠ_(n−1) for every sufficiently high-degree positive cubature rule, excluding the full package eventually. Its load-bearing external input is Greenfeld–Lev's spectral-polytope facet theorem; the local work proves the near-critical-frame, stationary-limit and completeness steps. Separate results exclude reflection-invariant finite cosets at minimal interpolation cardinality, prove exponential growth for monotone-height Padua stacks, and classify the ten-node finite-coset case. A certified twenty-node nonlattice degree-five rule shows that finite exceptions exist. Minimal-cardinality interpolation without positive cubature remains open at the desired quality.

## 1. Target and known comparisons

Throughout, C=[−1,1]³,

    dμ(x)=π^(−3)∏_(j=1)^3(1−x_j²)^(−1/2)dx,
    N_n=dimΠ_n=binom(n+3,3).

For a Π_n-unisolvent set X of N_n distinct nodes, Λ(X)=sup_(x∈C)Σ_(ξ∈X)|ℓ_ξ(x)| is the norm of its interpolation projector on C(C). The strong target additionally asks for strictly positive weights exact on Π_(2n−1) and Λ=O(log³(n+2)). Positivity and cubature are extra requirements; results about them are not lower bounds for every interpolation scheme.

The basic parity-grid cubature and Fourier/hyperinterpolation mechanism are established prior work. [De Marchi–Vianello–Xu, Thm2.2](https://arxiv.org/pdf/0805.3529v1) gives positive degree2n−1 cubature with about n³/4 nodes. [Li–Sun–Xu, Cor4.12](https://arxiv.org/pdf/0808.0180v2) proves a log³ interpolation bound on that scale in a larger frequency-selected polynomial space, not ordinary Π_n at N_n nodes. Their n³/4+O(n²) cubature assertion is a conjecture. [Li–Xu](https://arxiv.org/pdf/0809.1079v1) has all-dimensional interpolation/cubature families on nonlinear A_d orbit domains; their transformed domain and degree dictionary do not identify them with this cube problem.

Two general baselines calibrate interpolation claims. Compact Fekete maximization gives Λ≤N_n: replacing one row of a maximizing Vandermonde proves |ℓ_ξ|≤1. This is existence, not a cheap closed formula. The explicit nested RLeja lower-set construction has the verified bound

    Λ≤8 binom(n+9,9)=O(n⁹)=O(N_n³),

using [Chkifa, Cor4.3/eq4.8](https://arxiv.org/pdf/1503.01731v2). Its value is explicit nesting; its order and mechanism are known. [Dolbeault–Chkifa, Cor1.4](https://arxiv.org/pdf/2306.07435v2) supplies other general interpolation bounds, with optimal-design computation an explicit caveat. [Krieg–Pozharska–M.Ullrich–T.Ullrich, Thm1](https://arxiv.org/pdf/2401.02220v2) gives O(√N) sampling projections using2N evaluations in arbitrary N-dimensional spaces; its worst-case sharpness is not a √N lower barrier for cube polynomials.

## 2. Eventual fixed excess for positive cubature

**Theorem A.** There are γ>0 and n₀ such that every positive rule on C exact on Π_(2n−1) for μ, with n≥n₀ and N distinct support nodes, satisfies

    N≥(1+γ)binom(n+2,3).

Consequently positive rules with N=N_n do not exist for all sufficiently large n, since N_n/binom(n+2,3)=1+3/n.

**Status:** PROVED with explicit LITERATURE dependency. The [full proof](final-d1/spectral-obstruction.md) depends on three local proved lemmas and primary-checked [Greenfeld–Lev, Thm1.1](https://arxiv.org/pdf/1602.08854v2). The [supplemental adversarial reconstruction](final-check/d1-audit.md) passed the R1–R4 argument and fixed-weight transfer at its pinned file hashes. This is separate from formal Claude acceptance. Neither γ nor n₀ is made effective; no sharp1/4 leading constant is obtained.

Here is the proof structure. Exactness on products of degree≤n−1 polynomials makes the weighted evaluation matrix an isometry. Its row projection has leverage q_i≤1, and Σ_i(1−q_i)=N−dimΠ_(n−1). Reflecting angular representatives by coordinate signs, with stabilizers counted exactly, gives positive Haar cubature on the torus. Near-critical polynomial cardinality squeezes the torus count to the cardinality m_n of the integer l1 ball of radius n−1.

Discarding o(m_n) low-leverage atoms leaves normalized kernel correlations tending to zero. After scaling by n/(2π), the Fourier kernels converge uniformly on compact sets to

    F(u)=|O|^(−1)∫_O exp(2πi ξ·u)dξ,
    O={ξ∈R³:||ξ||₁≤1},   |O|=4/3.

Since F(0)=1, retained configurations are uniformly separated. Random translation over a period cell and compactness produce a stationary law of orthogonal exponential sets Λ for L²(O). Uniform local count bounds preserve the exact mean counting measure |O|dx. These are the conclusions of the [stationary-limit lemma](final-d1/stationary-limit.md), rather than an assumption about a deterministic density.

Completeness needs a further argument. Plancherel gives ∫|F|²=1/|O|; the mean measure therefore gives EΣ_(λ∈Λ)|F(y−λ)|²=1. Bessel bounds this sum by1, so equality holds almost surely for every rational y on one probability-one event. Equality in Hilbert projection and Fourier uniqueness make the exponentials complete. The [complete-law lemma](final-d1/complete-law.md) does not equate critical deterministic density with completeness.

Greenfeld–Lev's theorem requires every facet of a spectral convex polytope to be centrally symmetric. O has triangular facets, so it cannot have this complete spectrum. Negating Theorem A would supply rules with n→∞ and N/dimΠ_(n−1)→1, giving the contradiction. The diamond in dimension two has a lattice spectrum and the actual Padua torus lifts converge to it; the proof therefore preserves the bivariate control.

This proof develops an inherited spectral-limit programme. [Antezana–Marzo–Ortega-Cerdà, Thm14/proof](https://arxiv.org/pdf/2101.08064v1) already uses kernel blow-up to obstruct exact orthogonal polynomial-kernel bases on weighted balls. [Kolountzakis, Thm1 and §2](https://arxiv.org/pdf/1606.02452) proves that exact function packings arbitrarily near tiling density imply a tiling. Their mechanisms are substantive predecessors. The local distinction is the passage from arbitrary near-critical positive Chebyshev frames to a stationary orthogonal law with preserved critical mean intensity, followed by completeness. No first-result claim is made. Spherical p≠2 complete-interpolation results do not supply a p=2 cubature extension.

A routine fixed-polynomial transfer also works: if p>0 on C is fixed and ν=cμ/p, multiplying a ν-rule's weights by p/c gives a μ-rule losing only deg p in exactness. Thus an eventual fixed excess follows for this bounded subclass; see [weight-corollary.md](final-d1/weight-corollary.md). It retains the source dependency; the completed supplemental R4 review covers this transfer. General full-support doubling weights remain OPEN: moving-center kernel universality and retained bulk count have not been established in [general-weight-open.md](final-d1/general-weight-open.md).

## 3. Restricted interpolation obstructions and finite classification

**Theorem B — one reflection-invariant coset.** Let H≤(R/Z)³ be finite and A=a+H invariant under each coordinate reflection. For n≥2, its cosine image cannot simultaneously have N_n nodes and injective Π_n evaluation. This [local PROVED theorem](theory/t1-minimal-obstruction.md) uses the binary-code classification of reflection-stable cosets, short coordinate annihilators and exact parity counts; it requires no weights or cubature. It does not cover noninvariant cosets, coset unions or arbitrary nodes. Its d=2 specialization explicitly permits Padua points.

**Theorem C — monotone-height stack.** Place a degree-(n−k) Padua set in the plane z=cos(kπ/n), k=0,…,n, with the stated local convention. This N_n-node set is unisolvent, but its continuous cube Lebesgue constant satisfies

    liminf_(n→∞) n^(−1)logΛ ≥ 3ζ(3)/(2π²)>0.

The [local analytic proof](theory/t4-monotone-lower.md) evaluates the weighted height-Vandermonde logarithmic asymptotic and compares determinants across height permutations. Recursive/Radon–Berzolari unisolvence and the determinant mechanism are standard; the particular asymptotic estimate is the scoped local calculation. Reordered stacks are not excluded. No numerical growth fit proves this theorem.

**Theorem D — ten-node finite cosets.** Up to phase translation by H and independent coordinate sign changes of the cosine image, every Π₂-unisolvent ten-node finite-coset set is represented by four order16 subgroups or32 order19 subgroups, at zero phase. There is no positive-dimensional unisolvent phase stratum. The [computer-assisted classification](theory/t7-r06-n2-census.md) uses an analytic reduction to orders10..80, a complete HNF/phase enumeration and exact rank predicates, with independent full replay and independently implemented census. This is a finite-coset result, not a classification of arbitrary ten-node sets or an all-degree family.

Chebyshev lattice generation, shifting, HNF search and folding are older frameworks; [Poppe–Cools](https://web.maths.unsw.edu.au/~josefdick/MCQMC_Proceedings/MCQMC_Proceedings_2010_Preprints/PoppeCools-final.pdf) is a direct search predecessor. [Dencker–Erb](https://arxiv.org/pdf/1511.04564v2) proves discrete orthogonality and interpolation on Lissajous–Chebyshev nodes in selected spaces. The read statements do not give Theorems B–D, but incomplete primary coverage prevents an exhaustive priority claim. [Carnicer–Sauer, Thm3.1](https://arxiv.org/pdf/1610.01850) supplies a modern primary Radon–Berzolari/cardinal-formula comparison.

## 4. What lattice and finite computations establish

For full-support unshifted cosine images carrying positive degree2n−1 cubature, the dual integer lattice has minimum l1 norm≥2n. The regular octahedron's lattice-packing density18/19 gives detL≥38n³/27 and hence |X|≥19n³/108. Thus this class cannot have N_n nodes when n≥110. This [proved application with explicit LITERATURE dependency](theory/t9-r06-packing-source.md) uses primary-checked [Betke–Henk](https://arxiv.org/pdf/math/9909172v1). It supplies an explicit class-specific threshold complementary to Theorem A's non-effective arbitrary-node result.

The packing reduction and determinant candidates are inherited. [Cools–Lyness2001](https://doi.org/10.1090/S0025-5718-01-01326-6), §2 and Tables1/3, already gives the shortest-dual-vector reduction and matching candidate values for n1..15. Its K-optimality is weaker than unrestricted lattice optimality. [Kuperberg, Prop3.1/Thm3.2](https://arxiv.org/pdf/math/0405366) likewise states the lattice-design/dual-packing mechanism. Local unrestricted certificates may strengthen certification, not establish discovery of those values.

The elementary double-Lee anticode bound detL≥(2/3)n(2n²+1), followed by exact unrestricted HNF restart, removes the packing dependency for the four [minima n4..7](final-d4/finite-minima.md):92,178,304,486. This does not remove the dependency above n7 or identify global cosine-fold minima. The broader determinant list, global folded minima and rank-constrained fold minima are different optimization objectives.

Oversampling remains useful. The parity-grid Π_n projector uses (3/2+o(1))N_n nodes and has O(log³(n+2)) norm by [the local transfer](theory/t10-log3-corollary.md) from [Kolomoitsev–Lomako, Thm4.1](https://arxiv.org/pdf/1801.00608v1); the integer-translated octahedron has a fixed triangulation and the normalized Haar L1 convention matches. This is PROVED with explicit LITERATURE dependency. A local O(log⁴) proof is separate. Neither bound transfers to a square N_n-node submatrix without the missing inverse-restriction control.

Three final finite programmes calibrate these distinctions:

- **Nonlattice cubic rule:** twenty distinct interior nodes with strictly positive weights are exact on Π₅ and Π₃-unisolvent. A fixed rational coordinate pair excludes containment in the cosine image of any single finite torus coset. The [computer-assisted finite theorem](final-d3/theory.md) passed an exact directed-dyadic checker, independent frozen replay and separate Fraction reconstruction. Its sampled Λ≈30.0121 remains MEASURED, with no certified continuum bound or all-degree continuation.
- **Algebraic real calibration:** known Chung–Yao natural-lattice nodes admit rational rectangular and symmetric determinantal pencils, N_n distinct real affine nodes and Π_n cardinal polynomials for every n. The [elementary realization](final-d2/real-calibration-theory.md) shows that broad real-node existence is not an obstruction for those families. Sparse bivariate Hilbert–Burch recurrence-residual pencils were already developed in IDEA-199; the final Padua n2..4 exact-arithmetic checks remain MEASURED within their finite scope after independent replay and do not make pencil existence new. The three-round [bounded programme](final-d2/outcome.md) found best sampled Λ≈5478.15/546899.58 at n3/4 after eight full symmetric-matrix searches. These poor local paths from a badly conditioned known geometry neither reject the broad matrix family nor prove a 3D recurrence transfer. Four random n4 exact-algebra cases reached their actual CPU caps without conclusions. Full 3D quality remains OPEN.
- **Certified finite norm:** the retained optimized dyadic n12/N455 payload has the rigorous continuum enclosure **25.961333≤Λ≤29.062900**, obtained by intersecting nonnested m2/m3 mesh enclosures. The local inverse-residual calculation and primary-checked [Białas-Cież–Kenne–Sommariva–Vianello mesh theorem](https://arxiv.org/pdf/2311.18656v1) provide the bound. The [certificate reduction](final-d4/certificate-reduction.md) and receipts [m2](evidence/fd4-payload-m2.json)/[m3](evidence/fd4-payload-m3.json) identify the exact nodes and arithmetic. All13 QR meshes, both optimized-n12 meshes, Fraction/integer controls and a rational cosine check passed the [supplemental independent review](final-check-d4/audit.md); formal Claude review remains separate. Other historical optimized coordinates were unavailable; the freshly certified QR baselines n4..16 are separate inputs. Floating normalized-Gram eigenvalues remain MEASURED and establish no uniform Riesz theorem.

External numerical comparisons must use optimized benchmarks without calling them certified optima. [Gunzburger–Teckentrup, Table1](https://arxiv.org/pdf/1407.3291v1) reports d=3 values2.00,2.95,4.05,5.09,6.40 for n1..5; these include a stronger n4 value than the topic's historical5.54. A finite exact cubature theorem can therefore have much weaker interpolation quality than a numerical benchmark with different guarantees.

## 5. Claim ledger and remaining programme

| Claim | Status and essential dependency | What remains outside it |
|---|---|---|
| Eventual positive Chebyshev excess | PROVED with explicit LITERATURE dependency: local D1 lemmas + GL1.1; supplemental R1–R4 reconstruction PASS | Effective γ,n₀; sharp1/4 coefficient; signed rules; arbitrary interpolation |
| Fixed inverse-positive-polynomial weight transfer | PROVED with explicit LITERATURE dependency through D1; elementary transfer | General doubling/universality; separate later-round review coverage |
| Reflection-invariant single-coset exclusion | Local PROVED analytic theorem; accepted historical audit scope | Noninvariant cosets/unions and arbitrary nodes |
| Monotone stack exponential rate | Local PROVED analytic theorem; accepted historical audit scope | Reordered stacks and effective onset |
| n2 finite-coset census | PROVED computer-assisted finite theorem; full independent census/replay | Arbitrary node sets and higher degrees |
| n4..7 determinant minima | PROVED exact finite restart with local double-Lee cutoff; supplemental independent replay PASS | Dependency removal n8..16; global folded objectives |
| Existing packing/RLeja/log3 consequences | PROVED with explicit LITERATURE dependencies, exact source statements/applications checked | Bare external PROVED or inheritance of unread external proofs |
| Twenty-node nonlattice cubic rule | PROVED computer-assisted finite theorem; independent exact reconstruction | Small Λ and all-degree continuation; sampled30.0121 is MEASURED |
| Real determinantal natural-lattice calibration | Local PROVED algebraic realization of known nodes; final review separate | Useful 3D quality, sparse recurrence transfer, positive cubature |
| n12 optimized dyadic continuum norm interval | PROVED with explicit LITERATURE dependency; supplemental independent meshes/arithmetic PASS | Missing historical optimized inputs and any asymptotic quality law |
| Exact-N all-degree Π_n interpolation with log³ growth | OPEN | No scoped obstruction above settles it without positivity/coset/order hypotheses |

The contribution is a collection of precise obstructions, a completed source-dependent positive-cubature argument, exact finite classifications/certificates and calibrated failure boundaries. It does not construct an all-degree three-dimensional Padua family. The remaining interpolation question and the general-weight extension are explicitly retained.

Primary reading coverage, failed retrievals and claim-specific comparisons are recorded in [source-records.md](final-d5/source-records.md), [E4 verification](final-d5/e4-verification.md) and [novelty-gate.md](final-d5/novelty-gate.md). Wang–Wang–Wang2014, original Golomb–Welch, Gravier–Mollard–Payan full definitions/proof and Cools–Poppe2011 remain named fulltext gaps. Their metadata or later citations are not proof dependencies. Exact source statements and normalization/application were checked for the imports actually used; full external proof chains are not claimed locally reconstructed.
