# Audit 02 — focused re-audit of response-01

**Verdict: CHANGES REQUIRED; stage WORK.** One new P2 remains in the quantitative summary. The response otherwise repairs the audited normalization, source-coverage, parameter and classical-setting distinctions. Existing PD theorem statements, proofs and statuses are unchanged and are not rejected by this finding.

- Candidate/rules: `41bbc231be4b5ccc7c3f92e5818a53b950ccc25f`, PR #11, `claude/mz-prior-art-20261101`.
- Prior audit: audit-01, candidate `4f937137f9baac5e51814964e6a83aeb2df38815`, delivery `64c3c79b8fe2fac27645b181aab79e3206886d16`. This report does not edit audit-01 or response-01.
- Auditor: Codex; requested allocation `gpt-6-astra`, high. Two independent bounded checks used that explicit allocation. Resolved runtime model/effort metadata is not separately exposed.
- Rules read: candidate AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md, unchanged from audit-01. Date: 2026-11-01, Europe/Oslo.
- Scope: response-01's final five-item list. Compared the 15 response-changed files against audit delivery, and manuscript changes against `4f93713`. Re-read the complete candidate `state/IDEAS.md` (457 lines), including all obstruction/disposition tables, because T6 adds a material historical attribution. Relevant unchanged candidate/theory records were reviewed in audit-01 and their distinctions remain applicable. Literature INDEX was read before source inspection. No new mechanism or novelty clearance.

## R1 — P2: the simple U evaluation does not yield the squared-log order

Locations: `topics/mz-prior-art-20261101/translation.md:86` and `topics/mz-prior-art-20261101/response-01.md:40`.

These passages group the full-sequence vanishing, the reciprocal-log bound and the squared-log order, then say they come from the exact CC evaluation of U_(N-1). The displayed evaluation has Q_N(U_(N-1)^2)=Theta(1) and integral U_(N-1)^2=Theta(log N). Its Rayleigh quotient is therefore Theta(1/log N). It establishes an **upper bound** on lambda_-(N,N-1) and vanishing along every N, not an eigenvalue asymptotic of reciprocal-log order or the stronger squared-log result.

The exact formulas make the error quantitative. For S_N=sum_(j=1)^N 1/(2j-1), the U quotient is 1/S_N for odd N and N^2/((N^2-1)S_N) for even N. Since S_N=(1/2)log N+O(1), both are asymptotic to 2/log N, and multiplying this quotient by log^2 N diverges.

Split each summary: PD-T019's simple U test gives lambda_-<=O(1/log N) and the every-N limit; PD-T018's separate harmonic-combination witness gives the O(1/log^2 N) upper bound, and PD-T017 supplies the matching lower bound. Use “upper bound from this witness” rather than “its 1/log N rate” when referring to the minimum eigenvalue. The manuscript already cites both the simple proposition and harmonic theorem and expressly distinguishes them after Proposition 5.1; its harmonic proof is not defective. The corrected comparison note also distinguishes them. Propagate that distinction to T6 and response-01, without changing any accepted PD status.

## Dispositions of audit-01

