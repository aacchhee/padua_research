# Round 3: open problems after ingesting the new papers, a 2023–2026 search and an exact-arithmetic sweep

*31 October 2026. This round builds on "Open problems verification.md" (round 2) and supersedes its short list in §3. Every candidate below went through an adversarial prior-art check. Detailed notes, quotes and scripts are in `research_notes/Recent open problems 2023 2026/` and its `code/` folder.*

## 1. Bottom line

Twelve papers were ingested: Humet's thesis, Elhay–Golub–Kautsky 1991, Bartels–Jezioranski 1985, Xu 1994, Huhtanen 2002, Huhtanen–Larsen SIMAX 2002, Sauer 2007, plus the five round-2 papers. A 2023–2026 search was run along four lines, and about 240 of your bttb papers were catalogued for exact-arithmetic work. Of roughly 30 candidates, **one floating-point problem is a clear survivor, two short notes are low-risk wins, and the exact-arithmetic side has a single shared hard core**, which is your BTTB "Popov curse".

| Rank | Problem | Status after adversarial check | Fit | Risk |
|---|---|---|---|---|
| 1 | **Paige-type finite-precision theory for the truncated bivariate Lanczos recurrence** (Weisfeld–Bartels–Jezioranski–Huhtanen–Larsen) | **Open core**: an author-stated conjecture (HL SIMAX 2002, p. 1088), confirmed numerically here | very high | medium |
| 2 | **Exact/structured: OP recurrences from moments ("drl Scalar-FGLM") at Õ(N^{(ω+1)/2})**, then the shared core of breaking that exponent (ideal of points, multi-Hankel, generic BTTB) | Baseline is a routine derivation **nobody has written up**; it closes a stated gap (Berthomieu–Faugère 2022). The core is open and very hard | very high (links Padua and BTTB) | low (baseline) / very high (core) |
| 3 | **Marcinkiewicz–Zygmund constants of Clenshaw–Curtis and Padua rules** | Narrow open core. Also refutes an assumption in An–Wu (BIT 2022) | medium–high (Hankel spectra) | low |
| 4 | **Quasi-linear total-degree bivariate interpolation without precomputation** | Open; stuck at Õ(N^{(ω+1)/2}) (BJS 2008). It would imply rank 2's Gröbner basis in Õ(N^{3/2}) | high | very high |
| 5 | Structured Cholesky for bivariate measure modification when q nearly vanishes, plus a rank theorem | Narrow core; the round-3 "quasiseparable" claim was largely an artifact | high | medium |
| 6 | Stability of computing nearest-neighbour recurrence coefficients of discrete multiple OPs | Narrow core; Leuven's stated future work, so coordinate with them | high | medium (competition) |
| 7 | Stability proof for Chebyshev-basis truncated-normal-form rootfinding on [−1,1]² | Open, explicitly left by Mourrain–Telen–Van Barel | medium | high |
| 8 | Whole-ideal backward certificate for approximate border bases (e.g. via a quantitative Lin theorem) | Open but narrow; most is in Kreuzer–Poulisse–Robbiano 2009 | medium | high |

This session's own computations also support three short **notes**:
- **(a)** why the 2010 Givens updating loses 0.6–1.1 digits against HL, and why the "larger redundant pivot" rule is catastrophic (§5);
- **(b)** the MZ result in rank 3;
- **(c)** finite-field Padua points (§4.3): the discriminant closed form, the quadratic Padua set, and the open conjecture characterising unisolvent checkerboard sets over any field through quasi-definite alternation functionals. Harris–Simanek is the ordered real special case.

## 2. Ingestion results that change earlier conclusions

