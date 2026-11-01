# L2 prior-art check 01 — mechanisms (a)–(d)

- Reviewer: Claude Opus 5.5, effort high. I am an independent prior-art checker, not the L2 developer.
- Date: 2026-11-01. Scope: L2 rounds R01–R03 (`directions/L2/R01.md`–`R03.md`, `STATUS.md`, `candidates.md`) and the four mechanisms named by the orchestrator.
- Authorization: AC authorized reading related literature anywhere online (coordinator brief). No fulltext or long extract is stored in the repository.
- **How fulltexts were read.** Every "fulltext" below went through WebFetch: a summarising model answers a prompt against the fetched page. **I did not read these texts verbatim.** Quotes are as that model returned them (≤ 25 words each). Locators are the model's reading. Anything load-bearing must be re-checked against the PDF before it is cited in a paper.
- **This review makes no novelty claims.** "No matching result found in the documented search" covers only the queries, dates and limits logged below.

## Search log (2026-11-01)

**Repository first.** I read the following:
- `literature/INDEX.md`, by grep on the relevant rows.
- The records zhu-nakatsukasa-2026, brubeck-nakatsukasa-trefethen-2021, hokanson-2020, liu-narayan-2023, meurant-sommariva-2019, simon-1984-mathcomp, simon-1984-laa, larsen-1998, jia-li-2021, carson-et-al-2025, barrio-pena-sauer-2010, mourrain-2017, paige-rozloznik-strakos-2006 and paige-vandooren-1999.
- The headers of the records lin-1997, sauer-2007, kressner-2018, he-kressner-plestenjak-2025, xu-tams-1994-operator and sinha-2026.
- The reviews `reviews/L1-prior-art-01.md` and `reviews/L3-prior-art-01.md` (verdict lines only).
- The L2 round files, and the code header and selection rules in `tracks/bivariate-lanczos/code/L2/l2_core.py`.

Web searches (WebSearch; S = standard, E = extended):

| # | Mode | Query (abridged) | Useful hits |
|---|---|---|---|
| 1 | E | stability analysis "Vandermonde with Arnoldi" rounding error multivariate | ZN 2301.12241; Niu et al. 2603.23858 |
| 2 | E | "Vandermonde with Arnoldi" error analysis backward stability Hessenberg evaluation | confluent V+A; par.nsf 10547074 (Zhang–Su–Li) |
| 3 | S | Carpraux Godunov Kuznetsov condition number Krylov bases subspaces | Malyshev–Sadkane ETNA 23 (ref. list) |
| 4 | S | Braconier Langlois Rioual influence of orthogonality Arnoldi | no direct copy found |
| 5 | S | Paige augmented stability Lanczos; Paige–Panayotov–Zemke | Paige SIMAX 2010 PDF (McGill) |
| 6 | S | "Condition number of the Krylov bases and subspaces" 1996 | as 3 |
| 7 | S | Kuznetsov perturbation bounds Krylov bases Hessenberg forms | as 3 |
| 8 | E | commutator computed multiplication matrices error indicator normal form Telen Van Barel | Telen–Mourrain–Van Barel 1803.07974 |
| 9 | E | approximate border basis multiplication matrices almost commute (Kreuzer–Poulisse–Robbiano) | Lin-type results only |
| 10 | S | Heldt–Kreuzer–Pokutta–Poulisse approximate zero-dimensional ideals | Passau PDF |
| 11 | S | Telen Mourrain Van Barel truncated normal forms commute | as 8 |
| 12 | S | G. W. Stewart backward error bounds approximate Krylov subspaces | UMD DRUM report CS-TR-4247 |
| 13 | S | lower bound angle computed vs exact invariant subspace residual | nothing specific |
| 14 | S | Drkošová–Greenbaum–Rozložník–Strakoš numerical stability of GMRES | metadata (ASEP) |
| 15 | E | semiorthogonality partial reorthogonalization two matrices / block Lanczos | Simon LAA 61 PDF link (blocked) |
| 16 | S | Austin et al. practical algorithms multivariate rational approximation | eScholarship PDF |
| 17 | S | Reichel fast QR Vandermonde-like polynomial least squares 1991 | SIAM page (blocked) |
| 18 | E | Sommariva Vianello discrete OPs QR twice computed basis span accuracy | De Marchi–Piazzon–Sommariva–Vianello CMMSE 2015 |
| 19 | E | multivariate Arnoldi OPs finite precision computed basis "total degree" commute | Zhang et al. 2404.09266; Liu–Narayan |
| 20 | E | multivariate V+A 2025/2026 stability loss of orthogonality Lanczos | nothing new |

