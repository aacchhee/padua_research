# X1 sources: Xu points, Xu interpolation, BdMV O(log² n), BCDMV Conjecture (17)

Reader: Claude (claude-opus-5-5), literature reader for topic `padua-xu-lebesgue-20261114`. Date of all reads: 2026-11-14.

Access method: WebFetch only. WebFetch returns a model digest of the PDF's text layer, not page images. Direct download (curl) was refused by the egress proxy for every host tried: uoregon.edu, univr.it, unipd.it, arxiv.org. ScienceDirect, doi.org and akjournals were also blocked. No PDF is kept anywhere.

Status words used:
- **READ**: the item was seen in the text layer.
- **GARBLED**: the text layer is ambiguous, and a reconstruction is given.
- **VERIFIED-NUM**: the reader checked the item numerically with a throwaway script in /tmp, not committed. The script is described in §8.
- **UNVERIFIED**: not seen in any source.

Paraphrases only. Every quote is under 15 words.

---

## 1. Sources read

### S1. Xu 1996

Y. Xu, "Lagrange interpolation on Chebyshev points of two variables", J. Approx. Theory 87(2) (1996) 220–238.
- DOI 10.1006/jath.1996.0102, checked in Crossref 2026-11-14: title, volume 87, issue 2, pp. 220–238, Nov 1996.
- OpenAlex W2046146039, cited by 74. The journal PDF location is ScienceDirect pii S0021904596901021, which was blocked.

URL read: author preprint https://pages.uoregon.edu/yuan/paper/JAT96.pdf. The preprint has its own page numbers (pp. 1–14). The map from preprint pages to journal pages is in `topics/padua-literature-20261103/addenda/journal-versions-2026-11-05.addendum.md` §A12:
- (2.1)–(2.5) are on journal pp. 223–224;
- (2.11)–(2.13) are on p. 227;
- (2.14)–(2.21) are on pp. 228–230.

Sections read: §2, equations (2.1)–(2.21), at preprint pp. 2–9; Theorem 3.1 and 3.3 statements.

Gaps:
- The preprint text layer is GARBLED in (2.1), (2.2), (2.5) summation limits, (2.15), (2.16), (2.20) and (2.21).
- The digest reproduced (2.15) and (2.20) with K_{n−1} where BCDMV say it should be K_{n+1}. That is consistent with the misprint BCDMV report; see S3.
- The journal version was not re-read here. It was read in full by AC's 2026-11-05 supplied copy, but that note records only locators, not formulas.

### S2. BdMV 2006

L. Bos, S. De Marchi, M. Vianello, "On the Lebesgue constant for the Xu interpolation formula", J. Approx. Theory 141(2) (2006) 134–141.
- DOI 10.1016/j.jat.2006.01.005. Crossref checked: vol. 141, issue 2, pp. 134–141, Aug 2006.
- OpenAlex W2007857521, cited by 30. WoS 000240171800003.
- Padova IRIS record hdl 11577/1566050: the published PDF there is restricted.
- Verona IRIS hdl 11562/29814 has no file. Its title field reads differently: "The Lebesgue constant of the Xu interpolation points".

URL read: author preprint https://www.math.unipd.it/~marcov/pdf/LebesgueXu.pdf. It has no journal pagination; preprint pp. 1–9. Read: abstract, §1, §2 (eqs. (2)–(9)), Theorem 1 (eq. (10)), and the proof sketch (Lemmas 1–5, eqs. (17)–(18)).

Gaps:
- The text layer of eq. (10) is GARBLED. The reconstruction is in §4.2.
- Journal page numbers for Theorem 1 are not known.

### S3. BCDMV 2006 (LIT-486)

L. Bos, M. Caliari, S. De Marchi, M. Vianello, "A numerical study of the Xu polynomial interpolation formula in two variables", Computing 76(3–4) (2006) 311–324.
- DOI 10.1007/s00607-005-0137-z. Crossref: online 3 Nov 2005.
- OpenAlex W2098548175, cited by 22.

URL read: author PDF with journal pagination, https://profs.scienze.univr.it/caliari/pdf/BCDMV06C.pdf.

Read:
- §1 (pp. 311–312);
- §2 (pp. 312–317: eqs. (1)–(11), Tables 1–6);
- §3 (pp. 317–319: eqs. (12)–(17), Figs. 1–2);
- §4 (pp. 319–323: Table 7 p. 320, Tables 8–16, §4.1);
- §5 (pp. 323–324).

This closes the LIT-486 gap "§§1–2 and 4 not read" at text-layer level.

Gap: the relation symbol in (17), p. 319, is lost in the text layer. The layer shows a double space between "Λ^Xu_n" and "(2/π log(n+1))²". It needs a page-image check; see §4.1.

### S3'. BCCDMV ETNA 2006 (companion survey by the same group)

L. Bos, M. Caliari, S. De Marchi, M. Vianello, "Bivariate interpolation at Xu points: results, extensions and applications", Electron. Trans. Numer. Anal. 25 (2006) 1–16. Bibliographic data from geodesic.mathdoc.fr (ETNA_2006__25__a32); open access; no DOI.

