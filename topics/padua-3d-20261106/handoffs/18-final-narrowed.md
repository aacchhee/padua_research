# Handoff 18 — padua-3d-20261106 — audit-04 response and the final narrowed deep-structure round set

- Status: superseded by 19: AC approved the pending decisions (frontier plan, E4 convention, storage allowance, deviations, lattice boundary) on 2026-11-08
- Previous handoff: [17-pruning-audit.md](17-pruning-audit.md)
- Next agent / model / effort: **Codex.**
  - Coordinator: gpt-6-astra high.
  - Mathematical development: gpt-6.1-sol xhigh. C1 is a proof; Astra ultra is allowed for a stalled C1 proof, with written justification.
  - Code and checks: gpt-6.1-sol high.
  - Mechanical record work: gpt-6.1-sol medium.
- Role: developer and orchestrator.
- Branch: `codex/padua-3d-20261106`.
- Input head SHA: `286e310400398a1ab7604c209ced1a7e7c7f0b71`, the commit that adds `frontier-assessment.md`; the following commit publishes this file. Audit outputs: report `1cb3841`, auditor fixes `bbf4b42`.
- Main / base: `f70a260e5b5f9a01209dc8a05faabdcf8db1feeb`. Fetch first and reconcile if it has moved.
- Stage: **WORK**.
- Written by / date: Claude, claude-opus-5-5 xhigh · 2026-11-08.

## AC instructions this step implements (verbatim; see the LOG entry of 2026-11-08)

- "When finished, use opus extra to reassess the 3d frontier: should this direction be frozen or is it worth pursuing some extra rounds? …"
- "… I suspect that one has to look for deeper algebraic structures in 2D, not just sin/cos intersections, that may transfer to 3D …"
- "otherwise this branch becomes substantial. I authorize exceeding all limits with 100%, to be potentially discussed at PR"
- "so you mean the determinantal route is worth studying deeper?"

Claude's decision, in [frontier-assessment.md](../frontier-assessment.md): **NARROW, then FREEZE.**

**Storage allowance.** Claude's reading is up to 100% over the storage limits: 32 KiB per file and manifest, 10 MB repository total. This is provisional and goes to discussion at PR. AC may override this handoff's plan at any time.

## Part A — respond to audit 04 (`response-04.md`)

Answer [audit-04](../audit-04.md) G1–G7, and every item that [audit-04-fixes.md](../audit-04-fixes.md) returns to the developer. Each gets a fix, an evidence-based rejection or an explicit unresolved item.

- **G1.** n7 tie-repair label or disclosure. Amend "n5/7 selectors unchanged".
- **G2.** C1 hardware-dependent cost-gate addendum or disposition revision.
- **G3.** Refresh or retire the stale `independent-r06-pins.json` replay.
- **G4.** Add the reciprocal "Split into" entries.
- **G5.** Disclose the U3 F absolute-versus-relative tolerance.
- **G6.** Pruning and U2 gate addendum: LIT-385, LIT-386, the design literature, Lebesgue-point optimization literature, and Gunzburger–Teckentrup.
- **G7.** Pruning candidate records and dispositions; P5 in template form; the agent component in provisional IDs.

**Manifest limit.** Under the allowance the master manifest may grow up to 32 KiB. Record the use of the allowance in the PR body, not as permanent policy. Do not split files to evade the limit.

## Part B — final narrowed round set (new counters, ceilings only)

These are new counters, separate from all earlier ones. **All other construction, optimization and pruning directions are frozen:** T7–T10 construction searches, U1–U3, and P. Do not spend their unused slots.

The stop rule is strict:
- Each item ends with an actual outcome or its kill rule.
- "Programme exhausted" is not a reason while a listed step remains untried.
- Preregister in `gates.md` and an item protocol before every run.
- The novelty gate for each new mechanism must read the full `state/IDEAS.md` before generation. Candidate records follow `templates/IDEA.md` and use the provisional IDs in the assessment, `IDEA?padua-3d-20261106-claude-01..08`.

