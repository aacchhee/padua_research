# 3-D Padua frontier reassessment and inspiration round — 2026-11-08

- Author: **Claude, Opus 5.5 (`claude-opus-5-5`), xhigh**, ideas-campaign orchestrator. This is the Opus 5.5 xhigh row of the WORKFLOW allocation table, requested by AC as "opus extra".
- Scouts: six independent Opus 5.5 xhigh subagents covering literature and neighbouring fields, plus one strategy scout. Their full reports, with sources and their own coverage limits, are in [frontier-2026-11-08/](frontier-2026-11-08/):
  - [S1](frontier-2026-11-08/S1.md): multivariate interpolation literature;
  - [S2](frontier-2026-11-08/S2.md): Weyl groups and generalized Chebyshev polynomials;
  - [S3](frontier-2026-11-08/S3.md): sampling, lattice rules, subsampling;
  - [S4](frontier-2026-11-08/S4.md): algebra, combinatorics, sphere, physics;
  - [S5](frontier-2026-11-08/S5.md): strategy and hardness;
  - [S6](frontier-2026-11-08/S6.md): deep structure of 2-D Padua.
- Shared input: [brief](frontier-2026-11-08/brief.md).
- Repository read at `dafb8c8` and after `bbf4b42`. No claim, status or registry entry is changed here, and no novelty is claimed.

## AC's questions (verbatim, 2026-11-08)

> "When finished, use opus extra to reassess the 3d frontier: should this direction be frozen or is it worth pursuing some extra rounds? seems that the case is genuinely hard, but you may try to do inspiration round with literature and maybe neigboring fields before deciding."

> "looks like there is a huge gap between log 3d asymptotics and what is actually available of point sets. in 2D Padua group was lucky with lissajous. But I suspect that one has to look for deeper algebraic structures in 2D, not just sin/cos intersections, that may transfer to 3D. I feel that Lissajous/Chebyshev is just a well-known representation of deeper structures"

> "so you mean the determinantal route is worth studying deeper?"

## Gate and coverage

**Registry reading.**
- The audit-04 novelty subagent read the complete current `state/IDEAS.md` at `e7c9900` the same day, including every obstruction and disposition table.
- For each candidate below, targeted searches of IDEAS, INDEX and the topic found **no** entry for the following:

  | Search terms | Hits |
  |---|---|
  | spectral sets, Fuglede, Lev–Matolcsi | none |
  | Riesz bases | none in IDEAS; one INDEX row |
  | determinantal, symmetroid, Eagon–Northcott, Józefiak, Pfaffian | none |
  | Lee spheres, Golomb–Welch | none |
  | Gunzburger–Teckentrup | none in registries |

- Joint spectra and commuting extensions are covered by IDEA-120 and related rows, which are untested.

**Literature reading.**
- Mostly arXiv full texts or abstracts, read by the scouts.
- Many publisher hosts were blocked, so Sloan–Womersley, Wang–Wang–Wang's full text, Cools–Lyness and others remain unread.
- Each scout report states exactly what it read. Nothing below is a locally verified proof.

**Disclosed deviation.** Scouts S1, S2 and S3 ran small sanity scripts themselves (copies in [frontier-2026-11-08/code/](frontier-2026-11-08/code/)). WORKFLOW reserves such scripts in ideas campaigns for Sonnet 5.5 high. Their outputs are leads only, not repository evidence.

## What the literature says (LITERATURE / scout-read; coverage in the scout reports)

**Openness is stated explicitly** by:
- Li–Sun–Xu 2009 (arXiv 0808.0180). Their conjecture: degree-(2n−1) cube cubature needs n³/4 + O(n²) nodes. Reaching n³/6 is "an open question".
- Bos–De Marchi–Vianello 2017 (no 3-D self-intersections).
- Gunzburger–Teckentrup (arXiv 1407.3291). They conjecture log^d, with growth "not known analytically".
- Białas-Cież–Kenne–Sommariva–Vianello 2023 ("no explicit good family known" in the cube).
- Bloom–Bos–Calvi–Levenberg (LIT-383).
- Xu 2024 ("we do not know any family … for d > 2").

