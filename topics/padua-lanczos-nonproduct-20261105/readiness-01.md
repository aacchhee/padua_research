# Readiness 01 — padua-lanczos-nonproduct-20261105 — registry diff and reservation refresh

- **Checker:** Claude, configured `claude-opus-5-5`, high effort, as handoff 07 specifies. One independent Claude Opus (high) subagent reviewed the IDEAS, crosswalk, CURRENT and RESULTS diff, the topic-record diff, the six new OPEN records and the links. The orchestrator reviewed the PROOF_STATUS and LIT rows and ran the reservation refresh.
- **Date:** 2026-11-06.
- **Rules read:** `54b01f10c2eefaba6115e021276df5d45193bdab`. AGENTS.md, WORKFLOW and the role files there are unchanged since `be9a831`.
- **Input:**
  - preparation output `418b8166121d3717c4d1916ae6c4619953cb4573`;
  - reservation checkpoint `6b313567702b0ec465330e2ca4b8186d8be210a4`;
  - branch head at check `54b01f1`, which adds only handoffs 06 and 07.
- **Scope:** this is the single readiness check (WORKFLOW, Work cycle step 5): a reviewed `git diff` of the shared registries plus a reservation refresh. It is not a further substantive audit.
  - Mechanical registration adds no candidate, mechanism or novelty claim, so the full `state/IDEAS.md` reread is omitted; audit 01 did it.
  - Accepted mathematics, finite outcomes and AC's decisions are not reopened.
- **Verdict:** **READY.**
  - No BLOCKING, MAJOR or material finding.
  - Three MINOR findings, fixed in place by the auditor in separate commit `0f2d44e`. This is the topic's third review round (audit 01, audit 02, readiness 01), so in-place fixes are allowed; they are listed below.

## Registry diff (`be9a831..418b816`)

Reviewed: `PROOF_STATUS.md`, `state/IDEAS.md`, `literature/INDEX.md`, `ID_CROSSWALK.md`, `state/CURRENT.md` and `RESULTS.md`.

- **Additions only.** No pre-existing byte changed (numstat deletions = 0). `RESULTS.md` gains only this topic's section, which matches `results/padua-lanczos-nonproduct-20261105.md` apart from relative-path prefixes.
- **PROOF_STATUS, assigned results:**
  - PD-T472–488: 13 PROVED and 4 MEASURED records at their audited scopes.
  - PD-T473 says the chain holds "under BJ only".
  - PD-T480 carries the title AC accepted for P3, the η-independence caveat and "certified strict ordering for n≥18".
  - PD-T486 states the exact two-sided Padua bound for m≥2, 1≤s<m.
  - PD-T487/488 are finite-only, with all three screens INCONCLUSIVE.
- **PROOF_STATUS, new OPEN homes:** PD-T489–494 re-home targets already stated in handoff 01, the ideas records and audit 01's accepted scope.
  - Each is OPEN, and each says its supporting lemmas do not make it PARTIAL.
  - None assigns an exponent, parameter point, sufficient condition or theorem.
  - The range α,β,γ>−1 in PD-T489 is the standard admissible domain, not a claim.
- **PROOF_STATUS, PD-N178:** PROVED, scoped to covariance-only absolute capacity. Only IDEA-581 is REJECTED: refuted, linked to PD-N178, and the original ratio criterion IDEA-578 stays OPEN.
- **IDEA-570–584** match the provisional records for disposition, scope, predecessors and resume conditions, using only allowed disposition words:
  - IDEA-576 carries the permanent timing qualifier with `2ebea9a`/`6988024` and "AC decision 2026-11-06: accepted".
  - IDEA-577 (the n-independent perturbation) is deferred, has no proof status and is not a PR precondition.
  - IDEA-575 (D65) is deferred with a resume condition.
  - The unnumbered subroute aliases are retained.
  - No administrative PD-N exists.
- **LIT-630** is a bounded developer source-reading record, labelled LITERATURE. It is not local verification, not a priority clearance, and not a duplicate of LIT-292 Chapter 3.
- **ID_CROSSWALK** maps every full provisional ID used in the topic, checked by git-grep at both commits. It disambiguates P4-01/P4-04, P2-03/P2-04 and the lowercase p5 theory records from the uppercase P5 candidates.
- **No process stage in shared entries.** The only match for a process word is a resume condition in IDEA-580, which is allowed.
- **Topic diff `72cbce7..418b816`:**
  - Existing records change only IDs, provisional-alias lines, `<a id>` anchors preserving the old headings, one link, allocation-state lines and audit 02 B1.
  - **B1 is fixed:** `p3-03` now says "so |eta|=1 lies outside the admitted positive full-support family".
  - No statement, assumption, quantifier, status or evidence changed.
  - Code, evidence, inventory, audit-01-checks, audits 01/02, response 01, manifests, rules, templates and `.github/` are byte-unchanged (`git diff --stat` is empty).
  - `git diff --check be9a831 418b816` is clean.
