# Independent supplemental review: audit-02 execution response

Status: **SOURCE, SYNTHETIC CONTROLS AND LOCAL KNOWN-CASE INTEGRATION ACCEPT**
for candidate v3, with the exact scopes and separate integration record below.
The initial notes preserve their preliminary scope. This supplements and does
not replace the Claude audit.

## Identity and scope

Rules read at `4a5de2012bad94601c713b2ff5517f2e3fb80af2`:
`AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md`.
Reviewer allocation requested and accepted by the orchestration API:
Codex `gpt-6-astra`, medium. Actual serving model/effort metadata is unexposed.
The reviewer initially inferred a different allocation from generic context;
that inference had no runtime evidence and was withdrawn before auditing.
Root alone controls Git and shared records; this reviewer owns this file.

Scope is the new operational variant under `code/audit02_execution/`, PA1–PA4
and runtime-related A-7/A-8/A-10/A-12. The original Syvert2 ZIP, its source,
the frozen mathematical engine/native sources and all mathematical claims
remain outside changes. No novelty claim or new mechanism is proposed, so
WORKFLOW's full novelty inventory exception applies to this technical review.
No new mathematical claim, final ID, degree certification or gap closure follows.

Inputs read in full: interim audit-02, T1 engine report, T2 pack report,
and handoff 11. Initial source inspection is explicitly of mutable files,
not an acceptance of an exact candidate. Commands to date are file listing,
text reads and read-only Git identity lookup. No candidate import, fixture,
compiler, native engine or measurement has executed in this review.

## Acceptance obligations

- **PA1:** Record initial SIGCHLD, reset before any operational child, refuse
  inherited nondefault disposition. Each operational child gets a genuine
  waitpid status; ECHILD is failure, never exit zero. The unchanged engine
  must inherit SIG_DFL. Exercise default exit 7 and ignored inheritance.
- **PA2:** SIGHUP/SIGQUIT reach owned-child cleanup. Worker parent-death
  setup checks parent identity after prctl. Cross-boot collection is allowed
  only for fully quiescent, identity-bound records; failed preflight has a
  supported no-attempt recovery preserving its history. Manual quiescence
  attestation is not evidence. Supervisor SIGKILL can leave engine descendants
  despite worker PDEATHSIG; that path must remain nonquiescent and unsupported
  until a justified recovery, rather than being described as complete cleanup.
- **PA3:** Keep first-failure stop as root's current decision. Partial returns
  validate every claimed completed attempt and report the exact completed,
  failed/interrupted and never-started sets. They claim no 273-degree closure.
  Degrees 161–191 have valid numerical and three-actual-corner routes; lacking
  the two analytic shortcuts does not imply their failure.
- **PA4:** Fixed known cases 41 and 511 only, each primary followed by a fresh
  process, with two workers, 2 GiB per worker, assigned affinity and pinned
  libraries inherited by compiler and engines. Record actual capture and
  closure. Four 120-CPU-second engine envelopes are the stated scientific
  maximum, with separately specified supervisory allowances. A later data
  audit is not an independently executed rerun. No residual/bulk/dry run.
- **A-7/A-10:** Compare public pinned runtime bytes before jobs and inspect
  actual loaded closure; record snapshot locators and retrieval limitations.
- **A-8:** Enforce short paths before starting; never truncate receipts or
  relax their strict 16384-byte bound.
- **A-12:** Append-only admission/history, exact prior never-started matching,
  no deleted-attempt retry. Bound ZIP member and total declared sizes before
  decompression, compare inventory sizes and stream hashes; all later reads
  must remain within the established bounds.

The reported local sandbox (4 CPU quota, 16 GiB memory, approximately 28 GiB
free disk) calls for a separate two-worker local profile. The old Syvert2
40-worker/128-GiB-disk assumptions cannot be silently reused or claimed tested.
Generated evidence must fit the temporary repository ceiling with measured
headroom; full raw capture remains outside Git and archival transfer pending.

## Early observations sent to developer (unfrozen source)

1. `normalize_startup` initially refused nondefault SIGCHLD before preserving
   a machine-readable initial disposition. Refusal was safe but the initial
   record requirement still needed implementation.
2. Admission before mkdir prevents retry after interruption but creates an
   admitted-with-no-directory possibility. Such a state must fail closed or
   be explicitly represented in incomplete coverage, never retried silently.
3. SIGKILL parent-death on the worker does not kill its separately sessioned
   engine descendants. Ordinary catchable supervisor signals can clean them
   through the supervisor subreaper; hard-death handling needs honest scope.

These observations are design feedback, not final findings against a frozen
candidate. Focused review and preregistered checks await exact source hashes,
publication and root release. No acceptance or execution is claimed yet.

## Exact source review — 2026-11-07

**Static source disposition: ACCEPT for bounded synthetic testing and the
separately gated known-case integration plan. Execution acceptance remains
PENDING.** No unresolved MAJOR or BLOCKING source finding in this scope.

Candidate v2 manifest `c132c271232b54902820d2089c241f179669163d8ebd3ebbd519f2f0e6eebdec`
and candidate v3 manifest
`836dcbf098ecb391b740fa884e594e260b74705e88d26339dcc5cba9bbbf673f`
were each checked using `sha256sum -c CANDIDATE.sha256`: all19 rows matched,
13 Python files and6 launchers. Every v2 source file was read in full;
v3's two narrow changes and all row hashes were rechecked. SPEC,
PREREGISTRATION, README and feasibility were read. Source provenance is this
exact manifest; root's subsequent publication commit is recorded separately.

