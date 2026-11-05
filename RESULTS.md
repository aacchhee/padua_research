# Padua research — results (merged view)

One section per topic. Each topic replaces only its own section, from its own `results/<topic-slug>.md`, at PR preparation and in its own PR (rule: `agents/WORKFLOW.md`). Earlier topics kept their results files on AC's computer; they are added here when their files are migrated.

## padua-mz-2d-20261101 — signed Padua MZ in two dimensions (PR #14, merged `e0d9e3d`, 2026-11-01)

- **Audit:** Claude audit-01 (Opus 5.5 xhigh) accepted the mathematics: 17 PROVED, 2 MEASURED, 3 OPEN. Response-01 fixed six record findings.
- **PROVED:**
  - Exact all-degree signed Padua aliases; the degree of exactness is precisely m (PD-T106).
  - A masked-tensor defect architecture of at most 160 terms (PD-T109).
  - Certified extreme-eigenvalue brackets at m=10/20/30/40 (PD-T107).
  - An m30 witness with η > 3/4 (PD-N044).
  - Corner weights negative for every m≥3, of size −(4 log m + O(1))/m⁴ (PD-T111).
  - Diamond-filter reconstruction (PD-T115).
  - Signed hyperinterpolation norm and reproduction degree (PD-T112/113); the endpoint operator reproduces only Π₁ (PD-N051).
  - Tensor-CC control with endpoint order log⁻² (PD-T117).
- **OPEN:**
  - λ_max < 2 for all m (PD-T110).
  - Positivity, endpoint order and η convergence for all m (PD-T028).
  - η(θ) < 1 at a fixed degree ratio (PD-T116).
  - A uniform operator norm (PD-T114).
- **Details:** [results/padua-mz-2d-20261101.md](results/padua-mz-2d-20261101.md)

## results-in-repo-20261101 — repository-only results tracking (PR #16, draft)

- **Rule (Codex audit-01 accepted it):**
  - Each topic keeps `results/<topic-slug>.md` in the repository.
  - This `RESULTS.md` is the merged view, updated in each topic's own PR.
  - All agent work must run from the cloud; AC's machine is only for unfetchable papers and cold storage.
- **Response:** response-01 corrected the migrated PR14 summary (audit F1–F3).
- **Details:** [results/results-in-repo-20261101.md](results/results-in-repo-20261101.md)

## padua-lanczos-drift-20261101 — finite-precision span drift in bivariate Lanczos (PR #15, draft)

- **Audits:** Claude audit-01 and Codex audits 02–04. Audit-04 accepted the final response; no PROVED or MEASURED claim was refuted.
- **PROVED:**
  - PD-T144: for the named Padua certificate, ρ_n = O(n⁻⁵), limsup n⁵ρ_n ≤ 20√2π⁴/9 (sharper ≈ 219.5). This splits PD-T075(U1); PD-T075 is now PARTIAL.
  - PD-T145: an explicit square-case √ε family (reading (E)).
  - PD-T136/137: the normal-quotient span derivative and rational certificates.
  - PD-T138: the formal scalar-CGS2 normal map.
  - PD-T139: the finite aggregate separation, κ ratio > 1126 on T24 and > 11.72 on rotated Q24.
  - PD-T141: the finite formal scalar separation, > 800 on T24 and > 7 on rotQ24 (thresholds post hoc).
  - PD-T142/143: a computed-polynomial span certificate and a fixed-degree selection criterion.
  - PD-N062: a fixed-degree closure lemma; projection-only rules cannot remove the drift.
  - PD-N063: three failed Padua witness paths.
- **MEASURED:**
  - PD-T140: the scalar experiment. Its factor-ten target is PARTIAL (T24 proved, rotQ24 OPEN).
  - PD-T146: public polyrat V+A span gaps of 0.0041 and 0.0102 at near-machine orthogonality.
- **OPEN:** all-degree drift, general staircase safety, PD-T055, PD-T075(U2) and PD-T056(G). Formal-model results imply no IEEE claim.
- **IDs:** PD-T136–146, PD-N062–063, IDEA-246–267.
- **Details:** [results/padua-lanczos-drift-20261101.md](results/padua-lanczos-drift-20261101.md)

## padua-proof-attempts-2-20261101