**Pages fetched (WebFetch):**
- arXiv 2301.12241, three times: PDF twice and HTML once (the ar5iv copy was truncated).
- arXiv 1911.09988 PDF; arXiv 2009.10803 PDF.
- arXiv abstract pages of 2603.23858 and 2608.21268, and the Pith page of 2605.25176.
- arXiv HTML of 2404.09266v2, read twice.
- par.nsf.gov 10547074 (Zhang–Su–Li) and 10435784 (Liu–Narayan v2).
- The McGill PDF of Paige 2010; the ETNA 23 pp. 5–14 abstract and PDF.
- The DRUM item and PDF of Stewart CS-TR-4247.
- The Passau PDF of Heldt et al.; arXiv 1803.07974 and 0710.2641.
- The eScholarship PDF of Austin et al. 2021; the CMMSE 2015 PDF (wams.pdf); the ASEP record of DGRS 1995.

**Coverage limits.**
- Blocked: the ScienceDirect PDF of Simon LAA 61 (so its Theorem 5 is still unread) and SIAM epubs (Reichel 1991).
- Rate-limited: the arXiv PDF of Austin et al. 1912.02272. The published CPC version was read instead.
- Not read:
  - ZN Appendix B (Algorithms 4–5), which is absent from all three copies fetched;
  - Braconier–Langlois–Rioual 2000;
  - Carpraux–Godunov–Kuznetsov 1996 and Kuznetsov 1997 (citations confirmed only);
  - Paige–Panayotov–Zemke 2014;
  - Greenbaum–Rozložník–Strakoš 1997;
  - Kreuzer–Poulisse–Robbiano 2009;
  - Corless–Gianni–Trager 1997; Stetter 2004;
  - Dunkl–Xu 2014 (L1 also did not read it).
- Not searched: zbMATH, MathSciNet, Google Scholar, forward-citation chases.

---

## (a) Span drift under full reorthogonalization: computed spans ≠ S_n; J-sections wrong up to 1e-2

**What the V+A papers actually claim (fulltexts via WebFetch).**

1. **Zhu–Nakatsukasa, arXiv 2301.12241 / IMA JNA 46(4) 2026.** No backward-stability or forward-error theorem for multivariate V+A, and no analysis of the computed Hessenberg matrices.
   - §2: "By construction, the discrete orthogonal basis φ spans the polynomial space P_n^1". This is an exact-arithmetic, univariate statement.
   - §2.1 / Remark 3 (§5.1): the CGS2 loss-of-orthogonality bound ε_m = O(MN^{3/2}u) on ‖Q*Q − I‖, citing Higham Thm 19.4 and "[15, Thm 2]". ε_m enters only the near-optimality (fit) bound.
   - The "stable with high probability" statement (Theorem 6) is about **sampling**, not rounding.
   - §5.2: "the discrete orthogonal polynomials generated by V+A are unaffected by the ill-conditioning of A". The only basis-versus-exact comparisons (φ_30 against scaled Legendre, §2.3.1 Fig. 2 and Fig. 10) are **1D**. The 2D evidence is fit error only, on tensor and elliptical domains.
   - No triangles or rotated domains appear. Commutativity is not discussed, and nothing is said about the computed span in floating point.
