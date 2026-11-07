# E08 actual-origin lower allowance — Paper development record

Rules/input: 8f1211b6162b0e49e042f293665b3a4a7e95f667, 2026-11-07.
Branch codex/padua-argmax-bridge-20261105. Assigned mathematical developer,
parent-requested Codex Sol xhigh; serving metadata unexposed. Parent
alone controls Git, LOG, results, registries, handoffs and integration.
Owned only E08-origin-lower.md under theory, ideas and attempts.

## Outcome and exact scope

The [theory](../theory/E08-origin-lower.md) gives a complete developer
paper proof, distinct audit pending, of E_n(0)>=-e0 for every integer
n>=32, both parities, with

    e0=D+Mesh+pi[log n+25log(2n+2)+193/3]/[8(n+1)^2]
             +1/(8n^2)+[71/n^2-22/(45(n+1))]_+.

D and Mesh are the unchanged E02/D16 functions. Scalar e0 is positive
and strictly decreasing on all real n>=32 and smaller than old E0.
The positive part vanishes for all real n>=148. From n>=160 the
usable lower allowance is D+Mesh+1/n, also strictly decreasing.
This is a one-sided origin improvement only, without a new global
onset or a claim E_n(0)>=0. No equality/sign/limit conclusion was
inferred from PD-T271 decimal enclosures.

## Read/search coverage and chronology

At the input head, read AGENTS.md, agents/WORKFLOW.md and
agents/codex/CODEX.md and the current topic allocation. Rules hashes:

- AGENTS.md: `c44a76f138fce01f02c06753b22fbc83fd5c1ee701785d49ba17cef5f8eee05b`
- WORKFLOW.md: `65e6b7268f4df4c97a3271ead27199381747b940ebba5cce2796a0bf7b8b9209`
- CODEX.md: `871b4f8e18d207c9ba25933ff413e7bedf32d1d036b2f7d5b4ecec397f257610`

The full registry scan, searches, corner shortlist, dispositions and
read-snapshot hashes are in the canonical
[idea record](../ideas/E08-origin-lower.md). It records a **narrow
unwaived prospective-gate timing defect**: the full corner gate
preceded the direct candidate, but full newly shortlisted E02/E03
operator records were completed after the first operator intuition.
No retroactive compliance or permission waiver is claimed. The exact
four late full reads are identified there. Parent was informed before
freeze. All those reads finished before writing the theory. This
attempt does not claim a complete prospective gate for that refinement.

Read-only commands used rg/rg --files across registries, topic records,
theory, logs, literature INDEX and negative-result descriptions; sed
and cat read exact records in bounded chunks. Initial broad truncated
registry output was repaired by overlapping narrow reads. Read-only
git rev-parse/status inspected head and unrelated work; sha256sum
identified rule/catalog and final artifact bytes. A stale nonexistent
D03 theory path was corrected to its actual idea/attempt, and a stale
D07 six-row path was corrected to D07-endpoint-six-row-allowance.md.
Neither failed read was counted as coverage. No source/PDF was opened.

## Mathematical development and cheapest checks

1. Reconstructed the PD-T159 exact corner, endpoint 1/m, weights and
   same-mesh L_n^2 identity; PD-T269 deformation and PD-T270 harmonic
   sum were read at their original finite scope. D03's exact origin
   polynomial identification gives
   E_n(0)=Delta_n-kappa-(L_n^2-1)/m+(L_n^2-A_n^2).
   This exposes why finite deformation positivity or a logarithmic
   mesh shift alone cannot prove the stronger sign. That alternative
   was stopped without claiming a target refutation.
2. The accepted complete origin telescope leaves D and Mesh unchanged.
   At origin D07's R2 four positive samples are (pi,0) twice and
   (2pi,+/-pi). Their exact reciprocal-displacement bracket is
   pi^(-2)[4/mu+2/(2mu-1)+2/(3(2mu+1))]>=56/(9pi^2).
   Four endpoint errors give -4/m, actual central rows give +2/m,
   and accepted finite geometry costs <=71/n^2. Thus Eret(0)>
   22/(45m)-71/n^2. No row/collision reference was substituted.
3. For the exact fixed F0 operator, both actual initial holes and
   both actual central holes were retained. Reapplied E02's derivative
   variation to [h/2,pi-h/2], increasing log m to log(2m), rather than
   extending the old [2h,pi-h] quantifier silently. Midpoint error costs
   pi V/(4m^2). Initial positive-hole integrals cost
   119pi/(24m^2)+1/(8n^2). On both central holes the complete F0 is
   <-1/25 for n>=32, so their omitted integrals help a LOWER bound.
4. Assembled all terms and differentiated explicit scalar functions.
   n Bout strictly decreases for real n>=32; rational bounds at 32
   and 160 give Bout<3/n and Bout<1/n on the corresponding half-lines.
   The positive part decreases until its unique zero and then stays
   zero; it is zero from 148. This proves all stated unbounded-range
   transfer and strict improvement over old E0 analytically.

These are paper calculations written in the proof, not claimed
executions of an exact-arithmetic or interval checker. The first
operator proposal reported to parent had the same displayed e0,
Bout and 22/45 gain as the final theorem; its status was explicitly
unadopted/proof in progress, with distinct review required. No initial
numerical or unverified origin-nonnegative claim was adopted.

## Computation, evidence and independence

Actual mathematical jobs: **none**. No scripts, scalar evaluations,
quadrature, endpoint checks, native/source jobs, pack jobs, fits or
degree scans were run. No measured numerical claim or execution
receipt is created. Only read/search/hash/prose and read-only Git
inspection were used; edits are the three allocated Markdown files.
No CPU timing, independent rerun or audit acceptance is invented.

Independent audit is requested via parent with frozen hashes of all
three artifacts. Audit should reconstruct exact (8)--(12), retained
row multiplicities and 22/45, the full F0 hole signs and derivative
variation on its enlarged interval, and all-real-n monotonicity.
The canonical chronology defect must remain separate from acceptance
or rejection of the mathematical theorem. No computation is needed
for this paper scope. If an auditor finds a mathematical gap, return
it with exact scope; no weaker global conclusion may be inferred.

Runs needed: none for this analytic theorem. A separate future global
assembly/source/pack task requires its own authorization and complete
proof contracts. This allocation stops at proof freeze and distinct
audit; no new candidate, source edit, shared-file edit or final ID.
