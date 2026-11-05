# Effective all-degree Padua argmax (PD-T099): campaign log

- Branch: `codex/padua-argmax-effective-20261103` · Base: main `440d107` · Developer: Codex (gpt-6-astra ultra, at AC's instruction) · Auditor: Claude (Opus 5.5 xhigh)
- Stage: PR (finalization checks) · Open handoff: [handoffs/07-finalization.md](handoffs/07-finalization.md)
- Reserved final-ID ranges: PD-T246–265, PD-N084–091, IDEA336–355, LIT466–473; first pushed in `ed8db2f`, [ALLOCATIONS.md](ALLOCATIONS.md). Final assignments: PD-T246–252, PD-N084–086, IDEA336–348, LIT466–470; [map](final-id-map.json).
- Claims: PD-T?argmax-effective-claude-01 — pilot gate measurements — MEASURED — [record](theory/argmax-effective-claude-01-pilot-measurements.md).
- For the PR: final IDs, PROOF_STATUS/IDEAS/INDEX rows, a RESULTS.md section, and the Claude audit.
- Open for AC: none at setup. Ask AC before using the NTNU servers.

## 2026-11-03 — Claude, claude-opus-5-5 (configured; effort not exposed) — campaign setup

- AC's requests:
  - "Reassess the frontier at Padua repo …"; then
  - "I want this work to be divided. First, write a handout for codex for Effective all-n argmax. This looks like a topic that warrants astra with ultra reasoning. Write all what you know about the problem, possible routes, and some easy gates. This campaign may be more adventurous."
- Rules read at `440d107`. Since `2b52b43` only agents/WORKFLOW.md changed (PR #18 storage rule: regenerable outputs to cold storage, small committed evidence). AGENTS.md and the role files are unchanged.
- Branch created from main `440d107`. The topic was opened by Claude for Codex development under AC's instruction.
- Read for the brief:
  - PR #17's report.md and gated/REPORT.md;
  - statements of gated-codex-01…05, 07–11, 13–15;
  - attempts/P0-finite.md;
  - PROOF_STATUS rows PD-T099, PD-T181, PD-T206–235 and PD-N078–083;
  - IDEAS rows 316–335;
  - literature INDEX entries LIT-312, 379 and 388.
- Pilot measurements (MEASURED; [record](theory/argmax-effective-claude-01-pilot-measurements.md)):
  - G2: true local corner constant;
  - G3: true global primitive constant and far-coset margin;
  - G0/G1: timings of the existing PD-T210 certifier at n = 17, 20, 24, 32, with the checker run on n = 17.
  - These are scratch runs: the certificates are regenerable and not committed, and no independent replay has been done. Degrees 17+ are therefore **not** certified.
- Written: [BRIEF.md](BRIEF.md) (knowledge base, routes R1–R6, gates G0–G8), [handoff 01](handoffs/01-work.md) (binding instruction and pre-registered gate criteria), and `results/padua-argmax-effective-20261103.md`.
- Novelty gate: deferred to the developer (handoff step 0). The brief lists the closest entries; no new mechanism is claimed here.
- Subagents: none.

- Addendum after handoff 01 was published (`71cf7be`): the pilot n = 32 producer run completed (complete cover, 282 leaves, 1464 s). Its row was added to the pilot record and outputs/certifier_pilot.md. This is MEASURED timing only, with no change to the handoff instruction.

- 2026-11-03 12:02, AC: "do you specify to focus on c/flint in sandbox if codex goes for big n?" Handoff 01 only said "port … if G1 shows that it pays". Per WORKFLOW redirection, handoff 01 is set to `superseded by 02`, and [handoff 02](handoffs/02-work.md) repeats the full instruction with step 4 and G1 amended:
  - large-n certification uses a C/FLINT (or GMP/MPFR) port run in the sandbox, with pure Python only up to about n = 32;
  - the port is validated against the reference checker on n = 9–24;
  - an independent checker port is cross-validated with the corruption controls;
  - no external machines without asking AC.

## 2026-11-03 — Codex continuation of handoff 02: setup

- Rules and input head: `8a1f394739293953e1566fd24a0a193cc78ff26f`.
- Fetched main `440d1079e42c3ef21c40d1cf8870f5b206410c6a`, unchanged
  from the branch base and already an ancestor; no merge needed.
- Role: orchestrator/developer. AC's explicit gpt-6-astra ultra request
  and handoff 02 override the usual allocation for difficult mathematics.
  Requested worker models/efforts and disjoint ownership are in [plan.md](plan.md).
- The selected managed sandbox started successfully. Network commands use
  its supported network permission and inherited proxy. GCC/GMP are available;
  no NTNU or other external machines are used.
- [Plan](plan.md) records the unmodified gate criteria and bounded first round.
  Producer/checker ports have separate arithmetic implementations; independent
  pilot/G0 replays are assigned. Runtime model metadata is not independently
  exposed beyond configured/requested tool settings.

## Development checkpoints

### Development checkpoint — native arithmetic and bounded gates

- Draft [PR19](https://github.com/aacchhee/padua_research/pull/19) opened;
  audit PENDING. Permanent ranges reserved in `ed8db2fc364d0ba34c3c06815460b3b2971787b5`:
  PD-T246–265, PD-N084–091, IDEA336–355, LIT466–473. No final assignments.
- Independent C/GMP producer and C++/GMP checker implemented. Overlap and
  independent reference runs are still in progress; no uncompleted degree
  is claimed at this checkpoint. The independent reviewer found and the
  producer fixed a start/end source-provenance race; final sources are
  snapshotted before compilation. Record frozen hashes with each run.
- G2/G3 pilots reproduced byte-for-byte by a separate worker. Extended
  measurements remain MEASURED; complete receipts are still being finalized.
  G6's float screen saw no reversal in1536 E-C comparisons n13–60; exact
  spot checks are separate pending work.
- The exact n4 fixed-sign-cardinal obstruction has a durable theory record
  and supplementary independent analytic reconstruction. It does not refute
  the undefined full G7 envelope class or PD-T099.
- [R1/R2/R5 attempt](attempts/r1-r2-r5.md): G5 lacks a specified uniform
  remainder model, R2 tail control remains unresolved, and the full-sign
  coefficientwise dual Bernstein test is equivalent to the existing test.
  These limitations are not fabricated threshold/negative-theorem claims.
- [G8 source reading](literature-g8.md) records bounded primary coverage,
  access gaps and a survey journal correction. No1-D proof is transferred.

- Independent replay of the pilot (handoff step 0).
- Gates G0–G8 and routes R1–R6, as in handoff 02.


### Analytic and bounded-gate completion

- Exact spectrum and all-degree normalized slopes proved in codex-06a/06b:
  A_n,B_n<=-n^2 Lambda_c/8. Strict local decrease is explicit for
  0<h_x+h_y<=1/(2[n(n+1)]^3); the fixed phase zone remains OPEN.
- Two scoped analytic obstructions preserve failed candidate history:
  all-positive spectrum fails at n3, and the (3,1) gradient/value ratio
  grows like -5n^3/(2*pi^2), blocking only uniform affine sign preservation.
- Supplementary astra high reviewer independently reconstructed all four
  corner proofs, the n4 G7-F obstruction and the R5 coefficient equivalence.
  The review is separate from required Claude audit.
- G6 exact three-pair evidence and independent acceptance/control receipts
  are committed; full floating samples remain outside Git. G2/G3/G4 and
  G6 are MEASURED at their recorded finite sample scopes. G5 remains
  undefined without a uniform remainder/margin model, not a failed theorem.
- Native producer contiguous through32 complete; independently reconstructed
  acceptance and fresh Python G0 continuation are being finalized. Only
  final receipt-backed degrees will enter the finite theorem.
- No new permissions, outside machine or third-party fulltext storage used.


### Final inspection finding — GMP rational canonicalization

- Native checker author found that `mpq_class(num,den)` operands in the
  Bernstein transform weights were added before canonicalization, contrary
  to GMP's arithmetic contract. Earlier numerical agreement and acceptance
  are retained as historical observations, not treated as resolving this.
- Reopened native25+ acceptance and corrected the weight construction.
  Independent exact Fraction comparison of production weights and corrected
  full replays are assigned across checker/gates/supplementary workers.
  Original Python G0 and analytic corner/obstruction proofs are unaffected.
- Producer inspection found explicit canonicalization of imported weights;
  a targeted unreduced-weight input control at2 reproduced every scientific
  field. Producer source and all canonical certificates remain unchanged.


### Development complete — corrected finite evidence and audit assembly

- Final corrected kernel `b0c871e7711219edfe3ce01480d8d1de3503a20d9b59f82b63a00eff248bc6e0`
  accepted every canonical certificate9–32. Different-agent execution:
  checker worker9–24 and29–31; gates worker25–28; supplementary reviewer32.
  Fresh independent Python G0 accepted17–24 with identical mathematical
  payloads; original Python checker also accepted every native overlap9–24.
- Corrected36-case corruption controls at9 and17, optimized-mode controls,
  compiled units and all23,816 canonical transform weights at2–40 passed.
  Earlier noncanonical-kernel receipts are explicitly historical/non-supporting.
- Native40 completed352leaves, but its corrected independent checker reached
  the authorized600CPU-second cap without acceptance. Degree40 is not
  certified;33–39 unrun. This is a capacity limit, not a mathematical failure.
- Finite global range is now2–32; all-degree normalized slopes and an explicit
  n^-6 physical local radius are proved. Three exact edge comparisons and
  three narrowly scoped analytic obstructions are retained. PD-T099 remains
  OPEN, with no explicit global n0; G5 lacks a uniform quantitative model.
- Primary producer speedup is11.6–11.9x on measured overlap degrees. Corrected
  producer+checker two-point capacity projections are61/82 for24h/7days,
  explicitly heuristic and constrained by precision/memory/support limits.
  Python producer-only projections51/70 omit checker CPU; no false pipeline
  comparison or certified-degree extrapolation is made.
- Small exact witnesses/receipts and the source/evidence inventory are retained
  in Git. Bulk raw gates/comparisons have a verified local archive87815bytes,
  SHA2567aafe2207be329528e39015fa233e96011050869efd00f1ebbd41cfbf4db2ae9;
  external/Windows delivery remains pending. No third-party fulltext stored.
- Final checks: exact replay/control results as above; evidence inventory and
  certificate-to-acceptance associations; Python syntax, JSON parsing, local
  Markdown links, git diff whitespace and allowed-path scope. No new math
  test is inferred from integrity checks.
- Main refetched unchanged at440d107. Concurrent draftPR20 honors this topic's
  reservation and uses the next disjoint ranges. No shared registry mutation.
- Current runs needed: required Claude Opus5.5 xhigh audit (including complete
  state/IDEAS.md), then the repository response/preparation workflow. No more
  development computation is queued. Final IDs and shared rows are deferred.
  Handoff02 completion and new03 are published in the next, separate commit.


## 2026-11-03 — Claude, claude-opus-5-5 xhigh — audit-01 (handoff 03)

- Rules read at `82feb49a8aa6e7de3c5fc7eac6dfc3625b3499a2`; audited scientific input `d790d58`. Main `440d107` refetched unchanged. Open PRs: #19 (this) and #20 (disjoint reservations, no shared-row collision).
- Role: independent auditor/orchestrator of the audit step. One Claude technical sub-auditor (Opus 5.5) replayed certificates; it made no Git or repository changes.
- Read: rules, BRIEF, handoffs 01–03, plan, report, all theory/ideas/attempt records, independent-check files, literature-g8, proposed changes, allocations, cold-storage record, and the complete `state/IDEAS.md`.
- Executed (scratch, outside Git): my own reconstruction of codex-06a/06b for n2–40 (direct solve to n14), PD-T227 formulas n2–30, radius sanity, PD-N 06b limit, G2 spot K(17)=0.289285, G6 float margins, manifest check. Sub-auditor: native replay of all 16 committed certificates n17–32 (accepted), reference Python checker n17/18/20 (accepted), 36/36 controls at n9 and n17 plus 10 extra corruptions and kernel mutants (rejected), independent coverage/corner checks, G6 exact checker (accepted, 11/11 controls), code inspection.
- Outcome: [audit-01.md](audit-01.md). All mathematics ACCEPTED at stated scopes, no status change. No CRITICAL/MAJOR findings; F1–F10 MINOR (record durability, wording, receipt provenance), N1–N10 notes. PD-T099 stays OPEN.
- Handoff 03 closed; [handoff 04](handoffs/04-response.md) opens the Codex response.
- Handoff links: [03-audit](handoffs/03-audit.md) done in `0ddc60a`; [04-response](handoffs/04-response.md) open.


## 2026-11-05 — Codex — documentation response to audit-01 (handoff 04)

- Rules read at `e5149eadfe49692ed67f84ba483c9737e2a649d3`; role: topic orchestrator/developer response. Bounded mechanical edits delegated to configured `gpt-6.1-sol`, medium. Orchestrator runtime identifies itself as GPT-6; a more specific serving-model/effort receipt is not exposed, so none is inferred.
- Fetched main `440d1079e42c3ef21c40d1cf8870f5b206410c6a`, unchanged and already an ancestor. Refreshed live PR heads: #19 `e5149eadfe49692ed67f84ba483c9737e2a649d3`, #20 `407fe83f5a709ae6d8da986d6eee074a0bcb21fc`, #21 `d669363c9bce16da2af0f3b7db05a031b911edd5`. No allocation, registry edit or integration rehearsal is needed in this response step; preparation must refresh the union again.
- Scope: answer F1–F10 in [response-01.md](response-01.md) with documentation fixes, explicit preparation deferrals and provenance limitations. No new mechanism, novelty/priority claim or mathematical development; the novelty gate is inapplicable to this mechanical response. The accepted statements, proof steps, statuses, checker code and certificates remain unchanged.
- Scratch artifacts are not assumed to survive workspace loss. Delivery to AC remains unverified; committed regeneration commands support remeasurement, not recovery of original raw bytes.
- Next: Claude Opus 5.5 high response protocol check, then PR preparation. No claim of completing that separate-agent check; only AC merges.
- F8 disclosure uses a separate linked provenance note: the native README is hash-pinned by the retained acceptance summary and is preserved with all receipt bytes. The derived evidence inventory is refreshed for documentation changes; audit-01 retains its original audited manifest identity.
- Verification executed: evidence inventory verified (84 files, degrees17–32), documentation links and allowed-path/protected-file checks, all F1–F10 response rows, and `git diff --check`. The inventory changes only four documentation entries; no scientific replay was performed or required.
- Handoff04 done in `6d73a6a482aa293f37db510f270205440a621a7c`; [handoff05](handoffs/05-response-check.md) opens the distinct Claude protocol check.

## 2026-11-05 — Claude, claude-opus-5-5 high — response protocol check (handoff 05)

- Rules read at `3decae238fd2248d5d9bff8217e16a7ba49b83c4` (unchanged since audit-01). Candidate `6d73a6a` vs audit input `e5149ea`. Main `440d107` unchanged. Open PRs #19–#22; PR21 (LIT482–561) and PR22 (PD-T286–293, PD-N100–103, IDEA376–383, LIT562–573) reservations disjoint from this topic.
- Checked: word-diffs of the three theory files, report and COLD_STORAGE (wording only); no change under code/, evidence/, audit-01 or handoffs 01–03; manifest verifier (`verified: true`, 84 files) and entry-level inventory diff (four documentation rows only); provenance facts in checker-provenance-01 against native-checker-summary.json. No novelty content, so the IDEAS reread is omitted (audit-01 read it in full).
- Outcome: [response-check-01.md](response-check-01.md) ACCEPTS the response. F8's missing per-receipt compiler/GMP mapping is an acceptable documented limitation, given audit-01's rebuilt replays. Stage PR; F5/F7 and the union scan move to preparation.
- Handoff links: [05-response-check](handoffs/05-response-check.md) done in `99553c5`; [06-pr-preparation](handoffs/06-pr-preparation.md) open.


## 2026-11-05 — Codex — PR preparation and AC-directed finalization

- Rules read at `37ff693c03a1c0c85b865d27b15403b03e5b3fec`; main unchanged `440d1079e42c3ef21c40d1cf8870f5b206410c6a`, already an ancestor. Mechanical registry work delegated to configured gpt-6.1-sol medium; root retains Git and PR control. Specific serving metadata beyond configured workers is not exposed.
- AC steering: "no more claude, fix everything yourself unless MAJOR" overrides handoff06's planned additional Claude preparation check. Handoff06 is superseded by [handoff07](handoffs/07-finalization.md); accepted audit-01 and response-check-01 remain unchanged. Resolve minor preparation findings locally and escalate only MAJOR issues.
- Scope is mechanical final-ID substitution and registration of already audited claims, with no new mechanism, novelty or priority claim; no new novelty gate or literature reading is required.
- Refreshed all-state PR population: open19–24; every closed PR is merged. Fresh full-file union scan covers55 ledger/registry copies and finds no range collision. Permanent reservations and gaps are preserved.
- Final registration:7 theory records (4 PROVED,3 MEASURED),3 PROVED scoped negative statements,13 idea dispositions,5 bounded literature records and the existing LIT379 addendum. F5/F7 completed; PD-T099 stays OPEN. No scientific status is upgraded.
- Checks executed: worker structural/link checks independently rerun by root (29 unique mapped records,3271 local link targets across25 files, exact RESULTS copy after link rebasing); root checked historical primary registry-row preservation except the three requested dated annotations and unchanged theory statuses. Existing historical duplicate PD-T140 rows are unchanged; no duplicate is introduced by this topic.
- Root diff review confirms only final-ID/alias/reference substitution and audit/registration metadata in theory records; no mathematical statement, proof step or domain change. Code, pinned native README, certificates, receipts, audit-01 and response-check-01 are byte-identical to the accepted input. No scientific replay is needed for mechanical registration.
- Evidence inventory regenerated and verified:84 files, degrees17–32,500421 payload bytes,11467 manifest bytes. Historical audit manifest identity remains in audit-01. `git diff --check` passes. Remaining disclosed limitations: original raw archive delivery unverified and original bytes unavailable; developer receipt-level compiler/GMP mapping incomplete, accepted as a documented limitation by response-check-01.