| Item | Ceiling | Content | Kill / stop |
|---|---|---|---|
| **D1 = C1** spectral obstruction | 6 rounds | Write a full proof attempt (see below). | Stop after 4 rounds without closing the limit step, and record the sketch as OPEN or CONDITIONAL. |
| **D2 = C2** determinantal / symmetroid | 3 rounds | Four steps, in order (see below). | Kill if no real-in-cube configuration exists at n = 3 or 4. Also kill if the 2-D calibration shows no exploitable structure **and** the best Λ exceeds twice the Gunzburger–Teckentrup optimum at both n = 3 (4.05) and n = 4 (5.09). |
| **D3 = C7** | 1 round | Certify one non-lattice Padua-type set at n = 3: a positive degree-5 rule on 20 nodes, unisolvent for degree 3. Use interval Newton plus exact rank. Record its Λ, MEASURED. | Fail after 1 round. |
| **D4 = C3 + C4** | 2 rounds | Normalized-Gram λ_min diagnostic and certified two-sided Λ intervals (Białas-Cież et al.) for the topic's best sets at n = 4..16. Double-Lee-sphere bound det L ≥ (2/3)·n·(2n²+1), and an enumerator restart that makes the n4..7 minima independent of the 18/19 import. | Finish, or record measured infeasibility. |
| **D5 = C8** framing and paper | 3 record rounds (not research) | Primary or coverage-labelled records and framing corrections (see below). Then draft a short paper note, `paper-note-draft.md`. | — |

**D1 details.** For every positive cubature on the cube, exact through degree 2n−1 (product Chebyshev measure; also try general doubling weights), aim to prove N ≥ (1+c)·n³/6 for n ≥ n₀.
- Use the exact identity Σδ_i = N − dim Π_{n−1}.
- Prove a local limit to exponentials on the octahedron at critical density.
- Contradict Lev–Matolcsi 2022 / Greenfeld–Lev 2017; import the exact statements as LITERATURE with primary reading.
- Kill tests: the argument must admit 2-D Padua; it must be consistent with sphere and disk cubature literature; the identity must check exactly on the topic's lattice rules.
- Independent rerun of any computation.

**D2 details.**
1. Derive the Hilbert–Burch matrix of the 2-D Padua points and identify its structure.
2. At n = 2, 3, 4, run exact Gröbner bases, radicality and standard-monomial unisolvence checks for random and structured pencils, over a large prime and over Q.
3. Search for configurations with all nodes real and inside the cube, starting from the Ottem–Ranestad–Sturmfels–Vinzant real-node symmetroids and from Jacobi-structured Aᵢ. The Jacobi-structured case is the concrete IDEA-120 link.
4. Optimize Λ over the matrix parameters (MEASURED).

**D5 details.**
- Li–Sun–Xu Cor. 4.12 and conjecture; Li–Xu 2010.
- Wang–Wang–Wang, which may make T10's conditional log³ known.
- Gunzburger–Teckentrup as benchmark; Krieg–Pozharska–Ullrich–Ullrich; Dolbeault–Chkifa; Fekete ≤ N.
- Golomb–Welch, Horak–AlBdaiwi and Gravier–Mollard–Payan for the lattice packing and tiling work.
- Bel-Afia–Meroni–Telen and Lev–Matolcsi.
- Run a fulltext novelty gate for the note's claims: the reflection-coset theorem, the monotone-stack exponential bound, the n=2 classification, the lattice minima and packing consequence, and D1 if proved.

## Read first

- AGENTS.md, WORKFLOW and CODEX.md at the head.
- The LOG entries of 2026-11-08.
- [audit-04](../audit-04.md), its appendices and [audit-04-fixes](../audit-04-fixes.md).
- [frontier-assessment.md](../frontier-assessment.md) and all [scout reports](../frontier-2026-11-08/), especially S2 and S4 (C1), S6 (C2), S1 (C7) and S3 (C3/C4).
- The full `state/IDEAS.md` for the new gates.

## Scope limits

- Do not reopen accepted theorems or frozen directions.
- Do not edit audit reports, fix notes, the frontier record or earlier handoff bodies.
- No final IDs, reservations or shared-registry edits.
- Do not touch other topics, main, tags, `.github/` or settings. Only AC merges.
- Keep exact certificates small and committed. Bulk outputs are regenerate-only, with identities recorded.

## Acceptance and handoff

- `response-04.md` and its fixes.
- D1–D5 records, with protocols, theory files with explicit statuses, code and receipts.
- The paper-note draft.
- Updated rounds, report, LOG, results and PR.

Then:
- Commit the outputs.
- In a following commit, close this handoff and open handoff 19: a Claude audit (Opus 5.5 xhigh) covering the focused audit-04 response plus D1–D5.
- If accepted, the following step is Codex PR preparation: reservation, registry application and readiness, which **freezes** the direction.
