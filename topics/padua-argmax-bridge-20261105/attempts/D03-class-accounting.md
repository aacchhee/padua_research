# D03: existing phase-certificate class accounting

2026-11-06; rules/input head
`084a64f6465956f9c75b5538f83752c30318f151`.
Codex, parent-assigned gpt-6.1-sol medium; serving metadata unexposed.
This implements handoff08 B5's first accounting step and audit-01-ideas
P3. It adds no mathematical mechanism or novelty claim, so no independent
novelty search is needed. Only saved records and checker source text were
read. No checker was imported or run, no kernel was loaded, and no degree
or pilot was executed.

## Accounting result: MEASURED saved-record counts

| Degree | Far | Corner orbit + defect | Maximum exclusion + defect | Local corner + defect | Outside | Total | Near subtotal |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 17 | 524 | 704 | 0 | 28 | 32 | 1288 | 732 |
| 24 | 512 | 456 | 0 | 20 | 32 | 1020 | 476 |
| 32 | 280 | 28 | 24 | 0 | 32 | 364 | 52 |

"Near subtotal" means precisely the sum of the three defect-labelled
classes in this table. It does not assert that those leaves match a
particular geometric phase-radius cutoff. The fifth original class,
local-corner-plus-defect, is retained rather than silently recoded as
corner orbit or maximum exclusion. The n32 subtotal reproduces the
audit's280 far /52 near /32 outside count.

| Degree | Whole checker process CPU-s | Checker timed-region CPU-s | Compiler/build-helper CPU-s | Total subprocess CPU-s |
|---:|---:|---:|---:|---:|
| 17 | 109.449514 | 109.380850969 | 1.287483 | Not separately recorded |
| 24 | 202.067842 | 202.022073057 | 1.164960 | Not separately recorded |
| 32 | 138.193144816 | 138.175126666 | 1.171140 | 139.405409 |

The CPU numbers are historical receipt values, not new timings. The
whole-process and internal timed-region measures have different start
and end points. The full subprocess total additionally includes the
recorded build helpers and surrounding worker scope.

**Per-class checker CPU is unavailable for every class and degree.**
The saved replay entries contain only root, path, kind, valid and bounds.
The checker sources place process_time() around the whole replay; they
do not time individual leaves or classes. No total was allocated by
leaf fraction, and no near-only throughput or speedup is measured here.

## Predicate meaning and original success scope

Source inspection: check.py:121-132, check_r6.py:147-158,
check_r8.py:101-113; check_r9.py:48 delegates unchanged acceptance
to check_r8.check. The original labels name acceptance predicates:

* outside: exact geometry excludes the physical phase diamond; no
  kernel.bounds call is made for that leaf;
* far: S_upper < corner_lower;
* corner-orbit-plus-defect: corner_orbit_upper < corner_lower and
  S_upper - defect_lower < corner_lower;
* local-corner-plus-defect: the inherited or published local-patch
  premise applies, and S_upper - defect_lower < corner_lower;
* maximum-exclusion-plus-defect: the published bootstrap premise's
  range applies, and S_upper - defect_lower < corner_lower.

The native bounds call returns all three quantities for every nonoutside
leaf. Thus these counts alone do not say how much native work a future
far-eliminated checker would save, even for these exact candidates.

The n17 record is the accepted complete round5 replay of its frozen1288
leaf candidate. The n24 record is the accepted complete round6 replay,
with round5 native kernel, of its1020-leaf candidate. The n32 record is
the accepted complete round9 replay of the unchanged bootstrap-r8
candidate,364 leaves. These remain their original success scopes; this
accounting is not a current validation of their certificates.

## Reproducibility and identities

Executed command:

    python3 topics/padua-argmax-bridge-20261105/code/post_audit_D03_class_accounting/account.py

Exit0; accounting process CPU0.050429s through receipt preparation.
The script only uses Python standard-library file parsing and hashing.
It verifies the frozen committed receipt hashes, then the receipts'
local raw-report and candidate byte identities, the raw reports'
candidate hashes, all recorded checker-source hashes, complete/accepted
flags, matching leaf counts and original(root,path,kind) sets. It counts
saved replay labels and checks them against candidate labels. It does
not execute the predicates or replay the tree geometry.

Small result receipt:
`../code/post_audit_D03_class_accounting/accounting.json`,10,874 bytes,
SHA256`a1c2dddacd1ccffcee66ca6466088eef9cbcdde341fc50968c17011380a6d8f5`.
It pins the accounting script, all three receipt→raw-report→candidate
chains, verified checker sources and source timing lines. The immutable
raw artifacts were all present and left unchanged.

Receipt inputs:

* evidence/phase-checker-full-n17-round5.json:
  `49060e7633068f6ffb531e63614855a5d88c466c10e6d4d1b07a8c21043e6423`;
* evidence/phase-r6-n24.json:
  `4392ef9c09da02b10c2379619a840782f8f339be88b67a1183f803f74ead9fdd`;
* evidence/phase-r9-n32.json:
  `5bdab76556a37552121afabe172d641e57a60026d1b07b36c4f6e5e5069977ae`.

## What this resolves and leaves unknown

The existing records show that far predicates occupy substantial leaf
counts in all three candidates. They do not establish a CPU cost for
the retained near classes. The sharp decrease in near leaf counts from
n17 to n32 cannot be extrapolated: these use different candidate
construction and checker versions, not one controlled scaling study.
Consequently this accounting supports investigating the cost question,
but supplies no measured near-only throughput or all-degree cost gate.

Runs needed within D03 accounting: none. Any later near-only pilot
requires the separate handoff08 B5 prerequisites and bounded plan;
none is authorized or performed by this record.

## Distinct root check — 2026-11-06

Codex coordinator, requested Astra high, independently parsed all three
saved raw reports and candidates in a fresh Python process. The check
rehashed each receipt/raw/candidate chain and the accounting source,
recounted candidate and replay kinds separately, checked the complete
saved acceptance flags and matched every row above. PASS;0.011006483
process CPU-s. This was an independent saved-record recount, not a
certificate/kernel replay. Source inspection confirms that native bounds
is called for every nonoutside leaf and process_time measures whole
replay scope. Per-class costs remain unavailable. No mathematical or
novelty claim is added; final Claude audit remains separate.