2. **Brubeck–Nakatsukasa–Trefethen 2021 (arXiv 1911.09988).** Univariate, with no proof: §4 calls the two-pass variant an "extremely stable alternative", asserted without proof. §4 also gives the Lanczos caveat. Accuracy is measured end-to-end (the fit only). There is no multivariate section, because §6 is complex 1D.
3. **Hokanson, arXiv 2009.10803, §2.1, Alg. 2.1.** No claim about rounding error, about the accuracy of the recurrence matrices, or about the span in floating point. Its selection rule is "the smallest k such that I[k] + e_j = I[ℓ+1]" (the text and the algorithm differ, ℓ vs ℓ+1). The multivariate extension is credited to Austin et al.
4. **Austin et al., Comput. Phys. Commun. 261 (2021) 107663, §3.2.** This is a multivariate Stieltjes process with "the standard technique of performing the orthogonalization twice". It makes no stability analysis, and the ordering is chosen for convenience.
5. **L.-H. Zhang, Y. Su, R.-C. Li, "Accurate polynomial fitting and evaluation via Arnoldi", NACO 14(3) (2024) 526–546.** This is **the only rounding-error theorem found for V+A**.
   - It is univariate and real. Thm 3.1 bounds the forward error of the **fitted/evaluated values**. Lemma 3.1 is the Arnoldi residual relation ‖F‖_F ≤ √n‖X‖u.
   - The distance of Q̂ or Ĥ from the exact basis or recurrence is **not bounded**. Remark 3.2 says only κ₂(Q̂) enters.
   - Its multivariate confluent follow-up (Zhang–Zhang–Yang–Wu, arXiv 2404.09266) has no finite-precision result. It uses the same smallest-index selection.

**1D background on "the computed space is a different space".**
- With full reorthogonalization, 1D Arnoldi is backward stable: the computed basis is an exact Krylov basis of a nearby matrix. This is DGRS BIT 35 (1995), metadata only, so the claim is from background knowledge and was not read here.
- The distance of that space from the exact one is then a Krylov-subspace conditioning question: Carpraux–Godunov–Kuznetsov LAA 248 (1996) 136–160 and Kuznetsov LAA 265 (1997) 1–28 (citations confirmed via the Malyshev–Sadkane reference list; not read); Paige–Van Dooren 1999 (record 049).
- Without reorthogonalization, Paige 2010 (SIMAX 31, Thm 3.1, Cor. 3.4, read via WebFetch) shows the computed vectors span a Krylov space of an **augmented** matrix. It explicitly gives no distance to the Krylov space of A.
- Stewart (CS-TR-4247, 2001, Thm 3.2, Cor. 3.3) computes the minimal backward perturbation making a given subspace Krylov. He calls bounding the angle to the nearest Krylov subspace "a seemingly difficult and currently unsolved problem" (as digested).

**Relation.**
- No published claim found says multivariate V+A computes S_n to rounding accuracy. The papers prove or measure fit accuracy, loss of orthogonality, or 1D basis accuracy only. **Nothing found contradicts or subsumes (a).**
- (a) is consistent with accurate fits. A basis of a nearby space still gives near-optimal least squares as long as that space approximates f as well, and ZN/Zhang–Su–Li measure only fits.
- ZN §5.2's "unaffected" sentence is the closest tension. It is supported only by 1D basis comparisons and by 2D fit errors, so it does not address 2D span accuracy.
- The 1D analogue is known: backward stability, then Krylov conditioning. The 2D-specific content of (a) was not found in the documented search. That content is the drift with full CGS2 on non-product sets, a drift that tracks working precision and that no reorthogonalization removes.
- **Selection mapping (my reading, to be checked by the developer).** In the campaign code, 'dev' (= BJ) forms (t,0) = X·(t−1,0) and (t,j≥1) = Y·(t−1,j−1). With a within-degree ordering x^{t−j}y^j, Hokanson's (and Zhang et al.'s) smallest-index rule picks exactly that parent. So L2's "fullcgs2 + dev" appears to coincide with Hokanson Alg. 2.1 and ZN's V+A, up to the within-degree order convention (not verified).

**Verdict: partially known.**
- The 1D mechanism is known: backward stability plus Krylov-space conditioning.
- That V+A fits are accurate despite imperfect bases is known (Zhang–Su–Li; ZN fit experiments).
- For 2D span drift under full reorthogonalization, scaling with u and not removed by reorthogonalization: no matching result found in the documented search.
- Not contradicted by any V+A theorem read.
- **Caveat:** ZN Appendix B (Alg. 4/5) was not seen. Its multivariate evaluation via stored H's is the place where a span/H-accuracy remark would sit.

