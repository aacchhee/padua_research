# INTERIM Claude audit-01: Padua argmax bridge (handoff 07)

**This is an INTERIM audit.** It is not a final approval, a readiness check
or a PR-stage promotion. AC directed (handoff 07) that the topic and PR27
stay at stage **WORK** and that Codex does the next development. The
companion deliverable with Claude's own ideas is
[audit-01-ideas.md](audit-01-ideas.md).

## Decision

**I found no BLOCKING or MAJOR finding within the audited scope. The
mathematics of the half-million theorem reconstructs at every integer
n>=500000. The finite range 2–40 meets the computer-proof requirements,
and an independent rerun of n37 accepted. The C03 known-n32 checker result
reproduces on a different software stack.** Nine MINOR record findings
(F1–F9) and several NOTEs go back to Codex. None of them changes a
statement, estimate, threshold or status. Stage stays WORK as instructed.

| Claim (current records) | Interim disposition |
|---|---|
| Exact two-corner global argmax for every integer n>=500000 ([C13 assembly](theory/C13-onset-budget.md)) | Supported. Assembly, cover and all three comparisons reconstructed; see the residual-scope paragraph below |
| Near representation <1/1000; near excess <383/12500; near noncorner deficit >1/32 | Supported; arithmetic exact; every lower-domain recheck verified |
| Corner value Lambda_c>A_n²+d(n)-1/1000; actual corner loss >=r2/6 | Supported; margin p(131/10)-1/6=961/192000 |
| Far representation E_far(n0)<290652925961/525000000000; far deficit >1/2000 | Supported; exact slack 382900852945861/466667600000000000 |
| Finite 33–40 exact computer proof; 2–32 inherited | Supported; n37 independently replayed ACCEPTED |
| C03 mode0 known-n32 PASS 364/364, ~3.08x subprocess speedup | Supported as a single known-case measurement; reproduced |
| C12/C15 guarded whole-box S-upper and the C11 partial sums | No violation in adversarial fuzzing; scope wording honest |
| Gap 41–499999, PD-T099 all-degree, original tight C1 | Remain **OPEN**. Not touched by this audit |

