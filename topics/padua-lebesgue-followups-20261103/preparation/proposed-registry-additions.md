# Concrete shared-record additions proposed for T2–T4

Dated 2026-11-05 status supersession: [Claude audit-01](../audit-01.md)
accepts the mathematics; [response-01](../response-01.md) answers the minor
findings. Earlier pending/absent-audit wording and PENDING markers below are
retained proposal history/placeholders, not the current audit status. Preparation
must replace those markers with the actual evidence when applying the proposals.
The T2/T3 protocol deviation remains recorded for AC; no proposal is applied here.

Proposal only, 2026-11-03. Prepared by bounded Codex mechanical worker
(configured gpt-6.1-sol medium), under rules read at
`3f5196cf3639407c25b021fa30f70cc1d3ae113a`. Read against shared files
in the working tree at `66eaf855ffd6c68f929996df0621032c4364af7d`.
No shared file is changed and no final ID is assigned. These are literal
additive old→new snippets for later preparation after the required Claude
audit and a fresh allocation check. All six theorem IDs and three candidate
IDs below remain provisional. The `unassigned` crosswalk values are deliberate
proposal markers, not final mappings. A preparation commit must replace them
with actual reserved-range assignments and preserve these provisional aliases.

The scientific scope comes from the six theory files, gates T2/T3 and T4,
report, and supplementary independent analytic check. No novelty or priority
claim is proposed. Mathematical PROVED labels describe the written local
proofs; Claude audit is PENDING. Supplementary Astra checking does not constitute
Claude audit or clean prospective protocol clearance.

The T2/T3 timing qualification is mandatory in every summary that could imply
protocol acceptance: the initial complete registry/obstruction screen and
inherited-theory reading preceded derivation, but some linked full candidate
and attempt bodies were read later. Later coverage completion and successful
mathematical checks do not retroactively satisfy the prospective gate.

Existing PD-T180/184 proposals and T1 source comparison remain owned by the
orchestrator in [proposed-record-changes.md](../proposed-record-changes.md).
That file also supplies the proposed PD-T098/211/230 row annotations. Do not
apply duplicate replacements from this document. Here the PD-T098 annotation
is purely additive and preserves the original sharp target verbatim.

## PROOF_STATUS.md — six additive theorem rows

Old: no rows for these six provisional IDs.

New: append this section, using the existing eight-column registry schema.
At preparation, give the section its actual dated/audited stage; until then
retain the explicit PENDING language below.