Stage PR (prepared for AC review); Claude Opus 5.5 xhigh audit-01 accepted for the stated scope, with minor findings answered in response-01. [PR12](https://github.com/aacchhee/padua_research/pull/12) is prepared after merged PR15; only AC merges.

- A2 PROVED: requested corner b coefficient, explicit absolute remainder ≤ 68; local results 01–04.
- A5 certification item PARTIAL by degree: closed counts 15, 27, 25, 41, 50 for n = 3–7 and separate corner-only globals. Degree 8 has at least 44 strict interior maxima; exact counts/global remain OPEN. PD-T100's measured-search status stays MEASURED.
- A4(a) PROVED at its central-envelope scope: R_cen = Λ_c − g + o(1), both parities, 0.548504986190 < g < 0.548525055355; exact all-four-edge formula. Full-square A4 and global runner-up identification remain OPEN.
- PD-N072 PROVED; specified S(α) REJECTED: refuted on positive n = 1, p = 1/10, M = 4 sections. Count 1/2 differs from valid reference count 1 at the required square-root gap. Other counts/reference existence are not refuted.
- B1 PROVED for generic exterior parallel real diagonal poles, every fixed admissible sample/finite T; literal even-count Ldiag taper except finitely many parameters. Other classes, fixed parameters and stability remain OPEN.

[Full report, proofs and evidence](topics/padua-proof-attempts-2-20261101/report.md).
Next: Codex (gpt-6.1-sol medium): Continue codex/padua-proof-attempts-2-20261101. Only AC merges.

Final registration: PD-T156–197; PD-N072–073; IDEA-286–311. [Exact ID map](topics/padua-proof-attempts-2-20261101/COLD_STORAGE.md). Reservation gaps PD-T198–205, PD-N074–077, IDEA-312–315 remain permanent.

## cold-storage-20261102


Branch: `claude/cold-storage-20261102`. Finalized 2026-11-03; Stage PR, ready for AC's merge decision. Claude developed the cleanup/response; Codex (AC-requested/configured gpt-6-astra high) independently accepted [audit-02](topics/cold-storage-20261102/audit-02.md). Backend model/effort metadata is not separately exposed.

- **Cleanup.** 176 files, **15,846,089 bytes**, archived from nine topic/track directories. Git-measured batches: 163 / 15,418,937 bytes and 13 / 427,152 bytes. Every artifact retains its exact source commit/path/blob, size and SHA-256; all 176 identities verify. No mathematical claim, status or ID changes.
- **Retrieval.** Complete command/reader metadata and superseding human correction sections remain committed. The POSIX tool preflights collisions, protects tracked/local files, uses no-follow traversal, reads exported payloads back before issuing v2 receipts and verifies transferred archives without Git using `verify-archive DIR --manifest M`.
- **Validation.** 23 storage tests and 8 independently written fault controls pass; all nine manifests verify. Charter and track-MZ export/verify/clean cycles pass with 11 direct source-byte comparisons. Audit-01's three scientific outputs and historical patch remain byte-identically reproduced; audit-02 changes no science.
- **Integration.** PR #18 first. A disposable squash rehearsal against PR #17 reference head `cdb12257af24ea2542de707b9730f8278d69a168` finds two later conflicts, both shared tool files; keeping PR #18's audited versions resolves them and passes all 23 storage tests. PR #17's branch was not changed or declared ready here.
- **Separate archival work.** AC delivery is unconfirmed, native Windows is unsupported, WSL/drvfs is untested, and no history purge was performed. Current retrieval uses Git objects. A purge needs independently verified physical archives, preserved code/metadata and migrated locators; an export receipt alone is insufficient.

All assigned repository work is complete under AC's instruction to finalize without more Claude rounds. No further agent continuation is requested. [PR #18](https://github.com/aacchhee/padua_research/pull/18) is for AC alone to merge. [Log](topics/cold-storage-20261102/LOG.md) · [audit evidence](topics/cold-storage-20261102/audit-02/receipt.json).

## padua-argmax-alln-20261101

Branch:`claude/padua-argmax-alln-20261101`; [PR17](https://github.com/aacchhee/padua_research/pull/17).
2026-11-03. Codex gpt-6.1-sol high final preparation under AC's instruction
to finalize without another Claude round. Original mathematical acceptance:
[Claude audit-01](topics/padua-argmax-alln-20261101/audit-01.md);
response-01 accepted by [response review](topics/padua-argmax-alln-20261101/response-review-01.md);
CS1–CS3 resolved by [audit-03](topics/padua-argmax-alln-20261101/audit-03-storage-repair.md).
Distinct Astra high [final preparation audit](topics/padua-argmax-alln-20261101/prep-support/final-audit.md) and [actual-main integration audit](topics/padua-argmax-alln-20261101/prep-support/integration-audit.md) both PASS within their stated scopes; no unresolved preparation finding remains.

- **PROVED PD-T229:** for every sufficiently large degree, exactly the two
  physical nonnode corners are global maximizers. N_* is existential and
  non-effective. [Eventual theorem](topics/padua-argmax-alln-20261101/theory/gated-codex-15-eventual-global-argmax.md).
- **PROVED finite2–16:** PD-T209(n2), inheritedPD-T162/166/169/174/177(n3–7),
  reusedPD-T181(n8),PD-T214(n9–16), with correctnessPD-T210. Exact/outward
  arithmetic and independent replays; no degree>=17 global certificate.
- **PROVED support PD-T211/212/215–228/230:** compact edge gaps,
  two-phase/finite-defect localization, exact row identities, physical
  first variation and reflection-first local bound. PD-T231 proves ten
  finite whole-cell E-C comparisons atn7/12. All-n E-C remains OPEN.
- **PROVED negatives PD-N078/079/080:** only tie-inclusive O-Lt,
  primitive coset-maximality/pure-quadratic gain, and common-phase E-P
  translation. They do not reject PD-T099 or every pairing method.
- **MEASURED PD-T206/207/208/213/232–235:** original finite observations,
  profile/pairing screens and newly rehomed D1/D2/D3 diagnostics. Scoped
  **MEASURED PD-N081/082/083** preserve numerical O-R/T2/T3 failures and
  their optimizer/stabilization limits; no universal negative inferred.

**PD-T099 remains OPEN.** Finite2–16 plus eventualn>=N_* leave the unknown
finite bridge17<=n<N_*. General-beta series, center-minimality, all-n
slope/energy and effective entry remain OPEN. The authorized campaign
stopped at6/2/1rounds; no further research round was run.

All37scientific records and20precise candidate formulations have permanent
IDs/aliases under the [unchanged reservations](topics/padua-argmax-alln-20261101/ALLOCATIONS.md).
PD-T236–245 andLIT460–465 remain permanent unused gaps. [Canonical candidates](topics/padua-argmax-alln-20261101/FINAL_CANDIDATES.md)
preserve every history, split and scoped close-out. No manuscript or novelty
clearance is claimed.

Optimization hardening refuses -O/-OO/PYTHONOPTIMIZE for active proof
acceptance entry points; mathematical predicates/frozen certificates are
unchanged. Exact enumerated hardening-delta source-version adapters permit historical
certificate pins. Developer and separate independent replays are in
[preparation support](topics/padua-argmax-alln-20261101/prep-support/).
Historical audit/evidence records remain immutable. Numerical summary
leaf exactness is platform-dependent; the unified T1 artifact remains
byte-exact and scratch-only.

Main1acebf7 now includes auditedPR18. Its exact helper/tests retain all
PR17guards and add destination readback/v2receipts/offlineverify-archive;
S1's implementation issue is resolved. The combined branch receives a
separate [integration recheck](topics/padua-argmax-alln-20261101/prep-support/integration-audit.md).
The inherited n4 pairing certificate is retrieved only into owned scratch
for replay. **AC delivery remains PENDING**; current archive verification
against the trusted manifest is required before reliance/purge. Supported
POSIX/WSL requires quiescent storage/index; no native Windows or hostile
concurrency guarantee. No history rewrite/clone shrink. Only AC merges.

## padua-argmax-effective-20261103 — effective Padua argmax (PR #19)

Branch `codex/padua-argmax-effective-20261103`; [PR19](https://github.com/aacchhee/padua_research/pull/19).
Rules/input8a1f394, base440d107. Claude [audit-01](topics/padua-argmax-effective-20261103/audit-01.md) (2026-11-03) accepts all mathematics at the stated scopes; the [developer response](topics/padua-argmax-effective-20261103/response-01.md) to F1–F10 is accepted by the Claude [response check](topics/padua-argmax-effective-20261103/response-check-01.md) (2026-11-05).

**PD-T099 remains OPEN.** No explicit global threshold n0 or counterexample
was obtained. The effective campaign supplies two kinds of progress:

- PD-T250’s exact corner-active spectrum and PD-T251 prove, for every n>=2,
  A_n,B_n<=-n^2 Lambda_c/8. Strict corner descent holds when
  0<h_x+h_y<=1/(2[n(n+1)]^3). This closes the all-degree normalized slope
  premise; weighted energy and the fixed scaled phase radius remain OPEN.
- PD-T246: a C/GMP producer and separately implemented C++/GMP checker extend exact
  finite certification to every degree17–32, giving the continuous range2–32. The final degree set and acceptance evidence are
  in the [finite theorem](topics/padua-argmax-effective-20261103/theory/argmax-effective-codex-01-finite-global-argmax.md).

The n40 producer completed, but its corrected checker reached a600CPU-second
limit without acceptance; n40 is not certified and33–39 were not run.

PD-T249: three strict whole-cell edge comparisons are proved at n13,17,24.
PD-N084–086: scoped analytic obstructions refute a fixed-sign-cardinal envelope at n4,
complete spectral positivity, and uniform per-cardinal affine sign
preservation. These do not refute PD-T099 or aggregate/reflected approaches.

PD-T247/248: G2/G3/G4 and the1536-comparison G6 screen remain MEASURED at finite sample
scope. G5 cannot produce n0 without explicit uniform remainder and defect
bounds. G8 source coverage is partial; no1-D theorem is transferred.

The [report](topics/padua-argmax-effective-20261103/report.md) gives route
outcomes, costs, evidence and remaining obligations. Small exact witnesses
are committed; the historical bulk archive and all 16 raw payload paths are absent in this
session, with no verified delivery or durable locator. These outputs are
regenerable-only; regeneration does not recover their original bytes. [Final ID map](topics/padua-argmax-effective-20261103/final-id-map.json): PD-T246–252, PD-N084–086, IDEA-336–348, LIT-466–470; the existing LIT-379 rereading retains its ID. Pilot-only measurements remain MEASURED under PD-T252.

PR preparation registers the accepted scopes; completed preparation is historical after merge. AC alone decides whether to merge. No further Claude round is requested under AC’s 2026-11-05 direction. The missing developer per-receipt compiler/GMP mapping remains an accepted documented limitation in the [response check](topics/padua-argmax-effective-20261103/response-check-01.md); raw archive delivery remains unverified. No research run is scheduled.

## padua-lebesgue-followups-20261103 — small follow-ups for the Padua Lebesgue-function paper

This file is written only by the topic orchestrator. Branch `codex/padua-lebesgue-followups-20261103`; [PR #20](https://github.com/aacchhee/padua_research/pull/20).

### Status (2026-11-05): PR ready — generated-output archival verified

Four bounded targets, specified in [handoff 01](topics/padua-lebesgue-followups-20261103/handoffs/01-work.md):

- **T1:** certified n = 8 maxima count (PD-T180/184; PROVED 44/16/2 = 62; certified candidate correction of LIT-388 v1 Table 3’s numerical 38/56).
- **T2:** centre-minimality of the edge-defect integrals g_v and g_h.
- **T3:** a general-β series for them.
- **T4:** the constant term c (κ = c − c₁²) of the corner expansion (PD-T098).

T1: PD-T184 and PD-T180 are PROVED: exactly 44 interior and 62 total strict
maxima. Both complete original interior and boundary predicate blocks were
independently replayed; fresh generation, exact proof identity, literal joining
and both original-accounting compositions completed. No developer monolithic joined run
is claimed; Claude subsequently completed one as audit evidence. [Count proof](topics/padua-lebesgue-followups-20261103/theory/t1-closed-count.md).
T2–T4 core analytic targets are complete and accepted by Claude audit-01.

- **PROVED PD-T266, Claude audit-01 accepted:** both limiting
  edge defects have unique centre minima, vertical `g` and horizontal exactly
  `1`. [Theory](topics/padua-lebesgue-followups-20261103/theory/t2-01-edge-centre-minima.md).
- **PROVED PD-T267, Claude audit-01 accepted:** common
  logarithmic endpoint expansion with explicit errors.
  [Theory](topics/padua-lebesgue-followups-20261103/theory/t2-02-common-endpoint-expansion.md).
- **PROVED PD-T268, Claude audit-01 accepted:** general-position
  geometric series with rigorous tails, exact-Fraction enclosures and direct
  outward quadrature independently rerun at five positions.
  [Theory](topics/padua-lebesgue-followups-20261103/theory/t3-01-general-position-series.md).
- **PROVED PD-T271, Claude audit-01 accepted:** parity-independent
  corner constant `c`, with an explicit vanishing remainder and independently
  reproduced enclosure
  `1.846160310423926079759838737947 < c < 1.846160310423926079759838737948`.
  [Constant](topics/padua-lebesgue-followups-20261103/theory/t4-03-corner-constant.md),
  [PD-T269 defect limit and series](topics/padua-lebesgue-followups-20261103/theory/t4-01-corner-defect-limit.md),
  [PD-T270 one-dimensional bound](topics/padua-lebesgue-followups-20261103/theory/t4-02-one-dimensional-remainder.md), sharpening the predecessor PD-T158 estimate.

Final registration assigns PD-T266–271 to t2-01/02, t3-01 and t4-01/02/03,
respectively; every provisional alias is retained. IDEA-356/357/358 retain the
T2/T3/T4 candidates; T1 reuses IDEA-299 and existing PD-T180/184.
The full PD-T098 expansion, including `-1/N` and `O(log N/N²)`, stays
OPEN. No finite-degree or all-degree argmax conclusion is added here.

Protocol qualification: some linked full T2/T3 candidate/attempt reads were
completed after the first mechanisms. Later reading and supplementary review
do not retroactively cure that timing deviation. Claude confirmed minor impact,
with acceptance of the recorded deviation left to AC. Physical cold-storage delivery remains pending.

### Claude audit-01 (2026-11-05)

Mathematics ACCEPTED for all four targets ([audit-01](topics/padua-lebesgue-followups-20261103/audit-01.md)). Independent auditor evidence:
- a monolithic original n=8 `Verifier.run` (archived interior + independently regenerated boundary) certified 44 + 16 + 2 = 62 in one process;
- an Arb digamma-route enclosure of κ confirmed the κ and c brackets.

All nine MINOR findings (wording, proposal format, provenance/budget notes) are answered by editorial fixes in [response-01](topics/padua-lebesgue-followups-20261103/response-01.md). Registration, fresh reservation checks, integration rehearsal and independent preparation review are complete. AC-directed archival resolves the storage finding; PR20 is ready for AC’s merge decision. The T2/T3 gate-timing deviation is recorded with minor impact and left for AC's decision.

### Current boundary and post-merge frontier

Stage: PR ready for AC’s merge decision. AC directed generated outputs to cold
storage; 326 raw captures (1,155,908 bytes) were exported and separately restored
with exact hashes before removal from the tracked tree. Including all new
retrieval manifests, the conservative count is now **3,859,377 bytes**.
[Independent storage review](topics/padua-lebesgue-followups-20261103/preparation/cold-storage-review.md)
accepts the migration and resolves S1 by reduction, without a waiver.
Small essential receipts and all code remain tracked; source blobs stay retrievable.
Physical AC delivery remains pending; local verified staging is not delivery.
The mathematics is unchanged. No further agent research or preparation is queued.

Dated 2026-11-05 supersession: earlier CURRENT/RESULTS center-minimality and
general-β-series OPEN clauses are historical and superseded only at the proved
limiting-integral scopes PD-T266/268. Earlier exact n8 count OPEN clauses are
superseded only by PD-T184/180; failed/deadline attempts remain history.
PD-T100 remains MEASURED, PD-T183 remains the separate lower bound, and
PD-T181 remains the separate accepted global theorem. After merge, these
registrations and completed results remain the topic's outcome; PD-T098's sharp
expansion and PD-T099's all-degree bridge retain their separate OPEN scopes.
Finite PSLQ nulls remain MEASURED. No finite-degree ordering, broader count,
priority, manuscript or author-contact claim follows. The certified 44/62 is
only a candidate correction of the inspected LIT-388 v1 Table 3 numerical 38/56;
no accepted erratum or later-version coverage is claimed.

The T2/T3 prospective-gate deviation remains confirmed, not waived or cured;
[audit-01](topics/padua-lebesgue-followups-20261103/audit-01.md) and
[response-01](topics/padua-lebesgue-followups-20261103/response-01.md) preserve
its minor-impact assessment for AC's decision. Physical cold-storage delivery
remains pending. Only AC merges.

## padua-mz-2d-frontier-20261105

[PR23](https://github.com/aacchhee/padua_research/pull/23), branch `codex/padua-mz-2d-frontier-20261105`. Development complete2026-11-05. [Claude audit-01](topics/padua-mz-2d-frontier-20261105/audit-01.md) (Opus5.5 xhigh): mathematics ACCEPTED at stated scopes, all statuses accepted; seven P3 documentation findings answered in [response-01](topics/padua-mz-2d-frontier-20261105/response-01.md): A1–A6 fixed, optionalA7 declined. StagePR, preparation complete for AC’s review; no re-audit required for the permitted wording response. AC decision: PD-T028/110/116 keep Status OPEN with `REJECTED: refuted` disposition. Final IDs T294–300/N104–107/IDEA384–397 and shared records are prepared on this branch; no LIT assignment. [Full report](topics/padua-mz-2d-frontier-20261105/report.md).

- **PROVED analytic refutations in development, F1/F2/F3:** along evenm, signed Padua lambda_min→−infinity and lambda_max→+infinity, already on Pi_floor(theta*m) for every fixedtheta>1/2. Thus universal positivity, upper threshold below2, positive endpoint log-orders and eta→1 are false. At theta<=1/2, exactness gives eta=0. Explicit polynomial carriers have signed energies/logm→−16ab/9 and+8ab/9 with bounded continuous norms. [Weight lemma](topics/padua-mz-2d-frontier-20261105/theory/f12-local-weight-asymptotic.md), [negative carrier](topics/padua-mz-2d-frontier-20261105/theory/f12-eventual-negative-carrier.md), [upper carrier](topics/padua-mz-2d-frontier-20261105/theory/f12-eventual-upper-carrier.md), [sharp threshold](topics/padua-mz-2d-frontier-20261105/theory/f3-fixed-ratio-threshold.md). No effective finite onset, odd-m classification or sharp extremal growth law is claimed.
- **PROVED in development, F4:** every m>=2,n<m has `2<=||H_(m,n)||_(C→L2)<=C*=28.3763348311…<30`, independent of signed spectral positivity. [Weighted-L1 proof](topics/padua-mz-2d-frontier-20261105/theory/f4-uniform-density-bound.md). Positive-reference smooth diamond equivalence is a separate proved theorem; failed absolute-Gram majorants remain failed.
- **PROVED computer-assisted finite cases:** m60 strict minimum(0.188593,0.188594), maximum(1.802011,1.802012); m80 minimum(0.172730,0.172731), maximum(1.816497,1.816498). Producer times46.9s/302.4s; independent whole-pencil reconstructions/fresh-transform acceptances232.6s/569.1s. Producer coverage every integer2..60 plus80; independent acceptance specifically10/20/30/40/60/80. No complete independently certified2..80 range; m100 stopped without acceptance.
- **MEASURED:** G3 kills the originally specified localized upper model; G2 fits INCONCLUSIVE because heldout upper grid is incomplete. Floating every-integer2..239 screen at n=m−1/m−2 has no hits. Posthoc m1600,n1599 has minimum≈−0.02341441659, residual1.95e−13, saved vector; this specific point remains uncertified and is not the proof of the analytic refutations. G5 numerical screen NOT RUN because the analytic uniform norm theorem resolves boundedness directly.
- **OPEN:** 1-D PD-T027 sharp upper limit/uniform gap; effective first violating degrees, exact finite certification of the m1600 hit, sharp signed spectral growth constants and odd-m behavior.

Supplementary Astra high reconstructed all new analytic results with no gap found and separately ran exact/float checks; required Claude audit remains distinct. All development aliases and final results/candidates, including failed/equivalent/deferred routes, are retained. Bulk output is regenerable temporary staging; external Padua cold-storage delivery is pending. Registration uses the fresh live union scan at main d9b7cb8 and all open PR21–24; impact checks, nine clean disposable squash rehearsals and the independent protocol review passed, with AC’s display decision unchanged. No subsequent mathematical campaign is assigned by preparation. Only AC merges.

Registered homes: PD-T294 harmonic profile,295 weights,296 positive reference,297 uniform norm,298/299 exact m60/m80,300 finite MEASURED observations; PD-N104 sign-discard intermediary,105/106 opposite carrier energies,107 sharp signed ratio threshold. Permanent unused gaps T301–323/N108–115/IDEA398–413/LIT574–581; no accepted ID renumbered.

Preparation preserves all accepted scientific source/receipt/auditor identities; no mathematical rerun. Core registration candidate05ccb20 passed the distinct Astra medium protocol check. Main and foreign heads remained unchanged at the final reservation recheck. This PR’s readiness does not approve the other draft PRs or prescribe AC’s merge order.

## nn-mop-iep-20261103 — nearest-neighbour MOPs as a commuting-pair IEP

This file is written only by the topic orchestrator. Branch `codex/nn-mop-iep-20261103`;
draft [PR22](https://github.com/aacchhee/padua_research/pull/22).

### Status (2026-11-05): prepared and protocol-checked; ready for AC's merge decision

- PROVED, standard formulation: under explicit normality, moment systems
  uniquely give the finite polynomial triangle and both NN coefficient arrays.
  [PD-T286](topics/nn-mop-iep-20261103/theory/finite-moment-formulation.md).
- PROVED, positive split: the interior diagonal differences are nonzero under
  opposite-corner normality; the marginal Jacobi data reconstruct the full
  coefficient triangle through degree N-1 using only divisors through N-2.
  Terminal d=0 is a final boundary condition. The former PD-N?…01 failure
  classification is withdrawn; its original wording remains historical.
  [PD-T288](topics/nn-mop-iep-20261103/theory/interior-divisor-nonvanishing.md),
  [PD-T289](topics/nn-mop-iep-20261103/theory/marginal-reconstruction.md),
  [split map](topics/nn-mop-iep-20261103/SPLITS.md).
- MEASURED: 14 exact cases N=2,...,8; 476 recurrences and 70 shifted flatness
  squares pass. Independent rerun plus separate small checker completed.
  [PD-T287](topics/nn-mop-iep-20261103/theory/finite-checks.md).
- MEASURED negative: all 112 tested fixed-site transfer pairs fail to commute
  at x=0; no universal impossibility of alternative encodings is claimed.
  [PD-N100](topics/nn-mop-iep-20261103/theory/fixed-site-dictionary-failure.md).
- Known exact reduction; numerical question OPEN: lattice zero curvature
  differs from PD-T057's multiplication sections. The marginal route needs
  only marginal Jacobi data; the shifted step-line route needs the shift
  family plus boundary information. No distinct new updater
  survives the gate, so no C3 comparison or stability
  equivalence is claimed. [Report](topics/nn-mop-iep-20261103/report.md),
  [gate](topics/nn-mop-iep-20261103/gate.md),
  [candidates](topics/nn-mop-iep-20261103/candidates.md).

- MEASURED C4-only pilot: source Kravchuk/Hahn weights, N4,8,12,16,24,32;
  binary64 Stieltjes plus A/B layers versus 140/220-digit references. All
  coefficients remain finite without zero division, but fieldwise normwise
  relative errors exceed one at Kravchuk N24/32 and Hahn N16/24/32.
  This is a finite implementation observation, not general instability or
  a source residual/C3 comparison. [PD-T290](topics/nn-mop-iep-20261103/theory/c4-baseline-measurements.md).
- Claude [audit-01](topics/nn-mop-iep-20261103/audit-01.md) accepted the
  original formulation and finite counts, returned F1–F4 and N1/N2.
  [Response-01](topics/nn-mop-iep-20261103/response-01.md) accepts all
  findings, rechecks primary formulas, corrects the C4 interpretation and
  executes the baseline. [Supplementary check](topics/nn-mop-iep-20261103/response-independent-01.md)
  supplies additional independent evidence. Claude audit-02 accepted the response.

- Claude [audit-02](topics/nn-mop-iep-20261103/audit-02.md) accepts response-01:
  PD-T288/289 PROVED, PD-T290 MEASURED and the provisional negative withdrawal.
  Auditor exact-reference checks cover sampled N4,8,12,16,24; N32 retains
  precision convergence. Approved E1/E2/X1 edits and final registration are
  complete. Claude [protocol check](topics/nn-mop-iep-20261103/preparation/protocol-check-01.md)
  passed; PR22 is ready for AC's merge decision.

### Next step

AC: merge decision on PR22 (handoff07). After the merge, `Claude (Sonnet 5.5 medium): Continue codex/nn-mop-iep-20261103.` closes the topic.
## padua-mz-cleanup-20261105 — MZ cleanup

[PR26](https://github.com/aacchhee/padua_research/pull/26), branch
`codex/padua-mz-cleanup-20261105`. Codex gpt-6.1-sol xhigh;
Claude audit-01 accepts the scientific scopes, and response-01 resolves
all 26 minor/editorial findings without material scientific changes.
Final registration and independent preparation checks are complete (PASS), recorded
in [the preparation record](topics/padua-mz-cleanup-20261105/preparation/record.md).

| Result | Status and scope | Durable record |
|---|---|---|
| PD-T376 | PROVED computer-assisted finite indefiniteness at m=1101,1240,1600; explicit trial quotients, not eigenvalue brackets or an earliest-crossing theorem | [Finite witnesses](topics/padua-mz-cleanup-20261105/theory/finite-indefiniteness.md) |
| PD-T377 | PROVED odd-m fixed-node logarithmic weight asymptotics and global packet majorant; extends PD-T295 | [Odd weights](topics/padua-mz-cleanup-20261105/theory/odd-weight-asymptotic.md) |
| PD-T378 | PROVED odd-m carriers and all-integer divergence of both signed extrema above half-exactness; exact identity at or below half-degree | [Carriers](topics/padua-mz-cleanup-20261105/theory/odd-carriers.md) |
| PD-T379 | PROVED continuous carrier norm limits and normalized one-sided logarithmic spectral bounds; no sharp limit or optimality claim | [Bounds](topics/padua-mz-cleanup-20261105/theory/growth-carrier-bounds.md) |
| PD-T380 | MEASURED 23 finite minima and predeclared slope comparison; local even window1238–1240, no certified positivity or global first crossing | [Measurements](topics/padua-mz-cleanup-20261105/theory/finite-measurements.md) |
| PD-T381 | OPEN original sharp logarithmic spectral limits; PD-T379 is separate support and does not make this target PARTIAL | [Sharp target](topics/padua-mz-cleanup-20261105/theory/sharp-growth-open.md) |

IDEA-466–469 retain active proved outcomes; IDEA-470 is deferred full-signed
localization, and IDEA-471 is the abandoned raw-slope interpretation.
[Full candidate records](topics/padua-mz-cleanup-20261105/novelty-gate-math.md)
and [alias map](topics/padua-mz-cleanup-20261105/preparation/final-id-map.json).
No PD-N or LIT assignment; unused reservation gaps remain permanent.

### Audit, manuscript and limitations

[Claude audit-01](topics/padua-mz-cleanup-20261105/audit-01.md) accepted
candidate10898ad at its stated mathematical, computer-assisted and MEASURED
scopes. In a fresh environment it regenerated distinct accepted finite
witnesses, preserving the distinction from original-byte retrieval.
[Response-01](topics/padua-mz-cleanup-20261105/response-01.md) resolves
F1–F26, including portable payload identities and the durable OPEN target.
Accepted source/receipt bytes and scientific formulas are preserved under
final identifier substitution. The manuscript has a clean 25-page build;
[build history](topics/padua-mz-cleanup-20261105/manuscript-changes.md).

K0/K1 pass; K2's movement toward raw-1/9 remains diagnostic only.
Sharp spectral constants, first crossings and PD-T027 remain OPEN.
Optional C6 was not run. The [cold-storage inventories](topics/padua-mz-cleanup-20261105/COLD_STORAGE.md)
retain actual original identities and pending external delivery; no delivery
or historical novelty clearance is claimed.

### Next step

AC reviews ready PR26 and decides whether to squash-merge it; only AC
merges. The independent [protocol review](topics/padua-mz-cleanup-20261105/preparation/protocol-check-01.md)
passes with no unresolved finding. All assigned agent work is complete.
This topic approves no other draft PR or merge sequence.


## padua-argmax-effective-2-20261105 — all-degree local descent and boundary profile

Branch `codex/padua-argmax-effective-2-20261105`; [PR25](https://github.com/aacchhee/padua_research/pull/25).
[Claude audit-01](topics/padua-argmax-effective-2-20261105/audit-01.md)
accepted the mathematics; [response-check-01](topics/padua-argmax-effective-2-20261105/response-check-01.md)
accepted all record corrections. Final registration is complete within the
original reservation; [Claude preparation-audit-01](topics/padua-argmax-effective-2-20261105/preparation-audit-01.md)
accepted registration, allocation, preservation, rehearsal and the PR body.

- **PROVED PD-T364:** narrow finite phase-chart sufficiency reduction;
  inherited identities remain verification/routine lemmas, with no new cover.
- **PROVED PD-T365:** exact profile on all closed phase-diamond edges, uniform
  error<=7/(12[n(n+1)]²), midpoint S_n=L_{n(n+1)}.
- **PROVED PD-T366:** all noncorner odd-center defects>=1/8192 for n>=48,
  rho<=1/10. No continuous primitive-excess comparison follows by sampling.
- **PROVED PD-T367/368/369:** W_n<=10^10 n^4 Lambda_c; explicit known-order
  norm re-derivation Lambda_n<=27500 Lambda_c; strict corner descent for
  every n>=2 at0<H<=10^-11/n² with loss n² Lambda_c H/16. This instantiates
  PD-T227 Scope(8), against PD-T228's larger eventual2^-17/n² radius.
  The new radius exceeds PD-T251's only for n>=473. Available all-degree
  strict descent uses max(1/(2[n(n+1)]³),10^-11/n²), retaining each theorem's
  quantitative loss only on its own domain. No first-explicit-constant claim.
- **MEASURED PD-T370:** existing finite phase/projection observations and
  INCOMPLETE box pilot at every listed degree. No A1 pass/kill or new degree.
- **PROVED PD-N132:** rejects only IDEA-456's leading-factor-only a*b_n trial.
  Full H2 and PD-T099 are not refuted. IDEA454–461 retain all eight candidate
  outcomes, including equivalent Markov and deferred profile/envelope routes.

[Final map](topics/padua-argmax-effective-2-20261105/preparation/final-id-map.json),
[durable report](topics/padua-argmax-effective-2-20261105/report.md),
[gate verdicts](topics/padua-argmax-effective-2-20261105/gates.md).
T02 remains unregistered CONDITIONAL A0 evidence; no LIT assigned.
Permanent gaps T371–375/N133–137/IDEA462–465/LIT594–597 remain unavailable.

**PD-T099 stays OPEN:** global certified degrees exactly2–32, bridge33<=n<N_*
unresolved, inherited N_* non-effective. There is no full-diamond N1 or
complete H1 certifier. Local/boundary supports are not a PARTIAL decomposition.
After merge, these scoped results replace completed preparation work; practical
H1/full-diamond H2 belongs to a later topic, not a queued run here.

AC decision/coverage items remain: broader A0 criterion reading; physical
cold-storage delivery; fulltext priority for T06's Bos2006 baseline and T03's
generating-curve analogue. All40 original outputs (118,964,704bytes) were
reverified retained and identical in this Codex sandbox; no delivery or durable
retention is claimed. Only AC decides whether to squash-merge PR25 after final readiness checks.
