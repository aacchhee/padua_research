# Handoff 02 — signed Padua MZ frontier — independent mathematical audit

- Status: done in 911ef85720f01ea1057bfff9343eedc019397f5d
- Previous handoff: [01-work.md](01-work.md), done in dee638408505c9977f3febd98fdd42c9bc512c92
- Next agent / model / effort: Claude, Opus 5.5 xhigh
- Role: distinct independent auditor and topic orchestrator for the audit step
- Branch: `codex/padua-mz-2d-frontier-20261105`
- Input head SHA: `dee638408505c9977f3febd98fdd42c9bc512c92` (development output candidate, distinct from the later commit publishing this handoff)
- Main / base: `440d1079e42c3ef21c40d1cf8870f5b206410c6a`, refetched unchanged at development close
- Stage: AUDIT
- Written: Codex orchestrator, 2026-11-05

## Task and decision

Read rules at the current branch head and record its full SHA. Fetch current main and topic/PR heads, preserving published history. Independently audit the complete development candidate above. This branch contains new mechanisms and negative mathematical claims: read the **complete state/IDEAS.md**, every obstruction/disposition table, relevant full predecessor records and the retained candidate files. Do not omit that gate because supplementary checks already exist. Claude Opus5.5 xhigh is requested for the novel signed spectral countersequences and uniform norm proof. The Astra high checks supplement, not replace, this distinct audit.

Developed answer differs from the initial positive working hypothesis: the signed spectral targets are false, while the C→L2 operator target is true. Determine whether every proof, quantifier, status and proposed disposition is justified. Return actionable findings instead of silently changing developer mathematics and approving the changes yourself.

## Claimed results and exact limits

1. `theory/f12-local-weight-asymptotic.md`, provisional PD-T…12: for every fixed retained j,k, along evenm, `m^4 w_jk/logm→−16e_j e_k(−1)^j`; global bound `4096[(1+j)(1+k)+log(m+1)]/m^4` holds over the whole grid. Check integrated cardinal normalization, exceptional mode, rectangle-minus-triangle identity, two delta-thin spectral strips, ordered limits and moving endpoint factors.
2. Negative carrier PD-N…13: `T_(m/2)(x) F_floor(am)(x) F_floor(bm)(y)` has admissible total degree, bounded continuous norm and signed energy/logm→−16ab/9. Positive carrier PD-N…14: the polynomial cosine difference, equivalently `sin(mt/2)sin(rt)` in angle notation, gives energy/logm→+8ab/9. Check degree-r versus length-r Fejer convention, finite DCT factors, top coefficient, whole-grid summable domination, continuous norm and variational signs.
3. `f3-fixed-ratio-threshold.md`, provisional PD-N…f3-01: eta=0 at theta<=1/2; for every fixed1/2<theta<1 both signed extrema diverge in opposite directions along evenm, already on Pi_floor(theta*m). This refutes the positive assertions in PD-T110/028/116. No effective onset, named finite certified violation, odd-m classification or sharp extremal order is claimed. Preserve original formulations/history and distinguish the old positive assertions from the resolved counterexample alternatives.
4. `f4-uniform-density-bound.md`, provisional PD-T…f4-01: every m>=2,0<=n<m has `2<=||H_(m,n)||_(C→L2)<=C*=28.3763348311…<30`. Check the absolute triangular-tail identity, O(1/m) remainder, raw Chebyshev loss, CC sine floor, checkerboard mass<=4, exact weighted-L1 norm and all edge cases. F4 needs neither signed positivity nor a uniform absolute-Gram spectrum; its norm domain is C, consistent with spectral divergence.
5. Positive-reference smooth diamond theorem, provisional PD-T…f3-01: full explicit filtered reconstruction and regularized sampled-energy equivalence. Check scalar plateau/support, parity lift, diagonal localization, discrete packing, weight Schur bounds and constants. It is explicitly a separate positive reference, never a signed-energy transfer.
6. Warmups: one scoped1-D sign-discard obstruction and harmonic low-Rayleigh boundary-mass escape. They do not resolve PD-T027 or classify actual spectral eigenvectors. That genuine1-D sharp upper-limit/gap question remains OPEN.
7. Separate computer-assisted cases60/80 (provisional PD-T…90/91): strict brackets in report, with actual independent whole-pencil reconstruction and fresh-transform exact acceptance. Producer covers every integer2..60 plus80; independently accepted set is exactly10/20/30/40/60/80. Do not call it a complete independently certified2..80 range. m100 was stopped without acceptance.

All claim-level proofs and statuses live in theory/, not just LOG. Inspect all candidates, including failed/equivalent/deferred routes and the deferred unmodulated Fejer variant. No global historical-novelty or new primary-fulltext claim is made. PR21's unmerged literature comparison is context, not a trusted theorem dependency.

