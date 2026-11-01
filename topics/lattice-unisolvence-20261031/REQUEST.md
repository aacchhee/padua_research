Codex (Sol 6.1 xhigh): New topic: exploratory campaign "Unisolvent lattice subsets beyond checkerboards — character patterns, axis factorization and three dimensions" in aacchhee/padua_research. Branch codex/lattice-unisolvence-20261031.

Rules and base: read AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md and record the SHA.
- Base this branch on codex/charter-unisolvence-20261031 at eb7bdcd, NOT main, because it builds on PD-T001/T002/T003 there. It is a stacked topic: its PR merges only after that branch's PR.
- Record the dependency, the merge order and all ID reservations in the shared ledger topics/padua-batch-20261031/ALLOCATIONS.md, used by the other open topics: charter-unisolvence, bivariate-lanczos, mz-constants, programme-ideas.
- Never rewrite or push to the base branch. If it changes after an audit, merge it in, never rebase.
- Do not edit the charter text; add a tracks/unisolvence/ subsection or a new track tracks/lattice-unisolvence/, plus one CURRENT.md paragraph at PR preparation.

Explicit AC instructions for this campaign (they take precedence over the default gate wording where they differ, as AGENTS.md allows):
- Step 0 is a literature baseline for this question: record sourced statements in literature/ (LIT? provisional IDs; anything not checked against a fulltext is marked UNVERIFIED). Exploration may then run before a full duplicate screen, but each candidate records its closest predecessor and kill test. Every candidate gets a prior-art check and an independent adversarial reconstruction (separate gpt-6-astra high/xhigh agent) before acceptance.
- Up to ten conceptual rounds per direction, with a justified extension to at most twenty; at most two substantive directions at a time; automatic continuation while a concrete opening survives. Ultra only for especially hard mathematics, with the reason written first.
- Status words and evidence rules unchanged:
  - Exact rank checks at random nodes are MEASURED for generic statements unless a proved reduction (e.g. Schwartz–Zippel with a written degree bound and a recorded failure probability, or a symbolic identity) turns them into a proof.
  - Lebesgue constants computed in floating point are MEASURED.
  - A computer proof needs a proved finite reduction, exact arithmetic, a committed checker and an independent rerun.
  - A paywalled load-bearing source → "pending-reference", not a stop.
