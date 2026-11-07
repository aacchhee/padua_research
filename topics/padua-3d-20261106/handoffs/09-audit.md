# Handoff09 — padua-3d-20261106 — focused material re-audit

- Status: superseded by 10: AC authorizes the usable-point-set campaign; focused audit04 scope preserved for the next combined audit.
- Previous handoff: [08-response.md](08-response.md)
- Next agent / model / effort: **Claude, Opus5.5 (claude-opus-5-5), xhigh**.
- Role: independent auditor of Codex development; orchestrator controls Git.
- Branch: `codex/padua-3d-20261106`.
- Input head SHA: `8eb90342eaf323b889737b5160c55f2f619763bc`.
  This is the completed handoff08 output; the following commit publishes
  this handoff and only closes08 by its status line. Progress checkpoint
  `056eace1511cfce9eda47f004656dbd44157c69e` was explicitly unfinished.
- Main / base: `f70a260e5b5f9a01209dc8a05faabdcf8db1feeb`. Refresh first,
  merge/reconcile if main moved; never rewrite published history.
- Stage: **AUDIT**.
- Written by/date: Codex, assigned gpt-6-astra high coordinator · 2026-11-06.

## Task and scope

Perform one focused substantive re-audit of the material handoff08 changes
and the audit03 response. Write `audit-04.md`. Do not redo accepted older
theorems or the complete T7 n2 classification. Audit new claim/status/ID
mapping, result-bearing source/evidence changes and response dispositions.
The previous verdict was mathematics accepted, six MAJOR process/search
findings. Each E1–E6 and every returned developer item has an explicit
response; check those dispositions, not an assumption that acceptance is
already granted. Independent Sol checks supplement this Claude audit.

Read the rules at the current head, LOG, response03 and its records/hygiene
companions, report-round08, results and rounds. Audit03 and audit03-fixes
are protected historical inputs. Read the complete current IDEAS registry
for the novelty/mechanism scope, every obstruction/disposition table, full
shortlisted records and linked proofs. The new gate supplement records all
missed predecessors, actual source-reading coverage and aliases.

### 1. Lattice objectives and complement (highest priority)

Read all `theory/r08-lattice-*.md`, the two round08 T9/T10 attempts,
`code/r08_lattice*`, `evidence/r08-lattice*` and
`independent-checks-round08-lattice.md`. Keep three objectives separate:
minimum determinant, folded count, and full-rank folded count.

- Exact determinant minima through16:2,12,38,92,178,304,486,724,1026,
  1412,1878,2432,3098,3868,4750,5772. n4..16 rely explicitly on imported
  packing. The new5772 improves old5792 seed;24 minimizers. Check the
  window lower bound and all empty q below the first passing determinant.
- Global folded minima n1..5:2,7,16,35,54; global full-rank minima:
  4,10,24,45,75. Exact q/8 reduction must justify globality; every deficient
  decisive rank is rational, never inferred from modular deficiency.
- No positive full-support unshifted exact-N rule at n3..7. Check transfer
  from the local identity-mass witness to all strictly positive weights,
  with Haar sufficient for every admissible lattice. Phases and removed
  zero masses are outside scope. n4fold35/rank30 and n5fold54/rank48
  illustrate why positive integration alone does not give interpolation.
- n7 complete q1..960 has584906253HNFs,21354010admissible, zero<=120.
  Producer's disjoint segments1..881,882..921,922..960 agree determinant
  by determinant with the separate full304.789s replay. Finish code and
  receipt pin every segment and comparison; scientific digest
  `909f9922a468ac00745d180344299e62d35e9b17e2b16ec881bd707eece5ae39`.
- n6windowmin91 and n7windowmin128 are **not global minima**. n6global
  continuation capped after703/720, no smaller fold found; no false
  globality follows. n8pilot was unexecuted/deferred after measured costs;
  no n8infeasibility claim. Degrees8..109 remain OPEN. Check stop(a) against
  actual scopes/caps, not an all-degree exhaustion declaration.
- n2order19 positive examples tie to24ofT7's32full-rank groups and3ofT2's
  old normalized survivors; fourth has dualmin3 and momentT111=1/4.

Reproduce in a fresh scratch directory with committed code. Core examples:

```sh
python topics/padua-3d-20261106/code/r08_lattice.py build /tmp/UNIQUE-enum
python topics/padua-3d-20261106/code/r08_lattice.py run min --degrees 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 --binary /tmp/UNIQUE-enum --scratch /tmp/UNIQUE-min --receipt /tmp/UNIQUE-min.json
python topics/padua-3d-20261106/code/r08_lattice.py run complement --degrees 2 3 4 5 6 7 --binary /tmp/UNIQUE-enum --scratch /tmp/UNIQUE-complement --receipt /tmp/UNIQUE-complement.json
```

Fresh replay may run past120seconds: record actual complete/capped coverage,
not a timeout-as-success. The independent report gives alternate congruence
commands/driver loops and monomial-rank checks. Full alternate n4 took
883.72seconds; proportional auditor scope may reuse accepted reductions
while independently executing consequential new finite results. Do not
require transient old raw paths: regenerate them from recorded commands.

