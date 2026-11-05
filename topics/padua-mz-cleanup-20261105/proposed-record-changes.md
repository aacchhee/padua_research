# Proposed shared-record changes — C5, 2026-11-05

Rules/input: ad503cb0603fc017444b0aa732240981eefa4d24. Codex
gpt-6.1-sol xhigh, mechanical housekeeping scope. Novelty gate not applicable:
these are pointers/status-preserving summaries of accepted results, with no
new mechanism or priority claim. No shared file was edited by this worker.

Apply only at PR preparation after refreshing main, checking the completed
C4 build and reconciling the audit. Add final cleanup IDs/results then, if
appropriate, without upgrading any measurement or rewriting historical scope.
The original old blocks were read at main 21dbfc9 and were reverified at
response head a64ef35 and current main aff30e8. A changed
upstream block requires a fresh semantic reconciliation, not blind replacement.

## PAPER_MAP.md — MZ manuscript row

Old:

```markdown
| Marcinkiewicz–Zygmund constants of Clenshaw–Curtis and Padua rules beyond half-exactness | strict upper threshold with endpoint constant2−4/N+4/N², endpoint logarithmic order, explicit fixed-ratio constants and signed Padua compression | [MZ source and build](tracks/mz-constants/paper/README.md) | PD-T013–019; PD-T021–026; PD-N004 | historical overlap and journal comparison; PD-T020/027/028 OPEN; no2D upper theorem | complete 15-page revised draft; original statements accepted in Claude audit-01 and response accepted in audit-02; development PR ready for AC decision; historical novelty unresolved, not for submission |
```

New:

```markdown
| Marcinkiewicz–Zygmund constants of Clenshaw–Curtis and Padua rules beyond half-exactness | explicit Clenshaw–Curtis spectral bounds and fixed-ratio constants; signed Padua compression, logarithmic spectral countersequences beyond half-exactness and a uniform continuous-input coefficient norm | [MZ source and build](tracks/mz-constants/paper/README.md) | PD-T013–019; PD-T021–026; PD-N004; PD-T295; PD-T297–299; PD-N105–107; PD-T?mz-cleanup-codex-01; PD-T?mz-cleanup-codex-02; PD-T?mz-cleanup-codex-03; PD-T?mz-cleanup-codex-04 (replace provisional aliases by final IDs at preparation) | PD-T020/027 OPEN; sharp signed spectral growth constants and effective all-degree onset; historical novelty unresolved, with PR21 comparisons at their eventual merged scope | revised manuscript scope/build in README; accepted 1-D and PR23 results retained; cleanup mathematics accepted at its stated scope by Claude audit-01; response/preparation pending; not for submission |
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
Claude [cleanup audit-01](../topics/padua-mz-cleanup-20261105/audit-01.md)
accepts the new mathematics at its stated scope; response and preparation
are separate. No finite positivity range,
first crossing theorem, sharp spectral constant or novelty clearance follows
from a float scan. The [manuscript README](../tracks/mz-constants/paper/README.md)
is the current scope/build record. Cold-storage delivery remains pending.
Only AC merges.

Updated: 2026-11-01. Owner: AC. Current integration: AC confirmed PR #10 next (2026-11-01); all other drafts will adjust after PR #10 merges. The original [charter](../topics/charter-unisolvence-20261031/LOG.md) and its historical pre-merge notes are preserved below.
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


## Response 01 registration proposals — no application during WORK

Prepared for audit findings F11 and F19 at response head `a64ef35`.
Everything below is literal text for later preparation, with provisional IDs
only. A final-ID map from the reserved ranges must replace each alias
consistently at preparation; the proposal does not allocate or reserve any
additional identifier. These proposed rows preserve the accepted scope and
all six retained candidate dispositions. No scientific registry is edited here.

### PROOF_STATUS.md — append a cleanup section

Old: no cleanup section or rows exist at the checked head. Append the following
new section at preparation, after a fresh ID/ledger check:

```markdown
## Signed Padua MZ cleanup — 2026-11-05

[Claude audit-01](topics/padua-mz-cleanup-20261105/audit-01.md) accepts the mathematics, computer-assisted reduction and MEASURED scopes at candidate 10898ad99882248e5e6f9d76641624146af97454; [response-01](topics/padua-mz-cleanup-20261105/response-01.md) resolves the record/provenance findings. The finite witnesses below are explicit trial directions, not extreme-eigenvalue brackets or a first-crossing theorem. The OPEN sharp-growth target is retained separately from the proved normalized one-sided bounds.

