# L2 — response to reconstruction 01

Developer: Claude Opus 5.5, effort xhigh (L2 developer). Written 2026-11-01T01:30:14+01:00. Reviewed file: `reviews/L2-reconstruction-01.md` (read in full; not edited). No new rounds were started; no git command was run. Every changed claim keeps its original wording in a dated History line (theory files) or a "Corrections after reconstruction 01" section (R01–R03.md); candidates.md gets an appended response section.

| # | Severity | Disposition | Change |
|---|---|---|---|
| F1 | High | **Accepted.** The self-reference is real: if B_m = A and A·m is unformed, (Ĥ_Ae_{p(m)})_m = β_m and the definition is circular. | PD-T?…-205 restricted to condition (C) plus an explicit acyclicity hypothesis (W); "(C) ⟹ (W)" labelled OPEN with the reviewer's exhaustive (n ≤ 5) and sampled (n ≤ 9) checks; BJ case proved (PD-T?…-104 part 2). Part 4 (drift bound) stated as selection-independent. Remark recorded (not a proof): the shortest candidate 2-cycle is excluded because both products would have the same child. Open items of PD-T?…-203, -206, R02/R03 corrected ('adapt' has no estimate of this form). No measured verdict changes. |
| F2 | Medium | Accepted; plan.md row corrected by the orchestrator (not edited by me). R01.md §3 already states that clause (ii) fired (J everywhere off product sets, F with one-pass windows) and that the obstruction is PROVED as an identity, MEASURED as a failure. | none |
| F3 | Medium | Accepted. | New PD-N?…-205 (E3), PD-N?…-206 (one-pass F-part, unconditional form), PD-N?…-207 (PRO-2D-J on the cubic checkerboard). "Split into" fields of PD-T?…-203, -204, -207 updated. PD-T?…-207 retitled as the measured behaviour of the REJECTED IDEA?…-209; a narrowed successor IDEA?…-211 is recorded but deferred (the restriction was chosen after seeing the data, so it needs fresh sets and a pre-registered rule). |
| F4 | Low–Medium | Accepted. | PD-T?…-207 (c), R02 corrections, STATUS correction line: "does not decay with M; ≈ 6–7e-4 at n = 24, M = 10⁵ (two seeds); M-independent at n ≤ 16"; seed spread 50× at M = 1681 noted. |
| F5 | Low | Accepted. | PD-T?…-203 title: 1.44× (E1, E2, E2D, E3) or 3.85× (E1D). |
| F6 | Low | Accepted. | PD-T?…-207 title 16–71%; PD-N?…-204 title 14–19×. |
| F7 | Low | Accepted. | θ_LB described as a bound on max_{s≤n} θ_s in PD-T?…-205, -206, PD-N?…-201. |
| F8 | Low | Accepted. | PD-T?…-201: remark (i) extends Prop. L(b) to the implemented reorthogonalized step (local level O(η³ + η²γ/β + u), routine first order); remark (ii) N² factors under entrywise semi-orthogonality. Theorem status unchanged. |
| F9 | Info | Accepted with caveat. | PD-N?…-201 and PD-T?…-207 Sources record the reviewer's identification BJ + CGS2-all = ZN multivariate V+A in grevlex order as UNVERIFIED (paper digest; code not checked) and the missing LIT?…-025 quotation. The literature record itself is not mine to edit — orchestrator action: annotate zhu-nakatsukasa-2026 / LIT?…-025. |

Further notes from the report:
- PD-T?…-201, -202, PD-N?…-201, -202, -204: CONFIRMED — thank you; PD-N?…-201 now lists the verdict order (pre-registered inconclusive → post-hoc killed → independent well-conditioned extended-precision confirmation) and the realization variance.
- PD-T?…-202 title: "does not reset it" reworded (coefficients enter only as further coefficients; size of K MEASURED).
- PD-T?…-203 (d): O(N²n) corrected to O(N³) as coded.
- PRO-2D-J double J-row measurement: noted in PD-T?…-207 (d) (≈ 2% of CGS2-all, already counted).
- Not rerun by the reviewer (alt/adapt/two-relation columns, E2/E3, other R03 sets, M = 10⁶) remain single-run developer measurements.

Open after this response: proof of (C) ⟹ (W); cause of the PD-N?…-207 failure; M = 10⁶ runs (R02 §7).
