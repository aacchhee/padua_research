# Plan — bivariate Lanczos campaign

Rules `d36722823441dc40c6e19d69a174459348dd309c`. Orchestrator Claude. Frozen 2026-10-31 before any direction launch; changes after freezing go to History with the reason.

## Object and notation (fixed for all directions)

Distinct nodes z_i = (x_i, y_i) ∈ ℝ², i = 1..M; weights w_i > 0; X = diag(x_i), Y = diag(y_i), commuting and symmetric; start vector q_0 = √w/‖√w‖. Π_n = real bivariate polynomials of total degree ≤ n, graded (total-degree, then a fixed within-degree) order; N_n = dim Π_n|_nodes ≤ (n+1)(n+2)/2. The truncated recurrence (Weisfeld 1959; Bartels–Jezioranski 1985; Huhtanen–Larsen BIT 2002) builds the orthonormal Q = [Q_0 | Q_1 | … | Q_n] (Q_k = degree-k block) by orthogonalising products x·q and y·q of degree-k vectors against a window of at most 2k+1 earlier vectors (HL BIT Thm 2.3, as reported; to be checked in the literature records). Sections: H_x = QᵀXQ, H_y = QᵀYQ (N_n × N_n, block tridiagonal in exact arithmetic); only part of H_y is formed by the recurrence. Cost O(M N^{3/2}). Context: Van Barel & Chesnokov, Numer. Algorithms 55 (2010) 383–402 (Givens IEP).

Labels used throughout: **[EXACT]** exact arithmetic; **[FP]** floating point with unit roundoff u; **[IDEALIZED: …]** labelled scaffolding (generic nodes, supplied commuting extensions, oracle spectra, perturbations given as data). Floating-point experiments are MEASURED only.

## Directions, slots and order

At most two substantive directions run at once. Slot assignment:

| Slot | Direction | Status | Model |
|---|---|---|---|
| 1 | **L1+L4** Paige-type theory, with the placement question L4 answered inside L1 (it decides which single-operator/block theory transfers) | R01–R07 done; paused 2026-10-31 (3 rounds left) to free the slot for L2 | Opus 5.5 xhigh |
| 2 | **L3** backward interpretation / commuting extensions | R01–R06 done; paused 2026-10-31 (4 rounds left) pending reconstruction 02 | Opus 5.5 xhigh |
| side | **L5** Givens deficit and pivot rules (AC: "short-note side direction"; treated as non-substantive, run alongside) | launch after Step 0 | Sonnet 5.5 high |
| queued → 1 | **L2** provable partial/selective reorthogonalization | launched 2026-10-31 in slot 1 after L1 paused at R07 | Opus 5.5 xhigh (theory and modest experiments) |

Rounds: ≤10 conceptual rounds per direction; extension to ≤20 only with a written justification in the direction's round ledger. Automatic continuation while a concrete opening survives. One round = one recorded attempt that ends with a dated round record `directions/<D>/R<nn>.md` (question, attempt, result with status labels, failed routes, next question).

## Frozen first questions

### L1-Q1 (with L4-Q1)

**L1-Q1.** In [FP], for the BJ window recurrence (classical Gram–Schmidt, no reorthogonalization) and the HL variant, write the exact local relations X Q = Q H_x + (boundary) + F_x and Y Q = Q H_y + (boundary) + F_y with the actual computed coefficient pattern (which entries of H_y are formed, which are implicit), and decide **whether loss of orthogonality is governed by Ritz pairs of a single section (H_x or H_y, as per-operator block-Paige theory would give) or genuinely needs joint Ritz pairs of Z = H_x + iH_y** (HL SIMAX 2002 p. 1088, as reported).
- Cheapest decisive test: compare measured max|QᵀQ − I| with the minimal Ritz residual of H_x, of H_y and of Z, on random, tensor-Chebyshev, Padua-with-cubature-weights and an irregular-domain node set (M ≤ ~10⁴ locally).
- Kill test (written before testing): if a single-section Ritz residual predicts loss as well as Z (same factor-3 band), the "joint Ritz" formulation is not the governing object and L1 reduces to per-operator (block) Paige theory; if no Ritz residual predicts it outside the input's three node sets, the measured relation is not a mechanism.
- Closest predecessors: Paige 1971/1976/1980; block Lanczos Paige identity (Sinha 2026; Šimonová–Tichý 2025, as reported); HL SIMAX 2002 conjecture.