**Residual scope.** The auditors verified every degree-dependent step that
C13 rechecks below 10^6, all of the exact arithmetic, the monotonicity, the
geometry and the assembly logic. For the **n-independent cores** of the
upstream proofs they read the proofs and spot-checked them numerically,
but did not fully re-derive them. These cores are listed under
[Not independently re-derived](#not-independently-re-derived). The
interim verdict depends on them as written, together with their accepted
supplementary Codex/Astra reviews. The later final audit must close them,
by re-derivation or by a targeted check.

## Identity, rules and audited candidate

- **Auditor:** Claude, configured and last-served model `claude-opus-5-5`
  (from session metadata). Handoff 07 requested Opus 5.5 xhigh. The session
  metadata reports `effort_level: high`, and I cannot verify xhigh from
  inside the session. This is a disclosure, not a silent substitution:
  WORKFLOW allows Opus 5.5 high or xhigh for a mathematical audit, and the
  handoff asked for xhigh. Six Claude subagents ran under this orchestrator.
  Each was instructed at Opus 5.5 xhigh; their effective effort is not
  exposed. Every one is distinct from the Codex developers (gpt-6-astra,
  gpt-6.1-sol).
- **Role:** interim independent auditor and independent idea proposer, and
  orchestrator for Git and the PR body in this step only. Subagents made no
  Git or repository changes.
- **Rules:** AGENTS.md, agents/WORKFLOW.md and agents/claude/CLAUDE_ROLES.md
  were read first at main `be9a8318150204711d5446d2ea26284cf1ed0819`. They
  are byte-identical at the audited head (`git diff` between the two commits
  is empty for AGENTS.md, agents/ and templates/).
- **Candidate:** branch `codex/padua-argmax-bridge-20261105` at
  `02beaef2b22f8232286713dab0a1b7c95582ce13`, which is science input
  `99c6b6f5ef75cbbd17e0127a0210c86eb2eb78d0` plus the handoff-only commit.
  The remote head was rechecked before writing and was unchanged. The main
  base is `76ba4214b100c86a44941f5e9a662ce9ce48efb8`.
- **This is audit round 1 for the topic.** Under WORKFLOW, MINOR findings
  therefore go back to the developer rather than being fixed in place.

Audited file identities (SHA-256) match handoff 07 and the focused review:

| File | SHA-256 |
|---|---|
| theory/C13-onset-budget.md | `bc975d53831052f536604dcc2cc9d2552e0f79ba7826a2453708d9ba34ef5ea0` |
| theory/C13-near-representation.md | `fa861e5908cad7ad983aa7c442badc1d59ef800af295487a897f4d787cd8e74b` |
| theory/C13-near-comparison.md | `44f412f3adaa7ca3c21175469d957418b16d479a5156328f48775ac951c0096c` |
| theory/C13-corner-value-lower.md | `6b4bd8029f593ff59d03db4c053487070b36eeb79e15da6c77a74b70448d50a0` |
| theory/C13-corner-comparison.md | `b951104ecd48154b9bde6bad2a90dfa26f6c7ce310563a4234df5069c9881bc2` |
| theory/C13-far-representation.md | `11b27272af82cc3c800008b2eee38eba3f700c3719917ae15b15727339bdd30a` |
| theory/C13-far-comparison.md | `e34aec6ac187dc77b734266514714fdedbe080c699c19d1e9ae5289353cea61b` |
| independent-checks-C13-onset.md | `e57cd31b2a4f1b987a634c0c9aee539357cd1edb232030ff5fea573a8a8c18e8` |
| theory/native-finite-range.md | `0501cf54cd94ed58ab32632a667b04007d378fc67b4dd7881a78c3d16c683595` |
| independent-checks-C03-cheap-n32.md | `1996b1375077eed5fe392a6cbeb4db1e740efa562e134c44fcb2d1ff2ffbb5a0` |
| code/cheap_rows_C12_box/box.cpp | `91700bd49211d97bf3b61e278936cdcb45f582e6673e18978ef59cb524340949` (matched) |
| code/cheap_rows_C15_global/global.cpp | `7f50e06624e6fa1a01a98ae0fe1f9c166b1f10174d9042c11bc19f5b527c4b6c` (matched) |

## Coverage and method

Five scoped audit reviews ran in parallel, plus a novelty gate and ideas
review. All reconstructed the claims themselves before reading the Codex/Astra
supplementary reports. Their full reports are committed as authored review
records under [audit-01/](audit-01/), and their small scripts under
[audit-01/code/](audit-01/code/).

| Review | Scope | Report |
|---|---|---|
| Near | C13 near representation and comparison; N1-06…17, C04, C05 finite-h, C02 dense band, as used | [near-review.md](audit-01/near-review.md) |
| Corner | C13 corner value lower and comparison; C07, C08 corner margin, C05 quarter-angle, PD-T159/269/270 | [corner-review.md](audit-01/corner-review.md) |
| Far | C13 far representation and comparison; C06 compact error, N1-01…08, all C08 far components | [far-review.md](audit-01/far-review.md) |
| Assembly and finite | C13 global assembly, PD-T364 cover, λ=S−Δ, equality set; native 33–40 reduction, checker, evidence; n37 rerun | [assembly-review.md](audit-01/assembly-review.md) |
| Cheap certifier | C03 n32 replay, predicates and identity closure; C02-row, C09, C08 row-box, C14, C12/C15 sources; scope wording | [cheap-review.md](audit-01/cheap-review.md) |
| Ideas and novelty gate | Full state/IDEAS.md and obstruction tables; proposals | [audit-01-ideas.md](audit-01-ideas.md) |

Novelty content in the audited claims: C13 is a quantitative lower-domain
re-estimate of existing fixed models and is not a new mechanism. Its gate
record was inspected. The full state/IDEAS.md read for the ideas
deliverable is recorded in audit-01-ideas.md.

## Executed checks

Labels: **[E]** executed by the auditors here, **[D]** own derivation,
**[I]** inspection. All outputs went to fresh scratch paths outside the
repository. No candidate byte was changed and no producer, new degree or
rescue retry was launched. Total execution was about 1,650 CPU-s.

| ID | Command / check | CPU | Exit | Outcome |
|---|---|---:|---:|---|
| X1 | Exact Fraction recomputation of C13 (12), (18), (24), (25), (26), p(131/10), d(n0) and the near defect margin (root `root_scalars.py`, near `eta0.py`/`misc.py`, far `f1_fractions.py`, corner `exact_checks.py` with mpmath interval checks) | <2 | 0 | All recorded rationals reproduced exactly; 50/50 corner checks |
| X2 | Interval check of 1−cos(1/4)>=191/6144, (2k/π)²>9/10, log 10>23/10, log 2<7/10, A_n<=L+2 | <1 | 0 | PASS |
| X3 | Float sanity of cover, λ=S−Δ at all physical odd charts, node ρ=π and corner equality set, n=2..8 (`cover_sanity.py`); measurement only | <1 | 0 after a fix to the auditor's own non-physical test point | Consistent; |λ−(S−Δ)|<=9e-15 |
| X4 | `g++ -O3 -std=c++17 …/native_checker/kernel.cpp -lgmpxx -lgmp` (g++ 13.3, GMP 6.3.0), then `python3 …/native_checker/check.py topics/padua-argmax-bridge-20261105/evidence/n37.json.gz --binary <fresh>/kernel --output <fresh>/replay-n37.json` | 833.6 | 0 | **ACCEPTED**; complete partition; 316 bound / 2 corner / 317 splits, matching the receipt. Certificate SHA matched; binary differs from the recorded one (different toolchain) |
| X5 | Native kernel negative controls at n=2,3,4: incomplete frontier and duplicate path | <5 | 1 (expected) | Rejected as required |
| X6 | C03 mode0 on the immutable n32 candidate via unchanged `check_r8.check` and an auditor driver; g++ 13.3, FLINT 3.0.1, Python 3.13 | 33.7 | 0 | **364/364 accepted**, 333 native calls; all 12 counters and the three minimum strict margins equal the record |
| X7 | Same harness with the C01/C02 kernel | 25.9 | 0 | Not accepted: 76 failed (48 far, 28 corner); first failure 0/0101 at the recorded margin |
| X8 | Same harness with the old hybrid v3 kernel | 131.4 | 0 | Accepted; same-host ratio 3.91x, so the claimed 3.08x is not overstated |
| X9 | Ratio-enclosure fuzz, three variants, k 2–513, intervals across poles and guards (mpmath 80 dps) | ~36 | 0 | 191,904 samples, 0 violations |
| X10 | C12/C15 whole-box fuzz against a 512-bit reference, n<=32, including forced fault probes | 518.8 | 0 | 349 boxes, 3,839 points, 0 violations; every fault probe that could fire charged the whole row |
| X11 | C11 partial cotangent sums, n<=4096 | small | 0 | 919 points, 0 violations |
| X12 | Float measurements, not premises: corner L_n−A_n, B_n slack, retained pairs at 5e5; λ−Λ_c≈−7r2 at n=2000/2001; far b_full−b_c, E_64, K_δ, Φ0'' on grids; n=50000 row and mesh agreement | small | 0 | All inside the stated bounds; the true far margin is much larger than the proof's 8.2e-4 slack |

n40 was not replayed because it would have exceeded the per-review cap of
about 1,367 CPU-s; it is not claimed. The author wrappers were not rerun
unchanged: they write to `local-output/`, refuse because the receipt
exists, and need the pinned FLINT 3.1.3. X6–X8 use the unchanged
acceptance function with an auditor driver.

## Independent reconstruction: main points

- **Assembly [D].** Every mesh rectangle has exactly one odd diagonal pair,
  and its normalized L1 distances sum to 2. Both vertices are admissible
  centres, so the closer one gives a physical chart with ρ<=π. Δ depends
  only on the physical point, so λ=S−Δ with Δ>=0 holds at every chart, and
  bounding S suffices in the far case. A node has ρ=π for every odd chart.
  The only odd corner centres are (n,m), plus (0,m) for even n or (n,0)
  for odd n. All their physical phases are inward, and the ρ<=1/2 part is
  exactly the patch A,B>=0, A+B<=1/2. Every other odd centre has an interior
  coordinate and receives C02's >1/16 floor (scope n>=4096, all parities,
  edges and the exceptional mode). There is no assumed maximum and no
  circularity. The equality set and reflection symmetry are correct.
