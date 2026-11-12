# Report — padua-effective-cubature-20261112, session 1 (handoff 01) and the explicit-γ campaign

Claude (Opus 5.5 xhigh, orchestrator), 2026-11-12. Rules read at `39a4bf5`. Development awaiting the Codex audit (now handoff 03, which supersedes 02 to cover the campaign). Statuses follow AGENTS.md; every ID is provisional, `PD-T?padua-effective-cubature-20261112-claude-NN`.

## 1. Summary

- **C0.** The Padua Lebesgue-constant corollary is registered as an assembly of merged results (-01, PROVED).
- **Theorem A in uniform form (-03).** There is a single constant γ_A = (3/4)D(int 2O) − 1 > 0, where D is the Delsarte constant of the open double octahedron. Every positive closed-cube rule exact on Π_{2n−1} has, for **every** n ≥ 1,

  N ≥ (1+γ_A)·n³/6.

  The proof is elementary (records -02, -03) plus one literature theorem (Kolountzakis–Lev–Matolcsi 2025, Thm 6.4: a convex non-tile has Delsarte constant above its volume). It replaces the compactness steps of D1-04.
- **Cap (-04).** γ_A ≤ 1/18, so this route excludes Padua packages only for n ≥ 110.
- **Explicit value (-07; explicit-γ campaign, AC: up to seven rounds, 3 used).** γ_A > 1/36. The witness is the Cohn–Elkies function of Dostert–Guzmán–de Oliveira Filho–Vallentin for translative octahedron packings, re-certified locally by a computer-assisted proof (γ₁ = 0.0278415687…). Hence every positive closed-cube rule exact on Π_{2n−1} has

  N ≥ 37n³/216 for every n ≥ 1;

  no positive Padua package exists for any n ≥ 218; and N > binom(n+2,3) for n ≥ 109. Independent rerun: PENDING_INDEP.
- **Plain-LP route (BRIEF E1 as written).** It is equivalent asymptotically to Turán's problem for the octahedron, which KLM report as open. Numerically the plain torus LP equals Fisher, ρ_n = 1 within 3·10⁻⁶ for n = 2…12. Q2 kills it (MEASURED).
- **Finite range.** No finite exclusion was found. Exact lattice witnesses prove that the torus LP route, in any form, cannot exclude a package at any n = 2…109 (-06, PD-N). This is exactly the range left open by the uniform bound. The plain cube LP gives λ ≈ 1.2 < 1+3/n at n = 3, 4 (MEASURED).

## 2. C0 corollary as registered (-01, PROVED, assembly)

Λ(Pad_n) = Λ_c(n), attained at the two non-node corners, for 2 ≤ n ≤ 32 and for every n ≥ N_*. Here N_* is existential (PD-T229). Hence, for n ≥ max(32, N_*),

  Λ(Pad_n) = (4/π²)log²N + b log N + c + R_n,  N = n+½,

with PD-T271's explicit |R_n| bound and c = 1.84616031042392607975983873794… (parity independent).
- Dependencies: PD-T209, T162/166/169/174/177, T181, T214, T246, T229, T269–T271.
- If PR #27 merges, it supersedes both halves.
- No priority claim.
- [Record](theory/lebesgue-constant-corollary.md); checks in [novelty-gate-C0.md](novelty-gate-C0.md) and [independent-checks-C0.md](independent-checks-C0.md).

## 3. Gates

| Gate | Verdict |
|---|---|
| Q0 replay | **PASS**: fd1 controls identical; D3 certificate PASS; D3 cube-LP cap λ₃ ≤ 1.63579 |
| Q1 LP sanity | **PASS**: Fisher reproduced exactly (torus and cube); no LP value above a lattice or D3 reference; 15 lattice witnesses re-verified independently |
| Q2 asymptotic screen | **Plain LP: KILL** (ρ_n − 1 ≤ 3e-6, n = 2…12). **Delsarte LP: INCONCLUSIVE** (ρ^Del ≈ 1.08 at n = 5…8, K = 3n−2; neither monotone nor 1/n-decaying) |
| Q3 certificates | **Not exercised**: no certificate produced; no finite exclusion claimed |

Details: [gates.md](gates.md).

## 4. The Turán-constant finding

- **The literature (KLM 2025, full text).**
  - Whether any symmetric convex body has Turán constant T(U) > 2^{−d}m(U) is a major open problem. T is unknown even for the regular octagon.
  - For the Delsarte constant (positive definite, φ ≤ 0 outside U, no support constraint), D(Δ(A)) > m(A) holds for every convex body A that does not tile.
- **Consequences.**
  - BRIEF E1 as written (spectrum inside the exact range ↔ T(2O)) would need the first known non-Turán convex body. It is deferred.
  - The cubature LP, however, admits the Delsarte relaxation: high frequencies need only nonpositive coefficients, since |ν̂(k)|² ≥ 0 (-02).
  - A transference argument gives M ≥ L³ D(int 2O) with L = (E+1)/2 for exactness E. Strictness then comes from KLM, because O does not tile (Greenfeld–Lev and Lev–Matolcsi, already used in D1-04).
- **Measurement.** The plain torus LP sits at Fisher, which is consistent with T(int 2O) = |O| (MEASURED only). The Delsarte LP sits above it at finite n.

## 5. Explicit γ and n₀

**γ_A ≥ γ₁ = 0.02784156869… > 1/36** (record -07).
- **Round 1.** An explicit γ_A is the same as an explicit Cohn–Elkies bound below 1 for translative packings of O/2: the Cohn–Elkies admissibility conditions are exactly Delsarte admissibility for int(K−K). DGOV (arXiv:1510.02331, Table 6) prove the bound 0.972912750 for the octahedron.
- **Round 2.** Their function f = P·e^{−π|x|²} (P of degree 26, taken from their ancillary file as data) is re-certified locally by `code/gamma_certificate.py`: f̂ ≥ 0, f ≤ 0 on |x|₁ ≥ 1.001, and the value in ball arithmetic. Verdict PASS in 121 s; independent rerun PENDING_INDEP.
- **Round 3.** An attempt to improve the value with a sampled LP was numerically unreliable; no claim (`attempts/E1-gamma.md`).