**Known near-results the topic has not yet recorded properly**
- **Li–Sun–Xu, Cor. 4.12.** Interpolation with Λ ≤ c·log³ n on about n³/4 ≈ 1.5N nodes, in the space Π*_n ⊋ Π_n (frequency body: the rhombic dodecahedron). The current INDEX entry LIT-010 is secondary-only. This is prior art for the topic's parity least-squares log³ statements.
- **Li–Xu 2010 (arXiv 0809.1079).** A complete Padua analogue in **every** dimension: exactly binom(n+d,d) nodes, degree-(2n−1) cubature, unique total-degree interpolation, Λ ≤ c(log n)^d. It lives on the A_d orbit-space domain, not the cube.
- **Wang–Wang–Wang 2014.** O(log³ n) hyperinterpolation, said by Bos–De Marchi–Vianello to settle De Marchi–Vianello–Xu's conjecture. Full text unread; this may already make T10's conditional log³ known.
- **Gunzburger–Teckentrup.** Optimized cube Λ for n = 1..5: 2.00, 2.95, 4.05, 5.09, 6.40. This is the external benchmark; the topic's U2 value is 5.54 at n = 4.
- **Krieg–Pozharska–Ullrich–Ullrich (arXiv 2401.02220).**
  - 2N points give a least-squares norm of O(√N) for any N-dimensional space; exactly N points give a linear norm in general.
  - The best norm with N + N^α points is open.
- **Dolbeault–Chkifa (SINUM 2024).** A randomized N-point selection with Λ ≤ 1 + 2N√N, better than the topic's explicit O(N³) R-Leja bound. Classical Fekete points give Λ ≤ N.
- **Białas-Cież et al.** Rigorous two-sided Λ bounds on Chebyshev meshes, about 7.7% in the cube. These would turn the topic's lower samples into certified intervals.
- **Coding theory.**
  - Horak–AlBdaiwi plus Gravier–Mollard–Payan: no Lee-sphere tiling of Z³ for radius ≥ 2. So exact-cardinality *trigonometric* lattice reconstruction of the octahedral set is impossible for n ≥ 2.
  - Golomb–Welch (1968) is the prior art for the T9 packing argument.
- **Exponential bases and tiling.**
  - Lev–Matolcsi (Acta Math 2022): a convex body is spectral iff it tiles.
  - Greenfeld–Lev 2017: spectral polytopes have centrally symmetric facets.
  - Gravin–Robins–Shiryaev: the octahedron does not even multi-tile.
- **Bel-Afia–Meroni–Telen 2024.** Interior Padua points are exactly the nodes of the Chebyshev curve. Cosine-parametrized Chebyshev surfaces have no finite set of interior nodes.
- **Neighbouring domains are equally open.**
  - Sphere S²: extremal-point interpolation has Λ ≈ N^0.56 (Marzo; An–Zhuang survey).
  - Tetrahedron: best explicit nodes reach Λ = 118 at n = 15 (Isaac 2020).

## Answer to AC's deep-structure question

AC's intuition is right, and the scouts can name the structure. **The deeper object behind 2-D Padua is discrete Fourier analysis on the orbit space of a lattice or root system whose frequency body tiles space.** Lissajous curves, cosine cosets and two-term ideals are presentations of it. Li–Xu show this structure exists in every dimension.

What breaks in 3-D is specific: **total degree on the cube corresponds to the octahedral frequency body, and the octahedron neither tiles, nor multi-tiles, nor is spectral.**
- **In 2-D** the diamond |k₁|+|k₂| ≤ n is a rotated square that tiles; this is the B₂ = C₂ / D₂ = A₁×A₁ coincidence. That is the actual source of the Padua "luck".
- **In 3-D** the related tiling bodies have about 3/2 the octahedron's volume: the rhombic dodecahedron of A₃ = D₃, and the C₃ grading. This explains the 1.5N that keeps reappearing in Li–Sun–Xu, De Marchi–Vianello–Xu and the topic's own parity grid.
- **Transport fails.** Only affine maps preserve total degree, so Li–Xu's A₃ construction cannot be carried to the cube.

The other characterizations either reduce in 3-D to cosets the topic has already killed, or fail by counting or by Gorenstein constraints: two-term ideals, Gorenstein/Pfaffian structure, Chebyshev-surface nodes, the reproducing-kernel formula, the finite-field dictionary ([S6](frontier-2026-11-08/S6.md)).

