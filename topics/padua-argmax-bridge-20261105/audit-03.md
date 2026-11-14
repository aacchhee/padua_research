# Claude audit-03: substantive audit of the completed results (handoff 28)

Companion record for the two manuscripts and their agreement:
[audit-03-manuscripts.md](audit-03-manuscripts.md). Review reports and
auditor scripts: [audit-03/](audit-03/). This is the substantive Claude
audit that handoff 13, 15, 16 and 28 require before PR readiness. It is
audit round 3 of the topic after [audit-01](audit-01.md) and
[audit-02](audit-02-interim.md). It is **not** a readiness decision, waives
nothing, and PR 27 stays a draft. Only AC merges.

## Decision

**Mathematics and evidence: ACCEPTED at the stated scopes, with record
corrections required.** I found no BLOCKING finding anywhere. No mathematical
error was found in the sharp corner expansion, the n>=320 analytic tail, the
finite completion, the F-series supports or the actual Syvert return. Two
record-structure MAJOR findings (G-1, F-01) concern what is declared a
premise, not whether a result holds. The manuscripts need revision
(see [audit-03-manuscripts.md](audit-03-manuscripts.md)). Because MAJOR
findings are open, the stage returns to **WORK** for a Codex response
(handoff 29). The unwaived chronology findings P1–P4 from audit-02 are
unchanged and still need AC's explicit disposition.

| Verdict | Result |
|---|---|
| 1. Mathematics and evidence support | **Supported, computer-assisted, within G01's named trust.** Independently re-derived or re-run at every scope below. Independent arithmetic for the 276 unsampled native degrees is still not available (E-06, I25) |
| 2. Journal paper (48 pp) | **Major revision** for presentation, a removable computational dependency, an inaccurate data statement and notation. No correctness defect found |
| 3. Companion (162 pp) | **Mathematics sound; pedagogy REVISE.** Several load-bearing steps are asserted, symbols are heavily reused, no figure in pp. 50–110 |
| 4. Agreement | **Agrees** mechanically (113/113 labels, 13 statements, 90 numbered environments, 211 display blocks, bibliographies byte-identical). Several fixes must be coordinated in both texts |

## Identity, rules and disclosures

- **Models.** AC's prompt named Claude Opus 5.5 xhigh. The session model was
  switched to Sonnet 5.5 (`/model`) before this turn, so the orchestrator ran
  as `claude-sonnet-5-5` and derived no mathematics. All audit and idea work
  was done by **thirteen Claude Opus 5.5 subagents instructed at xhigh**
  (effective effort not exposed): H, G, E, F, P, C1, C2A, C2B, C3, X, I, S
  and N below. All are distinct from the Codex developers and reviewers.
  WORKFLOW assigns mathematical audit to Opus 5.5 high or xhigh.
- **Role.** Independent auditor and idea author, orchestrator for Git in this
  step only. Subagents made no Git change and no repository edit.
- **Rules.** AGENTS.md, agents/WORKFLOW.md and agents/claude/CLAUDE_ROLES.md
  were read at be9a831 and are byte-identical at the audited head (empty
  `git diff` for AGENTS.md, agents/ and templates/).
- **Candidate.** `codex/padua-argmax-bridge-20261105` at
  `f366535e1fa4ede566cb83bdc554220c12b307cf` (handoff 28 names input head
  `c0d122c6801d4019ed7f0c98e23fc0d438d4e3b8`; they differ only in handoff and
  brief files). Base `f70a260e5b5f9a01209dc8a05faabdcf8db1feeb`.
- **AC decisions made during this audit** (recorded here once): (1) AC
  supplied the Syvert compact return as two parts; I joined them and verified
  36,045,486 B, sha256 `b00fd57f85ce6d96a6c1fa01e2307abd815088bb8fcb28b1587657ef142b109a`
  (equal to compact-return.md). (2) AC asked whether the proofs can be
  streamlined and **decided to move the analytic onset from 320 to 512**,
  certifying the extra degrees 320..510. The projected cost (about 1 CPU-hour,
  worst case about 2.4) fits a sandbox with the pinned runtime as well as
  Syvert; AC asked and the answer is in handoff 29. (3) AC asked
  for a single master notation register covering both texts, in
  [audit-03/n-notation.md](audit-03/n-notation.md).
