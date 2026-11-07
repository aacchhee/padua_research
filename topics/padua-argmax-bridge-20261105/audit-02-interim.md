# INTERIM Claude audit-02: n>=320 analytic theorem and the Syvert2 pack (handoff 10)

**This is an INTERIM audit.** It is not a final approval, a readiness
check or a release decision, and it waives nothing. AC required stage
**WORK** and that Codex implements next. The companion record with
Claude's own independent ideas is [audit-02-ideas.md](audit-02-ideas.md).

## Decision

- **Mathematics: no BLOCKING and no MAJOR *mathematical* finding.** The
  global theorem for every integer n>=320 reconstructs, given its named
  accepted premises. Those premises include the Arb-trusted PD-T271
  constants. The five mathematical areas reviewed (below) found only MINOR
  record issues. Every claimed PROVED or accepted status matches the text
  of its review record's disposition. No review accepts "with conditions".
- **Finite degrees 42, 63–64 and 159–160** are fully certified degrees (D36
  engine, not the hybrid). I reran all five independently and reproduced
  the committed proofs. The residual set is exactly the 273 degrees
  43–62, 65–158, 161–319. PD-T099 stays **OPEN**.
- **The new hybrid checker** implements the proved finite reduction. Every
  engine run I made reproduced the committed evidence field for field. No
  finite degree depends on the hybrid yet, because its 41 and 511 runs are
  already-proved controls.
- **The Syvert2 pack: no BLOCKING finding, but four MAJOR findings (PA1–PA4)
  to resolve before any release.** PA1 and PA2 are concrete code defects
  that were reproduced with synthetic controls. PA3 is a decision for AC
  and root. PA4 is a missing integration execution. I found no problem in
  the scientific reduction, which is exactly the 7+273=280 worklist.
- **Unwaived inherited MAJOR chronology findings P1–P4** (novelty-gate
  order of work in E08/E09/E14) remain exactly as recorded. None alleges a
  mathematical error, and none affects validity (the auditors re-derived
  the affected lemmas). Mathematical acceptance does not waive them. They
  need an explicit AC disposition before readiness.
- **Stage stays WORK** by AC's explicit instruction. PR27 stays draft.

| Scope | Interim disposition |
|---|---|
| Global argmax for every integer n>=320 (paper proof, E14-assembly320 and components) | Supported given named premises; MINOR record findings only |
| Scalar H (E07) and fixed model (E10/E11) | Supported; scalar theorem re-derived |
| Outer 13/500, corner-256 loss 1/30, far-192 gap 3/100 | Supported at their stated scopes; E15 is not a global-192 theorem |
| Finite degrees 2–42, 63–64, 159–160 | Supported; D38 degrees independently rerun |
| Hybrid engine (corner256 and far192 analytic leaves) | Supported; implements the stated reduction |
| Syvert2 pack scientific reduction | Correct (exactly 7+273) |
| Syvert2 pack protocol and code | **Four MAJOR findings (PA1–PA4) before any release** |
| Actual ZIP artifact | **Not inspected** (absent from this checkout) |
| Gap 43–319 (273 degrees), PD-T099 | **OPEN** |

## Identity, rules and audited candidate

- **Auditor identity (disclosure).** AC's prompt asked for Claude Opus 5.5
  xhigh. The session model was switched to Sonnet 5.5 (`/model`) before
  this turn, so the **orchestrator ran as `claude-sonnet-5-5`** and
  derived no mathematics itself. All mathematical and technical audit and
  the idea review were done by **six Claude Opus 5.5 subagents, each
  instructed at xhigh effort** (effective effort is not exposed).
  WORKFLOW assigns mathematical audit to Opus 5.5 high or xhigh, so the
  allocation is satisfied by the subagents. The orchestrator checked
  their outputs and read the key scalar results. Every one of them is
  distinct from the Codex developers and reviewers.
- **Role:** interim independent auditor and idea author; orchestrator for
  Git in this step only. Subagents made no Git change and no repository
  edit. One subagent briefly created an ignored `__pycache__` file inside
  the repository and removed it; no tracked file changed.