- **Near [D,E].** N1-06's own theorem domain is n>=804248. C13 correctly
  uses only its finite-sum identities, which need K_s>=R (X>=129). The
  403/n sinc-argument refinement is genuinely needed: the old 4rh bound
  gives 1.024e-3>1/1000 at n0. The 11270/n term is 45000·(1/4)+40·(1/2).
  The rest error is 5+10+50+10=75 per phase, charged twice to give 200.
  (16) is exactly C04 eq. (3), which depends on phase only. The N1-17
  identity has no degree floor. The tight margins are
  A(131/10)−1225/144−32/9−19/4=0.0456 and log n0−131/10≈0.022.
- **Corner [D,E].** PD-T270 gives |L_n−A_n|<=1/(4n²) for every n>=1, both
  parities. B_n>=A_n²−ε follows, and Λ_c=B_n+Δ_corner matches PD-T159
  exactly with no double count. Δ_corner>d(n) needs only n>=40 (PD-T269) and
  the C07 unordered-pair nonnegativity for n>=2. 28000=4·(2400+4600). C08's
  n>=10^6 is used only for its rounding to >1/2, which C13 does not use.
  Every n>=10^6 wording on the C07/C05 path holds at n0. H2(n0)=14.82, and
  the harmless-term total of 6.1e-6 decreases with n even though H2 grows.
