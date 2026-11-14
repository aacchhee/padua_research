# Claude audit-04: onset 512, elementary constants, independent arithmetic and new evidence (handoff 30)

Companion record for the two revised manuscripts and their agreement:
[audit-04-manuscripts.md](audit-04-manuscripts.md). Review reports, auditor scripts
and the page index: [audit-04/](audit-04/). This is audit round 4 of the topic,
after [audit-03](audit-03.md) and its [response](response-03.md). It is **not** a
readiness decision, waives nothing, and PR 27 stays a draft. Only AC merges.

## Decision

**Mathematics: ACCEPTED.** J01 (the two gates for the analytic tail from n >= 512)
and J02 (the elementary constants that replace PD-T271) are PROVED at their stated
scopes; I found no BLOCKING finding anywhere. The independent-arithmetic route
(I25/J03) is accepted at its written scope for degrees 41..511 on the data
available. The E-01..E-04 repair of the compact verifier is accepted.

**Evidence for the new degrees 320..510: NOT accepted by this audit yet.** One
MAJOR finding (E4-01) in the reader for the new return, and three off-Git
payloads were not supplied, so the actual 320..510 return, the I25 bundle and
the trusted package were not examined. See the limits below.

**Manuscripts:** the paper is mathematically accepted and needs minor revisions of
exposition; the companion's mathematics is sound but its teaching needs revision
in several places, including one regression. No pedagogical or notational finding
is a mathematical error. Details in [audit-04-manuscripts.md](audit-04-manuscripts.md).

Because MAJOR findings are open (one evidence-reader defect and several
manuscript-clarity items), the stage returns to **WORK** for a Codex response.

| Verdict | Result |
|---|---|
| 1. Mathematics and evidence | **Accepted** for J01, J02, I25 (41..511, available data), verifier repair. **Not yet accepted** for the 320..510 return (E4-01, files not supplied) |
| 2. Journal paper (51 pp) | **Mathematics accepted; exposition: minor revisions.** Two MAJOR groups of local edits (symbols used before definition; named tools only named) |
| 3. Companion (147 pp) | **Mathematics sound; pedagogy: accept after revision**, with one regression (C4B-01) and several teaching MAJORs |
| 4. Agreement | **Agrees.** Source baseline 24a98db passes (19 statements, 85 numbered environments carrying 86 equation numbers, 116 labels); paired silent mutations fail as required |

## Identity, rules and disclosures

- **Models.** AC's prompt named Claude Opus 5.5 xhigh. The session model is
  Sonnet 5.5 (switched with `/model`), so the orchestrator ran as
  `claude-sonnet-5-5` and derived no mathematics. All audit work was done by
  **eleven Claude Opus 5.5 subagents instructed at xhigh** (effective effort not
  exposed): J01, J02, J03, E4, P4, C4A, C4B, C4C, C4D, B4, N4. All are distinct from
  the Codex developers and reviewers.
- **Rules.** Read at be9a831; AGENTS.md, agents/ and templates/ are byte-identical
  at the audited head.
- **Candidate.** `codex/padua-argmax-bridge-20261105` at
  `70a50d7b2a72a30fd7a2af3b2ead54ae14470bf9`. The handoff names input head
  `f4c6229871a494b1b859d3140e81e9eb48b6b56a`; they differ only in handoff and
  brief files (the reviewers verified that the audited files are identical). The
  manuscript TeX/Bib freeze is `24a98db4c3c4c4d0eede2e3929532956df87911b`; no
  `.tex` or `.bib` file changed since. Base `f70a260e5b5f9a01209dc8a05faabdcf8db1feeb`.
- **Environment.** No Syvert or remote access. The proxy refuses deb.debian.org
  (HTTP 403), so the pinned Debian packages were not available; a package-less
  adapter was used for the compact verifier (136 reads of 19 header files not
  byte-checked, as in audit-03). Builds used TeX Live 2023 (Debian), so PDF bytes
  differ from the recorded ones.
- **Data actually available.** The original Syvert return (36,045,486 B, sha256
  `b00fd57f…`, supplied by AC in the previous round). **Not supplied despite two
  requests:** `i25-evidence-20261108T112304Z.zip` (2,843,611 B),
  `onset512-return-20261108.zip` (81,602,992 B), `padua30.zip` (25,111,335 B), the
  small certificates ZIP, the essential inventory and the review ZIP.

## Coverage