- **Rules:** AGENTS.md, agents/WORKFLOW.md and agents/claude/CLAUDE_ROLES.md
  were read at be9a831 earlier in this session. A diff against the audited
  head 1b6aa31 for AGENTS.md, agents/ and templates/ is empty.
- **Candidate:** branch `codex/padua-argmax-bridge-20261105` at
  `1b6aa31ae759022ce89bb8a3be70a881790e259f`. The handoff names input head
  `a68533f1e93d3432b4c1ede65e1cb8ea43d16935`; the two differ only in the
  handoff files. Integrated main/base is
  `f70a260e5b5f9a01209dc8a05faabdcf8db1feeb`.
- **Round:** this is a second interim audit of the topic after audit-01
  (F1–F9 were answered in response-01.md). No in-place MINOR fixes are
  made (WORKFLOW reserves those for the third audit round onward).
- **Hashes verified** [E] (all match the records): the 10 audited
  theory-file byte prefixes against the hashes their reviews accepted; the
  hybrid FREEZE (4153 B, `0d9ce0a5dbb7fb37…`), all 9 AUDIT.sha256 entries
  and all 13 FREEZE code/data rows; the D36 FREEZE and rows; CANDIDATE.sha256
  (16 files); every committed hybrid and D38 certificate; the global320
  review (36528 B, `25529c8a5ad54111…`), the hybrid-engine review
  (51294 B, `f812fd447e…`), 12 cited prefix/report hashes, and the
  evidence receipts of operational runs 01, 02, 03 and the genuine-data
  check.

## Coverage and method

| Review | Scope | Record |
|---|---|---|
| M1 | E14 global320 assembly, cover, equality set, scalar chain, premise domains, P1–P4 | [m1-global320.md](audit-02/m1-global320.md) |
| M2 | E07 scalar H, E06, E10/E11 fixed model, E04/E05 constants, PD-T271 scope | [m2-H-model.md](audit-02/m2-H-model.md) |
| M3 | E13/E14 outer, E12 corner-256, E15 far-192, E08/E12 negative statements, chronology P1–P4 | [m3-outer-corner.md](audit-02/m3-outer-corner.md) |
| T1 | Hybrid engine source and reduction; finite degrees 42/63–64/159–160; independent reruns | [t1-engine.md](audit-02/t1-engine.md) |
| T2 | Syvert2 pack: reduction, protocol, quiescence, verifier, operational controls, records | [t2-pack.md](audit-02/t2-pack.md) |
| I | Novelty gate and Claude's own ideas | [audit-02-ideas.md](audit-02-ideas.md) |

Novelty content: the audited claims continue existing models and the
campaign's own records; the full state/IDEAS.md read is recorded in
audit-02-ideas.md. The M1–M3, T1 and T2 reviews used the gate records
only where they bear on the chronology findings.

## Executed checks

Labels: **[E]** executed by the auditors, **[D]** own derivation, **[I]**
inspection. All outputs went to fresh scratch paths. No candidate byte was
changed. **No numerical pack case, no residual degree (43–62, 65–158,
161–319), no bulk run and no remote or Syvert2 access was started.**