- **Truncated recurrence prior art goes back to 1959.** Weisfeld 1959 and Bartels–Jezioranski 1985 (ACM TOMS, Alg. 634) already have the truncated multivariate recurrence. In 2D the window is 2k+1, identical to HL BIT 2002 Thm 2.3; it works in any dimension, at O(MN^{3/2}). BJ say nothing about rounding errors. HL's claim (BIT p. 393) that the discrete bivariate problem "has not been considered" is wrong.
- **Downdating without Q is classical.** EGK 1991 already downdate the truncated Jacobi matrix without Q, and this carries over to 2D. Moreover H_x = C_x R⁻¹, so the Q-free state *is* the classical sliding-window least-squares R-factor. Node removal is therefore LINPACK/Saunders Cholesky downdating, whose stability is known (Stewart 1979/1995; Bojanczyk–Brent–Van Dooren–de Hoog 1987; Chang–Paige 1998).
  - In tests, the classical R-factor downdate was **20–4000× more accurate** than the EGK-type one, and recovered after a nearly singular window; the EGK-type one did not.
  - Round-2 candidate C is closed apart from a negative note.
- **Approximate ideals: concept and bounds already exist.** Sauer 2007 already defines ε-approximate ideals and H-bases, gives a pivoted-QR algorithm and an a-priori bound. Kreuzer–Poulisse–Robbiano 2009 (Thm 1.4.8) certify AVI output. HL SIMAX already uses a relative zero test. Round-2 candidate D shrinks to rank 8.
- **Humet's thesis (posthumous, compiled by Van Barel, 2019) pre-empts nothing.** It has no downdating, no stability analysis and no truncated variant. Its "Greedy Update" keeps the basis fixed.
  - **Correction to round 2:** ETNA 2014's "stability analysis … not covered" refers to low-rank updates of the Lagrange matrix, not to the IEP.
  - Chapter 5 (slides only) extends your 2010 IEP to **vector** weights, with an unproved "Generalised Implicit Q theorem". It is unpublished prior art if you ever write that up.
- **Xu 1994 (SIAM J. Math. Anal.)** covers only cubature with dim Π_{n−1} nodes. Padua cubature (exact to 2n−1, failing exactly on T_{2n}(x), checked) needs Xu's Pitman RN 312 extension. Round 2 cited the wrong source. Xu himself reports d = 3, n = 3 failing and expects mostly negative existence results.
- **Huhtanen 2002:** for commuting Hermitian A, B, the matrix N = A + iB is normal and B is generically a polynomial in A. So f(A,B)b largely reduces to univariate Lanczos, which makes round-2 Problem 9 weaker still.
- **Morrow–Patterson O(n²) is now proved** (Beberok–Białas-Cież–De Marchi, Constr. Approx. 63, 2026).
- **"Hyperinterpolation directly on Padua points" is trivial:** the Gram matrix is I plus a single rank-1 term.

## 3. Floating-point candidates and verdicts