URL read: https://www.math.unipd.it/~marcov/pdf/etna.pdf. It prints running-head page numbers. Read: §2 (pp. 3–7), Theorem 2.1 and Conjecture (2.15) (p. 5), Table 2.3 (p. 7).

### S4. Kolomoitsev–Lomako 2021 (LIT-379)

Yu. Kolomoitsev, T. Lomako, "Asymptotics of the Lebesgue constants for bivariate approximation processes", Appl. Math. Comput. 403 (2021) 126192. DOI 10.1016/j.amc.2021.126192.

URL read: arXiv v1 https://arxiv.org/pdf/2009.07114v1. Searched for every occurrence of "Xu", "open", "unknown", "not known", "remains", "problem", "question" and "conjecture". The result is in §5.

Gap: the digest gave no page numbers. The repo record LIT-379 says the arXiv and AMC numbering coincide.

### S5. Forward-citation sources

See §6. In the citation lists below, "digest" means a WebFetch digest of the full text or of the abstract, as stated in each entry.

---

## 2. Index conventions (all sources)

| Source | Degree parameter | 1-D nodes | Parities treated | Node-set name |
|---|---|---|---|---|
| Xu 1996 | n: cubature degree 2n−1; Π_{n−1} ⊂ V_n² ⊂ Π_n | z_k = z_{k,n} = cos(kπ/n), 0 ≤ k ≤ n (preprint p. 4; no "Lobatto" name) | n = 2m, eq. (2.14); n = 2m−1, eq. (2.19) | x_{i,j} = (z_i, z_j) |
| BdMV 2006 | same n as Xu | z_k = cos(kπ/n), k = 0..n, n = 2m (eq. (2), preprint p. 4) | even n only ("for simplicity's sake", p. 4). Odd n is mentioned only in the intro (N = (n+1)²/2, p. 3). | x_{2i,2j+1}, x_{2i+1,2j} (eqs. (3)–(4)) |
| BCDMV 2006 | same n as Xu | z_k = z_{k,n} = cos(kπ/n), k = 0..n, n = 2m (eq. (1), p. 312) | even n only | X_N, eq. (2), p. 312 |
| ETNA 2006 | same n | ξ_k = cos(kπ/n), n = 2m (p. 3) | even n only (p. 3) | z_{2i,2j+1}, z_{2i+1,2j} |
| Erb–Kaethner–Ahlborg–Buzug 2016 (arXiv 1411.7589) | XU_{2n} and XU_{2n+1}: their n is half the degree | Chebyshev–Lobatto | both | Remark 1 §2: p = 0 in their Lisa characterisation gives XU_{2n}. §6 defines XU_{2n+1}, with \|XU_{2n}\| = 2n(n+1) and \|XU_{2n+1}\| = 2(n+1)². |
| Xu 2017 survey (arXiv 1709.00651) | n = 2m (nodes (10)); n = 2m−1 (nodes (11)) | same | both | **kernel index shifts**: K*_n = K_{n−1} + Σ Q_j Q_j there, so K_{n−1} reproduces Π_{n−1}. In Xu 1996 and BCDMV, K_n reproduces Π_{n−1}. |

Convention flags:
- **(C1) Reproducing kernel index.** In Xu 1996 and in BdMV, BCDMV and ETNA, K_n(x,y) = Σ_{k=0}^{n−1} P_k(x)ᵀP_k(y) (Xu preprint p. 3), so K_n reproduces Π_{n−1}. Xu's 2017 survey shifts this index by one. All formulas below use the 1996/BCDMV convention.
- **(C2) Normalisation.** Xu writes orthonormal products P^n_k(x,y) = T̂_{n−k}(x) T̂_k(y), with T̂_0 = 1 and T̂_k = √2 cos kθ (preprint pp. 2–3). The correction term in K*_n uses **unscaled** T_n(t) = cos(n arccos t). BCDMV p. 313 state this explicitly as one of their corrections to Xu. VERIFIED-NUM.
- **(C3) Measure.** W_0(x,y) = π⁻² (1−x²)^{−1/2} (1−y²)^{−1/2} on [−1,1]², normalised to mass 1 (Xu preprint p. 2).
- Every paper used here uses the same n for the same node set, **except** Erb et al., who write XU_{2n} and XU_{2n+1}.

---

## 3. Exact definitions

Notation (1996/BCDMV convention):
- z_k = cos(kπ/n), 0 ≤ k ≤ n;
- x_{a,b} = (z_a, z_b);
- angles: x = (cos θ₁, cos θ₂) and y = (cos φ₁, cos φ₂).

### 3.1 Node sets

- **n = 2m (even).** Xu (2.14), journal p. 228 (preprint p. 8); BCDMV (2), p. 312; BdMV (3)–(4).
  - X_n = {x_{2i,2j+1}: 0 ≤ i ≤ m, 0 ≤ j ≤ m−1} ∪ {x_{2i+1,2j}: 0 ≤ i ≤ m−1, 0 ≤ j ≤ m}.
  - Equivalently, X_n = {x_{a,b}: 0 ≤ a,b ≤ n, a+b odd}.
  - N = n(n+2)/2 = dim Π_{n−1} + n/2. This is minimal: it attains Möller's lower bound (2.3) for degree 2n−1. READ, VERIFIED-NUM.