**One genuinely new algebraic family survives: determinantal / symmetroid node sets** (candidate C2 below).

## Why the 3-D case looks genuinely hard (diagnosis, not theorem)

1. **Structural.** Every known minimal-node polylog construction in any dimension rests on a tiling or spectral frequency body. The octahedron has none.
   - Two scouts (S2, S4) independently sketched a spectral-limit argument (C1). It suggests that *no* positive cubature exact through degree 2n−1 can live on (1+o(1))·dim Π_n nodes in the cube, for any nodes and any positive weights.
   - This would remove the whole cubature-based Padua mechanism asymptotically, not just lattice versions.
2. **Interpolation itself.** A uniformly well-conditioned exact-N family would resemble a Riesz basis of exponentials for the octahedron, which is an open problem in harmonic analysis. S3 measures that 2-D Padua is numerically such a "Riesz family": normalized Gram spectrum in [0.999, 1.998] at n = 48, while 3-D sets lose this property.
3. **Numerics** cannot decide log³ against n^α for practical n (S5). The best measured minimal-node values grow like about √N, which matches the sphere state of the art.
4. **Diminishing returns.** About 50 counted rounds in three days. The last 26 (U1–U3 and pruning) gave finite certificates and measured gains only. Every constructive class lost on quality.

## Candidate records (provisional, Claude ideas campaign; no novelty claimed)

Every candidate below is also limited by audit 04's missing source comparisons, gate G6.

### C1 — spectral obstruction to near-Gaussian positive cubature on the cube

| | |
|---|---|
| ID | IDEA?padua-3d-20261106-claude-01 |
| Sources | S2 I1, S4 I1, found independently |
| Status | Not a recorded result: a sketch to be proved or refuted |

- **Mechanism.** For a positive rule exact on Π_{2n−1}, the exact identity Σ_i δ_i = N − dim Π_{n−1} holds, with δ_i = 1 − w_i·K_{n−1}(x_i, x_i) ≥ 0.
  - Padua-type sets would make almost every δ_i small.
  - A local blow-up at an interior point would then yield a spectrum of exponentials for the octahedron at critical density. That contradicts Lev–Matolcsi / Greenfeld–Lev.
- **Claim to be proved.** There is c > 0 such that every positive degree-(2n−1) cube rule needs at least (1+c)·n³/6 nodes for n ≥ n₀.
  - That gives no Padua-type sets for large n, whatever the nodes, phases, unions or weights.
  - It is a partial answer toward the Li–Sun–Xu n³/4 conjecture.
- **Closest entries.**
  - In the topic: T9-03 / PD-N T9 (n ≥ 110, unshifted lattices only), the r08 lattice minima, and IDEA-120.
  - In the literature: the Li–Sun–Xu conjecture and Möller-type bounds.
  - No spectral-set entry exists anywhere in the repository.
- **Separation from those entries.** C1 needs no lattice and no unshifted support, so it covers arbitrary node sets. It is falsified if a positive degree-(2n−1) family with (1+o(1))·n³/6 nodes exists, or if the limit step fails.
- **Kill tests.**
  - The argument must allow 2-D Padua (the diamond tiles).
  - It must check against S²-design and disk literature.
  - The exact identity must hold on the topic's lattice rules.
  - It needs a written, audited proof.
- **Value.** It does not decide finite n, and it is not an interpolation lower bound.
- **Assessment.** Promise 4/5, difficulty 3–4/5. **Recommended.**

### C2 — determinantal / symmetroid node sets

| | |
|---|---|
| ID | IDEA?padua-3d-20261106-claude-02 |
| Source | S6 R1 |
| Status | New constructive algebraic family, quality untested |

- **Mechanism.** Two loci:
  - the rank ≤ n locus of an (n+3)×(n+1) matrix of affine-linear forms in (x,y,z) (Eagon–Northcott);
  - the corank-2 locus of a symmetric pencil A₀ + xA₁ + yA₂ + zA₃ of size (n+2) (Józefiak).
