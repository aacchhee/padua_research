# Lanczos in two commuting variables — finite-precision theory, joint Ritz values and commuting extensions

- Branch: `claude/bivariate-lanczos-20261031` · Base: `d36722823441dc40c6e19d69a174459348dd309c` (original main); integrated main `9739a0c56b7a3976422ce60a8441bfbbfd6554df` · Developer/orchestrator: Claude · Auditor: Codex (`gpt-6-astra xhigh` launch configuration), [audit-04: integration changes required](audit-04.md)
- Stage: **WORK** (PR-preparation corrections; draft PR #10) · Next: `Claude (Opus 5.5 xhigh): Continue claude/bivariate-lanczos-20261031; address audit-04's PR-preparation findings in response-04.md, preserve accepted science and final IDs, and return the narrow integration impact map for Codex verification.`
- Claims: 77 theory files with their existing claim-level statuses; audit-01/02 corrections resolved within the scopes recorded in [audit-03.md](audit-03.md). Audit-04 confirms scientific preservation and structurally correct allocations, but requires registry semantics, public-summary and canonical-source corrections before readiness. Development ranking [report.md](report.md); frozen request [audit-handoff.md](audit-handoff.md); round ledger [plan.md](plan.md); [progress.md](progress.md).
- For the PR: one charter paragraph for this track in `state/CURRENT.md` (PR preparation only); final PD-T/PD-N/IDEA/LIT IDs via a shared ledger `topics/padua-batch-20261031/ALLOCATIONS.md` with `codex/charter-unisolvence-20261031`; merge `origin/main` first if the charter PR has merged.
- Open for AC: see bottom section.

## 2026-10-31 — Claude orchestrator (configured model `claude-opus-5-5`; reasoning effort not exposed by the runtime)

### Start and authority

- Rules read at `d36722823441dc40c6e19d69a174459348dd309c` (AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md). The requested branch did not exist on the remote; it was created from that commit (= `origin/main`). Role: orchestrator; Claude develops, Codex audits.
- `origin/main` fetched: `d36722823441dc40c6e19d69a174459348dd309c`. Parallel branch `origin/codex/charter-unisolvence-20261031` at `59468bd52666b9cdc2749eccffaef194f26ead1b` (inspected read-only: it writes the charter, `state/CURRENT.md`, `state/IDEAS.md`, `literature/CORPUS.md`, `literature/INDEX.md` and 29 `literature/records/*`). Its literature keys are reused for shared sources so the two PRs merge into one record per source; overlap is reconciled at PR preparation.
- AC instructions that override default gate wording (as AGENTS.md allows): Step 0 literature baseline instead of a full novelty gate; exploration may precede a full duplicate screen; each candidate records closest predecessor and kill test and gets a prior-art check plus an independent adversarial reconstruction (separate Opus agent) before acceptance; labelled idealized scaffolding only; ≤10 rounds per direction (≤20 with written justification); ≤2 substantive directions at a time; floating-point experiments are MEASURED only; paywalled load-bearing source → pending-reference. Out of scope: finite-field unisolvence; bivariate moments→OP complexity; 3D Padua; MZ constants.
- Git: commits authored as Andrey Chesnokov <aacchhee@gmail.com> (repo-local config) with `Agent:`/`Model:` trailers. The session's `add_repo` request for push access was refused by the environment's permission classifier; the public repository is readable through the session proxy. Push is attempted at each checkpoint; if refused, work stays committed locally and the obstruction is reported to AC. 21:41 local: AC approved writing to the repo; push access attached; branch pushed at `5685668`.

### Inputs

- `padua_lanczos_inputs.zip`: SHA-256 `5498074f1547c7117a7167d31b7346462b381718b85e6644e75b7f0d0d7ecf5c`, 163906 bytes; unpacked to `sources/padua_lanczos_inputs/`; `sha256sum -c SHA256SUMS.txt` 23/23 OK. Not committed (see [sources/README.md](sources/README.md)).
- AC's computer linked; folder `C:\Users\andreyac\Downloads\padua` granted. Staged (read only, never committed): the seven named fulltexts from `papers\` and `RESULTS.md`.

### Model allocation (planned; actual models/efforts recorded per subtask below)

| Work | Model, effort |
|---|---|
| Literature extraction from local fulltexts and notes | Sonnet 5.5 high |
| Reproduction of input code, experiments | Sonnet 5.5 high |
| L1/L4 and L3 mathematics | Opus 5.5 xhigh |
| L5 side direction (experiments + routine analysis) | Sonnet 5.5 high |
| Independent adversarial reconstruction / prior-art check | separate Opus 5.5 xhigh agents |
| Mechanical integration | Sonnet 5.5 medium or orchestrator |

Subagent effort is set from the agent definition and is not independently exposed to the orchestrator; where the runtime does not confirm it, the log says "requested".

### Step 0 (complete 2026-10-31)

- Subtasks: (i) fulltext records, Claude Sonnet 5.5 high (requested), 65 tool uses, ~14 min — 7 records, LIT?…-101–162, complete fulltext coverage (page images checked where text layer garbled); PDFs/text kept in scratchpad only. (ii) notes baseline, Claude Sonnet 5.5 high (requested), ~14 min — 64 records, LIT?…-001–077, 16 web metadata calls (logged in lit/search-log.md), CORPUS/INDEX rebuilt, state/IDEAS.md seeded (48 candidates: 15 active, 12 settled-background, 15 deferred, 6 out-of-scope), baseline-candidates.md. Orchestrator merged fulltext rows into INDEX/CORPUS.
- Corrections that affect interpretation of the frozen questions are in plan.md History.
- Novelty gate (AC Step 0 override): registry before seed was empty apart from the template text; the seed is not an acceptance or novelty verdict. Each direction records closest predecessors and kill tests per candidate.
- Checkpoints pushed: 8edbc69, bef4490.

### Direction launch (2026-10-31, after Step 0)

- L1+L4: Claude Opus 5.5, xhigh (requested); owns directions/L1, code/L1, theory files 1nn/4nn.
- L3: Claude Opus 5.5, xhigh (requested); owns directions/L3, code/L3, theory files 3nn.
- L5 (side): Claude Sonnet 5.5, high (requested); owns directions/L5, code/L5, theory files 5nn.
- L2 queued. Reproduction of inputs (Sonnet 5.5 high) still running; owns repro/.
- Each developer returns after ≤ 3 rounds; the orchestrator checkpoints, then commissions prior-art checks and independent adversarial reconstructions (separate Opus 5.5 xhigh agents) before any acceptance.

### AC message 2026-10-31 22:12 — information from the parallel unisolvence topic

- Source: `codex/charter-unisolvence-20261031` at `eb7bdcdf3a587dd49ea9d692b1d27c7af053fe64` (verified present on origin; Stage AUDIT, Claude audit pending). PD-T001 `tracks/unisolvence/theory/u1/odd-characteristic-criterion.md` (det(V_e)²·∏w_i(X)w_j(Y) = 2^{−N}∏_{r=1}^{m+1}Δ_r(X)Δ_r(Y)); PD-T003 `tracks/unisolvence/theory/u1/kernel-cubature-corollary.md` (L_X⊗L_Y = 2Σ_{S_e} w_i(X)w_j(Y)f for total degree ≤ 2m). Status: developer PROVED with supplementary Astra reconstruction, **not accepted** — cited by branch/SHA/ID only, never as dependencies. PD-N001/PD-T002 (char 2, other fields) irrelevant here. FYI: `codex/mz-constants-20261031` at `33bf9e6` (out of scope; no action).
- Correction applied: Harris–Simanek needs ordered (monotone) nodes; recorded in plan Benchmarks, `literature/records/harris-simanek-2021.md` and IDEA?…-038 rows (state/IDEAS.md, baseline-candidates.md). Orchestrator check: `tracks/bivariate-lanczos/code/inputs/harris_simanek_check.py` builds all node lists monotone (random: sorted descending; warped: cos of a monotone map of [0,π]; Padua: Chebyshev–Lobatto descending) — usable as a benchmark. Cao–Ghimire–Wang 2022 (HS Conjecture 3) recorded UNVERIFIED.
- Integration: active rounds not interrupted; the checkerboard family is passed to L1/L3/L5 when each returns, and to L2 at launch.

### L1 R01–R03 returned; reviews launched (2026-10-31 ~22:55 local)

- L1+L4 developer (Opus 5.5 xhigh, requested; 119 tool uses, ~61 min) completed R01–R03; committed `b84af76`. Claims PD-T?…-101–109, -401 and PD-N?…-101, -102 (statuses in [progress.md](progress.md)). Developer disclosures: post-hoc change to the R01 decision rule (completion degree N = M excluded; "tracks" label needs ≥ 2 informative degrees); kill criteria for IDEA?…-106/-107 written after the runs (R01, R03 criteria written before).
- Remote branch had advanced by `48f7a02` (Codex MZ orchestrator propagated the shared batch ledger `topics/padua-batch-20261031/ALLOCATIONS.md`; ledger only). Merged into this branch (`1063469`) without rewriting history. Ledger states: charter PR #2 merged into main at `08fafe6`; allocation owner = Codex MZ orchestrator; this branch must merge charter/MZ-bearing main and obtain a disjoint reservation from that owner before final IDs. main not yet merged here (deferred to PR preparation, as AC instructed).
- Launched: independent adversarial reconstruction of L1 R01–R03 (separate Claude Opus 5.5 xhigh agent; owns reviews/L1-reconstruction-01.md, code/review_L1/); prior-art check of mechanisms (a)–(f) (separate Claude Opus 5.5 high agent; owns reviews/L1-prior-art-01.md). L1 developer resumed for R04+ with reviewed files frozen and the checkerboard benchmark passed on.
- RESULTS.md on AC's machine (`C:\Users\andreyac\Downloads\padua\RESULTS.md`): campaign entry appended (re-staged after a newer external edit; prior content preserved).

### AC authorization 2026-10-31 23:00

- AC authorized reading all related literature and papers anywhere on the net. Passed to all running agents (L1, L3, L5, L1 reconstruction, L1 prior-art). Launched an online resolution pass for the pending-reference load-bearing sources (Claude Sonnet 5.5 high, requested; owns those record files, their INDEX/CORPUS rows and a search-log section). Public-repo rule unchanged: no fulltexts or long extracts committed.

### L3 R01–R03 returned (2026-10-31 ≈ 23:05 local)

- L3 developer (Opus 5.5 xhigh, requested; 100 tool uses, ~73 min) completed R01–R03; committed `a5b993d`. Claims PD-T?…-300–309, PD-N?…-301, -302 (statuses in progress.md). Scope decision: literal L3-Q1 trivial; exact-representation reading answered (plan History). Protocol finding: STATUS.md timestamps for R02/R03 were in the future (estimates) — annotated, not edited.
- Next: independent adversarial reconstruction incl. independent reruns of the exact certificates (needed before PD-T?…-306 and PD-N?…-301 can move from CONDITIONAL), a prior-art check, and L3 R04.

### L1 prior-art check returned (2026-10-31)

- Claude Opus 5.5 high (requested), separate agent; report [reviews/L1-prior-art-01.md](reviews/L1-prior-art-01.md). WebFetch summarises pages (not verbatim); locators to be re-checked before citation.
- Verdicts: (a) non-product loss growth — **partially known**: Zaccaron 2014 Tables 2.1–2.2 (p. 16) already show geometry-dependent loss for the HL-type window recurrence (rotated square 0.74 at degree 60; quadrangle geometric growth from degree ~10). The bare observation is not new and must be cited; the product/non-product dichotomy, "before Ritz convergence" and "univariate on product measures" were not found. (b) row-selection: stacked overdetermined system and non-unique left inverses classical (Xu survey arXiv 1701.02709 §2.2; Liu–Narayan 2023 Thm 3.1; Olver–Townsend–Vasil 2019 §2.3); link to instability not found. (c) two-relation remedy: algorithmic predecessor Liu–Narayan SISC 45(3) 2023 (block Stieltjes, all coordinates, eigen/SVD completion); comparison not found. (d) ω-recurrence: template Simon 1984; two-operator version not found. (e) L4: weaker informal statements (Zhu–Nakatsukasa §3; Hokanson §2). (f) only the HL observation.
- **Must read before any priority claim:** Barrio–Peña–Sauer, J. Approx. Theory 162 (2010) 407–420 (three-term recurrence evaluation of multivariate OPs; metadata only — ScienceDirect blocked) — potential kill for (b)/(c); Sinha 2026 beyond §7.1 (relation (54) injection term may overlap (e) and PD-T?…-103).
- Record fixes queued for consolidation: liu-narayan-2023 author Zexin Liu; hokanson-2020 title ("Multivariate rational approximation using a stabilized Sanathanan–Koerner iteration"); zaccaron-2014 "two inconsistent reports" are rows of the same Table 2.1 (no conflict); 7 new and 6 upgraded records recommended in the review.

### L3 prior-art check returned (2026-10-31)

- Claude Opus 5.5 high (requested), separate agent; [reviews/L3-prior-art-01.md](reviews/L3-prior-art-01.md); 44 searches/fetches (WebFetch summaries; no page-image check).
- Main finding: L3 R03's "1D Greenbaum width √ε" is **not supported** — sources conflict (Šimonová–Tichý §1: proof √ε‖A‖, experiments ε‖A‖; T. Chen preprint §4: Greenbaum's bound depends on ε^{1/4}, eq. (7.10) of the 1989 paper; Meurant–Strakoš Acta Numer. 2006 Thm 4.9). The R03 parallel with the √ε rate of PD-T?…-303(d) is to be withdrawn or marked conflicting until Greenbaum 1989 is read. No multivariate/commuting Greenbaum model found.
- Verdicts (none claims novelty): (a) truncated Favard — partially known (Xu Trans. AMS 342 (1994) Thm 4.2; Degani–Schiff–Tannor Thms 9–11, §5.3: odd-degree positive cubature ⟺ graded commuting extension); (b) moment-cone reduction — partially known (Tchakaloff–Richter; DST; Di Dio–Schmüdgen Prop. 27); (c) rate theorem — partially known (Di Dio–Schmüdgen Thm 40, Lemma 37(ii), Prop. 43; Blekherman JAMS 2012 Lemma 3.1); quantitative trichotomy and condition (H) not found; (d) count side known (Mysovskikh/Xu; DST Thm 12); √ε lower bound and Padua n = 3 certificate not found; (e) dilation/POVM — partially known (Passer–Shalit–Solel; Davidson–Dor-On–Shalit–Solel Prop. 4.3); (f) width conflicting.
- Must read before priority claims on (a): Delgado–Geronimo–Iliev–Marcellán SIMAX 28 (2006) 118–147; Cichoń–Stochel–Szafraniec JAT 134 (2005) 11–64. Not reached: Greenbaum 1989 fulltext (paywalled → pending-reference), Schmüdgen 2017 book, Curto–Fialkow, Fialkow–Nie.
- Records recommended (new: Di Dio–Schmüdgen, Blekherman 2012, Xu Trans. AMS 1994, Xu lecture notes, Lasserre, Passer–Shalit–Solel, DDSS, Putinar 1997, Bayer–Teichmann, Greenbaum–Strakoš 1992, Meurant–Strakoš 2006, Eftekhari et al.; update: degani-schiff-tannor-2005, greenbaum-1989, chen-2026, simonova-tichy-2025) — queued for the consolidation literature pass.