| Item | Focused disposition | Evidence and limits |
|---|---|---|
| F1: T4 normalization | RESOLVED | C_CC=2 C_src; choosing M>=1 precedes the proposition. Multipliers 2, (2 pi M)^2 and 2 give 16 pi^2 M^2 C_src. Floor/degree inclusion and absolute angular gaps are correct. Original source pages still not independently obtained. |
| T4 consequence/wording | RESOLVED within documented consequence | Its chosen window n/N<=1/pi<1/2 lies inside exactness. RELATED is a defensible conservative classification of this documented specialization; no conclusion about all possible applications of the source theorem is implied. Manuscript abstract, §1, §4, comparison and dated correction adopt the narrower assessment. |
| F2: coverage/survey grouping | RESOLVED as a wording/coverage correction | Manuscript now states source-specific reading coverage, qualifies exclusions to inspected portions, separates Sloan–Smith 1978/1980, and recognizes the survey's genuine nodal-norm theorems. The dated LIT-048 addendum records a full section/keyword screen. This auditor did not obtain the institutional PDF and does not independently certify every page or its absence of theorem statements. The earlier blanket exclusion is withdrawn. |
| F3: Konig–Nielsen | RESOLVED; selected primary statement rechecked | a=max(alpha,beta), with the finite formula for a>-1/2, gives 8/3 at (0,1). The U specialization is critical p=3 with Jacobi measure, not Lebesgue p=2. |
| F4: Gauss-to-CC attribution | RESOLVED as to the earlier invalid inference; R1 remains in the new quantitative summary | Gauss/mixed-weight and same-weight sources are now analogues. T6 supplies a separately conditional full-space CC consequence. Its deduction does not assert degree N-1 failure, a full-sequence limit or a rate. |
| N1: constants/orientation | RESOLVED | T2 comparison constants are reciprocally squared; T4 uses absolute gaps. |
| N2: T5 endpoints | RESOLVED | c=N^-2; an absolute tau works in (1.31); interior and endpoint coefficients have the claimed N^(2-4 sigma) inflation for each fixed admissible sigma. No optimization in sigma is claimed. |
| N3: source cells | RESOLVED | Don–Gottlieb is discrete GLL energy; Widom–Wilf's unnecessary unqualified rate is replaced with regime/erratum qualifications. Original inaccessible-source limits persist. |
| N4: reading summaries | SUBSTANTIALLY RESOLVED; minor residual below | LIT-063 coverage and bibliography say the letter was read; new block says seven additions. The first descriptive cell in the LIT-063 row still says “1990 addendum pending.” |
| LMN fixed-l dependence | RESOLVED in the focused manuscript/comparison edits | C_l replaces an allegedly l-independent constant. The earlier dated record is preserved as history; the source theorem was not re-certified from its inaccessible fulltext. |

## T6 and LIT-299