- **Why it is promising.** Both give exactly N points with the Hilbert function of Π_n. If the locus is finite, reduced and real in the cube, unisolvence follows algebraically. At n = 1 it gives the Cayley-cubic 4-node set.
- **Link to IDEA-120.** With Aᵢ built from truncated Chebyshev multiplication (Jacobi) matrices, this becomes a concrete form of the never-run joint-spectrum / commuting-extension idea.
- **Closest entries.** None for determinantal loci. IDEA-120 for joint spectra. The 2-D Padua Hilbert–Burch structure has never been derived.
- **Separation from those entries.** Not a coset, lattice, curve or optimization over free coordinates. It is a low-parameter algebraic family. The family is killed if no real-in-cube configuration exists, or if quality is no better than generic optimization.
- **Calibration caveat.** In 2-D every point set is determinantal (Hilbert–Burch), so the property is not special there. The question is whether Padua's Hilbert–Burch matrix has a special shape, banded or Chebyshev-structured, whose 3-D analogue gives good points. That 2-D calibration is the first test.
- **Kill rule.**
  - Kill if the 2-D calibration shows no exploitable structure **and** the 3-D optimized Λ exceeds twice the Gunzburger–Teckentrup optimum at both n = 3 (4.05) and n = 4 (5.09).
  - Kill if no real-in-cube configuration is found at n = 3 or 4.
- **Assessment.** Promise 3/5 for a structured family, 1/5 for log³; difficulty 2/5 for the tests. **Recommended as a bounded test.**

### C3 — Riesz / normalized-Gram diagnostics and whole-cube certificates

| | |
|---|---|
| ID | IDEA?padua-3d-20261106-claude-03 |
| Sources | S3 idea 1, S4 I2/I3; Białas-Cież et al. |

- **Mechanism.**
  - Compute λ_min of the normalized-kernel Gram matrix and the certificate Λ ≤ √(K∞/λ*) for the topic's best sets.
  - Apply mesh-to-continuum certificates, turning MEASURED lower samples into certified two-sided intervals.
- **Value.** Mostly for the paper: certified values, and a diagnostic that separates "2-D Padua-like" from "3-D".
- **Kill.** If λ_min decays polynomially under two optimizers, record the "Riesz gap" as MEASURED and stop.
- **Assessment.** Promise 2/5 for the target, 4/5 for record quality; difficulty 1–2/5. **Recommended (cheap).**

### C4 — Lee-code lattice dictionary

| | |
|---|---|
| ID | IDEA?padua-3d-20261106-claude-04 |
| Source | S3 idea 2 |

- **Mechanism.** The double-Lee-sphere bound det L ≥ (2/3)·n·(2n²+1).
  - It equals the exact minima 2, 12 and 38 at n = 1..3.
  - Restarting the enumerator at this bound would make the n4..7 determinant minima independent of the imported 18/19 theorem, with few extra determinants to check.
- **Also.** Record the Golomb–Welch and Lee-tiling prior art.
- **Assessment.** Promise 2/5 (rigour; reduces the E4 dependency), difficulty 1/5. **Recommended (cheap).**

### C5 — reflection-invariant lattice bound n³/4

| | |
|---|---|
| ID | IDEA?padua-3d-20261106-claude-05 |
| Source | S6 R3 |

- **Mechanism.** Classify the orthorhombic P/C/I/F lattices. Their octahedral packing densities 1/6, 1/3, 1/3 and 2/3 give about n³/4 folded nodes for fully reflection-invariant unshifted rules. That would be the Li–Sun–Xu conjecture within this class.
- **Assessment.** Promise 2/5, difficulty 2/5. Deferred as optional; it is subsumed if C1 succeeds.

### C6 — sign-fixed-class failure for sign-invariant subgroups

| | |
|---|---|
| ID | IDEA?padua-3d-20261106-claude-06 |
| Source | S1 idea 1 |

- **Mechanism.** Extend T1 to arbitrary phases and unions of cosets of sign-invariant subgroups.
- **Assessment.** It narrows the coset class but escapes nothing. Promise 2/5. Deferred.

### C7 — certified non-lattice Padua-type sets at n = 3

| | |
|---|---|
| ID | IDEA?padua-3d-20261106-claude-07 |
| Sources | S1 idea 2, S5 Bet B |