### 2. T8 half-shift and material finite-status proposals

Read the round08 T8 gate/protocol/attempt, four `theory/t8-r08-*` files,
producer/tie-correction/checker code, all `t8-r08-*` receipts and independent
report. New scoped hand theorem: every even n>=2 fails in the first-unit
M=2Nhalf-shift class; check fixed-node trace and all quantifiers.

Exact cubic class:741normalized triples, exactly8full-rank, all exact
coefficient determinants2^49. The original binary64 objective picked a
different near-tied tuple; after quality was known the correction used
exact equality plus the originally registered lex rule to choose(1,4,11).
Both code/receipts preserved; check the post-run repair rather than treat
it as prospective new selection. n5/7 scores remain floating near-tie
sensitive; no exact global argmax claimed. Corrected selected samples:
9.788798269/70.372944840/136.690399705 at n3/5/7. QR losses exclude
promising status; the literal two-Leja-loss trigger did **not** fire.

The old-nine M=N existence subsection is now a separate narrowly
computer-assisted PROVED proposal through12. Check explicit tuples,
fold/ring reduction, arithmetic safety, primes/order/determinants,
committed evidence and actual independent fresh-prime replays. Do not
upgrade the mixed old quality document or all-degree existence.

Useful independent commands, with BLAS/OMP threads1:

```sh
python topics/padua-3d-20261106/code/t8_r08_check.py --structure --census-n3 --quality --output /tmp/UNIQUE-t8-census.json
python topics/padua-3d-20261106/code/t8_r08_check.py --halfshift topics/padua-3d-20261106/evidence/t8-r08-halfshift-corrected.json --quality --output /tmp/UNIQUE-t8-corrected.json
python topics/padua-3d-20261106/code/t8_r08_check.py --old-witnesses topics/padua-3d-20261106/evidence/t8-r06-witnesses.json --output /tmp/UNIQUE-t8-old.json
```

### 3. Response03 records, labels and source/evidence repairs

- E2: original extraction kill n6/7, n8..16 post-kill; n8same-orderQR35.816
  versus45.458. Scoped MEASURED PD-N homes, not exact structured singularity.
- E5/E6: all requested predecessors, Belinsky secondary lead and exact
  coverage limits; complete IDEA dispositions/resumes, standalone missing
  T9 IDs, standard measurement namespace, D3, source reuse. No final IDs.
- E4 is an **AC convention decision**, not silently resolved by developer
  or auditor. Proposal: PROVED with explicit LITERATURE dependency when
  exact primary statement/normalization and application are checked;
  CONDITIONAL for an unverified application premise. Applied uniformly
  to packing, R-Leja and T10log3, the last a material relabel. Check actual
  source coverage/applicability and preserve AC's decision question. No
  local external-theorem proof, Belinsky full text, Minkowski original or
  full erratum is claimed. Original-source request remains pending.
- q2Gauss sentence fixed:8<10, not q³>N; T_q(x1) proves non-unisolvence
  at every q>=2. Original short-dual counterexample remains valid.
- Two no-prose-pin generator edits, transparent historical receipt
  corrections,31code-only pins and18receipt refs;664actual shifted folds
  plus analytic rank invariance; authenticated n2..7selection/quality/rank
  linkage. The51rawhash check is26legacy-T9+25T7/T8, excludesT10/node-only
  hashes. Commands/list and real replays are in response-03-hygiene.
- Single manifest v4:204artifacts,994297bytes,15804-byte manifest. Lossless
  RFC1924base85SHA-256; recursive arbitrary suffixes includingC++, excludes
  only Python bytecode caches. Eight mutation controls actually pass.
  Verify code/data, never pin prose.
- Canonical new T8 gate-reading timing qualification is in its attempt.
  Published pre-run bytes do not repair post-run visibility of unrelated
  current MZ disposition rows. Older deviations/AC decisions remain
  canonical in deviations01/02. No retrospective compliance claim.

## Scope limits and acceptance

Do not change main, tags, settings, `.github/`, other topics or protected
audit/handoff bodies. Only AC merges. Do not allocate/reserve final IDs or
apply shared registries. No new construction campaign; audit this material
batch only. Counters continue T7=3,T8=3,T9=3,T10=3of25, not restarted.

This is audit04: WORKFLOW's third-round rule applies. Fix each eligible
MINOR wording/link/stale-record item directly, in a separate auditor-fix
commit listed in audit04. Material claim/code/status/ID/disposition changes
return to developer; preserve disagreements for AC. Do not edit the
developer's mathematical claims and call that independent approval.

Expected outputs: audit-04.md with exact audited head, actual source/gate
reading, separate executed commands, findings/severity and residual scope;
any eligible minor fixes separate/listed; LOG and results/PR updated by
the orchestrator; stage PR if accepted or WORK for returned findings.
Commit/push audit outputs first. In a following commit change only this
handoff status to done in that outputSHA and add handoff10 for the precise
next step (developer response or PR preparation). Preserve exactly one
open handoff. End with the short model/effort continuation prompt.
