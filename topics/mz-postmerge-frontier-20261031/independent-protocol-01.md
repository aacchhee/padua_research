# Independent protocol review 01 — supplemental only

Rules read at `07c5f5465d6de306aa81dbe8ca1f615295163864` on `codex/mz-postmerge-frontier-20261031`, 2026-10-31. Reviewer: independent Codex subagent, requested `gpt-6-astra`, medium; the orchestrator confirmed these exact dispatch settings. Authoritative runtime model/effort metadata is not exposed in this child context; requested configuration is not represented as independently observed runtime metadata.

**Verdict: no actionable finding within the bounded administrative scope. Supplemental only; required Claude audit remains PENDING.** This review does not approve scientific claims, clear novelty, or replace the cross-agent handoff.

## Scope and findings

Reviewed the current working diff against base `07c5f5465d6de306aa81dbe8ca1f615295163864` plus the four new administrative files identified below. The only tracked changes are CURRENT's MZ paragraph, the original MZ log's completion prose, and the batch ledger's integration prose. The charter prefix of CURRENT is byte-identical. The complete ledger Final reservations section and named allocation owner are byte-identical. No theory, source record, status registry, idea registry, crosswalk, manuscript, code, rule or template changed. No new ID or reservation is allocated.

Git independently confirms base/main has exactly parents `08fafe62d9798385dfafaacc9a41344272737e68` and `8ee04f4e5db46dd25fe5752ce605dde27098aae6`; the ready head is an ancestor. Base/main and ready head both resolve to tree `88108c08d0e4cd0584b262b9ac088ca592757896`. The receipt accurately calls this an observed two-parent merge, rather than claiming the planned squash occurred. The GitHub merge timestamp is reported evidence from the developer's receipt, not a fresh independent API query by this reviewer. The one-second difference from Git commit timestamp is not inconsistent: commit creation and PR merge metadata need not be identical.

The frontier faithfully summarizes PD-T020, PD-T027 and PD-T028 as OPEN, preserves finite spectra as MEASURED, and points to the named pending-reference Nevai III/addendum comparison. Its proposed later steps are already present in those records and audit-02; no new mechanism is activated. Deferred rule classification and certified/fast-spectrum routes match the existing MZ disposition entries. Audit-01's mathematical acceptance is correctly distinguished from its overall changes-requested verdict by the reference to acceptance of the original mathematical statements; audit-02 accepted the response scope. Nothing here grants publication/priority clearance.

Novelty gate exemption: this is administrative closure and faithful restatement of existing targets, with no new mechanism, mathematical assertion, priority claim, candidate or status upgrade. Therefore a full IDEAS novelty audit and literature search were not required; only relevant existing dispositions were inspected. No historical mathematics was re-proved, numerical program rerun, new source investigated, or remote state mutated.

## Commands actually executed

All commands ran from `/workspace/padua_research`. Initial discovery/read commands: `pwd && rg --files -g AGENTS.md -g WORKFLOW.md -g CODEX.md`; `cat AGENTS.md agents/WORKFLOW.md agents/codex/CODEX.md`.

Review commands:

```sh
git rev-parse HEAD
git status --short
git diff --stat 07c5f5465d6de306aa81dbe8ca1f615295163864
git diff 07c5f5465d6de306aa81dbe8ca1f615295163864
rg --files topics/mz-postmerge-frontier-20261031
cat topics/mz-constants/POST_MERGE.md topics/mz-postmerge-frontier-20261031/*
git show -s --format=fuller 07c5f5465d6de306aa81dbe8ca1f615295163864
git rev-parse 07c5f5465d6de306aa81dbe8ca1f615295163864^1 07c5f5465d6de306aa81dbe8ca1f615295163864^2 07c5f5465d6de306aa81dbe8ca1f615295163864^{tree} 8ee04f4e5db46dd25fe5752ce605dde27098aae6^{tree}
cat tracks/mz-constants/theory/m2-sharp-constant-open.md tracks/mz-constants/theory/open-upper-limit.md tracks/mz-constants/theory/open-padua-target.md literature/records/mz-mean-convergence-screen.md topics/mz-constants/audit-01.md topics/mz-constants/audit-02.md topics/padua-batch-20261031/ALLOCATIONS.md
sed -n '1,45p' topics/mz-constants/audit-01.md
sed -n '100,150p' literature/records/mz-mean-convergence-screen.md
rg -n 'deferred|certif|fast|classification' state/IDEAS.md
```

The combined canonical-source read was output-truncated in historical audit-01 material; its verdict/coverage beginning was separately reread. This is bounded administrative comparison, not a claim of full historical audit coverage.

An inline Python check executed the following exact substantive assertions (with `git(*a)` defined as `subprocess.check_output(['git',*a])`, `base` and `ready` set to the full SHAs above):