| ID | Candidate (source) | Verdict | Key evidence |
|---|---|---|---|
| F1 | Paige/Greenbaum theory for truncated bivariate Lanczos; partial reorthogonalization | **Open core** | No analysis exists. Freund band Lanczos, ABLE, Šimonová–Tichý BIT 2025, T. Chen 2026 and Sinha 2026 all treat one operator with block starts; HL has one start and two operators. Experiment: loss ≈ u / (smallest Ritz residual of H_x+iH_y), within a factor of 3, on random nodes; none on tensor grids. A Greenbaum-type "nearby larger node set" statement may be ill-posed, because it needs a commuting extension. Partial reorthogonalization is close to Simon 1984 / Jia–Li 2021. |
| F6 | Conditioning of (nodes, weights) → (H_x, H_y); pivot choice | Essentially solved / trivial | Fischer 1998 univariate; the bivariate case is a QR-perturbation exercise. Your 2010 method's deficit is systematic but comes from rotation counting (error ∝ M vs √M). |
| F3 | Q-free downdating, sliding windows, streaming Christoffel functions | Essentially solved | See §2. Streaming Christoffel functions are standard QR recursive least squares; reported instabilities come from Sherman–Morrison on monomial moments. |
| F2 | Bivariate measure modification in optimal complexity (Gumerov–Rigg–Slevinsky 2024 question) | Partially addressed; claim downgraded | For q bounded away from 0, R is just numerically sparse (O(N) significant entries). Genuine structure appears only when q nearly vanishes: quasiseparable ranks then grow slowly (7→8). The structure depends on the basis. A bug in the round-3 rank script was found and fixed. |
| F5 | IEP for nearest-neighbour MOP recurrences; bivariate discrete MOPs | Partially addressed | Computable today: univariate or step-line IEP plus the Filipuk–Haneczok–Van Assche 2015 recursions, but with no stability analysis. Aptekarev–Denisov–Yattselev (trees) excludes finite supports. The bivariate case has no application. |
| F10 | Discrete bivariate orthogonal Laurent polynomials | Trivial / low value | Your 2010 method with four operators; Humet Ch. 5 already allows Laurent orders. |
| F9 | Moments → block Jacobi; stable multivariate continued fractions | Essentially solved | Standard multivariate Prony / flat-extension pipeline (Mourrain 2018, Collowald–Hubert 2018, Sahnoun–Usevich–Comon 2017, Peña–Sauer 2024). |
| F7 | MZ constants of CC/Padua beyond half-exactness (An–Sommariva–Vianello, Jan 2026) | **Open, narrow** | 1D: η<1 ⇔ λ_max<2 (λ_min>0 is free). A rigorous bound λ_min ≤ 2/(ln N+1.96) gives η→1, which **breaks An–Wu's assumed η=3/4** (BIT 2022, Cor. 4.1) for N ≳ 420; numerically η=0.784 already at N=80. Numerics to N=20480: λ_max=1.004437 constant; 1/λ_min = 1.05+0.46 ln N+0.081 ln²N. The x-marginal of the Padua rule is exactly 2×CC, so η_Padua ≥ η_CC. |
| F8 | Histopolation on Padua triangles | Ill-posed / done / low value | QRCP triangle selection is already their Algorithm 2; their mesh condition is sharp up to log². |
| F11 | Stable Chebyshev-basis rootfinding on [−1,1]² | Open core, high risk | Mourrain–Telen–Van Barel (JSC) already use Chebyshev TNF; Graf–Townsend's instability theorem (LAA 729, 2026) covers monomials only. A stability proof is missing. |
| F12 | Sketched truncated multivariate V+A | Trivial | Sketch-and-precondition already handles M≫N; the sketched inner product destroys the band structure. |
| F4 | Certified approximate border/H-bases | Substantially addressed | Kreuzer–Poulisse–Robbiano 2009; Sauer's p. 307 question is nearly tautological. Open: a whole-ideal backward certificate (Fassino 2010). A possible route via quantitative Lin's theorem (Kachkovskiy–Safarov 2016) is my inference. |

## 4. Exact arithmetic

### 4.1 The frontier, after the adversarial check

All "balanced" bivariate exact problems sit at **Õ(N^{(ω+1)/2})**, i.e. n^{ω+1} with N = n², which is the Popov-curse exponent. The cause is the same everywhere: an m×m polynomial matrix with m ≈ √N. No lower bound beyond output size is known, and the explicit outputs are Θ(N^{3/2}). So progress means either removing the dependence on ω or changing the output format.