```markdown
## Padua Lebesgue follow-ups — scoped T2–T4 results

Written development claims; required Claude audit PENDING. Supplementary independent analytic reconstruction/reruns are recorded separately. T2/T3 gate timing is qualified: some linked predecessor candidate/attempt bodies were read after initial derivation; subsequent reading does not provide prospective protocol clearance. No historical novelty claim.

| ID | Statement and scope | Status | Status by mathematical part | Disposition / reason | Depends on | Theory file | Evidence / audit |
|---|---|---|---|---|---|---|---|
| PD-T?lebesgue-followups-codex-t2-01 | Both limiting edge-defect integrals are reflection symmetric and strictly decrease on (0,pi/2]; unique central minima g_v(pi/2)=g and g_h(pi/2)=1 | PROVED | Exact one-dimensional representations, strict monotonicity and central values proved analytically | Retained variant with explicit position comparison; no finite-degree ordering or effective threshold | PD-T211/212 definitions; PD-T187/188 central normalization | [record](topics/padua-lebesgue-followups-20261103/theory/t2-01-edge-centre-minima.md) | [supplementary independent check](topics/padua-lebesgue-followups-20261103/independent-checks-analytic.md); [qualified gate](topics/padua-lebesgue-followups-20261103/gate-t2-t3.md); Claude audit PENDING |
| PD-T?lebesgue-followups-codex-t2-02 | Common endpoint expansion g_e(beta)=(8 log(2)/pi^2) log(1/d)+1/3+12 log(2)^2/pi^2+O(d), d=min(beta,pi-beta), e=v,h | PROVED | Explicit bounds in sin(beta) and d in the linked theorem; both endpoints | Retained consequence; endpoint limit belongs to the limiting integrals, with no interchange with n→infinity | PD-T?lebesgue-followups-codex-t2-01; PD-T211/212 definitions | [record](topics/padua-lebesgue-followups-20261103/theory/t2-02-common-endpoint-expansion.md) | [supplementary independent check](topics/padua-lebesgue-followups-20261103/independent-checks-analytic.md); [qualified gate](topics/padua-lebesgue-followups-20261103/gate-t2-t3.md); Claude audit PENDING |
| PD-T?lebesgue-followups-codex-t3-01 | Computable general-position geometric series and explicit tails for both edge-defect integrals, every beta in (0,pi) | PROVED | Vertical expansion ratio at most 1/2; two horizontal charts select a ratio at most 1/2; exact central specialization | Retained variant of PD-T188; pointwise angle scope, endpoint prefactors may grow; finite evaluations are verification records | PD-T?lebesgue-followups-codex-t2-01/02; PD-T188 central identification | [record](topics/padua-lebesgue-followups-20261103/theory/t3-01-general-position-series.md) | [verification](topics/padua-lebesgue-followups-20261103/evidence/t3-verification.md); [independent check and actual reruns](topics/padua-lebesgue-followups-20261103/independent-checks-analytic.md); [qualified gate](topics/padua-lebesgue-followups-20261103/gate-t2-t3.md); Claude audit PENDING |
| PD-T?lebesgue-followups-codex-t4-01 | Parity-independent limit kappa=lim_n(Lambda_c(n)-L_n^2), positive integral and geometric coefficient series | PROVED | Full integer sequence; explicit error at n>=32 bounded by 604 n^(-1/5)+((log n+2)^2+1)/(n+1); exact geometric tail | Retained constant-term split from PD-T098; sharp correction/remainder excluded | PD-T159 exact corner deformation and bound; PD-T101 through PD-T159 | [record](topics/padua-lebesgue-followups-20261103/theory/t4-01-corner-defect-limit.md) | Written analytic proof; [gate](topics/padua-lebesgue-followups-20261103/gate-t4.md); [supplementary independent check](topics/padua-lebesgue-followups-20261103/independent-checks-analytic.md); Claude audit PENDING |
| PD-T?lebesgue-followups-codex-t4-02 | For every integer n>=1, absolute difference between L_n and (2/pi)(log n+gamma+log(8/pi)) is at most 1/(4n^2) | PROVED | Both parities; locally proved harmonic-tail and midpoint-rule bounds | Retained substantive one-dimensional supporting theorem; sharpens PD-T158's predecessor 2/n estimate to 1/(4n^2); no sharp corner correction inferred | PD-T159 definition of L_n; PD-T?lebesgue-followups-codex-t4-01 local cotangent identity | [record](topics/padua-lebesgue-followups-20261103/theory/t4-02-one-dimensional-remainder.md) | Written analytic proof; [supplementary independent check](topics/padua-lebesgue-followups-20261103/independent-checks-analytic.md); Claude audit PENDING |
| PD-T?lebesgue-followups-codex-t4-03 | Lambda_c(n)=(4/pi^2)log^2 N+b log N+c+R_n, N=n+1/2; parity-independent c=c1^2+kappa and explicit R_n→0 | PROVED | Explicit n>=32 bound in theorem; rigorous decimal brackets for kappa and c via geometric tail plus outward Arb arithmetic | Retained constant-term split; original PD-T098 with -1/N and O(log N/N^2) remains OPEN; no global argmax consequence | PD-T?lebesgue-followups-codex-t4-01/02; PD-T159/158 elementary bounds | [record](topics/padua-lebesgue-followups-20261103/theory/t4-03-corner-constant.md) | [developer enclosure](topics/padua-lebesgue-followups-20261103/evidence/t4-constant.json); [independent proof check and enclosure reruns](topics/padua-lebesgue-followups-20261103/independent-checks-analytic.md); Arb outward arithmetic trusted; Claude audit PENDING |
```

Old: no dated T2–T4 follow-up annotation after the PD-T098 row.

