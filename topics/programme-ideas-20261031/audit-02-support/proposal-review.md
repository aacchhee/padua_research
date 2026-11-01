# Proposal re-audit — response-01 and addendum

- Audited head/rules: `cadb35066160e466cb1704b9791ad6f374446422`.
- Integration base recorded by parent: `9739a0c`; root owns all Git operations.
- Independent auditor: Codex supplementary proposal subagent; requested `gpt-6-astra xhigh`, runtime model/effort not independently exposed.
- Scope: audit-01 A1/A6 and proposal-related A9 corrections; PD-T?programme-ideas-claude-04/05/06, revised proposal/report/decisive file, IDEA-17, OPEN_TARGETS A1–A5, exact n=3 edge identity. Rules read at this head; complete prior state/IDEAS read in audit-01 and all additions since614709d read now, including new disposition/obstruction tables. No new mechanism or novelty claim is proposed here.

## Accepted corrections

1. `proposal-1.md`, `report.md`, and PD-T04/05/06 now distinguish the OPEN expansion/argmax from MEASURED finite evidence and counts. The pre-registered fit spread±3.3e-5 and selected post-registration model stability±2e-12 are reported separately; T2 precision/separation is inconclusive. Failure of PSLQ does not identify a new two-dimensional constant. The former recommendation to send a correction is withdrawn. The count proof obligations explicitly preserve the four logical gaps from audit-01, as well as rigorous arithmetic and an independent checker. Both first papers are described as unfinished.
2. PD-T04 OPEN, PD-T05 OPEN, and PD-T06 MEASURED correctly retain their intended statements and epistemic labels. Supporting finite measurements are explicitly scoped; no prior substantive PROVED claim is downgraded by these records. The new n=3 identity is a small supporting calculation, not a claim that the counting target has become PARTIAL or PROVED.
3. Current code is described as Padua-specific. The recorded minimum margin4.34e-7 at n=6 is correct. T1 summaries now say no counterexample on finite meshes at75 tested degrees, rather than proving the continuum/all-degree assertion.
4. Exact edge identity accepted: the developer script was independently executed and its output matches. A separate verifier checks the proposed degree3 polynomial by Kronecker values at all10 exact nodes and nonzero Vandermonde determinant243/16. Thus

   `L_(2,2)(x,y) = (x-1)(2x^2+x+2y^2-2)/3`

   is the cardinal polynomial of node(-1/2,0). Its restriction and all tangential derivatives onx=1 vanish; in angle coordinates its normal first derivative also vanishes atθ=0. This confirms the claimed identity used in A5-partial. It does not locate/enclose the background critical point and does not repair the discarded-box logic or certify any count.
5. All files in `checks/code/decisive/gen4-2/` have identical Git blob IDs at614709d and the audited head (comparison in `proposal-identity.json`). The expensive unchanged T3 replay was not repeated; audit-01's actual replay and independent220-point validation retain their original scope.

## Remaining finding — Major (A1/A6 not fully propagated)

The **live canonical IDEA-17** still contains unstruck current claims that contradict its corrected theory records and the response's claim of withdrawing them everywhere:

- `ideas/candidates.md:451` rejects the published39/42/56 and adversary29/38 as “undercounts (certified41/50/62)”; this is an active disposition, not a historical quote.
- `ideas/candidates.md:450` says the adversary's counts were “later shown to be undercounts.” The current evidence supports only a disagreement with the candidate counts, pending certification.
- `ideas/candidates.md:442` says the second-order term “stands and is now MEASURED to12digits,” without the required model-conditioned/post-registration qualification or the failed original precision target.

Required resolution: replace these current scientific statements with the accepted MEASURED candidate-count and post-registration fit-stability wording. Retain the superseded text as expressly historical or struck if desired. Search the response-edited source for remaining active versions of the same claims: for example `checks/decisive-gen4-2.md:90,95` still calls the counts “certified,” and its T1 result paragraph still says the theorem is “true in the whole tested range.” Its new header and adjacent corrective notes substantially qualify these passages, so they are less serious than the canonical IDEA disposition, but making the historical/current distinction explicit would complete the promised propagation.

This is a consistency/status finding. It does not refute the measured counts or fits.

## OPEN_TARGETS clarifications — Minor

- **A4, line47:** the proposed “Done when” conditions are insufficient as written. An expansion at a corner and an edge midpoint, plus a bound outside their neighbourhoods and finite small-n checking, leaves the neighbourhood interiors uncontrolled. Add local upper bounds throughout each remaining corner/edge neighbourhood (and strictness away from the corners if the stronger “attained only” target is intended), or state another complete coverage argument. A point-value comparison does not exclude a nearby higher bump. The argmax conjecture remains OPEN; this is a proof-plan omission.
- **A1, lines5/13:** define `U_m(t)=sin(mt)/sin(t)` by its continuous extension at integer multiples ofπ. Actual corner/node terms hit these removable singularities, so the literal ratio is otherwise undefined in the displayed all-corners formula. This is a routine definition correction, not a counterexample to the intended identity.
- **A2, line35:** distinguish the global Padua Lebesgue constant from its corner value. The cited Kolomoitsev–Lomako Theorem2.1 as inspected in audit-01 establishes the former's leading term. It does not by itself prove the same asymptotic forΛ_c without an extra corner lower-bound comparison. Restrict the “Known” sentence to globalΛ and retain the corner-leading step as an obligation, or provide the exact source/proof bridge. No new source fetch was performed in this re-audit.

## Commands executed and evidence

From `/workspace/programme-integration`:

1. `python topics/programme-ideas-20261031/checks/code/response-02/padua_n3_edge_identity.py > topics/programme-ideas-20261031/audit-02-support/proposal-edge-rerun.txt` — exact output matches the developer's committed output.
2. `python topics/programme-ideas-20261031/audit-02-support/proposal-edge-independent.py > topics/programme-ideas-20261031/audit-02-support/proposal-edge-independent.txt` — independent exact nodal/uniqueness check PASS, with JSON evidence. Python3.12.14; SymPy1.14.0; no randomness or numerical tolerance.
3. Read-only Git object comparisons of the decisive gen4-2 subtree at614709d andcadb350; no changed producer/checker/output blobs.

Source and output hashes, sizes, Git blob identities, and this report's identity are recorded in `proposal-manifest.json` and `proposal-identity.json`. No developer files were modified. No Git mutation or external communication was performed by this subagent.

Disposition: accepted corrections above; one remaining Major propagation finding and three Minor target-definition/proof-plan clarifications. Root decides the integrated audit outcome. No new count certification or expansion proof is claimed.
