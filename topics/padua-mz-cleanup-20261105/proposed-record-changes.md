# Proposed shared-record changes — C5, 2026-11-05

Rules/input: ad503cb0603fc017444b0aa732240981eefa4d24. Codex
gpt-6.1-sol xhigh, mechanical housekeeping scope. Novelty gate not applicable:
these are pointers/status-preserving summaries of accepted results, with no
new mechanism or priority claim. No shared file was edited by this worker.

Apply only at PR preparation after refreshing main, checking the completed
C4 build and reconciling the audit. Add final cleanup IDs/results then, if
appropriate, without upgrading any measurement or rewriting historical scope.
The exact old blocks below were read from current main21dbfc9. A changed
upstream block requires a fresh semantic reconciliation, not blind replacement.

## PAPER_MAP.md — MZ manuscript row

Old:

```markdown
| Marcinkiewicz–Zygmund constants of Clenshaw–Curtis and Padua rules beyond half-exactness | strict upper threshold with endpoint constant2−4/N+4/N², endpoint logarithmic order, explicit fixed-ratio constants and signed Padua compression | [MZ source and build](tracks/mz-constants/paper/README.md) | PD-T013–019; PD-T021–026; PD-N004 | historical overlap and journal comparison; PD-T020/027/028 OPEN; no2D upper theorem | complete 15-page revised draft; original statements accepted in Claude audit-01 and response accepted in audit-02; development PR ready for AC decision; historical novelty unresolved, not for submission |
```

New:

```markdown
| Marcinkiewicz–Zygmund constants of Clenshaw–Curtis and Padua rules beyond half-exactness | explicit Clenshaw–Curtis spectral bounds and fixed-ratio constants; signed Padua compression, logarithmic spectral countersequences beyond half-exactness and a uniform continuous-input coefficient norm | [MZ source and build](tracks/mz-constants/paper/README.md) | PD-T013–019; PD-T021–026; PD-N004; PD-T295–299; PD-N105–107 | PD-T020/027 OPEN; sharp signed spectral growth constants and effective all-degree onset; historical novelty unresolved, with PR21 comparisons at their eventual merged scope | revised manuscript scope/build in README; accepted 1-D and PR23 results retained; cleanup additions require their separate audit and preparation; not for submission |
```

## state/CURRENT.md — current signed-Padua section

Old:

```markdown
## Signed Padua MZ — accepted frontier, 2026-11-05

[Report](../topics/padua-mz-2d-frontier-20261105/report.md),
[results](../results/padua-mz-2d-frontier-20261105.md): PD-N105/106 prove that
signed minimum/maximum eigenvalues tend to minus/plus infinity along even m;
PD-N107 extends this to every fixed 1/2<theta<1 at n=floor(theta*m).
For 0<=theta<=1/2, exactness gives Gram identity and eta=0.
PD-T295 supplies the fixed-node weight asymptotics. PD-T297 proves
2<=||H_(m,n)||_(C→L2)<=28.3763348311…<30 for every m>=2 and 0<=n<m,
resolving PD-T114 at its unchanged endpoint target. The positive-reference
PD-T296 diamond theorem is separate and supplies no signed transfer.

This dated statement supersedes only the signed-Padua positive OPEN clauses
in the historical MZ/PR14 sections below. AC retains Status OPEN for
PD-T028/110/116 with binding **REJECTED: refuted** dispositions via
PD-N105/106/107; those historical positive assertions are neither unresolved
conjectures nor usable dependencies. The genuine 1-D sharp upper-limit/gap
target PD-T027 remains OPEN; PD-N104 and PD-T294 do not settle it.

PD-T298/299 prove the new finite m60/80 cases. Independent exact acceptance is
exactly m10/20/30/40/60/80; producer coverage 2..60 plus80 is not a gap-free
independently certified 2..80 range. PD-T300 retains only finite MEASURED
observations: m100 stopped without acceptance and the m1600 negative float hit
is uncertified. The analytic carriers prove existence only, give no effective
finite onset, and do not explain that float hit. Odd-m classification and sharp
extremal growth remain open. G2 is INCONCLUSIVE, the G4 original screen is
INCOMPLETE through239, and G5 was NOT RUN.

[Claude audit-01](../topics/padua-mz-2d-frontier-20261105/audit-01.md) accepted
the mathematics and statuses; [response-01](../topics/padua-mz-2d-frontier-20261105/response-01.md)
disposes of the editorial findings. Shared registration and preparation checks are complete for
PR23; it is prepared for AC’s review/merge decision, without approving another draft PR. Detailed preparation stage and checks
remain in the [topic log](../topics/padua-mz-2d-frontier-20261105/LOG.md), rather
than becoming a continuing research task. After merge, the scoped results and
remaining mathematical questions above are the frontier. External cold-storage
delivery remains pending and nonblocking: no accepted claim requires retained
bulk, since the checker regenerates exact pencils. No manuscript, submission or
historical-priority claim is added. Only AC merges.

Updated: 2026-11-01. Owner: AC. Current integration: AC confirmed PR #10 next (2026-11-01); all other drafts will adjust after PR #10 merges. The original [charter](../topics/charter-unisolvence-20261031/LOG.md) and its historical pre-merge notes are preserved below.
```