- **Mechanism.** The scout search found 20-node positive degree-5 rules, unisolvent for degree 3, in 7 of 12 starts. Their sampled Λ is 38–609, against the optimum of about 4.05.
- **Next step.** Certify one with interval Newton plus an exact rank check.
- **Value.** It settles "Padua-type exists at some n ≥ 3", and shows that exact cubature does not buy quality in 3-D.
- **Assessment.** Promise 2/5, difficulty 1–2/5. **Recommended (cheap, 1 round).**

### C8 — framing corrections, no new mechanism

| | |
|---|---|
| ID | IDEA?padua-3d-20261106-claude-08 |
| Status | Record work |

- **Content.**
  - Record Li–Sun–Xu Cor. 4.12 and Li–Xu 2010 as primary sources.
  - Cite Wang–Wang–Wang for T10.
  - Use Gunzburger–Teckentrup as the U2 benchmark.
  - Place R-Leja O(N³) against Fekete (N) and Dolbeault–Chkifa (N^{3/2}).
  - Record Golomb–Welch, Horak–AlBdaiwi and Gravier–Mollard–Payan for the lattice packing work.
  - Add the KPUU and Białas-Cież results.
- **Assessment.** **Required** before any paper note. It also feeds the audit-04 gate finding G6.

**Rejected or deferred from the scouts**, with reasons in their reports:
- Transporting Weyl-orbit or A_d constructions to the cube: impossible, since only affine maps preserve total degree.
- Chebyshev-sum or Chmutov surface nodes: counting fails (ratio → 9/4); no interior nodes.
- Gorenstein/Pfaffian ideal structure: h-vector mismatch.
- Weighted Fekete: weights cancel in square interpolation.
- Moussa–Chkifa cyclic plans B/C: duplicates of the repository's M = 2N−1 / 2N−2 classes.
- BSS/MSS thinning of the 1.5N grid to polylog: needs about N² samples.
- Dominant D-optimal designs: √N-type only, likely classical.

## Recommendation

**NARROW, then FREEZE.**

**Stop now** (no more rounds): all open-ended construction, optimization and pruning work — the T7–T10 coset, cyclic and lattice construction searches, U1–U3, and the P campaign. The existing finite results and their audits stand.

**Fund one final, bounded "deep-structure" round set**, with these ceilings. They are ceilings, not quotas; the developer is Codex and the auditor is Claude.

| Item | Ceiling (rounds) | Kill or stop rule |
|---|---|---|
| C1 spectral obstruction: written proof attempt plus kill tests | 6 | Stop if the limit step cannot be closed after 4 rounds; record the sketch as CONDITIONAL/OPEN |
| C2 determinantal/symmetroid: 2-D Hilbert–Burch calibration; exact Gröbner/radical/unisolvence checks at n = 2..4; real-in-cube search; Λ optimization over matrix parameters | 3 | As in C2 |
| C7 certified Padua-type set at n = 3 | 1 | Interval Newton fails in 1 round |
| C3 Gram diagnostic and certified Λ intervals; C4 Lee bound and enumerator restart | 2 | Finish or record infeasibility |
| C8 literature and framing corrections, then a paper-note draft (fulltext novelty gate first) | 3 | Not research rounds; record work |

Expected yield:
- One structural theorem (C1). If it holds, it is the most valuable outcome left: a partial answer toward a published conjecture, and a principled explanation of why 3-D lacks a Padua mechanism.
- One decisive test of a genuinely new algebraic family (C2).
- Certified versions of existing finite claims.
- A publishable, honestly framed note.

S5 estimates the probability of a polylog minimal-node family from any further rounds at about 1–3%; Claude concurs. **After this set, freeze the 3-D direction** with PR preparation, unless C1 fails in an informative way or C2 shows real structure. Either would be a new, stated resume condition for AC.

**Resume conditions after freezing:**
- an explicit non-lattice, non-curve algebraic family whose 2-D specialization reproduces Padua;
- or a spectral or Riesz-basis result for the octahedron;
- or AC's decision.

**AC decisions requested:**
1. Approve, modify or reject the narrowed round set above.
2. The E4 label convention, still pending.
3. Storage, now within the 100% allowance; discuss at PR.
4. The earlier canonical deviations.