**Explicit consequences** (rules exact on Π_{2n−1}, positive, nodes in the closed cube):
- N ≥ 37n³/216 for all n;
- N ≥ (1+γ)binom(n+2,3) for n ≥ n₀(γ), explicit for each γ < 1/36 (e.g. n₀(1/72) = 220);
- no package for n ≥ 218.

The package range 110 ≤ n ≤ 217 is decided neither way. γ_A could be anywhere in (1/36, 1/18].

Consistency check:
- The extreme value γ_A = 1/18 reproduces the merged lattice-class bound |X| ≥ 19n³/108 of the 3-D note (§4, threshold n ≥ 110).
- That bound is the special case in which the rule is a lattice cosine image.
- So the general bound can never be better than the lattice-class bound, and could match it only if γ_A attained the packing cap.

## 6. Certified finite bounds and the degree list

- No finite-n exclusion certificate (Q3) was produced. The explicit uniform bound N ≥ 37n³/216 (-07) exceeds Fisher for n ≥ 109. The degree list of positive packages:
  - packages exist for n = 1, 2 (lattice) and n = 3 (D3);
  - existence is OPEN for every 4 ≤ n ≤ 217;
  - **no package exists for n ≥ 218** (-07, explicit).
- **Proved limitations.**
  - The uniform bound decides no n ≤ 109 (-03 (iv)).
  - The finite torus LPs (plain or Delsarte, any spectrum), combined with M ≤ 8N, decide no n = 2…109 (-06; 108 exact lattice witnesses, two code paths). No witness of this kind can exist for n ≥ 110, by the packing bound.
- **Measured limitation.** The plain cube-native LP has λ₃ ≈ 1.210 and λ₄ ≲ 1.201, against the required 2 and 1.75 ([attempts/E3.md](attempts/E3.md)).

## 7. What remains OPEN

1. The value of γ_A within (1/36, 1/18]. Improving 1/36 needs a better certified function; the resume conditions are in `attempts/E1-gamma.md`.
2. Finite exclusions for 4 ≤ n ≤ 217. In 110 ≤ n ≤ 217 this would follow from a larger certified γ. The torus route is proved useless there (-06). Candidate routes:
   - the Delsarte extension of the cube LP (IDEA?…-claude-06, not run);
   - separation-based Cohn–Elkies strengthening (-04 candidate, deferred);
   - a sharper orbit conversion than M ≤ 8N.
3. Whether T(int 2O) > |O| (literature-open; not pursued).
4. E2, quantitative compactness: not attempted, deferred.

## 8. Effect on the 3-D note (`topics/padua-3d-20261106/paper-note-draft.md`)

- §2 currently says that Theorem A "supplies no effective γ or n₀" and rests on compactness plus Greenfeld–Lev.
- After audit, the note can add a second proof of Theorem A. It is stronger in form: N ≥ (1+γ_A)n³/6 at every n, with one named constant γ_A ∈ (0, 1/18], whose positivity comes from KLM Thm 6.4. This removes the compactness lemmas from the existence statement, but does not make γ explicit.
- §4's lattice-class threshold n ≥ 110 becomes the extremal case of the general bound: arbitrary rules would reach the same threshold if and only if γ_A = 1/18.
- The note's "no effective γ or n₀" is superseded, after audit, by record -07. Theorem A holds with γ = 1/36 in the uniform form N ≥ 37n³/216 for every n, and packages are excluded for every n ≥ 218. The explicit constant uses DGOV's octahedron packing function, re-certified locally.
- The abstract sentence "non-effective fixed relative excess … once n is sufficiently large" can become "an explicit fixed relative excess N ≥ (37/36)n³/6 valid for every n, excluding the full package for n ≥ 218".
- No edit to the merged note is made on this branch.

## 9. Records and evidence

| ID | Record | Status |
|---|---|---|
| -01 | [lebesgue-constant-corollary.md](theory/lebesgue-constant-corollary.md) | PROVED (assembly) |
| -02 | [delsarte-bound.md](theory/delsarte-bound.md) | PROVED |
| -03 | [uniform-theorem-a.md](theory/uniform-theorem-a.md) | PROVED with LITERATURE dependency |
| -04 | [lp-cap.md](theory/lp-cap.md) | PROVED |
| -05 | [explicit-gamma-target.md](theory/explicit-gamma-target.md) | CLOSED by -07 |
| -06 | [limitation-torus-lp-finite.md](theory/limitation-torus-lp-finite.md) | PD-N, PROVED (exact witnesses) |
| -07 | [explicit-gamma.md](theory/explicit-gamma.md) | PROVED, computer-assisted (local certificate); independent rerun PENDING_INDEP |

Supporting files:
- Evidence: [evidence-manifest.json](evidence-manifest.json).
- Literature: [literature-effective.md](literature-effective.md).
- Candidates: [novelty-gate-E1.md](novelty-gate-E1.md).
- Attempts: [attempts/](attempts/).
- Rounds: [rounds.md](rounds.md).
- Independent checks: [independent-checks-E1.md](independent-checks-E1.md).

Independent Opus checks: [C0](independent-checks-C0.md), [E1](independent-checks-E1.md), and [E1b](independent-checks-E1b.md) for -02 (d), -03 (ii′) and -06. None has a BLOCKING finding, and every finding is dispositioned. The Codex audit is pending (handoff 02).
