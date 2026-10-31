# Current frontier

Updated: 2026-10-31. Owner: AC. Campaign topic: [charter and exploration](../topics/charter-unisolvence-20261031/LOG.md).

## Campaign charter

Subject: algebraic characterization of unisolvent bivariate node sets for total-degree interpolation over an arbitrary field K, with Padua-type sets as the motivating family. For m≥0, Π_m=K[x,y] of total degree at most m; an N=(m+1)(m+2)/2 point set is unisolvent when evaluation Π_m→K^N is an isomorphism. Distinct labelled X=(h_0,…,h_m), Y=(g_0,…,g_{m+1}) define S_e={(h_i,g_j):i+j≡e mod 2}, e∈{0,1}; both have N points. Labels matter.

Background: Van Barel–Chesnokov, Numer. Algorithms 55 (2010), 383–402, relates a zero pivot of the bivariate orthogonal-polynomial recurrence to a polynomial vanishing on the nodes. This is a supplied literature attribution, not a locally checked proof. Here rank deficiency of the evaluation map, and explicit polynomial certificates, are the algebraic target.

Success criterion: prove U1, or refute its exact stated scope with a precisely checked counterexample; then pursue surviving U2 generalizations and U3 consequences as far as evidence and round budget carry. U1 asks whether S_e is unisolvent iff both alternation functionals L_H(f)=Σ_i(-1)^i f(H_i)/ω_H′(H_i) have all leading Hankel minors of orders 1,…,|H|-1 nonzero (the source's finite-support quasi-definiteness cutoff). The finite cutoff is explicit: ordinary infinite quasi-definiteness is impossible for a finite-support functional. Characteristic 2 is included in the question until separately resolved.

Model: exact field arithmetic for proofs. Real ordered positivity is a special hypothesis, never silently imposed on arbitrary fields. Algebraic closures, generic nodes, symbolic indeterminate nodes and oracle data are allowed only with explicit labels. Finite-field and floating-point samples are MEASURED. Computer proofs require a proved finite reduction, exact committed checker and evidence, and independent rerun.

## Scope and working policy

U1 checkerboards is the priority. U0 registers finite-field Padua existence/rationality, discriminant, quadratic-character sets and small evaluation codes after independent re-verification. U2 records other parity/lattice patterns; U3 records kernels, Lagrange formulas, cubature, discrete forms, algebraic zero-pivot certificates and labelling counts. At most two substantive directions at a time. Ten conceptual rounds each, extendible to twenty only with a recorded justification; automatically continue a concrete opening.

Out of scope: finite-precision Lanczos/recurrence theory; complexity of bivariate moments→orthogonal polynomials (aacchhee/bttb-research, codex/bivariate-schur-campaign-20261031); 3D Padua points; Marcinkiewicz–Zygmund constants. General d≥3 pattern questions may only be registered without developing excluded 3D Padua or the parallel moment-complexity campaign.

Step 0 is a literature baseline under AC's explicit override, not a complete novelty gate. Every candidate retains its closest predecessor, falsifiable separation and kill test, and receives a prior-art check and independent adversarial reconstruction before acceptance. Retain failed routes, corrections and side notes; scoped PD-N only for refuted/failed mechanisms. The public repository contains citations and statements, never third-party PDFs or fulltext extracts.

## Evidence and next step

Source import verified17/17 checksums; bounded exploration and independent supplementary checks are complete. [Plan](../topics/charter-unisolvence-20261031/plan.md), [progress](../topics/charter-unisolvence-20261031/progress.md), [literature baseline](../literature/INDEX.md). Claude audit-01 ACCEPTED the mathematical scope and all status/disposition classifications; response-01 resolves A1/A2 and records AC’s A3 waiver. Written epistemic statuses are unchanged in PROOF_STATUS.md.

Cold storage chosen by AC: `C:\Users\andreyac\Downloads\padua\cold_storage\charter-unisolvence-20261031\`. Stage handoff files and a manifest; do not claim Windows delivery from the cloud workspace.

Stage PR. Next: `Codex (gpt-6.1-sol medium): Continue codex/charter-unisolvence-20261031 — check PR #2 readiness before AC’s merge.`

## Developed results and retained frontier

PD-N001 refutes original U1 necessity in characteristic2 (F4,m1 andF8,m2). PD-T001 proves its exact characteristic≠2 restriction; PD-T002 gives a corrected even-index barycentric criterion over every field, both parities, allm≥0, with within-axis distinctness only. For lengthL axes, the corrected cutoff is1,…,floor((L−2)/2); empty ranges are vacuous. PD-T003 gives the monic-OP kernel/discrete-product cubature consequence in characteristic≠2.

PD-T004–008 prove canonical good-characteristic Padua Gram/unisolvence, finite-field rationality, Dickson squared discriminant, quadratic-character description and general code structure. PD-T009/010 keep finite checks/distances MEASURED. PD-T012 proves universal linear-code upper bounds matching the measured q7 attainments. PD-T011 retains ideal/recurrence and unrestricted-transform source extensions OPEN, deferred after bounded registration. U2 other-pattern and U3 counting/pivot/decoding frontiers remain deferred.

Mechanisms are conservatively attributed to existing determinant and kernel theory; no publication-level novelty claim. [Track](../tracks/unisolvence/README.md), [ranked report](../topics/charter-unisolvence-20261031/report.md), [audit handoff](../topics/charter-unisolvence-20261031/AUDIT_HANDOFF.md). Four U0 and five U1 conceptual rounds used; no extension or ultra assignment. The source theory remains retrievable through frozen commits and the ID crosswalk.

## Post-audit PR preparation

[Audit-01](../topics/charter-unisolvence-20261031/audit-01.md) accepted the mathematics. [Response-01](../topics/charter-unisolvence-20261031/response-01.md) resolves the registry-link and stale-handoff findings without changing claims, proofs, checkers or statuses. The [shared batch ledger](../topics/padua-batch-20261031/ALLOCATIONS.md) records charter first, MZ second, and the remaining topics in AC’s chosen order; later members must reconcile/rehearse before their own readiness.

AC stated: “I have no windows python. proceed as is, no need to check”. The Windows verification/receipt requirement is therefore waived for readiness. Cloud bundle integrity is verified; Windows delivery and verification remain unconfirmed and are no longer blocking. No merge, force-push, tag, rule or workflow change is authorized by this waiver. Only AC merges.