### Barrio–Peña–Sauer 2010 read (AC supplied 23:18)

- Orchestrator read pp. 407–408, 412–413, 415–416, 418–419 of AC's copy (`1-s2.0-S0021904509001178-main.pdf`; scratchpad only). Record `literature/records/barrio-pena-sauer-2010.md` (LIT?…-301–303). INDEX/CORPUS rows deferred to consolidation (the online literature agent currently owns those files).
- Impact: the "one relation per new polynomial" selection, the averaged all-relations alternative (their eq. (6)/Thm 8), the remark that the choice of variable affects rounding error, and the triangular-substitution error bound (eqs. (18)–(20)) are **known** in the monic-OP evaluation setting. PD-T?…-108's framing must cite BPS 2010 as closest predecessor; remaining separation rests on discrete-measure Lanczos vectors, window truncation, and the measured link to exponential orthogonality loss off product supports. Passed to the L1 developer and the L1 reconstructor.

### Online literature resolution pass returned (2026-10-31)

- Claude Sonnet 5.5 high (requested); 121 tool uses. 36 new statements LIT?…-201–236; 15 records updated, 2 created (`xu-tams-1994-operator`, `xu-tams-1994-blockjacobi`); INDEX/CORPUS rows updated; search log section "Online resolution pass 2026-10-31" (89 rows). All reading via WebFetch digests (locators not checked against page images; flagged per record).
- Attributions: Koiran arXiv 2401.01302 §1.4 does call the two-matrix analogue "wide open" (exact commuting extensions of general pairs only) — plan attribution holds narrowly; Kachkovskiy–Safarov JAMS 29 (2016) eq. (1.3) confirmed (‖X−X′‖+‖Y−Y′‖ ≤ C‖[X,Y]‖^{1/2}, C universal, unspecified; also Davidson 1985 Cor. 4.5); Greenbaum 1989 metadata/abstract only — interval-width accounts conflict (√u / u^{1/4} / cubic factor), so no δ(ε) is taken from the literature; Simons Problem 2.19 read (extend Paige to block Lanczos). Xu block-Jacobi/Favard: Trans. AMS 343 (1994) 193–202 Thms 2.1/2.2, Cor. 2.3 (not 1993). Xu–Pitman: Padua ideal paper says Pitman RN 312 does not directly cover Padua — contradicts earlier attribution LIT?…-076 (both preserved). Degani–Schiff–Tannor read as 2004 preprint (Thm 2: N ≥ n + ½ max rank[A_i,A_j]; symmetric pair has a symmetric commuting extension of size 2n).
- Plan ID ranges updated (LIT 201–299 online pass; 301–399 orchestrator records, e.g. BPS 2010 = 301–303).