## (b) Reference-free lower bound θ ≥ δ_J/(2‖J‖) from the commutator/consistency residual; not reset by reorthogonalization

**Closest prior statements.**
1. **Stewart, CS-TR-4247 (2001), Thm 3.2 / Cor. 3.3.** The residual S = (I − UU*)AU of a subspace decides whether the subspace is Krylov (rank S ≤ 1). Stewart gives a minimal backward perturbation in terms of S, but **no forward angle bound**, which he calls unsolved.
   - This is the same "residual of a nesting/invariance relation" idea for one operator.
   - Here the relation is J S_s ⊂ S_{s+1} for a *given* exact family, which makes a forward lower bound elementary.
2. **Paige 2010.** Augmented backward stability of one-operator Lanczos (structure, not an angle bound).
3. **Commuting-matrix literature.**
   - Lin's theorem (record lin-1997): small commutator implies a nearby commuting pair.
   - He–Kressner–Plestenjak 2025 (record): joint diagonalization of nearly commuting matrices.
   - Liu–Narayan 2023 (v2 via par.nsf, digest): the commuting conditions (6a–6c) are imposed as algorithm constraints and checked only through orthogonality, not as an error indicator.
   - Xu TAMS 1994, Lemma 4.4 (record): commutation equals compatibility equations (2.4)–(2.6).
4. **Polynomial-system solvers.**
   - Telen–Mourrain–Van Barel (arXiv 1803.07974) assess accuracy by residual/backward error. They do **not** use the commutator.
   - Heldt–Kreuzer–Pokutta–Poulisse (2006 preprint) build approximate border bases from evaluation vectors on points via SVD. They use **no** commutator criterion.

**Relation.**
- The inequality is an elementary residual-to-angle perturbation bound (the "easy direction" of Davis–Kahan type arguments). It applies because (I − P_{s+1})J P_s = 0 holds exactly.
- I did not find it stated for graded total-degree spaces, nor used as a reference-free certificate for multivariate V+A or Lanczos output.
- No source found states that reorthogonalization coefficients leave the commutator/consistency residual unchanged (the clamped shadow recursion, PD-T?…-202/-205).
- The commutator of computed multiplication matrices as an accuracy indicator was **not** found in the normal-form papers read. Kreuzer–Poulisse–Robbiano 2009, Stetter 2004 and Corless–Gianni–Trager 1997 were not read, and are the most likely places.

**Verdict: partially known.**
- The ingredients are known: elementary subspace perturbation; commutation equals Favard compatibility (Xu); near-commuting theory (Lin).
- No matching result found in the documented search for:
  - the bound as stated;
  - its use as a reference-free drift certificate;
  - the non-reset property under reorthogonalization.
- Read KPR 2009 and Stetter before a priority statement on "commutator as error indicator".

## (c) Simon-type semi-orthogonality theorem for the formed (x) sections; PRO-2D at 0.16–0.71 of CGS2-against-all

**Closest prior statements.**
1. **Simon, Math. Comp. 42 (1984).** Thm 2, p. 119: semiorthogonality at √u ⇒ T_j is the projection "up to roundoff"; the proof is deferred (record 211). The ω-recurrence and partial reorthogonalization are in §§4–10; the cost is about 20% of full reorthogonalization (Table 10.3, record 212).
   - **Simon LAA 61 Thm 5 is still unread** (ScienceDirect blocked again).
2. **Jia–Li, Numer. Algorithms 2021 (arXiv 2001.04402, fulltext via WebFetch).**
   - Def. 3.1 sets the level ω₀ = √(ε/(2k+1)). Local orthogonality is assumed in (2.11)–(2.12). Thms 3.3/3.4 give B_k = M_kᵀQ_AN_k + O(ε) and B̂_k up to O(‖B̂_k⁻¹‖ε).
   - JBDPRO uses Larsen-type coupled recurrences, η = ε^{3/4}, and runs at 55–81% of the full-reorthogonalization time.
   - The process is driven by **one** operator (QQᵀ on the stacked (A; L)) with two coupled bidiagonalizations. It has no commuting operators, no growing blocks and no implicit sections.