## Read first

AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md; handoffs01/02; LOG, report, plan, gates, numerical-plan/results, attemptsF1–F4, all ideas and theory files; independent-checks-g0/math/cert; code and compact evidence; proposed-record-changes; allocations and scan; COLD_STORAGE and cold-storage.json. Read the frozen predecessor definitions and PD-T101/106/107/111/112/115/117 plus required CC dependencies PD-T013–024 and scoped negatives PD-N044–053. The complete development inventory pins84 identities, excluding mutable LOG/handoffs.

## Actual checks and reproduction

Start with:

```sh
python topics/padua-mz-2d-frontier-20261105/code/evidence_manifest.py
OPENBLAS_NUM_THREADS=1 python topics/padua-mz-2d-frontier-20261105/code/independent_carrier_check.py /tmp/audit-carrier.json
python topics/padua-mz-2d-frontier-20261105/code/independent_f3_check.py /tmp/audit-filter.json
OPENBLAS_NUM_THREADS=1 python topics/padua-mz-2d-frontier-20261105/code/independent_f4_check.py /tmp/audit-norm.json
```

These are supplementary regression programs, not substitutes for reconstructing all-m analytic proofs. The checker report pins reviewed proof hashes and distinguishes executed runs from inspections. Independently rerun consequential exact/native code at an appropriate scope; commands and trust limits are in certifier-results.md and independent-checks-cert.md. The port uses native C/GMP rational pencil construction and native FLINT integer congruences through Python, not a standalone C checker. Different-language independent reconstruction uses Fraction/repeated reflections and fresh scale1e13 transforms, but shares FLINT and the signed-dominance predicate. Inspect canonical arithmetic, positive common scales, offblocks, invertibility implication and malformed controls.

Fresh cloud replay can install python-flint0.9.0 to a scratch target. Regenerate the C pencil into the scratch path expected by the historical receipt, or pass the newly generated receipt to independent_cert.py. Historical scratch paths are not prerequisites for analytic proofs. Full exact m80 developer and independent runs took about302/569s under shared load; m60 about47/233s. Do not execute a huge campaign merely to reproduce finite illustrations unnecessarily.

Numerics: new operator agrees with small dense reference including oddm9/11; continuous G3 Gauss integration is degree-sufficient and refined. G2 fits are INCONCLUSIVE because heldout upper600/800/1000 is incomplete. G3 kills original localized R1. G4 actually ran m2..239 at both offsets,476 rows, no hits; posthoc minimum-onlym1600 is about−.0234144 with residual1.95e−13 but is **uncertified at that finite degree**. The analytic negative countersequence does not supply an effective onset or certify that point. G5 numerical screen NOT RUN, purpose superseded by the analytic norm proof. Verify dated gate pivots preserve original criteria and do not claim unrun success.

## Evidence and scope limits

Only this topic and its dedicated results file differ from main. No final IDs or shared scientific registries were changed. Reservations: T294–323/N104–115/IDEA384–413/LIT574–581, first pushed e79c576 and linked from draftPR23; unused IDs are permanent gaps. Recheck live union before any later assignment/readiness, including the parallel Lanczos frontier and all active PRs. No new reservation is needed for this audit.

Bulk output is regenerable local scratch, not an archival delivery. Small receipts/code are committed. Cold-storage.json has zero Git-backed entries plus a separate inventory of12 actually present staged files; the existing storage tool cannot export fresh scratch without Git blobs. External delivery remains PENDING. Do not infer durability from the empty-entry verification. Check whether any computer-proof premise genuinely requires retained bulk; the independent checker regenerates the complete exact pencil and transforms.

Preserve previous handoff bodies, source receipts and developer proofs. Only edit your audit outputs and orchestration metadata; return mathematical findings for developer response. Do not merge, force-push, tag, touch .github/, compute elsewhere, or mutate another topic. Only AC merges.

## Outputs and next handoff

Write audit-01.md with exact candidate/hash scope, full novelty read coverage, independent reconstruction and actual reruns, claim-by-claim status decisions, findings/severity and residual limits. Audit the proposed historical-OPEN/refuted disposition display explicitly; an old label must never make a refuted positive assertion usable or unresolved. Update LOG, dedicated results and PR23 WORK/AUDIT/PR sections with accurate audit disposition, retaining draft unless audited preparation is separately complete.

Findings set WORK and open a numbered developer-response handoff. Acceptance sets PR and opens a numbered preparation handoff (fresh reservations, final mapping/shared updates, integration impact/rehearsal as applicable). Do not silently perform preparation during the audit. Commit audit outputs first, then in a following commit mark this handoff done in that output SHA and add the next numbered handoff; push before replying. Exactly one handoff remains open. Only AC merges.
