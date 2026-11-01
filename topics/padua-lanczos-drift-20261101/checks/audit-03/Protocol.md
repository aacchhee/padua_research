# Audit 03 — bounded protocol review

**Verdict: ACCEPT within this protocol scope. No high, medium or low finding.
A02-L8 is RESOLVED.** Scientific acceptance, novelty, current GitHub state and
integration are separate reviewer/orchestrator responsibilities.

Auditor: independent Codex protocol subagent, explicitly configured
`gpt-6-astra` xhigh by the orchestrator; resolved serving model/effort is not
independently exposed. Rules read at published head
`c8849a89a601e0a56342d3d568086ab8abdbc4c0`. Candidate:
`ea829d92d509f79326a1cc037844a1bac3b4de13`; response start:
`1df5f89fe52f62c49d5addd58dcfea7246c5a688`; pinned main:
`28aaa20861d08074b77efc74eaef75cdcb36234d`; original base:
`806cc7b4509fd93bae652f9545d32d95529f8281`.
Candidate-to-published-head changes are only handoffs 07/08.

The scope is administrative consistency, input identities, historical-file
preservation and repository limits. No mathematical proposition, candidate
mechanism, novelty or literature-priority claim is generated or accepted here.
The WORKFLOW exception therefore permits omitting a full `state/IDEAS.md`
read. The ID scan reads that registry mechanically; it is not a novelty review.

Read coverage: rules, handoff08, audit02 and its protocol report/checker,
response02 and all four developer reports, current plan/report/proposals,
COLD_STORAGE, topic results and the relevant LOG history. New evidence
structures, pin declarations and selected source are inspected as identified
in the receipt. `e1_scalar_finite_check.py` is inspected for pins/reuse, not
scientifically re-audited; `integration_check.py` is inspected and never run.

## Executed verification

From repository root:

```sh
python -B topics/padua-lanczos-drift-20261101/checks/audit-03/Protocol/check.py --output topics/padua-lanczos-drift-20261101/evidence/audit-03-protocol-checks.json
```

The independent standard-library checker uses read-only `git show`, `diff`
and `ls-tree`; no checkout, worktree, merge, branch or index mutation occurs.
The [receipt](../../evidence/audit-03-protocol-checks.json) contains exact
read-input identities, the checker hash, Python version and per-check results.
All final mechanical checks pass. An initial checker iteration used an overly
narrow literal wording test and rejected a valid directory link; those two
checker assumptions were corrected, without changing developer files.

- **L8:** all four active files explicitly place results in the repository.
  Proposals require only this topic's root RESULTS section at preparation,
  preserving other sections; the old Windows results file is marked a
  historical copy. Cold-storage delivery remains a distinct pending item.
  The topic results file accurately identifies response02/Codex re-audit,
  provisional IDs, bounded statuses, developer versus independent execution,
  the INCONCLUSIVE both-grid test, and remaining open targets. Links resolve.
  Acceptance of the PARTIAL target label and the new PROVED record belongs to
  E1; this is a consistency check against the declared response.
- **Frozen history:** 89 pre-existing audit/check/report/evidence files are
  byte-identical to response start, including audits01/02, response01,
  their checker/report directories and every pre-existing topic evidence
  file. All 23 output identities in audit02's manifest still match.
- **Response02 pins:** 54 explicit repository pin checks pass, covering the
  historical response01 manifest at its prior revision, audit02 outputs,
  new checker code and their repository inputs. Every full SHA256 in the
  four new developer reports resolves to the declared current or previous
  campaign bytes. The historical response01 manifest's only current mismatch
  is the disclosed E6 docstring edit; its old pin matches response start.
  Removing only that module docstring gives identical old/new Python ASTs.
- **Evidence consistency:** recorded PASS fields are internally consistent.
  Independently comparing the frozen E6 files gives 391 leaves, 387 compared,
  370 numeric and zero unequal compared leaves, exactly the embedded receipt.
  The four masks are command, Python, elapsed time and the changed E6 source
  hash; NumPy/SciPy remain compared. The unchanged external polyrat hashes
  agree with response01; no new third-party retrieval is claimed here.
- **Boundaries:** all 77 original bivariate theory files are identical to
  both main and the original base. Protected paths, rules, scientific
  registries and root RESULTS match main. Allocation ledger/crosswalk are
  unchanged since response start. There is no assignment of reserved final
  IDs in registries, crosswalk table rows or track record declarations.
  All 15 literal OLD blocks and the optional History anchor are unique at
  main/head and after sequential in-memory replacement. No proposal is applied.

## Size limits and remaining work

Conservative inventory of every new own campaign file versus pinned main,
including prose, code and the repository results file:

| Pin | Files | Total bytes | JSON bytes |
|---|---:|---:|---:|
| response start `1df5f89` | 156 | 3,906,521 | 2,813,629 |
| candidate `ea829d9` | 173 | 4,275,727 | 2,971,323 |
| published input `c8849a8` | 174 | 4,280,121 | 2,971,323 |

The largest file is `e1-full-sweep.json`, 616,693 bytes. Even this conservative
all-file inventory fits decimal 1 MB/file and 5 MB total limits, with 719,879
bytes left before audit03 additions. The orchestrator must count the complete
audit03 publication, including this report/checker/receipt. No historical
file was deleted or evidence split to meet the limits.

Response02's four raw E1 developer regeneration files are absent at their
declared workspace paths here. Their historical hashes are preserved, not
presented as newly verified bytes; they are expressly regenerable working
outputs, not a cold-storage deposit or hidden essential input. The committed
evidence and producer pins do verify. E1's actual reconstruction is separately
attributed to its reviewer. Earlier audit02 verification of the original ZIP
and raw artifacts is historical evidence; it was not repeated by this worker.
The earlier unretained record05 working-byte pin and pending Windows custody
remain the disclosed limitations from audit02.

Preparation advice: synchronize the original plan/report header references to
the initial Claude audit/base when preparing the PR. The authoritative current
response, handoff and results file already identify Codex re-audit correctly;
this historical-header cleanup does not reopen A02-L8 or scientific claims.
Fresh remote union checks, integration rehearsal, final output-size accounting
and handoff allocation belong to the orchestrator. No Windows write/readback,
final-ID allocation, scientific checker execution or readiness decision is
claimed by this protocol review.
