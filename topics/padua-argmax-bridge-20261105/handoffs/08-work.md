# Handoff 08: Padua argmax bridge. Answer interim audit-01 and implement Claude's ranked plan

- Status: open
- Previous handoff: 07-interim-claude-audit.md
- Next agent / model / effort: Codex, gpt-6-astra high coordinator. Development: Sol medium for technical work and Sol xhigh for ordinary mathematics. A distinct Astra high/xhigh agent does supplementary checks. Astra ultra only with a recorded written justification.
- Role: orchestrator and developer
- Branch: codex/padua-argmax-bridge-20261105
- Input head SHA: `0cef8cba437a83aaa6116fec5b6eed034e8f2454` (interim audit outputs); this handoff is the following handoff-only commit
- Main / base: `76ba4214b100c86a44941f5e9a662ce9ce48efb8`
- Stage: WORK
- Written by / date: Claude, `claude-opus-5-5` (session effort metadata high; xhigh requested) · 2026-11-06

## Authority

AC: "this will be interim audit and it has to come with own ideas on how
to close the gap and set branch to work", and "codex does the work then".
The interim audit and ideas are complete, and the stage is WORK. AC has
already authorized this return to development, so no routine permission
question is needed. Pushes to this working branch remain authorized. Do
not push main, merge, force-push, change tags, `.github` or settings, or
mark PR27 ready. The closed fifteen-round campaign stays **15/15**. Record
the resumed work as a new, separately named work step (for example
"post-audit step A1…"), not as C16 or a reset count. Keep each step's
budget bounded and preregistered under the existing gates. Only AC
decides on further large allowances or a Syvert pack.

## Read first

1. AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md at the current
   head; record the SHA.
2. This handoff, [audit-01.md](../audit-01.md) and
   [audit-01-ideas.md](../audit-01-ideas.md).
3. The five scoped review records in [audit-01/](../audit-01/), and the
   LOG entry dated 2026-11-06 "INTERIM Claude audit-01".
4. Then the records each task below names.

## Task A: answer audit-01 (record fixes only)

Write `response-01.md`, answering F1–F9 one by one with the exact
change, or with a reasoned dispute for AC. All nine are MINOR record
findings. No statement, estimate, parameter, threshold or status may
change. If a fix seems to need one, it is no longer MINOR: stop and
record it.

- **F1.** The C13 status lines are stale. The focused review pins the
  bytes, so use a dated addendum or a re-pinned focused-review note. Do
  not make a silent edit.
- **F2, F3, F4.** Wording and traceability in the seven C13 files: widen
  the degree-domain lemma, fix the log n0<14 citation, complete the corner
  floor list, add the exact upstream equation citations, and inline
  u>=191/6144.
- **F5.** Archive the frozen 6cc04de4… C13 snapshot, its extraction
  script, and the C03 postcheck JSON and its script in the pending cold
  storage with hashes. Alternatively, record once that they cannot be
  repeated.
- **F6, F7, F8.** C03 record identity, closure-scope wording and
  CPU-measure labels. Apply them in gates, report, results and the PR
  body.
- **F9.** Document the non-additive out[] diagnostics in the C12/C15
  source contract notes. Do not change source behaviour unless a separately
  reviewed source change is justified.

Acceptance: every finding has a disposition, and the diff of the
response's record edits is limited to wording, citations and status
addenda. Supplementary Astra review of the diff is optional. The later
final Claude audit checks it.

## Task B: implement the ranked plan from audit-01-ideas.md

Each item is a new candidate with its own provisional IDEA/attempt/theory
records under the existing novelty and kill gates. Do not edit or reuse
the frozen C13 proofs, or any old n>=10^6 or n>=500000 quantifier, below
its own floor. Every numerical result stays MEASURED until there is a
validated enclosure and an independent check. Start with B1 and B2; these
two have bounded, cheap first tests.

**B1 (P4, highest priority, cheapest).** Write a MEASURED script that
evaluates C07's A1, A2, A3 and sine-channel sums exactly as defined (same
index sets, same normalization, both parities) at n=10^3, 10^4 and 10^5.
Report the actual constant K0 that replaces the "+16" in [L/3+16].

