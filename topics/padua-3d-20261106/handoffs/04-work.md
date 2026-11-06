# Handoff 04 — padua-3d-20261106 — new directions T7/T8/T9, plus the audit-01 response

- Status: open
- Previous handoff: [03-response.md](03-response.md), superseded by this handoff.
- Next agent / model / effort: **Codex**.
  - Coordinator: **gpt-6-astra high**, as in handoffs 01–03.
  - Mathematical workers: gpt-6.1-sol xhigh.
  - Code and screens: gpt-6.1-sol medium (high for the exact enumeration code).
  - Astra ultra is allowed **when necessary** (AC's original instruction), each time with a written justification in the LOG.
- Role: developer and orchestrator.
- Branch: `codex/padua-3d-20261106`.
- Input head SHA: `636c90e974845c81befa404e0ff752cb414ea60e`. This is the published audit and handoff-03 head; the following commit publishes this file.
- Main / base: `76ba4214b100c86a44941f5e9a662ce9ce48efb8`. Fetch `main` first and reconcile if it has moved.
- Stage: **WORK**.
- Written by / date: Claude, claude-opus-5-5 xhigh · 2026-11-06, at AC's request.

## AC's instruction (2026-11-06, verbatim)

> "Write a handoff for what you know about Cosets without reflection symmetry and Untested variants of cyclic orbit, and set the branch to work so that codex uses same restarted budget on those directions"

> "Add also what you know on Closing the gap between log³ n and everything observed."

**Budget.** Each new direction gets the handoff-01 budget, **restarted at zero**: **25 rounds each for T7, T8 and T9**, under the same round, gate and stop rules. T9 also gets 25, not T6's cap of 8: this is Claude's reading of "same restarted budget" for the added direction, and AC may correct it. Earlier T1–T6 rounds do not count against them. Add T7/T8/T9 rows to [rounds.md](../rounds.md). Budgets are ceilings, not targets. Stop a direction early only on a gate kill, a proved obstruction or a recorded exhaustion, and log the reason for AC.

## Part A — finish the audit-01 response (carried over unchanged)

Carry out the whole task of [handoff 03](03-response.md) (Task items 1–7, scope limits and acceptance). Answer every finding of [audit-01](../audit-01.md) in `response-01.md`.

Two items gate Part B:
- **M2 (dispositions of the T2 phase, union, mod-6, omit-n3 and T2(a)/(b)/(c) routes).** These become T8's starting records. Record their dispositions before T8's preregistration; T8 may then resume them under its own records.
- **M1/M3 (gate coverage).** The T7, T8 and T9 novelty gates must read the full `state/IDEAS.md`, including every obstruction and disposition table, before any mechanism run. Log the read explicitly, so that the T2 timing deviation is not repeated.

## Part B — new directions

The facts below come from the batch records and audit 01, and they are labelled. Items marked *(sketch)* or *(hypothesis)* are leads for the developer to prove, test or refute. They are **not** recorded results and must not be cited as such.

### Common setting

- A = a + H, where H is a finite subgroup of T³ = (R/2πZ)³ and a ∈ T³.
- X = cos(A), applied coordinatewise; it is the set of sign orbits of A.
- Target: |X| = N = binom(n+3,3) and evaluation Π_n → R^X bijective, then quality, i.e. the Lebesgue constant against the same-degree controls in [report.md](../report.md).
- Use the folded Chebyshev/character dictionary of [t3-cyclic-rank.md](../theory/t3-cyclic-rank.md). It covers phases. Extend it from cyclic H to general H first, as a written lemma.

### T7 — cosets without whole-coset reflection symmetry

**What is known**
- **PROVED and audited:** [PD-N?…T1-01](../theory/t1-minimal-obstruction.md) excludes every whole coset invariant under each of R₁, R₂, R₃, for every n≥2, via the [classification](../theory/t1-reflection-classification.md). T7 is exactly the complement inside the coset class. The broad target [t1-open-class.md](../theory/t1-open-class.md) is OPEN.
- **Verified by the auditor (audit-01 NOTE; orchestrator check, 2026-11-06):**
  - Take H = {2π(i, j, i+j)/4 : i, j ∈ Z/4} ≅ (Z/4)², with a = 0.
  - H is invariant under none of R₁, R₂, R₃. Its 16 torus points fold to **10 distinct nodes in {−1,0,1}³**, and these are **Π₂-unisolvent** (|det| = 256 in the monomial basis).
  - All 10 nodes lie on the cubic x²+y²+z²−2xyz−1 = 0, the compatible relation u = (1,1,−1) with q(u) = 3 in [t3-short-relations.md](../theory/t3-short-relations.md).
  - So the reflection hypothesis of T1 cannot simply be dropped. The same plane family cannot reach n ≥ 3.
- **PROVED, cyclic case only:** a compatible relation u in the dual lattice with q(u) ≤ n kills injectivity ([t3-short-relations.md](../theory/t3-short-relations.md)). All unshifted cyclic orbits mod 39 fail at n=3 ([t3-degree3-extension.md](../theory/t3-degree3-extension.md)).

**Leads**
- *(sketch, to prove)* **Short-relation obstruction for general H.** If H^⊥ ⊂ Z³ (with a compatible phase) contains u with q(u) ≤ n, then X is not Π_n-injective. The cyclic proof uses only the relation; check that.
  - Consequence: a surviving H must have **no compatible dual vector of q-degree ≤ n**. That is a lattice-packing condition on H^⊥ against the octahedron, linking to the deferred Haar-lattice packing lead (`literature-T1.md`, `t1-open-class.md`).
- *(sketch, to prove)* **The class is finite at each fixed degree.**
  - For a node x, the k′ ∈ H with cos(k′) = x satisfy k′_j = ±k_j coordinatewise, so at most 8 points fold together. Hence |X| ≥ |H|/8 and |H| ≤ 8N.
  - Translations a either create fold coincidences, which forces 2a_j into special positions (a finite set of classes), or are generic, giving |X| = |H| and a Zariski-open unisolvence condition.
  - So for fixed n the class is finitely many subgroups × (finitely many special translation classes + one generic stratum). Prove this before relying on it for exhaustiveness.
- *(hypothesis)* **Rank 3 and translations are the live part.**
  - Rank-1 H are T2/T8's cyclic orbits.
  - The verified rank-2 example lives in a plane u·θ = 0 and is capped at n = 2 by that plane's own relation.
  - Every rank-2 H lies in such a plane, so presumably all rank-2 cases die once q(u) ≤ n.

**Cheapest decisive test.** Run an exhaustive exact census at n = 2 and n = 3 over every subgroup of T³ with |H| ≤ 8N (80 and 160), every special translation class, and the generic stratum.
- Filter by exact |X| = N, then exact rank: modular rank, then exact rational or cyclotomic confirmation of every deficiency, as in T2.
- Separate the reflection-invariant part (reproduce T1: zero survivors) from the rest.
- Starting code (audit evidence, not developer code): `audit-01/code/bf_cosets.py` and `bf_fast.py` (subgroup normal forms, |H| ≤ 160).

**Decision rules**
- **No survivors at n = 3:** record a scoped finite PD-N with a proved finite reduction and an independent rerun, and try to prove the general-H short-relation obstruction for all n.
- **Survivors:** apply D2. Preregister a degree-uniform rule before seeing n = 4, 5. Screen quality against Leja/QR. Also test the 2-D Padua structural marker: a positive-weight cubature exact on a large space, i.e. conditions (i)–(iii) of C_k, since it, not unisolvence alone, is what drives Padua's logarithmic growth.

### T8 — untested variants of cyclic orbits

**What is known (PROVED or MEASURED, audited)**
- The screened class:
  - unshifted, odd modulus M = 2N−1, first generator coordinate 1, node parameters k = 0..N−1;
  - full-rank survivors: 4 at n=2, 0 at n=3, 4 at n=4.
- The survivors are only **two node sets per degree** (audit m3):
  - n=4: (1,15,19) ≡ (1,21,29), and (1,11,15) ≡ (1,25,30);
  - n=2: (1,3,7) ≡ (1,4,6) ≡ (1,5,8).
- n=4 best Λ = 37.49, against Leja 19.50 and QR 11.24 (MEASURED, 21³ mesh). The survivors are unisolvent but of poor quality.
- n=3 is closed for every unshifted generator mod 39 (PROVED). No other modulus, phase or degree is closed.
- The census symmetry: units of Z/M plus coordinate permutations give 36/171/561 pairs = 18/100/301 classes.

**Untested variants, in suggested order**
1. **Generating-curve sampling with even moduli and non-unit coordinates.**
   - *(fact to re-verify in the gate)* 2-D Padua is itself a cyclic cosine orbit outside the screened slice: angles (kπ/n, kπ/(n+1)), with even modulus 2n(n+1), z = (n+1, n), and no unit coordinate. Its cardinality comes from fold coincidences, i.e. curve self-intersections.
   - The direct 3-D analogue samples (cos z₁t, cos z₂t, cos z₃t) at t = kπ/M, with even M and general z.
   - This is handoff-01 T2(a) (Lissajous–Chebyshev / Dencker–Erb), which was never executed (audit M2a).
   - Known warning: generic 3-D Lissajous curves do not self-intersect (Bos–De Marchi–Vianello 2017, BRIEF P3′), so exact count N needs designed coincidences.
   - By the fold bound above (sketch), M ≤ 8N for primitive z, so the n = 2, 3 classes are finite. Census them exhaustively.
2. **Phase-shifted orbits.**
   - With a generic phase, no folding occurs and |X| = M, so M = N exactly, with unisolvence a generic condition.
   - Special phases in (π/M)Z³ give finitely many fold patterns.
   - The dictionary in [t3-cyclic-rank.md](../theory/t3-cyclic-rank.md) already includes φ, and `code/t3_checks.py` has phase cases.
3. **Degree sequences omitting n = 3.** Run the same unshifted odd slice at n = 5 (N = 56, M = 111; 1,485 pairs before symmetry reduction) and n = 6. This is cheap, but it can only matter if a quality rule also survives.
4. **Unions of two or three cosets** (T2(b)), sized exactly N. Read IDEA-182/PD-N034 (adjacent-mod-4 unions, an infinite singular subsequence) first. This is the closest negative precedent.
5. **Lattice sample plus structured correction** (T2(d)), and **mod-6 fibres** (T2(c)). Both need a stated structural reason before any run; PD-N037 is the warning.

**Gate and quality**
- D2 is unchanged: preregister in `gates.md` and a T8 preregistration before each run, with a degree-uniform rule and kill rules.
- Census by node-set equivalence classes. Apply the preregistered tie rule literally.
- A family is promising only under D2's full criteria. Finite unisolvent survivors that lose to Leja/QR do not pass, as T2 showed.

### T9 — closing the gap between log³ n and everything observed

**What is known**
- **Universal lower bound, PROVED here and audited ([t6-universal-lower-bound.md](../theory/t6-universal-lower-bound.md)).** Every Π_n-unisolvent X ⊂ [−1,1]³ with N nodes has Λ(X) ≥ max(1, H_{⌊n/2⌋}³/(648π³)).
  - The order log³ n is already in Subbotin (1982 Russian, 1983 English); see [literature-T6.md](../literature-T6.md).
  - The explicit constant exceeds 1 only for n ≈ 7.2×10¹¹ (audit m7). At practical n, nothing beyond Λ ≥ 1 is proved.
  - Where the proof loses: a factor 27 = 3³ in the reflection correction ‖M‖ ≤ 27, and 24 = d·2^d plus π³ in the Fourier lemma.
  - The actual octahedral Fourier Lebesgue constants are ‖D_n‖₁ = 3.38, 9.16, 14.26, 21.12 at n = 2, 8, 16, 32 (auditor MEASURED, [audit-01/T5-T6.md](../audit-01/T5-T6.md)). That is 400–2500 times the lemma's bound.
- **Proved in this topic for constructions:**
  - The monotone Padua stack has Λ ≥ exp((0.1827 + o(1))·n) ([t4-monotone-lower.md](../theory/t4-monotone-lower.md)).
  - Exact-greedy stacks have Λ ≤ exp(O(n log n)) ([t4-stack-upper.md](../theory/t4-stack-upper.md)).
  - No explicit 3-D minimal set in this repository has a *proved* polynomial bound.
- **Classical and literature facts** (to cite as LITERATURE; verify before use):
  - **Fekete points** maximize |det V|. Cramer's rule gives every Lagrange polynomial sup-norm ≤ 1, so **Λ ≤ N = O(n³)**: classical and nonconstructive, with a three-line proof. This is the proved existence upper end.
  - Approximate Fekete/discrete Leja points from weakly admissible meshes satisfy Λ ≤ N·C(A_n) only (LIT-382, UNVERIFIED secondary).
  - Approximate Fekete points from 3-D Lissajous meshes "seem to increase quadratically", numerically only (LIT-392, UNVERIFIED).
  - **Hyperinterpolation** on the cube has operator norm O(log^d n) (Wang–Wang–Wang 2014, LIT-391, UNVERIFIED). De Marchi–Vianello–Xu 2009 (LIT-322) give degree-(2n+1) Chebyshev cubature on about n³/4 nodes, about 1.5·N.
  - So **log³ n is attained by a discrete projection with about 1.5× oversampling** (as reported). The open gap is specific to **minimal-node interpolation**.
  - *Literature lead, not in INDEX, unverified:* Chkifa–Cohen–Schwab-type bounds (Found. Comput. Math. 2014) control lower-set interpolation Lebesgue constants by products of univariate Lebesgue constants of the axis sequence. Check whether this gives a proved polynomial bound for the Leja lower-set reference or for an R-Leja variant. That would be an explicit minimal set with a proved polynomial Λ, for the total-degree simplex (a lower set).
- **Measured** (21³ mesh maxima; these are underestimates of the true sup, not certified):

| n | QR approximate Fekete | Leja lower set | Leja-height stack | (log n)³ |
|---|---|---|---|---|
| 4 | 11.2 | 19.5 | 18.6 | 2.7 |
| 7 | 26.9 | 49.8 | 51.8 | 7.2 |

  The best cyclic survivor at n=4 is 37.5. The degrees are too few and too small to separate log³ n from n^α. No fit was promoted.

**A structural explanation to test** *(sketch by Claude, 2026-11-06; NOT a recorded result; every step is an obligation)*
- **The 2-D Padua mechanism.** The Padua cubature is the pushforward of Haar measure on a cyclic torus coset. The equal-weight coset average of T_a(x)T_b(y)T_c(z) is 2^{−d} Σ_ε e^{iεk·a}·[εk ∈ H^⊥], summed over sign vectors ε.
  - With a = 0, the pushed-forward rule is exact through degree D iff H^⊥ has no nonzero vector of ℓ1-norm ≤ D.
  - A Padua-type degree-(2n−1) rule therefore needs H^⊥ to be a **lattice packing of ℓ1-balls (cross-polytopes) of radius n**.
  - By the fold bound, a node has at most 8 preimages (2^d in general), so |X| ≥ |H|/2^d.
- **In 2-D the diamond tiles the plane by a lattice**, so this can be tight. That is consistent with Padua's exact count; check it against the Padua generator.
- **In 3-D the octahedron does not tile.** Its lattice packing density is 18/19 (Minkowski 1904; verify the source). Hence |H| = det H^⊥ ≥ (19/18)·(4/3)n³, and |X| ≥ (19/18)·n³/6.
  - This exceeds N = (n³+6n²+11n+6)/6 exactly when n³ > 108n²+198n+108, i.e. **for n ≥ 110**.
  - So a *single unshifted coset carrying its own Haar cubature of degree 2n−1 on exactly N nodes* would be impossible for n ≥ 110. The finite range n < 110 stays open.
- **Escapes** (the scope to state):
  - nonzero phases, whose cancellation can rescue exactness;
  - non-Haar weights;
  - unions of cosets;
  - lower exactness degree, for interpolation without the cubature property.
- **Small consistency check (Claude, exact sympy, unrecorded).** The T7 10-point example carries the equal-weight pushforward rule exact through degree 2 (weights 1/16 and 1/8), and *no* weights exact through degree 3. This matches its dual vector (1,1,−1) of ℓ1-norm 3. The developer must reproduce it.
- **Relevance.** If proved, this explains why Padua's log² mechanism does not transfer to 3-D, and it points the search to the escapes above. It fits the deferred Haar-lattice packing lead of T1.

**Routes, cheapest first**
1. **Measurement (MEASURED only).** Certified or refined maxima for the QR, Leja, Leja-height and best cyclic sets at n ≤ 12–16: mesh refinement plus local maximization, preregistered. Also the Lebesgue constants of locally optimized Fekete points at small n. Preregistered fits of log^k n against n^α, with D2's fit rules. This decides what the target growth actually looks like.
2. **Packing sketch.** Write and prove or refute it, including the 2-D tightness check and the phase case. A proof gives a scoped PD-N, or a PD-T where it states a structure theorem. Screen the finite complement only where it is feasible.
3. **Lower bounds.**
   - Sharpen the universal constant: avoid the 27 loss, or compare directly with ‖D_n‖₁. A useful target is a lower bound exceeding 1 at practical n.
   - Class-specific lower bounds: every stack ordering, using the permutation-mean comparison of T4 (alternating ≈ 0.089 per degree, MEASURED); coset classes, through their shortest dual vectors.
4. **Upper bounds.** The first *proved* polynomial bound for an explicit minimal 3-D set: the Leja lower set via product bounds, or Leja-height stacks improving exp(O(n log n)). Check the literature before claiming anything new.
5. **Near-Padua constructions.** Start from the log³ hyperinterpolation nodes (about 1.5·N) or a non-Haar positive cubature of degree 2n−1. Extract or correct to exactly N nodes while tracking Λ. Use T5's commutator-rank node bounds as constraints: by Claude's reading of `evidence/t5-exact.json`, degree 2n−1 = 5, 7, 9 needs at least 12, 24, 41 nodes, against N = 20, 35, 56, so they do not exclude it. Verify that reading.

**Decision rules.** Statuses follow the evidence rules. A measured growth fit never becomes a theorem. Any novelty claim needs the full gate and a source comparison. Stop T9 when routes 1–3 are recorded with outcomes and routes 4–5 are either screened or deferred with resume conditions.

### Rules carried from handoff 01 and audit 01

- D0/D1 have passed. Any new tool must first reproduce:
  - the T2 census and the H39 result;
  - 2-D Padua as a cyclic orbit (T8.1) or coset (T7) at n ≤ 10;
  - T1's zero-survivor result on the invariant part.
- **D3:** an obstruction counts only if its d = 2 specialization provably admits 2-D Padua, and it is checked by enumeration over the **full** finite class wherever that class is finite (audit M4).
- Every candidate gets a provisional IDEA-template record, including failed, deferred and equivalent ones, with closest entries, falsifier and resume condition.
- Numerical agreement earns MEASURED only.
- A computer-assisted PROVED needs all of: a proved finite reduction, exact arithmetic, committed checker and evidence, and an independent rerun.
- Provisional IDs continue the topic's scheme (`…-codex-T7-nn`, `…-codex-T8-nn`, `…-codex-T9-nn`).

## Read first

- AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md at the branch head.
- The LOG (including the AC instruction entry for this handoff), BRIEF, [handoff 01](01-work.md) for T2(a)–(d), D2/D3 and the round rules, and [handoff 03](03-response.md).
- [audit-01.md](../audit-01.md) and [audit-01/T1.md](../audit-01/T1.md) (NOTE-1 example, full-cap enumeration), [audit-01/T2-T3.md](../audit-01/T2-T3.md) (symmetry classes) and [audit-01/novelty-records.md](../audit-01/novelty-records.md).
- The full `state/IDEAS.md`, `literature/INDEX.md`, and the T1/T2/T3 theory, attempt, gate and literature files.

## Scope limits

- Do not reopen the accepted T1–T6 theorems, the H39 cover, the T4 kill at n=7, or any killed fixed family.
- Do not edit the audit report or its appendices.
- No final IDs, reservations or shared-registry edits in this step.
- Do not change other topics, main, tags, `.github/` or repository settings. Only AC merges. Keep earlier handoff bodies intact.
- Keep receipts under 16 KiB with committed code. Large censuses stay regenerate-only, with identities recorded.

## Acceptance and outputs

**Part A:** `response-01.md` and fixes, as in handoff 03.

**Part B:**
- `attempts/T7.md`, `attempts/T8.md`, `attempts/T9.md`, `novelty-gate-T7.md`, `novelty-gate-T8.md`, `novelty-gate-T9.md`, the preregistrations, and `theory/t7-*.md`, `theory/t8-*.md` and `theory/t9-*.md`, with explicit statuses;
- code and receipts;
- updated `rounds.md`, `gates.md`, `report.md`, the LOG and the results file;
- for each direction, a recorded stop reason.

Checkpoint and push substantial results promptly. When done:
- Commit the outputs.
- In a following commit, close this handoff `done in <sha>` and open handoff 05: a Claude audit covering the focused re-audit of the Part A material changes plus a substantive audit of T7/T8/T9 (Opus 5.5 xhigh).
- Push before replying, and end with the short continuation prompt.