**L4-Q1.** Can the graded spaces span{p(X,Y)q_0 : deg p ≤ n} (all n) be produced as a band/block Krylov sequence of **one** symmetric operator with an n-independent number of starting vectors? If not, give the obstruction and identify which band/block-Lanczos finite-precision statements (block Paige identity; block Gram–Schmidt stability, Carson et al. arXiv 2408.10109; Šimonová–Tichý) transfer to the form "Lanczos for X with injected vectors from Y".
- Kill test: an explicit operator A = f(X, Y) and fixed start block reproducing the graded spaces for all n kills "genuinely different".

### L3-Q1

Given [IDEALIZED: perturbations given as data] computed sections (Ĥ_x, Ĥ_y) of degree n that satisfy the exact structural zero pattern and the recurrence relations up to O(ε), **does there exist a positive discrete measure μ′ supported within distance δ of the original nodes whose exact degree-n sections equal (Ĥ_x, Ĥ_y) up to O(ε)** (a Greenbaum-type backward interpretation)? Decide, separately for the overdetermined case (M ≥ dim Π_{2n+1}, generic nodes) and the square case M = N_n (Padua), either an existence statement with an explicit δ(ε) or an explicit obstruction family.
- Kill test: an explicit small-n perturbation satisfying all interior commutativity conditions but admitting no representing measure in any δ-neighbourhood with δ → 0 as ε → 0 establishes an obstruction (for that case); a construction that always works with δ = O(ε) kills the obstruction claim and moves the question to constants and support size.
- Closest predecessors: Greenbaum 1989; quantitative Lin's theorem (Kachkovskiy–Safarov 2016); commuting extensions (Degani–Schiff–Tannor 2005); Xu 1994 block Jacobi commutativity conditions; truncated moment problem / flat extension (Curto–Fialkow); Koiran 2024 ("wide open" two-matrix case, as reported). Link to cubature existence to be recorded.

### L5-Q1

Does the 2010 Givens point-by-point updating have error growing ∝ M (O(M) rotations per entry) while HL, CGS2 and Householder grow ∝ √M, **measured** over M from 66 to ≥ 2000 with ≥ 5 node orders/seeds on Padua (cubature and random weights) and random nodes; and is the "larger redundant pivot" catastrophe (≈ 7e-4 on Padua n = 20, random weights, as reported) present **only** on orders with non-unisolvent intermediate prefixes?
- Kill test: fitted Givens slope ≤ 0.7 on the larger range, or HL/CGS2 slopes ≥ 0.9, kills the rotation-counting explanation; a catastrophe on an order whose prefixes are all unisolvent kills the prefix mechanism.
- Closest predecessors: Higham ASNA ch. 18–19 (rotation/Householder error analysis); seed paper p. 392 pivot heuristic; Humet/ETNA 2014 heuristic (as reported).

### L2-Q1 (frozen now, launched later)