| ID | Statement and scope | Status | Status by mathematical part | Disposition / reason | Depends on | Theory file | Evidence / audit |
|---|---|---|---|---|---|---|---|
| PD-T?mz-cleanup-codex-01 | Signed Padua Gram form on Pi_(m-1) is indefinite at m=1101,1240,1600; explicit dyadic trial quotients lie in the recorded strict rational intervals | PROVED | Computer-assisted finite reduction; exact positive continuous norm and outward negative energy at each listed degree | Retained finite certification; no earliest crossing or smaller-degree positivity claim | PD-T101/106 signed kernel; Legendre orthogonality; FLINT/Arb producer trust and documented alternate IEEE/BLAS path | [finite theorem](topics/padua-mz-cleanup-20261105/theory/finite-indefiniteness.md) | Committed producer/checker code and small receipts; separate actual runs and independently regenerated Claude certificates; large artifact delivery PENDING; [audit-01](topics/padua-mz-cleanup-20261105/audit-01.md); [response-01](topics/padua-mz-cleanup-20261105/response-01.md) |
| PD-T?mz-cleanup-codex-02 | Odd-m fixed-index signed Padua weights satisfy m^4 w_jk/log m -> -16 e_j e_k (-1)^j, with whole-grid majorant 8192 | PROVED | Fixed retained indices before the limit; every odd m>=5 for the stated majorant | Retained odd-parity extension of PD-T295; no uniform moving-index asymptotic or sign classification | PD-T101/111 cardinal normalization; PD-T295's elementary tail/triangle estimates | [odd weights](topics/padua-mz-cleanup-20261105/theory/odd-weight-asymptotic.md) | Written proof, supplementary reconstruction and Claude audit; [audit-01](topics/padua-mz-cleanup-20261105/audit-01.md); [response-01](topics/padua-mz-cleanup-20261105/response-01.md) |
| PD-T?mz-cleanup-codex-03 | Odd-m admissible y carriers give opposite logarithmic signed energies; both extrema diverge over all integers at endpoint and each fixed ratio theta>1/2, while theta<=1/2 is exactly identity | PROVED | Odd packets proved by whole signed sums; all-integer synthesis combines PD-N105–107 | Retained parity completion; existence only, no feasible analytic-carrier onset or identification of the finite minimizing branch | PD-T?mz-cleanup-codex-02; PD-N105/106 Fejer conventions and even cases; PD-N107 | [odd carriers](topics/padua-mz-cleanup-20261105/theory/odd-carriers.md) | Written proof, exact parity checks and independent reconstructions; [audit-01](topics/padua-mz-cleanup-20261105/audit-01.md); [response-01](topics/padua-mz-cleanup-20261105/response-01.md) |
| PD-T?mz-cleanup-codex-04 | Exact continuous carrier norm limits give limsup lambda_minus/log m <= -c_minus and liminf lambda_plus/log m >= c_plus over all m, with exact constants in the record | PROVED | Positive exact norm limits and explicit normalized one-sided spectral bounds | Retained supporting quantitative result; constants not claimed optimal, and no existence/value of either sharp spectral limit | PD-N105/106; PD-T?mz-cleanup-codex-03; locally proved continuous mass/cosine-transform identities | [normalized bounds](topics/padua-mz-cleanup-20261105/theory/growth-carrier-bounds.md) | Analytic proof and independent checks; split from OPEN PD-T?mz-cleanup-codex-06; [audit-01](topics/padua-mz-cleanup-20261105/audit-01.md); [response-01](topics/padua-mz-cleanup-20261105/response-01.md) |
| PD-T?mz-cleanup-codex-05 | Twenty-three finite minimum-only observations and the predeclared higher-window logarithmic fit diagnostic | MEASURED | Exact recorded grids, residuals and fitted windows; local even sign window 1238–1240 | Finite evidence only; no monotonicity, earlier positivity, global first crossing or spectral limit inferred | Frozen definitions, copied numerical code and recorded receipts; PD-T300 historical fit baseline | [measurements](topics/padua-mz-cleanup-20261105/theory/finite-measurements.md) | Small scan summary and code; six rows separately rerun by Claude, not all 23; [audit-01](topics/padua-mz-cleanup-20261105/audit-01.md); [response-01](topics/padua-mz-cleanup-20261105/response-01.md) |
| PD-T?mz-cleanup-codex-06 | Determine existence and values of the even/odd logarithmic limits of lambda_minus(m,m-1) and lambda_plus(m,m-1), including their agreement and hence full-integer limits | OPEN | Separate parity limits, their values and agreement remain unresolved | Original C3 sharp-growth target retained; split-off PD-T?mz-cleanup-codex-04 supplies supporting one-sided bounds only | PD-N105/106 and PD-T?mz-cleanup-codex-03 show divergence; PD-T?mz-cleanup-codex-04 supporting bounds do not settle these limits | [sharp target](topics/padua-mz-cleanup-20261105/theory/sharp-growth-open.md) | No proof of either limit; MEASURED fits are not a premise; [audit-01 F11](topics/padua-mz-cleanup-20261105/audit-01.md); [response-01](topics/padua-mz-cleanup-20261105/response-01.md) |
```

### state/IDEAS.md — append all cleanup candidates and retained routes

Old: no cleanup candidate section exists. Append at preparation:

```markdown
## Signed Padua MZ cleanup — retained candidate records, 2026-11-05

