# Sharp MZ constants via limiting operators (PD-T020, PD-T027, PD-T381): log

- Branch: `codex/padua-mz-sharp-constants-20261106` · Base: main `76ba421` · Developer: Codex · Auditor: Claude (Opus 5.5 xhigh)
- Stage: WORK · Next: `Codex (gpt-6-astra high): Continue codex/padua-mz-sharp-constants-20261106.` · Open handoff: [handoffs/01-work.md](handoffs/01-work.md)
- Reserved final-ID ranges: none. Reserve when first needed (PR #29 rules).
- Claims: none yet.

## 2026-11-06 — Claude, claude-opus-5-5 (configured; effort not exposed) — topic setup

- AC asked for one more substantial reasoning round alongside the argmax bridge. Claude suggested sharp MZ constants via limiting operators. AC: "yes, open sharp-constants codex topic under the suggested rules".
- Directions:
  - S1: the PD-T020 Mellin/Carleman mesoscopic model, in the Widom–Wilf Hilbert-matrix style;
  - S2: the PD-T027 microscopic Wiener–Hopf / Toeplitz-plus-Hankel endpoint limit, with a uniform B < 2;
  - S3: the PD-T381 2-D corner Mellin model, per parity;
  - S4: high-precision numerics.
- Coordinator gpt-6-astra high; up to 15 rounds per direction, in parallel.
- Claude's earlier chat remark compared the measured 2-D slope −0.0915 with 1/9. That was wrong: 1/9 belongs to the unnormalized Q(p²)/log m. The proved normalized constant is c₋ ≈ 0.0296 (PD-T379), and handoff 01 states the correct comparison.
- Rules read at `76ba421`. Branch created from main `76ba421`. Only this LOG, handoff 01 and the results stub were added. No computation was run and no claim made.

## Runs needed

- K0–K5 and S1–S4 as in handoff 01.


## 2026-11-06 — Codex continuation setup and K0

- Rules read at `2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861`; current main/base `76ba4214b100c86a44941f5e9a662ce9ce48efb8` is already the topic parent. No base merge needed. Setup plan/gates published in6e928d9 before first run. Draft PR31 opened.
- Shell Git fetch failed connecting to configured proxy8080. Connector reads work. The pinned source corpus `/workspace/sharp-work` preserves paths; [input inventory](input-snapshot.json) verifies79 files by Git blob/SHA256. The older checkout is untouched. Publication uses Git data APIs and expected-head lease.
- Coordinator requested gpt-6-astra high; serving metadata unexposed. S4 development requested gpt-6.1-sol medium; S1–S3 requested gpt-6.1-sol xhigh, disjoint paths. A distinct gpt-6-astra high checker is rerunning K0. Required Claude audit remains PENDING.
- K0 developer replay PASS under the explicit finite-norm interpretation: six CC cases N40–1280, maximum relative difference3.997e-15; Padua minima m800/1000 bit-identical to pinned PD-T300 values. Carrier finite norm formula agrees with independently assembled composite angular quadrature within3.31e-16 throughm4096; finite-to-limit offsets remain nonzero and decrease. These are MEASURED, not new spectral proofs.
- Original K0's request for matching a carrier norm limit at1e-10 is ill-posed at a finite degree without an error allowance. We preserve that criterion and record a dated clarification in gates.md: compare exact finite norm to a separate quadrature at1e-10, then measure finite-to-limit discrepancy separately. The first global x-Gauss check lost accuracy at high degree; its code/receipt are retained, its issue explained by endpoint sensitivity, and the composite angular check replaces it. No fit was performed.
- S1–S3 cleared to develop after K0 and their novelty gates. No new mechanism proposed by coordinator; gate/predecessor reading belongs in each direction's record. No final ID range reserved.

## Round S4-2 — structured CC solver and scan registration

- gpt-6.1-sol medium constructs the exact finite nodal reciprocal mass representation with projected degree-N constraint; Toeplitz/Hankel FFT products require linear storage. Both extrema agree with dense N40–1280 within4.62e-14 relative. Details and initial serialization failure are in [attempt S4](attempts/S4.md); [validation receipt](evidence/S4-structured-validation.json).
- This is routine finite-coordinate algebra, no new mechanism or limiting model; novelty gate is not needed for this implementation replay. S1–S3's novelty gates remain required before model development.
- [Scan proposal](S4-scan-proposal.json) accepted before scan, with raw values allowed and final fits held for model registration. S4 round2 progressed; no failed-progress count.

## Supplementary independent K0 replay

- Distinct gpt-6-astra high requested; serving metadata unexposed. [Independent check](independent-checks-k0.md) separately executed CC, finite carrier and Padua replays. Padua used changed seed20261106: m800 relative discrepancy2.22e-16, m1000 1.84e-14. No unresolved finding in the declared numerical replay scope. Same underlying spectral algorithms remain a limitation; no rigorous enclosure is claimed. This supplements, and does not replace, the future Claude audit.
- [Receipt](evidence/check-k0-replay.json), SHA256145b99de6a7949b3b061de5f4be9910f8c8f10f4ceb067d2a137f5a5a9002432. Gates K1–K5 still PENDING. Raw large CC scan authorized at e2652c3; no final fit authorized.

## Mathematical round1 checkpoints and raw CC scan

- S1 gpt-6.1-sol xhigh completes novelty gate, registers conditional model c=pi^4/8 on both parities, and proves the separate Volterra model norm. [Attempt S1](attempts/S1.md). Finite CC norm transfer and matching bounds remain unresolved. This prediction precedes final K1 computation/disclosure.
- S2 gpt-6.1-sol xhigh completes IDEA386's missing transition estimate and proves an analytic uniform CC upper bound5/3 using exact R=M−H+K, positive H and PD-T015. [Uniform bound](theory/S2-uniform-upper.md), [attempt S2](attempts/S2.md). Distinct Astra review underway; required Claude audit pending. Sharp upper limit remains OPEN.
- S3 gpt-6.1-sol xhigh completes novelty gate and proves a strict rational-parameter improvement of PD-T379's one-sided negative coefficient, about0.02964177, on both parities. [Theory](theory/S3-normalized-carrier-improvement.md), [attempt S3](attempts/S3.md). This is a known-family quantitative variant, not a sharp constant or a factor-three explanation.
- S4 gpt-6.1-sol medium scans42 raw CC rows throughN102401, all guards pass; no fits yet. Total55.18s, peak264800KiB. Full local receipt55192bytes is off-Git, SHA2567ce16e5c61fb82fe1fc4125bbd9570fdc7579db7aa139cd116b4807322f500f2; [short summary](evidence/S4-raw-scan-summary.json). Selective75digit N20/40 agreement1.89e-15. Local raw artifact archival is pending AC-designated cold storage; retain generating/checking code and essential short receipts.
- [Distinct Astra structured-solver check](independent-checks-S4.md) independently reconstructs exact finite algebra and separately runs both parities atN101/1281/8192/8193, with errors<=1.973e-13 to dense and<=3.031e-14 in sparse exact-moment form. No rigorous enclosures or asymptotic proof follows.
- [Literature screen](literature-screen.md) records fulltext coverage and inaccessible primary sources; use the handoff's fit as an ansatz, not an independently verified Widom–Wilf theorem. Basor–Ehrhardt1999 fulltext read and provisionally recorded; it supplies no model identification or finite-N error here.

## Decisive S1 transfer allocation

- Allocate gpt-6-astra ultra to the decisive finite-to-model error problem in S1: determine whether the exact CC reciprocal interpolation operator admits the sharp Volterra leading norm with an o(logN) operator remainder. This is the specifically authorized hard limit/error step in handoff01, not routine mathematics; require a written proof or a precise unresolved obligation. S1 model prediction is already published977c07a; final fits have not been supplied to the hard-step worker.

## K1/K2 decision and retained S1 one-sided theorem

- Exact pre-registered fit [receipt](evidence/S4-k1-fit.json) passes K1 for both parities (window intercept agreement1.185%). K2 rejects first limiting-model prediction by7.268% versus the5% threshold. S1 declines an unjustified fitted revision and stops; no threshold change or extension. Gate rejection is numerical and operational, not mathematical refutation.
- S1 had completed [one-sided theorem](theory/S1-sharp-one-sided.md) before receiving K2: limsup log²N lambda_min<=pi^4/8 on allN and each parity. Its exact parity-reflected trials, signed pole remainder and oscillatory Jacobian estimates are now submitted for independent review. It proves neither sharpness nor a limit. The separately proved Volterra lemma received a MINOR absolute-square display correction for its complex statement; no mathematical claim changed.
- The allocated hard S1 full-transfer worker was interrupted immediately when K2 arrived and remains stopped. No full-transfer proof or execution is claimed. No revised model is launched.
- [S2 deficit corollary](theory/S2-eta-deficit.md) and [uniform5/3 proof](theory/S2-uniform-upper.md) pass distinct Astra mathematical review in [independent-checks-S2.md](independent-checks-S2.md); required Claude audit remains pending.
- S2 round2 registers the exact [endpoint operator model](theory/S2-endpoint-model.md), with common-parity norm prediction, before its Galerkin calculation and K3 final extrapolation. Operator transfer remains OPEN.