| Review | Execution | CPU | Outcome |
|---|---|---:|---|
| M1 | 142 exact-Fraction checks of the final chain (kWx/kWy, annular quadratic at rho=1/2, 3/5, 1, floors, gaps); 40-digit interval evaluation of the literal outer and corner-256 functions; log-grid scan n=320..1e15; symbolic line-maximum check; float PD-T364 cardinal sanity at n=320, 321 | about 4.3 min | All pass. Three non-zero exits were bugs in the auditor's own scripts (a pi>3 variant the records do not claim; 3.6e-15 float rounding at the corner origin; a strict test with pi set equal to its upper bound); reruns passed |
| M2 | 10 scripts (mpmath, sympy): E07 definition and derivation (5)–(21), rational constant -311/71680, Gauss-Legendre samples at 134 points, E06 map, E10/E11 baseline and paired inequality, E07-global512 (30 rational links), E04/E05/halfnear constants | about 65 s | All exit 0. One earlier attempt exited 127 (no `/usr/bin/time`); nothing ran |
| M3 | Interval (200-bit) and exact checks of E14-outer320 at n=320 (F=0.0692>13/500, Gb numerator 195191/2400000), E13 geometry on the closed diamond, E15 at (192, 7/24), E12 at n=256 (corner coefficient 0.167>1/30), E08/E12 obstruction arithmetic | about 6 s | All exit 0. A first `python3 -I` attempt exited 127 and was replaced |
| T1 | Nine engine runs, each once, EXIT 0 observed: hybrid produce 41 (TREE 13/64 S/3 actual/101 nodes), verify of committed primary-41, produce 511 (GRID 30/45 S/0 actual/51 nodes/3 analytic far leaves), verify of committed primary-511, D36 verify of the D38 primaries 42, 63, 64, 159, 160. An independent finite-layer checker written from the theory statements (not importing `checker.py`) over 16 certificates | 52.8 s | Every proof field equals the committed evidence, including on a different toolchain; the independent checker agrees on all 16 |
| T2 | `review_controls_03.py` under Python 3.13.18 and 3.11 in copied trees; own fake-worker controls (SIGCHLD default and ignored, reboot, delete-and-resume, SIGHUP, preflight failure); exact-checker reconstruction of the four committed receipts; `git ls-tree` size inventory | about 15 s plus 6.5 s per controls run | 67 events identical to the recorded receipt on both Pythons; findings PA1, PA2 reproduced |

**Environment difference (disclosed).** The pinned Debian runtime could not
be fetched: the session proxy refuses deb.debian.org. T1 used Ubuntu
libflint 3.1.3-2 and libmpfr 4.2.2-1 (same version strings, rebuilt, all
three hashes differ from the pins), system gmp 6.3, mpfr 4.2.1, glibc
2.39, g++ 13.3 and Python 3.13.18. The original runs used g++ 14.2. The
engine's own freeze check passed on every run. The pinned GMP/glibc>=2.38
claim, the six package hashes, the original toolchain and the actual ZIP
were **not** tested.

## Findings

All severities are the auditors' own. Locations are in the linked reports.

### MAJOR (operational pack; resolve before any Syvert2 release)

- **PA1. A recorded "EXIT0" can be fabricated by an inherited SIGCHLD set to
  ignore.** Exit codes come from Python's `subprocess` in `server.py`,
  `job_worker.py` and the engine's stage supervisor. CPython turns a
  missing child (ECHILD) into return code 0, and an ignored SIGCHLD
  survives `exec`. If `beregning`, a shell or a batch wrapper starts the
  launcher that way, the kernel reaps children and every observed exit
  reads 0. [E] A fake case that exits 7 is recorded with
  `observed_returncode 7` and a first failure under default SIGCHLD, and
  with `observed_returncode 0`, no first failure and a quiescent run under
  ignored SIGCHLD. The per-attempt proof data must still validate, so this
  alone does not admit a false proof, but it defeats the independent EXIT0
  check that the D36 limitation was about. Fix: reset SIGCHLD to default
  at the top of `server.py` and `job_worker.py`, record the inherited
  disposition in preflight, and add a control.
- **PA2. Ordinary events leave only an unspecified manual recovery,** which
  would mean hand-writing `COLLECTION.json` with `quiescent:true`, the very
  attestation the protocol exists to prevent. [E] A changed boot id makes
  collection of a fully quiescent completed campaign refuse permanently
  (`ownership.py`), and admission and resume too. SIGHUP is not handled
  (`server.py` handles SIGINT and SIGTERM only), so a hang-up kills the
  supervisor with the state false while the worker keeps running. A
  recoverable preflight failure (disk floor, hostname, missing tool) makes
  the group unrunnable in that directory, fresh or resumed. Fixes: handle
  SIGHUP and SIGQUIT like SIGTERM and set a parent-death signal in the
  worker; define the recovery for these cases.
- **PA3. Decision for AC and root (not a code defect): stop-on-first-failure
  against 273 open degrees.** The frozen D40 obligation is implemented
  faithfully. One non-certification (plausible in 161–191, where neither
  the n>=192 nor the n>=256 premise applies) stops admissions, up to 39
  in-flight cases become failed attempts that can never be reused, and
  `verify_return.py` is all-or-nothing, so no completed subset can be
  data-validated. Options: keep it, or separate the operational stop from a
  recorded scientific terminal failure that does not halt the campaign.
  Either way, add a partial-return verifier.
