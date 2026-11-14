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

## padua-literature-20261103

Audited source footing for the Padua Lebesgue function, Clenshaw–Curtis/Padua MZ constants, bivariate Lanczos/V+A and Leuven IEP/MOP line. This is literature attribution and bounded source reading, with no new local mathematical proof or PD status change.

- **Registration:** 58 provisional statement aliases reconciled. 31 new statement IDs LIT-482–512; 27 aliases reuse accepted IDs. LIT-513–561 remain permanent unused gaps. [Exact map](topics/padua-literature-20261103/preparation/final-id-map.json), [deduplication](topics/padua-literature-20261103/preparation/literature-dedup.md), [ledger](topics/padua-literature-20261103/ALLOCATIONS.md). Existing PR22 source identities/coverage, including both distinct halves of LIT-420, are preserved.
- **P1:** the Padua vertex maximum was conjectured in the 2008 poster and observed in De Marchi2022. KL2021 supplies the published global coefficient4/π² and hence the corner upper estimate; no unchecked transfer of its noncorner lower estimate to the corner is asserted. Exact-corner/second-term and proof comparisons retain their documented search limits. [Comparison](topics/padua-literature-20261103/p1-comparison.md).
- **P2:** signed cubature existence/exactness is attributed to SVZ2008; the reported journal normalization misprint is qualified by its source-reading provenance. Mastroianni–Russo's powered weight hypothesis and excluded CC/A2 endpoint are recorded; the missing borderline-MZ decay estimate is distinguished from its polynomial approximation-error rates. [Comparison](topics/padua-literature-20261103/p2-comparison.md).
- **P3:** the full-sequence Favard/commuting machinery is classical; finite/truncated/words/manifold claims keep their distinct comparison scopes. Greenbaum branches, exact-section versus actual-run quantities, and revised V+A locators are separated. [Comparison](topics/padua-literature-20261103/p3-comparison.md).
- **P4:** source authorship, RQ/QR, finite stability observations, Laurie author-awareness and future-work wording are corrected. Proposed joint questions remain unregistered and require their own future novelty gate; classical downdating is distinguished. [Memo](topics/padua-literature-20261103/p4-memo.md).
- **Search scope:** AC's dated MathSciNet zero result is an indexed-query outcome, not publication absence. Title/review-only triage is not full-text exclusion. No exhaustive priority or manuscript/submission readiness is certified.
- **Audit:** audit01 F1–F6 resolved in audit02; F7 resolved in audit03. Inaccessible journal/image/NTNU/Crossref checks remain developer-verified only; acceptance does not promote them to independent auditor verification. [Audit02](topics/padua-literature-20261103/audit-02.md), [audit03](topics/padua-literature-20261103/audit-03.md).
- **Preparation:** main includes merged PR25/26/22; audited proposals are applied with explicit ID/alias mapping and preserved foreign records. Verification, rehearsal and independent preparation review are recorded in [preparation/record.md](topics/padua-literature-20261103/preparation/record.md).
- **Remaining reading:** print-only and version/coverage gaps stay in [DOWNLOADS](topics/padua-literature-20261103/DOWNLOADS.md) and the source records. They qualify this bounded literature registration; no new source campaign is assigned here.

The scientific statuses mentioned in historical comparison memos are those of their input scope. Current PROOF_STATUS.md and the separately accepted newer campaigns are authoritative, including the signed-Padua supersessions; this literature PR changes none of them. Only AC merges.

## padua-lanczos-frontier-20261105 — aggregate separation and closure certificates