- Preserve every candidate, failed pattern, correction and side note. Scoped PD-N only for refuted mechanisms with evidence; a measured failure over a finite range does not become a universal negative.
- Cold storage (AC's choice): C:\Users\andreyac\Downloads\padua\cold_storage\<slug>\, with manifests per templates/COLD_STORAGE.md. Large searches may go to AC's NTNU servers (syvert0/1/2) through "Runs needed" with exact commands.
- The repository is public: never commit third-party PDFs or fulltext extracts.
- Out of scope: Lanczos/recurrence finite-precision theory; MZ constants; the bivariate moments → OPs complexity question (bttb-research); 3D Padua via minimal or near-minimal CUBATURE (Li–Sun–Xu NMTMA 2009 conjecture ≥ n³/4 nodes for degree 2n−1) — this campaign seeks interpolation sets, which need no cubature property.

Starting point (on the base branch; developer PROVED, Claude audit pending):
- PD-T001: in characteristic ≠ 2, for distinct labelled X (length m+1), Y (length m+2) and the parity subset S_e = {(x_i,y_j): i+j ≡ e mod 2}:
    det(V_e)²·∏ w_i(X)w_j(Y) = 2^{−N}∏ Δ_r(X)Δ_r(Y), with w_i = (−1)^i/ω′(h_i) and Δ_r the alternation Hankel minors.
  So unisolvence is decided axis by axis.
- PD-T002: the all-field version via even-index barycentric functionals B_H.
- PD-T003: kernel and product cubature through degree 2m.
- Attribution: a reformulation of the known axis determinant factorization (De Marchi–Usevich 2014; de Camargo–De Marchi 2015).
- Background: Padua points are the Chebyshev–Lobatto case, with Lebesgue constant (4/π²)log²n + O(log n).
Treat base-branch results as external until their audit is accepted; re-check whatever is load-bearing here.

Non-triviality: any lower set {i+j ≤ n} of a product grid is unisolvent for Π_n with arbitrary distinct nodes (Biermann; Chung–Yao natural lattices 1977; Gasca–Maeztu GC sets 1982; Carnicer–Gasca). Unisolvence alone is therefore not a result. A pattern counts only if it is
- (a) periodic / character-defined on the index lattice (like the checkerboard), and
- (b) has an axis-factorized determinant or an analogous structural criterion, and/or
- (c) for Chebyshev-type nodes has a Lebesgue constant growing polylogarithmically, or at least far slower than lower sets.
Report all three properties for every pattern.

Directions (choose, merge, reorder or replace; freeze each first question in plan.md before launch):
- C0. Counting and catalogue.
  - Enumerate index patterns that have exactly dim Π_n^d points, for d = 2 and d = 3: dim Π_n³ = C(n+3,3). Candidates are subsets of grids L_1×…×L_d cut out by congruences or character level sets, {i : χ(i) = c} for characters χ of (Z/k)^d, possibly unions of cosets or boundary-corrected versions.
  - Record the admissible (L_1, …, L_d, k, χ, c) families and the counting identities; rule out families by counting where possible.
  - Cheapest decisive test first: does any d = 3 character pattern with the right cardinality exist for infinitely many n?
- C1. Character-pattern unisolvence in 2D beyond index 2.
  - For index-k patterns (k = 3, 4, …) in X×Y grids of suitable sizes, with weights carrying k-th roots of unity (generalizing (−1)^i), seek a determinant identity factoring into axis-wise Hankel or Toeplitz-type minors.
  - Test generic unisolvence by exact rank at random nodes over several primes and over Q; then attempt the PD-T001 proof template (Lagrange identities plus triangular tensor Gram factorization).
  - Note which fields contain the needed roots of unity; relate to the finite-field Padua results (tracks/unisolvence/theory/u0/).
- C2. Known 2D families as test cases: Xu points, Morrow–Patterson, Lissajous / Lissajous–Chebyshev (degenerate and non-degenerate; Erb, Dencker–Erb) and Harris-type alternation sets. Which are total-degree unisolvent for arbitrary distinct axis nodes, which only for special nodes, and does an axis-factorization criterion exist for them?
- C3. Three dimensions — the main target.
  - Find periodic/character patterns in X×Y×Z with C(n+3,3) points that are generically unisolvent for Π_n³. Prove axis factorization, or a scoped obstruction.
  - For Chebyshev–Lobatto axes, measure Lebesgue constants against known 3D sets: approximate Fekete/Leja from weakly admissible meshes, the trivariate Lissajous extraction of Bos–De Marchi–Vianello 2017 ("we cannot obtain total-degree polynomial interpolation" by the curve itself), the De Marchi–Vianello–Xu 2009 3D hyperinterpolation nodes, and the Cools–Poppe Chebyshev lattices.
  - Cheapest decisive test: exact rank over F_p (several primes) at random axis nodes for n ≤ 6, every admissible C0 pattern. A pattern failing for all n ≤ 6 gets a scoped negative record.
- C4. Structure and consequences, for any surviving pattern: kernel/Lagrange formulas, product-type discrete functionals with cubature-like exactness (as in PD-T003), the vanishing ideal and its generators (cf. Bos–De Marchi–Vianello–Xu 2007 for Padua), fast transforms over C and over finite fields, and the Lebesgue constant theory (log^d?).

Literature baseline (Step 0; check fulltexts where possible):
- unisolvence: Chung–Yao 1977; Gasca–Maeztu 1982; Carnicer–Gasca; Biermann;
- Padua theory: Bos–Caliari–De Marchi–Vianello–Xu 2006; Bos–De Marchi–Vianello–Xu 2007;
- known 2D and lattice families: Xu 1996 (Chebyshev points of two variables); Morrow–Patterson 1978; Harris 2015/2018; Harris–Simanek 2021 with Cao–Ghimire–Wang 2022; Cools–Poppe 2011;
- 3D attempts: Dencker–Erb 2017 (d-dimensional Lissajous–Chebyshev); Bos–De Marchi–Vianello 2017 (trivariate Lissajous); De Marchi–Vianello–Xu 2009; Li–Sun–Xu 2009;
- determinant factorization: De Marchi–Usevich 2014; de Camargo–De Marchi 2015;
- open-problem statements: De Marchi 2022 survey (Constr. Math. Anal. 5(1); "we do not know the Padua points on [−1,1]^d, d ≥ 3"); Xu, arXiv 2407.09903.

Deliverables:
- the literature baseline;
- IDEA records for every pattern tried;
- plan.md, with directions, frozen first questions and a round ledger;
- progress.md;
- one folder per direction with round records;
- theory files with provisional PD-T?/PD-N? IDs;
- exact checkers with small outputs;
- report.md ranking survivors with development briefs, and stating plainly whether any 3D candidate survives;
- an audit handoff for Claude.
Give the usual progress updates. At the end set Stage AUDIT and Next: `Claude (Opus 5.5 xhigh): Continue codex/lattice-unisolvence-20261031.`