- **Environment differences.** The proxy blocks deb.debian.org and most
  hosts, so the pinned Debian runtime was not available. Native replays used
  Ubuntu FLINT 3.0.1, MPFR 4.2.1, GMP 6.3.0, g++ 13.3, glibc 2.39 and
  Python 3.13; builds used TeX Live 2023 (Debian). Where results are
  bit-identical across this change it is stated; where a pinned identity could
  not be checked it is listed under limits.

## Coverage

| Review | Scope | Report |
|---|---|---|
| H | Sharp corner expansion, both parities (H01–H06, canonical theorem, paper Section 3 consistency) | [h-corner.md](audit-03/h-corner.md) |
| G | G01 all-degree assembly, finite completion 2..319, small-degree scheme, trust list, audit-02 dispositions | [g-assembly.md](audit-03/g-assembly.md) |
| E | Actual compact return, compact pack and verifier, audit-02 operational dispositions, native replays | [e-evidence.md](audit-03/e-evidence.md) |
| F | F01–F10 completed paper-only supports | [f-series.md](audit-03/f-series.md) |
| P | Journal paper (referee report, every section) | [p-paper.md](audit-03/p-paper.md) |
| C1, C2A, C2B, C3 | Companion, four readers covering every line of main.tex and all six sections | [c1](audit-03/c1-companion.md), [c2a](audit-03/c2a-companion.md), [c2b](audit-03/c2b-companion.md), [c3](audit-03/c3-companion.md) |
| X | Fresh builds, correspondence, bibliography, literature and application citations, novelty gate | [x-build-literature.md](audit-03/x-build-literature.md) |
| I | Own proof and presentation ideas, novelty gate | [i-ideas.md](audit-03/i-ideas.md) |
| S | Proof-architecture streamlining (AC's special question) | [s-streamline.md](audit-03/s-streamline.md) |
| N | Master notation register | [n-notation.md](audit-03/n-notation.md) |

## Executed checks

Labels: [E] executed, [D] own derivation, [I] inspection only. All outputs went
to fresh scratch paths outside the repository; no candidate byte changed. No
producer, residual-degree discovery run, bulk run or remote access was started
(see E for the four preregistered replays).

| Review | What ran | CPU | Result |
|---|---|---:|---|
| H | Independent exact finite corner sum solved from the Padua nodes; Lambda_c at n=2..64, 100/101 to 3200/3201 and 6400/6401 to 204800/204801, both parities (Arb 128-bit); constants kappa, b, c, I1, I2, I_B, C_B; identity checks | about 530 s, all exit 0 | Matches direct interpolation to 1e-39 (n=2..12). With R = Lambda_c - [A(N)^2 + kappa - 1/N]: N*R from 0.227 (n=2) to -7.2e-6 (n=204800); N^2\|R\|/log N <= 0.62; remainder order log N/N^2 looks attained (measured). kappa = 0.91971011838849253509951822579024 inside PD-T271's enclosure |
| G | Own certifier (python-flint/Arb, exact rationals) for n=2..17 and 24; replays of certificate paths at 16, 17, 32; exact-rational verifier on all 8 committed receipts; direct PD-T364 recomputation of every retained S key, three lambda points and the origin lower for 41, 199, 238; exact check of the PD-T271 consequences | about 21 min | Complete partitions and the two-corner equality sets; wrong-parity control fails as it should; all native upper bounds dominate the reviewer's enclosures (one exact tie at S=1); 9/10 < kappa < 23/25, C_* < 1847/1000, C_* > 4383/2420 confirmed without Arb |
| E | Archive rehash and member listing (no extraction); trusted package regenerated offline; unmodified `verify_compact.py` (exit 1, missing .deb); same through a minimal adapter (exit 0, PASS, identical to committed verification.json); own independent rational recheck of all 560 certificates; four preregistered native calls | about 55 s | **560/560 certificates pass both checkers**; coverage exactly 41..319 plus 511; draw reproduces 199, 238; committed primaries equal archive bytes. Native: verify 199 (exit 0, 10.11 s), verify 238 (exit 0, 11.05 s), verify 511 (exit 0, 7.25 s), produce 41 (exit 0, 6.57 s); all retained numbers bit-equal to the Syvert primaries |
| F | F07 at n=256 (120-bit intervals, 26 bounds), 60,000-n direction scan, F01 reanchor grid (251,001 points), entropy integral J, F08 kernel moments, F09 identities, F06 samples, F02 slopes; 42 hashes | about 2.5 min | All explicit constants pass; no violation |
| P | Corner expansion reconstruction; every displayed rational at n=320, 256, 192 (100+ checks); selected-pair floors; regional bounds and the 1/30 descent on grids | about 2.4 min | All hold; floors 5.5–54x below the actual smallest projections |
| X | Both PDFs built with fresh output dirs; correspondence checker; own TeX block diff; aux label comparison; evidence index; float constant check; 11 web searches | under 1 min CPU | Both build, 0 undefined references, 0 overfull boxes; 113/113 labels, 13/90/211 blocks identical; evidence index 396 entries / 32,414 B passes |
| C1–C3 | Re-derivation by hand, sympy and mpmath of every added derivation and example (Lemma 2.1, corner rows, Bernstein/Riesz proof, odd-center cover by brute force for n=2..8, coefficient ledgers, n=320/256/192 gate tables) | under 10 min total | No error changed any constant; corrected items listed below |
| I, S | Rational enclosure of kappa and C_*; independent S evaluator vs native bounds; third corner term; second-largest maximum; onset gate evaluations | about 4 min | Measured/enclosed, none claimed proved |

## Findings: mathematics and evidence

IDs are the reviewers' own and are unique. Locations, reasons and exact fixes
are in the linked reports. Note that "P-nn" are paper-review IDs, unrelated to
the chronology findings P1–P4.

### MAJOR (record structure)

- **G-1. The accepted evaluator theorems are premises that no statement lists.**
  The phase vertex enclosures are not plain interval sums. S comes from the
  D23 backend (C02 row decomposition, truncated, plus the proved D23 eq. (2)
  remainder resting on C02, N5 and C06); actual lambda comes from the D06
  four-copy rows and C11 rows. These theorems are premises for every degree
  41..319, yet G01 lines 51–53 and 75–79, paper `certification-unified.tex`
  lines 17–34, 110–141 and 245–253 and `paper/README.md` lines 58–60 present
  the endpoints as pure library arithmetic. Fix: name them in G01 and add a
  vertex-enclosure lemma or citation in paper Section 5 and its evidence
  boundary. Alternative (I-1 in G, I25 in I): re-validate every retained key by
  direct finite sums, already demonstrated at 41, 199 and 238.
- **F-01. The H sharp-corner theorem uses F03 identities, which sit in an
  OPEN record.** F03's exact identities (3), (4), (6), (7), (8) are declared
  premises in H01, H04, H05, H06 and the canonical H theorem, and pinned by
  independent-checks-H-main.md, but live in `theory/F03-origin-sign.md`, whose
  overall status is OPEN. WORKFLOW's split rule requires a proved part that
  another result depends on to have its own file, ID and status. The
  statements "F01–F10 are not premises" in campaign-F-summary, G01 (about line
  111), the results file and the audit brief are true for G01 but silent about
  H. The mathematics is sound (re-derived, and (3) and (6) match direct
  Lagrange computation to 1.7e-13 at 23 degrees). Fix: split F03 sections 1–3
  into a PROVED supporting record, keep the target OPEN, repoint H, correct
  the wording.

### MINOR

- **H-C01** stale status words in H01/H04/H05 (**fixed by dated addenda**, see
  below). **H-C02** the exact reduction's only written source is F03
  (OPEN); add PD-T226 and the paper's self-contained derivation
  (corner-unified.tex:83-107) to H01 section 1. **H-C03** H04:129 has the two
  coefficients of the |W''| majorant swapped; the correct form
  (8/pi)[(16/27) sum k^-2 + (4/9) sum k^-4] is still <= 4.74 < 5, so nothing
  downstream changes (math content, returned to the developer).
- **G-2** G01 claims canonical PROOF_STATUS links for 2..40, but
  `native-finite-range.md` (33..40) has no row and its line 25 still says the
  audit is pending. **G-3** G01 credits D29 for floors where 64..319 use
  C02's tiers; name C02 and give the tier map. **G-4** G01's trust list omits
  FLINT, the Python interpreter and parsing, and the LP64/binary64
  conventions; the paper's 2..40 paragraph states no trust base. **G-5** the
  paper applies corner-256 and far-192 but never says they inherit the
  PD-T271 enclosure; the introduction attributes it only to "the analytic
  argument".
- **E-01** `verify_compact.py` `reader()` returns archive payloads before
  trusted package files, so a return could shadow `FREEZE.json` or
  `asset_provenance.json`; no impact here (disjoint names); require disjoint
  name sets. **E-02** the verifier does not check the admission ledger,
  startup/resume history, tree equality of fresh and primary, per-pass
  summary result or the attempt/raw hashes; the reviewer's independent check
  covered all of them. **E-10** custody and size: the `cold-storage.json`
  entry for the return points to an absent path (the AC transfer is pending,
  as recorded), `cold-storage.json` is 23,904 B (over the usual 16 KiB with no
  recorded exception), and the size bound leaves only 225,999 B of headroom.
- **F-03** F-series theory prefixes still read "PROVED developer PAPER ...
  review pending"; registries should carry plain statuses at PR preparation.
- **X-17** paper-positioning.md contradicted the paper on the corner
  expansion's dependency (**fixed by dated addendum**).

### NOTE / EDITORIAL (selected; full lists in the reports)

- **E-06** (most consequential note). For the 276 degrees not replayed natively
  off Syvert, the server "fresh" pass is a deterministic re-execution: 280 of
  280 pairs are bit-equal, so it is not independent arithmetic. "No degree gap
  remains" is accurate as a coverage statement under G01's named trust. The
  cheapest way to raise confidence needs no new retrieval: replay the remaining
  276 archive primaries locally, about 4.4k CPU-s (about 20 minutes on 4 cores),
  or run the independent evaluator of idea I25, about 2–3 CPU-h; either needs
  its own preregistration and AC's authorization.
- **E-03/E-04/E-05/E-08/E-09**: a PASS accepts any completed subset (add an
  `--expect-plan` flag); the 24 GiB bound is checked only after loading; the
  frozen engine's `stage_run` still uses the standard library `child.wait()`
  (sound inside the normalized tree, but "PA1 fixed everywhere" is too broad);
  `sha256sum -c` on AUDIT.sha256 shows SPEC.md FAILED (the documented
  historical prefix pin); preregistration, native results and the first
  appearance of the seed are in one commit so Git cannot show ordering (the
  sample was fixed inside the archive before any replay).
- **E-07 EDITORIAL** the committed `fresh-n199/238.json` are sandbox replays
  (**fixed by a dated note**).
- **G-6/G-7/G-8/G-9**, **H-C04..H-C08** (the integration review accepted H-sharp
  at a hash that is not the committed version, which the log describes as a
  permitted status update; the measured log N/N^2 term means the remainder
  order is probably sharp; notation and spacing), **F-02, F-04..F-06**
  (the H theorem implies E_n(0) > 0 for large n, not effectively; the F01 gate
  closes at N=231 in float evaluation only, which must not be cited as a
  result; the F-series ancestors should be listed in the final IDEA entries).

### What the earlier reviews missed

The Sol/Astra reviews are completed prior checks. Independent execution found
what they did not: the H reviews ran no numerics and missed the swapped
coefficients (H-C03); the compact-return reviews did not exercise the
shadowing path of the verifier (E-01) or the absent verifier checks (E-02); the
F-rounds were accepted on paper reconstruction only, so F07/F06/F09/F08
constants were first machine-checked here; the audit-02 SIGCHLD defect (PA1) is
confirmed fixed by running the controls. None changes a status.

### Chronology findings P1–P4 (inherited)

Unchanged from [audit-02-interim.md](audit-02-interim.md): preserved in the
canonical E08/E09/E14 records, not waived here. Mathematical correctness does
not repair chronology. AC's disposition is still required before readiness, and
one rule should be applied to the E14-wide-signed "no violation" ruling versus
P4.

## Notation register (AC's request)

[audit-03/n-notation.md](audit-03/n-notation.md) lists 61 base symbols with two or
more meanings (229 meaning rows, 32 ranked entries) with exact definition sites,
live ranges, affected numbered formulas, a renaming plan and draft notation tables
for Sections 3, 4.1, 4.3 and 5. Worst: epsilon/varepsilon (seven roles; two values of
l = -log sin epsilon in Section 4.2), T, H, C and D, k/K, j/J, a/A/B. Beyond the
reviewers' seeds it found Euler's gamma reused as an angle in the proof of Lemma 4.6,
the companion's kappa = 8 a_0/(3 pi), zeta as a root of unity beside Riemann zeta,
and k = n/m and mu = n/m as two names for one number. Companion-only renames keep
`check_correspondence.py` passing. **Any paper-wide rename fails it, even when both
texts are renamed identically**, because the script requires the paper to be
byte-identical to frozen commit c6e195f. That needs an AC decision: re-baseline, or
switch to the rename-aware check the editor implemented and self-tested
(`notation_scan.py --baseline-rev ... --rename-map ...`). I recommend the
rename-aware check.

## Addendum: local native replay of the 276 unsampled primaries (AC decision 3)

Done after the findings above were written. Result in
[replay276.md](replay276.md): **276 of 276 verify calls accepted** (observed exit 0, no
timeout, no first failure), and every fresh receipt equals the Syvert primary on all compared
fields; 2312.5 CPU-s in total, about 10 minutes on 4 cores, non-pinned Ubuntu library stack. With the
four earlier replays, all 280 degrees are natively re-executed off Syvert. This resolves the
faithfulness part of E-06; independent arithmetic (idea I25) remains with Codex. The limits
listed under "Not re-derived, or not tested" for these 276 degrees change accordingly: their
native premises are no longer unreplayed, but they are still the same engine and Arb kernels.

## Audit-02 dispositions, checked in the code actually used

PA1 fixed and confirmed by running controls on the released process guard (exit
code 7 preserved; an external reap raises instead of returning 0; an inherited
ignored SIGCHLD is refused). PA2 code present, not exercised, moot for this
run (one clean quiescent epoch). PA3 the verifier accepts partial subsets; the
real run had no failure. PA4 resolved by the actual execution of all 280 pairs.
A-7 pin check real and passed for both samples. A-8 moot (largest returned
receipt 6,425 B against 16,384 B). A-10 locators present in the released
provenance, retrieval untested. A-12 partly addressed (E-02, E-04).

## Auditor in-place MINOR fixes (third audit round rule)

Allowed classes only: stale process text and links, by dated addendum without
changing pinned text. They are committed separately from this report.

1. `theory/H01-exact-sum.md`, `theory/H04-smooth-quadrature.md`,
   `theory/H05-digamma-centering.md` (end of each file): dated status
   addenda for H-C01, linking the accepting reviews.
2. `paper-positioning.md` (end): dated addendum for X-17.
3. `compact-return.md` (end): dated clarification for E-07.
4. `theory/G01-all-degrees.md` (end): dated clarification for G-6 ("prescribed"
   -> executed and reviewed), plus a pointer that G-1 and G-4 are returned to
   the developer.

Not fixed in place, because they are not eligible: H-C03 (math content), G-1,
G-2..G-5 (trust-list and record content), F-01 (record structure), E-01/E-02
(code), E-10, and all manuscript findings. The developer may dispute any fix;
disputes go to AC.

## Not re-derived, or not tested

Reconstructed independently: the corner expansion and its constants; the exact
finite corner sum; the finite reduction at the level needed for strict
exclusion; the odd-center cover; the actual return's certificates (rational
layer) and four native replays; selected-pair constants; the displayed
gate arithmetic at n=320/256/192; F07, F08, F09, F06, F02 constants.