- **n = 2m−1 (odd).** Xu (2.19), journal pp. 229–230 (preprint p. 9).
  - X_n = {x_{2i,2j}: 0 ≤ i,j ≤ m−1} ∪ {x_{2i+1,2j+1}: 0 ≤ i,j ≤ m−1}.
  - The even indices are 0..n−1 and the odd indices are 1..n. Equivalently, X_n = {x_{a,b}: 0 ≤ a,b ≤ n, a+b even}.
  - N = (n+1)²/2 = dim Π_{n−1} + (n+1)/2, one more than the lower bound. READ, VERIFIED-NUM.
- BdMV, BCDMV and ETNA define **only the even case**.

### 3.2 Vertices and parity (main finding)

A vertex (±1, ±1) is x_{a,b} with a, b ∈ {0, n}.

- **n even.** a+b ∈ {0, n, 2n} is even, so **no vertex is a node**.
  - X_n is invariant under x₁ ↦ −x₁ (a ↦ n−a keeps the parity of a+b because n is even), under x₂ ↦ −x₂, and under the swap x₁ ↔ x₂.
  - So the Lebesgue function has full square (D4) symmetry, and all four vertex values are equal. VERIFIED-NUM for n = 2..100 even.
- **n odd.** (1,1) = x_{0,0} and (−1,−1) = x_{n,n} are **nodes**, so λ = 1 there. (1,−1) and (−1,1) are **non-nodes**.
  - The symmetry group is only {id, swap, central reflection}.
  - So "maximum at the four vertices" is false as stated for odd n.
- **Scope of Conjecture (17).** BCDMV's whole paper restricts to n = 2m (eq. (1), p. 312), so Conjecture (17) is a statement about **even n only**. The same holds for ETNA (2.15) and BdMV Theorem 1.
- **Odd n in later sources.** Erb–Kaethner–Ahlborg–Buzug (Numer. Math. 133 (2016), arXiv 1411.7589, §6) quote ((2/π) log(2n+2))² for XU_{2n+1}, citing [2] (BCDMV/ETNA). This is a secondary restatement at the odd degree n' = 2n+1 of the same log(n'+1) form. No source states the vertex claim for odd n.
- **Reader check (not published).** On a 121×121 angle grid for n = 5 and 7, the maximum sits at the two non-node vertices (1,−1) and (−1,1). Numbers are in §8.

### 3.3 Interpolation space V_n² (Xu's Π*_n)

Xu (2.11), journal p. 227 (preprint p. 7) defines it abstractly: V_n² = Π_{n−1}² ⊕ span{V⁺P_n}, where V⁺ is a Moore–Penrose inverse built from the node-annihilating combinations of the degree-n orthonormal vector P_n. Xu 2017 survey eq. (6) gives the same in words: Π_{n−1} plus orthonormal degree-n polynomials not spanned by those vanishing on the nodes.

Explicit product-Chebyshev form below: reader derivation plus VERIFIED-NUM. It agrees with Dencker–Erb arXiv 1711.00557 §9.2 eq. (9.2): for m = (n,n), the degree-n coefficients satisfy c_{(γ₁,γ₂)} = (−1)^{κ₂−κ₁} c_{(γ₂,γ₁)}, and the middle index is excluded when the parities differ.

- **On the nodes.** T_{n−j}(z_a) = (−1)^a T_j(z_a). Hence, on X_n:
  - T_{n−j}(x)T_j(y) = (−1)^a T_j(x)T_j(y);
  - T_j(x)T_{n−j}(y) = (−1)^b T_j(x)T_j(y).
- **n even** (a+b odd; Dencker–Erb κ = (0,1)). The symmetric combinations vanish on X_n.
  - V_n² = Π_{n−1} ⊕ span{T_{n−j}(x)T_j(y) − T_j(x)T_{n−j}(y): 0 ≤ j ≤ n/2 − 1}, i.e. n/2 extra functions.
  - j = 0 gives T_n(x) − T_n(y).
  - T_{n/2}(x)T_{n/2}(y) vanishes on X_n and is excluded.
- **n odd** (a+b even; κ = (0,0)). The antisymmetric combinations vanish on X_n.
  - V_n² = Π_{n−1} ⊕ span{T_{n−j}(x)T_j(y) + T_j(x)T_{n−j}(y): 0 ≤ j ≤ (n−1)/2}, i.e. (n+1)/2 extra functions.
  - j = 0 gives T_n(x) + T_n(y).
- Dimension check: n(n+1)/2 + n/2 = n(n+2)/2, and n(n+1)/2 + (n+1)/2 = (n+1)²/2. Both match N.
- BCDMV and BdMV state only Π_{n−1} ⊂ V_n² ⊂ Π_n (BCDMV p. 312).

### 3.4 Kernel and fundamental Lagrange polynomials

