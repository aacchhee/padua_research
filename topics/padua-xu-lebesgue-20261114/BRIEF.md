# BRIEF: Lebesgue constants of Xu points and of Morrow–Patterson points

Written by Claude (claude-opus-5-5), 2026-11-14.

AC's request: "I have resources for one rather extensive Fable round." After the frontier assessment AC wrote: "make a brief for fable 5.2. same branch for both directions 1 and 2. Research on fable 5.2 xhigh, audit opus 5.5. xhigh. Up to ten rounds per direction, researcher in each round may be downgraded to opus 5.5 if the problem does not look challenging."

This file is a knowledge base and a plan, and carries no status of its own.
- Literature items are pointers. Cite one only after a fulltext read, unless an existing LIT record already covers the exact statement.
- Statements marked **verify** are Claude's recollection and must be checked before anything relies on them.

## 0. Why these two problems

PR #27 (open, branch `codex/padua-argmax-bridge-20261105`) proves, for every n ≥ 2, where the Padua Lebesgue function attains its maximum: the two non-node corners. It also proves the sharp corner expansion
Λ = (4/π²)log²N + b log N + c − (…)/N + O(log N/N²), with N = n + ½.
The proof has three parts:
- an analytic corner expansion;
- localization: away from the corners the Lebesgue function is strictly below the corner value, beyond an explicit onset;
- finite certificates below the onset: exact polynomial witnesses for small n, and phase-tree certificates checked by an independent direct-sum checker.

Two sibling problems are published as open and are untouched in this repository. No PD-T or PD-N row mentions Xu or Morrow–Patterson points.

1. **X1, Xu points.** Bos–Caliari–De Marchi–Vianello, *Computing* 76 (2006) 311–324 ([LIT-486](../../literature/records/bcdmv-computing-2006.md), read at pp. 318–319 and 324):
   - p. 318 observes numerically that the Lebesgue function of the Xu interpolation points peaks at the four vertices of the square.
   - p. 319, Conjecture (17): Λ^Xu_n behaves like ((2/π) log(n+1))², with the maximum attained at the four vertices.
   - p. 324 lists this again as open.

   This is the Xu counterpart of what PR #27 settles for Padua points. A proof settles a 20-year-old conjecture. A certified counterexample, a degree where the maximum leaves the vertices, would be an equally clean negative result.