[PR24](https://github.com/aacchhee/padua_research/pull/24). Stage PR, ready for merge decision. Claude audit-01 accepted the mathematics and audit-02 accepted response-01 with minor record findings, addressed in preparation. Final IDs are assigned; Claude preparation audit-03 accepted the preparation, and PR24 is marked ready for AC's merge decision (only AC merges).

- **PROVED, computer-assisted:** rotQ24 degree12 full formal scalar-CGS2 comparison, all90 sources: `K_BJ² >= 2041704913997 > 100 * 13462956266 >= 100 K_alt²`. This proves the rotQ24 conjunct; together with PD-T141(c), both target conjuncts are proved, with the separate target row registered at preparation. [Theory](topics/padua-lanczos-frontier-20261105/theory/l4-envelope-bound.md), [fixed rational readout](topics/padua-lanczos-frontier-20261105/evidence/l4-readout-certificate.json), [independent execution/checks](topics/padua-lanczos-frontier-20261105/independent-checks-l4.md). Same inherited error-sign witness, stronger full-output readout; no IEEE/all-degree claim.
- **PROVED, scoped route obstruction:** the same absolute envelope cannot prove factor ten with the fixed old BJ lower. [Negative record](topics/padua-lanczos-frontier-20261105/theory/l4-N01-fixed-lower-envelope-obstruction.md). The stronger lower escapes it; the true capacity target is not rejected.
- **G0 RESOLVED:** independently checked arithmetic-sensitivity explanation, preserving original FAIL and missing historical trajectory. [Disposition](topics/padua-lanczos-frontier-20261105/g0-disposition-02.md).
- **PROVED, analytic:** all-degree BJ/mirror aggregate-source span separation on the saved positive weighted SH_n family, an affine image of a product grid, with exponential BJ lower and polynomial mirror upper. Both bounds hold for n>=2; their ratio bound exceeds1 only for n>=18, with no small-n ordering claimed. [Theory](topics/padua-lanczos-frontier-20261105/theory/l1-01-sheared-U-aggregate-separation.md), [independent adversarial check](topics/padua-lanczos-frontier-20261105/independent-checks-sh.md). No scalar-operation or IEEE conclusion.
- **PROVED finite reduction; G2 W/R PASS:** smooth exact-base rule invariance and actual X-closure derivative; exact fixed certificates independently regenerated on T24 and rotQ24. [Reduction](topics/padua-lanczos-frontier-20261105/theory/l2-smooth-rule-closure-reduction.md), [evidence](topics/padua-lanczos-frontier-20261105/independent-checks-l1-l2.md). Original working-precision PD-T055 stays OPEN.
- **PROVED, analytic:** saved all-degree worst-case and mean-square X-closure targets on SH_n, via a separate positive-weight extension and actual nested-projector derivative. [W theorem](topics/padua-lanczos-frontier-20261105/theory/l2-sh-worst-case-closure-growth.md), [R theorem](topics/padua-lanczos-frontier-20261105/theory/l2-sh-random-closure-growth.md), [independent reconstruction](topics/padua-lanczos-frontier-20261105/independent-checks-l1-l2.md). The full original source law is retained in the formal first-order smooth exact-base aggregate model; no working-precision/IEEE claim.
- **G1 scan complete:**all152/152 rows independently matched on both frozen grids, four rules, degrees2–20 and all sources. Historical1800s cost stops and failed60s guards are preserved. Actual frozen fits and distinct report verification pass. Both interval verdicts are INCONCLUSIVE by certified slope counterchoices; neither grid triggers the finite KILL rule, and no asymptotic conclusion follows. [Finite measured record](topics/padua-lanczos-frontier-20261105/theory/g1-finite-growth-measurements.md).
- Original PD-T140 experiment remains INCONCLUSIVE/MEASURED. Remaining broader L3/L5/L6 and L7/G3 work is scoped in [report](topics/padua-lanczos-frontier-20261105/report.md). Relevant L1/L2 and L3/L4 source gates are complete; AC accepted the disclosed pre-gate deviation on2026-11-05; it remains permanently disclosed, not waived and not cured.

Next: AC's merge decision on PR24; no further agent step is required for this PR. Claude preparation audit-03 accepted final IDs, registry application and integration checks under handoff11. Original broader research obligations remain OPEN. AC accepted A-P1 on2026-11-05 with permanent disclosure; see [preparation](topics/padua-lanczos-frontier-20261105/preparation/record.md). Large raw arrays stay off Git; archival delivery pending.

Handoff04: finite-error selection theorem PROVED under its explicit per-column finite-budget/full-projection model, with independent mathematical reconstruction. The broader L3 target is OPEN; this is a PROVED supporting reformulation, not a result uniform over Hres alone. L5 finite upper/lower certificate reduction is also PROVED; the independently checked finite n3 bracket is `1/512 <= delta_obs(3) <= 1/2`; n4–8 and the asymptotic U2 target remain open. G4 both-row replay discrepancy is RESOLVED by independently checked high-degree reference/residual/kernel controls, preserving original failed screens and missing historical trajectories. The natural suite was unrun at that historical handoff; current measured outcomes follow. See the current report for exact scope.

Handoff05: the saved natural suite now completes with independent all-case checks and a separate triangle rerun:16/24 references accepted,on Haswell20/1280 accepted cells satisfy the loss rule, and six within-group paired-seed advantages appear on triangle24/tanh/boundary. The within-group grouping is post-registration; six additional cross-group directions qualify. Audit default AVX-512 gives18 losses/nine within-group directions, so specific cells and pairs depend on the platform. Large recurrence replay errors limit interpretation to measured end-to-end behavior. Separate exact lower bounds delta_obs(4)>=1/2048 and delta_obs(5)>=1/16384 are independently checked; both upper searches remain inconclusive under their caps. G1 fused14=72.527s fails its original60s scheduling guard; a dated one-case scheduling successor allocates the original1800s ceiling for the first unchanged-engine BJ20 run, without changing any scientific acceptance criterion.

L6: the complete-square quantitative residual theorem and scoped e/u obstruction are independently reviewed. One frozen binary64 n1 run is MEASURED with certified complete64u residual/Gram budgets; an independent367-operation/47-state replay verifies exact raw symmetry defect2^-55. The separate finite raw exact-match nonrealizability claim is PROVED for those14slots/fixedorthonormalgauge. No corrected positive model or general G conclusion.

2026-11-05 preparation: registered PD-T324–339, PD-N116–118 and11 distinct IDEA414–424; eight duplicate/equivalent continuations reuse existing IDEA IDs with complete aliases. No LIT assignment. Complete mathematical scopes/statuses and permanent unused gaps are in the exact map/crosswalk. PD-T331 is the finite rotQ24 factor-ten conjunct; PD-N116 is only its fixed-old-lower route obstruction. All original unresolved targets retain their status. P3 attribution now cites merged PR21, unchanged memo blob4741c38943f37ae05ba525552ceafc3f32ac5537 with the same bounded coverage. Required preparation audit and AC's merge decision remain outstanding.

## padua-lanczos-nonproduct-20261105 — non-affine-product Lanczos span drift

- **PROVED, PD-T478–480:** non-affine-product measures moment-equivalent to
  SH_n through degree 2n+1, with an n-dependent weight mode, retain the
  exponential BJ lower and polynomial full-source mirror upper for every
  n>=2 and 0<|eta|<1. Gram matrices, monic basis, creators, pivots, source
  scales and frozen response are eta-independent; only the ambient normal
  projector changes. Every 0<eta_0<1 is a sufficient uniform radius, and
  the displayed ratio lower first exceeds1 at n=18.
  [Admission](topics/padua-lanczos-nonproduct-20261105/theory/p3-01-high-mode-weight-admission.md),
  [moments](topics/padua-lanczos-nonproduct-20261105/theory/p3-02-exact-moments-creators.md),
  [separation](topics/padua-lanczos-nonproduct-20261105/theory/p3-03-uniform-capacity-radius.md).
- **PROVED, PD-T485/486:** positive Chebyshev Padua measures are non-product;
  at every m>s>=1, BJ and mirror satisfy
  sqrt(ceil(s/2))<=kappa<=2sqrt(2)(s+1)(N_s-1). Both are unbounded with a
  polynomial upper uniformly in m>s; no sharp exponent or alternative-rule
  upper follows.
  [Admission](topics/padua-lanczos-nonproduct-20261105/theory/p5-01-padua-admission.md),
  [capacity](topics/padua-lanczos-nonproduct-20261105/theory/p5-02-padua-polynomial-capacity.md).
- **PROVED, PD-T472/474/477/481:** triangle, continuous radial disk and D36/D65
  rational ring admissions and the affine-product definition at their stated
  injectivity and positive full-support scopes. D36 and D65 are distinct
  measures with no asserted continuous-disk cubature equivalence.
  [Definition](topics/padua-lanczos-nonproduct-20261105/theory/nonproduct-definition.md),
  [triangle](topics/padua-lanczos-nonproduct-20261105/theory/p1-triangle-admission.md),
  [disk](topics/padua-lanczos-nonproduct-20261105/theory/p2-01-family-admission.md),
  [D65](topics/padua-lanczos-nonproduct-20261105/theory/p2-04-low-denominator-rings.md).
- **PROVED, PD-T475/482–484:** whole-algorithm covariance, weighted finite
  normal quotient (including its restricted terminal-block corollary), exact
  atomless capacity and moment/source transfer. Covariance does not identify
  fixed-order BJ/mirror; finite cubature does not identify arbitrary-source
  capacities. [Covariance](topics/padua-lanczos-nonproduct-20261105/theory/p2-02-rotation-covariance.md),
  [weighted](topics/padua-lanczos-nonproduct-20261105/theory/p4-weighted-normal-quotient.md),
  [atomless](topics/padua-lanczos-nonproduct-20261105/theory/p4-continuous-capacity.md),
  [transfer](topics/padua-lanczos-nonproduct-20261105/theory/p4-moment-capacity-transfer.md).
- **PROVED, PD-N178:** fixed covariance and distinct principal-axis angles
  do not bound absolute degree-two capacity on the explicit thin-annulus
  family. Only IDEA-581 is REJECTED: refuted; the all-degree BJ/best ratio
  criterion stays OPEN. [Obstruction](topics/padua-lanczos-nonproduct-20261105/theory/p4-covariance-capacity-obstruction.md).
- **MEASURED, PD-T473/476:** finite triangle/radial-disk moment and creator
  probes through8. The central-binomial chain is under BJ only; no full-source
  bounded-order recursion or asymptotic rate is established.
  [Triangle](topics/padua-lanczos-nonproduct-20261105/theory/p1-continuous-creator-probe.md),
  [disk](topics/padua-lanczos-nonproduct-20261105/theory/p2-03-finite-recurrence-probe.md).
- **MEASURED, PD-T487/488:** H24_222/D36x9 each have60 matched exact four-rule
  rows through16. Their screens and inherited T24 reanalysis are INCONCLUSIVE.
  D65 has a degree8 pilot and incomplete degree12 cost probe. Analytical
  P3/P5 bounds have no fit premise.
  [Endpoints](topics/padua-lanczos-nonproduct-20261105/theory/p6-finite-scans.md),
  [screens](topics/padua-lanczos-nonproduct-20261105/theory/p6-n2-screen.md).

**OPEN, PD-T489–494:** continuous triangle and disk rates, a useful all-degree
structural criterion, sharp Padua exponents, alternating/pivot Padua uppers,
and n-independent perturbation robustness. Supporting lemmas do not upgrade
these targets to PARTIAL. IDEA-577 defers the fixed-perturbation follow-up;
it is not a precondition for the proved moment-equivalent variant.
[Crosswalk](ID_CROSSWALK.md#non-affine-product-lanczos--canonical-mappings).

[N0](topics/padua-lanczos-nonproduct-20261105/n0-replay.md) is executed
verification evidence with no separate claim ID. The scoped mathematics and
finite checks are accepted in [Claude audit01](topics/padua-lanczos-nonproduct-20261105/audit-01.md)
and the BJ-only correction in [audit02](topics/padua-lanczos-nonproduct-20261105/audit-02.md).
[Canonical AC decisions](topics/padua-lanczos-nonproduct-20261105/LOG.md#2026-11-06--claude-audit-01)
retain the P3 timing qualifier, accepted weaker scope and screen deviation.
LIT-630 is bounded source-reading coverage only. No IEEE activation, nonlinear
geometry theorem, priority or external archive delivery is claimed.

## NN MOP conditioning and stability — scoped records

Intrinsic conditioning, finite accuracy gains and strict joint-data compatibility are separate questions. The following claims have the scopes stated in their linked theory records and completed [audit-01](topics/nn-mop-stability-20261105/audit-01.md), [audit-02](topics/nn-mop-stability-20261105/audit-02.md) and [G5 audit](topics/nn-mop-stability-20261105/audit-g5-01.md).

- **PROVED; Claude audit-01 supported:** explicit all-N Krawtchouk lower bound with exponential base at least5+2sqrt(6), plus a separate proximity obstruction to O(1/d_min). Sharp matching upper growth remains OPEN. [Proofs/receipt](topics/nn-mop-stability-20261105/attempts/D1-hard.md).
- **PROVED; Claude audit-01 supported:** local derivative/norm formula, coarse upper bound, generic normality reduction and finite exact Hahn normality at every N4–64 (43,676 checks, independently replayed). [Finite theorem](topics/nn-mop-stability-20261105/theory/conditioning-hahn-normality-finite.md).
- **MEASURED:** complete NN/monic-step-line condition table, all N4–64 at180/260dps. G0 reproduces all12 baseline errors exactly; stable marginals do not clear C4 layers under G2. [D1](topics/nn-mop-stability-20261105/attempts/D1.md), [D2](topics/nn-mop-stability-20261105/attempts/D2.md).
- **MEASURED:** two native whole-triangle designs gain>=2digits in several attainable cases. **PROVED; audit-01 supported:** actual-image projection geometry and exact raw-array incompatibility. Numerical mixed fits can be small atN4 but miss100u atN8; general backward stability OPEN. [D3](topics/nn-mop-stability-20261105/attempts/D3.md), [D5](topics/nn-mop-stability-20261105/attempts/D5.md).
- **PROVED / MEASURED, separate records:** finite Christoffel/Toda algebra, normality/orbit obstructions and a scoped failed solver. Positive graph mixed-test encoding does not yield a full NN-to-Padua transfer. [D4](topics/nn-mop-stability-20261105/attempts/D4.md), [D6](topics/nn-mop-stability-20261105/attempts/D6.md).
- **MEASURED:** G5 reproduction gate PASS (one configuration, Octave8.4, to the decade); large-N variation measured; topic-metric comparison not yet run. The supplied-source experiment was independently repeated with Octave9.4, whose selected gate also passes. Direct paper-table/hash verification in the Codex executor remains unresolved; paper-data comparison is attributed to Claude’s source-bundle receipt. [G5 run/audit](topics/nn-mop-stability-20261105/audit-g5-01.md).

Three supplementary independent reports and exact checker code are committed. Large raw outputs/figures remain off Git with identities/commands; no external archival delivery is claimed. Exact normality verification covers61 sizes/43,676 checks. The committed12-case projection reference is an explicitly new fixed-configuration rerun; original temporary witness bytes are unavailable. Binary64 values have the platform scope stated in the native/projection theory records. Sharp-growth and general stable-solver targets remain OPEN; a passing reproduction is no stability theorem.

## nn-mop-conditioning-20261106

The [candidate/result map](topics/nn-mop-conditioning-20261106/candidate-result-map.md) and [ID crosswalk](ID_CROSSWALK.md#nn-mop-conditioning-20261106-allocations) preserve the provisional aliases.

- **PROVED — PD-T502/503/504:** positive fixed/smooth diagonal gauges retain b-field sensitivity; scalar and fixed-mass derivative formulas and separate monic matrix spectral sensitivity bounds are explicit. These concern the stated input/output metrics. [Gauge invariants](topics/nn-mop-conditioning-20261106/theory/c1-gauge-invariants.md), [scalar derivatives](topics/nn-mop-conditioning-20261106/theory/c1-scalar-derivative.md), [matrix metric](topics/nn-mop-conditioning-20261106/theory/c1-matrix-metric.md).
- **PROVED — PD-T509/506:** exact benchmark Krawtchouk NN and six-field gauge exponential base 5+2sqrt(6). The all-field upper has a loose polynomial prefactor; useful matching prefactors and finite-error radii remain OPEN. [Sharp upper](topics/nn-mop-conditioning-20261106/theory/c2-sharp-upper.md), [gauge rate](topics/nn-mop-conditioning-20261106/theory/c1-gauge-sharp-rate.md).
- **PROVED — PD-T511/512/513/508:** exact benchmark Hahn normality for every N>=2, a simple base-two lower, terminal parity-row rate rho_H=12.1136005841… and that full-map/gauge lower liminf. No matching full-map upper is proved. [Normality](topics/nn-mop-conditioning-20261106/theory/c2-hahn-normality.md), [simple lower](topics/nn-mop-conditioning-20261106/theory/c2-hahn-lower.md), [terminal rate](topics/nn-mop-conditioning-20261106/theory/c2-hahn-terminal-rate.md), [gauge lower](topics/nn-mop-conditioning-20261106/theory/c1-hahn-gauge-lower.md).
- **PROVED — PD-T510:** explicit all-N general-parameter Krawtchouk lower base for fixed distinct binomial pairs in (0,1); no matching general upper. [Theorem](topics/nn-mop-conditioning-20261106/theory/c2-krawtchouk-parameter-lower.md).
- **PROVED — PD-T517:** a finite positive gauge attains max(kappa_b1,kappa_b2) for both exact benchmarks, all N>=2 and the six stated node/mass models. General non-dominant inputs, step-line scaling and relative global matrix-norm optimization are outside this theorem. [Attainment theorem](topics/nn-mop-conditioning-20261106/theory/response-gauge-infimum.md).
- **PROVED negatives — PD-N181/182/183; REJECTED: failed:** three scoped Hahn upper-estimate mechanisms fail: separate global maxima, unchanged nonterminal positive differences and universal polynomial unweighted grid-derivative transfer. The full Hahn upper target remains OPEN. [Envelope](topics/nn-mop-conditioning-20261106/theory/c2-hahn-upper-envelope.md), [positivity](topics/nn-mop-conditioning-20261106/theory/response-c2-positivity-failure.md), [node transfer](topics/nn-mop-conditioning-20261106/theory/response-c2-node-transfer-failure.md).
- **MEASURED — PD-T505/507/514/516:** N4–64 metric controls and native/external comparisons through N32. M1 passes in the specified metric. The developer stack completed 232 native solves; the audit stack completed 231, with Krawtchouk N32 A-LU breakdown and changed LU maxima. M2/M4 source gates and 348 external calls are recorded on the developer platform; external NN errors include an explicit H+d0 lift. The 348-case matrix-error/capacity comparison is diagnostic. [Measurements and limits](topics/nn-mop-conditioning-20261106/report.md).

**PARTIAL — PD-T448:** the exact benchmark Krawtchouk rate conjunct is solved by PD-T509. Krawtchouk matching prefactors/useful constants/radius and full-Hahn rate/prefactors/useful constants/radius remain OPEN. Supporting normality, lower bounds and measurements are not solved target parts. The historical D1 mechanism questions remain OPEN supporting leads outside the registered statement. [Parent record](topics/nn-mop-stability-20261105/theory/conditioning-growth-target.md).

**OPEN — PD-T515 and PD-T449:** the distinct A-LU forward target and general weak/joint backward-stability targets remain unresolved. Finite solver gains and local image geometry supply no general algorithmic stability theorem. [Forward target](topics/nn-mop-conditioning-20261106/theory/c3-weak-stability-open.md), [backward target](topics/nn-mop-stability-20261105/theory/stable-solver-target.md).

[Audit01](topics/nn-mop-conditioning-20261106/audit-01.md) and [focused audit02](topics/nn-mop-conditioning-20261106/audit-02.md) accept the scoped science. General-input gauge minimizers outside b dominance, matching Hahn/general-parameter uppers, outward numerical enclosures, finite-error radii, licensed Advanpix execution and cold-storage delivery remain unresolved/unrun.

## padua-mz-sharp-constants-20261106 — sharp MZ constants

- **PD-T020 — PROVED.** For unnormalized Lebesgue Clenshaw–Curtis quadrature, (log N)^2 lambda_min tends to pi^4/8 on both Pi_(N-1) and Pi_N, through all integers N and both parities. [PD-T546 reverse bound](topics/padua-mz-sharp-constants-20261106/theory/P3-reverse-bound.md) combines with [PD-T523 matching limsup](topics/padua-mz-sharp-constants-20261106/theory/S1-sharp-one-sided.md); PD-T522/544/545 supply the Volterra, signed-remainder and discrete-primitive dependencies.
- **PD-T027 — PARTIAL.** Its uniform-gap conjunct is PROVED by [PD-T526](topics/padua-mz-sharp-constants-20261106/theory/S2-uniform-upper.md), with all-N bound5/3<2. Existence of the common-parity sharp upper limit and its exact endpoint-norm characterization are PROVED by [PD-T530](topics/padua-mz-sharp-constants-20261106/theory/S2-qualitative-limit.md). The decimal-value conjunct remains OPEN under the recorded target decomposition. [PD-T527](topics/padua-mz-sharp-constants-20261106/theory/S2-eta-deficit.md) proves the logarithmic eta-deficit law; PD-T528 is the registered model definition/prediction pointer, with no separate duplicate theorem; PD-T529/531 give fixed-trial errors and computable finite brackets tending to zero width.
- **PD-T381 — PARTIAL.** Existence of both signed logarithmic limits, agreement of the even/odd limits and their characterization as inf/sup spectrum(B) are PROVED by [PD-T534](topics/padua-mz-sharp-constants-20261106/theory/S3-full-form-log-model.md), [PD-T535](topics/padua-mz-sharp-constants-20261106/theory/S3-corner-kernel-hard.md) and [PD-T536](topics/padua-mz-sharp-constants-20261106/theory/S3-corner-operator-limit.md). The values conjunct (decimal c_minus/c_plus) remains OPEN. Exact norm-tail120/K and explicit finite-m errors are proved; finite proxy decimals have no certified accuracy.
- **Supporting Padua kernel results — PROVED.** [PD-T539](topics/padua-mz-sharp-constants-20261106/theory/P1-elliptic-kernel.md) identifies the exact elliptic kernel with the accepted product-cutoff operator. [PD-T540](topics/padua-mz-sharp-constants-20261106/theory/P1-positive-spectrum.md) proves c_minus=-norm(B), a simple almost-everywhere positive ground state and0<c_plus<norm(B). [PD-T541](topics/padua-mz-sharp-constants-20261106/theory/P1-rectangle-certificate.md) proves the finite rectangle reduction; [PD-T542](topics/padua-mz-sharp-constants-20261106/theory/P1-numeric-certificate.md) gives the computer-assisted enclosure[-0.477809279990884889210594,-0.013164946500379018110831] for c_minus, with **no useful digits** certified.
- **Supporting endpoint certificate — computer-assisted PROVED.** [PD-T547](topics/padua-mz-sharp-constants-20261106/theory/P4-certified-lower.md) gives Lambda_edge>=1.0044369 from one exact J512 Rayleigh trial. The narrow trial-quotient interval is not an upper enclosure of Lambda_edge. [PD-T548](topics/padua-mz-sharp-constants-20261106/theory/P4-denominator-closed-form.md) proves every closed-form denominator entry. Exact arithmetic, committed trial/checkers and actual independent reruns support the certificate.
- **Scoped carrier results — PROVED.** [PD-T533](topics/padua-mz-sharp-constants-20261106/theory/S3-normalized-carrier-improvement.md) strengthens the inherited fixed-family negative bound. [PD-T537](topics/padua-mz-sharp-constants-20261106/theory/S3-carrier-family-ceiling.md) proves the limiting fixed-parameter family cannot reach0.0915; this does not bound broader packets or the full spectral constant.
- **Distinct finite observations — MEASURED.** [PD-T525](topics/padua-mz-sharp-constants-20261106/theory/S1-measured.md), [PD-T532](topics/padua-mz-sharp-constants-20261106/theory/S2-measured.md) and [PD-T538](topics/padua-mz-sharp-constants-20261106/theory/S3-measured.md) retain CC fits, the J512/B_K proxies, all16 Padua minima and normalization diagnostics. K2 is no evidence against equality because its fitted intercept exceeds the proved limsup bound. K4's finite proxy rejection predicts no asymptotic-value failure.
- **PD-T543 — MEASURED.** The [four-case finite-mode test](topics/padua-mz-sharp-constants-20261106/theory/P2-measurements.md) at1600/1601/3000/3001 gives PASS_FINITE_TEST, with independent m1600 and summary agreement. Only mode-2 weight, L-distance and branch-difference rate were prospective; the Qmin secant criterion was essentially postdictive from earlier S4 rows. No two-term theorem, crossing-degree or asymptotic decimal follows; original gates/receipts are unchanged.

The retained [S1 prediction record PD-T524](topics/padua-mz-sharp-constants-20261106/theory/S1-model.md) preserves its historical CONDITIONAL statement; its target is resolved separately by PD-T546. All fourteen candidate records remain represented under consolidated IDEA-071/386/469/470 and new IDEA-608–611. [Final ID/alias map](topics/padua-mz-sharp-constants-20261106/final-id-map.json). [LIT-633](topics/padua-mz-sharp-constants-20261106/literature/basor-ehrhardt-1999.md) reports bounded same-symbol Toeplitz-plus-Hankel results; no external theorem is inherited for the actual endpoint model.

The original target wording and explicit decompositions remain in the target histories and [crosswalk](ID_CROSSWALK.md); the canonical interpretation decision is in [LOG](topics/padua-mz-sharp-constants-20261106/LOG.md). Completed [audit-01](topics/padua-mz-sharp-constants-20261106/audit-01.md), [audit-02](topics/padua-mz-sharp-constants-20261106/audit-02.md) and [audit-03](topics/padua-mz-sharp-constants-20261106/audit-03.md) establish their recorded scopes. Decimal values, practical sharp endpoint upper certification and practical convergence refinements remain OPEN.

## padua-3d-20261106

For normalized product-Chebyshev measure, **PD-T557 — PROVED with explicit LITERATURE dependency** — gives a fixed eventual node excess over dimPi_(n−1) for positive rules exact through degree2n−1 with all nodes in the closed cube. PD-T554–556 supply locally PROVED frame/local-limit/completeness steps; Greenfeld–Lev (LIT-659) supplies the facet theorem. Constants are non-effective. PD-T558 covers fixed inverse-polynomial weight changes; general full-support doubling is OPEN in PD-T559.

- **PROVED:** PD-T562 certifies one20-node positive precision-five cubic-unisolvent set outside every single translated finite-subgroup cosine image. Its rounded-center sampledLambda30.0121 (PD-T563) is MEASURED and poor against the numerical4.05benchmark. No all-degree construction follows.
- **PROVED with explicit LITERATURE dependency:** PD-T565 certifies25.961333≤Lambda≤29.062900 for the retained455-point degree12 set and gives thirteen separate QR n4..16 intervals. Other historical optimized coordinates are unavailable. The mesh theorem LIT-666 remains explicit.
- **PROVED locally:** PD-T566/567 give the elementary double-Lee bound and packing-free determinant minima92/178/304/486 at n4..7. Prior lattice candidates and reportedly known optimality are credited, without a first-value claim.
- PD-N186 and PD-N191 prove the restricted reflection-coset and monotone-stack obstructions. Finite classifications, lattice objectives and the rest of the130 claims preserve their own statuses/scopes in the [proof registry](PROOF_STATUS.md).
- Known determinantal real calibrations are PROVED in PD-T561; bounded quality observations PD-T560 are MEASURED. The general algebraic quality target remains OPEN. Failed/capped paths and deferred candidates are retained.
- Portable pruning sets save14–16percent of sites:546 at degree12 (rank455),1163 at degree16 (rank969), with exact determination/unique-LS proofs and finite measured quality tradeoffs. The full grids retain stronger measured stability.

The general exact-cardinality polylog interpolation problem remains OPEN. Research directions are frozen, with quantitative C5/C6 resume conditions and completed record-only C8 in IDEA-620/IDEA-621/IDEA-623. All108 candidates, aliases and38 newly indexed literature facts are retained.

[Paper](topics/padua-3d-20261106/paper-note-draft.md) · [repository companion](topics/padua-3d-20261106/paper-repository-context.md) · [complete result report](topics/padua-3d-20261106/final-narrowed-report.md) · [final-ID map](topics/padua-3d-20261106/pr-preparation/final-id-map.json) · [accepted audit05](topics/padua-3d-20261106/audit-05.md) · [accepted audit06](topics/padua-3d-20261106/audit-06.md).

## padua-effective-cubature-20261112

For positive cubature for normalized product-Chebyshev measure with all nodes in the closed cube:
- **PD-T679, PROVED (computer-assisted).** γ_A>1/36. Every rule exact on Π_(2n−1) has N≥37n³/216 for every n≥1, exceeds dimΠ_(n−1) for n≥109, and no positive Padua package (N=binom(n+3,3)) exists for n≥218. This makes the PD-T557 excess explicit.
  - The certificate re-proves locally, from its coefficients taken as data, the Dostert–Guzmán–de Oliveira Filho–Vallentin octahedron Cohn–Elkies function (LIT-717). There are two independent code paths, both PASS. A cross-agent replay was blocked by HTTP 403 on the third-party input.
  - PD-T678 gives an explicit compactly supported witness with the same γ>1/36.
- **PD-T675, PROVED.** A local Delsarte transference bound N≥((E+1)/2)³·D(int 2O)/8 at exactness E.
- **PD-T676, PROVED with explicit LITERATURE dependency.** With Kolountzakis–Lev–Matolcsi Thm 6.4 (LIT-716), PD-T676 gives a uniform excess N≥(1+γ_A)n³/6 at every n, governed by one Delsarte constant.
- **PD-T677, PROVED.** γ_A≤1/18. So this route alone decides no package degree n≤109.
- **PD-N246, PROVED.** The finite torus LPs with M≤8N cannot exclude any n=2…109 (exact lattice witnesses).
- **Open.** Package existence for 4≤n≤217 remains OPEN.
- **Measured.** The plain torus LP is indistinguishable from Fisher (MEASURED; its pre-registered KILL was not established, so the route is deferred). The Delsarte torus LP is ≈1.08 at n=5…8; the cube-native LP is ≈1.2 at n=2…4.

**PD-T674, PROVED (assembly).** The Padua Lebesgue constant equals the corner value for 2≤n≤32 and every n≥N_* (existential), with the explicit three-term expansion for n≥max(32,N_*).

All seven candidates (IDEA-756–762) and the literature records LIT-716/717 are retained. The novelty gate was completed retrospectively, and the S4 route attribution is kept.

[Results](results/padua-effective-cubature-20261112.md) · [report](topics/padua-effective-cubature-20261112/report.md) · [final-ID map](topics/padua-effective-cubature-20261112/pr-preparation/final-id-map.json) · [audits 01–03](topics/padua-effective-cubature-20261112/audit-03.md)