Full mechanisms, predecessors, obstructions, separation/kill tests and outcome histories are preserved in the [gate/candidate records](../topics/padua-mz-cleanup-20261105/novelty-gate-math.md). These are local variants/retained routes, not historical-priority claims. [Claude audit-01](../topics/padua-mz-cleanup-20261105/audit-01.md) accepts the three developed mathematical variants at their stated scopes; [response-01](../topics/padua-mz-cleanup-20261105/response-01.md) adds the previously considered routes and complete fields requested by F21/F22 without a new mechanism or verdict change. No new PD-N is created merely for an abandoned interpretation or deferred proof route.

| ID / aliases | Exact candidate / closest predecessor / kill test | Disposition and durable record |
|---|---|---|
| IDEA?mz-cleanup-codex-01; dyadic outward-enclosure certifier; fixed-point trial-energy witness | Round a proposed total-degree polynomial to exact dyadic Legendre coefficients, compute positive norm exactly, and enclose its full signed nodal energy outward. Closest IDEA-058 and PD-T298/299; bounded implementation-variant precedent IDEA-343/344. Kill: an accepted-sign inconsistency, degree/norm failure or precision-straddling enclosure under the recorded feasibility criterion. | retained bounded implementation variant; finite PD-T?mz-cleanup-codex-01 PROVED at m1101/1240/1600. Distinct integer/Arb producer and forward-error checker paths; no eigenvalue accuracy premise or first-crossing theorem. |
| IDEA?mz-cleanup-codex-02; floor-half spectral triangle; odd-m logarithmic weights | Extend PD-T295 from even m to odd m with h_m=0, retaining the actual cardinal formula. Closest PD-T111's both-parity corner and IDEA-389's common weight support. Kill: a surviving exceptional logarithm or changed fixed-index phase/sign. | retained parity variant; PD-T?mz-cleanup-codex-02 PROVED at its fixed-index/whole-grid scopes. |
| IDEA?mz-cleanup-codex-03; y-carrier odd-grid packet; literal half-degree/naive-axis-swap subroutes | Use the genuinely even y mesh m+1 at odd m, with full signed-sum domination and exact total-degree budget. Closest IDEA-388/389/390/394; PD-N047 degree and PD-N048 full-signed-form obligations remain binding. Kill: failed parity isolation, degree budget or nonzero signed coefficient. | retained parity variant; PD-T?mz-cleanup-codex-03 PROVED. Literal T_(m/2)(x) and a naive axis swap are abandoned subroutes under this same candidate, with reasons retained; no duplicate theorem or PD-N. |
| IDEA?mz-cleanup-codex-04; continuous Fejer mass limit; normalized carrier coefficients | Compute exact continuous norms of inherited packets before converting signed energy coefficients to Rayleigh bounds. Closest IDEA-385/PD-T294, IDEA-071/PD-T020 and IDEA-389/390; PD-N048 prevents using negative corner mass alone. Kill: wrong rescaling, divergent/zero norm or already-covered normalization. | retained quantitative variant; PD-T?mz-cleanup-codex-04 PROVED supporting one-sided bounds. Original PD-T?mz-cleanup-codex-06 sharp-growth target remains OPEN. |
| IDEA?mz-cleanup-codex-05; sharp signed localization; matching logarithmic controls | Bound the complete signed nodal form with sharp continuous normalization to match opposite-direction logarithmic estimates. Closest PD-N048's corner-subtraction obstruction and the existing carrier/support records. Kill/resume test: a global full-signed estimate with explicit normalized error, not negative corner mass alone. | deferred, not rejected; resume only with the stated full-signed global estimate and exact normalization. OPEN PD-T?mz-cleanup-codex-06 remains the target; no PD-N assigned to an incomplete route. |
| IDEA?mz-cleanup-codex-06; raw-energy/same-branch interpretation | Interpret the measured slope near -1/9 as the raw PD-N105 carrier coefficient or identify the measured branch from it. Closest IDEA-253's record-discipline precedent and the accepted packet records. Kill: the raw numerator lacks the continuous norm denominator or branch identification is unsupported. | abandoned interpretation: raw-energy coefficients are not spectral coefficients and the fit identifies no eigenvector branch. Related PD-T?mz-cleanup-codex-05 stays MEASURED diagnostic evidence; no refutation of the OPEN spectral target and no PD-N. |
```

### ID_CROSSWALK.md — append local-to-final mapping template and sharp-target split

Old: no cleanup mappings exist. Append at preparation after substituting
freshly checked final IDs; `<final ...>` are literal preparation placeholders,
not allocations:

```markdown
## Signed Padua MZ cleanup — final mapping and preserved split