Does an ω-recurrence (Simon 1984 template) derived from the L1 local relations track measured |QᵀQ − I| within a constant factor on the L1 benchmark set, and does maintaining semi-orthogonality √u guarantee sections accurate to O(u)·‖(X, Y)‖ (Simon's theorem analogue)? Kill test: an ω-estimate that underestimates measured loss by > 10× on any benchmark, or a semi-orthogonal run with section error ≫ u, kills that criterion. Cost comparison against full reorthogonalization O(M N²) and CGS2 / Vandermonde-with-Arnoldi (Zhu–Nakatsukasa, IMA JNA 46 (2026)). Runs with M ≈ 10⁶ go to AC's servers (syvert0/1/2) as Runs needed.

## Benchmarks

Exact families with closed-form sparse recurrences: Padua points with cubature weights (`closed_form_H.py`), Harris–Simanek checkerboard sets (`harris_simanek_check.py`); plus random, tensor-Chebyshev and irregular-domain node sets.

- **Ordered nodes required (AC correction, 2026-10-31).** Harris–Simanek checkerboards S_e = {(x_i, y_j) : i + j ≡ e} are used only with **ordered (monotone) real** X (length m+1) and Y (length m+2); unordered labels can lose unisolvence (X = (0,1,2), Y = (0,1,3,2): rank 5 of 6) and make the alternation weights indefinite. `harris_simanek_check.py` uses monotone lists in all its cases (orchestrator check).
- **Tunable positive M = N family.** For ordered X, Y the alternation weights w_i(H) = (−1)^i/ω_H′(h_i) have constant sign; after a global sign flip, S_e with weights w_i(X)w_j(Y) is a positive discrete measure with M = N points. Reported closed form, **pending external audit**: the graded orthonormal basis is the product p_a(x)q_b(y) of the univariate orthonormal polynomials for (X, w(X)) and (Y, w(Y)), so H_x, H_y are explicit (univariate Jacobi coefficients plus top-degree folding). Source: `codex/charter-unisolvence-20261031` at `eb7bdcd`, PD-T001 (`tracks/unisolvence/theory/u1/odd-characteristic-criterion.md`) and PD-T003 (`.../kernel-cubature-corollary.md`, exactness through degree 2m), developer PROVED with supplementary Astra reconstruction, **not accepted**; cite by branch/SHA/ID only, never as an accepted dependency. The "≤ 3 nonzeros per column" claim of the round-3 notes is to be checked against our own construction.
- Uses: L1/L4 a third structured control (neither tensor nor Padua-special) with conditioning dialled by node clustering/grading; L2 semi-orthogonality tests with known exact sections; L3 a known exact positive representing measure; L5 nested orders S_e(m) ⊂ S_e(m+1) whose prefixes are full checkerboards at each degree milestone (controlled prefix-mechanism test); unordered labels predict singular prefixes for [EXACT] pivot experiments (outside w > 0). Caveat: M = N only; M ≫ N experiments need other node sets.

## ID allocation

Provisional IDs `<NS>?bivariate-lanczos-claude-<nnn>`: literature 001–099 (notes baseline), 101–199 (fulltext-read records), 201–299 (online resolution pass), 301–399 (orchestrator/later records); IDEA seeds 001–099; direction-local ranges L1 100s, L2 200s, L3 300s, L4 400s, L5 500s for IDEA/PD-T/PD-N. Final IDs only at PR preparation via `topics/padua-batch-20261031/ALLOCATIONS.md`, shared with `codex/charter-unisolvence-20261031`.

## Round ledger

| Direction | Round | Date | Question | Outcome (status-labelled) | Record |
|---|---|---|---|---|---|
| L1+L4 | R01 | 2026-10-31 | L1-Q1, L4-Q1 (frozen) | Kill test K1 and K2 both fire (MEASURED); local relations PROVED; L4 obstruction PROVED | [R01](directions/L1/R01.md) |
| L1 | R02 | 2026-10-31 | What governs loss off product supports | Block Paige identity, node-row representation, exact ω-recurrence PROVED; amplification by per-node propagator MEASURED | [R02](directions/L1/R02.md) |
| L1 | R03 | 2026-10-31 | A priori vs feedback; truncation vs row selection | Row-selection characterization PROVED; exact-coefficient growth and two-relation remedy MEASURED | [R03](directions/L1/R03.md) |
| L3 | R01 | 2026-10-31 | L3-Q1 (frozen) | Literal reading trivial; exact reading via moment cone; overdetermined δ = 0 PROVED | [R01](directions/L3/R01.md) |
| L3 | R02 | 2026-10-31 | Square-case rates | δ ≳ √ε necessary PROVED; rate theorem with condition (H) PROVED; Padua n = 2/3 CONDITIONAL | [R02](directions/L3/R02.md) |
| L3 | R03 | 2026-10-31 | Checkerboard control, literature | (H) survey MEASURED; count-alone hypothesis refuted (MEASURED); literature confirmations | [R03](directions/L3/R03.md) |
| L1 | R04 | 2026-10-31 | Near-product upper bound; checkerboard control | Near-product bound PROVED (weak); clustered-checkerboard loss and remedy failure MEASURED (PD-N?…-103) | [R04](directions/L1/R04.md) |
| L1 | R05 | 2026-10-31 | Exact certificates; error channels | Moment-matching factorisation PROVED; triangle-grid growth certificate CONDITIONAL; two error channels MEASURED; corrections PC-1–10 | [R05](directions/L1/R05.md) |
| L1 | R06 | 2026-10-31 | Coefficient-map conditioning (clustered checkerboards) | Off-pattern channel MEASURED; gain identity PROVED (114 parts 1–4) | [R06](directions/L1/R06.md) |
| L1 | R07 | 2026-10-31 | Why actual errors are benign vs generic noise | Closed-loop model MEASURED (115); open-loop estimates fail (PD-N?…-104) | [R07](directions/L1/R07.md) |
| L5 | R01 | 2026-10-31 | L5-Q1 (frozen) | Slopes MEASURED (rotation counting not killed on controlled families); prefix mechanism killed (MEASURED) | [R01](directions/L5/R01.md) |
| L5 | R02 | 2026-10-31 | Worst-case rotation bound | Routine backward bound PROVED (no M vs √M separation) | [R02](directions/L5/R02.md) |
| L5 | R03 | 2026-10-31 | Safe pivot/deflation rules | No rule beats 'scheme' (MEASURED); prefix-extension lemma PROVED; invariant proof OPEN | [R03](directions/L5/R03.md) |
| L3 | R04 | 2026-10-31 | Exact certificates for equispaced checkerboards | (H) certified n = 1..7 CONDITIONAL; margins MEASURED | [R04](directions/L3/R04.md) |
| L3 | R05 | 2026-10-31 | Padua obstruction for all n | Interior lemma PROVED; P_n certificate for n ≥ 4 CONDITIONAL (313/N303) | [R05](directions/L3/R05.md) |
| L3 | R06 | 2026-10-31 | Greenbaum reading (G) | Consistency ⟺ symmetry PROVED (314); asymmetry ≈ forward error MEASURED (315); G OPEN | [R06](directions/L3/R06.md) |

## History

- 2026-10-31: plan frozen before launch (orchestrator).
- 2026-10-31 (L3 R01 scope decision, developer; to be checked by reconstruction and audit): read literally, L3-Q1 ("exact sections of μ′ equal (Ĥ_x, Ĥ_y) up to O(ε)") is trivially answered by μ′ = μ, δ = 0. L3 therefore answers the exact-representation reading (consistent ε-perturbed data represented exactly / with residual smaller than the perturbation). The frozen wording is preserved; both readings and their answers are recorded in theory file PD-T?…-300.
  - Correction (L3 reconstruction 01, finding M1): "the literal question is trivial" is overstated. It is trivial only under the extra assumption that the computed sections are close to the exact ones; read on the sections alone it is trivially negative (exact sections of a far-away measure satisfy every relation); read together with the local relations of the computed basis it is the Greenbaum regime (G), correctly kept OPEN in PD-T?…-300. The exact reading (E) is an openly recorded substitution with a stronger conclusion, not the frozen question itself.
- 2026-10-31 22:12: Benchmarks section updated per AC message (ordered nodes; checkerboard product-OP closed form pending external audit). Frozen questions unchanged.
- 2026-10-31, Step 0 corrections (frozen questions not reworded; these notes govern their interpretation; sources: fulltext records LIT?…-101–162, notes records LIT?…-001–077):
  - HL SIMAX 2002 p. 1088 is an **observation**, not a conjecture: finite-precision behaviour "seems similar" to Lanczos, some loss of orthogonality among vectors of different cycles, "appears closely connected" to convergence of Ritz values of the square part of the section N_k of the normal operator N in the (N, N*) form, eq. (4.2). It mentions neither H_x/H_y separately nor data. That paper's window is 2k (its Thm 3.7); HL BIT Thm 2.3 (p. 397) gives ≤ 2k+1 for commuting symmetric (H, K), exact arithmetic only. O(M N^{3/2}) is not a published statement there (no flop count given).
  - None of the seven fulltexts contains a rounding analysis of the bivariate recurrence. Huhtanen SIMAX 2002 is single-operator Lanczos for a linear-system solver (no bivariate recurrence).
  - Xu SIAM J. Math. Anal. 25 (1994) 991–1001 is the quasi-orthogonal zeros / Gaussian-cubature paper (Thms 3.1, 4.1, 5.1); the block-Jacobi/Favard theory is only recalled there (pp. 993) and lives in Xu's Trans. AMS paper (pending-reference).
  - VB–C pivot remark is on p. 395 (not 392); EGK "no observable pattern" on p. 352 (not 351).
  - Koiran 2024 "wide open" attribution not found in the inputs; the only candidate (arXiv 2401.01302) concerns exact commuting extensions — UNVERIFIED. The Kachkovskiy–Safarov almost-commuting bound attributed in the inputs is not confirmed from the abstract — UNVERIFIED.