| Problem (K², generic, balanced) | Best known | Source (St = stated, Sp = one-line specialisation, D = derived here) |
|---|---|---|
| Degree-order Gröbner basis of N points | Õ(N^{(ω+1)/2}) | Jeannerod–Neiger–Schost–Villard JSC 2017 Prop. 2.1 (Sp); single elements: van der Hoeven–Lecerf 2021/2025 (St) |
| Multiplication matrices = exact recurrence matrices | Õ(N^{(ω+1)/2}) | D, via the row above |
| drl→lex change of order | Õ(N^{(ω+1)/2}) | Berthomieu–Neiger–Safey El Din ISSAC 2022 (St) |
| Precomputation for evaluation/interpolation | Õ(N^{(ω+1)/2}) | Neiger–Rosenkilde–Solomatov 2020; van der Hoeven–Lecerf (St) |
| Interpolation, no precomputation | Õ(N^{(ω+1)/2}) | Bostan–Jeannerod–Schost TCS 2008 Cor. 2 (St) |
| Evaluation, no precomputation | ≈ N^{1.31–1.41} algebraic; N^{1+o(1)} bit over F_q | Nüsken–Ziegler; Kedlaya–Umans; van der Hoeven–Lecerf |
| Lex multi-Hankel | D^{(ω+1)/2}; quasi-linear for "random" sequences | Berthomieu–Boyer–Faugère 2017; Berthomieu–Lebreton–Tran ISSAC 2025 (scope unverified) |
| **drl multi-Hankel (moments → OPs/border basis)** | stated O((#T)^ω) / ≈N³; **derived Õ(N^{(ω+1)/2})** (displacement rank 2(n+1)) | St / D, checked over GF(10⁶+3) |
| Generic BTTB solve, N = n² | Õ(N^{(ω+1)/2}); displacement rank exactly 2n | BJS 2008 (St for block-Toeplitz; Sp for BTTB) |
| Hermite–Padé mod ⟨X^d, Y^d⟩ | stated Õ(m^ω d^{ω+2}); **derived Õ(m^{ω−1}d^{ω+1})** | Naldi–Neiger 2020 / D (linearize in Y; JNV 2020). Scoop risk: Naldi–Neiger have a paper in preparation |

**Structural finding (checked computationally; see §6b T2 for the corrected reading, "not flat at colength N"):** generic BTTB is **not flat** at colength N. For a random two-level Hankel table, H⁻¹H_x and H⁻¹H_y fail to commute, with commutator rank exactly 2(n−1) (n = 2…5); for moments of an N-atomic measure the commutator is zero. So recurrence-guessing results cannot be transplanted to generic BTTB directly. The low-rank defect suggests a "flat plus rank-√N correction" attack, which is speculative but ties the two projects together.

### 4.2 Exact-arithmetic verdicts

| ID | Candidate | Verdict |
|---|---|---|
| X1 | Exact Van Barel–Chesnokov recurrence over Q/F_p; bit sizes; breakdown over F_q | **Mostly settled.** Mourrain ISSAC 2017 computes the orthogonal bases and multiplication matrices exactly, with pivoting around isotropy; bit bounds are textbook. Breakdown rates match finite-geometry counts (the earlier "90%" mixed non-unisolvent sets with genuine breakdown). Left: a graded look-ahead that keeps block-tridiagonality (modest; check Benouahmane–Cuyt first). |
| X2 | Beat N^{(ω+1)/2} for ideal/multiplication matrices of points | **Open core.** From the points, compute a terse/vanilla representation (van der Hoeven–Larrieu 2018) or a Hilbert–Burch pencil in o(N^{(ω+1)/2}), or the Gröbner basis in Õ(N^{3/2}) independent of ω. The "degree-1 quotients ≈ OP recurrence" bridge **fails**: ideals of points are not complete intersections. |
| X3 | Computational Hilbert–Burch for unisolvent sets | Partly covered. A linear (n+2)×(n+1) matrix exists for every unisolvent set (Gaeta 1951; Eisenbud). Not a compression (≈6N vs 2N numbers). Left: an "inverse rectangular two-parameter eigenvalue problem", a reframing whose numerical benefit is unproven. |
| X4 | Superfast drl guessing / exact bivariate OPs from moments | **Open.** (i) Writing up Õ(N^{(ω+1)/2}) is routine but unpublished; it closes Berthomieu–Faugère's stated gap at baseline level and contradicts Mourrain 2017's remark that displacement rank does not help. (ii) An output-optimal, ω-free "2-D half-gcd" for flat data is the hard part. |
| X5 | Bivariate Padé mod ⟨X^d, Y^d⟩ via BTTB merges | Solved down to the curse exponent by a routine reduction; BTTB merges give no exponent gain. |
| X6 | Quasi-linear total-degree interpolation without precomputation | **Open, very hard.** X6 ⇒ X2. |
| X7 | Exact (non)existence certificates for minimal cubature, d ≥ 3 | Partly covered (Noskov–Schmid; Hirao–Sawa design theory). Li–Sun–Xu is asymptotic, so no finite certificate settles it. Niche: cube/product-Chebyshev degrees 5–9. |

### 4.3 Padua points over finite fields

**Verdict: partly known and formally straightforward. At most a short note, with one genuinely open conjecture.** Notes are in `finite_field_padua.md`; code in `padua_checks/ff_padua/` (`python3 -I run_all.py`, about 40 s).

**Why it is mostly known.** Every Padua identity is a sum over roots of unity of orders 2n and 2(n+1). It therefore holds over Z[ζ_{2n}, ζ_{2n+2}, 1/(2n(n+1))] and reduces mod any p ∤ 2n(n+1). That covers cardinality, unisolvence, cubature and discrete orthogonality, the ideal and H-basis, the sparse recurrence matrices (≤ 2 nonzeros per column, entries in {1, ½}) and the DCT-I fast transform. The hoped-for application, quasi-linear exact total-degree interpolation on dim Π_n points, already exists: van der Hoeven's truncated FFT (ISSAC 2004) and van der Hoeven–Schost (AAECC 2013), both under weaker field conditions. No paper defines Padua, Lissajous, Xu, Morrow–Patterson or Chebyshev-lattice sets over finite fields.

**Small results that are probably new** (all checked in exact arithmetic mod p):
- **Existence.** Pad_n is defined over F̄_p iff p ∤ 2n(n+1), so never in characteristic 2.
  - All points lie in F_q iff q ≡ ±1 mod 2n and mod 2(n+1). There are four split/non-split types, q ≡ 1, 2n+1, 2n²−1 or −1 mod 2n(n+1); the smallest field is F_{2n+1}.
  - Dickson polynomials with a ≠ 1 add nothing.
- **Padua discriminant in closed form.** det V_mon² = 2^{(n²+3n+6)/2} (n(n+1))^{(n+1)(n+2)/2} in Dickson coordinates (2x, 2y). Consequence: p ∤ 2n(n+1) is necessary *and* sufficient for unisolvence mod p.
- **The "quadratic Padua set" of F_q, q = 2n+1.** Pad_n = {(x,y) ∈ X×Y : χ((x+1)(y+1)) = 1}, with X, Y defined by the quadratic character of x²−1 and y²−1. It is unisolvent, with (q+1)(q+3)/8 points; verified for all primes q ≤ 47.
- **Padua evaluation codes.** These have an explicit weighted dual and beat the footprint bound. [10,3,7]_7 and [10,6,4]_7 are optimal; over larger fields the codes are within 1–2 of Griesmer, so not optimal in general.

**Correction, and the one open item.**
- **Correction.** Harris–Simanek unisolvence is **not** field-independent, and needs ordered nodes even over Q. Their proof uses monotonicity and positivity. Counterexample: X = (0,1,2), Y = (0,1,3,2) gives rank 5/6 over Q and F_101. Round 2's "any distinct node sequences" was wrong.
- **Conjecture (open).** A labelled checkerboard set is unisolvent iff two discrete "alternation" functionals, f ↦ Σ(−1)^k f(h_k)/ω′(h_k) on X and the analogous one on Y, are quasi-definite (all leading Hankel minors nonzero). It held in 14,400/14,400 random tests (p = 13, 31, 101; m ≤ 6). Ordered real nodes make both functionals positive definite, which recovers Harris–Simanek.

Recommendation: do not present the fast transform as new. A short note could combine the discriminant, the quadratic set, the reduction-mod-p dictionary, and the counterexample with the conjecture.

## 5. New results from this session's own computations (working track)

1. **Accuracy of your 2010 Givens updating.** Against a long-double reference it trails HL by 0.6–1.1 digits, for every node order and weight tried. The error grows like M (slope ≈0.96), against ≈√M for Householder/CGS2, consistent with O(M) rotations per entry. So it is not EGK's "patternless" noise.
2. **The "use the larger redundant pivot" rule is catastrophic in updating.** Errors reach 7e-4 on Padua n = 20 with random weights. The cause: mid-update, the points processed so far are not unisolvent (Padua points arrive column by column with equal x), so both pivots sit at rounding level. Your fixed scheme stays robust.
3. **Truncated bivariate Lanczos loses orthogonality** at ≈ u / min Ritz residual of H_x + iH_y; this does not happen on tensor grids. Numerical support for HL's conjecture.
4. **Classical R-factor downdating beats EGK-type Q-free downdating by 20–4000×** in sliding windows, and is relationally stable.
5. **MZ constants of Clenshaw–Curtis:** λ_max = 1.004437 constant up to N = 20480, with 1/λ_min ≈ 1.05+0.46 ln N+0.081 ln²N. A rigorous η→1 refutes An–Wu's η=3/4 assumption. The Padua x-marginal is exactly 2×CC.
6. **Exact structure:** the drl multi-Hankel displacement rank is 2(n+1); the generic two-level Hankel commutator has rank 2(n−1); Hermite–Padé reduces to Õ(m^{ω−1}d^{ω+1}).
7. **Measure modification:** for q bounded away from 0, the Cholesky factor is numerically sparse. For q = 1.001 − x on the disk (Koornwinder basis), R is exactly bidiagonal.

## 6. Suggested plan

- **Main line (rank 1):** a finite-precision theory of truncated bivariate Lanczos, with a reorthogonalization criterion. Note 1 above is a natural companion: it explains your own method's accuracy and fixes the pivot rule.
- **Bridge to BTTB (rank 2):** write up drl Scalar-FGLM / exact bivariate OPs from moments at Õ(N^{(ω+1)/2}). Then treat "flat plus rank-2(n−1) correction" as a common attack on the curse for points, moments and BTTB.
- **Quick win (rank 3):** a short note proving λ_max < 2 and the 1/log² N law for Clenshaw–Curtis, with the An–Wu consequence. Consider contacting An, Sommariva or Vianello, since an An–Sommariva–Xue paper is in preparation on a neighbouring question.
- **Coordinate before investing:**
  - Van Barel/Vandebril on rank 6 (their stated future work) and on Humet Ch. 5;
  - Naldi–Neiger on the Hermite–Padé reduction.

## 6b. What the bttb-research campaign contributes

This section comes from two read-only mappings of aacchhee/bttb-research at commit b68e9997. They are in `bttb_repo_exact_mapping.md` and `bttb_repo_numeric_mapping.md`, with probe scripts `code/bttbmap_*` and `code/drl_*`. Repo statuses are quoted unchanged; nothing below upgrades them.

**The bridge.** In an orthonormal product-Chebyshev basis on the box, the Gram matrix of a modifier Q(x,y) is exactly a symmetric block of a BTTB matrix with symbol Q(cos θ, cos η). For the first kind it is the even⊗even block of T_{2n−1}(q); this was checked to 5e-15. C3's folded variables are therefore the Padua coordinates, and C3's quadrantal-symmetry hypothesis holds automatically. This covers Chebyshev measures on the box only; on total-degree index sets only spectral inequalities transfer, by interlacing.

| Transfer | BTTB source (status) | Padua direction | What is still needed |
|---|---|---|---|
| **T1. Exact "2-D Schur step" for total-degree moments** | EX-L1172 / EX-T1174 (PROVED over algebraically closed fields; nonuniform promise-input references): generic *box* two-level Hankel tables extend to a Gorenstein functional on a complete intersection, with det H_n = κ·Norm(h)·det H_{n−1}(ν) | X4(ii) / X1, the ω-free moments → OPs target and the shared core | A drl analogue (two curves of degree n+1, length (n+1)², Euler–Jacobi residue) passed every exact check over GF(10⁶+3) for n = 2..5, including flat N-atomic tables (MEASURED). Open: per-level cost C(j) ≤ C(j−1)+Õ(j²), and a novelty check against apolarity / cactus-rank literature (Iarrobino–Kanev, Ranestad–Schreyer) |
| **T2. Quantifying "generic tables are not flat"** | EX-T308(a), EX-N943 (CONDITIONAL); EX-T516 §6 repair inequality; Degani–Schiff–Tannor Thm 2 (already in AC's BTTB folder) | Rank-2 core, "flat + low-rank correction" | A commuting repair needs correction ranks summing to ≥ n−1, and any Gorenstein extension has colength ≥ N+n−1. The excess colength is Θ(N), not √N. **The round-3 phrasing must become "not flat at colength N"**: EX-L1172 shows generic tables *are* flat at colength N+(n−1)². |
| **T3. MZ constants, λ_min ≥ c/log² N** | C4-T03(ii) (PROVED: weighted Schur test giving a log² bound) | Rank 3 | The template fits CC in Lagrange coordinates. Its hypotheses were measured for N = 40…1280 (entry-bound constant flat at 0.250; weight floor constant 1.000). Prove both and combine with the rigorous upper bound. Note: λ_max ≥ 2(4N²−1)/(4N²−2) > 2 at n = N, so "λ_max < 2" is a statement about Π_{N−1} only. pySuperDC can compute the full 1D spectrum (HSS rank ≤ 9 in node order). |
| **T4. Measure modification with Chebyshev modifiers** | C3-T04(d′), C3-T04(c), C3-L02, C3-L06/T06 (PROVED in their scopes) | Rank 5 | A rigorous λ_min lower bound, small-eigenvalue counts, and an exact soft-O(N) solver for G_Cheb(Q₀²h)+σ (real shift only). A corner zero becomes a point zero of order 2 (CDGS's own elliptic setting). **Interior-curve zeros are blocked by R04/R07**, and measured ranks grow ~n there. A rank theorem must exclude curve zeros and use C3's boundary method for them. |
| **T5. Curse optimality inside programme models** | EX-T390/391/945 (PROVED in programme models) | Rank-2 core | These bound programmes correct on whole dense-block / fixed-pair displacement classes by ≈ n^{ω+1}; they apply directly to box/lex multi-Hankel. drl needs a new embedding. They do not cover a single solve, which is the ω-free target. |
| **T6. Root-free tensor-algebra weights** | EX-T852 (PROVED, every field, Õ(N^{3/2})) | flat product-ideal case | Proves the product-ideal case only at N^{3/2}. Nothing supports "near-linear tower arithmetic". |

**Blocks and drops.**
- **X5 (Hermite–Padé) is dropped as a separate direction.** EX-L1072 maps BTTB solving to an m = 3 box Hermite–Padé problem, so X5 and generic BTTB coincide at the curse level.
- **"Prove the curse ≍ matrix multiplication" (idea J) is blocked as stated** by EX-P306: Padua instances have Θ(N) inputs, not N^{3/2}.
- The banded/half-strip solvers do not apply to positive measures.
- **Rank 1 (finite-precision Lanczos) gets nothing from the repo.** All of its CG/GMRES theory is exact-arithmetic.

**Corrections to Padua notes from the repo's literature records:**
- **Mourrain 2017's displacement-rank remark** is §3.3, pp. 338–339 (LIT-1658), and is a comparison remark, not a theorem.
- **Berthomieu–Boyer–Faugère Prop. 16** is p. 61 (§6) and carries a factor μ (LIT-1317).
- **BJS's deterministic block-Toeplitz bound** is second-hand (LIT-177).
- **"X4(i) is routine"** holds only for a randomised generic version: BJMS is Las Vegas with field-size conditions (LIT-187/372).
- **Neiger ISSAC 2016 Thm 1.4** (LIT-1586) is the deterministic basis for frontier row 1; the Gröbner-basis-of-points corollary itself is not stated there.
- **Villard 2018** is confirmed (LIT-1160).
- **Already on file:** Degani–Schiff–Tannor 2005 is in AC's BTTB folder (CORPUS row 28). DGIM 2006, Laurent–Mourrain, Naldi–Neiger, JNV, Xia–Chandrasekaran–Gu–Li 2010 (LIT-1747), Xi–Xia 2016 and Chandrasekaran–Gu–Pals 2006 have statement-level records.

**Effect on the ranking.**
- **Rank 2 now has a concrete first step:** T1, the drl 2-D Schur step, whose exact screen passed. It should be developed inside bttb-research, since it reuses EX-L1172/1174.
- **Rank 3 now has a proof template:** C4-T03(ii).
- **Rank 5 is reshaped:** boundary or corner zeros only, with C3 tools for curves.

## 7. Papers to obtain (deduplicated, by priority)

| # | Paper | Why |
|---|---|---|
| 1 | Google Scholar "Cited by" exports for Huhtanen–Larsen BIT 2002 and Bartels–Jezioranski 1985 | The last places a rank-1 analysis could hide |
| 2 | Simons report, arXiv 2602.05394 (open access; our fetches failed), §§2, 4–6 | Exact wording of Problems 2.19 and 4.3 |
| 3 | Aliaga–Boley–Freund–Hernández, Math. Comp. 69 (2000), [doi:10.1090/S0025-5718-99-01163-1](https://doi.org/10.1090/S0025-5718-99-01163-1); Simon, LAA 61 (1984); Jia–Li, Numer. Algorithms (2021), [doi:10.1007/s11075-020-01064-8](https://doi.org/10.1007/s11075-020-01064-8) | Band-Lanczos and partial-reorthogonalization baselines for rank 1 |
| 4 | Berthomieu–Lebreton–Tran, ISSAC 2025, [doi:10.1145/3747199.3747569](https://doi.org/10.1145/3747199.3747569) (hal-04937888) | Whether drl is covered or is future work (rank 2) |
| 5 | V. Neiger, PhD thesis 2016 (HAL tel-01431413) | Whether the degree-order Gröbner basis of points is stated |
| 6 | van der Hoeven–Larrieu, ISSAC 2018 (hal-01702547) and Berthomieu HDR 2023 (tel-04289532) | Terse/vanilla representations; perspectives |
| 7 | An–Sommariva–Vianello, Math. Comput. Simul. 252 (2027), journal version; An–Wu, BIT 2022 (published version) | Rank 3: check for an erratum, or that they already proved it |
| 8 | Gumerov–Rigg–Slevinsky, SIAM, [doi:10.1137/25M1724213](https://doi.org/10.1137/25M1724213); Chandrasekaran–Dewilde–Gu–Somasunderam SIMAX 2010 | Rank 5 |
| 9 | Y. Xu, *Minimal Cubature Rules* (CUP 2025), [doi:10.1017/9781009663939](https://doi.org/10.1017/9781009663939), Ch. 5, 9, 10; Y. Xu, Pitman RN 312 (1994) | Open problems in cubature; the correct Padua-type theory |
| 10 | Nakatsukasa–Trefethen, Acta Numer. 35 (2026), [doi:10.1017/S0962492925100263](https://doi.org/10.1017/S0962492925100263) | List of 20 open problems (our fetch was cut off) |
| 11 | S. Telen, PhD thesis (KU Leuven 2020); Mourrain–Telen–Van Barel, JSC (arXiv 1803.07974) | Rank 7 |
| 12 | Still missing from round 2: Van Barel–Bultheel, Contemp. Math. 281 (2001); Elsner–Ikramov, LAA 254 (1997). (Degani–Schiff–Tannor 2005 is already in your BTTB folder, CORPUS row 28.) | Background / prior art |

Lower priority, listed in the notes: Kreuzer–Poulisse–Robbiano 2009; Abbott–Fassino–Torrente 2008; Fassino–Torrente 2013; Schmid, SIMAX 1995; Hirao–Sawa SINUM 2009; Stewart, IEEE TSP 1995; Fischer 1998.

**Search limits this round:** the arXiv API and search, Semantic Scholar, OpenAlex, Crossref, Google Scholar, HAL, dl.acm.org and epubs.siam.org were mostly blocked. Most "nobody has done X" findings are therefore negative web-search results, not proofs of absence. Citations marked "(mem)" or "[not fetched]" in the notes are from memory.