| Review | Scope | Report |
|---|---|---|
| J01 | The two gates, radius-one polynomial, selected-pair floor, seams, corners, integration of 2..40 / 41..511 / >=512 | [j01-gates.md](audit-04/j01-gates.md) |
| J02 | Elementary constants, F03 identities support, H04 majorant, dispositions of audit-03 record findings | [j02-constants.md](audit-04/j02-constants.md) |
| J03 | I25 independent arithmetic: sources, trust base, completed run record, reruns, corruption controls | [j03-i25.md](audit-04/j03-i25.md) |
| E4 | New return reader, E-01..E-04 repair, I25 outer accounting, deposit and custody | [e4-evidence.md](audit-04/e4-evidence.md) |
| P4 | 51-page paper, referee | [p4-paper.md](audit-04/p4-paper.md) |
| C4A–C4D | 147-page companion, four readers (every line of main.tex and the six sections) | [c4a](audit-04/c4a-companion.md), [c4b](audit-04/c4b-companion.md), [c4c](audit-04/c4c-companion.md), [c4d](audit-04/c4d-companion.md) |
| B4 | Fresh builds, correspondence helper, mutation test, bibliography, evidence index | [b4-build.md](audit-04/b4-build.md) |
| N4 | Notation, first use of symbols and named tools | [n4-notation.md](audit-04/n4-notation.md) |

## Executed checks

Labels: [E] executed by the auditors, [D] own derivation, [I] inspection only. All
outputs went to fresh scratch paths outside the repository. No native degree
campaign, no archive code and no remote computation were run.

| Review | What ran | CPU | Result |
|---|---|---:|---|
| J01 | Frozen analytic checker from a byte copy; own exact evaluator written from the J01 definitions (different pi formula, log reduction, trig bounds); symbolic check of square completion and vertex identities; exact slacks | about 8 s, all exit 0 | Every receipt interval reproduced. Slacks: 41/1000 − max P(512) = 2.14e-4; −1/7 − P(512)(1/2) = 2.13e-4; G(512,1) − 1/2 = 0.0343; G(192,pi/2) − 3/100 = 0.0683; F_h(295) − 1/20 > 0 while F_h(294) < 1/20 |
| J02 | Developer `check.py` from a copy (exit 0); own exact bracket computation (integer dyadic intervals, no floating point, different series: Hutton for pi, own gamma bracket, integral-test zeta bounds, kappa at K = 14); cross-check with mpmath; F03 identities at n = 2..12, 15, 16, 20, 21, 31, 32 | about 10 s | 44/44 certified checks; kappa in [0.91971006, 0.91971018] (> 9/10), j in [0.1435417, 0.1435423] (> 23/250), t0 = 0.44127120 (< 221/500), C* in [1.8461602, 1.8461609] (< 4629/2500), C_inf-bound 2.22146 (< 9/4); direct quadrature kappa = 0.91971011838849253510 |
| J03 | Reviewed `run.py` unchanged on 41, 63, 64, 159, 160, 192, 199, 238, 255, 256, 511 (both passes); own 31 corruption controls; independent 256-bit Arb reimplementation at 41, 199, 511; analytic-far leaves forced numerical at 6 degrees; 612 polygon-maximum cases | about 4.1 min | 22/22 accepted; 31 arithmetic controls and 27/27 developer corruptions pass; all 154 vertex values and 6 corner values lie inside I25's intervals (widths <= 3.9e-12, margins >= 1e8 larger); forced-numerical far leaves reject, so far-192 is genuinely needed |
| E4 | `verify_compact` repaired, three runs on the old return incl. `--expect-plan all`; 30 focused controls; 21 own rehashed corruptions; 13 synthetic reader controls and a fail-open probe; I25 outer accounting; snapshot reproduction; evidence index; size bound | about 103 s | Repair accepted; **reader fails open under `python -O`** (E4-01); snapshot a433c7d reproduced byte for byte; size bound reproduces |
| B4 | Two fresh builds; correspondence helper in default, archival and artifact modes; own parser on the fresh `.aux`; 7 paired-mutation tests; bibliography | under 2 min | Both build with 0 errors; helper PASS; every paired silent mutation fails the 24a98db baseline while pairwise comparison passes |
| P4, C4A–C4D, N4 | Re-derivation of every added or changed derivation (hand, sympy, mpmath, exact Fractions); the n = 2 certificate; odd-centre cover n = 2..8; gate and corner-256 arithmetic; notation and first-use scripts | under 8 min total | No mathematical error found; all consequential constants reproduce |

## Dependency and trust conclusion