- **PA4. The real `job_worker.py` to engine path has never executed.** Every
  control substitutes the fake worker, and the four known-case runs were
  plain engine calls. Untested together: the 2 GiB address-space and 260 s
  CPU limits inherited by the compiler, single-core affinity,
  `LD_LIBRARY_PATH` pointing at the pinned libraries (inherited by the
  compiler; [E] `cc1plus` links libgmp and libmpfr, so it would load the
  pinned versions), and in-worker evidence capture under 40-way
  concurrency. Recommend a preregistered local dress rehearsal of the
  actual ZIP on known degrees, or a recorded decision that `run_small` on
  Syvert2 is that test.

### MAJOR (inherited research-chronology findings; unwaived)

P1–P4 remain exactly as recorded in the E08/E09/E14 records and in
independent-checks-E14-global320.md section P4. The auditors read each
fully and do not waive them:
- **P1** (E09 global384/outer): the first CEhat intuition came before the
  E08-origin, E09-signed and E10 records were fully read.
- **P2** (E09 signed T): a preliminary axis observation came before the
  last fresh search.
- **P3** (E08 origin): the first operator intuition came before four
  E02/E03 records were read.
- **P4** (E14 annular): the requested local inventory was written after the
  first coefficient and sign reasoning.

P1–P3 breach WORKFLOW's "generate candidates only after the gate"; P4
breaches an explicit root instruction. None is BLOCKING, none alleges a
mathematical error, and the auditors re-derived the affected lemmas (for
example the E09 quotient lemma). Original chronology is kept (each
disclosure is in the first published commit; the E14 first-commit
prefixes are unchanged). By substance the M3 review ranks them
P1 > P3 > P4 > P2. **Note for AC:** the E14-wide-signed review ruled a
similar local-inventory order "no violation" while P4 is MAJOR. The stated
difference is the explicit annular task instruction. AC should apply one
rule, and each finding needs an explicit disposition before readiness.

### MINOR (record and wording; none changes a statement or constant)

- **A-1. Stale status text.** Dated adoption appendices still say "global
  onset remains 768 / residual 719" as current: E04-radiusone-defect:234,
  E04-wide-corner1:182, E04-wide-retained-origin:368, the three E03 files,
  E05-cusp-aware-error:357. The E12/E15 header status lines still say
  "adoption pending". The "Status: OPEN" header of E14-assembly320.md is
  the hash-preserved first snapshot. Add a dated pointer to the current
  state without editing pinned text.
- **A-2. Hash labels.** "Hmax461214a5" and "consequence map b6a9db93"
  (E14-assembly320:138-139; E12-corner256:38) are SHA-256 prefixes of the
  review files independent-checks-E07-H.md and E06-H.md, not of the theory
  records. Say so.
- **A-3. Node paragraph source.** E14-assembly320:178-185 uses C-infinity(0)>0
  without naming its source (D08/PD-T271 bound C-infinity(0)>4383/2420) and
  an unnamed form of M-infinity(0,L). The paragraph is redundant, because
  the outer bound already covers nodes at rho=pi.
- **A-4. Incomplete dependency strings** in `checker.py` (lines 28, 33):
  E12 omits the wide relative allowance used at the two axis points
  (E04-assembly640 eq. 4), the D27 norm adapter and D08 Peano; E15 omits
  C08's model loss. These are metadata, not proof gates (SPEC:216-217). Fix
  in prose, not in frozen code.
- **A-5. Domain transfer without a citation.** E12-corner256:94 uses
  E04-assembly640 eq. (4) at n=256 "component-wise n>=32", while E04's own
  theorem is stated for n>=640. Each component is stated for n>=32 (the
  auditors spot-checked D37, E04-wide-retained-origin, E02-paired-outer),
  but no review records the transfer. Add one explicit citation line.
- **A-6. PD-T271 dependency not named** in the PD-N obstructions
  (E08:46, E12-obstruction:66-67): their bound j<1/4 rests on PD-T271
  enclosures.