- **Far [D,E].** All seven terms of (23) are exactly C06's complete error
  decomposition (18). None is omitted, and Q is charged once. Each upstream
  validity condition holds at n0: n>=ceil(12800π) for N1-06, m>=5050π,
  n>=512, m>6400π. (25) re-derives from the C08 identity for b_full−b_c and
  the split C_far=E_64+K_δ. The −3L term is separated before π²<10 is used,
  so every inequality points the right way. u>=191/6144 is the alternating
  Taylor bound at x=1/4. a>=0 on the whole far diamond.

## Findings

All findings are record findings. None changes a statement, estimate,
parameter, threshold or status.

- **F1 MINOR: stale status in all seven C13 records.** Each still says the
  focused F1/F2 check is pending. Locations: C13-onset-budget.md:33-35, :50,
  :122-123; near-representation:26; near-comparison:34; corner-value-lower:28;
  corner-comparison:30; far-representation:32; far-comparison:25.
  independent-checks-C13-onset.md:302-367 records ACCEPTED for exactly these
  hashes. Because that review pins the bytes, update the status through a
  dated addendum or a re-pinned focused-review note rather than a silent
  edit.
- **F2 MINOR: degree-domain lemma scope and log n0<14.** The lemma covers
  only (c log n+d)/n^j with c,d>0. Several terms actually used are outside
  that form:
  - near: c=0 terms, L(δ+h/2)/(6m), G(δ+h);
  - corner: (L+2)²/n, (L+2)/(2n²), m²/n³, m·H2/n^j;
  - far: 7082790000/n², (2/63)(1+1/n).
  The auditors checked every one of these and each decreases (or is
  handled as stated). Separately, "log10>23/10 and log2<7/10 give
  log n0<14" is miscited: the upper bound needs log 10<2303/1000 or
  e^14>n0. The conclusion is true. Widen the lemma and fix the citation in
  all seven files.
- **F3 MINOR: incomplete "every numerical floor check" list.**
  C13-corner-comparison.md:70-83 says it lists every check but omits five:
  τ²<101/100; the (21) bracket <71/10; |X|,|T_B|<=π/2+1/(4n)<8/5;
  sin T0>=(99/100)T0; and C05 section 1's m/(2πn)<1/6 and |T|<=3Z/2. Each
  holds for n>=~3000. Complete the list or soften the wording.
- **F4 MINOR: traceability of imported constants.** Make each of these
  explicit:
  - near: (16) is C04 eq. (3); the 11270 derivation; "old n>900000
    rounding" is C05-model (11).
  - far: inline the phase-only proof of u>=191/6144 (it sits in
    C08-far-model-comparison.md:268-274, a file scoped to n>=10^6); list
    the N1-01/02/04/05 conditions (n>=2, 2<=R<=n) and the m>6400π
    replacement for C06:278's "because n>=10^6"; (2k/π)²>9/10 follows from
    N1-16's k>3/2 and π²<10, not from C08.
  - corner: (19) also needs L_n>=A_n−1/(4n²)>0 and A_n<=L+2; and the
    comparison's use of Λ_c>=A_n²−ε relies on Δ_corner>=0 (C07 pairing).
- **F5 MINOR: non-durable preservation and postcheck artifacts.** Two
  artifacts exist only at /tmp paths on the Codex host and are in no Git
  ref or cold-storage record:
  - the frozen original C13 proof (`6cc04de4…`, 483 lines) and its
    extraction script (C13-onset-budget.md:107-110; attempts/C13-onset.md:80-87, 114-118);
  - the C03 exact-margin postcheck `/tmp/c03-full-postcheck.json` and its
    script (independent-checks-C03-cheap-n32.md:144).

  No claim depends on them: the split mathematics is complete, and X6
  reproduces every postcheck number. However, the byte-preservation and
  postcheck claims cannot be repeated. Archive both with hashes in the
  pending cold-storage transfer, or record the limitation once in LOG and
  the checks.
- **F6 MINOR:** independent-checks-C03-cheap-n32.md:1-12 does not name the
  executing agent, model or effort, which WORKFLOW requires for execution
  records.