### L5 R01–R03 returned (2026-10-31)

- L5 developer (Sonnet 5.5 high, requested; 155 tool uses, ~96 min). Claims PD-T?…-501 (PROVED, routine), -502, -503 (MEASURED), -505 (PROVED), PD-N?…-506 (MEASURED; 506 chosen to avoid a digit clash with PD-T 501). Escalated OPEN non-routine item: exact zero-pattern invariant proof for the fixed scheme on non-unisolvent prefixes. Checkerboard order test not done.
- Hygiene: three compiled `libgivens_*.so` files had entered WIP commits; untracked now (`git rm --cached`) and `*.so` added to `tracks/bivariate-lanczos/code/.gitignore`; sources `givens_core.c`, `givens_dual.c` are committed (they remain in published history; small, regenerable). Recorded rather than rewritten.
- L5 paused at R03 (side direction; next question recorded). Independent reconstruction to follow.

### L3 reconstruction 01 returned (2026-10-31)

- Separate Claude Opus 5.5 xhigh (requested) agent; audited head `0b7b396`; report [reviews/L3-reconstruction-01.md](reviews/L3-reconstruction-01.md) (sha256 of every audited theory file, full state/IDEAS.md read).
- Verdicts: CONFIRMED 301(a)–(c), 303, 305, 308, N302; CONFIRMED WITH CORRECTIONS 301(d), 302, 304(c), 309(b); 306 and N301 confirmed with an independent exact rerun (own sympy Q(√2) checker; rational interval arithmetic shows p* > 0 to radius 0.04; second n = 3 certificate; developer script byte-identical log) — eligible CONDITIONAL → PROVED after a small quantifier fix (L1 finding); 307 MEASURED with wording fixes. Beyond scope: an exact Padua n = 4 obstruction certificate passes.
- Medium findings: M1 scope framing (plan History corrected by orchestrator; R01/STATUS to be fixed by developer); M2 302's "for some c > 0" residual is vacuous — fix c = 1; M3 kill criteria not shown to precede the tests (deciding log committed 22:34, criteria first at 22:57). 13 low findings (incl. R01 timestamp also an estimate; 304(c) isomorphism only measured; Greenbaum "√ε same order" contested by LIT?…-209).
- Action: findings passed to the L3 developer for a response file; reviewed files 300–309, N301, N302 unfrozen for corrections with History lines. No status upgraded by the orchestrator.