Read but not re-derived: the n-independent upstream cores listed in audit-01 and
audit-02; PD-T269 sections 2–3, PD-T270's constant, PD-T271's own proofs (its
consequences were confirmed rationally); H02, H03, H06 proofs (H03 identities
only numerically); the E14 component proofs and the insides of E12 and E15
(arithmetic re-run); the C02/D29 selected-pair geometry (constants and clamps
checked); D23 eq. (2) and the C02/N5/C06/D06/C11 row theorems; F05 background
and central proofs, F01 retained and outer proofs, F04/F09 profile counts; the
correctness of the native Arb kernels (trusted); Syvert-side observed exits for
unsampled degrees.

Not tested: byte preservation of the recorded PDFs (no `local-output/`); the pinned
Debian runtime, the original g++ 14.2 toolchain and the 177 absent .deb and
header files (19 header files inside the sampled histories could be checked
only against manifest rows); network retrieval and AC cold storage; native
replays of the 276 other degrees; replays of degrees 18..23, 25..31 and 33..40
in the reviewer's own code (the repository's accepted records cover them).
No priority or novelty verdict beyond the bounded searches in X and I.

## Prioritized response plan

For Codex (details and bounded first tasks are in handoff 29):
1. Decide and execute the **onset 512** restructuring AC chose: the two
   closed-form gates and short monotone lemmas, and certificates for degrees
   320..510 on the frozen engine (about 1 CPU-h, about 25 MB), with the usual
   fresh and compact review.