- **The analytic tail from 512 has no finite-certificate premise and no
  computational premise.** The only computer-assisted inputs of the tail are exact
  rational checks (`onset512_analytic/check.py`, reproduced independently by J01 and
  J02), whose trust is Python `Fraction` arithmetic. PD-T271, the Arb enclosure, the
  annulus, the outer-geometry block and E15's majorant are not consumed anywhere
  (a grep of both texts and the theory records finds only software-name mentions and
  historical text). J02's direction check: each constant is consumed in the
  direction its proof needs.
- **Finite coverage.** Bernstein completion 2..40, phase certificates 41..511 (far-192
  and corner-256 leaves with their own guards), analytic tail from 512. The partition
  is exact.
- **The I25 route** recertifies each stored tree for 41..511 with its own bounds,
  under the explicit trust base (Python/Fraction, guarded NumPy int64, IEEE binary64
  with round to nearest and gradual underflow) and the named analytic premises. It
  replaces the evaluator theorems behind the old vertex bounds (D23, C02-row, N5, C06;
  D06 and C11), the native corner lower bound and norm, and the Arb/FLINT/MPFR/GMP/
  compiler stack as numerical trust. It does **not** validate stored native endpoints
  (`all_native_endpoints_validated: false`; exactly one stored S upper per certificate,
  always at key (0,1) where S = 1 exactly, fails the new <= stored test) and it leaves
  as premises: the kernel and cardinal-reflection identities, folding and chart cover,
  positive interpolation with Bernstein's inequality, the selected-pair floors, squared
  Peano, corner-256 and far-192 with the J02 constants, and the IEEE model.
  Audit-03 G-1 is therefore replaced for these witnesses, as response-03 states.
- **Not yet established:** the same for degrees 320..510 on actual data (see limits).

## Findings: mathematics and evidence

IDs are the reviewers' own and are unique (prefixes J1-, J2-, J3-, E4-). Locations,
reasons and fixes are in the linked reports.

### MAJOR

