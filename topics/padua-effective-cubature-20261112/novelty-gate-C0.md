# Novelty gate C0 — Padua Lebesgue-constant corollary

Date: 2026-11-12. Author: Claude subagent (Sonnet 5.5, high) for orchestrator Claude Opus 5.5. Rules read at `0abf5e7d912b41c9b9248d4dc9f4580425683b53`. Record under test: `theory/lebesgue-constant-corollary.md` (provisional `PD-T?padua-effective-cubature-20261112-claude-01`).

## Verdict

**Corollary assembly of registered results. No new mechanism. No IDEA candidate generated.** The record is the conjunction of PD-T209/162/166/169/174/177/181/214/246 (n = 2..32), PD-T229 (n ≥ N_*) and PD-T271 (three-term expansion of Λ_c(n), n ≥ 32). The gate therefore applies in its "no novelty content" form (WORKFLOW, work cycle step 2): no mechanism is proposed, so no separation criterion or kill test is needed. Priority is handled by the literature comparison, not by this gate.

**Duplicate check.** No existing PD-T record, IDEA entry, results file or topic log states the combined corollary (the global Lebesgue constant Λ(Pad_n) as a three-term expansion, or "max λ_n = Λ_c(n) for 2 ≤ n ≤ 32 and n ≥ N_*" together with the expansion). C0 is therefore not a duplicate. The nearest items (below) state the two halves separately. PR #27 (`codex/padua-argmax-bridge-20261105`, open draft, head `8a94ce6`) states a **stronger, unmerged** result. It claims (a) the argmax for every n ≥ 2 and (b) the sharp corner expansion Λ_c = (4/π²)log²N + b log N + c − 1/N + O(log N/N²), PROVED, which its manuscript says also holds for Λ_n. If merged and audited, it would supersede **both** halves of C0. C0 would then be a weaker variant: it is recorded only because its dependencies are merged and its remainder bound (1) is numerically explicit. *Corrected 2026-11-12 after independent check M1; the earlier sentence said PR #27 would supersede only the first half.*

## Search scope

Repository at `0abf5e7d` (read-only):

- `state/IDEAS.md` (1278 lines, about 570 IDEA rows or headings): scanned by grep and headings, with aliases. Counts of matching lines, case-insensitive: "argmax" 59, "Lebesgue" 17, "asymptotic" 17, "Lambda_c" 1; "Lebesgue constant", "corner value" and "three-term" 0 (the three-term hits elsewhere are orthogonal-polynomial recurrences, irrelevant).
- Full rows read for the shortlist below. The obstruction and disposition tables were **not** read in full: no mechanism is proposed, so none can be escaped or repeated. This is a stated limit of the gate, not a claim of exhaustive coverage.
- `PROOF_STATUS.md`, `RESULTS.md`, `state/CURRENT.md`, `ID_CROSSWALK.md`, `results/*.md`: grep for "Lebesgue constant", "three-term", "max(32", "Λ(Pad", "T271" and "b log N". No combined statement found. PD-T271 is cited only as PD-T098's constant-term split and, in later topics, as an input (`topics/padua-argmax-effective-2-20261105/attempts/H2.md`, L31).
- `topics/`: grep for "b log N" and "corollary" with "global" / "Lebesgue constant". Hits are the PD-T098 records, `padua-lebesgue-followups-20261103/report.md` (L96: the corner expansion `Lambda_c(n) = (4/pi^2) log^2 N + b log N + c + o(1)`, about the corner value only) and the proposed registry additions. None states the maximum over the square.
- `topics/padua-literature-20261103/p1-comparison.md`: every row read; it has no row for PD-T271 and no statement of the global three-term form.
- `literature/INDEX.md`: LIT-379 (Kolomoitsev–Lomako), LIT-482 (Kuznetsova), LIT-484 (Pimenova) read for priority.
- `git show origin/codex/padua-argmax-bridge-20261105:` (results file, `G01-all-degrees.md`, `C01-effective-argmax.md`): read to date the PR #27 note. *Corrected 2026-11-12 (independent check M1):* that branch claims both the all-n argmax and the sharp corner expansion with the −1/N term (its results file L11–13; `H-sharp-corner-expansion.md`), and its manuscript applies it to Λ_n. It also uses PD-T271 as a dependency.

Search terms: "Lebesgue constant", "three-term", "asymptotic", "corner value", "argmax", "Lambda_c", "Λ(Pad", "b log N", "max(32", "T271", "exp(10^12)".

## Shortlist and what each says

| Entry | What it says | Relation to C0 |
|---|---|---|
| IDEA-206 (`state/IDEAS.md` L504) | Lebesgue theory of checkerboard (Padua-type) interpolation: umbrella project. A1 (PD-T101) closed; finite global argmax 2..16 and eventual equality (PD-T209, T181, T214, T229, inherited T162/166/169/174/177) PROVED; threshold non-effective; PD-T099 and the full PD-T098 expansion OPEN | Parent. C0 combines its PROVED pieces; it adds no open obligation and does not touch PD-T098/T099 |
| IDEA-305 (L841) | Uniform phase/gain/defect assembly for the central envelope (PD-T189–192) | Mechanism behind the localization used by PD-T229 through its descendants; not used directly |
| IDEA-320 (L871) | Global-maximum-only finite certifier; retained in tested finite scope, exact n = 2, 8–16 plus inherited 3–7 | Mechanism behind PD-T246; implemented natively as IDEA-343/344 (PD-T246 canonical) |
| IDEA-326 (L877) | Defect domination without raw-profile convergence; qualitative localization established, effective global entry OPEN | Source of the non-effectiveness of N_* |
| IDEA-358 (L933) | Parity-free corner constant, explicit remainder (PD-T269/270/271); sharp −1/N term deferred | Source of (ii) for the corner value; C0 transfers it to the maximum via (i) |
| IDEA-336, IDEA-454 to 457 (L901, L1012–1015) | Effective-threshold attempts: IDEA-336 deferred/OPEN; IDEA-454 certifier OPEN; later phase-2 theorems | Would make N_* effective; none does; not dependencies |
| PD-T098 / PD-T099 rows | Sharp expansion and all-n argmax, both OPEN | C0 restates neither. It is a different statement: eventual-or-finite equality plus the constant-term expansion |

## Differences from the closest entries

- Closest statement of the expansion: PD-T271, for Λ_c(n) only (the corner value, not the maximum over the square). C0 adds the identification Λ_c(n) = max λ_n from (i) on the stated n-set.
- Closest statement of the identification: PD-T246 (2..32) and PD-T229 (n ≥ N_*). They say nothing about the expansion.
- C0 does not close PD-T099 (the 33 ≤ n < N_* gap stays open) and does not touch PD-T098's sharp form.

## Candidates

None generated (no considered, failed, deferred or rejected candidate to preserve). If the orchestrator wishes to register C0 as a distinct IDEA row, the honest label is "assembly variant, no new mechanism", closest IDEA-206/358/320.

## Literature note

Only the leading term of the Padua Lebesgue constant is published (Kolomoitsev–Lomako 2021, LIT-379; Kuznetsova 1995, LIT-482); see the priority wording in the theory file, taken from `p1-comparison.md`. That search was documented but not exhaustive.