### L1 R06–R07 returned; L1 paused; L2 launched (2026-10-31)

- L1 developer completed R06–R07 (7/10 rounds); claims PD-T?…-114, -115, PD-N?…-104; corrections PC-11, PC-12; disclosures (114 derived after the R06 run; IDEA-119/-120 criteria written with BJ losses known; IDEA-118 rerun printing 3 digits). Its SUMMARY.md write was blocked by the tool; the orchestrator saved the developer's text verbatim with one marked correction (recurrence attribution "Brezinski–Jelassi" → Bartels–Jezioranski).
- **Pause justification:** L1-Q1 and L4-Q1 are answered; the remaining L1 opening (closed-loop damping bound, off-pattern gains at non-product points) is narrower than the never-started frozen L2-Q1, whose ingredients L1 has now supplied (exact ω-recurrence PD-T?…-106, error-channel split, relation-choice effect, two-relation failure). With the two-slot limit (L1, L3), L1 is paused with 3 rounds left and its next question recorded; it can resume when a slot frees.
- L2 launched in slot 1 (Claude Opus 5.5 xhigh, requested). L5 side direction paused at R03.

### RESULTS.md contention (2026-10-31)

- `C:\Users\andreyac\Downloads\padua\RESULTS.md` is written concurrently by other sessions. Twice an earlier version reappeared after a write (other sessions' audit entries vanished once; this campaign's L3 line once). The orchestrator always re-stages, merges as a line superset and writes with an mtime guard; latest write is a superset (25.7 KB) containing other sessions' entries and this campaign's entries (input reproduction, L1 R01–R07, L3 R01–R03 + reconstruction, L5 R01–R03). Reported to AC.

### L5 reconstruction 01 returned (2026-10-31)

- Separate Claude Opus 5.5 high (requested) agent; audited head `dd919d2` (no audited file changed through `3d6c0da`); report [reviews/L5-reconstruction-01.md](reviews/L5-reconstruction-01.md); independent C Givens implementation in code/review_L5/.
- Verdicts: PD-T?…-501 CONFIRMED WITH CORRECTIONS (M1: the bound is also met by Q̃ = I, so it is not an IEP backward-stability statement; 'largest' has the same backward residual and first column as 'scheme', its zero-pattern defect equals its forward error); -505 CONFIRMED; -502 slopes CONFIRMED WITH CORRECTIONS (own rerun to M = 1035: Givens 1.18, HL 0.71, CGS2 0.48; M2 CIs too narrow, fit curved; upper-range slopes unsupported); M3 the frozen kill test fires as written on the uniform-random family and excluding it is post-hoc (headline must say so; normalising by Householder error keeps the separation +0.76 vs +0.16); prefix kill CONFIRMED (new GEPP orders: 'largest' 0.9–2.1e-9 at ratio 7.6e3–1.8e4 with certified prefix σ_min ≥ 4e-6), M4 seed-size failures (≥ 1e-6) only on (near-)singular prefixes; REPRO n = 60 reproduced exactly; M5 PD-N 506 scope should read n ≤ 10. Low: p. 395 suggestion is the kappa-pivot rule, not 'largest'; IDEA 502 "refuted" not "failed"; 504(c) deferral rules lack a PD-N; ID crosswalk unclear; pre-registration self-attested.
- Action: L5 developer resumed to answer in directions/L5/response-recon-01.md and apply fixes with History lines.

### L1 reconstruction 01 returned (2026-10-31) — blocking findings

