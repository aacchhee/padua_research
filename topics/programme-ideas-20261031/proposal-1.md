# Proposal 1 — Lebesgue theory of Padua interpolation: corner expansion, certified maxima, coordinated counting (PROJECT, not programme)

Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator) · 2026-11-01

Candidate gen4-draft-2 (IDEA?programme-ideas-claude-17), after `gate.md` §5 item 9, `checks/adversarial-gen4-2.md` (WOUNDED) and `checks/decisive-gen4-2.md` (RESIDUE CONFIRMED). Nothing is rerun here.

## Central question

What is the second-order asymptotic expansion of the Lebesgue constant of the Padua points, where on the square is the Lebesgue function maximal, and how many local maxima does it have — each answer a proof or a certified computation, not a mesh observation.

## Template theory

Univariate Lebesgue-constant theory on [−1,1]: the Chebyshev expansion (2/π) log n + (2/π)(γ + log(8/π)) + O(1/n²) (Günttner; Shivakumar–Wong 1982; Smith 2006), the Ehlich–Zeller endpoint maximum, Brutman's local maxima. Missing on the square: an exact second term for Padua (Kolomoitsev–Lomako 2021 Thm 2.1 leaves O(log n)), a proof that the maximum sits at a non-node corner (an observation since De Marchi 2022), a certified count of local maxima (Białas-Cież–De Marchi–Suder 2026 publish uncertified tables). A universal lower bound is excluded: the projection-constant route is capped at (16/π⁴) log² n (`adversarial-gen4-2.md` (iii)).

## Sub-problems and payoffs

**Paper A — corner expansion and corner-argmax theorem.** The corner value is an exact O(N) sum of closed-form kernel terms (MEASURED to 2.1e-13, n = 3…64) with a pure Euler–Maclaurin expansion in N = n + ½: Λ_c = (4/π²) log² N + b log N + c − 1/N + (0.912 − 0.195 log N)/N² + …, b = (8/π²)(γ + log(8/π)) to 12 digits, c = 1.846160310424 ± 2e-12 for even and odd n alike, κ = c − c₁² = 0.9197101183886 ± 2e-12 (`decisive-gen4-2.md` T2). To prove: (i) the factorisation giving b; (ii) the nature of κ, which matches no small-height combination of 1-D constants at 12 digits; (iii) the −1/(n+½) term; (iv) the corner argmax — the runner-up is an edge maximum near the midpoint of x = ±1 with gap → ≈ 0.548 (T1), so the proof needs constant-order expansions at two points plus an a-priori bound elsewhere. Payoff: a short classical-analysis paper.

**Paper B — certified crease-aware counting tool and corrected table.** A quadtree in Chebyshev angles with Bernstein/Lipschitz certificates and exact lemmas at degenerate points certifies every local maximum of λ_n for n ≤ 8 in ≤ 130 s, resolving the crease pairs (1.7e-3–2.2e-2 apart) that fixed meshes miss: 15, 27, 25, 41, 50, 62 maxima for n = 3…8 against the published 15, 27, 25, 39, 42, 56 (`decisive-gen4-2.md` T3; IEEE double, margins ≥ 1.5e-6). Payoff: a tool paper in the ETNA-2024 line with an immediate correction; node-set agnostic code.

**Paper C — counting theorem, with Kraków–Padova, only if BSV 2012 leaves room.** The certified counts are non-monotone in n and exceed the conjectured bounds by a growing margin, so the theorem to prove is a crease-pair count, not "one maximum per Lissajous cell" (`adversarial-gen4-2.md` (iii)); it is BDS 2026 §4's question and should be done with them. The former sub-problem 4 (Padua–Jacobi / checkerboard Fekete) is not a paper: BSV 2012 own the family and the degree-dependent Λ-optimal parameters (Table 5), De Marchi–Usevich 2014 Prop. 1 is the separability, and determinant-optimal sets lose to BSV's (Λ 6.60 vs 5.92 at n = 10); what BSV leave is a univariate two-species extremal remark, for Paper C at most.

## First three tests

Already run (pre-registered in `checks/decisive-gen4-2.md`; scripts in `checks/code/decisive/gen4-2/`):
1. T1 corner argmax — n = 2…64 and twelve degrees to n = 200 on Chebyshev-angle meshes plus edge grids, maxima Newton-polished: no non-corner value exceeds Λ_c(n) at any of 75 degrees; G(n) ≈ 0.5483 + 0.839/n for n ≥ 32; kill did not fire (pre-registered "harder case").
2. T2 one-page test — exact kernel-sum identity; long-double values to n = 8192 cross-checked with mpmath; b, c, κ to 12 digits with the N = n + ½ structure; κ not identified against 1-D constants (three tiers, PSLQ); kill did not fire.
3. T3 certified counting — complete certification n = 3…8, zero undecided boxes, n = 8 in 129 s; validated by ring tests and valley depths ≥ 2.3e-8; kill did not fire.

