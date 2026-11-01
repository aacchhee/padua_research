# PD-N?programme-ideas-claude-02 — Windowed rational Lanczos recurrences for one-linear-pole-per-degree bivariate spaces: three-block window fails algebraically; tested corrected windows lose orthogonality ≈ 10× per degree

Final ID: **PD-N040** (allocated 2026-11-01 under AC's authorisation; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-N.
Aliases: gen1-3 K3; "three-block orthogonalisation window" (refuted form); L3, L3c ("project two, constrain one"), L4c; windowed pencil-pair IEP solver; Finding 0.
Split from: `checks/decisive-gen1-3.md` Finding 0, T3 and Verdict at `614709d` ("the O(MN^{3/2}) solver does not exist; only full reorthogonalisation works").
Split into: none.

## Statement

Spaces: V_t = Π_t/π_t with π_t = ℓ_1⋯ℓ_t, one linear factor ℓ_s per degree (pole classes Ppt, Pbhh, Ldiag, Pdiag, generic real lines as defined in `checks/decisive-gen1-3.md`), discrete inner product of the stated node sets, W_t the degree-t orthogonal block of V_t.

(i) **Three-block window (MEASURED, exact blocks).** For M = 120 random nodes, t ≤ 9 and five pole classes, the candidates C_t = (W_{t−1} + W_t + xW_t + yW_t)/ℓ_{t+1} contain W_{t+1} (to 1e-15 … 3e-7), but projecting C_t off the last three blocks does not isolate W_{t+1}: the remainder loses exactly one dimension per additional projected block (ranks 22, 15, 14, …, 9 for k = 1, …, 8 at t = 7) and reaches dim W_{t+1} = t + 2 only after all older blocks are projected. The polynomial control has no such leakage (≤ 1e-16).
(ii) **Corrected windows (MEASURED, finite precision).** The step "project off W_t, W_{t−1}, then keep the part orthogonal to W_{t−2} as a constraint" (L3c) isolates W_{t+1} with exact blocks for all five classes at t ≤ 9 (not proved). Run as a recurrence, L3c and the variant L4c lose orthogonality: δ = max|QᴴWQ − I| at n = 24, N = 325 (64² Chebyshev grid, M = 4096) ranges over 2.7e-2 … 5.4e-1 across classes Ppt and Pbhh, ε_min ∈ {3e-4, 3e-3, 3e-2} and both pole orderings (primary Ppt, 3e-4, far-first: 0.27), and 0.19–0.73 on M = 400 random nodes, n = 22; growth ≈ 10× per degree from t ≈ 6, the same slope in 80-bit precision shifted by about three degrees. Full reorthogonalisation (LF, O(MN²)) stays at 2e-15 … 3e-14, and the polynomial windowed control at ≤ 1.3e-14.

## Definitions

As in `checks/decisive-gen1-3.md` (pre-registration and Results).

## Assumptions

The pole classes, tapers, orderings, node sets, degrees and implementations L3, L3c, L4c of `checks/code/decisive/gen1-3/orf2d.py` (frozen at `614709d`); known block dimensions enforced in L3c/L4c after floating-point rank decisions fail at t ≈ 9 (declared deviation).

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (i) three-block window is not a Lanczos step | MEASURED (exact blocks, finite scope) | `checks/code/decisive/gen1-3/window_exact.py/.out` |
| (ii) "project two, constrain one" isolates W_{t+1} | MEASURED (t ≤ 9), not proved | same |
| (ii) orthogonality loss of L3c, L4c | MEASURED | `run_T1_T3.py` → `T1_T3.out`; primary setting independently replayed by the Codex audit (L3 0.9425/0.9844, L3c 0.2882/0.3979, L4c 0.3041/0.4525, LF 3.0e-15/5.5e-14 far/near; values vary with BLAS/library versions, qualitative failure reproduced; `audit-support/rejections-check.json`) |

Candidate / claim disposition: the candidate mechanism "windowed rational Lanczos as an O(MN^{3/2}) conditioned solver" (gen1-draft-3 residue, IDEA?programme-ideas-claude-03) is REJECTED.
Rejection reason: failed — within the tested implementations and parameter sets it does not produce an orthonormal basis (K3 fired: δ > 1e-6).

## Negative-result scope (PD-N only)

Attempted mechanism: windowed rational Lanczos for one-linear-pole-per-degree total-degree spaces (IDEA?programme-ideas-claude-03), implementations L3, L3c, L4c.
Parameter range: as in the Statement. **Not covered (untested):** the rotation-based (Givens-updating) pencil-pair IEP; selective or partial reorthogonalisation; pole-cancelled candidate forms; other pole placements or orderings; n > 24; any proof that no stable O(MN^{3/2}) algorithm exists. The negative is about the tested implementations, not about the rational-function family.

## Depends on

None.

## Checks

`checks/code/decisive/gen1-3/` (frozen at `614709d`): `window_exact.py/.out`, `run_T1_T3.py`/`T1_T3.out`, `run_T1b.py`/`T1b.out`, `orf2d.py`. Pre-registration at `a8364b9332e651c4e64115667b0411d38234fcd0`. Audit replay as in the table.

## Sources

Boullé–Herremans–Huybrechs, arXiv 2312.13202 (target space and stated open least-squares solver problem; coverage as recorded in `checks/decisive-gen1-3.md`).

## Proof or evidence

Finite measurements as tabulated.

## Scope

A MEASURED failure of the tested implementations on the tested settings; it does not exclude a stable windowed algorithm of another form.

## Open items

The untested alternatives listed above; a proof of (ii)'s exact-block statement (`OPEN_TARGETS.md` B1).

Registered (provisional ID) in `PROOF_STATUS.md` and `state/IDEAS.md` by the response-01 addendum at AC's instruction "register negative results" (2026-11-01).

## History

- 2026-11-01, gen1-3 adversarial agent (claude-fable-5-1, xhigh): three-block window asserted from a complement-dimension count.
- 2026-11-01, gen1-3 decisive agent (claude-fable-5-1, xhigh): Finding 0 and K3; Verdict wording "the O(MN^{3/2}) solver does not exist", "only O(MN²) rational Arnoldi works".
- 2026-11-01, Codex audit-01 A5 / rejections-review "scope caution": negative is about the tested implementations.
- 2026-11-01, response-01 (claude-opus-5-5, effort not exposed): this record; broad wording qualified in the sources.