2. Remove PD-T271 from the chain by the elementary rational enclosure of
   kappa and C_* (paper series at K=3); delete the unused bounds
   (kappa < 23/25, the H0 upper bound).
3. Fix the record MAJORs G-1 and F-01 and the MINORs above, including a
   complete trust table.
4. Answer all manuscript findings in one coordinated response
   ([audit-03-manuscripts.md](audit-03-manuscripts.md)), starting with the
   master notation register.
5. Run the independent second-arithmetic recheck of all 560 certificates
   (I25), or the local native replay of the 276 remaining degrees, as an
   explicitly authorized and preregistered step.

For AC: disposition of P1–P4; whether to authorize I25 or the local replay; the
where degrees 320..510 are certified (Codex's environment with the pinned runtime, or Syvert); data deposit and DOI
for the certificates before submission; confirm funding and AI-disclosure
text.

## Own proof ideas

[i-ideas.md](audit-03/i-ideas.md) (ranked I25–I30): I25 independent second
arithmetic for all 560 certificates; I26 an exact-rational lemma removing
PD-T271 (superseded by the same finding in S and P); I27 a third corner term
(measured N^2 R = -(7/36) log N + 0.9115 - 1/(2N) + o(1/N), with the alternative
coefficient -(1+kappa)/pi^2 refuted); I28/I29 how to make the
computer-assisted part refereeable and which figures to add; I30 the
second-largest maximum (edge-centre gap about 0.55, approaching 0.5485).
[s-streamline.md](audit-03/s-streamline.md) holds the architecture options and
their costs, including the options AC did not choose.

2026-11-08 · orchestrator `claude-sonnet-5-5`; audit work by thirteen Claude
Opus 5.5 subagents (instructed xhigh) · rules read at be9a831, unchanged at
f366535.