Two MINOR findings against v2 were returned, fixed by the developer and
verified in v3:

- `assets.py`: snapshot `/package/` indices used binary package names.
  Indices now use source names flint/mpfr4/gmp; binary API locator unchanged.
- `server.py`: collector prepass omitted member-size/count bounds and excluded
  COLLECTION from the total. It now permits at most199999 payload entries
  plus COLLECTION, bounds each payload to512MiB and includes COLLECTION in
  the24GiB expanded total, matching the verifier. Availability of snapshot
  locators and actual large-bound behavior remain unexecuted.

The SIGCHLD reset/refusal record and strict waitpid adapter are present at
both operational entrypoints, with no substitution of ECHILD for zero. The
unchanged engine inherits default SIGCHLD. HUP/QUIT follow stop/cleanup;
worker PDEATHSIG is now catchable SIGTERM with parent-identity check before
any engine child. Its hard-kill limitation remains explicit. Historical
collection preserves the old writer domain and requires every group already
quiescent; nonquiescent reboot recovery remains deliberately unsupported.
Preflight-only resume preserves history and admits no retry. Missing admitted
directories refuse resume but appear incomplete in partial-return coverage.

Partial mode has an exact disjoint plan/admission partition and invokes full
attempt validation for every claimed completed status. Such validation errors
propagate. Incomplete records cannot create completed degree claims. The
admission chain and preserved prior-summary hash link resumed pending sets;
this is operational deletion detection, not authenticated history against an
actor replacing all records. Full mode still requires exact280 success.

Preflight authenticates arithmetic bytes before loader/compiler admission;
full pass validation also checks loaded FLINT/GMP/MPFR identities by family
against trusted packaged hashes. Short resolved roots, unchanged receipt cap,
and unchanged scientific freeze preserve the intended proof boundary. Actual
compiler/library compatibility and concurrent capture remain PA4's pending
execution obligation. Initial2workers are explicit even though PROFILE permits
up to4; no4-worker or residual run is thereby released. Builder still needs
exact local pinned packages and published source; it offers no substitution.

The resource assessment is appropriately conditional: `/workspace` overlay,
not `/tmp` tmpfs, hosts the prospective artifact; known-case timings are not a
residual campaign forecast. Collector measures archive peak and preserves raw
on insufficient space. No current raw-size theorem or full-campaign capacity
claim is accepted. Cold-storage retrieval/transfer remains pending.

Independent synthetic controls and their exact command, substitutions,
bounds and harness hash are preregistered in
`code/audit02_execution_review/PREREGISTRATION.md`. They have NOT executed.
No scientific/native/compiler execution has occurred in this review.

## Controls01 result and focused continuation

The published preregistered command ran once at4787aea and returned directly
observed exit1. The first five controls passed: actual exit7, ignored SIGCHLD
refusal/record, ECHILD refusal, HUP cleanup and QUIT cleanup. Parentdeath failed
before launching the fake engine because the harness's inherited hardCPU12
conflicted with the actual worker's requested260. This is my fixture defect;
it does not establish a source defect. The observer cleaned one fake sleeping
supervisor. The remaining six cases did not execute. See
`code/audit02_execution_review/RESULT-01.md` for exact raw identity and record.

A focused corrected harness/preregistration02 retains the failed run and
selects only parentdeath plus the six unreached cases. The parentdeath fixture
alone lowers its copied wrapper CPU profile to10; actual source and scientific
caps stay unchanged. Further execution is pending publication/root release.
Static-source acceptance remains unchanged; operational acceptance is pending.

## Controls02 result — 2026-11-07

The focused published command executed once atffe4d42 and returned directly
observed exit0. All seven selected scenarios passed: parentdeath, simulated
quiescent reboot/false-state refusal, preflight-only recovery, admitted-job
deletion refusal, partial-return routing/error propagation, ZIP bounds and
pre-loader arithmetic pin refusal. Every observer cleanup list and stderr
was empty. Exact receipt SHA256 is
`ad4c6564e0e5750b237ef2b2acd925694cdbe9108820697b92218dbbc27cc592`;
see `code/audit02_execution_review/RESULT-02.md` and retained `/workspace/p02c2`.

Together with the first five controls01 passes, all12 planned synthetic
scenarios have now executed successfully at their stated fixture scopes.
The initial parentdeath fixture failure remains preserved. **Static source
and bounded synthetic operational review: ACCEPT. Actual worker-to-real-engine
integration remains PENDING.** In particular, the sentinel partial test does
not validate genuine proof closure, and the parentdeath fixture intentionally
uses wrapperCPU10. Actual41/511, compiler loading, concurrent capture and
complete raw evidence remain separately released future work; no numerical
or native execution has occurred in this review.

## Actual integration closure

The separate accepted observer and actual local known41/511 execution have
now completed. Independent full data reviews of both unpacked evidence and
returned ZIP pass, without any reviewer native rerun. See
`independent-checks-audit02-known-integration.md` for exact identities, commands,
measurements and limitations. PA4 is addressed for this two-worker local
variant and these known cases; original Syvert2 release and the273 residual
degrees remain outside this acceptance. No further campaign is authorized.