3. **Larsen 1998 (PROPACK)**: secondary account only.

**Relation.**
- (c) is a transcription of the Simon/Larsen/Jia–Li template to two commuting coordinate operators. Its hypotheses have the same shape: semiorthogonality plus local orthogonality ⇒ O(u) projected-section accuracy.
- The new ingredients are:
  - the restriction to the **formed** sections;
  - the failure for the implicit J-section, which connects to (b);
  - the trigger needing measured J-rows, because commutator sources dominate after reorthogonalization (PD-N?…-202).
- The cost ratio 0.16–0.71 is in the same range as Simon (≈ 0.2) and Jia–Li (0.55–0.81). It is a measurement in a new setting, not a new kind of result.

**Verdict: partially known.** The template is known (Simon; Jia–Li for a matrix pair). For a two-commuting-operator / graded-block version, and the formed-versus-implicit split: no matching result found in the documented search. The JBD analogue is the closest predecessor and must be cited as such.

## (d) Selection-rule dependence of drift and loss

**Closest prior statements.**
- **BPS 2010.** Remark 9, p. 413, and §5, pp. 415–416 (record 302): the choice of variable affects rounding error in monic-OP evaluation; two heuristic strategies; no growth or geometry analysis.
- **Hokanson §2.1.** "many orderings do not satisfy this constraint!" This is about the exact-arithmetic span property.
- **Austin et al. §3.2, ZN §3 ("carefully selecting one coordinate") and Zhang et al. 2404.09266 eq. (2.2).** These give fixed rules, justified structurally, with no numerical-effect analysis.
- **Liu–Narayan.** The all-relations alternative (L1 review (c)).

**Relation.** That the selection is a numerical degree of freedom is known: BPS for evaluation. In the V+A literature the selection is fixed by structure. Not found:
- the effect of the selection on span drift under full reorthogonalization;
- the coupled residual recursion for general one-relation selections (PD-T?…-205);
- the measured ranking adapt ≪ alt ≪ dev < mirror, with two-relation best except on the cubic checkerboard.

**Verdict: partially known.** The selection freedom and its effect on rounding are known (BPS 2010). For its effect on span drift and J-closure under full reorthogonalization: no matching result found in the documented search.

---

## Direct answer: does ZN / BNT / Hokanson prove a stability that contradicts or subsumes (a)?

**No**, in the parts read. None proves that the computed Q̂ spans S_n, or that computed recurrence matrices are accurate, in 2D.
- ZN's rounding content is the CGS2 orthogonality bound feeding a fit bound. Its basis-accuracy evidence is 1D.
- BNT is 1D and gives no proof.
- Hokanson makes no stability claim.
- The one V+A rounding theorem (Zhang–Su–Li 2024) bounds fitted values only, in 1D.

So (a) is a span statement and the literature makes fit statements. Both can hold at once.