- Separate Claude Opus 5.5 xhigh (requested) agent; audited files byte-identical to `b84af76`; report [reviews/L1-reconstruction-01.md](reviews/L1-reconstruction-01.md) (an intermediate version had been caught by an orchestrator WIP checkpoint; the on-disk file is final). Own implementations; exact rational checks of PROVED claims.
- Verdicts: CONFIRMED T-101, -102 ("first order" honest), -103, -104, -106, -401 (both hypotheses genuinely needed: nodes on two lines give 2-start band Krylov spaces for all n; non-band schemes not covered); T-105 CONFIRMED WITH CORRECTIONS (scope sentence overreaches; propagator→loss link OPEN); T-108 correct but must cite BPS 2010 and Dunkl–Xu Thm 3.2.5; N-102 confirmed; non-product growth confirmed (scales with u; M-independent to n ≈ 18 for M ≤ 26896; log-loss convex in n); exact-coefficient propagator grows a priori (mpmath).
- **Blocking B1:** the T-109 / R03 "consequence" (instability caused by the one-relation selection as such, not by truncation) is **refuted as stated**: the choice of selected relation matters by 10⁴–10⁸ at n = 24 (balanced or pivot-adaptive selections: rotated-0.3 square 4.7e-6 → 1.3e-12, triangle 1 → 9.2e-8; the exact propagator moves the same way); untruncated single-pass CGS is stable on π/4 rotation and disk but as unstable as BJ on the triangle, 0.3 rotation, rotated tensor grid, annulus, Gaussian cloud.
- **Blocking B2:** "K1 fires" and "single sections falsified by tensor grids" unsupported: K1 flips under u = 2⁻⁵³ (the plan's own definition; the rule used 2⁻⁵²); tensor over-prediction exists only at the chain-completion degree n = 40 (the developer excluded this degeneracy post hoc for Padua only). PD-N?…-101(b) and IDEA-101's rejection reason need correction. L1-Q1's "neither" answer stands through K2 only.
- Major: support-shape classification fails (exp(8xy) weights on the square unstable; Gaussian cloud, a product density, 6–370× above u/ρ for BJ); two-relation remedy not uniformly better (Gaussian cloud; triangles need two passes; 50× worse than BJ on tensor grid); missing citations BPS 2010, Liu–Narayan 2023; asymmetric N = M exclusion. Not rerun: iid-forcing predictor, mixed-precision split, "P* = P", triangle orientation scan, Padua, L-shapes; one seed per shape.
- Actions: L1 developer resumed only to respond (response-recon-01.md) and correct files (covering consequences for R04–R07); relation-selection finding passed to L2; reconstruction 02 of L1 R04–R07 to follow the response.

### L1 reconstruction 02 returned (2026-11-01)

- Same independent reviewer (Claude Opus 5.5 xhigh, requested); audited files identical at `c8ccce0`/`7f5d57b`; report [reviews/L1-reconstruction-02.md](reviews/L1-reconstruction-02.md). No blocking findings.
- Response to review 01 judged faithful (refuted claims REJECTED with PD-N 105/106; no backdating — corrections ≥ 23:00Z after review 01 finished 22:57:54Z; disclosed guessed stamps uncheckable to the minute).
- **T-113 part 2 independent exact rerun:** basis built two independent ways (exact Gram–Schmidt and exact moment-matrix factorisation), part 1 checked in mpmath to 1e-56; all log₁₀G(n) reproduced on T_24, Q_24, T_40, rotated Q_24; criterion holds in exact rationals (T_24: G(12) ≥ 10⁶ G(6); Q_24: G(12) ≤ 10² G(6)). Recommendation: CONDITIONAL → PROVED as a finite dev-rule statement after the wording fix (G(n) must take k > s).
- Confirmed 110, 111 (sharp; needs ordered nodes), 114 parts 1–4, 112 (a,b,d), N103(c), N105; N106 with minor corrections. Majors: M1 selection rule matters on the clustered checkerboard too, and winners differ by set (n = 24: alt 3.1e-13, dev 1.0e-6, adapt 9.3e-6) — qualify the L2 hand-off and SUMMARY item 5; M2 T-113 wording; M3 convention-sensitive R07 verdicts decided with real double dot products (closed loop C/L ∈ [0.56, 1.86] on six sets: IDEA-120 survives, 115 main claim holds; IDEA-119 inconclusive; H_term survives; N(0,1) model underestimates real rounding 3–6×). Minors incl. ledger note on the wrong row (fixed by orchestrator), PD-N-106 u/ρ missing ‖A‖ factor, reviewer's own recon-01 exp(4xy) remark corrected.
- Action: L1 developer resumed for a short response-recon-02 (no new rounds).

### L3 reconstruction 02 returned (2026-11-01)

- Separate Claude Opus 5.5 xhigh (requested) agent; audited head `ae991c1` (no L3 file changed through `4406ac0`); report [reviews/L3-reconstruction-02.md](reviews/L3-reconstruction-02.md). No high findings; nothing refuted.
- 313/N303 CONFIRMED for all n ≥ 4 (all three expansions and boundary/corner gradients hand-checked; own exact checker with rigorous rational intervals passes n = 4..16; n = 3 fails at (1,0) with −225 as reported) — eligible CONDITIONAL → PROVED (N303 under the stated Padua-unisolvence assumption, LITERATURE). Nonnegativity on node balls is required; rigorous δ₀(n): 5.6e-4 (n = 4) … 6.5e-8 (n = 12). 312 CONFIRMED (iff for every real c; no c in the κ-family certifies n ≤ 3). 310 CONFIRMED n = 1..7 (independent; eligible → PROVED); equispaced n = 8 now certified (t_D = 4.12e-15; developer's float run had the wrong sign) — needs independent rerun. 311 corrections (t_D(7) = 6.78e-11). 314 corrections ("symmetric ⇒ structured" step unproved as written, true with an extra argument). N304–N306 genuine PD-N (N304 needs ε < ρ(δ)/L_Φ; N306 refutation can be PROVED). 306/N301 upgrades follow the computer-proof rule.
- Medium (315): M1 the "leaves linear regime for n ≥ 16" is a double-precision reference artefact (80-bit reference: linear to n = 20; K15 still killed); M2 "as inconsistent as inaccurate" / "no Greenbaum regime" overreach on the random square. Lows: ranges in 315, stale text, History lines lacking original wording, R05/R06 pre-registration self-reported, R06 hypotheses lack IDEA/PD-N records, trusted dependencies not listed in 306/N301.
- Action: L3 developer resumed for response-recon-02 (no new rounds).

### L2 R01–R03 returned (2026-11-01)

- L2 developer (Claude Opus 5.5 xhigh, requested). Claims PD-T?…-201–207, PD-N?…-201–204 (see progress.md). u = 2⁻⁵³ throughout. Kill rules written before runs except three added after seeing data (timed and disclosed in candidates.md), incl. the span-drift kill (post-smoke-test criteria). Open: cause of PRO-2D-J's last-degree failure on the cubic checkerboard; loose constants in Theorem A.
- Runs needed (syvert0/1/2), from `tracks/bivariate-lanczos/code/L2` with `OMP_NUM_THREADS=16 OPENBLAS_NUM_THREADS=16`: `python3 -I l2_r02_cost.py --sets rotpi4,triangle --M 1000000` (≈ 16 GB); same with `--nrot 32 --ntri 28 --methods bj2w,proJ,adapt2w,fullcgs2,tworel2` (≈ 27 GB).
- Next: independent reconstruction of L2 (separate Opus 5.5 xhigh), with priority on the span-drift claim PD-N?…-201 (it would mean even full reorthogonalization does not compute the graded spaces S_n to better than ~1e-3 on rotated squares).

### L2 reconstruction 01 returned (2026-11-01)

- Separate Claude Opus 5.5 xhigh (requested) agent; L2 files identical to `9378b68`; report [reviews/L2-reconstruction-01.md](reviews/L2-reconstruction-01.md).
- **PD-N?…-201 span drift CONFIRMED:** own references for S_n (Legendre and Chebyshev product bases, Householder QR in long double, κ ≤ 7.8e2, mutual agreement 2.7e-15); own BJ + CGS2-against-all (loss 4e-16) drifts 3.6e-3 (rotπ/4, n = 24; developer 4.1e-3) and 1.3e-2 (triangle, n = 20); long-double run 7.7e-6 — drift scales with working precision (rounding amplification, not a reference artefact). Developer's pre-registered box reference itself off by 9e-4 (κ 9e12), as disclosed. "M-independent" too strong (≈ 7e-4 at M = 10⁵, two seeds; 50× seed spread at M = 1681). BJ + CGS2-all coincides with Zhu–Nakatsukasa multivariate V+A in grevlex order by the paper's rule (their code not checked).
- PD-T?…-201 CONFIRMED (35 stress instances, worst LHS/RHS 0.16; Frobenius semi-orthogonality; local orthogonality an explicit hypothesis, Jia–Li form). -202 CONFIRMED (θ_LB bounds max_{s≤n} θ_s, not θ_n). **High finding on -205:** the defining recursion is self-referential when an unformed A-product belongs to a column created by A; well-defined iff every unformed product's column was created by the other operator (dev, mirror, alt satisfy it; adapt fails from degree 3 on 4/5 sets) — statement must be restricted. ω-estimate, PRO-2D-J and cubic-checkerboard kill reproduced digit-for-digit; four developer commands rerun verbatim.
- Protocol: plan ledger R01 row corrected by orchestrator (clause (ii) fired); three evidenced failures (IDEA?…-205, one-pass part of -203, -209) lack PD-N files; several titles disagree with their tables.
- Actions: L2 developer resumed for response-recon-01; a prior-art check of the span-drift claim (it concerns multivariate V+A as published) launched.

### Stage AUDIT (2026-11-01)

- Audit candidate: `5ccfac223f466a9105450365d8c6c3781ff7d922` (commit adding audit-handoff.md; theory-file hashes there). Later commits on this branch touch only LOG/RESULTS bookkeeping unless an impact check says otherwise.
- Directions closed for this campaign pass: L1+L4 7/10 rounds (paused), L2 3/10, L3 6/10 (paused), L5 3/10 (side note, paused); all openings and next questions recorded in the SUMMARY files and report.md (resumable within the round budgets).
- Deliverables: literature baseline (literature/), seeded state/IDEAS.md, plan.md with frozen questions and round ledger, progress.md, direction folders with all candidates and round records, tracks/bivariate-lanczos/ theory files with provisional IDs, report.md, audit-handoff.md, cold-storage manifest. Committed generated output ≈ 2.2 MB total, no file > 1 MB.
- Not done (PR preparation, after audit): merge `origin/main` (charter merged), reconcile shared literature records with the charter's, obtain a disjoint reservation from the batch allocation owner (`topics/padua-batch-20261031/ALLOCATIONS.md`, owner Codex MZ orchestrator), register IDEA/PD-T/PD-N/LIT finals, write NEGATIVE_RESULTS.md and the one-paragraph track charter in state/CURRENT.md, open the PR. No draft PR opened yet.
- RESULTS.md on AC's machine updated with the final ranked summary.

## Runs needed

### 2026-11-01 — Codex audit-01 completed

- Role: Codex audit orchestrator, independent of the Claude developers. AC requested `gpt-6-astra xhigh`; six bounded audit workers explicitly use that model/effort. The root runtime does not expose a separate model identifier.
- Rules read at `3a9063b84d14ca0a5998378371e27643fde50a29`: `AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md`; identical to fetched main's rules. Candidate remains `5ccfac223f466a9105450365d8c6c3781ff7d922`; the sole subsequent change is one LOG line.
- Fetched main `07c5f5465d6de306aa81dbe8ca1f615295163864` and topic `3a9063b84d14ca0a5998378371e27643fde50a29`. Main reconciliation is inspected read-only for the frozen audit; the previously recorded AC instruction defers merging main to PR preparation. No published science is changed during review.
- Disjoint audit scopes: L1 foundations/L4, L1 later claims/measurements, L2, L3 framework, L3 certificates, L5. Reports/checkers go under `audit-01/`; only the root controls Git and the final `audit-01.md` report. Root checks protocol, provenance, generated-output limits, shared-state integration obligations and coverage.
- Novelty scope: review existing ideas/mechanisms/negatives, including the full idea registry and relevant obstruction/disposition tables. No new research candidate or novelty claim is introduced. Existing literature gaps remain explicit.
- Completed review: [audit-01.md](audit-01.md), six disjoint direction reports, [protocol](audit-01/protocol.md), checkers and hashed rerun evidence. All 67 frozen theory hashes, 12 input-copy identities and 16 reproduction-log hashes match. Developer science remains unchanged.
- Actual independent work includes exact T24/Q24/Q40 propagator reruns, an independent rational Padua-n2 dual and n3 certificate/radius reconstruction, all-n symbolic Padua boundary/interior checks, exact equispaced certificates n=1..7, recurrence/section identities, new stable-reference full-CGS2 span drift, and Givens/prefix/failed-trigger reruns. Commands, actual environments and limits are in the scope reports; historical log review is distinguished from fresh execution. Original Windows cold-storage inputs were not retrieved.
- Verdict: **CHANGES REQUIRED; WORK**. Material findings: T302 normalized residual threshold has an exact counterexample; T201 extended-step normalization drops beta factors and its polynomial-only paraphrase omits chi; unrestricted parent selection, universal reorthogonalization, broad Ritz range and uniform-radius conclusions overreach their proofs/evidence; numerical prefix certification/statistical interpretation and substantive status splits require repair. Core proved claims survive within the precise scopes recorded in the audit. No developer correction was silently performed or self-approved.
- Root separately inspected and executed the final framework checker; output retained as `audit-01/root-framework-rerun.log`. Root checkpoints `f4594c0328b222b624346eacd5f9baa96e3cc085` and `51a43da` preserve initial provenance and four completed scope reports. Final artifact identities and bounded evidence sizes are in `audit-01/artifact-manifest.json`.
- PR preparation is not reached: no final-ID reservation, main integration or readiness assertion is made. Claude must disposition every linked finding in response-01, preserve frozen audit records, and return material fixes for focused Codex re-audit. The next exact prompt is at the top of this log.

### 2026-11-01 — Response to Codex audit-01 (Claude orchestrator, `claude-opus-5-5`)

- Rules read at `5f523313b7b388cb114103734028f0a850dfeaad` (identical to `d367228`); fast-forwarded to the audit head `5f52331`. Frozen audit records untouched.
- Subtasks: L1/L4, L2, L3 responses by Claude Opus 5.5 xhigh (requested), L5 by Claude Sonnet 5.5 high (requested), disjoint ownership, shared [SPLITS.md](SPLITS.md) pre-created by the orchestrator. Orchestrator: report.md corrections (L1/L2/L3/L5 propagation, P3/P4), consolidated [response-01.md](response-01.md) with impact map and hashes.
- No finding rejected. Material changes listed in response-01 §Impact map (T108, T113, T401, T201, T202/208/210, T205/209, T302(b)/N309, T304/316–318, 319, splits 116/117). Status upgrades only with written proof or recorded independent evidence (T113 Q40: audit's exact rerun; 209: new developer proof, pending audit).
- Checkpoints: `8745e57` (L5), `11576cb` (L1; also swept in-progress L2/L3 theory edits, disclosed in its message), `026be3d` (L3), `c90aeb5` (report), `075d4074017445a0fd4d7443ffac97cd7f8c106b` (L2 + response-01) = **re-audit candidate**.
- PR preparation still pending (merge main; shared records; batch-owner reservation; finals; rehearsal).

### 2026-11-01 — Response to Codex audit-02 (Claude orchestrator, `claude-opus-5-5`)

- Rules read at `4470ab4` (unchanged). Audit-02: four low findings A2-L1–A2-L4, all fixed by textual qualifications with History lines in T116, T208 (two), T318; three optional editorial notes applied (report θ notation, L5 docstring with byte-identical rerun, T302(b3) Φ domain). Verification candidate `aea01283ad49d9a4527df727ad386c5f671933ee`. No status, proof or evidence identity changed; checker code and logs untouched. [response-02.md](response-02.md) carries the narrow impact map (6 files).

### 2026-11-01 — PR preparation (Claude orchestrator, `claude-opus-5-5`)

- Audit-03 (Codex) CLEAN; Stage PR. Rules: main `9739a0c` adds the local working-track rule (WORKFLOW §Computation and evidence); re-read after merging main.
- **AC instruction (2026-11-01, answer to the orchestrator's question on final IDs): "Claude allocates now"** — for this PR Claude allocates the final IDs as the next free ranges and records the owner change for this PR in the batch ledger.
- Merged `origin/main` `9739a0c` into the branch (`1167c33`): 14 shared literature records kept as one record per source (main's content first, this topic's statements after); INDEX/CORPUS/IDEAS keep main's rows plus this topic's sections; ledger from main. No theory, direction or audit file changed by the merge.
- Literature consolidation (audit-01 P2): 29 new records, 15 updated, 49 statements (Claude Sonnet 5.5 high, requested), commit before allocation.
- Allocation (`pr-prep/allocate.py --apply`): PD-T029–080 (52), PD-N007–031 (25), IDEA-077–176 (100), LIT-066–292 (227); `Final ID:` line added to all 77 theory files (header only); literature headings and index rows show final IDs with provisional in parentheses; registry rows added to PROOF_STATUS.md, ID_CROSSWALK.md (incl. 11 split mappings from SPLITS.md), state/IDEAS.md; NEGATIVE_RESULTS.md and AUDIT_LOG.md filled; one charter paragraph in state/CURRENT.md; two briefs in PAPER_MAP.md; ledger block recorded. Scientific statements and statuses unchanged.

- Rehearsal ([pr-prep/REHEARSAL.md](pr-prep/REHEARSAL.md)): squash of `1edf4b9` onto main `9739a0c`, 0 conflicts, tree identical to the branch, checker exit 0, main registry rows preserved except documented intended edits.
- Local working track (new WORKFLOW rule): wrote `C:\Users\andreyac\Downloads\padua\results\bivariate-lanczos-20261031.md`; replaced this topic's two older sections of the shared `RESULTS.md` by one section merged from it (staged current bytes, merged, mtime-guarded write; other topics' sections untouched).
- **Draft PR [#10](https://github.com/aacchhee/padua_research/pull/10)** opened against main (WORK/AUDIT/PR sections; AUDIT marks the focused integration review PENDING). Only AC merges.

Consolidated list (exact commands in the cited records): L1 SUMMARY §6; L2 above; L3 SUMMARY §5; L5 R01 §7 and R03 §7 and response-recon-01; repro/REPRO.md §5. None executed by this session; all require AC's servers (syvert0/1/2) or more time.

## Open for AC

- (resolved 2026-10-31 21:41) Push access attached after AC approval.

## 2026-11-01 — Codex focused re-audit of response-01 (completed)

- Requested role: independent Codex re-auditor, `gpt-6-astra xhigh`. Five bounded workers reuse the explicitly configured Astra/xhigh audit agents for L1/L4, L2, L3 residual conventions, L3 formula/scope and L5. Root owns the impact inventory, cross-scope disposition and Git; no developer correction is made by the auditors.
- Rules read at session-start branch head `50b0d304001b48607527e5086a67045f534d9472`: `AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md` (byte-identical to the prior read). Fetched main `0d058fb410166bd97b178be57910f2d256d0b529`; topic fast-forwarded from `5f523313b7b388cb114103734028f0a850dfeaad` to `50b0d304001b48607527e5086a67045f534d9472`. The previously recorded preparation boundary still defers merging main; this is a frozen focused audit.
- Scientific response candidate: `075d4074017445a0fd4d7443ffac97cd7f8c106b`. The publication delta to `50b0d30` changes LOG and the response's self-SHA pin, not science. This inspected metadata-only delta is recorded explicitly despite the response's shorthand “only LOG bookkeeping.”
- Executed root command: `python3 topics/bivariate-lanczos-20261031/audit-02/check_impact.py > topics/bivariate-lanczos-20261031/audit-02/impact-check.json`. Result PASS: all 65 response-declared changed/new theory hashes match, 10 are new, 12 original theory files unchanged, 77 total. Every audit-01 artifact identity remains intact; rules/IDEAS/literature registry bytes are unchanged, so their prior full reads are reused. All producer-code changes are additions of response checkers; existing producer implementations are unchanged.
- Review scope includes all prior finding dispositions, changed hypotheses/status splits, new proofs 209/318 and their dependencies, propagation into summaries, the exact normalization refutation and evidence interpretation. No new research candidate, primary-source reading or novelty claim is introduced. Independent executions and inspected historical evidence are distinguished in the completed `audit-02/` reports.
- Completed result: [audit-02.md](audit-02.md), five scope reports, protocol, independent checkers and execution manifests. Original audit-01 scientific findings resolved within scope. T209 and T318 confirmed by independent analytic reconstruction and changed checks; T302/N309 conventions and L5 paired statistics are clean in scope. Prior broad suites were reused only after identity checks; no repeated large-M or C experiment is claimed.
- **CHANGES REQUIRED; WORK**: four new low-severity qualifications, A2-L1–A2-L4 (T116 B-denominator hypothesis; T208 zero-operator quotient; T208 conditioning premise for numerical projector evaluation; T318 perturbed-functional evidence label). No high/medium finding and no failure of the surviving exact inequalities or new proofs. Developer science remains unchanged by the audit. The next response can be narrow, preserving all proved/conditional/measured/open statuses and frozen audit records.
- Root checkpoint `84958660511d57227e11e6ef1712bed21c4d0233` published the initial impact receipt. Final audit artifact identities and cumulative budget check are in `audit-02/artifact-manifest.json`; the response source remains pinned to `075d4074017445a0fd4d7443ffac97cd7f8c106b`. PR preparation, main integration, literature consolidation, owner reservations, final IDs and rehearsal remain deferred.

## 2026-11-01 — Codex narrow verification of response-02 (completed)

- User requested `gpt-6-astra xhigh` verification of A2-L1–A2-L4 and the narrow impact map. Root and the continuing explicitly configured Astra/xhigh auditor independently inspected the changes. Rules read at the session start and verified identical at `63ffc67f8bc60bd30abcd94769b6aa1d1e783d88`; main fetched at `9739a0c56b7a3976422ce60a8441bfbbfd6554df`.
- Response candidate `aea01283ad49d9a4527df727ad386c5f671933ee`; published head `63ffc67f8bc60bd30abcd94769b6aa1d1e783d88`; baseline `4470ab4857050b3acab114ddcbffc8996d4f2d88`. The publication delta is LOG/response self-SHA bookkeeping only. Main integration remains for the preparation boundary; the auditors changed no developer science or frozen evidence.
- **CLEAN**: A2-L1–A2-L4 and the named editorials resolved. [audit-03.md](audit-03.md) and [independent verification](audit-03/independent-verification.md) record the dispositions. The root impact checker passes all six mapped hashes, exactly four changed theory files with unchanged statuses, 73 other theory files unchanged, and preserved audit artifacts. The L5 code change is docstring-only by AST comparison; its actual analysis rerun and `cmp` exit 0 with byte-identical output.
- Stage **PR — preparation pending**. No new mathematical status, experiment result or novelty claim is introduced by verification. Prior audit coverage and unresolved scientific targets remain as declared. Canonical literature consolidation, merge of current main, batch-owner/shared-state reconciliation, final IDs/crosswalk and rehearsal are the next authorized preparation work; material changes require recorded impact review.
- Actual commands, content identities and retained-output budget are in `audit-03/check_response.py`, `impact-check.json` and `artifact-manifest.json`. Old broad suites were not repeated, and no external archive/fulltext was retrieved.

## 2026-11-01 — Codex focused PR-preparation integration review (completed)

- AC requested independent `gpt-6-astra xhigh` review of draft PR #10 before merging. Root orchestrates; three continuing explicitly configured Astra/xhigh workers own disjoint registry, literature, and scientific-preservation reports. Root runtime model/effort metadata is not separately exposed. No developer correction or Git mutation by workers.
- Rules read at `a2dd845b8a231e1b00733e1361e2a9ad3bad222f`: AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md. Topic fast-forwarded from audit-03 publication `cf01449fc96233c9074ce25efcb056535414aa1d`; fetched main `9739a0c56b7a3976422ce60a8441bfbbfd6554df`. Rules equal current main, including its local working-track paragraph. Reviewed source is `a2dd845`; PR body's `2e1530be33a3ecc5a9d677e25b86ccacb13b90b2` differs only by LOG publication metadata.
- Scope: final-ID and split mapping, global registration, merged/new literature, shared summaries, allocation coordination, preservation of the accepted science and exact-head integration. No new idea or novelty claim. Registry/literature auditor reads are recorded in their reports; root identity-only work does not claim a fresh general novelty or primary-source audit.
- Root actually rehearsed main→reviewed PR head by squash in `/tmp/padua-pr10-audit04`, leaving main unchanged: 0 conflicts, tree `d9209d88668415a5c2ecda22b6809edd786cfc63` identical to reviewed head. Developer semantic checker exits 0; independent root structural/preservation checker also exits 0. Correct structure does not establish disposition/dependency/summary fidelity.
- All 77 theory bodies are unchanged except matching Final ID headers; 574 other pre-existing topic/track science/evidence files are byte-identical, including 139 code files and frozen audit/review records. No mathematical suite, producer experiment or large-M run was repeated. No status upgrade. All 404 mappings, 100 candidates, 227 literature statements and 11 split mappings are structurally complete; no main collision.
- **CHANGES REQUIRED; WORK**: [audit-04.md](audit-04.md) records four medium integration findings (superseded IDEA dispositions; reversed/omitted dependency edges; wrong status/operator or missing hypotheses in public summaries; duplicate arXiv source record) and one low generator-repeat-run defect. The destructive generator reproduction occurred only in a disposable copy. Accepted scientific claims remain intact. Claude must disposition findings in response-04 with stable IDs and a narrow impact map; no correction was silently made by the auditors.
- Current active PR snapshots: #6 `9bd14a6d2c4da69139a10107d8a787f2be0c5c9e`, #9 `95279b833bca5967fcf47c1b71a56ff622185b4e`, #11 `4f937137f9baac5e51814964e6a83aeb2df38815`. #11's LIT-293–298 is disjoint from this PR's LIT-066–292; later allocations must reconcile it too. This audit does not approve those PRs or the remaining batch merge sequence. The logged AC owner exception remains valid; no reauthorization is requested.
- Reports, checkers, exact input identities and bounded retained evidence are under `audit-04/`; its artifact manifest records hashes and cumulative size. PR metadata was inspected read-only and the existing draft attached to this chat. AC's local Windows working track and cold storage were not accessed or independently verified. Only AC merges.