2. **X2, Morrow–Patterson points.** [LIT-378](../../literature/INDEX.md) is UNVERIFIED (a secondary report, not yet checked against the fulltext). It says Beberok–Białas-Cież–De Marchi (*Constr. Approx.* 63 (2026) 31–65; arXiv [2412.14595](https://arxiv.org/abs/2412.14595)) prove Λ_MP = O(n²) and leave the lower bound, and the Xu-type "MPX" variants, open.
   - A matching lower bound Λ_MP ≥ c·n² with an explicit c completes their order result. It may need only one point evaluation with a closed-form asymptotic.
   - The sharp constant lim Λ_MP/n², and where the maximum sits, are stretch goals.

Both problems use the same toolkit: the Chebyshev product measure, closed-form reproducing kernels on Chebyshev–Lobatto grids, Dirichlet-kernel asymptotics, and corner or edge analysis. That is why they share one branch.

## 1. Direction X1: the Xu Lebesgue constant and its maximizers

### 1.1 Objects (verify all definitions against the primary sources first)

- **Sources.**
  - Xu, "Lagrange interpolation on Chebyshev points of two variables", *J. Approx. Theory* 87 (1996) 220–238 (**verify** citation details). This is the original construction: the interpolation space, the compact kernel formula, and the link to the minimal cubature of degree 2n−1 for the product Chebyshev measure of the first kind.
  - Bos–De Marchi–Vianello, "On the Lebesgue constant for the Xu interpolation formula", *J. Approx. Theory* 141 (2006) (**verify**). Proves Λ^Xu_n = O(log² n).
  - BCDMV 2006 (LIT-486). Numerical study, compact formulas, Conjecture (17).
  - Also check Xu's 1996 kernel identities as restated in later Padua papers, e.g. Bos–De Marchi–Vianello–Xu, *Numer. Math.* 108 (2007) (`bos-dmv-xu-2007` in `literature/CORPUS.md`; fulltext still pending there).
- **Points.** The Xu points of degree n are a checkerboard (parity) subset of the (n+1)×(n+1) Chebyshev–Lobatto grid (cos(iπ/n), cos(jπ/n)). The parity class depends on n. Their number is dim Π_{n−1} plus a parity-dependent number of extra functions, chosen so that interpolation is unique in a space Π*_n with Π_{n−1} ⊂ Π*_n ⊂ Π_n. **Verify** the exact parity convention, the cardinality and Π*_n for both parities.
- **Corners.** Under some conventions some of the four vertices are nodes, where the Lebesgue function equals 1. "Maximum at the four vertices" can then only hold for the parity in which no vertex is a node.
  - First task of X1: establish exactly which vertices are nodes, for each parity.
  - Restate Conjecture (17) precisely: argmax set equal to the non-node vertices, and the asymptotic statement. The statement on record is "behaves like ((2/π) log(n+1))²".
  - The Padua analogue has exactly two non-node corners (PD-T101, PD-T229, PR #27).
- **Kernel.** The Xu interpolant has a closed-form fundamental function: the reproducing kernel of Π_{n−1}, or of a slight modification of it, for the product Chebyshev weight, divided by its value on the diagonal, with a parity-dependent correction term. This parallels the Padua kernel K_n(x,y) used throughout PR #27. Sums over the grid become trigonometric sums in the angles (θ, φ), and that is how the Padua corner expansions were done.

### 1.2 Target outcomes, from strongest to weakest

1. **Full analogue of PR #27.** For every n ≥ 2, the exact argmax set of the Xu Lebesgue function on [−1,1]² is the set of non-node vertices, together with a sharp corner expansion Λ^Xu_n = (4/π²)log²n + b_Xu log n + c_Xu + O(…) with explicit constants and remainder. Only use whichever expansion variable (n, n+½, n+1) makes the expansion cleanest.
2. **Asymptotic version.** The argmax set is as above for every n ≥ N_* with N_* explicit, together with certificates for every n < N_*. If N_* is only existential, then the result is "eventually", as PD-T229 was for Padua.
3. **Leading constant only.** Λ^Xu_n ~ (4/π²) log² n, proved; that is Conjecture (17) in its asymptotic sense. This may follow from a corner lower bound plus a matching global upper bound, without locating the argmax.
4. **Negative result.** A degree n where some non-vertex point has a certified Lebesgue value above every vertex value refutes the argmax part of (17). It must be recorded as a PD-N with an interval-certified witness. Then pursue the corrected conjecture: which points maximize, and is the leading constant still 4/π²?

### 1.3 How to reuse PR #27

PR #27 is NOT merged.
- Read it with `git show origin/codex/padua-argmax-bridge-20261105:<path>`.
- Entry points:
  - `topics/padua-argmax-bridge-20261105/paper/main.tex` and its `sections/`: the 51-page Constructive Approximation manuscript, which states the proof architecture;
  - `companion-paper/`: the 147-page explanatory companion;
  - `report.md`: current result at the top;
  - `theory/G01-all-degrees.md`, `theory/H-sharp-corner-expansion.md`, `theory/J01-onset512-gates.md`, `theory/J02-elementary-constant-enclosure.md`;
  - `code/independent_phase_checker/`: the direct-sum certificate checker design.
- Do not read all ~200 `independent-checks-*` files. Open one only when a specific lemma needs its review.
- **Status rule.** Methods may be copied and adapted freely. Any X1 statement that uses an *unmerged PR #27 lemma as a lemma* is CONDITIONAL on that lemma until PR #27 merges, or until the lemma is re-proved inside this topic for the Xu kernel. Re-proving it for the Xu kernel is the normal case, because the kernels differ.
- On main the Padua background is: PD-T101 (corner value), PD-T229 (eventual argmax), PD-T246 (certified 2–32), PD-T269–T271 (three-term expansion), and PD-T674 (corollary, PR #34). Use their records for conventions.

### 1.4 What is expected to be different from Padua

These are guesses to test, not facts.
- The Xu grid is square, (n+1)×(n+1), while the Padua grid is (n+1)×(n+2). The four-fold symmetry of the square may make the vertex analysis cleaner, but the parity-dependent extra functions in Π*_n may create a boundary layer that Padua lacks.
- BdMV's O(log² n) proof gives a global upper bound with a non-sharp constant. The localization step, "far from the corners the Lebesgue function is ≤ (1−δ) × corner value", is where most of PR #27's effort went. Expect the same here.
- The finite range below the analytic onset may again need certificates. Plan this early: the analytic onset decides the certificate budget.

## 2. Direction X2: Morrow–Patterson lower bound

### 2.1 Objects (verify against the primary sources)

- **Sources.**
  - Morrow–Patterson, "Construction of algebraic cubature rules using polynomial ideal theory", *SIAM J. Numer. Anal.* 15 (1978) 953–976 (**verify**).
  - Caliari–De Marchi–Vianello 2005, the numerical paper that compared MP, extended MP (EMP) and Padua points and observed roughly quadratic growth of Λ_MP (**verify**).
  - Beberok–Białas-Cież–De Marchi 2026 (arXiv 2412.14595). The fulltext is open, so read it first and upgrade LIT-378 from UNVERIFIED with page and theorem numbers.
- **Points.** MP points of degree n (n even in the original construction; **verify**) are binom(n+2, 2) points on a Chebyshev-type grid with interlaced ordinates. They are unisolvent for Π_n.
- **Interpolant.** It has a compact kernel formula related to a degree-(2n+1) cubature.

### 2.2 Target outcomes

1. **Lower bound.** Λ_MP(n) ≥ c·n² for every admissible n ≥ n₀, with c and n₀ explicit. The likely route is an explicit point, probably at or near a corner or the boundary, where the fundamental functions add up coherently. Find it numerically first (MEASURED), then prove its asymptotic.
2. **Sharp constant.** Prove that lim Λ_MP(n)/n² exists and identify it. Locate the maximum, eventually or for every n.
3. **MPX variants.** Do the same for the Xu-type variants that BBDM leave open, if the fulltext defines them.

### 2.3 Expected difficulty

X2.1 may be much easier than X1. It needs only one carefully chosen point, not global localization. This is the main case where AC's downgrade rule applies (§4): a round that only executes a closed-form asymptotic can run on Opus 5.5 xhigh.

## 3. Novelty and literature obligations

- **Novelty gate** (AGENTS.md: relaxed scan at start, full IDEAS read at audit). At least these entries are relevant: IDEA-047 (survey MP, deferred), IDEA-048 (interior-maxima geometry), LIT-302 (coverage-qualified alternation/interpolation literature), LIT-378, LIT-388 (Białas-Cież–De Marchi–Suder 2026, interior maxima counts), LIT-486.
- **Forward-citation search before any priority claim.** Search for papers since 2006 that cite BCDMV 2006 or BdMV 2006 and might have settled Conjecture (17) or the MP lower bound. Search the De Marchi, Vianello, Białas-Cież, Erb and Xu groups especially. Record the documented search. The only admissible negative is "no matching result found in the documented search".
- **Reading rules.** Read each fulltext once, record LIT entries with page and theorem numbers, and cite by LIT-nnn from then on. Never commit PDFs or extracts; the repository is public. Give AC clickable DOI or journal links for anything unreachable.

## 4. Models and rounds (AC, 2026-11-14)

- **Researcher.** Fable 5.2 xhigh, for mathematical development in both directions.
- **Per-round downgrade.**
  - At the start of each round, the orchestrator may run that round's researcher on Opus 5.5 xhigh instead, when the round's problem does not look challenging: routine asymptotics, verification, bookkeeping or literature.
  - Record the choice and a one-line reason in `rounds.md` before the round starts.
  - A round that turns out harder than expected may be re-run on Fable.
- **Code and certificates.** Sonnet 5.5 high. Mechanical edits: Sonnet 5.5 medium. AC's standing preference: development subagents on Sonnet, reviews on Opus.
- **Independent subagent checks.** A separate Opus 5.5 instance, never the agent that produced the result.
- **Audit: Opus 5.5 xhigh** (AC's explicit instruction).
  - For this topic it replaces the default "Codex audits Claude development".
  - The auditor must be a distinct Claude thread that did not develop the work. The developer never approves its own work.
- **Workflow deviations.** Two settings depart from agents/WORKFLOW.md, both by AC's explicit instruction:
  - Fable used for mathematical development (the workflow table restricts Fable 5.1 to ideas campaigns);
  - a Claude auditor for Claude development.

  The LOG records both as AC rulings of 2026-11-14.
- **Model availability.** If Fable 5.2 is not available to the thread, report it and propose a substitute (Fable 5.1 xhigh, or Opus 5.5 xhigh) before mathematical work begins. Never substitute silently (WORKFLOW, "Do not request unavailable models silently").
- **Round budget.** Up to 10 rounds for X1 and up to 10 for X2.
  - A round ends with a pushed LOG entry.
  - Two consecutive rounds without recorded progress end a direction.
  - AC may raise the budget.