[Reservation](topics/padua-mz-cleanup-20261105/ALLOCATIONS.md) was first published in ee490356ce51d5e2f4a84f2c45e6ccb98a19bd90; final IDs are assigned from its permanent ranges after the live union recheck. No accepted ID is renumbered. All development aliases and route dispositions remain in [the candidate record](topics/padua-mz-cleanup-20261105/novelty-gate-math.md).

| Provisional alias | Final ID at preparation | Durable record / disposition |
|---|---|---|
| PD-T?mz-cleanup-codex-01 | <final finite theorem ID> | [finite theorem](topics/padua-mz-cleanup-20261105/theory/finite-indefiniteness.md); PROVED |
| PD-T?mz-cleanup-codex-02 | <final odd-weight ID> | [odd weights](topics/padua-mz-cleanup-20261105/theory/odd-weight-asymptotic.md); PROVED extension of PD-T295, not a split of its accepted statement |
| PD-T?mz-cleanup-codex-03 | <final odd-carrier ID> | [odd carriers](topics/padua-mz-cleanup-20261105/theory/odd-carriers.md); PROVED extension of PD-N105–107, not a relabeling |
| PD-T?mz-cleanup-codex-04 | <final normalized-bound ID> | [bounds](topics/padua-mz-cleanup-20261105/theory/growth-carrier-bounds.md); PROVED supporting result split from PD-T?mz-cleanup-codex-06 |
| PD-T?mz-cleanup-codex-05 | <final measurement ID> | [finite measurements](topics/padua-mz-cleanup-20261105/theory/finite-measurements.md); MEASURED |
| PD-T?mz-cleanup-codex-06 | <final sharp-target ID> | [original sharp target](topics/padua-mz-cleanup-20261105/theory/sharp-growth-open.md); OPEN; Split into PD-T?mz-cleanup-codex-04; supporting one-sided bounds do not prove existence/value of the spectral limits |
| IDEA?mz-cleanup-codex-01 | <final certifier candidate ID> | retained bounded implementation variant; PD-T?mz-cleanup-codex-01 |
| IDEA?mz-cleanup-codex-02 | <final odd-weight candidate ID> | retained parity variant; PD-T?mz-cleanup-codex-02 |
| IDEA?mz-cleanup-codex-03 | <final odd-carrier candidate ID> | retained parity variant with abandoned literal-half-degree/naive-swap subroutes; PD-T?mz-cleanup-codex-03 |
| IDEA?mz-cleanup-codex-04 | <final normalization candidate ID> | retained quantitative variant; PD-T?mz-cleanup-codex-04 |
| IDEA?mz-cleanup-codex-05 | <final localization candidate ID> | deferred; OPEN PD-T?mz-cleanup-codex-06 |
| IDEA?mz-cleanup-codex-06 | <final raw-interpretation candidate ID> | abandoned; no new theorem or PD-N |
```

The original-to-split mapping is **C3 sharp-growth target
PD-T?mz-cleanup-codex-06 (OPEN) -> supporting normalized carrier result
PD-T?mz-cleanup-codex-04 (PROVED)**. The original statement is preserved
verbatim in sharp-growth-open.md. This is not a decomposition of the target's
own assertions and does not make the OPEN target PARTIAL. PD-T295 and
PD-N105–107 are extended, not split or narrowed.

## Dated historical-row qualifiers — exact old/new text for preparation

The following replacements preserve each old statement and status as historical
scope, adding only a dated pointer to the separate cleanup record. They must
not retroactively certify PD-T300 or change AC's OPEN-plus-refuted display.

### state/IDEAS.md — historical PR23 introductory scope

Old:

```markdown
AC directs Status OPEN with REJECTED: refuted disposition for PD-T028/110/116, linked to PROVED PD-N105/106/107; their positive formulations are historical and unusable as assertions. PD-T114 is PROVED through PD-T297; the genuine 1D PD-T027 upper-limit/gap target stays OPEN. Every even-m carrier conclusion is existential without an effective onset, odd-m classification or sharp extremal rate. The finite m1600 float hit stays MEASURED and uncertified.
```

New:

```markdown
AC directs Status OPEN with REJECTED: refuted disposition for PD-T028/110/116, linked to PROVED PD-N105/106/107; their positive formulations are historical and unusable as assertions. PD-T114 is PROVED through PD-T297; the genuine 1D PD-T027 upper-limit/gap target stays OPEN. Every even-m carrier conclusion is existential without an effective onset, odd-m classification or sharp extremal rate. The finite m1600 float hit stays MEASURED and uncertified. Dated cleanup qualifier (2026-11-05): that is the historical PR23 scope; the separately proved finite PD-T?mz-cleanup-codex-01 now certifies negative directions at m1101/1240/1600, and PD-T?mz-cleanup-codex-02/03 supply the odd-parity completion. PD-T300 and its original float hit remain MEASURED in their own scope; sharp spectral limits remain OPEN under PD-T?mz-cleanup-codex-06.
```

### state/IDEAS.md — IDEA-389

Old:

```markdown
| IDEA-389; `IDEA?mz2d-frontier-codex-15` | exact even-node carrier exposes negative logarithmic mass; [full candidate](../topics/padua-mz-2d-frontier-20261105/ideas-f12.md) | Retained PROVED countersequence, [PD-N105](../topics/padua-mz-2d-frontier-20261105/theory/f12-eventual-negative-carrier.md): even m, negative logarithmic signed energy and bounded continuous norm. Existence only; no feasible finite witness/onset and no explanation of the uncertified m1600 float hit. |
```

New:

```markdown
| IDEA-389; `IDEA?mz2d-frontier-codex-15` | exact even-node carrier exposes negative logarithmic mass; [full candidate](../topics/padua-mz-2d-frontier-20261105/ideas-f12.md) | Retained PROVED countersequence, [PD-N105](../topics/padua-mz-2d-frontier-20261105/theory/f12-eventual-negative-carrier.md): even m, negative logarithmic signed energy and bounded continuous norm. Existence only; no feasible finite witness/onset and no explanation of the uncertified m1600 float hit. Dated cleanup qualifier (2026-11-05): the quoted uncertified-hit wording is historical PR23 scope. Separate PD-T?mz-cleanup-codex-01 certifies finite negative trial directions; the existential analytic carrier still supplies no feasible onset or explanation of that finite branch. |
```

### PROOF_STATUS.md — PD-T295

Old:

```markdown
| PD-T295 | Logarithmic fixed-node signed Padua weights and global summable majorant | PROVED | Even m; every fixed admissible j,k; whole-grid majorant under stated conventions | Retained common supporting theorem; no odd-m weight classification | PD-T101/111 cardinal normalization; elementary Fourier series | [PD-T295](topics/padua-mz-2d-frontier-20261105/theory/f12-local-weight-asymptotic.md) | Analytic proof; auditor weight-formula check; [Claude audit-01](topics/padua-mz-2d-frontier-20261105/audit-01.md) accepted candidate dee638408505c9977f3febd98fdd42c9bc512c92; [response-01](topics/padua-mz-2d-frontier-20261105/response-01.md) |
```

New:

```markdown
| PD-T295 | Logarithmic fixed-node signed Padua weights and global summable majorant | PROVED | Even m; every fixed admissible j,k; whole-grid majorant under stated conventions | Retained common supporting theorem; no odd-m weight classification Dated cleanup qualifier (2026-11-05): odd weights are separately proved in PD-T?mz-cleanup-codex-02; this accepted even-m statement is unchanged. | PD-T101/111 cardinal normalization; elementary Fourier series | [PD-T295](topics/padua-mz-2d-frontier-20261105/theory/f12-local-weight-asymptotic.md) | Analytic proof; auditor weight-formula check; [Claude audit-01](topics/padua-mz-2d-frontier-20261105/audit-01.md) accepted candidate dee638408505c9977f3febd98fdd42c9bc512c92; [response-01](topics/padua-mz-2d-frontier-20261105/response-01.md) |
```

### PROOF_STATUS.md — PD-T300

Old:

```markdown
| PD-T300 | Finite signed Padua spectral, localization and candidate-probe measurements | MEASURED | Endpoint rows through400; 476 screen rows m2..239 at n=m−1/m−2; separate minima800/1000/1200/1600; bounded probes | G2 INCONCLUSIVE; G3 original R1 killed in finite scope; G4 INCOMPLETE; m1600 negative float hit uncertified | Frozen definitions; recorded numerical code/receipts; no general spectral theorem | [PD-T300](topics/padua-mz-2d-frontier-20261105/theory/frontier-measurements.md) | Existing audit-accepted numerical-results/report and receipts transcribed; no new run or certification; [Claude audit-01](topics/padua-mz-2d-frontier-20261105/audit-01.md) accepted candidate dee638408505c9977f3febd98fdd42c9bc512c92; [response-01](topics/padua-mz-2d-frontier-20261105/response-01.md) |
```

New:

```markdown
| PD-T300 | Finite signed Padua spectral, localization and candidate-probe measurements | MEASURED | Endpoint rows through400; 476 screen rows m2..239 at n=m−1/m−2; separate minima800/1000/1200/1600; bounded probes | G2 INCONCLUSIVE; G3 original R1 killed in finite scope; G4 INCOMPLETE; m1600 negative float hit uncertified Dated cleanup qualifier (2026-11-05): the uncertified-hit wording is historical PR23 scope; separate PD-T?mz-cleanup-codex-01 certifies explicit finite witnesses. This measurement record remains MEASURED and is not retroactively certified. | Frozen definitions; recorded numerical code/receipts; no general spectral theorem | [PD-T300](topics/padua-mz-2d-frontier-20261105/theory/frontier-measurements.md) | Existing audit-accepted numerical-results/report and receipts transcribed; no new run or certification; [Claude audit-01](topics/padua-mz-2d-frontier-20261105/audit-01.md) accepted candidate dee638408505c9977f3febd98fdd42c9bc512c92; [response-01](topics/padua-mz-2d-frontier-20261105/response-01.md) |
```

### PROOF_STATUS.md — PD-N107

Old:

```markdown
| PD-N107 | Half-exactness is the sharp threshold for uniform signed strong MZ | PROVED | Theta<=1/2 exact; every fixed 1/2<theta<1 has opposite divergent extrema along even m | PD-T116 positive universal assertion REJECTED: refuted; counterexample alternative resolved; no odd-m classification | PD-T295; PD-N105/106; routine half-degree exactness | [PD-N107](topics/padua-mz-2d-frontier-20261105/theory/f3-fixed-ratio-threshold.md) | Analytic carrier specialization; independent reconstruction; [Claude audit-01](topics/padua-mz-2d-frontier-20261105/audit-01.md) accepted candidate dee638408505c9977f3febd98fdd42c9bc512c92; [response-01](topics/padua-mz-2d-frontier-20261105/response-01.md) |
```

New:

```markdown
| PD-N107 | Half-exactness is the sharp threshold for uniform signed strong MZ | PROVED | Theta<=1/2 exact; every fixed 1/2<theta<1 has opposite divergent extrema along even m | PD-T116 positive universal assertion REJECTED: refuted; counterexample alternative resolved; no odd-m classification Dated cleanup qualifier (2026-11-05): the even-m scope is unchanged; PD-T?mz-cleanup-codex-03 separately supplies odd carriers and all-integer synthesis. | PD-T295; PD-N105/106; routine half-degree exactness | [PD-N107](topics/padua-mz-2d-frontier-20261105/theory/f3-fixed-ratio-threshold.md) | Analytic carrier specialization; independent reconstruction; [Claude audit-01](topics/padua-mz-2d-frontier-20261105/audit-01.md) accepted candidate dee638408505c9977f3febd98fdd42c9bc512c92; [response-01](topics/padua-mz-2d-frontier-20261105/response-01.md) |
```


## Response verification and preparation boundary

At response head a64ef35 / main aff30e8, every replacement's literal old
block above occurs once in the named source file, including the preserved
CURRENT.md file-level owner/charter line. The appended registration sections
are absent at that head. The proposal changes only later registration text;
no existing mathematical statement, status, scientific evidence or accepted
ID is altered by this response. Preparation must regenerate and verify these
literal blocks if main changes, substitute the final mapping consistently,
and keep every unrelated registry/RESULTS.md section intact.
