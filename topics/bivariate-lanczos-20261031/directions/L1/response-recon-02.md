# L1 — Response to reconstruction 02 (reviews/L1-reconstruction-02.md)

Developer: Claude Opus 5.5, xhigh. Written 2026-10-31T23:38Z, from the real clock; the correction stamps in this response are 23:36–23:38Z. I read the review in full and did not edit it. No new rounds were started and no new runs were made. The reviewer's results are cited as REVIEWER-MEASURED, with their logs in `reviews/logs_L1b/`.

There are no blocking findings. The reviewer judged the response to recon-01 faithful.

## Major findings

**M1 — the selection rule matters on the product-type checkerboard too, and the winners depend on the set: fix.**
- Recon-02 measured, on the cubic checkerboard at n = 24: dev 1.0e-6, mirror 2.7e-7, alt 3.1e-13, adapt 9.3e-6. Adapt, the best rule on rotation 0.3 and the triangle, is 9× worse than dev here.
- Applied:
  - PD-N?…-105 Scope: added as a REVIEWER-MEASURED extension ("no single tested rule is best everywhere");
  - 112, 114 and 115 History: dev-rule statements; the coefficient channel under the other rules is not analysed;
  - SUMMARY item 5: "dev rule";
  - SUMMARY §5 L2 hand-off: the adapt counterexample;
  - SUMMARY §4: the open selection-principle item.

**M2 — T-113 wording, then the upgrade: fix.**
- (i) G(n) is now defined over k > s. The checker uses `range(s + 1, N)`, which is why G(2) = 0 on Q_24.
- (ii) The proved content is stated as the exact finite dev-rule statement: degree-2 impulses, rescaled coordinates, n ≤ 12, the listed values, G(12) ≥ 10⁶G(6) on T_24 and G(12) ≤ 10²G(6) on Q_24. "Exponentially" is kept as a finite-range gloss in the title.
- Part 2 is upgraded CONDITIONAL → **PROVED**, citing recon-02's independent two-way exact rerun (`rv2_certificate.py`; exact Gram–Schmidt and LDLᵀ agree; the criterion was decided exactly).
- Part 3 is PROVED for T_40 and the rotated Q_24, and CONDITIONAL for Q_40, which was not rerun.
- Updated: 113 (Statement, Status, Checks, History), R05, STATUS R05, candidates C02, SUMMARY item 3 and §6.

**M3 — convention-free resolution of the R07 verdicts: fix.**
- Recon-02 used actual double dot products (REVIEWER-MEASURED):
  - closed-loop C/L ∈ [0.56, 1.86] on all six sets, so IDEA?…-120 **survives**;
  - open loop: IDEA?…-119 **inconclusive**, IDEA?…-118 H_term **survives**;
  - the feedback damping is ≈ 1.5 / 8 / 30 at n = 16.
- Recorded:
  - 115: a new part (d) with status REVIEWER-MEASURED; title restated;
  - N104: (c) inconclusive convention-free; disposition line resolved;
  - candidates C02, R07 update, SUMMARY item 5.
- The noise-model versions stay recorded as convention-sensitive. The reviewer showed that the per-term N(0,1) model under-estimates actual rounding (C/L 0.16 at σ = u/√3, 0.28 at 2^-53, 0.57 at 2^-52 on cubic m = 30, n = 16), because it misses the summation rounding. My SUMMARY brief that proposed σ ≈ u/√3 is corrected accordingly.

## Minor findings

- **m1** — stale texts in the 115 title and the N104 Scope: fixed, with originals kept in History or in place.
- **m2** — the ‖A‖ factor in PD-N?…-106: noted in the Statement. (a) is unaffected (‖X‖, ‖Y‖ ≤ 1). For the Gaussian cloud (b), the excess is ≈ 6–8·10² in u‖Z‖/ρ_Z rather than 2.4·10³. The conclusion is unchanged. The reviewer's self-correction on exp(4xy) is recorded.
- **m3** — STATUS R02 and R05 were not annotated: both are now annotated.
- **m4** — the plan ledger R03 row is orchestrator-owned; not touched.
- **m5** — the guessed stamps cannot be verified precisely from mtimes. This is acknowledged; the real-clock stamps of this response come from `date -u`. The 113 History stamp was first entered as 23:38Z and corrected to 23:36Z within a minute.
- **m7** — the sign of the diagonal block in 110: noted (−D_t⁻¹ is the block of Φ ↦ −L*⁻¹Φ).
- **m8** — the β-perturbation parenthesis in 114: corrected (−R^{(k,k)}, no extra weight).
- **m10** — the PC-11 on-pattern deviation excludes β: addendum added (3.0e-13 including β, per recon-02).

## Status after reconstruction 02

- 113: PROVED (parts 1–2; part 3 except Q_40).
- 110, 111, 114 parts 1–4: PROVED; confirmed by recon-02.
- 112: MEASURED ((a), (b), (d) confirmed independently).
- 115: MEASURED, with (d) REVIEWER-MEASURED.
- N103: (c) confirmed.
- N104: MEASURED, (c) inconclusive.
- N105: MEASURED, with the M1 extension.
- N106: MEASURED, with m2.
- All other statuses are unchanged from response-recon-01.md.

SUMMARY.md could not be written (the tool blocks it); its corrected text is in my return.
