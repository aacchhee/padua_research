# Effective all-degree Padua argmax (PD-T099): campaign log

- Branch: `codex/padua-argmax-effective-20261103` · Base: main `440d107` · Developer: Codex (gpt-6-astra ultra, at AC's instruction) · Auditor: Claude (Opus 5.5 xhigh)
- Stage: WORK · Next: `Codex (gpt-6-astra ultra): Continue codex/padua-argmax-effective-20261103.` · Open handoff: [handoffs/02-work.md](handoffs/02-work.md)
- Reserved final-ID ranges: PD-T246–265, PD-N084–091, IDEA336–355, LIT466–473; first pushed in `ed8db2f`, [ALLOCATIONS.md](ALLOCATIONS.md). Final assignments pending.
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

## Runs needed (continuation)

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
