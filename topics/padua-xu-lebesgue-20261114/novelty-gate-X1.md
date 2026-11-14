# Novelty gate X1 — Xu-points Lebesgue function: vertex value, expansion, argmax

Orchestrator: Claude (Opus 5.5), 2026-11-14, rules `2d60e22`. A relaxed scan at the start of the topic, as BRIEF §3 and AGENTS.md require. The full `state/IDEAS.md` read is the auditor's, at audit.

## Scan scope and terms

- `state/IDEAS.md` (1296 lines) and `PROOF_STATUS.md` (745 lines): `grep -i` for: Xu point, Xu interp, XU, Morrow, MPX, vertex, vertices, checkerboard, Lebesgue constant, argmax, four corners.
  - "Xu point": IDEAS 0, PROOF_STATUS 0.
  - "Morrow": IDEAS 1 (IDEA-047), PROOF_STATUS 0.
  - "argmax": 59 IDEAS / 70 PROOF_STATUS lines, all of them Padua.
- The same terms across `topics/`, `tracks/` and `literature/`: 19 files mention Xu points and 47 mention Morrow. They are context, survey or literature notes: programme-ideas, padua-literature, padua-3d, mz-constants, padua-mz-2d. None contains a Xu-point Lebesgue claim.
- Full entries read:
  - IDEA-047, IDEA-048, IDEA-206 (Lebesgue theory of checkerboard (Padua-type) interpolation; proposal-1) and IDEA-318;
  - PD-T101 (Padua corner formula record);
  - the PROOF_STATUS rows PD-T098/099, T229, T246, T269–T271, T364, T368 and T674;
  - LIT-379 (Kolomoitsev–Lomako) and LIT-486 (BCDMV).

## Shortlist and verdicts

| Provisional candidate | Closest entries | Separation criterion (falsifiable) | Cheapest decisive test | Verdict |
|---|---|---|---|---|
| X1-C1: closed form of λ^Xu_n at the non-node vertices, with a sharp three-term expansion | PD-T101, PD-T269–T271 (Padua corner value and expansion, N = n+½); LIT-379 (KL, Lissajous–Chebyshev leading term) | Different node set: the (n+1)² Chebyshev–Lobatto checkerboard with parity n+1. Different space V_n (σ-extra functions), and a different kernel ½(K_n+K_{n+1}) − ½(±)T_n-correction. KL Thm 2.1 excludes the m = n case. **Killed if** λ^Xu_n(v) equals a Padua corner value Λ_c(m) (or a fixed affine combination of them) under some index map, identically in n. The expansion would then be a corollary of PD-T269–T271. | Compare the high-precision Xu vertex values (evidence/xu-vertex-values.json) with Padua Λ_c(m) for nearby m and with ½(Λ_c(m)+Λ_c(m′)). Use PSLQ on the differences for n ≤ 40. | **new-variant** pending the test. A corollary relation, if found, is recorded and used, and only the residual is claimed. |
| X1-C2: exact argmax set = V* (n even: all four vertices), eventually or for every n | PD-T229, PD-T246, PD-T364, PD-T674 (Padua argmax at the two non-node corners) | Different kernel and node geometry; the D4 symmetry (Lemma S) has no Padua counterpart. Padua localization (PD-T215–T228) is proved for the Padua phase-diamond only. **Killed if** a certified non-vertex point beats the vertices (G1 kill). | G1 screen, n ≤ 60 | **new** (conjecture of BCDMV 2006, open in the documented search) |
| X1-C3: odd-n variant (V* = {(1,−1), (−1,1)}) | none | Outside the published conjecture's even-n setting | G1 screen, odd n | **new-variant**; reported separately |

Forward-citation search: lit-notes/X1-sources.md §6. No matching result was found in the documented search. The source statements are not exhaustive: BdMV Thm 1's constant and the lower-bound papers are unread (X1-sources §9).