```python
changed=git('diff','--name-only',base).decode().splitlines()
assert set(changed)=={'state/CURRENT.md','topics/mz-constants/LOG.md','topics/padua-batch-20261031/ALLOCATIONS.md'},changed
old=git('show',base+':state/CURRENT.md');new=Path('state/CURRENT.md').read_bytes();assert old.split(b'MZ track')[0]==new.split(b'MZ track')[0]
p='topics/padua-batch-20261031/ALLOCATIONS.md';old=git('show',base+':'+p);new=Path(p).read_bytes()
assert old.split(b'## Final reservations')[1].split(b'## Members')[0]==new.split(b'## Final reservations')[1].split(b'## Members')[0]
owner=b'**Allocation owner: the root Codex MZ orchestrator.**';assert owner in old and owner in new
assert git('rev-parse',base+'^{tree}')==git('rev-parse',ready+'^{tree}')
assert subprocess.run(['git','merge-base','--is-ancestor',ready,base]).returncode==0
assert git('show','-s','--format=%P',base).decode().split()==['08fafe62d9798385dfafaacc9a41344272737e68',ready]
```

Result: all assertions PASS; `git branch --show-current` returned `codex/mz-postmerge-frontier-20261031`. File hashes below were computed with `hashlib.sha256(Path(p).read_bytes()).hexdigest()`.

## Reviewed identities

Hashes pin the reviewed working snapshots, not a future commit. Later edits require an impact check. Canonical source hashes identify the files consulted; they do not imply a complete proof audit.

| File | SHA-256 |
|---|---|
| `AGENTS.md` | `60bfe28edf232c69948efdd2f7a48edfd99af52644513a2fc378c866e742cb60` |
| `agents/WORKFLOW.md` | `b1c1c14c83e02bf38283159f81ec278ae336ab56c95d0c026b9ada3314d1ffaa` |
| `agents/codex/CODEX.md` | `28ca2976171a34860e2bf8d24292af6b92bee34ce22ba1e497891b366533083b` |
| `state/CURRENT.md` | `e46dbae3742565acb7c96148b632cec998b5e4ebf98c40878f26365c68e6cf31` |
| `topics/mz-constants/LOG.md` | `f3d77c3148a3d184455fb4dee4e17616cf1978e53b35154aafa34f3619ec795e` |
| `topics/padua-batch-20261031/ALLOCATIONS.md` | `4e7f0d145143af96061d566f7f593d04318ec3b1ec3e342becdaeed31d94248f` |
| `topics/mz-constants/POST_MERGE.md` | `7e5b652904d453648340c463e7bc88a80f36216c7186a3e462ffabcec6388714` |
| `topics/mz-postmerge-frontier-20261031/LOG.md` | `f7ce435539b433bb565d81eae44ce75fcbda5b310054e53072db93c91ffac976` |
| `topics/mz-postmerge-frontier-20261031/merge-verification.json` | `0343bc6ed387eb74235a2708b3574c67e1c087ce6c804cebd3b15ff2f622f560` |
| `tracks/mz-constants/theory/m2-sharp-constant-open.md` | `1a0310059d03746be25de5114c8ddb87fd113c400c12db2e9d7140ad56cabe41` |
| `tracks/mz-constants/theory/open-upper-limit.md` | `3a9b96df7a21995b986ea08271e9fa1bface2a1fd300029665a1462e95125c7c` |
| `tracks/mz-constants/theory/open-padua-target.md` | `3ab82f62455fec55436a3f087914c8fbd1bc0b68066494e0424a3be1975f4c66` |
| `literature/records/mz-mean-convergence-screen.md` | `58270d1eec08635db5fb1538de93a697b0e052805a1ccd9294fc3761bc93bb27` |
| `topics/mz-constants/audit-01.md` | `34ee03fcd864dd9cc8b62b61984d71ad8fc46587023f740c4b1e0ff398f3aa08` |
| `topics/mz-constants/audit-02.md` | `8f29e51808f41c34cd39c2acc348d751ddf02afd2075e19dc2c5910d197c4407` |
| `state/IDEAS.md` | `1686b5060fe185e1def687368e92b3b9c4bb929ead113cbc6f6c73e33798aea4` |

| `topics/mz-postmerge-frontier-20261031/checks.json` | `8ff7815e022657e6c3dc4cdb686e4901740ecff8992aba20711f2efe3c600d9c` |

## Final snapshot impact check

The orchestrator completed LOG and added checks.json during review. I reread both using `cat topics/mz-postmerge-frontier-20261031/LOG.md topics/mz-postmerge-frontier-20261031/checks.json`. LOG only adds verification counts and pending-Claude wording. An independent inline Python check enumerated `git ls-tree -r --name-only BASE`, excluded the three allowed modified paths, asserted the resulting count equals 308, and compared each remaining file byte-for-byte with `git show BASE:PATH`: all passed. I also verified every checks.json file hash against current bytes and ran `git diff --check` successfully. The developer-reported 24-link check was inspected, not independently rerun. The hashes above reflect this final reviewed snapshot. No finding added.

## Limits and next step

No Git mutations, network requests or network mutations were performed by this reviewer. Only this report was written. No claim is made about live remote branch state, new propagation to other members, archival delivery or historical numerical reproducibility. The receipt's external PR metadata remains developer-reported; local commit topology and content identity were independently verified.

Suggested next prompt: `Claude (Sonnet 5.5 high): Audit the administrative post-merge frontier update against main at 07c5f5465d6de306aa81dbe8ca1f615295163864; preserve accepted results and allocations, and treat independent-protocol-01.md as supplemental only.`