New: append the following paragraph to the new topic section (or use the root
proposal's equivalent row annotation once, never both).

```markdown
PD-T098 retains its original statement and OPEN status, including the -1/N correction and O(log N/N^2) remainder. Its constant-term consequence is proved separately as PD-T?lebesgue-followups-codex-t4-03, with defect-limit and one-dimensional supporting splits PD-T?lebesgue-followups-codex-t4-01/02. This is not a proof of the full sharp expansion and does not silently narrow the original target. PD-T211/212/230 retain their existing statements and statuses; their excluded limiting-integral centre-minimality obligation is discharged separately by PD-T?lebesgue-followups-codex-t2-01, with endpoint expansion in t2-02. No finite-degree or effective-rate obligation is discharged by these integral theorems.
```

## state/IDEAS.md — three retained candidate records and route memory

Old: no `Padua Lebesgue follow-ups — T2–T4` section or rows for these aliases.

New: append the following literal section. These are candidate dispositions,
not extra mathematical status IDs or a claim of novel mechanisms.

```markdown
## Padua Lebesgue follow-ups — T2–T4

Three retained variants at bounded repository-search scope; no historical novelty claim. Required Claude audit PENDING. For T2/T3, some linked full predecessor candidate/attempt bodies were read after initial derivation; later completed coverage and supplementary mathematical checks do not retroactively satisfy the prospective gate. Full timing and predecessor records: [qualified T2/T3 gate](../topics/padua-lebesgue-followups-20261103/gate-t2-t3.md), [T4 gate](../topics/padua-lebesgue-followups-20261103/gate-t4.md).

| ID / aliases | Exact candidate / closest predecessor / kill test | Disposition and durable record |
|---|---|---|
| IDEA?lebesgue-followups-codex-t2-01; exact-switch integration; edge-defect centre minimum | Compare both literal inherited integrals at different macroscopic angles via exact switch/one-dimensional integration. Closest IDEA-304/318/324/326/332, PD-T188/211/212/230 and MEASURED PD-T207/208 profiles. Dated 2026-11-05 F1 comparison: finite measured profile vs proved limiting-integral ordering; finite-n cell ordering is a different object. Separate exact position comparison distinguishes this variant. Kill: a wrong reflection identity, numerator normalization or reversed minimum; an already stated exact comparison would consolidate as duplicate. | retained; both unique centre minima and common endpoint expansion PROVED in [t2-01](../topics/padua-lebesgue-followups-20261103/theory/t2-01-edge-centre-minima.md)/[t2-02](../topics/padua-lebesgue-followups-20261103/theory/t2-02-common-endpoint-expansion.md). Finite-n E-P obstruction PD-N080 does not reject limiting-integral ordering. Gate timing qualification above; Claude audit PENDING. |
| IDEA?lebesgue-followups-codex-t3-01; arbitrary-position evaluation; two-chart geometric series | Extend IDEA-304/PD-T188 from central angle to every beta in (0,pi), with computable geometric tails. Closest entries also IDEA-318/324 and MEASURED PD-T207/208 (PD-T208 left the general-beta series underived). Dated 2026-11-05 F1 separation: finite measured profile vs proved limiting-integral ordering and all-interior-angle evaluation; finite-n ordering is a different object. Kill: switch/normalization mismatch, wrong central specialization or invalid truncation bound. | retained variant; [t3-01](../topics/padua-lebesgue-followups-20261103/theory/t3-01-general-position-series.md) PROVED, pointwise angle scope; selected ratio at most 1/2, no uniform endpoint prefactor. Exact-series/outward-quadrature reruns are verification; original-double-integral floating diagnostic is MEASURED, not a premise. Gate timing qualification above; Claude audit PENDING. |
| IDEA?lebesgue-followups-codex-t4-01; signed odd-offset deformation; parity-free corner constant | Strengthen IDEA-287/288 and PD-T159's bounded signed deformation to convergence with explicit remainder; preserve exact endpoint weights. Kill: a missed surviving endpoint term, wrong limit or parity dependence. | retained variant completing the constant-term portion of PD-T098; [t4-01](../topics/padua-lebesgue-followups-20261103/theory/t4-01-corner-defect-limit.md), [t4-02](../topics/padua-lebesgue-followups-20261103/theory/t4-02-one-dimensional-remainder.md), [t4-03](../topics/padua-lebesgue-followups-20261103/theory/t4-03-corner-constant.md) PROVED at written scope. Sharp -1/N and O(log N/N^2) goals remain OPEN/deferred; Claude audit PENDING. |

Route memory retained under these same candidates: PD-T188's unshifted central alternating Taylor series is an equivalent existing central check, not a new mechanism. The complementary elliptic K expansion is valid but degenerates as a single global numerical chart; retained as the endpoint chart paired with a centre chart. A heavy interval mesh for centre-minimality was unused after the exact proof, with no failure or PD-N assigned. No separate sharp-remainder mechanism was generated after the T4 core stopping criterion. Two finite PSLQ searches (two recorded bases, coefficient height 10^6, tolerance 1e-85, max 1000 steps, 110 digits) found no relation; this is MEASURED evidence, not independence or universal closed-form exclusion. Exact bases and commands remain in [T4 attempt](../topics/padua-lebesgue-followups-20261103/attempts/T4.md) and [receipt](../topics/padua-lebesgue-followups-20261103/evidence/t4-relations.json).
```

## ID_CROSSWALK.md — additive provisional map and original-to-split history

Old: no section for this topic's six T2–T4 theory aliases or three candidates.

New: append this section only at preparation, resolving `unassigned` then.
The topic ledger link is a link to an existing reservation, not a new reservation
or a grant of priority from this proposal.

```markdown
## Padua Lebesgue follow-ups — T2–T4 aliases and scoped splits

Owner branch `codex/padua-lebesgue-followups-20261103`; scientific base `440d1079e42c3ef21c40d1cf8870f5b206410c6a`; rules/input `3f5196cf3639407c25b021fa30f70cc1d3ae113a`. [Permanent topic reservation](topics/padua-lebesgue-followups-20261103/ALLOCATIONS.md). No alias is silently renumbered; final assignments require a fresh live union scan. Required Claude audit PENDING; T2/T3 timing qualification remains in the [gate](topics/padua-lebesgue-followups-20261103/gate-t2-t3.md).

| Provisional alias | Final ID | Input / ownership | Canonical record | Disposition / scope |
|---|---|---|---|---|
| PD-T?lebesgue-followups-codex-t2-01 | unassigned | codex/padua-lebesgue-followups-20261103 | [record](topics/padua-lebesgue-followups-20261103/theory/t2-01-edge-centre-minima.md) | PROVED limiting-integral centre minima only |
| PD-T?lebesgue-followups-codex-t2-02 | unassigned | codex/padua-lebesgue-followups-20261103 | [record](topics/padua-lebesgue-followups-20261103/theory/t2-02-common-endpoint-expansion.md) | PROVED endpoint expansion of limiting integrals |
| PD-T?lebesgue-followups-codex-t3-01 | unassigned | codex/padua-lebesgue-followups-20261103 | [record](topics/padua-lebesgue-followups-20261103/theory/t3-01-general-position-series.md) | PROVED general-position series/tails |
| PD-T?lebesgue-followups-codex-t4-01 | unassigned | codex/padua-lebesgue-followups-20261103 | [record](topics/padua-lebesgue-followups-20261103/theory/t4-01-corner-defect-limit.md) | PROVED parity-independent defect limit/rate/series |
| PD-T?lebesgue-followups-codex-t4-02 | unassigned | codex/padua-lebesgue-followups-20261103 | [record](topics/padua-lebesgue-followups-20261103/theory/t4-02-one-dimensional-remainder.md) | PROVED one-dimensional all-n quadratic error |
| PD-T?lebesgue-followups-codex-t4-03 | unassigned | codex/padua-lebesgue-followups-20261103 | [record](topics/padua-lebesgue-followups-20261103/theory/t4-03-corner-constant.md) | PROVED c-term and explicit vanishing error; full PD-T098 OPEN |
| IDEA?lebesgue-followups-codex-t2-01 | unassigned | codex/padua-lebesgue-followups-20261103 | [record](topics/padua-lebesgue-followups-20261103/gate-t2-t3.md) | retained variant; gate timing qualification applies |
| IDEA?lebesgue-followups-codex-t3-01 | unassigned | codex/padua-lebesgue-followups-20261103 | [record](topics/padua-lebesgue-followups-20261103/gate-t2-t3.md) | retained arbitrary-position variant; gate timing qualification applies |
| IDEA?lebesgue-followups-codex-t4-01 | unassigned | codex/padua-lebesgue-followups-20261103 | [record](topics/padua-lebesgue-followups-20261103/gate-t4.md) | retained constant-term variant; sharper target deferred |

Original-to-split history: PD-T098's constant-term portion → PD-T?lebesgue-followups-codex-t4-03; its substantive supporting defect-limit and one-dimensional estimates → t4-01/t4-02. PD-T098 retains its exact original sharp expansion, including -1/N and O(log N/N^2), and remains OPEN. Excluded limiting-integral centre-minimality in PD-T211/212/230 → t2-01, with separate endpoint obligation → t2-02; their inherited finite-degree envelope statements are preserved. General-position evaluation extends PD-T188 → t3-01 without replacing or weakening PD-T188. These links confer no finite-n ordering, effective threshold, global argmax result or all-degree bridge. T1 PD-T180/184 completion/splits are recorded separately by the orchestrator.
```

## topics/README.md — append a topic entry

Old: no entry for this topic.

New:

```markdown
## Padua Lebesgue follow-ups — scoped development

[padua-lebesgue-followups-20261103](padua-lebesgue-followups-20261103/LOG.md), branch `codex/padua-lebesgue-followups-20261103`: [report](padua-lebesgue-followups-20261103/report.md), [reserved ranges](padua-lebesgue-followups-20261103/ALLOCATIONS.md). T2–T4 separately prove limiting edge-defect centre minima, endpoint expansion, general-position geometric evaluation and a parity-independent corner constant with explicit vanishing error. Six provisional theorem IDs and three retained candidates; full sharp PD-T098 remains OPEN. Required Claude audit PENDING; T2/T3 prospective-gate timing qualification retained. T1 completion is tracked separately in the report; no manuscript or priority claim.
```

## state/CURRENT.md — append scoped frontier paragraph

Old: no topic-specific T2–T4 frontier paragraph.

New:

```markdown
## Padua Lebesgue follow-ups — T2–T4 frontier

Dated 2026-11-05 supersession: the earlier CURRENT/RESULTS clauses leaving limiting-integral center-minimality and general-beta series OPEN are superseded at exactly the t2-01/t3-01 scopes below. The old clauses remain historical; finite-degree cell ordering and effective degree rates remain outside these theorems.

[Scoped report](../topics/padua-lebesgue-followups-20261103/report.md): PROVED local analytical results give unique limiting edge-defect centre minima (vertical g, horizontal exactly 1), common logarithmic endpoint expansion, arbitrary-position geometric series with explicit tails, and the parity-independent corner constant c with explicit R_n→0. The six records remain under provisional IDs in [theory](../topics/padua-lebesgue-followups-20261103/proposed-record-changes.md). PD-T098's full -1/N and O(log N/N^2) expansion remains OPEN; no finite-degree cell ordering, effective argmax threshold or finite all-degree bridge follows. Required Claude audit PENDING. T2/T3 some linked full predecessor records were read after initial derivation; the [qualified gate](../topics/padua-lebesgue-followups-20261103/gate-t2-t3.md) and [supplementary check](../topics/padua-lebesgue-followups-20261103/independent-checks-analytic.md) preserve this prospective-protocol limitation. Next: required Claude audit and dispositions before preparation; no historical novelty claim.
```

## PAPER_MAP.md — append a brief, not a manuscript

Old: no T2–T4 follow-up brief row.

New:

```markdown
## Padua Lebesgue follow-ups — scoped analytic brief

| Brief | Question | Supporting results | Remaining gaps | Readiness |
|---|---|---|---|---|
| [Lebesgue follow-ups T2–T4](topics/padua-lebesgue-followups-20261103/report.md) | Limiting edge-defect shape/evaluation and the Padua corner constant | PD-T?lebesgue-followups-codex-t2-01/02, t3-01, t4-01/02/03 at their individual written PROVED scopes | Full sharp PD-T098 OPEN; finite-degree ordering/effective argmax bridge excluded; historical novelty/source limits retained | Development brief only; required Claude audit PENDING; T2/T3 prospective-gate timing qualification preserved; no manuscript or submission claim |
```

## Literature index and results-view decisions

`literature/INDEX.md`: for T2–T4 the literal old→new is **unchanged → unchanged**.
These local proofs import no new external theorem and warrant no new literature
ID or coverage claim. LIT-388 is reused for the separately owned T1 primary-source
comparison; the orchestrator should append its final exact T1 scope once settled,
using [literature-comparison.md](../literature-comparison.md) and preserving all
historical addenda. This document deliberately does not freeze a T1 total.

`RESULTS.md`: append/replace only this topic's eventual own section from
`results/padua-lebesgue-followups-20261103.md`, under the orchestrator's ownership,
after synchronizing T1. No proposed replacement for another topic's section.
The literal T2–T4 content for that section can be the CURRENT paragraph above
with root-relative links and its next step updated at the actual stage.

No `theory/INDEX.md` exists; do not create one for this task. The genuinely needed
index link is the additive `topics/README.md` entry above. Do not add administrative
PD-N entries for an unused mesh, equivalent central series, deferred sharp goal
or finite unsuccessful PSLQ search.

## Before application: bounded unresolved choices

1. Required Claude audit and finding dispositions are absent; no proposal claims
   them. Retain the T2/T3 gate timing qualification after mathematical acceptance.
2. The final-ID mapping and audited input SHA must be filled by preparation,
   after a fresh live scan; none is selected here.
3. The orchestrator synchronized stale T4 supplementary-check status wording
   and repaired the odd-index TeX annotation. The independent report records
   the editorial old→new hash check; mathematical scope and code are unchanged.
4. Reconcile existing PD-T098/211/230 annotations with root proposals once;
   preserve original histories and exact sharp wording. T1 PD-T180/184, its
   LIT-388 addendum and combined results summary remain root-owned and evolving.
5. On actual preparation, replace PENDING stage text only with recorded evidence;
   do not publish these provisional crosswalk `unassigned` markers as final IDs.