New:

```markdown
## Signed Padua MZ — accepted frontier and cleanup

The accepted [PR23 report](../topics/padua-mz-2d-frontier-20261105/report.md)
and [results](../results/padua-mz-2d-frontier-20261105.md) prove opposite
signed spectral divergence along even m (PD-N105/106), and its extension to
every fixed 1/2<theta<1 (PD-N107). Exactness gives Gram identity for
0<=theta<=1/2. PD-T295 supplies even-m fixed-node logarithmic weights.
PD-T297 proves 2<=||H_(m,n)||_(C→L2)<=28.3763348311…<30 for every
m>=2,0<=n<m, resolving PD-T114. PD-T296 is a separate positive-reference
diamond theorem and never a signed transfer.

AC retains registry Status OPEN for PD-T028/110/116 with binding
**REJECTED: refuted** dispositions via PD-N105/106/107. Their historical
positive statements are neither unresolved conjectures nor usable dependencies.
PD-T020 and the genuine one-dimensional PD-T027 remain OPEN; the scoped
PD-N104 intermediary obstruction and PD-T294 do not resolve PD-T027.

PD-T298/299 certify m60/80; independent inherited coverage is exactly
m10/20/30/40/60/80, not a gap-free independently certified 2..80 range.
PD-T300 is finite MEASURED evidence only. Its original m1600 negative hit
was uncertified in PR23; original G2 is INCONCLUSIVE, G4 is INCOMPLETE
through239, and G5 was NOT RUN. Those historical scopes remain unchanged.

The separate [cleanup report](../topics/padua-mz-cleanup-20261105/report.md)
and [results](../results/padua-mz-cleanup-20261105.md) record subsequent finite
witness, parity and growth-constant work at their individual statuses, plus
[manuscript integration](../topics/padua-mz-cleanup-20261105/manuscript-changes.md).
New results require the cleanup audit/preparation; no finite positivity range,
first crossing theorem, sharp spectral constant or novelty clearance follows
from a float scan. The [manuscript README](../tracks/mz-constants/paper/README.md)
is the current scope/build record. Cold-storage delivery remains pending.
Only AC merges.
```

## tracks/mz-constants/README.md — final frontier paragraph

Old:

```markdown
The new exact finite cases [PD-T298 m60](../../topics/padua-mz-2d-frontier-20261105/theory/cert-finite-extension.md) and [PD-T299 m80](../../topics/padua-mz-2d-frontier-20261105/theory/cert-finite-extension-m80.md) have actual independent acceptances, in addition to inherited m10/20/30/40. This is no gap-free certified2..80 range. [PD-T300](../../topics/padua-mz-2d-frontier-20261105/theory/frontier-measurements.md) preserves finite measurements only: G2 INCONCLUSIVE, G4 INCOMPLETE through239, and the separate m1600 float minimum uncertified. The analytic carriers prove existence only, give no effective onset, and do not explain or certify that float observation. Odd-m behavior, sharp growth and finite thresholds remain open. Cold-storage delivery remains pending; no scientific campaign was rerun for preparation.
```

New:

```markdown
The new exact finite cases [PD-T298 m60](../../topics/padua-mz-2d-frontier-20261105/theory/cert-finite-extension.md) and [PD-T299 m80](../../topics/padua-mz-2d-frontier-20261105/theory/cert-finite-extension-m80.md) have actual independent acceptances, in addition to inherited m10/20/30/40. This is no gap-free certified2..80 range. [PD-T300](../../topics/padua-mz-2d-frontier-20261105/theory/frontier-measurements.md) preserves only the original finite measurements and gate dispositions. The later [MZ cleanup](../../topics/padua-mz-cleanup-20261105/report.md), [results](../../results/padua-mz-cleanup-20261105.md) and [manuscript changes](../../topics/padua-mz-cleanup-20261105/manuscript-changes.md) record subsequent finite-witness/parity work at its own status and audit scope. The [manuscript scope and build](paper/README.md) now include signed Padua logarithmic spectral countersequences beyond half-exactness and the uniform C→L2 coefficient norm. Sharp growth constants, effective all-degree thresholds, PD-T027 and historical novelty retain their explicitly recorded unresolved scope. [Cold-storage delivery](../../topics/padua-mz-cleanup-20261105/COLD_STORAGE.md) remains pending; no external delivery is implied by a local stage.
```
