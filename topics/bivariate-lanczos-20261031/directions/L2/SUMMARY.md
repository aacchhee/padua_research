# L2 — Direction summary after R03 + reconstruction 01 (2026-11-01)

> Orchestrator note: saved by the orchestrator from the L2 developer's hand-back text (content unchanged apart from formatting). Response: [response-recon-01.md](response-recon-01.md).

Developer Claude Opus 5.5 xhigh; 3 of 10 rounds; u = 2⁻⁵³; IDs provisional; no novelty claims.

## Ranked surviving results

1. **PD-T?…-201 PROVED (confirmed):** exact 2D Simon bound max|W_nᵀ F W_{n−1} − T_F| ≤ 2ε_c + 2(μ₁ + η²)τ₁ + ηγ + O(η²)‖T‖ + 4‖E‖; a two-pass window gives local orthogonality (Prop. L) ⇒ O(u) F-section.
2. **PD-N?…-201 MEASURED (confirmed with independent well-conditioned references):** BJ + any reorthogonalization, incl. CGS2-against-all (V+A type; Zhu–Nakatsukasa identification UNVERIFIED), drifts from S_n on non-product sets (rot π/4 n = 24 ~4e-3, triangle n = 20 ~1e-2); linear in working precision; no decay with M to 1e5.
3. **PD-T?…-202 PROVED (confirmed):** commutator residual follows the Gram column recursion with clamped J-columns; reorthogonalization enters only as coefficients; reference-free drift bound (bounds max_{s≤n} θ_s). **PD-T?…-205 PROVED under condition (C) + acyclicity;** (C) ⇒ acyclic OPEN (checked n ≤ 5; proved for BJ).
4. **PD-T?…-203 MEASURED (confirmed on 3 sets):** ω-estimate not killed (max L/E 1.44, E1D 3.85); tracks ≤ 7× off clustered sets; 2.4e5 over on the cubic checkerboard.
5. **PD-T?…-206 MEASURED:** adaptive selection keeps the drift bound < √u on 5/6 non-product sets; two-relation on 6/6 but loss 0.53 on the cubic checkerboard.
6. **PD-T?…-207 MEASURED:** PRO-2D-J semi-orthogonal with O(u) F-sections on 11/12 sets at 0.16–0.71 of CGS2-all; REJECTED on the cubic checkerboard (PD-N?…-207); does not repair drift.
7. **PD-T?…-204 MEASURED:** F-error follows the local level; the two-pass window removes the local channel.

## Failed routes (PD-N, MEASURED)

202 rounding-only trigger; 203 every one-relation rule as a uniform drift fix; 204 exact/long-double window dots (coefficient channel only 1.3–8.5×); 205 E3 sources; 206 one-pass window F-sections; 207 PRO-2D-J on the cubic checkerboard.

## Prior-art separations (no novelty claim)

Simon 1984 Thm 2 (digest; qualitative, entrywise √u; LAA 61 Thm 5 unread): here an exact bound, Frobenius η, explicit local hypothesis (Jia–Li 2021 template also assumes it). Simon/PROPACK ω-recurrence: here 2D window, implicit J-section, commutator sources. Zhu–Nakatsukasa 2026 V+A: cost comparator; drift finding if the identification holds (check their code). Liu–Narayan 2023: two-relation algorithm predecessor. BPS 2010 Rem. 9 + L1 reconstruction 01: origin of selection rules. A dedicated prior-art check of the span drift is in reviews/L2-prior-art-01.md.

## Briefs

(a) Hybrid one/two-relation selection switched by the online defect δ_A(s), with PRO-2D-J on top, on fresh pre-registered sets (IDEA?…-211 deferred). (b) Prove (C) ⇒ acyclicity; residual theory for non-(C) rules (adapt). (c) M = 1e6 runs on syvert (R02 §7 commands). (d) Closed-loop source model for clustered product measures; cause of PD-N?…-207. (e) Ready for audit: 201, 202, 205 (restricted), measured tables.