- **A-7. Runtime library bytes are recorded but never compared with a pin**
  (build.py:8-10,49-56; runtime.py:66). A non-pinned libflint was accepted.
  FLINT/Arb is a declared trusted dependency, so this is a provenance gap,
  not a soundness gap. The committed receipts carry no library identity.
- **A-8. Receipt size depends on path length** (engine.py:154,157): +151 B
  in the auditor's run, and the estimated size at full caps is about
  15.6–15.7 KB against the 16384 B limit, so a long Syvert2 path could
  fail a near-cap case.
- **A-9. Receipts list the E15 dependencies (including PD-T271) for model-free
  degrees,** and the 3/100 is reported among "strict margins" although it
  is a theorem gap against the true corner value (checker.py:31-33,191).
- **A-10. Fresh-run recipe not reproducible in a new cloud session.** The
  runtime lives only in `local-output`, and the Debian mirror is denied
  here. Add snapshot.debian.org locators and archive the pinned packages in
  the pending cold-storage transfer.
- **A-11. Size bound understated by 2,333 B** (COLD_STORAGE.md growth that
  the reviewed size rule counts): the corrected bound is
  9,433,015 + 76,611 = 9,509,626 B, still below 10,000,000 [E].
- **A-12. Pack hygiene.** An out-of-protocol retry is undetectable after
  deleting failed job directories and resuming (require pending to equal
  the previous `never_started`, keep summaries append-only);
  `verify_return` reads members without checking size against the
  inventory, so a decompression bomb causes a memory failure (it fails
  closed; no extraction, so no zip-slip or symlink exposure); the README
  overstates resume utility; `syvert2-delivery.md:28` ("full artifact
  linkage") overstates what the genuine check exercised (`validate_pass`
  only); superseded prose remains at `final-syvert2-preparation.md:126`.

### NOTE

- The symbol kappa means 4*I4/pi^2 (about 0.354) in E10–E14 and a PD-T271
  constant (about 0.9197) in E06; each is defined locally.
- E13's "conditional reduction" is a proved implication with hypotheses
  K(N)>0 and F(N)>0, not a CONDITIONAL status; its gate is proved only at
  N=320.
- Accepted-but-conditional items: E13's gate (N=320 only); E08
  phase-global's all-n consequences (a separately supplied model
  inequality); E06 consequences were conditional on Hmax, which E07
  discharges; everything using j, t0 or C-infinity<9/4 depends on PD-T271;
  E15's physical use needs the D32 chart premise lambda<=S; E08 origin is
  one-sided only, for n>=160.
- The tightest exact margins in the final chain are C4 at 2.6e-6 and Mesh at
  1.8e-5 (M1), E13 geometry at 2.2e-5 (M3), and the half-near minimum
  8.03e-5 against 1/20000. All are valid. The M1 float cardinal sanity
  and the log-grid scan are measurements, not proofs.