- **E4-01. The reader for the new 320..510 return fails open under Python's
  optimization flag.** `code/local_onset512_campaign/return_bundle.py` performs every
  check with 47 `assert` statements (lines 139–222) and then prints "pairs 191,
  proofs 382" unconditionally (line 223). The documented command is `python3 -B`
  without `-E` (local-onset512-summary.md, the deposit README, the ZIP's README.txt).
  With `PYTHONOPTIMIZE=1` or `-O` the reviewer fed it a forged 26,529-byte ZIP with
  zero certificates and it exited 0 and printed acceptance; normal mode rejects it at
  line 166. Fix: replace the asserts by raised errors, refuse to run under
  optimization, compute the printed counts from verified data, document `-E`, apply the
  same to `runner.pins()` and the asserts in `RECHECK-SMALL-BUNDLE.md`, then re-review
  and rerun on the actual ZIP. This refutes no recorded result: the distinct reviewer's
  own controls were rejected in-process, so asserts were active in that run.

### MINOR

- **J1-02** three justifications left implicit in the proofs of Cor 4.6 and Cor 4.7
  (the replacement of 𝔧 by j* in U, that d_β is decreasing and why positivity of
  ℓx − ℓy needs it, the replacements t0 → t*, the bound A ≥ Θ cos h and evaluation at
  h1); one clause each, mirrored in the companion.
- **J2-01** log π > 11/10 is used (J_0 > 1/π; 𝔨 + Q < 0) but missing from the paper's
  input list. **J2-03** neither text says the J01 base values and the J02 K = 3 outputs
  come from the exact-rational `check.py`. **J2-09** the 12-digit kappa, b and c in the
  abstract and introduction no longer have a source in the paper; label them numerical
  values not used in any proof.
- **E4-02** the reader's trusted runtime manifest is anchored only to the archive's own
  claim (no external pin of `5b89fa66`/`da63280a`) and the checker runs before the pins
  authenticate it, the ordering E-01 fixed in `verify_compact`. **E4-03** the reader lacks
  the E-02 parity checks for the 189 unsampled pairs (summary and fresh-certificate
  identity, attempt status, runner identity), accepts extra members and uses loose
  truthiness checks. **E4-04** `verify_compact` accepts a rehashed
  `observed_returncode: false`, and its output does not record which plan was enforced.
  **E4-05** the I25 launcher takes worker exits from `Popen` (ECHILD maps to 0, SIGCHLD
  not normalized); mitigated because acceptance also requires 942 accepted rows; a wording
  change. **E4-06** stale or contradictory deposit text (`MANIFEST.json.in`
  pending_items[0], README lines 252–253 vs 289) and the README neither pins the
  repaired verifier (5867ac0c) nor warns that the deposited `padua30.zip` carries the
  unrepaired historical verifier (`7c2dad53`). **E4-07** the size-bound convention
  changed: 9,897,953 B credits the shrink of `cold-storage.json`; under the topic's
  earlier "no deletion credit" convention it is 9,917,613 B (both under the cap).
- **J3-01** produce and verify witnesses are byte-identical in tree, stored rows and
  origin lower (confirmed for all 280 old-return degrees, inferred for the 191 new
  ones), so I25 recertified 471 distinct trees, each twice; the paper, companion, J03
  and G01 say "two trees per degree". **J3-02** `RECHECK-SMALL-BUNDLE.md` suggests a
  3600 CPU-s cap for a serial full recheck; on this machine that projects about 3.75k
  CPU-s and would kill the run as failed; allow at least 7200 s. **J3-09** G01 says the IEEE
  model is "proved in J03"; it is assumed (**fixed in place**, below).

### NOTE / EDITORIAL (selected; full lists in the reports)

- J1-01 an optional simplification: the right side of (1) decreases in n at every point
  of the quadrant, so the three base checks at 512 already give what the assembly needs.
  J1-03 name H and `uc:origin-identity` as the source of j > 23/250 via H0 > 7/25.
  J1-04 the frozen certificate metadata still lists "E15" and "PD-T271" for far and
  corner leaves (disclosed in J03:175–180). J1-05 the checker asserts vertex < 1/2 while
  the paper prints < 3/20. J1-06 **the onset is tuned tightly** (slacks about 2.1e-4):
  rerun `check.py` after any edit to the comparison constants.
- J2-02 the elementary brackets are proved only inside the proof of `uc:master`; one
  "Elementary constants" lemma at the start of 4.1 would make the dependency visible.
  J2-06 the audit-03 H-C03 characterization is withdrawn (**fixed in place**). J2-07 the
  reviewed bytes of F03-support (fbdeed2e) and H04 (cd8a9462) were never committed (the
  audit covers the committed bytes). J2-10 response-03's E-05 row says the campaign
  summary scopes PA1; only the preregistration does. J2-11 the coarse chain is exact but
  tight: with every coarse threshold at its limit the C_inf gap is about 1.3e-5 against a
  true margin of 0.0285.
- J3-03..J3-08: the unproved stored upper is always at (0,1) where S = 1; add 2–3
  controls that must accept (raising stored numbers changes nothing); gradual underflow
  and rounding mode are recorded as constants, not tested at run time; the θ < 1 leaf
  requirement under GRID is conservative; a collapsed origin-leaf parent is accepted with
  smaller margins (the native trees are not minimal there; not a defect).
- E4-08..E4-11: the runner's in-flight pin and exit assertions leave no record; residual
  bounds (tar header blocks read before the size cap, zip symlink-typed members accepted as
  data, fresh keys compared as sets, compiler and Python recorded but not pinned); a
  distinct reviewer executed independent arithmetic only for n = 458 in the new range.

### Audit-03 dispositions, checked against the actual files

J02 and J01 confirmed the record-structure fixes: G-1..G-6, F-01 (the F03 identities now
live in the PROVED support record; the OPEN sign target is not a premise anywhere), the
H-C rows, E-07, E-10 (`cold-storage.json` is now 4,244 B), X-17, P-03 and C2A-07 exist and
are correct. The companion and paper readers found these audit-03 rows marked FIXED in
response-03 that are not fully supported by the text: C2B-M1, M3(b), M3(f), M4, m7, m9 and
m12 (companion), C1-02 and C1-09, C3-02/09/10/19, X-13 (eq. (54) and five other displays
still push their number onto its own line) and E-05. The details are in the manuscript
record. P1–P4 stay as recorded under AC's accepted disposition (no waiver, no backdating).

## Auditor in-place MINOR fixes (third-and-later audit rule)

Allowed classes only (stale process text, links, dated addenda; pinned text untouched);
committed separately from this report.

1. `theory/G01-all-degrees.md` (end): J2-04 (the PD-T271 sentence describes the 320 route; J02 replaces it for
   the 512 route) and J3-09 (the IEEE model is assumed, not proved).
2. `theory/F03-origin-sign.md` (end): J2-05 (header "Split into: none" is superseded by the
   support record).
3. `theory/H04-smooth-quadrature.md` (end): J2-06 (audit-03's H-C03 "swapped" characterization
   withdrawn).
4. `companion-paper/review.md` (end): C4A-10 (status line describes the old freeze; pointer to
   the current reviews).

Not fixed in place, with the reason: every TeX edit (any change to `paper/` or
`companion-paper/` sources breaks the 24a98db byte freeze and needs a new paired freeze and
baseline update); E4-01..E4-05 (code); J3-02 (recipe parameter); E4-06 (deposit text,
classification in doubt); J1-02 and all manuscript findings (proof text); the response-03
rows above.

## Limits and data-access gaps

- **Not examined because the files were not supplied** (requested twice): the canonical
  `onset512-return-20261108.zip`, the I25 bundle, `padua30.zip` (without which the reader
  cannot run even once the canonical ZIP arrives: its pin check reads 171 headers), the
  small certificates ZIP, the inventory and the review ZIP. Consequently no witness for
  degrees 320..510 (including 458) and no run of the documented reader on the actual ZIP.
  The exact commands for these checks are in
  [audit-04/WHEN-INPUTS-ARRIVE.md](audit-04/WHEN-INPUTS-ARRIVE.md); a data-only check of
  degrees 320, 384, 458 and 510 (about 1–2 CPU-minutes) plus the reader run would close the
  gap. No full replay is requested.
- The 632 MiB of unsampled complete native histories for 320..510 exist only in the
  ephemeral Codex campaign tree; there is no cold-storage entry, no Zenodo record and no
  DOI. Deposit preparation is not custody.
- Pinned Debian runtime and byte preservation of the original 48/162-page PDFs were not
  tested (no `local-output/`); the artifact mode of the correspondence helper cannot run
  without them (and ends in a traceback for nonexistent paths).
- The mathematical premises listed in the trust conclusion were traced, not re-proved;
  J01's component internals (telescope, pole and half-line, origin, E14 signed outer) were
  checked at statement, domain and assembly level.

## Not re-derived

The internals of the comparison theorem's components (the 11-page Theorem 4.5 charges, the
Section 3.3 aggregate constants) were re-derived in audit-03 and are unchanged in substance.
The E06/E07 scalar maximum internals, the inequality C_inf − C* <= −j u + t0 p (term
bookkeeping and constant inputs only), PD-T269 sections 2–3, PD-T270, C02 class counting
beyond displayed counts, the native Arb kernels (trusted), and all of D32/D29/D14/D19.

