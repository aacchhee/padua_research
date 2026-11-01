# Codex audit-03 — focused review of response-02

- **Decision: ACCEPTED for audit-02 B1–B4, with two nonblocking preparation notes below. Stage PR (preparation); draft PR #6 is not yet merge-ready.** No further scientific development or broad numerical replay is required to close these findings.
- Audited candidate/rules: `0ef90edc5b4d5639474cca7fa8d6d688e684e505`.
- Previous audit delivery: `39c5ae616111e47798c06229eca6d366bbcd9583`; prior scientific review remains audit-02 at `cadb35066160e466cb1704b9791ad6f374446422`.
- Main refreshed: `9739a0c56b7a3976422ce60a8441bfbbfd6554df`, already an ancestor; no merge needed. Working checkout was clean before fast-forwarding to the exact candidate.
- Reviewer/orchestrator: independent Codex, user-requested `gpt-6-astra high`; one supplementary target-formulation reviewer was explicitly allocated the same model/effort. Resolved runtime model/effort metadata is not independently exposed. Date: 2026-11-01. No developer files were repaired by the reviewer.

## Scope and decision

This is a focused review of the 13-file response-02 diff, its complete response table, affected canonical IDEA records, decisive-test annotations, three theory-record refinements, shared N03/N05 scope rows, open-target formulations and new small exact check. The review does not reopen unchanged scientific results, certify local-maxima completeness, prove an OPEN target, or clear publication novelty. Applicable rules were reread at the candidate and are unchanged from audit-02. The prior complete ideas/literature gate is retained; current registry annotations and relevant full records were checked against it. No new mechanism or priority claim is introduced by the response.

| Finding | Focused-review disposition |
|---|---|
| **B1 — canonical certification/precision remnants** | **Closed.** IDEA-17 now explicitly strikes the old certified-undercount disposition and twelve-digit second-order claim, preserving them as superseded history. Current wording retains candidate counts as MEASURED, the expansion/argmax as OPEN, and distinguishes the failed preregistered precision target from post-registration model-conditioned stability. Published and developer lists are no longer rejected on the basis of an unproved certificate. The decisive record's explicit response notes/table/verdict clarify the same limits; see N1 for residual editorial labels in that historical record. |
| **B2 — orbit-count scope** | **Closed.** IDEA-10 labels the old refutation verdict historical and limits the orbit argument to unrestricted GL gauges under its stabilizer assumption. The normalized-family staircase remains OPEN; investment abandonment is separate from refutation. |
| **B3 — nearby reference pairs** | **Substantive formulation repair accepted.** The target now defines computed-section/reference classes, positive pivot bound, pair metric, commutator defect, marginal spectral gap, reference neighborhood, explicit non-emptiness obligation, and constant dependencies. It remains an OPEN research question. N2 supplies a routine positive-gap boundary convention before using that target. No truth, exponent or count correctness is accepted for S(α) or S_F(α). |
| **B4.1 — parity and saturation** | **Closed.** N03, its registry summaries and the addendum distinguish universal even-degree centre cancellation from contradiction of a positive-deficit bound when `s<1`. The saturated example is reproduced exactly. The formal parity theorem is unchanged. |
| **B4.2 — measured Fourier scope** | **Closed.** N05 and shared rows now state n=1…6 at M=64 and n=1…8 at M=128,512, and record the generic-4/n=8 identity-error exception up to `2e-12`. The measured nonzero verdict and invariance dependency are unchanged. |
| **B4.3 — finite gauge** | **Closed on the stated nondegenerate cyclic class.** The proof replaces the free full-group/principal-bundle claim with a local finite-stabilizer description; the dimension is unchanged. Cyclicity justifies the effective action: a block gauge commuting with the pair sends the first-block vector to ±itself; commuting through all polynomial words then forces the gauge to be ±I on the cyclic space. |
| **B4.4 — argmax completion** | **Closed as a proof-plan repair.** The completion criterion now requires local bounds throughout the remaining corner/edge neighborhoods, global complement control and finite verification, or another full covering argument. It no longer treats point expansions as neighborhood control. No argmax proof is supplied or accepted. |
| **B4.5 — limits and source scope** | **Closed.** The sine ratio has the correct continuous extension `U_m(jπ)=(-1)^(j(m-1))m`. The global KL asymptotic is separated from the unproved matching corner lower bound. |
| **B4.6 — rational finite dimensions** | **Closed as an OPEN-target specification.** Nonzero denominators, full evaluation dimensions through t+1, the finite admissible degree range and a pole-class/general-position condition are explicit obligations. No rational recurrence lemma is accepted. |
| **B4.7 — genericity route** | **Closed as a proof-route repair.** The route explicitly calls for checking a rational/monic-basis reduction and clearing denominators to obtain a nonzero polynomial minor, rather than applying analyticity across disconnected components. Under the declared `H=D⁻¹ĤD`, the substitution `F=DED⁻¹` gives the claimed commutator and weighted-symmetry equations. A witness and the genericity proof remain unperformed/OPEN. |

