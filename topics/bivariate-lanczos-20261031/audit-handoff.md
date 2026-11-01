# Audit handoff to Codex — bivariate-lanczos-20261031

- Requested auditor: Codex `gpt-6-astra`, effort **xhigh** (novel mechanisms and negative claims; AGENTS.md/WORKFLOW.md allocation). Developer: Claude. AC alone merges.
- Branch `claude/bivariate-lanczos-20261031`. Rules SHA `d36722823441dc40c6e19d69a174459348dd309c`. Base `origin/main` at start `d36722823441dc40c6e19d69a174459348dd309c`; main has since advanced (charter PR #2 merged at `08fafe6`) and is **not yet merged** into this branch (deferred to PR preparation per AC). The branch contains the shared batch ledger commit `48f7a02` propagated by the Codex MZ orchestrator.
- **Candidate:** the commit that adds this file (the Stage AUDIT commit; its SHA is recorded in LOG.md and the reply to AC). File hashes of every theory file at that commit are listed below; any later divergence needs an impact check.

## Scope and what to read

1. Rules: AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md.
2. Topic: [LOG.md](LOG.md), [plan.md](plan.md) (frozen first questions L1-Q1, L4-Q1, L2-Q1, L3-Q1, L5-Q1; History with Step 0 corrections, AC messages and scope decisions), [progress.md](progress.md), [report.md](report.md) (ranked survivors and briefs).
3. Novelty/negative scope: full `state/IDEAS.md` (Step 0 seed — final IDEA entries are still in the direction `candidates.md` files and enter the registry at PR preparation), each `directions/L*/candidates.md`, `tracks/bivariate-lanczos/NEGATIVE_RESULTS.md` (to be filled at PR preparation from the PD-N theory files).
4. Per direction: `directions/L1/` (R01–R07, SUMMARY, response-recon-01/02), `directions/L2/` (R01–R03, SUMMARY, response-recon-01), `directions/L3/` (R01–R06, SUMMARY, response-recon-01/02), `directions/L5/` (R01–R03, response-recon-01). L4 is inside L1.
5. Independent Claude checks (supplementary, not a substitute for this audit): `reviews/L1-reconstruction-01.md`, `-02.md`, `L1-prior-art-01.md`, `L3-reconstruction-01.md`, `-02.md`, `L3-prior-art-01.md`, `L5-reconstruction-01.md`, `L2-reconstruction-01.md`, `L2-prior-art-01.md`; input reproduction `repro/REPRO.md`.
6. Literature: `literature/INDEX.md`, `CORPUS.md`, `records/` (Step 0 notes baseline LIT?…-001–077 UNVERIFIED; fulltext records 101–162; online pass 201–236 via WebFetch digests; BPS 2010 301–303). Shared keys with the merged charter (e.g. huhtanen-larsen-bit-2002, bartels-jezioranski-1985, egk-1991, xu-siam-1994, harris-simanek-2021, humet-2019, sauer-2007, degani-schiff-tannor-2005, xu-pitman-1994, mourrain-2017) will be reconciled into one record each at PR preparation.

## Claims requested for audit (developer statuses)

Priority order (see report.md §1):
1. L3 Padua obstruction: PD-N?…-N301 (n = 3), PD-T?…-313 and PD-N?…-N303 (n ≥ 4) — PROVED; computer-assisted parts with exact arithmetic and independent reruns (code/L3/exact_certificates.py; reviewer checkers in code/review_L3, review_L3b).
2. L3 framework: -301, -302, -303, -304, -305, -306, -309, -310, -312, -314 PROVED; -N302, -N304, -N306 PROVED negatives; -307, -311, -315, -N305, -N307, -N308 MEASURED; -300 OPEN target; scope decision on L3-Q1 readings (L0/L/E/G).
3. L1/L4: -101–-104, -106, -108, -110, -111, -113, -114 (1–4), -401 PROVED; -105 PROVED with IDEALIZED part; -107, -109, -112, -114(5), -115 MEASURED; PD-N -101(a), -102–-106 MEASURED; REJECTED: refuted — the R03 "selection, not truncation" consequence (PD-N -105) and the support-shape classifier (PD-N -106).
4. L2: -201, -202 PROVED; -205 PROVED under (C) + acyclicity; -203, -204, -206, -207 MEASURED; PD-N -201 (span drift) – -207 MEASURED.
5. L5: -501, -505 PROVED; -502, -503 MEASURED; PD-N -506, -507, -508 MEASURED.

Particular audit questions: (i) whether the L3 exact-representation reading (E) is an acceptable answer to the frozen L3-Q1 and that reading (G) is correctly OPEN; (ii) the computer-assisted proof requirements for N301/313/N303/310/113 (finite reduction, exact arithmetic, committed checker, independent rerun); (iii) the span-drift claim PD-N?…-201 and its relation to published multivariate V+A (identification UNVERIFIED); (iv) disclosed post-hoc kill criteria (L1 R01 decision rule, IDEA-106/-107, S1/S2, IDEA-115/-119/-120; L2 drift kill; L3 M3) and the u = 2⁻⁵² vs 2⁻⁵³ convention; (v) split/status rules across mixed theory files; (vi) PD-N eligibility under the L5 rule.

## Reproduction

Every completed run lists its command, seeds and log path in its round record (`directions/L*/R*.md` §Runs/Checks) and theory file §Checks. Environment: Python 3.13.18, numpy 2.5.3, scipy 1.18.1, sympy/mpmath as installed; 2-core / 7 GB cloud container. Logs are committed under `directions/*/logs/`, `repro/logs/`, `reviews/logs_*` (each < 1 MB; total committed generated output < 5 MB — verify). Compiled `.so` builds are untracked (sources committed). Runs not executed are under "Runs needed" (LOG.md and records), mostly M = 10⁵–10⁶ runs for AC's servers syvert0/1/2.

## Known open items and limitations

Greenbaum 1989 unread (pending-reference; interval-width accounts conflict); Delgado–Geronimo–Iliev–Marcellán 2006 and Cichoń–Stochel–Szafraniec 2005 unread (relevant to L3-301); Zhu–Nakatsukasa Appendix B and Simon LAA 61 unread (relevant to L2); many literature statements are UNVERIFIED digests; one seed per shape in several measured tables; subagent effort levels are as requested, not runtime-confirmed; some developer timestamps were estimates (annotated); RESULTS.md on AC's machine is subject to concurrent writes by other sessions.

## Theory-file hashes at the candidate commit

| sha256 | file |
|---|---|
| 175aaad3fce7cfde64c7f9644482d8eb2a24c7500b17b6a3150e7bbfb61ad9aa | `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-300-l3q1-backward-interpretation-target.md` |
| c0f84c2dab322e8f5c61a10bf8a0df45c291781f623bc0238f58f6366e52af2d | `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-301-truncated-favard-sections.md` |
| b2ba05315a0c3f5afab9cae52fa422f0163cb292a5dc7d2abbb63766e0b7f6cd | `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-302-backward-reduction-moment-cone.md` |
| 8207b3b87625bb692aa9da2da0efc0a14cee5cd1fe3ef02444cf798b28768a5a | `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-303-moment-cone-rate-theorem.md` |
| 8bfa07da8fb255dbb4b4a89b85b3206518755d366a60b734abebb8cc9d2e4c82 | `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-304-square-case-commutator-bounds.md` |
| 52f5ddda0bad49b102da6637a6b58428a881c0be2eb2863ca7cbf8682cd9ce48 | `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-305-three-node-square-case-sqrt-rate.md` |
| 52af1c9ddced7a788f3dd27448e156d6b8a5df5d82768c7bb2c7494aca885beb | `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-306-padua-n2-sqrt-rate.md` |
| e810d77b5f494b72ecb173d3607d9031d89bfe531623f047198cae6f35594f98 | `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-307-square-case-hessian-condition-measurements.md` |
| 59be05e16c06d18efd37475849449fa33e6999c976a9d5e3275329512ae5cc38 | `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-308-compression-model-no-obstruction.md` |
| 373d7d198a7d02d2ea119bc1d09080c53e085a1f88804dbb093ce5bcb4360696 | `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-309-square-case-quadratic-generator-form.md` |
| 0aad172c8b57c10901e16d08d3ba0b4bd5ff8eec4087fe10d269945bc7c350d9 | `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-310-equispaced-checkerboard-condition-H.md` |
| 0eeeea78604fbf201cc40c33bac1d0011b76e1e5edf9e96afd3c77c0e5dbcd47 | `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-311-equispaced-certificate-margins.md` |
| 80f59ddd11542339832392bd331ae0c5ec57811ae337e2b12303a81dcfdc394d | `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-312-padua-interior-turan-lemma.md` |
| 730b06228c9eff676f1d462a29a4b39de0169b5fb3790196d4e42b461b51842e | `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-313-padua-turan-certificate-all-n.md` |
| 3415a9ef3ea42a13881c8fabaf19e4af517bdfb97998c7788cc055280c9fb58f | `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-314-computed-data-consistency-symmetry.md` |
| c6aaee7dd79d453944460bc918fac5addf7db3a641ab2bb4195979ad63117db5 | `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-315-consistency-defect-measurements.md` |
| 50e455fcdcf88601d68537fe95da4da8666fcb00200692fa3053f52334509a21 | `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-N301-padua-n3-exact-backward-obstruction.md` |
| 0785d7797707748bef7590af7eeb7b523a1112d9d1cd511c29e1996a70441597 | `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-N302-square-case-linear-rate-refuted.md` |
| ed0e9a9d9dbfb5570427f46717481b4e9c40f68481d589e56a7415fe2bedbbab | `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-N303-padua-all-n-exact-backward-obstruction.md` |
| fd1e3d660fca62ae0b7eca8cffd46a3989a2ee2b0c3088b8e9324315a19bfe84 | `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-N304-compression-model-insufficient.md` |
| 37eb32350fbbe2ff30114d30c763a2c86f927f89697f36b220960a9af72e48b4 | `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-N305-closed-form-C1-fails.md` |
| 9228d8256b375becfea5e048971984c021114786f9b9f137f724582518addf6d | `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-N306-H-not-decided-by-count.md` |
| 544d6515ca705860ed626ed619067d606fd6a5ad398b75d05a849b5a9ed1669b | `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-N307-consistency-survives-loss-refuted.md` |
| 6f929ff78112f5304c73636fe3f876f7f42c4aef160f6e9a2fd86ddf38f855b8 | `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-N308-weight-only-greenbaum-fit-refuted.md` |
| 6e4ef4cdbbc63395b8ad181e464611a01bbc5ddeedb258e5132e3da151dda633 | `tracks/bivariate-lanczos/theory/checkerboard-and-near-product-measurements.md` |
| aecf9975248b07f5d05d1c579b3f42201d9e3252ffc1e5daca123972c37fe0fd | `tracks/bivariate-lanczos/theory/closed-loop-dot-product-rounding-carries-coefficient-channel.md` |
| 4737a7cc984d688950fdb1cc1865227dd0a44cb03511d3c927d43ae7ef529b68 | `tracks/bivariate-lanczos/theory/commutator-shadow-recursion-and-span-drift-bound.md` |
| 33bc73adb97f5c720209d1a07ad8b89ac87b342999d5d5d0c436dc846f0f12b3 | `tracks/bivariate-lanczos/theory/coupled-section-residuals-general-selection.md` |
| 4d7f17ff8cf75726df97a7c65ad84fb3f455911cb634bd04c0e08ce2533062e7 | `tracks/bivariate-lanczos/theory/exact-certificate-propagator-growth-triangle.md` |
| b9b984deee3dfa44ba27ab6e7c39ef7c43b98b2b5e678d20c4b6d4d2dd90eaa9 | `tracks/bivariate-lanczos/theory/exact-omega-recurrence-window.md` |
| d6240b158ad9850bbe36fc63d1d00356989cda2a3de2f3fc6bbc0e1a23728cc3 | `tracks/bivariate-lanczos/theory/exact-window-dots-do-not-remove-coefficient-channel.md` |
| d47d7de4e9ef3ec0afbb37a6e6ac888296a0d5f4aa4d4b2368591232cfc248b0 | `tracks/bivariate-lanczos/theory/fifo-threshold-deferral-failure.md` |
| 9dbeb5f4d94745dd02fbc8e51de968a6ff1b3011f84d5766df6141c12a23e692 | `tracks/bivariate-lanczos/theory/first-order-coefficient-channel-gains-product-type.md` |
| 13fd2f50b813b8cbad43d26df95cebd473992dd76c83da07cd4ad31271f68735 | `tracks/bivariate-lanczos/theory/fp-local-relations-window-recurrence.md` |
| a2707434f266388b8d69310b71ef1921d083b8e2e11051bc8a2653bba9ae589e | `tracks/bivariate-lanczos/theory/full-operator-paige-identity-growing-blocks.md` |
| 174b5c238b45f3f1e6b48ead39f7fdffdfd08c72be0ed0c1f61d74d04f761a6d | `tracks/bivariate-lanczos/theory/givens-deficit-slopes-measured.md` |
| 99808ffefad8a8dfa346b9f9dbcdb99a3de0448e4f18e0a87acdfcd08395d295 | `tracks/bivariate-lanczos/theory/givens-updating-rotation-count-backward-bound.md` |
| 47cd4f5b518ecba4dcf7a736293acf5f37dba31b5a6127b008fd5134df3aa1f5 | `tracks/bivariate-lanczos/theory/hl-simax-windowed-complex-recurrence-instability.md` |
| 54bf537b5178823af4dbea7ca546999588bc6124404a4d7f3ac269358014749d | `tracks/bivariate-lanczos/theory/l4-band-krylov-obstruction.md` |
| 2b1842e1c364957d45225b29754b2b3a9895b4eafe6a85b5ecb8c541693eb955 | `tracks/bivariate-lanczos/theory/largest-redundant-pivot-degradation.md` |
| dae0bf50b57fd6194079dc2545e64359ac316093dd1fbc2d7e0603363f59db73 | `tracks/bivariate-lanczos/theory/loss-regimes-node-propagator-measured.md` |
| 255db03e39e3c3a53e571ce3af841605804ffab56b88c618ec2462b836f754fc | `tracks/bivariate-lanczos/theory/magnitude-threshold-pivot-rules-failure.md` |
| 8fefaafadafecfb42f7f9db960fc10543ea0d1bba40057670d4ab2a85f798030 | `tracks/bivariate-lanczos/theory/moment-matching-product-factorization-checkerboards.md` |
| 7dd02ce2455ca553b8196ee771cad25f2a0f2e57f9e3c7d3c439dc30115cff29 | `tracks/bivariate-lanczos/theory/near-product-transfer-perturbation-bound.md` |
| 0c618867a1e2679e495e133a7326594e3cf9bb8208afad730e1bea94b1816023 | `tracks/bivariate-lanczos/theory/node-row-representation-and-commutator-residual.md` |
| 8decf8dafb97611b88a296ad0344f09e33225f7a0a26afa3cf493aa0096e6544 | `tracks/bivariate-lanczos/theory/non-product-amplification-is-a-priori-measured.md` |
| 90d8f7c4871f262a491306fb258a1cbf8e7a7fda1c4b3d5a72b82610ee673e63 | `tracks/bivariate-lanczos/theory/omega-estimate-componentwise-in-window-sources-fail.md` |
| d903f006fe8d382c3ebc3956c780abea5a702f1d506809327d919939d32a3d5a | `tracks/bivariate-lanczos/theory/omega-estimate-tracks-loss-measured.md` |
| 67126ec06209f896247ee850b8beabbd5f73bafa146681e79bcdbf0361f37c05 | `tracks/bivariate-lanczos/theory/one-pass-window-semi-orthogonality-insufficient-for-F-section.md` |
| 50190e070041cc3dd70641750b88bfac98a6fb45e24339e3ffd9d9b7831766b1 | `tracks/bivariate-lanczos/theory/one-relation-selections-do-not-keep-spans-near-Sn.md` |
| c6a51ae6b6862b1b5a4c81a07070ea0d21246e78e1fe4a09061d8d5cf1396bf8 | `tracks/bivariate-lanczos/theory/open-loop-coefficient-noise-estimates-fail.md` |
| 7fa040e8a025cb714e7ff79389b44b0f0cdd33e9568908e85a4679dd9af22b3d | `tracks/bivariate-lanczos/theory/prefix-unisolvence-order-statistics-measured.md` |
| 04433dc78c4133411a14e01b72cf57f6b37240970d7a9663b9b468a9f074a400 | `tracks/bivariate-lanczos/theory/pro2d-j-fails-on-clustered-checkerboard.md` |
| 37abe6b9e6cf0dc1a53f00f45d9015763e15ba5f6714fec4bfd8632832441439 | `tracks/bivariate-lanczos/theory/pro2d-rounding-only-trigger-fails.md` |
| ee3b4a4aa9c9e503dde06a1761fc46309b49db8043733cc7188176761c0584f6 | `tracks/bivariate-lanczos/theory/pro2d-strategy-and-cost-measured.md` |
| b304e439b9aa069af3865c7efe4e4ee6209cf03227ff1dbd74f16bf39e72a2f3 | `tracks/bivariate-lanczos/theory/product-measure-propagator-factorization.md` |
| 66623728ff6f85a269cd08032722248e016be8a470fd27f00ce8a8565169fee5 | `tracks/bivariate-lanczos/theory/r04-failed-scaling-and-predictor-hypotheses.md` |
| 973e46ceb5a5651f96cda4f874ce47304ceae9dc14cf957054f9832d577a6335 | `tracks/bivariate-lanczos/theory/reorthogonalization-does-not-restore-graded-spaces.md` |
| 5388763d07fb877c4a9f04b52621a536817a2a27b802ea432f511aa19f5b27b3 | `tracks/bivariate-lanczos/theory/ritz-residual-governance-fails-off-product-supports.md` |
| 4f5a695279c3a17cebcbc6dd21c314e50c2f78303338da209feeef6429694cbb | `tracks/bivariate-lanczos/theory/section-accuracy-and-two-pass-window-measured.md` |
| eb2ec6db92211e1f95dd44ea17c35fde9514368bea0e991bc09da706472cd397 | `tracks/bivariate-lanczos/theory/selection-and-truncation-both-matter-measured.md` |
| 8f79fc2a85b22b4b46c7f0710a0dee50ece83ea8c6b6f2a86ed01449cde4c4db | `tracks/bivariate-lanczos/theory/selection-rules-and-span-drift-measured.md` |
| e3613b227e577d3d69c878dd44fe608cf205abd92bff67dd97829d8dd86b981a | `tracks/bivariate-lanczos/theory/semi-orthogonality-implies-accurate-F-section.md` |
| 0a689dc93140d3d6bc0a5181f8f2fdabaa0a2fc83a2df7f6b84ca4e8f0e0017a | `tracks/bivariate-lanczos/theory/support-shape-does-not-classify-loss-regime.md` |
| 74e3779774bd193314501e58724a4e608001038e067ef873a519bddbfc11aa44 | `tracks/bivariate-lanczos/theory/unisolvent-prefix-extension-lemma.md` |
| f5110d68c4894fcbfef3718ecf677eafcc2a41ebe79cb3ef35c19b14a1be8f99 | `tracks/bivariate-lanczos/theory/window-coefficient-pattern-exact.md` |
| 75c3ea0e34de612cfb17362c603a56ea4419323742538d7275a6c33026c77ecd | `tracks/bivariate-lanczos/theory/window-recurrence-row-selection-of-jacobi-pencil.md` |
