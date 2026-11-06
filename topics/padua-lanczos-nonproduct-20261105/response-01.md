# Response 01 — audit01 findings

- Developer/orchestrator: Codex, requested gpt-6-astra high; mathematical
  record worker: configured gpt-6.1-sol high; mechanical workers: configured
  gpt-6.1-sol medium. Serving metadata is not independently exposed.
- Date: 2026-11-06. Rules/input: `1f809519b353512a447661b35df9e92ad0ec6e06`.
- Inputs: [audit01](audit-01.md), output `ea13ed4a6cdc97dcd43f71a68d31681dcd9676d6`;
  [handoff04](handoffs/04-response.md); [AC Q1–Q3 decisions](LOG.md#2026-11-06--claude-audit-01).
- Scope: answer every finding without reopening accepted proofs, reflection
  method, finite outcomes or the three INCONCLUSIVE screens. No new scans.
- Fix commits: A3 is isolated in `3b0a990dda7a630cf4ea904639c01dad717c2ea9`;
  other finding-specific edits are in `04ba07bc10a680dc2a6bc90041f5013ba11482e7`.
  This response-output commit adds the response, current stage/links and a
  stale P1 rerun-status correction. Audit01 and frozen receipts are unchanged.

## MAJOR findings

### A1 — corrected framing; AC's weaker variant retained

**Fixed** in `04ba07b`: [P3-03 title/Scope](theory/p3-03-uniform-capacity-radius.md#scope),
[report headline and paper paragraph](report.md), [N4 row](gates.md),
[results](../../results/padua-lanczos-nonproduct-20261105.md) and PR30 body.
The title/scope wording is: **non-affine-product measures moment-equivalent
to SH_n through degree 2n+1, with an n-dependent weight mode**. Gram matrices,
monic basis, creators, pivots, source scales and frozen response are
eta-independent; only the ambient normal projector changes. The theorem
Statement and proof arguments are unchanged.

The coordinator's original scope reading is now recorded once in
[LOG](LOG.md#2026-11-06--codex-response-setup-and-scope-clarification), with
AC's Q2 acceptance. [IDEA P3-02](ideas/P3.md) records the n-independent
perturbation as OPEN/deferred to a follow-up topic, not a precondition for
this PR. Its first step, degree-<=2n moment normal-quotient perturbation
bound and original faster-than-every-polynomial radius kill are explicit.
No development of that target was undertaken.

### A2 — expanded disclosure; unrecoverable historical precision explicit

**Fixed to the extent supported by preserved records** in `04ba07b`:
[canonical LOG disclosure](LOG.md#canonical-protocol-disclosure--p3-gate-timing).
It addresses all four requested items:

- (a) the proposal's date/launch window, mechanism, cancellation observation
  and target; an exact message timestamp is unavailable;
- (b) incomplete shortlisted-entry/theory and full-table reads; the exact
  titles still unread at that instant are unavailable;
- (c) the retained formula/range/target and the same recorded high-mode
  mechanism, while distinguishing that from an independently pinned copy
  of the original proposal, which does not survive;
- (d) first simultaneous Git appearance in `6988024`, so gate-before-admission
  order rests on self-report.

**Explicit unresolved historical facts:** the exact message time, exact
per-entry unread list and byte/formula/range identity with the unpreserved
proposal cannot be reconstructed. No claim that these facts were verified
is made. This preserves the audit's own no-transcripts limitation rather
than inventing a retrospective prospective gate.

The [P3 IDEA qualifier](ideas/P3.md) carries the audit's requested wording
and **AC decision 2026-11-06: accepted**. The [Q1 disposition](LOG.md#2026-11-06--claude-audit-01)
is decided; no new permission is requested. Mathematical acceptance is
unaffected, and the deviation remains disclosed, not waived or cured.

### A3 — material BJ-only chain correction

**Fixed** in `3b0a990`: [P1 probe statement/evidence](theory/p1-continuous-creator-probe.md)
and [P1 IDEA chain and downstream uses](ideas/P1.md). Every use of
`g_j=1/binom(2j,j)` and the displayed finite chain now explicitly says
**under BJ**. MEASURED status and degree-eight scope are retained.

Source inspection confirms `p1_moment_probe.py:153–161` uses only
`records["BJ"]`; its source SHA matches the frozen receipt. No new experiment
was needed. No mirror/alternating values were added. This is the sole
material correction in this response and receives a focused diff re-audit.

## MINOR findings

Unless stated otherwise, fixes below are in `04ba07b`.

| Finding | Response and location |
|---|---|
| 1 — ratio/radius | **Fixed:** [P3-03 certificate](theory/p3-03-uniform-capacity-radius.md) and [report](report.md) state the bound first exceeds1 at n=18, no ordering is certified at2–10, every 0<eta_0<1 is sufficient, and endpoint weights vanish. |
| 2 — omitted N2 screen | **Fixed record:** [canonical dated LOG entry](LOG.md#canonical-n2-chronology-correction--p3p5-analytic-proofs) records the retrospective deviation and AC's Q3 acceptance. [Runs needed](LOG.md#runs-needed) lists optional exact Padua2–16/four-rule evidence for the OPEN sharp-exponent question. No P3 scan or new scan for this PR is required. |
| 3 — P3 predecessors | **Fixed after full relevant reads:** [P3 gate addendum](novelty-gate-P3.md) and [IDEA](ideas/P3.md) add PD-N012(a), IDEA415/highest-U sign witness and PD-T039 part2's parity-mixture mechanism. This is retrospective, with verdict unchanged. |
| 4 — P5 predecessors | **Fixed after full relevant reads:** [P5 gate addendum](novelty-gate-P5.md) and [IDEA](ideas/P5.md) add PD-T040(a) and PD-N063. Verdict unchanged. |
| 5 — chronology | **Fixed:** [report](report.md) places D65 motivation after the D36 high producers; [LOG](LOG.md) replaces the fully preregistered P2 wording with the [actual post-run IDEA chronology](attempts/P2.md#execution-timing-and-parked-probe), and calls P1's three rounds recorded, without upgrading its literature-only round. |
| 6 — dispositions | **Fixed:** [P3 IDEA](ideas/P3.md) has dated actual results/successful weaker-variant disposition; [P2 IDEA](ideas/P2.md) defers D65 with a resume condition and uses explicit abandoned/deferred dispositions for the other routes; [P6 gate](novelty-gate-P6.md) marks its unpursued rational-Padua route abandoned. |
| 7 — namespace ambiguity | **Fixed:** full IDEA/PD-T/PD-N prefixes distinguish P2/P4/P5 references in the corresponding ideas/theory records, notably [the annulus rejection](theory/p4-covariance-capacity-obstruction.md). Existing lowercase P5 IDs remain identifiable rather than silently renamed. Shared crosswalk application is a later preparation task, not performed here. |
| 8 — split fields | **Fixed:** [definition](theory/nonproduct-definition.md), [weighted](theory/p4-weighted-normal-quotient.md), [atomless](theory/p4-continuous-capacity.md) and [transfer](theory/p4-moment-capacity-transfer.md) records identify the common OPEN structural target as origin and separate supporting results/dependencies, removing inconsistent theorem-to-theorem splits. No proof dependency changes. |
| 9 — full support | **Fixed clarification:** [definition admission](theory/nonproduct-definition.md) now says strictly positive weight at every triangular node, matching its existing definitions/proof and P1 admission. |
| 10 — parent target | **Fixed:** [P2 MEASURED record](theory/p2-03-finite-recurrence-probe.md) removes the OPEN parent recursion/rate from its parts table and links the separate target. |
| 11 — provenance | **Disclosed:** [canonical LOG qualification](LOG.md#canonical-frozen-receipt-provenance-qualification) records dirty-tree harness provenance and N0's original harness absent from Git. Frozen receipts remain byte-unchanged. |
| 12 — rounding | **Fixed:** [report slope displays](report.md) round outward at four decimal places; certified rational receipts and verdicts unchanged. |
| 13 — repeatability | **Fixed:** [report](report.md) calls the Astra high rerun repeatability using the same reflection source/binary, retains INCOMPLETE collector status and unsaved alternating exit/timing, and distinguishes artifact acceptance. |
| 14 — gates/results | **Fixed:** [N1](gates.md) links D65 admission; [results](../../results/padua-lanczos-nonproduct-20261105.md) includes the PROVED covariance obstruction and MEASURED P1/P2 probes. |
| 15 — literature | **Fixed:** [P1 source checkpoint](theory/p1-literature-checkpoint.md) cross-references LIT292's AC-supplied Chapter3 read, distinguishes unread Chapter5 and keeps Xu2015's distinct provisional record. |
| 16 — symmetry | **Fixed wording only:** [report](report.md) and [LOG](LOG.md) say D4-invariant, not fully rotation-invariant. No exhaustive-affine-symmetry proof is added; therefore no additional material change. |
| 17 — checker provenance | **Fixed:** [P5 checker](code/p5_exact_checks.py) comments identify the hardcoded analytic lower field; executable AST is unchanged. [P5 attempt addendum](attempts/P5.md) discloses missing historical Python/platform metadata instead of inventing it. Frozen receipt unchanged. |
| 18 — stale text/spacing | **Fixed:** [weighted model](theory/p4-weighted-normal-quotient.md), [P4 attempt](attempts/P4.md) and annulus links identify actual supplementary and Claude reruns. P3/LOG spacing is corrected. This response output also updates the P1 current rerun-status table; historical execution chronology remains labelled as history. |

## Validation and remaining scope

- No new scientific execution; accepted proofs and computed results are unchanged.
- P5 executable AST equals the pre-response AST; only comments changed.
- Frozen evidence, inventory and audit01 bytes equal input `1f80951`.
- Diff whitespace, changed-file scope and local Markdown paths were checked.
- No new symmetry proof, final ID, reservation, shared registry edit, storage
  cleanup, external delivery or claim of PR readiness.
- NOTEs are preserved; no action is required. AC's storage decision and
  Q1–Q3 are settled, and are not referred back as open questions.

**Next:** focused Claude Opus5.5 high re-audit of
`1f809519b353512a447661b35df9e92ad0ec6e06..3b0a990dda7a630cf4ea904639c01dad717c2ea9`
(the two A3 files), with the mechanical response/readiness inputs. This is
not another substantive audit of accepted P3/P4/P5 proofs or P6 outcomes.
The eventual readiness check still needs final-ID reservation/registry
application from subsequent preparation. Only AC merges.
