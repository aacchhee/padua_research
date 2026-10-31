# Plan — bivariate Lanczos campaign

Rules `d36722823441dc40c6e19d69a174459348dd309c`. Orchestrator Claude. Frozen 2026-10-31 before any direction launch; changes after freezing go to History with the reason.

## Object and notation (fixed for all directions)

Distinct nodes z_i = (x_i, y_i) ∈ ℝ², i = 1..M; weights w_i > 0; X = diag(x_i), Y = diag(y_i), commuting and symmetric; start vector q_0 = √w/‖√w‖. Π_n = real bivariate polynomials of total degree ≤ n, graded (total-degree, then a fixed within-degree) order; N_n = dim Π_n|_nodes ≤ (n+1)(n+2)/2. The truncated recurrence (Weisfeld 1959; Bartels–Jezioranski 1985; Huhtanen–Larsen BIT 2002) builds the orthonormal Q = [Q_0 | Q_1 | … | Q_n] (Q_k = degree-k block) by orthogonalising products x·q and y·q of degree-k vectors against a window of at most 2k+1 earlier vectors (HL BIT Thm 2.3, as reported; to be checked in the literature records). Sections: H_x = QᵀXQ, H_y = QᵀYQ (N_n × N_n, block tridiagonal in exact arithmetic); only part of H_y is formed by the recurrence. Cost O(M N^{3/2}). Context: Van Barel & Chesnokov, Numer. Algorithms 55 (2010) 383–402 (Givens IEP).

Labels used throughout: **[EXACT]** exact arithmetic; **[FP]** floating point with unit roundoff u; **[IDEALIZED: …]** labelled scaffolding (generic nodes, supplied commuting extensions, oracle spectra, perturbations given as data). Floating-point experiments are MEASURED only.

## Directions, slots and order

At most two substantive directions run at once. Slot assignment:

| Slot | Direction | Status | Model |
|---|---|---|---|
| 1 | **L1+L4** Paige-type theory, with the placement question L4 answered inside L1 (it decides which single-operator/block theory transfers) | launch after Step 0 | Opus 5.5 xhigh |
| 2 | **L3** backward interpretation / commuting extensions | launch after Step 0 | Opus 5.5 xhigh |
| side | **L5** Givens deficit and pivot rules (AC: "short-note side direction"; treated as non-substantive, run alongside) | launch after Step 0 | Sonnet 5.5 high |
| queued | **L2** provable partial/selective reorthogonalization | deferred until L1 yields a usable local-relation/bound statement or a slot frees | Opus 5.5 xhigh (theory), Sonnet 5.5 high (code) |

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

## ID allocation

Provisional IDs `<NS>?bivariate-lanczos-claude-<nnn>`: literature 001–199 (fulltext-read records 101–199); IDEA seeds 001–099; direction-local ranges L1 100s, L2 200s, L3 300s, L4 400s, L5 500s for IDEA/PD-T/PD-N. Final IDs only at PR preparation via `topics/padua-batch-20261031/ALLOCATIONS.md`, shared with `codex/charter-unisolvence-20261031`.

## Round ledger

| Direction | Round | Date | Question | Outcome (status-labelled) | Record |
|---|---|---|---|---|---|

## History

- 2026-10-31: plan frozen before launch (orchestrator).