- E07's constant -311/71680 is about 24 times weaker than the observed
  supremum of f''' / sin(x/2), and the observed quadratic drop of H is
  about 60 times the proved coefficient. Both are valid and loose. The
  chain needs PD-T271 only for H0>7/25 (margin about 0.03); a certified
  interval quadrature of the one-dimensional H0 integral could replace
  the Arb premise.
- Do not use mpmath's default tanh-sinh quadrature for H at the cusp
  (wrong H(pi) values); Gauss-Legendre is reliable.
- SPLIT in the hybrid engine is proved unreachable dead code. TREE
  certificates carry grid premises they never use. Per-case CPU is
  dominated by compilation and environment-dependent (auditor runs were
  14–24% cheaper than recorded; the review's 28.060015 CPU-s total is exact
  against the committed accounts).
- Residual-degree behavior (static): the producer is a bounded
  depth-first search (depth 18, 2047 nodes, 256 S calls, CPU/wall caps), so
  it cannot loop. Degrees 43–191 use the model-free route (three actual
  corner points, numeric only), 192–255 use three f leaves with forced GRID
  norm, and 256–319 also use the E12 corner.
- Other pack notes: the verifier does not recount native-call caps or check
  hostname (the engine enforces them); `cleanup_killed` can list a pid
  twice; a tiny PID-reuse window exists before each kill; the summary
  `phase` stays "preflight" during dispatch; `cold-storage.json` has no ZIP
  entry (consistent with the pending transfer); the match to the bttb A/B/C
  interfaces is interface-level only and the bttb repository was not
  accessed.

## Verified as claimed

- The residual set [2,319] minus the proved degrees is exactly 43–62,
  65–158, 161–319 (273); the small group is the seven proved degrees;
  disjoint; 280 cases in total [E]. Far-field leaves need n>=192 in both
  decode and verify, the analytic corner needs n>=256, and the floor tiers
  switch at 64/160/512 [I].
- The analytic far leaf fires only for integer n>=192 and normalised phase
  sum in [1/2, 1], which is exactly pi/2<=rho<=pi (the native kernel takes
  alpha/pi); a cell straddling rho=pi/2 is rejected. TREE norm is rejected
  whenever an f leaf is present (four places). The proof size cap is strict
  [I, D].
- All pack caps listed in the handoff are enforced in code, not only in
  prose; failed cases cannot be retried; the verifier demands the full
  evidence inventory; exit codes come from `waitpid` (subject to PA1)
  [I].
- Runs 01 and 02 are preserved as failures (observed exit 1, `no_rerun`,
  harness hashes match); control 03's 67 events reproduce; the four
  committed receipts reconstruct under the exact checker; the evidence
  index is 336 entries / 27,665 B, every entry rehashes and none is
  >=16 KiB; 14 of the 22 genuine-data pins are checkable here and all
  match [E].

## Not independently re-derived or not tested

Mathematics (read, or checked numerically only): the PD-T364/PD-T101
framework (numerical check at n=5, 6, 320, 321); E01-F1/F2 floor proofs
and the E02 band extension; the E09/E14-wide signed-T cores; D37's Erow
and Rmesh; the E03/E04 retained rows; D13's mesh bound; E08's CEphi
operator bounds (rows, outer cells, mesh, log, collisions) and origin
proof; E13's derivation beyond its base coefficients; D08 squared-Peano
and D27 adapter; the model-loss inequality; C04, C08 and N1 scalar facts;
PD-T271's t4-01/t4-02 proofs and Arb enclosures; D10/D24/D37 decomposition
of C-infinity; C06 J identities (numerically consistent to 1e-16); finite-n
operator inputs of E01/E02/E03/E08. The full proofs of D32, D29, D14, D19,
E12 and E15 were checked for statements, domains and interfaces, with the
arithmetic re-run. The C13-era upstream cores listed in audit-01 remain
open for the final audit.

Execution and artifacts: the actual ZIP (25,104,521 B) and `local-output/`;
the six .deb files and the GLIBC_2.38 claim; the pinned Debian runtime and
g++ 14.2; correctness of the native Arb kernels (trusted); kill, cap and
timeout failure paths; the real worker-to-engine path; any residual
degree, bulk, Syvert2 or remote run; controls 01/02 (historical, target
the removed scanner); `genuine_data_check.py` (needs the absent
local-output; 14 of 22 pins were checked by hand); the bttb repository.

## Required response and stage

Codex should answer PA1–PA4 with a code change, a recorded decision or a
reasoned dispute, and answer A-1…A-12 as record-only fixes in
`response-02.md`. P1–P4 need AC's explicit disposition and are not for
Codex to waive. Codex should then use [audit-02-ideas.md](audit-02-ideas.md)
for the next research steps. Handoff 11 specifies the work. Per AC the topic
and PR27 stay at stage **WORK**. A source change to the pack changes its
identity: it needs a rebuilt ZIP with a new recorded identity, a focused
re-review, and no claim that it is the original `8274249f…` artifact. A
later final audit must cover the open items above and any material change.
Final IDs, registry application and readiness stay deferred. Only AC
merges.

2026-11-07 · Claude orchestrator `claude-sonnet-5-5`; audit work by six
Claude Opus 5.5 subagents (instructed xhigh) · rules at be9a831 = 1b6aa31.
