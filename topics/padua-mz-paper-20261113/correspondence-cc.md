# MZ-CC correspondence table (task 1; gate W1)

Every numbered statement that is, or will be, in MZ-CC. Status from `PROOF_STATUS.md` at `b5388c2` (unchanged on this branch). "Planned §" refers to [plan-cc.md](plan-cc.md). "In paper" is one of **verbatim** (statement equals the record's scope), **weakened** (explicitly weaker; reason given), **omitted** (reason given), or **to add** (not yet in the text). This table is updated whenever the text changes; the final state is checked before the final build.

Rule (W1): every PROVED row is verbatim or explicitly weakened; no OPEN or MEASURED item appears as proved.

| Current label (post-split no.) | Planned | ID | Record status | Exact scope of the record | In paper (now → target) |
|---|---|---|---|---|---|
| lem:identities (2.1) | Lemma 2.1 | PD-T013 | PROVED | weights, positivity, aliasing, ADE, mass/defect matrices | verbatim → verbatim |
| lem:weight-comparison (3.1) | Lemma 2.2 | part of PD-T017 proof | PROVED (routine step) | interior two-sided comparison, m_j/N² floor; S_N error bound | verbatim → verbatim + displayed S_N error bound (already in its proof) |
| lem:floor (2.2) | Lemma 2.3 | PD-T015 | PROVED | E/N ⪯ M ⪯ (π/2)E on Π_{N−1} | verbatim → verbatim |
| thm:upper (2.3) | Thm 3.1 | PD-T014, PD-T022 | PROVED | Q_N(p²) ≤ (2−4/N+4/N²)∫p² on Π_n, n<N; N=2 exact; strict for N≥3 | verbatim → verbatim |
| Remark 2.4 (alt. proof) | Remark | PD-T015 application | PROVED (historical bound 2−2/(πN)) | | verbatim → shortened, still a proved remark |
| Remark 2.5 | Remark 3.5 | PD-N002, PD-T016 | PROVED | D not PSD for N≥5; T_N quotient 2(4N²−1)/(4N²−2) > 2 | verbatim → verbatim |
| thm:ratio-upper (4.1) | Thm 3.2 | PD-T022 | PROVED | Q_N(p²) ≤ (1+ρ)∫p², strict if 2n>N | verbatim → verbatim |
| cor:ratio-endpoint (4.2) | Cor 3.3 | PD-T022 | PROVED | | verbatim → verbatim |
| — | Thm 3.4 | PD-T526 | PROVED | λ_max(G_{N,N−1}) ≤ 5/3 for every N≥2; not sharp | absent → **to add**, verbatim |
| thm:cardinal (3.2) | Thm 4.1 | PD-T017 | PROVED | ∫p² ≤ K_N Q_N(p²) on Π_N | verbatim → verbatim |
| thm:harmonic (3.3) | Thm 4.2 | PD-T018 | PROVED | λ_−(N,N−1) ≤ 128000/(log N)² for every N≥2 | verbatim → verbatim |
| — | Lemma 4.3 | PD-T522 | PROVED | ‖V‖ = 2/π on L²(0,1); quotient π⁴/8 attained at cos(πx/2); antisymmetric two-copy model | absent → **to add**, verbatim |
| — | Prop 4.4 | PD-T523 | PROVED | limsup (log N)²λ_−(N,N−1) ≤ π⁴/8, all N and each parity; trial family | absent → **to add**, verbatim |
| — | Lemma 4.6 | PD-T544 | PROVED | signed remainder bound 1600, every finite input | absent → **to add**, verbatim |
| — | Lemma 4.7 | PD-T545 | PROVED | discrete primitive bound (A_J²/2+3/2)E | absent → **to add**, verbatim |
| — | Thm 4.5 | PD-T546 (+PD-T523) | PROVED | lim (log N)²λ_−(N,N−1) = π⁴/8 through all N; same on Π_N; finite bound (2) for L ≥ 16 | absent → **to add**, verbatim (finite bound included) |
| cor:endpoint (3.4) | Cor 6.1 (absorbed) | PD-T017/018/014 consequence; PD-T527 | PROVED | η_N → 1; κ_2 ≍ (1+log N)² | verbatim → replaced by the sharper Cor 6.1 (old statement implied by it) |
| — | Cor 6.1 | PD-T527 | PROVED | min(1/K_N,1/3) ≤ 1−η_N ≤ min(1,128000/log²N) | absent → **to add**, verbatim |
| — | Cor 6.1 | PD-T?mz-paper-claude-01 (a)(b) | PROVED (new; independent check PASS with corrections, applied) | 1−η_N=λ_− for N≥57; (log N)²(1−η_N) → π⁴/8; κ_2/(log N)² → 8Λ_edge/π⁴ (numeric interval computer-assisted via PD-T547) |
| — | Cor 4.x | PD-T?mz-paper-claude-01 (d) | PROVED (new; check pending) | ‖𝓘_N‖_{ℓ²_w→L²}/log N → 2√2/π² | absent → **to add**, verbatim | absent → **to add**, verbatim; flagged for audit |
| rem:rate (3.5) | Remark 6.2 | — | — | | to be **rewritten**: the eventual dominance is now proved (Cor 6.1); effective onset not proved |
| — | Def. 5.0 | PD-T528 | definition/prediction pointer | definition of Λ_edge (P) | absent → **to add** as definition |
| — | Lemma C.1 (App. C) | PD-T548 | PROVED | closed-form C_ij (Si, Cin), absolute convergence | absent → **to add**, verbatim |
| — | Prop 5.2 | PD-T529 | PROVED | fixed-J errors (1)–(3); 1 ≤ Λ_edge ≤ 5/3; liminf ≥ Λ_edge on each parity | absent → **to add, weakened**: qualitative fixed-J convergence, positive definiteness of C, boundedness, liminf ≥ Λ_edge. The explicit constants are dropped because they only serve the omitted PD-T531 |
| — | Thm 5.3 | PD-T530 | PROVED | lim λ_max(G_{N,N−1}) = Λ_edge ∈ [1,3/2], all N; qualitative | absent → **to add**, verbatim |
| — | Prop 5.4 | PD-T547 | PROVED (computer-assisted) | Λ_edge ≥ 1.0044369, one-sided | absent → **to add**, verbatim, "one-sided" explicit |
| — | — | PD-T531 | PROVED | finite L_N ≤ … ≤ U_N, U_N−L_N → 0 | absent → **omitted**: its proof is long and nothing in the paper depends on it. Its practical bracket width exceeds 0.05 at every N evaluated, by MEASURED float estimates of the formula (PR #31 audit A8), so it adds no digits. Existence of the limit is Thm 5.3. The paper does not mention it. |
| — | §9 | PD-T027 | PARTIAL | uniform gap (PD-T526) and limit/identification (PD-T530) PROVED; **decimal value OPEN** | OPEN part stated as open problem only |
| — | §9 | PD-T020 | PROVED via PD-T546/523 | | the old §7 "open" sentence is **deleted**; Thm 4.5 states the result |
| thm:ratio-lower (4.3) | Thm 7.1 | PD-T023 | PROVED | | verbatim → verbatim |
| cor:strong (4.4) | Cor 7.2 | PD-T024 | PROVED | | verbatim → verbatim |
| prop:counterexample (5.1) | Prop 8.1 | PD-T019, PD-N004 | PROVED | exact U formulas; N=512 defect > 3/4 | verbatim → verbatim |
| prop:hyper (5.2) | Prop 8.2 | PD-T025 | PROVED | general upper-Gram estimate | verbatim → verbatim |
| eq:Bcc/eq:CCerror (text) | Cor 8.3 | PD-T025 CC application; PD-T?mz-paper-claude-01 (c) | PROVED | B=min{1+ρ,5/3} | text → **to add** improved constant; flagged |
| Table 1 | §9 | PD-T026 | MEASURED | N=40…1280 | measured → measured |
| — | §9 | PD-T532 | MEASURED | J512 proxy 1.0044369188646673 etc. | absent → optional, labelled MEASURED, "not a certified decimal" |
| — | §9 | PD-T525 | MEASURED | K1 fits; intercepts exceed π⁴/8 | absent → optional; if used, labelled MEASURED with the warning that the intercepts exceed the proved limit |
| — | — | PD-T524 | historical CONDITIONAL prediction | | **omitted** (superseded by PD-T546) |

Counts at this checkpoint: 14 numbered statements in the post-split text (12 statements + 2 unnamed remarks) all mapped; 12 planned additions; 2 omissions with reasons.

## Changes log

- 2026-11-13 (task 3, first integration): sections reordered as in plan-cc (§2 Preliminaries incl. weight lemma; §3 upper spectrum; §4 endpoint minimum; §5 stub; §6 consequences; §7 fixed ratio; §8 hyperinterpolation; §9 finite/open; Appendix A).
  - Added, verbatim at record scope: Thm `thm:five-thirds` (PD-T526, with the restriction/min consequence that is a one-line corollary of PD-T526 and PD-T022), Lemma `lem:volterra` (PD-T522), Prop `prop:sharp-trial` (PD-T523), Thm `thm:sharp-min` (PD-T546 with its finite bound for L≥16), Lemmas `lem:signed-remainder` (PD-T544) and `lem:discrete-primitive` (PD-T545), Appendix A with proofs.
  - **Proof-route change, for the audit:** the paper proves Prop. `prop:sharp-trial` (PD-T523) through the shared endpoint representation, Lemma `lem:endpoint-rep`(c). That lemma is the one-edge decomposition of the PD-T546 proof, §1–2, built on PD-T544. The record S1-sharp-one-sided instead proves a pointwise bound (D) for smooth envelopes. The statement is unchanged. The new route keeps every step: the discrete energy, the sum–integral comparison, the oscillation averaging, and the trial's degree cancellation. It replaces only the pointwise remainder by an L² remainder of size O(L), which is o(L^{3/2}).
  - Lemma `lem:endpoint-rep` collects PD-T546 proof §1–2 (weights (3)–(4), exact formula (5), remainder (6), one-edge decomposition (7) with the signed-error and cross-edge bounds (8)). It is not a new claim.
  - §5 is a stub, so the build is a working draft. `cor:endpoint` and `rem:rate` sit unchanged in §6 for now.
- 2026-11-13 (task 3, §5): §5 and Appendix B are written. Prop `prop:fixed-trial` (PD-T529, **weakened** as recorded above: qualitative fixed-J limits, positive definiteness, 1≤Λ_edge≤5/3, liminf ≥ Λ_edge) and Thm `thm:edge-limit` (PD-T530, verbatim: limit through all N, 1≤Λ_edge≤3/2). The definition (PD-T528) is given as the supremum over the core 𝒱₀, which is identical to the registered (P) because ĝ(πj)=u_j and ĝ(0)=−2Σ(−1)^j u_j. The transition matrices of PD-T526 are renamed H→Y, K→Z, since K_N is the constant of Thm 4.1. Appendix B follows the records S2-fixed-trial-limit §1, §3, §4 (constants dropped), its addendum, and S2-qualitative-limit §1–5. PD-T547 (certified lower bound) and Appendix C are not yet written.
- 2026-11-13 (handoff 03, MZ-CC tasks 1.1–1.6):
  - Prop `prop:edge-certified` (PD-T547) is in, verbatim and one-sided, with Appendix C: Lemma `lem:closed-form` (PD-T548) with a condensed proof, the finite reduction, the scalar enclosures, results and code.
  - Lemma `lem:U-exact` (PD-T019 formulas) has moved to §4.1. It adds the q_N<1/3 for N≥57 consequence of PD-T?mz-paper-claude-01 (a), with its proof. Prop `prop:counterexample` (§8) keeps the N=512 certificate.
  - Cor `cor:interp-norm` (PD-T?mz-paper-claude-01 (d)) is new. Cor `cor:endpoint` now states PD-T527 verbatim plus parts (a)(b) of the provisional claim, and replaces the old weaker corollary, which is implied. `rem:rate` is rewritten: no rate usable at computable N; decimal of Λ_edge open.
  - §8 uses B=min{1+ρ,5/3} (part (c)).
  - §9 is rewritten. Table 1 stays MEASURED, with a (log N)²λ_− column computed from the tabulated values. The J=512 Galerkin proxy (PD-T532) is labelled as a measurement. The old open sentences on PD-T020 and the PD-T027 limit are deleted, because both are now theorems. Open: decimal of Λ_edge, usable rates, operator identification.
  - In-heading `\id{}` labels are moved to TeX comments (`% IDs: …`).
