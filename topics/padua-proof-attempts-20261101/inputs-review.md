# Supplementary input and novelty review

- Rules/input SHA: `cadb35066160e466cb1704b9791ad6f374446422`.
- Reader: Codex supplementary input reviewer, assigned `gpt-6.1-sol xhigh`; runtime-resolved model/effort metadata is not separately exposed.
- Scope: input review only, before developing B5/A5; this is not the required Claude audit and reports no new mathematical result or execution of a scientific checker.

## Reading and search receipt

Read `AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md`, the complete uploaded task, all 496 lines of `state/IDEAS.md` (headings, identifiers, aliases, summaries and every obstruction/disposition table), all 122 lines of `literature/INDEX.md`, and `topics/programme-ideas-20261031/OPEN_TARGETS.md`.

Read the complete programme THEORY records 01, 04, 06 and N04; programme IDEA-08 and IDEA-17; the T2/T3 preregistration, results and response-01 corrections in `checks/decisive-gen4-2.md`; audit-01 A1; and `audit-support/proposal-review.md`. Read MZ IDEA-069 and its linked `tracks/mz-constants/theory/m2-l1-obstruction.md` (PD-N005). Source-record locator searches also inspected the existing Padua 2006/2007/2008 literature records; no primary publication was newly fetched or read by this reviewer.

Search actually run from the repository root:

```text
rg -l -i 'rhombus|corner.value|corner.kernel|pattern.commutant|degenerate.max|absolute.cardinal' state topics tracks literature
rg -n -i 'kernel|lagrange|corrected|Theorem' literature/lattice-unisolvence/records/padua-2006.md literature/lattice-unisolvence/records/padua-ideal-2007.md literature/lattice-unisolvence/records/caliari-demarchi-vianello-2008.md
```

Additional shortlisted-ID lookup: `rg -n 'IDEA-069|mz-constants-codex-25' topics/mz-constants/directions/M2/candidates.md`. The mechanism search returned the existing programme theory/checks/audit/report records and the MZ absolute-column obstruction. This is a bounded repository search, not a historical novelty clearance.

## Closest entries and distinctions

| Target | Closest entries read | Distinction to preserve / cheapest kill |
|---|---|---|
| A1 | Programme IDEA-17; PD-T?programme-ideas-claude-04; LIT-002/003 and LIT?lattice-codex-13/14/31 | Prove the exact finite corner identity already numerically observed, using the stated even checkerboard and normalization. This is proof completion of an existing target, with no new mechanism or priority claim. An exact mismatch kills this formula. |
| B5 | Programme IDEA-08; PD-T?programme-ideas-claude-01 and PD-N?programme-ideas-claude-04; contextual IDEA-014/039/051 | The proposed theorem is generic and degree-scoped, unlike the already refuted universal three-dimensional commutant claim. Each claimed degree requires an exact witness and a valid genericity argument. The Padua degree-two dimension-six example remains valid and must not be relabelled. |
| A5-partial | Programme IDEA-17; charter IDEA-048; PD-T?programme-ideas-claude-06; audit A1/P1 | Discharge only the degenerate identities, background root and rigorous Hessian bounds actually covered. Existence of these local identities does not certify completeness or the six total counts. |
| Padua contextual comparisons | IDEA-047, IDEA-048, MZ IDEA-069 / PD-N005 | IDEA-047 concerns Morrow–Patterson order bounds, IDEA-048 the Padua maxima question, and IDEA-069 the failed uniform absolute-cardinal L1-column route for CC MZ lower bounds. None supplies the missing proof here; the failed MZ hypothesis does not refute Padua corner identities or local maxima. |

No additional IDEA candidate is proposed in this review; the three targets are already retained in `OPEN_TARGETS.md`. Paper-level novelty, full source reading and historical attribution remain outside this bounded gate.

## Review cautions for development

1. **A1 conventions.** The author-preprint locator already recorded for the 2006 corrected-cardinal formula is Theorem 2, preprint p.8. The 2008 families rotate/reflect coordinates, so the exceptional correction axis and parity choice must be translated explicitly. The target starts at n=1 and includes node corners and removable sine-quotient singularities; testing only the large non-node corner is insufficient. The source theorem must be newly checked as LITERATURE by the developer, rather than inheriting the old record's reading or proof.
2. **B5 analytic argument.** Matrix entries may depend real-analytically on the parameters; the integer-valued rank itself is lower semicontinuous, not generally analytic. One nonzero analytic minor gives density on the component containing that witness, without a proof that the parameter domain is connected. A rational LDL representation and a nonzero polynomial numerator would avoid silently assuming connectedness. The diagonal scaling must preserve both the prescribed support and the correct symmetry condition (weighted self-adjointness in the rational basis); arbitrary similarity does not preserve ordinary symmetry.
3. **A5 coverage.** Log the actual `degenerate_max` call sites, outcomes and Z sets; a table of accepted notes alone may omit unsuccessful calls if the task is read literally as every use. Distinguish this path from the separate corner and edge-node handlers. Numerical angle coordinates in the old JSON are approximations, so the proof should identify exact points and explicitly enclose their relation to the recorded coordinates. Signs of background cardinals and validity on the claimed neighbourhood need rigorous checks.
4. **Remaining certification.** Preserve all four other A5 obligations: finite reduction/coverage, rigorous per-pattern root exclusions over the discarded region, all consistent sign-pattern decisions without the early return, and exact crease-crossing treatment. Rigorously proving local degeneracy conditions alone does not repair those logical gaps.
5. **Statuses and ownership.** A1 completion does not prove A2/A3 or the global corner argmax. B5 witnesses through n=6 do not prove all n. Keep existing records untouched and propose exact old-to-new edits separately. Any computer proof still needs the finite reduction, exact/rigorous arithmetic, committed essential evidence and an actual independent rerun.

## Unresolved items

No primary-source verification, scientific checker run, proof acceptance, final ID allocation or registry write was performed by this reviewer. Claude (Opus 5.5 xhigh) remains the assigned auditor for the final candidate.