## Prioritized response plan

For Codex (details in the next handoff):
1. **E4-01 first:** fix the reader's assert-based checks and documentation; re-review.
2. Obtain or supply the three missing payloads and run the preregistered checks in
   WHEN-INPUTS-ARRIVE.md; only then can 320..510 be accepted.
3. One coordinated editorial batch for both manuscripts (new paired freeze, rename-aware
   check, rebuild): see [audit-04-manuscripts.md](audit-04-manuscripts.md), starting with the
   companion regression C4B-01 and the symbols-before-definition and named-tool groups
   (N4-01, N4-02), then the proof-clause additions (J1-02, P4-06, P4-07, C4C-M3, C4D-01).
4. Record fixes E4-02..E4-07, J3-01, J3-02, J2-01, J2-03, J2-09 (wording and recipe items).
5. Keep J01's slacks in view: rerun `check.py` after any constant edit.

For AC: supply (or confirm unavailable) the three payloads; the Zenodo deposit and DOI;
the AI declaration remains yours (the audit's only report is that it omits Claude Sonnet 5.5
and still carries a draft sentence).

## Own proof and presentation ideas

No real mathematical gap was found, so none was manufactured. Useful, optional: (1) J1-01,
the monotone-in-the-quadrant simplification of gate (1), which removes the monotone-maximum,
optimizer-positivity and db < 5/48 steps; (2) one "Elementary constants" lemma at the start
of Section 4.1 (J2-02); (3) a hand-checkable table of rational enclosures at n =
192/256/295/512 (P4-05); (4) a short toolkit of the cotangent partial fraction and the
elementary-constant rules before Lemma 4.2 in the companion (C4B); (5) state outright that
I25 recertifies 471 distinct trees, each twice, and that stored native endpoints are neither
used nor validated (J3-01, C4D-04); (6) split the trust table into what the text proves and
what the program computes (C4D-05).

2026-11-08 · orchestrator `claude-sonnet-5-5`; audit work by eleven Claude Opus 5.5 subagents
(instructed xhigh) · rules read at be9a831, unchanged at 70a50d7.