- Cap: 5 CPU-min.
- Gate: K0_actual<=4 at n=10^3 (estimated corner onset about 10^3).
- Kill: K0_actual>=0.1L²−L/3 at n=2·10^4.
- On success: write a lemma with exact or rational tail bounds and a
  corner-value lower bound that does not round d(n). Then redo every
  degree floor check of the C07 path at the new onset; the 1−120/n and
  enlarged-strip counts are examples that must be redone.

**B2 (P1 T1-a and T1-c).** A read-only diagnostic: no new model, no change
to C06 code, cap 600 CPU-s, MEASURED receipt.

- At n∈{512, 2048, 8192}, take the four binding phases (1/4,1/4), (1.38,0),
  (1.45,1.45) and (π/2,π/2). Print the signed actual value of every C06
  error component: endpoint rows minus sinc profiles, mesh, collision,
  ordinary-interior quadrature, E_n, D_n and Q.
- T1-c: re-evaluate M_far at (1.45,1.45) and (π/2,π/2) with tighter
  quadrature and the exact g_R tail. Decide whether the measured
  non-decaying ~10^-3 discrepancy near a=0 is a diagnostic artifact or a
  missing model term.
- Gate: the success and kill rules of audit-01-ideas.md P1 item 3.
- No uniform C(L+1)/n error form may be written until T1-c is resolved.

**B3 (P1 T1-b), only after B2 passes.** Preregister before running:

- the far-diamond phase-box cover;
- the Arb precision (128–256 bit);
- validated enclosures of b_full, C_far and the n-independent error-side
  quantities per box;
- the exact acceptance rule m(B;log N1)−2E(B,N1)>0 for all L>=log N1;
- the seam ρ0 treatment, and the near use against the defect floor;
- the cap: at most 20 CPU-h total.

Independent review of the reduction and source comes before the validated
run. Keep producer and checker arithmetic distinct. It is an open
question to evaluate: does using M_far on the near domain against the
1/64, 1/32 or 1/16 floor remove the need for any near-model increment? It
is a separate route; it is not a second near-model correction.

**B4 (P2 measurement).** At n=10^3 and 10^4, measure the per-row quantity
n·[row−profile] summed over the R=64 far endpoint rows, and n·|∂²E_end|
for the near R=128 block. Compare them with the analytic 86237 and 45000.

- Cap: 15 CPU-min, MEASURED.
- Write a Taylor-model contract (order 3 in h=1/n, 256 bit) only if B2
  shows these blocks dominate.

**B5 (P3 accounting).** First, with no computation: tabulate leaves and
checker CPU by class (far, corner orbit, maximum exclusion, outside) in
the existing n17/24/32 receipts. A bounded floating near-only pilot at
n=512 (cap 1800 CPU-s) follows only after that and after B1/B2.

P5 (the declared first-order far correction) stays deferred unless B2
shows that the componentwise route is limited by cancellation.

## Frozen

- The seven C13 records and their proofs.
- The finite 2–40 theorem, its certificates and checker.
- The C03 checker and immutable n32 candidate; C12/C15 sources.
- The one-correction near model N1-15.
- All PD-N scopes.
- The 15/15 campaign count and the PR27 draft state.

Keep every failed receipt and audit record. No new finite degree with old
technology, no producer launch, no major cleanup and no Syvert pack.

## Publication and next step

- Checkpoint each completed task with its records and receipts.
- Check the essential-evidence index, the per-file 16 KiB limit and the
  10,000,000-byte temporary ceiling. audit-01 added about 205 KB of
  authored reviews and small scripts.
- Update LOG, report, results and the PR27 WORK, AUDIT and PR sections.
- Final IDs and the registry application stay deferred, and the
  reservation must be refreshed at preparation.
- When development reaches a coherent batch, hand off to Claude for the
  final audit. That audit must also cover the n-independent upstream cores
  listed in audit-01 under "Not independently re-derived".
- At the session boundary, commit outputs first. Then, in a separate
  commit, close this handoff as `done in <sha>` and add handoff 09.
  Exactly one handoff stays open.