The independent source checker reopened the [author PDF](https://www.mi.sanu.ac.rs/~gvm/radovi/n105p163.pdf), pp.163–167. Extracted Corollary 2.2 matches the strict iff condition and degree m+2r-1. The supporting paragraph gives the opposite norm direction, and the Christoffel remark gives the interior sum. Section 3's necessity proof was not audited; the literature dependence remains explicit.

With alpha=1/2, r=1, gamma=0, p=q=2 and N=m+1, the interior nodes are the CC interior nodes, the polynomial space is Pi_N, and the strict exponent equals 1/2=1/q. The interior weights are comparable to sin(theta)/N and therefore CC weights. Squaring the endpoint term (|P(1)|+|P(-1)|)/m gives, up to absolute factors, w_0(P(1)^2+P(-1)^2). The squared sum of the interior norm and endpoint term is uniformly comparable to Q_N(P^2), including m=1. Hence failure of the converse norm inequality entails inf_(N>=2) lambda_-(N,N)=0. Positivity at each fixed N makes this a subsequence with N tending to infinity. The restriction/full-space distinction and absence of a rate are correctly retained.

**Coverage limit:** the web extractor renders some non-strict glyphs as strict; screenshot responses contained no usable image payload. Thus this audit did not independently visually confirm r>=1 and gamma>=0. The developer records page-image inspection, and the paper's explicit gamma=0 specializations corroborate that boundary. T6 is accepted as a conditional deduction on the cited corollary, including admissibility of r=1,gamma=0; it is not a locally audited proof of the historical theorem. No inferred proof status is transferred to a PD record.

Two small precision notes:

- **E1, P3:** explicitly scope the Christoffel scale sin(theta)/m in translation.md:72 and the source record to the interior nodes. It is not a global endpoint formula: lambda_m(1,1)=2/m^2, while sin(theta)/m vanishes there. T6's actual argument correctly treats endpoints separately.
- **E2, P3:** finish the LIT-063 descriptive-cell cleanup noted above. The coverage cell and bibliography are already corrected; this is an internal current-summary inconsistency, not a new source finding.

The manuscript abstract/§1/§4 and post-Proposition-5.1 remark preserve the narrowed qualitative full-space claim. The phrase “For every N, the limit ... its 1/log N rate” in §1 should preferably say “the single-U upper bound and every-N vanishing” to keep the witness bound distinct from the true squared-log order. The non-exhaustive-search and no-first-proof qualifications remain intact.

## Reservation confirmation requested by AC

**Confirmed: LIT-293–299 is reserved to mz-prior-art-20261101. The next unreserved LIT is 300 after this reservation and the Lanczos block.** This confirms the recorded reservation; the auditor allocates no additional identifier and changes no existing identifier.

Current main is `21e620ba8b5f0e0706f3a8c6613517df04d9d469`, which merged PR #10 (`9fa30122fec9796ca718af210a2a13c7525038a2`). Main's INDEX has exactly 292 distinct numbered IDs, including all 227 of LIT-066–292, and none >=293. Candidate PR #11 has exactly seven distinct additions, 293–299. There is no collision. The other next ranges remain PD-T081, PD-N032 and IDEA-177.

Live PR #6 at `3e0100f1a339c3f63dcb638785917400089a31a6` and PR #12 at `95ca473cc21b2db6a9a46c62e86495ebe94eb397` have no numbered allocation >=293. Both retain the same programme pr-prep planning blob `7c584f1d6cc4d2050d17748e5a6c5443b0994601`, which proposes a future range starting at 293 only after reconciliation/owner authorization. This is a **stale planning conflict, not an existing ID collision**. Any subsequent allocation must preserve PR #11's reservation and start no earlier than LIT-300. This audit does not edit another topic's branch or authorize its allocation.

Before PR #11 merge readiness, incorporate/reconcile the now-merged Lanczos main as AC instructed, preserving its 292 numbered entries, current ledger instructions, all scientific records, and this seven-ID reservation. The present focused audit is against the requested pinned response, not a full integration rehearsal. No merge was performed.

## Executed verification and handoff

- Retrieved all 15 response-changed files plus the four rule/IDEAS inputs at the pinned candidate; verified all 19 local Git blob identities. The support manifest records the full fetched list, SHA-256 values, bytes, source revisions and actual checks. Existing audit-01 and its source checks were read, not represented as new independent executions.
- Independently rebuilt manuscript with pdflatex, bibtex, pdflatex, pdflatex: **17 A4 pages; no final LaTeX/BibTeX warnings, undefined references/citations, overfull or underfull boxes**. Source hashes exactly match response-01: manuscript `d1ae93ae7044250877b359f560ee9b609d6a87e37a5667e7a0aaab8fb85742b2`, bibliography `9901ae3dba63af176a1ced7c066da559588bd762ee8fe7bf25602e0a48c7da63`. Build output stays local at `/workspace/pr11-reaudit/build`.
- Reopened selected Lubinsky and Konig–Nielsen primary statements and the new LIT-299 source. Did not repeat the entire historical source survey or numerical experiments; no changed code or numerical claim required that. Mastroianni–Totik and the other inaccessible-primary coverage limits from audit-01 remain.
- Separate [T2–T5/F3 check](audit-support/response-01-t2-t5-check.md), [T6 check](audit-support/response-01-t6-check.md), [reservation receipt](audit-support/response-01-reservation-check.json) and [input manifest](audit-support/response-01-input-manifest.json) preserve evidence. No third-party fulltext is committed.

Next: developer corrects R1 (and the small wording notes) in a response-02, then requests a narrowly scoped re-audit. No PD status change, source-proof approval, publication, external contact or merge is authorized by this report. AC alone decides merge.