The five scoped negative records retain the audit-02 conclusions: **N01/N03/N04 PROVED; N02/N05 MEASURED**. T01–T03 remain PROVED; T04–T05 OPEN; T06 MEASURED. All provisional IDs/statuses are unchanged. Audit-01 and audit-02 evidence retain their original source scopes and limitations.

## Nonblocking preparation notes

These notes do not reopen the accepted mathematical records or require another research campaign. Resolve or explicitly dispose them during PR preparation, with an exact impact check if source files are edited.

**N1 — finish the historical-evidence wording cleanup.** In `checks/decisive-gen4-2.md:81–82,97,100`, a few old phrases remain, including “certified pairs/list/maxima”, “now on certified data”, “constant identified numerically to 12 digits” and “cheap first paper”. The new response-02 header and adjacent corrections explicitly state the operative OPEN/MEASURED limits, and the canonical IDEA/proposal/theory records now agree; therefore these residual labels do not block this focused acceptance. Replace them with candidate/model-conditioned wording, or mark the entire remaining legacy recommendation paragraph historical before using it as a standalone brief. They confer no certification or paper-readiness acceptance.

**N2 — state the positive-gap convention in OPEN_TARGETS B3.** At lines 65–69, require `g(H,Q)>0` and finite `C(n,p)>0` when using the asserted Weyl boundary-free consequence. If `δ=0`, the current non-strict inequality alone also admits `g=0`, for which that consequence and the earlier commuting inertia formula's boundary-free hypothesis do not follow. In the proposed obstruction sequence take `0<δ_m→0`; clarify any intended dependence of α and distinguish the spectral boundary gap from pair distance when describing that sequence. This is a narrow domain clarification of an OPEN target, not a counterexample developed inside the computed-section class and not an additional PD-N. The new metric, radius, reference class and constant dependencies resolve the substance of the original “nearby” finding.

## Verification actually performed

Command from the pinned working checkout:

```text
PYTHONDONTWRITEBYTECODE=1 python -I topics/programme-ideas-20261031/audit-03-support/check-response-02.py > topics/programme-ideas-20261031/audit-03-support/check-response-02.json
git diff --check
```

The new developer saturated-centre script was independently executed. Its JSON exactly matches the committed result: evaluation rank 6, `s_2(0)=1`, both residuals zero. An independent exact nodal argument checks `1-x²-y²+xy`: it is 1 at the centre and 0 at the other six nodes, so its x/y products vanish on the entire support. Exact rank 6 verifies the unisolvence hypothesis. This supplements the already accepted parity argument; it is not a new registered theorem.

The checker also verifies the declared similarity/weighted-symmetry substitution algebraically on symbolic symmetric matrices, all eleven registry statuses, source identities for the 13 changed paths and protected files, and the main ancestry. **All 184 existing code/output and prior audit-support files covered by the check are byte-identical to the previous audit delivery.** Both old audit reports, rules and ID crosswalk are unchanged. Only the new small developer checker/output was added under `checks/code/`; no old scientific producer or output changed.

Python 3.12.14 and SymPy 1.14.0 supplied exact arithmetic. The final receipt records commands, results, Git blob IDs, SHA256 and sizes. An initial receipt command-path metadata variable was corrected and the checker rerun before retaining the final output; the underlying exact execution passed in both runs. No expensive unchanged maxima, high-degree corner or 80-bit rational sweep was repeated.

The independent supplementary reviewer inspected the B3/B4 target and finite-gauge changes; its bounded assessment is in [targets-review.md](audit-03-support/targets-review.md). Root alone controls Git and publishes this decision. No new external source acquisition, author contact, Windows archive retrieval or cold-storage completion is claimed. Earlier access/novelty limits remain unchanged.

## Handoff

The audit correction cycle is complete for the reviewed B1–B4 scope. Stage **PR** means preparation can proceed; it is not a merge decision or a statement that all OPEN mathematics has been solved. Keep PR #6 draft until its ordinary preparation work is complete: recorded dispositions for N1/N2, current audit-evidence metadata, coordinated final-ID decisions, literature deduplication/integration and the applicable integration check/rehearsal. No final IDs are allocated by this review. Only AC merges.

Suggested next prompt: `Claude (Opus 5.5 high): Continue claude/programme-ideas-20261031 — prepare PR #6 after accepted audit-03, address N1/N2 with an exact impact check, preserve the accepted scopes, and reconcile the remaining registry/literature work.`