Next three:
4. Edge-midpoint expansion — the runner-up value as the same kernel sum, fitted to 12 digits (one day); the two constants must differ by 0.5483 ± 1e-3 or the argmax route changes.
5. Interval-arithmetic rerun of T3 at n ≤ 8, extension to n = 10–12 (≈ 20 min each), also for Morrow–Patterson and Xu points.
6. Read Kolomoitsev–Lomako 2021 in full and try their discretisation lemma on the corner sum; if it yields b, Paper A shrinks to κ and the argmax (one week).

## Closest prior work

Bos–Caliari–De Marchi–Vianello–Xu, JAT 143 (2006): Lagrange formula, Λ = O(log² n), no maximum location. Kolomoitsev–Lomako, AMC 403 (2021) 126192 (arXiv 2009.07114): leading term, O(log n) remainder, rhombus constant 16/π⁴, maximiser not identified. Briani–Sommariva–Vianello, JCAM 236 (2012) 2477–2486: Padua–Jacobi sets, Λ-optimised degree-dependent parameters (Table 5). Białas-Cież–De Marchi–Suder, arXiv 2605.23299 (May 2026): maxima tables n ≤ 8 without method, Remark 2, §4 open questions. De Marchi, Constr. Math. Anal. 5 (2022): corner observation, heuristic fit ((2/π) log(n+1) + 1.1)². Günttner / Brutman / Shivakumar–Wong 1-D expansions via Smith, Ann. Math. Inform. 33 (2006). Also Dencker–Erb–Kolomoitsev–Lomako, J. Complexity 43 (2017); Białas-Cież–Kenne–Sommariva–Vianello, ETNA 60 (2024); De Marchi–Usevich, LAA 449 (2014); de Camargo–De Marchi, DRNA 8 (2015).

## Ownership check

From `adversarial-gen4-2.md` Attack (i), checked 2026-11-01: Kolomoitsev and Lomako (arXiv 2009.07114; AMC 403 (2021)) own the leading-term method, left the remainder open, no 2022–2026 follow-up found (citation search blocked). Białas-Cież, De Marchi, Suder (Kraków–Padova; arXiv 2605.23299, May 2026) posed the counting question, give no method, announce no continuation; Beberok–Białas-Cież–De Marchi (arXiv 2412.14595; Constr. Approx. 63 (2026)) cover Morrow–Patterson only. Białas-Cież–Kenne–Sommariva–Vianello (arXiv 2311.18656; ETNA 60 (2024)) own certified brackets and LEBEVAL. Briani–Sommariva–Vianello (JCAM 236 (2012)) own the Padua–Jacobi family. De Marchi (CMA 5 (2022)) lists the corner statement as an observation. No group states a programme on the corner expansion or the argmax; criterion 4 holds for Papers A and B. Paper C is theirs by question.

## Why a project and not a programme

Criterion 5 fails, flagged by gate, adversary and decisive test alike: classical approximation theory plus certified numerics; none of AC's structured-matrix tools (HSS, bulge chasing, IEPs, exact BTTB) is needed. Criterion 1's escalating horizon is gone: sub-problem 2 is closed by the (16/π⁴) log² n ceiling with no replacement mechanism, sub-problem 4 is BSV 2012 plus DU 2014, so the "Erdős–Bernstein theory for the square" meant to carry years 3–5 has no anchor. What remains meets criteria 2–4 at project scale — two or three separable papers, decisive tests already run, no owner of the exact questions — and no more.

## Risk

Speed: Padova and Kraków publish here yearly, own LEBEVAL, and can produce a certified table quickly once the method is public; Kolomoitsev–Lomako's machinery may reach the second term with little extra work. Mathematics: κ may have no closed form, leaving Paper A with b proved and κ to 12 digits; the argmax proof may stall on the a-priori bound. Numerics: certificates run in IEEE double with reported margins, not interval arithmetic; the degenerate-edge lemma uses an unverified identity at n = 3. Fit: the project spends AC's time outside the structured-matrix line; it is justified only as a bounded 12–24-month side project whose first paper (B) is nearly finished.