- **Links.** Of 189 relative links added to the shared registries, 0 are missing and 0 anchors are unresolved; anchors were checked with a GitHub-slug approximation. One topic-LOG link to handoff 07 resolves only at `54b01f1`, which is expected.

## Reservation refresh

The refresh was executed at check time:
- The GitHub all-state PR listing returned **29 PRs**: open #27, #28 and #30, and 26 closed and merged. No PR is closed without merging, so no unrecorded retired reservation needs recovery.
- `git fetch` followed by `git ls-remote` confirmed these heads:

| Source | Head |
|---|---|
| main | `be9a8318150204711d5446d2ea26284cf1ed0819` (unchanged since the base) |
| PR27 `codex/padua-argmax-bridge-20261105` | `8dc1521cf68f7780bd10e02495f6f71a639c03c6` (as in the ledger's prepublication refresh) |
| PR28 `codex/nn-mop-stability-20261105` | `4e87fc0a771fc13c6d5791f0f4c2e746e4eb9a71` (unchanged) |
| PR30 (own) | `54b01f10c2eefaba6115e021276df5d45193bdab` |

**Independent scan.** The auditor wrote its own scanner (`scan_ids.py`, kept in session scratch and not committed) and ran it over the complete bytes of `PROOF_STATUS.md`, `state/IDEAS.md`, `literature/INDEX.md`, `ID_CROSSWALK.md` and every `*/ALLOCATIONS.md` at each head (15 or 16 files per head). The scanner:
- matches qualified three-digit tokens, ranges and abbreviated ledger ranges (T…, N…);
- excludes foreign four-digit LIT aliases.

**Maxima.**
- main, PR27 and PR28 each give **PD-T471, PD-N177, IDEA-569, LIT-629**.
- PR30 gives T501, N180, IDEA-589 and LIT-632, its own range ends.

**Collision check.**
- `git grep` for T472–501, N178–180, IDEA-570–589 and LIT-630–632 at main, PR27 and PR28 finds only PR28's own range endpoint "PD-T432–PD-T471". There is no overlap.
- The registry additions introduce exactly PD-T472–494, PD-N178, IDEA-570–584 and LIT-630; every other ID they cite was already accepted (PD-T033/039/040/136/324/338, PD-N012/063, IDEA-083/137/246/248/415).

**Priority and gaps.**
- Own permanent reservations: T472–501 (30), N178–180 (3), IDEA-570–589 (20), LIT-630–632 (3).
- Their priority is the first publication, `6b31356`.
- Unused T495–501, N179–180, IDEA-585–589 and LIT-631–632 remain permanent gaps.

**Before merge.** If main or a peer ledger changes before AC merges, this union check must be repeated, as WORKFLOW requires.

## Auditor MINOR fixes (commit `0f2d44e`, separate from this report)

1. **R1, wrong attribution in a results bullet.** `RESULTS.md` (topic section) and `results/padua-lanczos-nonproduct-20261105.md`: the "PROVED, PD-T472/474/477/481" bullet included "high-mode weight" admissions, which belong to PD-T478 and are covered by the PD-T478–480 bullet. The bullet now reads "triangle, continuous radial disk and D36/D65 rational ring admissions and the affine-product definition". No claim changed.
2. **R2, broken table.** In `theory/p3-fixed-perturbation-target.md`, the "Status by part" row ran over four physical lines and broke the Markdown table. It is now joined onto one line, with the text unchanged.
3. **R3, stale process text.** Four places were brought up to date:
   - `LOG.md` header: "Provisional IDs only" is replaced by the final ID ranges with an ALLOCATIONS link.
   - `ideas/P2.md` header: "No final IDs allocated" is replaced by a crosswalk link.
   - `ideas/P2.md` (D65 entry): "Implementation check is next" now states, in the past tense, that the check was still to come at that point.
   - `report.md`: "readiness … check is next" now links this record.

The developer may dispute any of these; disputes go to AC.

## NOTEs

- The six OPEN records introduce new provisional aliases (P1-03, P2-05, P3-04, P4-05, p5-03, p5-04), all mapped in the crosswalk.
- The pre-existing short alias `IDEA?P2-02` in `novelty-gate-P2.md` is unambiguous (→ IDEA-574).
- IDEA-576 states its permanent qualifier in the registry row, as handoff 07 requires.

## Decision requested from AC

Merge PR #30 by squash, at AC's discretion.
- Agent preparation is complete: the audits are accepted and the registry diff and reservations are ready.
- No final claim is upgraded by this readiness check.
- If main or a peer ledger (PR27/PR28) changes before the merge, refresh the reservation union first.

Only AC merges.
