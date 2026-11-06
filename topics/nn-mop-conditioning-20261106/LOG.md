# NN MOP conditioning: intrinsic or metric? Sharp rates, weak stability, IEP-MOP comparison: log

- Branch: `codex/nn-mop-conditioning-20261106` · Base: main `76ba421` · Developer: Codex · Auditor: Claude (Opus 5.5 xhigh)
- Stage: PR · Next: `Codex (gpt-6.1-sol, medium): Continue codex/nn-mop-conditioning-20261106.` · [Audit 02](audit-02.md) accepted the response with no BLOCKING or MAJOR findings; PR preparation is [handoff 05](handoffs/05-pr-prep.md).
- Reserved final-ID ranges: none. Reserve when first needed (PR #29 rules).
- Claims: accepted within audit-01 scope; response addresses classification, attribution, records and robustness; see response-01.md.

## 2026-11-06 — Claude, claude-opus-5-5 (configured; effort not exposed) — topic setup

- AC asked what can still be done on the IEP/Leuven line. Claude proposed step 1, a focused round, and then a note. AC: "yes open a codex branch for step 1".
- Claude's reading of PD-T434 (arithmetic only) shows the step-line κ has the same exponential base as NN, about 4 times smaller. The open question is therefore whether the exponential survives the 1-D control, diagonal gauges and the LIT-347 normalization.
- Directions:
  - C1: the metric question;
  - C2: sharp rates (Krawtchouk upper, Hahn lower, ρ(p₁, p₂));
  - C3: weak stability;
  - C4: the IEP-MOP field-by-field comparison.
- Up to 8 rounds per direction, in parallel; coordinator gpt-6-astra high.
- Rules read at `76ba421`. Branch created from main `76ba421`. Only this LOG, handoff 01 and the results stub were added. No computation was run and no claim made.

## Runs needed / undelivered artifacts

- Initial M0–M4/C1–C4 items are historical setup work; completed scope and amendments are in gates.md.
- Advanpix-dependent archive experiments remain unrun (licensed toolbox absent).
- Padua cold-storage delivery remains pending; no destination is attached.
- General weak stability and matching full-Hahn/general-pair uppers remain OPEN mathematical tasks, not completed executions.

## 2026-11-06 — Codex coordinator, requested gpt-6-astra high — replay and launch

Rules read at full topic head `b4a04981d42c7cd872957facf5e3995e4096ca67`;
AGENTS/workflow/Codex role blobs equal the local main rules already read.
Refreshed main through GitHub connector: `76ba4214b100c86a44941f5e9a662ce9ce48efb8`,
the topic's parent. No base integration required. Shell fetch failed at the
configured proxy; pinned-file snapshot and publication route are in plan.md.
GitHub connection profile reports the prescribed author name/email.
Serving model identity/effective effort are not independently exposed.

Plan written before first run. First parallel launch had a shell redirection
race creating the temporary output directory: Hahn did not start; restarted
after directory creation. Both 180-dps and both separate 260-dps runs then
completed successfully. Original M0 cannot be assessed to 1e-10 against a
seven-digit historical table. Dated M0a amendment in gates.md preserves that
limitation. All twelve values pass fresh precision agreement and historical
rounding checks: code/replay_gate.py and m0a-receipt.json. This is numerical
repeatability, not a certified enclosure or historical raw-file recovery.

After M0a, delegated disjoint C1 metrics and C2 sharp-rate mathematics to
Sol xhigh, C3 stability mathematics to Sol xhigh, and C4 source/metric/code
comparison to Sol medium, as handoff01 explicitly requests. No final IDs or
shared scientific registry changes. Open handoff01 remains open while this
session carries the work. Commands: predecessor conditioning.py --sizes
4 16 32 --family {krawtchouk,hahn} --dps {180,260}, followed by this topic's
code/replay_gate.py /tmp/nn-mop-conditioning-20261106. Receipts pin raw outputs.


## 2026-11-06 — canonical publication-author exception

Checkpoint 8666d8e0a4f99f9f4f751c8b0b16f9064b23881d was created by
the connector as Andrey Chesnokov <59649991+aacchhee@users.noreply.github.com>,
despite get_profile reporting the prescribed Gmail address. Coordinator
verified the commit author after publication, disclosed the mismatch to AC,
and requested continuation under the predecessor's exception. AC explicitly
answered “Allow the GitHub noreply author.” This author exception now applies
to continued publication here; do not rewrite the existing checkpoint.
Draft PR: https://github.com/aacchhee/padua_research/pull/32.

## 2026-11-06 — C4 checkpoint and decisive C2 hard step

C4 completed two useful preparation rounds: source-access/fulltext review,
then exact local coordinate-interface validation (six cases). Required pinned
archive bytes remain absent; M2/M4 are BLOCKED, not numerical failures.
See attempts/C4.md and external-code.md. No external solver ran.
The two preparation rounds are published together at this checkpoint.

C2 requested the all-triangle Krawtchouk upper-rate hard step after the
novelty gate. Assigned a bounded distinct Astra ultra worker: matching the
full node/weight Jacobian upper rate is the decisive hard step explicitly
authorized in handoff01, beyond the routine terminal-witness algebra.
C2 retains parameter-dependent lower/Hahn work; upper worker owns only
theory/c2-sharp-upper.md and attempts/C2-hard.md. No result claimed yet.
Supplementary distinct Astra high checker independently reruns M0 and C4,
then checks new gauge/rate mathematics; this supplements, not replaces,
the eventual Claude audit.

## 2026-11-06 — C3 completed and C4 source resumed

C3 records the precise common-input residual-transfer gap and preserves
PD-T449 OPEN; two consecutive empty proof rounds end that direction.
The all-integer N4–32 native grid completed232 solver cases:58 each for
LU/QR/nodeqr/C4. On kappa*u<=1, A-LU maximum E/(kappa*u) is .809315
Krawtchouk and .469316 Hahn; C4 reaches40533.1 at HahnN14. These are
platform-dependent measurements, not a theorem or M3 PASS. A distinct
worker replayed the same complete scientific payload identically.
A chain-rule omission in the draft residual reduction was caught by the
coordinator and corrected to include direct terminal-input dependence
before publication. See attempts/C3.md and its two theory records.

AC then supplied IEP-MOP-main.zip in this session. Root verified its exact
SHA256; C4 verified all27 member pins and inspected executed source,
obtained isolated Octave9.4 using authorized package downloads, and
re-passed actual M4. Earlier BLOCKED records are historical and will gain
dated addenda, not be erased. M2 and full comparison are in progress.

## 2026-11-06 — C1 metric screen and sharp Krawtchouk output

C1 completed all61 integer sizesN4–64 at180/260dps for both scalar
marginals and balanced-terminal derivative bounds, using a primal/adjoint
solve rather than repeating the full triangle Jacobian. The signed OLS
endpoint construction bounds fits of both fixed- and smooth-gauge infima;
all meet M1's intrinsic threshold. This is a finite MEASURED screen, not
a certified enclosure or exact optimizer. Written all-gauge diagonal
lower bounds prove exponential Krawtchouk sensitivity in the defined
fieldwise metric. Scalar controls grow slowly on this finite grid.
See C1 core theory, c1-summary.json and c1-grid.csv.

Gate timing qualification: C1 read the complete inventory/obstruction
tables and nearest PD-T432/437 before derivation, but completed older
linked nn-mop-iep candidate and PD-T286/289 bodies afterward. No historical
novelty or fully prospective linked-source coverage is claimed. This is
the canonical timing qualification; mathematics was checked against those
completed reads.

The bounded Astra ultra worker supplied a complete all-triangle upper
proof kappa_N<=3,000,000 N^13(5+2sqrt(6))^(N−1), including all node/weight
directions, both a fields and terminal successors. With PD-T437 this
fixes the exact benchmark asymptotic base. The worker's exact N2–6
checks passed50 Bernstein identities,735 coordinate jets,1050 a-field
derivatives and330 terminal coordinate checks. Root and supplementary
Astra checker reconstructed the analytic argument; separate exact checks
continue. Required Claude audit remains pending.

C4 found a real one-ulp JSON transport change when checking identical
inputs. Early decimal-transport comparison outputs are exploratory only.
The wrapper now uses IEEE754 hex transport; final comparisons and C1
error diagnostics will be generated only after bitwise input verification.
No provisional comparison ratios are promoted here.

## 2026-11-06 — completed source comparison and C2 round2 checkpoint

C4's five productive rounds finish the finite non-Advanpix comparison:
source/runtime/replay, fidelity/lift, broad grid, rejected decimal
transport and final exact-bit rerun. All348 external calls and58 bitwise
shared-input checks pass; all116 final postprocessed records complete.
External NN errors explicitly add H+d0 high-precision postprocessing.
Advanpix-only experiments remain unrun. Full commands, source/member
identities and platform are in external-code.md; tables and receipts pin
the final result. Earlier BLOCKED and decimal exploratory records remain
qualified by dated supersession.

C2 round2 proves analytic all-N Hahn normality and a nonsharp fixed-mass
exponential lower base2. Its exact N2–10 checks cover273 defining systems,
219 kernel determinants,54 cross expectations and9 terminal derivatives.
The root noticed the determinant-constant indexing in the draft; it was
corrected to product_(r=1)^t r! before publication. C2's general Krawtchouk
lower is separately exact-checked; supplementary review corrected a
benchmark-specialization prefactor description without changing the
general lower inequality.

Supplementary Astra high checking completed analytic reconstruction of
the current gauge, scalar, matrix, sharp Krawtchouk, parameter lower and
Hahn normality/lower proofs, plus separate exact/numerical runs. Final
C4 postprocessing replay matches116 records/58 bit identities; the own
348-row C1 error-diagnostic recomputation matches. See independent-checks-01.md.
This is not the required Claude audit or readiness.

C2 round3 remains productive on a new balanced-terminal Hahn asymptotic
route; its candidate rate is not a proved sharp rate and is not included
in the current report's theorem claims. Current round2 outputs can be
checkpointed while that disjoint work continues. No final-ID reservation
or shared registry edits have occurred.

## 2026-11-06 — stronger Hahn terminal rate, independently checked

C2 round3 gives the exact balanced-terminal parity-row rate
rho_H=12.1136005841302405…, largest root of
r^4−14r^3+24r^2−14r+1. It proves a full-Hahn-map lower liminf of that
base, including both size parities and fixed masses, but not a matching
full-map upper. The positive coefficient representation, elementary
finite-type entropy lower and saddle upper are written self-contained.
The main full-map sharp target remains OPEN.

Focused distinct Astra high check02 reconstructs the argument, independently
verifies every separate second-weight gradient at M2–11, exact positive
formulas and fixed-mass directions, and generating coefficients through
M20; the original saddle equation and quartic agree at110dps. No unresolved
defect was found in that scope. Report/results/note material now cite
this stronger bound while retaining the simpler base2 record. A failed
product-of-global-maxima upper route is being preserved separately; it
does not refute the full Hahn target.

## 2026-11-06 — completed bounded round; AUDIT

C2 stops at6 of an up-to8 direction budget after two consecutive upper
attempts without a new quantitative bound. The positive-difference
extension has a small exact counterexample; unweighted grid differentiation
loses an exponential factor. Those are scoped route failures, not a
refutation of the full Hahn upper. All considered routes and remaining
correlated inequalities are retained in attempts/C2.md.

C1 completed3 productive rounds, C2 six bounded direction rounds with
parallel decisive Krawtchouk support, C3 stopped after two empty proof
rounds, and C4 completed five productive rounds after AC restored source.
The original general weak-stability target and full Hahn/general-pair
uppers remain OPEN. No Advanpix-only execution or cold-storage delivery
is claimed. Report, note material and results use those exact limits.

Publication granularity: coordinator checkpoints were pushed throughout
this session, while several rapid worker-labeled subrounds were integrated
at one checkpoint rather than each having an individual pushed boundary.
No fabricated per-round push or exhaustive8-round search is claimed.

Supplementary checks01/02 are separate from the required single Claude
audit. Stage is now AUDIT; no final IDs/ranges or shared registry edits.
Evidence manifest pins code/data only, with repository-only verification
by code/verify_evidence.py; the optional raw check does not claim archives
will exist in another runtime. Final numbered audit handoff02 is published
in the following commit after scientific outputs, preserving01's body.
Only AC merges.

Final verification: code/verify_evidence.py --raw passed58 committed
code/data/import identities and11 temporary raw identities. Focused02
also reviewed the final gauge transfer and upper-envelope failure, then
independently reran the last upper-search checker over75 indices,860
weight coordinates and430 common-node coordinates. Those attempt formulas
do not claim a new full-map upper. All developer/checker files are now
frozen for the candidate; required Claude audit remains PENDING.

Next: [handoff02 — substantive Claude audit](handoffs/02-audit.md).

Publication byte check: local generated CSVs use CRLF. The connector
checkpoint materialization through text-mode reads had normalized those
line endings. Final publication uses raw UTF8 byte decoding, preserving
CSV bytes and their receipt/manifest identities; numeric values are
unchanged. Remote blob identities are checked before closing the work
handoff. Main was refreshed again and remains76ba421.

## 2026-11-06 — Claude, Opus 5.5 xhigh — substantive audit 01

Rules read at `64a45b3` (identical to `76ba421` for AGENTS/agents/IDEAS).
Audited candidate `cc1edd2`; main still `76ba421`. Claude orchestrated five
Claude audit workers (Opus 5.5 xhigh for A/B/C mathematics, high for D/E
technical and protocol scope); none changed Git or repository files.
Full IDEAS read (lines 1–1112) and targeted INDEX rows recorded in the audit.

Every PROVED and MEASURED claim is accepted within its scope. That includes
the Krawtchouk upper and limit, the Hahn normality/lower/terminal rate, the
envelope PD-N, the gauge/scalar/matrix theorems and the parameter lower.
Independent exact and high-precision scripts are in audit-01/claude. The C1
grid rerun is byte-identical; the C3 grid differs in platform-dependent LU
values, and Krawtchouk N32 A-LU breaks down on the audit stack. The source
archive and Octave are absent from this runtime, so M2, M4 and the 348
external calls were reviewed from receipts and code only, not rerun.

Three MAJOR findings: PD-T448 classification and split wording; missing
LIT-502 and Fischer (LIT-113) attribution; candidate and PD-N records for
the failed C2 subroutes. There are also eleven MINOR findings and seven NOTEs.
Stage WORK; the response is [handoff 03](handoffs/03-response.md).


## 2026-11-06 — Codex response start (requested gpt-6.1-sol high)

Rules read at3d5b29d7aa8c1274793139d7040695035e1bda22; main refreshed
and remains76ba4214b100c86a44941f5e9a662ce9ce48efb8, an ancestor.
The additional-network shell fetch now works. Preserved the prior local
pinned-file snapshot under /tmp/nn-mop-pre-response-3d5b29d and checked
out the actual topic commit; no user changes were discarded. Git actions
remain with the coordinator. User authorized work on some optional NOTEs.

The substantive audit accepted mathematics/measurement scopes. This step
proposes a PARTIAL decomposition of PD-T448 in classification-proposal.md,
adds attribution and failed-route records, fixes the listed MINOR items,
and develops optional NOTE-1 gauge attainment separately for focused audit.
Only topic/results files are changed; no final IDs/ranges or shared edits.

Canonical C3 gate-coverage qualification (MINOR-9): the original C3 read
used bounded table-summary views and omitted the PR15/17/22/23/25, cleanup,
frontier, nonproduct and unnumbered-subroute tables noted by audit-01.
It produced no new mechanism, so this causes no claim change. Completing
IDEA fields in this response is retrospective; it does not imply a fully
prospective original gate. The optional new gauge result has a fresh gate.

One correction to the earlier LOG statement that report/results both
included the stronger Hahn rate: the committed results file was stale.
This response repairs that file explicitly rather than treating the
previous statement as evidence that it had been published.

Optional NOTE-1 gate timing qualification: all closest NN/Fischer/C1
records and obstruction/disposition tables were read before development.
Four unrelated lattice inventory summary rows, IDEA177–180, were hidden
by a truncated aggregate view and reread only after proof drafting.
The new work refines the audit-supplied degree taper; no historical
novelty or perfectly prospective whole-inventory completion is claimed.
Gate/candidate histories link here rather than duplicating the exception.

The new finite-attainment theorem uses analytic all-N reductions plus96
exact finite comparisons; a distinct requested Astrahigh worker replayed
and independently reconstructed every comparison using direct SymPy
moment differentials. Both benchmark applications are PROVED in the
recorded computer-assisted sense, subject to the focused Claude audit.
It does not promise a numerically representable/useful small taper or
optimize a relative global matrix norm.

## 2026-11-06 — response completed; focused AUDIT

All3 MAJOR/all11 MINOR findings have explicit fixes in response-01.md.
PD-T448's direct solved Krawtchouk rate conjunct now has a PARTIAL
classification proposal, without a shared-registry edit. C2 failed
subforms and two scoped negative homes preserve accepted mathematics.
Source attribution separates scaled-algorithm residuals from fieldwise
forward conditioning; Fischer and the unverified AT-system lead retain
bounded coverage qualifiers. Namespace-qualified mappings preserve aliases.

New NOTE-1 finite positive attainment is PROVED for both benchmarks,
allN>=2 and six node/mass variants. The exact finite reduction has96
Fraction checks and an independent direct-moment reconstruction with
identical exact payload digests. It resolves only the stated b-dominant
fieldwise optimization, without promising practical floating scaling.

The changed postprocessor passes the116-case healthy scientific payload
comparison,58 bitwise identities and14 byte-identical CSVs; four actual-
producer-shaped missing/broken-native paths record statuses and blank
metrics. The extracted hard checker passes50/735/1050/330 exact counts.
The C1 diagnostic changes only its stale receipt identity, with12
summaries/348 underlying rows unchanged. The final M2 metadata replay
from existing bit-grid output matches; no fresh third-party execution is
claimed in this response. Historical source receipts keep their original
producer provenance; response-code-checks pins the robust-code replay.

The manifest now includes the missing c1-matrix-all.json raw artifact.
Verifier passes86 code/data/import identities and12 temporary raw pins.
No shared registries, final IDs/ranges, rules, workflows or unrelated
topic files changed. Supplementary response-independent.md found no
unresolved defect; it is not Claude approval or readiness.

Next: [handoff04 — focused re-audit](handoffs/04-reaudit.md), published
after the response scientific output, closing03 by status only.

## 2026-11-06 — Claude, Opus 5.5 xhigh — focused re-audit 02

Rules read at `7c0c067`, unchanged since `64a45b3`. Audited response input `b3350ad`;
main still `76ba421`. Claude orchestrated four audit workers: G (Opus 5.5 xhigh,
new gauge theorem), R (Opus 5.5 high, classification and records), K (Sonnet 5.5
high, code) and N (Opus 5.5 high, full IDEAS read). None changed Git or repository
files.

The new finite-gauge attainment theorem is accepted as PROVED. The auditor's own
exact check covers 138 model-cases. The PD-T448 PARTIAL proposal, the attribution
fixes, the C2 subroute records and the two new PD-N homes are accepted. The
c4_compare breakdown fix was verified on a real platform breakdown, with healthy
tables byte-identical. response_code_checks.py could not run here, because its
hard-coded /tmp inputs are absent; that part is receipt review only.

There are nine MINOR findings and five NOTEs; MINOR-6 and MINOR-7 are optional
code hardening. Stage PR; Codex PR preparation is [handoff 05](handoffs/05-pr-prep.md).


## 2026-11-06 — Codex PR preparation checkpoint

Rules read at full head `2f23ee8f554eada30673840318db90b675baba67`; main remains `76ba4214b100c86a44941f5e9a662ce9ce48efb8`. Codex gpt-6.1-sol medium orchestrates documentation and registration; bounded Sol high work prepared the accepted PD-T448 classification. No new mechanism or novelty claim is generated, so a new novelty gate is not applicable. Audit02 MINOR corrections are in response-02.md; optional code changes were declined in favor of documented limitations. Result-bearing code/data are unchanged.

The full union reservation check covers main and all four open draft PRs plus all merged/closed PR statuses. [ALLOCATIONS.md](ALLOCATIONS.md) reserves fresh headroom; [inventory](preparation/inventory.md) records 16 theory results, three scoped negatives and 14 ideas. No new LIT record. Final assignment and readiness remain to follow.