**Required check:** ZN Appendix B (Alg. 4/5, evaluation from stored H's) remains unseen.

## Flags

1. **Zhang–Su–Li 2024** is the only rounding analysis of V+A. Cite it to separate fit accuracy from span accuracy.
2. **ZN §5.2 "unaffected by ill-conditioning"** is the closest contrary-sounding claim. Quote it with its 1D support when stating (a).
3. **Stewart CS-TR-4247** gives the 1D residual/backward view and says the forward angle problem is open. Cite it for (b) as context.
4. **Jia–Li 2021** is the closest predecessor of the (c) theorem; cite it alongside Simon.
5. **Unread, potentially limiting:**
   - Kreuzer–Poulisse–Robbiano 2009 and Stetter 2004 (commutator of approximate multiplication matrices), for (b);
   - Simon LAA 61 Thm 5, for (c);
   - ZN Appendix B, for (a);
   - Braconier–Langlois–Rioual 2000, for the 1D background of (a).

## Recommended literature records

| Key | Citation | URL / DOI | Coverage now |
|---|---|---|---|
| zhang-su-li-2024 (new) | L.-H. Zhang, Y. Su, R.-C. Li, "Accurate polynomial fitting and evaluation via Arnoldi", Numer. Algebra Control Optim. 14(3) (2024) 526–546 | doi:10.3934/naco.2023002; https://par.nsf.gov/servlets/purl/10547074 | fulltext via WebFetch (Thm 3.1, Lemma 3.1, Remark 3.2) |
| zhang-zhang-yang-wu-2024 (new, minor) | L.-H. Zhang, Y.-N. Zhang, L. Yang, Y. Wu, "Multivariate confluent Vandermonde with G-Arnoldi and applications", arXiv:2404.09266 | arXiv | fulltext via WebFetch (selection eq. (2.2), Remark 3.1) |
| austin-et-al-2021 (new; L1 "pending") | A. P. Austin, M. Krishnamoorthy, S. Leyffer, S. Mrenna, J. Müller, H. Schulz, "Practical algorithms for multivariate rational approximation", Comput. Phys. Commun. 261 (2021) 107663 | doi:10.1016/j.cpc.2020.107663; eScholarship qt6dn0k7d8 | §3.2 via WebFetch |
| stewart-2001-krylov-backward (new) | G. W. Stewart, "Backward error bounds for approximate Krylov subspaces", UMD CS-TR-4247 / UMIACS-TR-2001-32 (2001) | https://drum.lib.umd.edu/handle/1903/1133 | fulltext via WebFetch (Thm 3.2, Cor. 3.3) |
| paige-2010-augmented (new) | C. C. Paige, "An augmented stability result for the Lanczos Hermitian matrix tridiagonalization process", SIAM J. Matrix Anal. Appl. 31(5) (2010) 2347–2359 | https://www.cs.mcgill.ca/~chris/pub/Pai10.pdf | fulltext via WebFetch (Thm 3.1, Cor. 3.2–3.4) |
| carpraux-godunov-kuznetsov-1996 (new, pending) | J.-F. Carpraux, S. K. Godunov, S. V. Kuznetsov, "Condition number of the Krylov bases and subspaces", Linear Algebra Appl. 248 (1996) 136–160 | — | citation only (Malyshev–Sadkane ref. list) |
| kuznetsov-1997 (new, pending) | S. V. Kuznetsov, "Perturbation bounds of the Krylov bases and associated Hessenberg forms", Linear Algebra Appl. 265 (1997) 1–28 | — | citation only |
| drkosova-et-al-1995 (new, pending) | J. Drkošová, A. Greenbaum, M. Rozložník, Z. Strakoš, "Numerical stability of GMRES", BIT 35(3) (1995) 309–330 | doi:10.1007/BF01732607 | metadata only |
| heldt-kreuzer-pokutta-poulisse (new, minor) | D. Heldt, M. Kreuzer, S. Pokutta, H. Poulisse, "Approximate computation of zero-dimensional polynomial ideals" (preprint 2006; J. Symb. Comput. 2009 per search hits, not verified) | Passau PDF | via WebFetch (Thm 3.1, Cor. 3.3; no commutator criterion) |
| telen-mourrain-vanbarel-2018 (new, minor) | S. Telen, B. Mourrain, M. Van Barel, "Solving polynomial systems via truncated normal forms" (arXiv:1803.07974) | arXiv | via WebFetch (no commutator indicator; residual/backward error) |
| zhu-nakatsukasa-2026 (upgrade) | as recorded | arXiv:2301.12241 | add: no rounding theorem; Remark 3 ε_m; Thm 6 is sampling; §5.2 quote with 1D support; App. B not seen |
| jia-li-2021 (upgrade) | as recorded | arXiv:2001.04402 | add: Def. 3.1 ω₀ = √(ε/(2k+1)), Thms 3.1/3.3/3.4, single-operator QQᵀ, cost 55–81% |
| hokanson-2020 (upgrade) | as in L1 review | arXiv:2009.10803 | add: selection "smallest k" = campaign 'dev' (mapping to verify); no stability claims |
| pending reads | Kreuzer–Poulisse–Robbiano 2009 ("From oil fields to Hilbert schemes"); Stetter, *Numerical Polynomial Algebra* (2004); Braconier–Langlois–Rioual LAA 309 (2000); Simon LAA 61 Thm 5; Reichel SIMAX 12 (1991) | — | not read |
