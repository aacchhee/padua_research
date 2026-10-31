# U1 bounded predecessor comparison

2026-10-31. Rules/base d36722823441dc40c6e19d69a174459348dd309c. Codex literature developer, gpt-6.1-sol medium. This addendum leaves frozen records01–40 and their provisional IDs unchanged. It is a literature comparison and locally derived overlap argument, not an acceptance audit or exhaustive novelty claim. U1 theory drafts were not present when initially inspected; the exact proposed criterion comes from the orchestrator’s task message.

## Verdict

**Classify the mechanism as a reformulation/corollary of existing determinant factorization, with explicit characteristic transfer and cutoff bookkeeping still requiring local proof.** The bounded search does not support calling an arbitrary-field Hankel criterion a new mechanism. The proposed even-index functional gives a useful uniform formulation, especially in characteristic2, but the underlying nonsingularity tests are already the axis factors of the established Padua-like determinant formula. A precise full theorem for both degree parities is not automatically inherited from an even-degree presentation.

The narrower publication-level question—whether exactly this finite list of barycentric Hankel minors and all-characteristic statement has previously been printed—remains UNVERIFIED. Absence of the words “Hankel” or “finite field” from inspected predecessors is not a mathematical separation.

## Source scope and overlap

[De Marchi–Usevich2014](https://arxiv.org/html/1311.6455), Proposition1, §4 Corollary1 eq23 and eq21–22: the determinant factors into axis-only evaluation determinants for arbitrary distinct real labels. Its application displays even total degree and says odd degree is similar. Order/interlacing is not needed for the identity itself. The printed coefficient setting is real; polynomial-identity specialization to other characteristics is an additional justification, not a quoted source theorem. The factors use consecutive low powers and multiples of the opposite-parity annihilator. Thus separating x/y factors or identifying a criterion by their nonvanishing duplicates this structural reduction.

[Camargo–De Marchi2015](https://drna.padovauniversitypress.it/system/files/papers/CamargoDemarchi-2015-RVD.pdf), Theorem2.1 and §3 Theorem3.1, was successfully accessed in this followup after earlier timeouts. Its factorization extends the triangular function-matrix construction to general rectangular sizes. Its real nonvanishing proof uses real-root counting; it must not be transferred to finite fields. Section3 discusses further factorization of the axis factors and describes their quotients by Vandermonde factors as generalized Schur-type polynomials. Inspected coverage: abstract, Theorem2.1 statement/proof opening, §3 pp.7–8 excerpts; remainder not audited.

[Floater2017](https://doi.org/10.1016/j.jat.2017.06.002): journal fulltext still returned403. The primary [Bernried slides](https://www.fim.uni-passau.de/fileadmin/dokumente/fakultaeten/fim/lehrstuhl/forster-heinlein/Bernried2017/Floater.pdf), slides8–14, establish the relevant ordered-real interlacing framework and its lower-space construction through Newton divided differences. The publisher’s indexed excerpt reduces uniqueness to nonsingular one-axis divided-difference blocks. This is further structural precedent; an exact identification of every Floater block with the proposed Hankel minors is pending the journal text.

The previously recorded Harris–Simanek and Cao–Ghimire–Wang results are ordered-real kernel predecessors; neither inspected excerpt states an arbitrary-field iff. Cao–Ghimire–Wang2022 resolves HS Conjecture3 over decreasing real nodes, so that conjecture is not an available real-field novelty opening.

## Local algebra explaining the overlap (not a source quotation)

Let O=(z_1,…,z_b) be one parity subset, E the other, c(t)=∏_O(t−z), a(t)=∏_E(t−z), with all labels distinct over a field K. Put

B_O(f)=Σ_(z∈O) f(z)/(c′(z)a(z)),
Δ_k=det[B_O(t^(i+j))]_(0≤i,j<k), Δ_0=1,
V(O)=det[z_i^j]_(1≤i≤b,0≤j<b).

For 0≤k≤b, define D_k as the b×b evaluation determinant on O of the ordered list

1,t,…,t^(k−1), a(t),ta(t),…,t^(b−k−1)a(t).

Empty portions are omitted. Then the local complementary-minor identity is

D_k = ± V(O) (∏_(z∈O)a(z)) Δ_k.                                      (C)

The sign depends only on ordering. Every prefactor on the right is nonzero. Consequently, each such predecessor axis factor is nonsingular exactly when the corresponding barycentric Hankel minor is nonzero. This is the precise overlap mechanism, rather than a similarity of names.

Derivation of (C): let A be the ordinary degree<b Vandermonde evaluation matrix on O. Premultiply the evaluation matrix defining D_k by A^(-1)diag(1/a(z)). Its final b−k columns become the first b−k coordinate vectors. Its determinant therefore reduces, up to sign, to the final k coefficient rows of the degree<b interpolants of t^i/a(t), 0≤i<k. By Lagrange interpolation, the coefficient of t^(b−1−j) in such an interpolant is B_O(t^(i+j)) plus a fixed linear combination of B_O(t^(i+ell)) for ell<j, with coefficient1 on the leading term. Reversing the final k rows gives a unit-triangular transform of the k×k Hankel matrix. Undoing the premultiplication yields (C). Divisions involve only distinct-node Vandermonde factors and nonzero a(z); no division by2, positivity, square roots or order is used. This argument is a local proof of the axis-factor conversion, not an independent proof of the complete U1 determinant formula.

For the full axis list H=E∪O, c′(z)a(z)=ω_H′(z). Thus B_O is exactly the odd/even-restricted barycentric functional, depending on indexing. For powers of degree≤L−2 the full barycentric sum vanishes, so the complementary parity functional equals −B_O in that degree range. In characteristic2 the minus sign becomes plus. This connects the proposed choice of even subset to the predecessor’s choice without requiring alternation signs. Recovering the reduced cutoff floor((L−2)/2), eliminating redundant upper minors and proving the complete two-axis determinant multiplicities are U1 obligations; (C) alone does not certify those steps.

The factorization identities are polynomial in independent node coordinates before divisions. To transfer a real identity, write it as a genuine integer-coefficient determinant identity with sign fixed and prove it over the generic fraction field, then specialize. Merely clearing denominators from a formula containing a power of2 can lose characteristic2 information; use (C) or another integral formulation directly. Track small m and empty products separately.

## Subresultants and Bézout comparison

The columns in D_k encode the bounded-degree relation r+a·s≡0 mod c. Hence their nonsingularity is the absence of a rational-approximation/syzygy defect for the coprime pair(a,c). This is the setting of Sylvester/subresultant and Bézout/Hankel correspondence. A subresultant label alone requires convention checks (which polynomial is numerator, degree ordering, principal index, reversal and normalizing units). No inspected Padua predecessor explicitly printed that full identification, and no new theorem about subresultants is claimed here.

Executed searches found a search-index excerpt for [Subresultants, Sylvester sums and the rational interpolation problem](https://arxiv.org/abs/1211.6895) and the publisher excerpt of [On the bilinear structure associated to Bezoutians](https://doi.org/10.1016/j.jalgebra.2013.10.030). These are pending fulltext comparisons, not verified theorem dependencies. Treat a proposed “subresultant” or “Bézout” reformulation conservatively as classical structured linear algebra until the exact difference is established.

## Actual checks and limits

Executed a small exact SymPy check of (C), ignoring sign, for b=1,…,5, every k=0,…,b, O=(1,…,b), E=(10,…,10+b). All20 cases passed (2+3+4+5+6=20). This finite check supports the handwritten conversion; it does not replace its proof or test generic node sets. No complete U1 checker or adversarial reconstruction was performed by this literature developer. No consequential computer-assisted theorem is asserted.

Additional exact web queries executed in this followup:

- `Floater 2017 polynomial interpolation interlacing rectangular grids pdf subresultant`
- `"Padua" "subresultant"`
- `"Padua" "Bezout"`
- `"Vandermonde determinants" "Hankel" "Usevich"`
- `"Floater" "interlacing" "pdf" "2017" -"fim.uni" -"cs2018"`
- `"Hankel" "subresultants" "rational" "Bezout" Vandermonde complementary minors`
- `"On certain" "Vandermonde" "Camargo" pdf`

The narrow Padua/subresultant and Padua/Bézout searches returned no directly matching claim in displayed results. This bounded negative result establishes neither novelty nor absence. No paper text was copied into Git. Exact theorem acceptance, classification and final allocations remain with the orchestrator and independent auditor.