- **F7 MINOR: identity-closure completeness is overstated.**
  "source_runtime_checks_complete" and "254 closure entries" do not hash the
  Python standard library, including `fractions.py`, which performs the
  exact acceptance arithmetic (replay.py `project_modules`;
  build_snapshot_r9.py:82-94). Scope the claim. X6 on a different Python
  mitigates this.
- **F8 MINOR:** gates.md:20 puts "46.09 total CPU" next to "3.08x
  subprocess". Name the measure on both numbers wherever they appear
  together (gates, report, results, PR body).
- **F9 MINOR: C12/C15 diagnostics in out[].** `c12_box` and `c15_global`
  return the S upper and non-additive diagnostics (relax, freeze, cube,
  tail, rho) in one `out[]` array. In C15 the freeze term is already
  included in out[0], so a future integrator could double-count it.
  Document this in the source contract or API notes before any integration.
  No current result is affected.

NOTEs, no action required:
- N1: C13-onset-budget.md:90 "every center parity" means both degree
  parities and edge centres; :92 "odd endpoint centers" means odd corner
  centres. Stating at :86-88 and in PD-T364:134 that both rectangle
  vertices are admissible centres would make it obvious that the chart is
  physical.
- N2: C07-positive-deformation uses τ=n/m, while C07-million, C05 and C13
  use τ=m/n. They are consistent, but the notation could mislead.
- N3: near-representation:123 cites "m/n<=2" for N1-11; its tail step uses
  m/n<=9/8. Harmless.
- N4: native-finite-range.md:76-79 gives portable replay commands only for
  n33/n34; 35–40 are in the separate check records. The lost 33–36 shell
  exit statuses are honestly disclosed, and acceptance rests on persisted
  receipts. The finite reduction is PD-T210 (PROVED), cited correctly, not
  the OPEN phase-checker-reduction.md.
- N5: the 3.08x figure is one run on unrecorded hosts. Variants 1 and 2 are
  unreleased and not fully replayed. C12/C15 cover the first-quadrant
  triangle only. "Fixed work" is per ratio evaluation; the per-box O(n²)
  board and O(n³) profile remain.
- N6: the tightest margins are the far slack 8.2e-4 (3.2e-4 above 1/2000),
  the corner p−1/6=0.005 and the near defect 61/100000 above 1/32. About
  0.17 of E_far does not depend on n (Q=0.14 under π>3, true value about
  0.123, plus 2/63). The measured true far margin is much larger, so the
  thin slack is an artifact of the error allocation. That fact drives
  proposal P1 in audit-01-ideas.md.
- N7: the upstream C02, C04, C05, C07 and C08 records still carry
  "independent review required" status lines. They have accepted
  supplementary reviews; the formal Claude audit covers them only as stated
  below.

## Not independently re-derived

These n-independent upstream cores were read and, where noted, checked
numerically, but not re-derived. The verdict depends on them as written,
together with their accepted supplementary reviews:
- N1-13's variation constants and N1-14; N1-16's 2(L+5) special-row
  bound;
- C05's derivative majorant (6)/(7), its counting sums and positive-class
  constants, and its strip/outer cancellation algebra; the E_rest
  single-charging was checked by structured inspection only;
- C06 §§1-3 J-identity and variation constants; N1-07 §§2-3 and N1-06 (12)
  (numerically consistent); N1-01/03/04 proofs (statements only);
- C04-near-01's Φ0''<=12 (numerical: peak 5.57); C03 slope; C01;
  PD-T269's cotangent partial fraction; PD-T270's midpoint and harmonic
  proof (read, and numerically consistent);
- the PD-T101/185/228 kernel and C02 four-copy normalization (supported by
  the X3 and X12 agreement);
- C02-row, C09 and C08 row-box analytic constants (statements read);
- the original build closure, raw cold-storage artifacts, n>32 whole
  boxes, and the C10 controller.

## Required response and stage

Codex should answer F1–F9 in `response-01.md`. These are MINOR record
fixes, and none needs a new mathematical argument. Per AC's handoff 07
instruction, the topic and PR27 stay at stage **WORK**. Codex resumes
development under [handoff 08](handoffs/08-work.md) using the prioritized
plan in [audit-01-ideas.md](audit-01-ideas.md). A later final audit must
cover the open items above and any material change. Final IDs, the
registry application and readiness remain pending, and only AC merges.

2026-11-06 · Claude, `claude-opus-5-5` (session metadata effort `high`;
xhigh requested) · rules at be9a831 = 02beaef (identical).