**Compact kernel.** Xu (2.1)–(2.2), journal p. 223; BCDMV (6)–(7), p. 313. READ (GARBLED in the Xu preprint, clean in BCDMV), VERIFIED-NUM against the orthonormal sum.

K_n(x,y) = D_n(θ₁+φ₁, θ₂+φ₂) + D_n(θ₁+φ₁, θ₂−φ₂) + D_n(θ₁−φ₁, θ₂+φ₂) + D_n(θ₁−φ₁, θ₂−φ₂),

D_n(α,β) = ½ · [cos((n−½)α) cos(α/2) − cos((n−½)β) cos(β/2)] / (cos α − cos β).

At cos α = cos β this is a removable singularity. BCDMV (9)–(10), pp. 313–314, give a stable form in Chebyshev polynomials of the second kind.

**Modified kernel, as corrected by BCDMV.** BCDMV (4), p. 312; BdMV (6); ETNA (2.4) p. 3. For a node x_{r,s}:
- **n even** (BCDMV (4)): K*_n(x, x_{r,s}) = ½[K_n(x, x_{r,s}) + K_{n+1}(x, x_{r,s})] − ½ (−1)^r (T_n(x₁) − T_n(x₂)).
- **n odd** (Xu (2.20), journal p. 230; the K_{n+1} correction is the reader's, by the same argument; VERIFIED-NUM): K*_n(x, x_{r,s}) = ½[K_n + K_{n+1}](x, x_{r,s}) − ½ (−1)^r (T_n(x₁) + T_n(x₂)).

Note that ½[K_n + K_{n+1}] = K_n + ½·(degree-n orthonormal block).

**Misprint flag.** BCDMV p. 313 say Xu's (2.15), (2.16) and (2.18) contain misprints: K_{n−1} should be K_{n+1}, T_n should be unscaled, and the r = n, s = n cases of (2.16) are wrong. The Xu preprint digest indeed shows K_{n−1}. The reader checked numerically that the K_{n−1} version is **not** cardinal: off-diagonal entries are O(1) for both parities, n = 2..8. The odd-case formula (2.20) shows the same K_{n−1}, so it needs the same correction, though BCDMV discuss only the even case.

**Fundamental polynomials.** Xu (2.12), journal p. 227; BCDMV (3), p. 312.

ℓ_{r,s}(x) = K*_n(x, x_{r,s}) / K*_n(x_{r,s}, x_{r,s}),  with K*_n(x_{r,s}, x_{k,l}) = 0 for (r,s) ≠ (k,l).

**Diagonal values.** BCDMV (5) and (8), p. 313; Xu (2.18), (2.16) and (2.21).
- General form: K*_n(x_{r,s}, x_{r,s}) = ½[K_n + K_{n+1}](x_{r,s}, x_{r,s}) − 1.
- Explicit values, with β = number of indices in {r, s} lying in {0, n}: K*_n(x_{r,s}, x_{r,s}) = (n²/2) · 2^β.
  - n even: β ∈ {0, 1}, giving n²/2 (interior) or n² (edge). BCDMV (8).
  - n odd: β = 2 also occurs at the corner nodes (1,1) and (−1,−1), giving 2n². Xu (2.21) is GARBLED; the values are VERIFIED-NUM.

### 3.5 Cubature weights

- Rule: λ_{r,s} = 1/K*_n(x_{r,s}, x_{r,s}) (Xu (2.13), p. 227).
- **n even:** λ = 2/n² for interior nodes and 1/n² for edge nodes. This is (2.4), journal p. 223–224 (preprint p. 4), a double sum over the two sub-lattices with halved end terms.
- **n odd:** λ = 2/n², 1/n² or 1/(2n²), the last at the two corner nodes. This is (2.5); its summation limits are GARBLED in the preprint.
- Both rules are exact on Π_{2n−1} for W_0 with total mass 1: VERIFIED-NUM for n = 5, 6, 7 (error ≤ 1e−15).

### 3.6 Lebesgue function and constant

BCDMV (15)–(16), p. 317–318:
- λ^Xu_n(x) = Σ_{x_{r,s} ∈ X_n} |ℓ_{r,s}(x)|;
- Λ^Xu_n = max over [−1,1]² of λ^Xu_n.

Crude bounds:
- (12)–(14), p. 317: |D_n| ≤ ¼(n² + (n−1)²), |K_n| ≤ n² + (n−1)², and |ℓ| ≤ 4 + 2/n².
- (16), p. 318: Λ ≤ (4 + 2/n²) N, roughly 2n².

---

## 4. Statements

### 4.1 Conjecture (17), BCDMV p. 319

Paraphrase:
- For the Xu points (n even, per the scope above), max over [−1,1]² of λ^Xu_n equals Λ^Xu_n, and this quantity behaves as ((2/π) log(n+1))² as n → ∞.
- Moreover, the maximum is attained at the four vertices of the square.
- It is introduced with the phrase "can be bounded as".

**Relation symbol: UNRESOLVED.** The BCDMV text layer drops it. The ETNA version (2.15), p. 5, has a clean text layer: max λ = Λ ≤ A_n ∼ ((2/π) log(n+1))², n → ∞, plus the same vertex sentence.

Two readings follow:
- (a) asymptotic equivalence, Λ^Xu_n ∼ (4/π²) log² n;
- (b) upper-bound form, Λ^Xu_n ≤ A_n with A_n ∼ (4/π²) log² n, i.e. limsup Λ/((2/π) log n)² ≤ 1.

Because there is a c log² n lower bound (§4.3), reading (b) plus a matching lower constant gives (a). ETNA p. 5 adds that the conjecture is "partially proved in [4]" (BdMV), concerning the order of growth.

**Supporting evidence.**
- BCDMV p. 318: maximisation on a uniform 1000×1000 grid for n ≤ 100. Fig. 1 shows n = 6.
- Fig. 2 (p. 318) plots λ^Xu_n(1,1) for n up to 100, with two comparison curves:
  - the least-squares fit (0.95 + (2/π) log(n+1))²;
  - the tensor-product bound (1 + (2/π) log(n+1))² (Brutman).

**Open-problem restatement**, §5, pp. 323–324:
- prove the growth rate;
- prove that the maxima are at the vertices, which reduces the problem to an explicit formula for λ^Xu_n(1,1).

### 4.2 BdMV Theorem 1, eq. (10)

Most likely reading (text layer GARBLED in both the preprint and ETNA Theorem 2.1, p. 5):

**Λ^Xu_n ≤ 8 ((2/π) log n + 5)² + 4,  n even.**

Evidence for this reading:
- The raw ETNA token stream is "Λ Xu n ≤ 8 / 2 / π / log n + 5 / 2 / + 4". Parentheses are dropped and the trailing "2" is the exponent, just as in "(1 + (2/π) log(n+1))2" a few lines earlier.
- The proof chain gives the same result:
  - Lemma 4: (1/n) Σ |sin nθ_k / sin θ_k| ≤ (2/π) log n + 4.
  - Lemma 5 (n even, one extra term): ≤ (2/π) log n + 5.
  - (17)–(18): the type-A sum ≤ product of the two factors ≤ ((2/π) log n + 5)².
  - The type-A Lebesgue part is ≤ 2 + 4·(that). Doubling for type B gives 4 + 8(…)².
- A digest reading "8√(…)" is an extraction artefact: that would contradict the paper's stated (log n)² claim.

Needs a page-image check (journal p. ∈ 134–141). Further notes:
- Range: even n; no other restriction is stated.
- **No lower bound is proved in BdMV.** Its §1 quotes C log n (interval), Berman (ball) and C log^d n for tensor-product cubes, and says the minimal growth for total degree on the square is unknown.
- BdMV says nothing on the location of the maximum.

### 4.3 Lower bounds of order log² n (secondary pointers; none read in full text)

- **Kolomoitsev–Lomako 2021, §1 (S4).** Lower bounds in [6] (Dencker–Erb–Kolomoitsev–Lomako, J. Complexity 43 (2017)), [24] (Subbotin, Math. USSR Sb. 46 (1983)) and [25] (Szili–Vértesi, JAT 159 (2009) 154–164) imply Λ_n ≥ c log² n for the Padua and Xu processes.
- **Xu 2017 survey** (arXiv 1709.00651, §3, Thm 7). ‖L_n‖_∞ = O(log² n), attributed to BdMV [3]. It is called the optimal order among projections from C(Ω) into Π*_n, attributed to Szili–Vértesi [24].
- **Della Vecchia–Mastroianni–Vértesi**, "Exact order of the Lebesgue constants for bivariate Lagrange interpolation at certain node-systems", Studia Sci. Math. Hungar. 46(1) (2009) 97–102, DOI 10.1556/SSCMath.2008.1078. It cites BdMV. Its abstract (OpenAlex) proves order (log n)² for two node sets on [−1,1]². **Which node sets, and the constant: UNVERIFIED** (full text blocked).
- No source gives an explicit lower constant, let alone 4/π².

---

## 5. Kolomoitsev–Lomako 2021 and the Xu points (orchestrator addition)

Findings from the arXiv v1 search (S4; no page numbers in the digest):

- **No "open problem" statement about Xu points.** The words "open", "not known", "remains", "question" and "conjecture" do not occur.
- The only "unknown" is in Remark 2.1, about the asymptotics of ‖F_mn‖ for ℓ₁-partial sums, citing Nazarov–Podkorytov [20].
- The introduction says that much less is known in the multivariate case. That is not a Xu-specific open-problem statement.
- The earlier repo note claiming KL list "exact asymptotics for Xu points" as open **could not be confirmed** in arXiv v1. The published AMC version was not re-read here; LIT-379 says its numbering coincides.
- **Xu points appear only in the introduction.** KL say a log² n growth result for interpolation at Xu points [28 = Xu 1996] was obtained earlier in [3 = BdMV]. They then say the lower bounds of [6, 24, 25] give Λ ≥ c log² n for the Padua and Xu processes.
- **Not a corollary of KL Theorem 2.1.** The Lissajous–Chebyshev theorem requires n = lm + p with l, p ∈ ℕ and 1 ≤ p < m. Hence n ≥ m+1 and m ≠ n. The only special case derived is Padua, LC_{n,n+1} = Pad_n, giving (4/π²) log² n + O(log n).
- **Xu points are LC nodes only in the general Dencker–Erb sense.** In arXiv 1711.00557 §9.2, Xu points are the equal-parameter case m = (n,n):
  - κ = (0,1) for even n;
  - κ = (0,0) for odd n;
  - interpolation space (9.2) as in §3.3.

  Dencker–Erb–Kolomoitsev–Lomako (J. Complexity 2017, arXiv 1608.03451) prove their LC interpolation results only for pairwise coprime parameters, which excludes (n,n). Erb–Kaethner–Ahlborg–Buzug get XU_{2n} only at the excluded value p = 0 of their non-degenerate family.
- **Conclusion.** A proof of Λ^Xu_n ∼ (4/π²) log² n, even n, is **not stated as known** in KL, BdMV, BCDMV, ETNA, Xu 2017, Erb et al., Dencker–Erb, De Marchi CMA 2022 or Ibrahimoglu 2016. In the documented search the best published facts are:
  - upper bound O(log² n), with the explicit constant 8 of §4.2 on log² n after scaling;
  - lower bound c log² n with unspecified c;
  - the leading constant 4/π² is conjectural (Conjecture (17)).

---

## 6. Forward-citation search log (2026-11-14)

| # | Query / endpoint | Outcome |
|---|---|---|
| Q1 | Crossref `query.bibliographic` for the BdMV title | DOI 10.1016/j.jat.2006.01.005, 141(2) 134–141. Crossref cited-by: BdMV 21, BCDMV 13. |
| Q2 | Crossref works/10.1006/jath.1996.0102 | Xu 1996 confirmed: 87(2) 220–238, Nov 1996. |
| Q3 | OpenAlex `filter=doi:` (3 works) | Ids W2046146039 (Xu), W2007857521 (BdMV), W2098548175 (BCDMV); OA locations listed. |
| Q4 | OpenAlex `filter=cites:W2098548175` (BCDMV) | 22 works, listed. |
| Q5 | OpenAlex `filter=cites:W2007857521` (BdMV) | 30 works, listed. |
| Q6 | Semantic Scholar citations of the BdMV DOI | 31; same set plus the BBCdM Morrow–Patterson paper (arXiv 2412.14595). |
| Q7 | Semantic Scholar citations of the BCDMV DOI | 22; same set as Q4. |
| Q8 | WebSearch `"Xu points" Lebesgue constant asymptotics log^2 vertices proof` | Only known items: BBCdM 2412.14595, KL 2009.07114, BdMV, BCDMV, Padua papers, unrelated cylinder paper. |
| Q9 | WebSearch `"Xu interpolation" Lebesgue function maximum vertices of the square conjecture` | BDS arXiv 2605.23299, BCDMV, hypXu, ETNA, BdMV. Nothing new. |
| Q10 | WebSearch for the Lebesgue constant of Xu points with 4/π² / (2/π log n)² | Only known items. |
| Q11 | WebSearch Della Vecchia–Mastroianni–Vértesi title (two variants) | Crossref and OpenAlex metadata only; full text blocked (akjournals). |
| Q12 | WebSearch Szili–Vértesi | Metadata only (JAT 159 (2009) 154–164, DOI 10.1016/j.jat.2008.11.014); no abstract. The Della Vecchia–Mastroianni–Vértesi Acta Math. Hungar. 139 (2013) 337–343 remark gives a new proof of the Szili–Vértesi lower estimate (abstract only). |
| Q13 | WebSearch Erb/Kaethner Lissajous "Xu points" | Erb et al. arXiv 1411.7589, 1503.00895, DRNA survey 2015, Dencker–Erb 1711.00557. |
| Q14 | WebSearch for De Marchi CMA 2022 PDF | Fetched paperCMA2022.pdf. |
| Q15 | WebSearch Pan–Li near-minimal nodes | Abstract unavailable (OpenAlex null; bohrium WAF). |

Per-item outcome for the citing works checked. For each: what was read, and what it says on Xu Lebesgue asymptotics or vertices.

- **Erb–Kaethner–Ahlborg–Buzug**, Numer. Math. 133 (2016), arXiv 1411.7589. Digest of the full text.
  - p = 0 gives XU_{2n} (Remark 1).
  - §6 quotes ((2/π) log(2n+2))² for XU_{2n+1}, citing BCDMV/ETNA.
  - Nothing new is proved.
- **Erb**, AMC 289 (2016), arXiv 1503.00895. First ~100k characters (digest).
  - Cites O(log² n) for Xu points.
  - Xu points are not identified as an LD case.
- **Erb et al. DRNA 8 (2015) survey.** Digest of the full text.
  - Says explicit upper bounds for the Xu Lebesgue constant exist [3, 4].
  - No asymptotics.
- **Dencker–Erb**, arXiv 1711.00557. Digest of the full text.
  - §9.2: Xu points as m = (n,n), with interpolation space (9.2).
  - No Lebesgue statement.
- **Dencker–Erb–Kolomoitsev–Lomako**, J. Complexity 43 (2017), arXiv 1608.03451. First ~100k characters (digest).
  - Xu points are not mentioned.
  - The interpolation results need coprime parameters.
- **Kolomoitsev–Lomako 2021.** See §5.
- **Kolomoitsev–Lomako**, JAT 2018, arXiv 1712.06075. Digest of the full text.
  - Lp-error results "with minor changes" for Xu points (§5.6).
  - No Lebesgue statement.
- **Xu 2017 survey**, arXiv 1709.00651. Digest of the full text.
  - O(log² n), with order optimality via Szili–Vértesi.
  - No asymptotics, no vertices.
- **De Marchi**, CMA 5 (2022), DOI 10.33205/cma.1070020, paperCMA2022.pdf. Digest of the full text.
  - No Xu discussion in the body.
  - The corner-maximum open problem is stated for **Padua** (§3.3).
  - The Padua fit (2/π log(n+1) + 1.1)².
- **Beberok–Białas-Cież–De Marchi**, Constr. Approx. 63 (2026), arXiv 2412.14595. Digest of the full text.
  - Remark 3, §6: Xu's generalised weights, with O(log² n) for Chebyshev weights.
  - No Xu-vertex statement.
  - The corner open problem in §7.1 is for MP points.
- **Białas-Cież–De Marchi–Suder**, arXiv 2605.23299 (May 2026). Digest of the full text.
  - Xu points are not mentioned.
  - Open problem on the number of local maxima on the square, for Padua and MP.
- **Ibrahimoglu**, J. Inequal. Appl. 2016:93. Digest of the full text.
  - Says O(ln²(n+1)) is achieved on the square, citing BdMV.
  - No conjecture status.
- **Liu–Zhu 2022**, DOI 10.1155/2022/5649969. Abstract only. Second-kind Chebyshev product zeros, O((n+2)²); different nodes.
- Not opened:
  - Della Vecchia–Mastroianni–Vértesi 2009 (blocked);
  - Szili–Vértesi 2009 (no OA);
  - Pan–Li 2020 (no abstract);
  - Xu 2012 / 2016 minimal-cubature papers;
  - Li–Sun 2008/2009 (cubic domain);
  - Hyper2d and hyperinterpolation papers, Žitňan papers, Sommariva–Vianello 2008, Cuyt–Yaman 2012, Zhao et al. 2013, Youssef–El-Sharkawy 2016, Gunzburger–Teckentrup 2014, Occorsio–Themistoclakis 2020, Iraji–Chitsaz 2017. These were judged off-target by title.

**Outcome.** No matching result was found in the documented search that proves or refutes either part of Conjecture (17): the asymptotic constant or the vertex maximum. Della Vecchia–Mastroianni–Vértesi 2009 is the one unread item that could contain an explicit lower constant for Xu points.

---

## 7. Published numerical values (G0 checks)

| n | Λ^Xu_n published | Source |
|---|---|---|
| 34 | 10 (rounded) | BCDMV Table 7, p. 320; ETNA Table 2.3, p. 7 |
| 48 | 12 | same |
| 62 | 13 | same |
| 76 | 14 | same |

Other published numbers:
- Fit (BCDMV Fig. 2, p. 318; ETNA Fig. 2.1, p. 6): Λ^Xu_n ≈ (0.95 + (2/π) log(n+1))², n even ≤ 100, least squares.
- Comparison curve: (1 + (2/π) log(n+1))².
- No other tabulated Λ^Xu values were found. BCDMV Table 1 is about D_n stability; Tables 8–16 are interpolation errors and CPU times.
- Same Table 7, for comparison: PD (Padua) 11, 13, 14, 15; MP 649, 1264, 2082, 3102; EMP 237, 456, 746, 1106.

**Reader reproduction** (VERIFIED-NUM; not a published number; λ at a vertex, n even, all four vertices equal):

| n | 2 | 4 | 6 | 8 | 10 | 20 | 34 | 48 | 62 | 76 | 100 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| λ(1,1) | 2.0000 | 3.4142 | 4.4285 | 5.2304 | 5.8992 | 8.2356 | 10.2881 | 11.7445 | 12.8877 | 13.8351 | 15.1653 |

- These round to Table 7's 10 / 12 / 13 / 14.
- The fit at n = 100 gives 15.12.
- On a 121×121 grid, the grid maximum equals the vertex value for n = 4, 6, 8.
- Odd n, at the non-node vertices: λ(1,−1) = 3.955542 (n = 5) and 4.849749 (n = 7). The grid maximum is attained there; λ = 1 at (1,1) and (−1,−1).

---

## 8. Conventions to implement

Self-contained specification. Tags: [X96] Xu 1996, [BCDMV], [BdMV], [DE17] Dencker–Erb 1711.00557, [R] reader derivation with VERIFIED-NUM.

1. **Parameters and nodes** [X96 (2.14), (2.19); BCDMV (1)–(2)].
   - Degree n ≥ 1; z_k = cos(kπ/n), k = 0..n; angles t_k = kπ/n.
   - X_n = {(z_a, z_b): 0 ≤ a,b ≤ n, a+b ≡ n+1 (mod 2)}. That is, a+b is odd for even n and even for odd n.
   - N = n(n+2)/2 for even n; (n+1)²/2 for odd n.
   - Vertices are non-nodes for even n. For odd n, (1,1) and (−1,−1) are nodes.
2. **Orthonormal basis** [X96 pp. 2–3].
   - T̂_0 = 1 and T̂_k(cos t) = √2 cos kt for k ≥ 1, under W_0 = π⁻² ((1−x²)(1−y²))^{−1/2}.
   - K_d(x,y) = Σ_{i+j ≤ d−1} T̂_i(x₁) T̂_j(x₂) T̂_i(y₁) T̂_j(y₂), which reproduces Π_{d−1}. **Index convention C1.**
3. **Space** [R; DE17 (9.2); X96 (2.11)]. V_n = Π_{n−1} ⊕ span{T_{n−j}(x₁)T_j(x₂) − σ T_j(x₁)T_{n−j}(x₂): 0 ≤ j < ⌈n/2⌉}, with σ = +1 for even n (antisymmetric) and σ = −1 for odd n (symmetric).
4. **Kernel at a node ξ = (z_r, z_s)** [BCDMV (4); X96 (2.15)/(2.20) with K_{n−1} → K_{n+1}; R].
   - K*_n(x, ξ) = ½[K_n(x, ξ) + K_{n+1}(x, ξ)] − ½ (−1)^r (T_n(x₁) − σ T_n(x₂)), where T_n is **unscaled** (C2).
   - Compact form for K_n: §3.4, with D_n from BCDMV (7) (stable form BCDMV (9)–(10)).
5. **Diagonal and weights** [BCDMV (8); X96 (2.13), (2.16), (2.21); R].
   - K*_n(ξ, ξ) = (n²/2) · 2^β, β = #{r, s} ∩ {0, n}.
   - Weights w_ξ = 1/K*_n(ξ, ξ) sum to 1 and give a rule exact on Π_{2n−1} for W_0.
6. **Fundamental functions and Lebesgue function** [BCDMV (3), (15)].
   - ℓ_ξ(x) = w_ξ · K*_n(x, ξ);
   - λ_n(x) = Σ_ξ |ℓ_ξ(x)|;
   - Λ_n = max over [−1,1]² of λ_n.
7. **Checks that pass in the reader's script** (throwaway: /tmp/x1chk/xu.py, leb.py, extra.py; not committed):
   - ℓ_ξ(η) = δ_{ξη} to 4e−14 for n = 2..8, both parities;
   - the compact D_n form equals the orthonormal sum (random points, n = 3, 6);
   - cubature exactness on Π_{2n−1};
   - λ(1,1) reproduces BCDMV Table 7.
8. **Disagreements and flags.**
   - (F1) Xu 1996 printed K_{n−1} (and possibly a scaled T_n) in (2.15)/(2.18)/(2.20). The correct form has K_{n+1} and unscaled T_n (BCDMV p. 313, and numerics).
   - (F2) Xu 2017 uses the shifted kernel index.
   - (F3) The odd-n formulas come only from Xu 1996, whose preprint is garbled; the odd case is validated only by numerics.
   - (F4) The relation symbol in (17) is unresolved (BCDMV text layer). ETNA (2.15) uses "≤ A_n ∼".
   - (F5) The BdMV constant is a reconstruction (§4.2).

---

## 9. Items NOT read (for the orchestrator's institutional browser)

1. Xu 1996, journal version §2, pp. 223–230: confirm the printed (2.5) limits, (2.15), (2.16), (2.20), (2.21). DOI 10.1006/jath.1996.0102; https://www.sciencedirect.com/science/article/pii/S0021904596901021.
2. BdMV, JAT 141 (2006) 134–141: Theorem 1 exact form and its page, and whether any remark on vertices or odd n appears. DOI 10.1016/j.jat.2006.01.005; https://www.sciencedirect.com/science/article/pii/S0021904506000220.
3. BCDMV, Computing 76 (2006), p. 319 page image: the relation symbol in (17). DOI 10.1007/s00607-005-0137-z. The author PDF is fine if rendered as an image.
4. Della Vecchia–Mastroianni–Vértesi, Studia Sci. Math. Hungar. 46 (2009) 97–102: which two node sets, and the lower-bound constant. DOI 10.1556/SSCMath.2008.1078.
5. Szili–Vértesi, JAT 159 (2009) 154–164: the exact class of projections covered (onto Π_n only, or onto V_n with Π_{n−1} ⊂ V_n ⊂ Π_n?). DOI 10.1016/j.jat.2008.11.014.
6. Kolomoitsev–Lomako AMC 403 (2021) 126192, published introduction: confirm there is no Xu "open problem" sentence added after arXiv v1. DOI 10.1016/j.amc.2021.126192.
7. Optional:
   - Pan–Li, Appl. Numer. Math. 154 (2020) 104–128, DOI 10.1016/j.apnum.2020.03.017 (may tabulate Lebesgue constants of odd-n Xu nodes);
   - Subbotin, Math. USSR Sb. 46 (1983) 561–570.
