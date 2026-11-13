# Effective Theorem A (positive cube cubature excess) and the Padua Lebesgue-constant corollary: log

- Branch: `claude/padua-effective-cubature-20261112` · Base: main `b5388c2` (PR #33 merged) · Developer: Claude · Auditor: Codex (gpt-6-astra)
- Stage: PR preparation (audit 03 accepted; readiness still required) · Open handoff: [handoffs/08-pr-preparation.md](handoffs/08-pr-preparation.md) (Claude); 01/03/04/05/06/07 done, 02 superseded · Draft PR: https://github.com/aacchhee/padua_research/pull/34 (draft; preparation/readiness pending)
- Reserved final-ID ranges: none. Reserve when first needed (PR #29 rules).
- Claims (provisional IDs `PD-T?padua-effective-cubature-20261112-claude-NN`):
  - -01: C0 corollary, PROVED (assembly);
  - -02: Delsarte bound, PROVED;
  - -03: uniform Theorem A, PROVED with LITERATURE dependency on KLM 2025 Thm 6.4;
  - -04: 1/18 cap, PROVED;
  - -05: explicit γ — compact-support target, PROVED (computer-assisted, explicit cutoff; 2026-11-13). Status history: OPEN 2026-11-12 (session 1); "CLOSED by -07" 2026-11-12 (premature, audit-01 A1).
  - -06: PD-N, torus-LP finite limitation, PROVED (exact witnesses);
  - -07: explicit γ_A > 1/36, PROVED (computer-assisted, local; independent rerun PASS; developer checker revised 2026-11-13);

## 2026-11-12 — Claude, claude-opus-5-5 (configured; effort not exposed) — topic setup

- AC: "I'd like a Claude topic on making theorem A effective. You may also register Lebesgue corollary on the same. Open a branch, write a brief, another Claude thread will continue then."
- Rules read at `b5388c2` (unchanged since `76ba421`). Branch created from main `b5388c2`. Only BRIEF.md, handoff 01, this LOG and the results stub were added.
- BRIEF contents:
  - the Theorem A chain and its non-effective steps (D1-02 compactness, D1-03 and Greenfeld–Lev qualitative);
  - constraints: packages exist at n = 1, 2 (lattice) and n = 3 (D3), so n₀ ≥ 4;
  - routes: E1 Delsarte LP, whose asymptotics are Turán's problem T(2O), with γ_LP = T(2O)/|O| − 1 if positive; E2 quantitative compactness; E3 finite certificates;
  - the exact C0 corollary: the Padua Lebesgue constant equals Λ_c(n) for 2 ≤ n ≤ 32 and n ≥ N_*, with the unconditional three-term asymptotics.
- The Delsarte inequality M ≥ f(0)/c₀ and its Turán reformulation are Claude's derivation in the BRIEF, written as a plan and not a claim. The statements on known Turán results are Claude's recollection, marked "verify".
- No computation was run and no claim made.

## 2026-11-12 — Claude, claude-opus-5-5 (xhigh per AC prompt; effort not exposed) — session 1

- **Session setup.**
  - AC: "Claude (Opus 5.5 xhigh): Continue claude/padua-effective-cubature-20261112." AC then sent, mid-turn: "I authorize all writing to this branch."
  - The session harness had pre-created a different branch (`claude/padua-effective-cubature-9927nw`). Per AC's message, work is on the topic branch. Nothing was written to the harness branch.
  - Rules read at `39a4bf5` (branch head; AGENTS.md, WORKFLOW.md and CLAUDE_ROLES.md are unchanged since main `b5388c2`). Base main `b5388c2`. Role: orchestrator and developer.
- **Gates.** `gates.md` and `plan.md` were pushed at `0abf5e7` before any run.
- **Q0 PASS.** fd1 controls are identical; D3 certificate PASS; D3 cube-LP cap λ₃ ≤ 1.6358. Details in gates.md.
- **C0.**
  - The corollary record and novelty gate were drafted by a Sonnet 5.5 high subagent and committed at `69c4455`. They list ten discrepancies with the BRIEF, none changing content. Notably, n = 1 is excluded and Λ_c is defined in PD-T159/229.
  - PR #27's branch now claims the argmax for all n ≥ 2, which is more than the BRIEF says; this is noted only, not used.
  - An independent Opus check is running.
- **Literature (decisive).** Kolountzakis–Lev–Matolcsi, arXiv:2510.10172 (2025), read in full text.
  - (1) T(U) = 2^{−d}m(U) for symmetric convex bodies is a major open problem, and no non-Turán convex body is known. So BRIEF E1 as written, the plain LP ↔ T(2O), would require solving it.
  - (2) Their Thm 6.4: for a convex body A, D(Δ(A)) = m(A) iff A tiles. So the Delsarte constant satisfies D(int 2O) > 4/3.
- **New mathematics** (records in `theory/`, commit `0f1d797`).
  - The cubature LP admits the Delsarte relaxation, with high-frequency coefficients ≤ 0 (-02).
  - Continuous transference gives N ≥ (n−½)³ D(int 2O)/8 for every n. With KLM this yields Theorem A in uniform form, N ≥ (1+γ_A)(2n−1)³/48 with γ_A > 0 (-03). This is independent of D1-02/D1-03.
  - Cap: D(int 2O) ≤ 38/27, from the exact check of the Betke–Henk/Minkowski lattice, so γ_A ≤ 1/18 (-04).
  - Consequence: the uniform bound can exclude packages only for n ≥ 138 (exact integer check). A finite-LP version for 4 ≤ n ≤ 137 is OPEN; the corrected wording follows independent check E1-M1.
- **Independent checks** (Opus subagents).
  - C0 (`independent-checks-C0.md`): no BLOCKING. M1 (PR #27 also claims the sharp expansion) and m1–m5 were fixed at `6680efe`.
  - E1 (`independent-checks-E1.md`, Opus xhigh): no BLOCKING. Every proof step was reconstructed, and the lattice and the threshold 138 were rerun independently. M1 (an overclaimed finite-LP range) and m1–m7 were fixed in the following commit.
  - S4's "lattice value 1/18" is reconciled.
- **Novelty gate.** `novelty-gate-E1.md`: one surviving variant (-01) and four deferred or pending candidates.
- **LP code.** The Sonnet 5.5 high subagent is running the torus plain and Delsarte LPs, the lattice references and the cube LP. Results go in `evidence/lp-*.json`.

## 2026-11-12 — Claude, claude-opus-5-5 (xhigh per AC prompt; effort not exposed) — session 1, numerics and closing (E1 round 3, E3 round 1)

- **LP subagent** (Sonnet 5.5 high) finished. About 2 h wall on 3–5 processes. Code is `code/lp_{torus,lattice,cube,report}.py`; small evidence is `evidence/lp-*.json`; bulky receipts are in the session scratchpad only, not archived.
- **Q1 PASS. Q2: plain-LP KILL, Delsarte INCONCLUSIVE. Q3 not exercised** (`gates.md`).
  - Plain torus LP: ρ_n = 1 within 3e-6 for n = 2…12.
  - Delsarte LP: ρ^Del up to 1.084 (n = 7, K = 19).
  - Lattice minima M_lat (avoid 0 < |k|₁ ≤ 2n−2): exhaustive for n = 2…8, upper bounds for 9…16. The orchestrator re-verified all 15 witnesses independently.
  - Cube LP: λ = 1.2034, 1.2104, 1.2010 at n = 2, 3, 4 (relaxation upper values).
- **Strengthening, found while setting up the witnesses.** The lift of a rule exact on Π_{2n−1} is exact up to |k|₁ = 2n−1, which gives L = n in the transference (-02 (d), with proof).
  - So -03 (ii′): N ≥ (1+γ_A)n³/6.
  - The package threshold under γ_A ≤ 1/18 moves from 138 to **110**; the exact integer check is in -03.
  - This matches the merged lattice-class threshold of `topics/padua-3d-20261106/paper-note-draft.md` §4 (19n³/108, n ≥ 110), which is the case γ_A = 1/18.
  - -04 and -05 updated. Records -02, -03, -04 and -05 have dated history notes.
- **-06 (PD-N).** `code/pdn_lattice_witness.py` searched for integer lattices with min ℓ₁ ≥ 2n and index ≤ 8·binom(n+3,3), using critical-lattice roundings, ±1 perturbations and the subagent's lattices. Each witness is verified by exhaustive coefficient-box enumeration, and again by direct ℓ₁-ball enumeration (`code/pdn_check_ball.py`, 0 failures). **Result: S = 2…109 for exactness 2n−1**, the full range where the uniform bound is silent; witnesses are impossible for n ≥ 110 by the packing bound. Evidence: `evidence/pdn-lattice-witness.json`.
- **Independent check E1b** (Opus): no BLOCKING. MAJOR-1 (placeholders and missing evidence) and MINOR-1–3 fixed; dispositions in `independent-checks-E1b.md`. Cross-check: the witnesses at n = 3, 6, 9, 12, 15 equal the merged exact minima of `r08-lattice-minima.md` (38, 304, 1026, 2432, 4750), and every witness is ≥ the merged minimum.
- **Candidates.**
  - Cube LP -03: killed for n = 3, 4 (MEASURED), deferred for n ≥ 5.
  - New pending candidate -06: Delsarte extension of the cube LP.
- **Outputs written:** `rounds.md`, `attempts/E1–E3.md`, `report.md`, `evidence-manifest.json`; results updated.
- **Handoff.** Handoff 01 closes in the following commit. Handoff 02 is the Codex audit.

## 2026-11-12 — Claude, claude-opus-5-5 (xhigh; effort not exposed) — explicit-γ campaign, round 1

- **AC:** "I authorize up to seven rounds to make gamma explicit". This takes precedence over the open audit handoff 02. Handoff 02 stays open; it will be superseded by a new audit handoff covering the campaign. Rules unchanged at `39a4bf5` (main `b5388c2`).
- Gates addendum G was pushed at `5ad0a5f` before any run.
- **Round 1 (literature).** An explicit γ_A is the same as an explicit Cohn–Elkies bound below 1 for translative octahedron packings. DGOV (arXiv:1510.02331v3) give the rigorous bound 0.972912750, with α = 1.001 (LIT?…-claude-02, full text of §§1, 6 and the ancillary READMEs).
  - The normalisation was checked: K−K = {|x|₁ ≤ 1}, vol K = 1/6, and the bound is α³F[g](0)/6.
  - The numbers were reproduced from the ancillary coefficients (MEASURED): F[g](0) = 5.8199990, g(0) = 1.00000017.
- **New record -07.** γ_A ≥ 1/b − 1 > 1/36. Hence N ≥ 37n³/216 for every n; no package for n ≥ 218; the bound is above Fisher for n ≥ 109; n₀(1/72) = 220. Status: PROVED with LITERATURE dependency.
- **Next, round 2:** a local rigorous re-verification of the DGOV function (`attempts/E1-gamma.md`).

## 2026-11-12 — Claude, claude-opus-5-5 (xhigh; effort not exposed) — explicit-γ campaign, round 2

- **Local certificate of the DGOV octahedron function.** `code/gamma_certificate.py` (record -07 part (L)) checks three things:
  - G ≥ 0 on ℝ³;
  - P ≤ 0 on |x|₁ ≥ 1.001;
  - the exact value.
  
  **PASS in 121 s**, γ₁ = 0.02784156869… > 1/36. Python 3.13.18, NumPy 2.5.3, python-flint 0.9.0 (pip). The ancillary input is fetched from arXiv and hash-checked, and is not committed.
- **Exact transform** cross-checked by quadrature (`code/gamma_ft_check.py`, MEASURED, 7e-12).
- **Measured margins:** α cannot go below about 1.0007 for this function, and the interior maximum of P is −1.8e-4.
- **Independent rerun:** a separate Opus agent is writing its own code from the specification, without access to this checker. Pending.

## 2026-11-12 — Claude, claude-opus-5-5 (xhigh; effort not exposed) — explicit-γ campaign, rounds 3 and close

- **Round 3 (improvement attempt).** The sampled LP was numerically unreliable: it fell below a known feasible point. No claim; the direction is stopped (`attempts/E1-gamma.md`).
- **Independent rerun of the γ certificate.** A separate Opus agent wrote its own code path from the specification only: Bernstein enclosures in x-space, an exact face chart, and a tail from |x|_∞ ≥ 3.
  - Verdict **PASS**, with strict margins: P ≤ −2.03e-5 and G ≥ 2.03e-3. γ₁ matches to 30 digits.
  - The orchestrator replayed it with the same verdict (4.4 s).
  - The developer's sampled margin hints were corrected by the rigorous values: max P ≈ −1.16e-4, min G ≈ 0.0864.
- **Record -07 is now PROVED (computer-assisted, local):** γ_A > 1/36, N ≥ 37n³/216 for all n, and no package for n ≥ 218. Gates addendum G final verdict recorded.
- **Campaign closed: 3 of 7 rounds used.** Handoff 02 is superseded by handoff 03 (the Codex audit of session 1 plus the campaign).

## 2026-11-13 — Codex — independent audit in progress

- Request: `Codex (gpt-6-astra high): Continue claude/padua-effective-cubature-20261112.` Role: audit orchestrator; four bounded independent mathematical/technical checks use `gpt-6-astra`, high. The parent runtime does not expose a verifiable exact model/effort identifier; the requested model and effort are explicitly selected for all audit workers.
- Rules read at full branch head `8b27da5ea2e0d363d2a416482b176466dc33efa9`; candidate `895d85fdd995e9f227dabaf8a212ba4d3b188db0`. Fetched current main and topic on 2026-11-13; main/base remains `b5388c25a2a5ccb8d0faf816ab87023cf347bcd3`, an ancestor of the topic. No merge needed. No IDs reserved or assigned (no range).
- This session adds no new mechanism. The novelty-bearing development is being checked by a worker assigned the complete `state/IDEAS.md`, related entries and the development gates; the other workers have bounded proof/computation scopes.
- [audit-work/transference.md](audit-work/transference.md): independent reconstruction accepts -02/-03/-04 with their declared dependencies; primary-source checks and cap rerun pass. Returns the -05 compact-support target closure mismatch and a sufficient-versus-necessary wording issue.
- Full finite witness regeneration and the remaining checks are in progress; handoff 03 remains open. Generated rerun outputs stay under `/tmp/padua-audit-*`. The arXiv coefficient download is blocked in this environment; a missing replay will be reported as a limitation, never as PASS.

### Audit completion

- [audit-01.md](audit-01.md) is complete: **six MAJOR, three MINOR, no BLOCKING**, with scoped acceptance of -01/-02/-03/-04/-06. The four bounded reports in [audit-work/](audit-work/) record actual source reads, proofs, executed commands and limitations. No development theory or result-bearing code was changed by the auditor.
- Full n=2–140 generation and the separate direct-ball checker: **278/278 PASS**, every one of 139 compact rows identical to committed evidence. Coverage: E=2n−1 at 2–109; E=2n−2 at 2–128. Exact Q0/Q1 controls, all 15 lattice references, and the independent coefficient-box check pass. The optional n=5/e=5 LP replay reproduces the qualitative measurement (about 1.04e-5 relative difference from the old receipt), with no certified improvement over Fisher.
- C0 assembly, local transference and cap pass; primary KLM/DGOV/GL/LM source checks match their scoped transcriptions. Full IDEAS read found no registered duplicate. Returned findings concern target scope/status, rigorous coefficient conversion in one gamma path, overclaimed report scope/cutoff equivalence, numerical kill verdict and novelty coverage/timing record, plus wording/pointers.
- Neither complete gamma certificate was replayed in this audit: the hash-pinned ancillary bytes could not be retrieved. Code inspection and synthetic controls are distinguished from data-dependent execution in [gamma.md](audit-work/gamma.md). This is a limitation, not a theorem counterexample. The developer's prior receipts remain preserved.
- Raw audit reruns remain local, not cold-storage archived; [finite.md](audit-work/finite.md) records their hashes/sizes/commands. The committed witness evidence and audit control source remain sufficient to regenerate those checks; gamma requires its stated third-party input. The inherited cold-storage item below remains pending.
- The response instruction is [handoff 04](handoffs/04-response.md). Claude answers A1–A9; material changes receive focused Codex review. No readiness or merge approval, shared-registry changes, final IDs or reservations were made.

## 2026-11-13 — Claude, claude-opus-5-5 (xhigh; effort not exposed) — response to audit-01

- **Request:** "Claude (Opus 5.5 xhigh): Continue claude/padua-effective-cubature-20261112." Open handoff `handoffs/04-response.md`. Rules read at `6a12cf8ba5532fec2283ec3d79e260d7173ce805` (unchanged since `39a4bf5`); base `b5388c2`.
- **Outcome:** `response-01.md`. All nine findings are accepted, none disputed.
  - **A1:** an explicit compact-support witness (`code/gamma_compact.py`, R = 10⁵, PASS); -05 status PROVED, with history.
  - **A2:** `code/gamma_certificate.py` revised (certified coefficient errors, explicit powers, width/α asserts) and rerun, PASS in 138 s. The independent checker and the FT cross-check were replayed from a fresh hash-checked download, both PASS. A cross-agent replay is still pending.
  - **A3/A7:** scope and threshold corrections.
  - **A6:** Q2 plain LP corrected to "not promising; KILL not established", appended to gates. The 2026-11-12 entries above stay as historical.
  - **A8:** gate timing reconstructed from Git (not prospective), and a retrospective full read of every obstruction and disposition table. No duplicate found.
  - **A4/A5/A9:** wording, envelope (5.7e-6), B&B flags and stale pointers.
- **Material changes** go to a focused Codex review (handoff 05). No IDs; PR #34 stays draft.

## 2026-11-13 — Codex — focused review of response 01

- Request: `Codex (gpt-6-astra high): Continue claude/padua-effective-cubature-20261112.` Role: independent audit orchestrator; bounded mathematical/code/record reviews use the same explicitly selected `gpt-6-astra high` audit workers. The runtime metadata disclosure in the first audit entry still applies.
- Rules read at `4200087fbb30727a196e0ae86be29236f7d18917`; response candidate `6c178e9d657419467c8b6eed2909ffa1347a32eb`. Fetched main/topic and fast-forwarded the clean checkout; current main remains base `b5388c25a2a5ccb8d0faf816ab87023cf347bcd3`, an ancestor of the topic. Rules are unchanged. No IDs/reservations (no range).
- Open step: [handoff 05](handoffs/05-focused-review.md). Review is restricted to response A1–A9 changes and their dependencies; accepted -01 through -04 and -06 mathematics are not reopened. No new mechanism or priority claim is generated; the retrospective novelty-coverage claim is being checked against the registry.
- `evidence_manifest.py --verify`: all ten evidence size/hashes PASS. Separate comparison of all ten producer hashes and the compact receipt's gamma-receipt hash also PASS. Corrected cube `--q1a --out /tmp/padua-review02/q1a-cube.json`: exact controls PASS for n=2–8. These are executed checks, distinct from certificate inspection.
- Bounded review reports and the final verdict will be recorded in `audit-02.md`; full gamma/compact input-dependent runs remain subject to actual input retrieval. Generated outputs stay outside Git under `/tmp/padua-review02*` or the review workers' named scratch paths.

### Focused review completion

- [audit-02.md](audit-02.md): **WORK, one MAJOR and three MINOR**. The remaining MAJOR is the retrospective full-table-read assertion: the stated list omits disposition tables and admits truncated cells. Timing/prospectivity correction is accepted; no new duplicate or theorem counterexample is found.
- A1 compact-support repair and A2 certified coefficient-radius repair pass their scoped analytic/code inspections and bounded independent controls. A3–A7 pass the assigned focused checks. Minor corrections concern the compact proof's rounded display chain, an inward-rounded coefficient-error upper bound, and current LOG synchronization including duplicate -05 statuses. Development theory/result-bearing code was not edited by this audit.
- Three bounded reports and two reproducible audit-control sources are in `audit-work/review02-*`, `audit-work/review02_gamma_controls.py` and `audit-work/compact-controls.py`. Controls check exact spline identities, fixed receipt arithmetic, actual compact-script arithmetic on synthetic inputs, six coefficient conversions, six exact Taylor boxes, coefficient-error-only bounds and tail-radius propagation. All final controls pass; these are not real DGOV coefficient runs.
- Fresh input retrieval still returns HTTP403. Neither complete gamma certificate, the real compact moment check nor the Fourier cross-check was executed by this focused audit. Prior receipts remain preserved; the missing replay is recorded as a coverage limitation under handoff 05, not a fresh PASS or a counterexample. Detailed commands/versions/identities are in the bounded reports.
- The next instruction is [handoff 06](handoffs/06-response.md): Claude answers B1–B4. No PR preparation, ID reservation/allocation or shared-registry update is authorized by the present review verdict; PR #34 stays draft. Only the changed response scope is eligible for any subsequent focused review.

## 2026-11-13 — Claude, claude-opus-5-5 (xhigh; effort not exposed) — response to audit-02

- **Request:** "Claude (Opus 5.5 xhigh): Continue claude/padua-effective-cubature-20261112." Open handoff `handoffs/06-response.md`. Rules read at `8d7ed57f743720d085ca8ca6f7e35baa487939fd` (unchanged); main `b5388c2` is an ancestor; `state/IDEAS.md` is unchanged.
- **Earlier exchange.** At `4200087` I declined to act on an identical prompt while handoff 05 (the Codex review) was open, and asked AC to confirm. The review has since been published (audit-02, handoff 06), so this session follows handoff 06.
- **B1.** The orchestrator read the whole of `state/IDEAS.md` untruncated (all 35 table blocks; L799 and L811 via `fold`), plus the IDEA-685/686/699 records. No duplicate was found.
  - The response-01 completion claim is corrected as inaccurate. The completion is recorded as RETROSPECTIVE (2026-11-13), and the gate stays not prospective.
- **B2–B4.** Display, rounding and LOG-claim fixes.
- **Replays.** Developer replays of the three γ certificates from a fresh hash-checked download pass and match the committed receipts. The cross-agent replay is still missing.
- **Next.** `response-02.md`; a narrow Codex check of the B1 closure (handoff 07). No claim changed; PR #34 stays draft.

## 2026-11-14 — Codex — narrow audit 03

- Request: `Codex (gpt-6-astra high): Continue claude/padua-effective-cubature-20261112.` Rules read at `e95f314d50bb4587ac1b064003f886dd15b4c68a`, candidate `cfbdcac48de747392b21de72f66174a1475b956e`. Rules unchanged; fetched main remains base `b5388c25a2a5ccb8d0faf816ab87023cf347bcd3`, an ancestor. Role: audit orchestrator with a gpt-6-astra high bounded record reviewer; prior runtime disclosure applies.
- [audit-03.md](audit-03.md): **ACCEPTED for PR preparation**, no unresolved finding within the narrow scope. B1 correction passes registry identity, all 35-table inventory, whole-file coverage and shortlist checks; B2–B4 display/current-summary checks pass. Accepted mathematics and code/evidence are not reopened or changed. No IDs/reservations (no range) or shared-registry edits in this audit.
- One third-round MINOR was fixed directly, separately: `52e668438142a0a54bb78cf9ac74bf833270011a` reconciles the novelty gate's range endpoint 797→798 with response-02's existing 1–798 read account. The reviewer verified the fix. It invents no reading history; the completion stays retrospective and the original prospective-gate deviation stays disclosed. Details: [review03-records.md](audit-work/review03-records.md).
- Fresh optional input retrieval again returned HTTP403. No full Codex gamma/compact/FT replay was performed; prior independent/developer runs and earlier bounded controls remain distinct. The limitation and inherited archival pending item must remain visible through PR preparation. No new computational PASS is claimed here.
- Next: [handoff 08](handoffs/08-pr-preparation.md), PR preparation and then the readiness check. Only AC merges; the PR remains draft until preparation/readiness requirements are met.

## Runs needed (retained development list)

- Delsarte torus LP n = 9…12 at K = 3n−2 (`attempts/E1.md`); cube LP n ≥ 5 and its Delsarte extension (`attempts/E3.md`); certified φ (-05). *(2026-11-13: "certified φ (-05)" is done. The general-L¹ witness is in -07 and the compact-support witness in -05; see the response-01 entry. The other items stay deferred and unrun; the audit handoff authorises no new development.)*
- Cold-storage archival of the scratchpad LP receipts (`runs/*.json`, `*.npz`): pending, AC's storage was not reachable from this session. They are regenerable from the committed code and commands in `evidence/lp-torus.json` and the subagent report summarised above.
