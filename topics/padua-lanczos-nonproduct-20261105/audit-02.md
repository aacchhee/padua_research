# Audit 02 — padua-lanczos-nonproduct-20261105 — focused re-audit of the A3 correction

- **Auditor:** Claude, independent of the Codex developer, configured `claude-opus-5-5`, high effort, as handoff 05 specifies. This is a narrow focused re-audit, so no subagents were used.
- **Date:** 2026-11-06.
- **Rules read:** `68bf172e26a4eac762d082601064f6f8f00adfa0`. AGENTS.md, WORKFLOW and the role files there are unchanged since `be9a831`.
- **Input:** handoff 05 input head `84f3d50ae265a0bc510cb6bb232fbc23f71f1b40`. The branch head `68bf172` differs from it only in handoffs 04 and 05.
- **Material diff:** `1f80951..3b0a990`.
- **Mechanical diffs:** `3b0a990..04ba07b` and `04ba07b..84f3d50`.
- **Verdict:** **ACCEPT; stage PR.** No BLOCKING or MAJOR finding, one MINOR and one NOTE. No further audit round is needed.

## Scope

This audit covers the following:
- **A3 correction:** the material statement correction (audit 01 A3) in `theory/p1-continuous-creator-probe.md` and `ideas/P1.md`.
- **Response 01:** `response-01.md` and its dispositions, reviewed by diff. The question is whether any change beyond A3 is material.
- **A2 record:** a check that the completed record claims nothing it could not verify.

Not reopened: the accepted P3/P4/P5 proofs, the P1/P2 admissions, the reflection method, the P6 outcomes, the three INCONCLUSIVE N2 verdicts, and AC's Q1–Q3 decisions.

**Novelty-read exception.** A3 qualifies an existing MEASURED finite identity. It adds no candidate, mechanism, novelty or negative claim. So the full `state/IDEAS.md` reread is omitted; audit 01 completed that read for this batch. The relevant P1 records and audit 01 were read.

## Checks actually performed

1. **A3 diff.**
   - Reviewed `git diff 1f80951 3b0a990` for the two A3 files. Every statement of g_j = 1/binom(2j,j), and of the displayed chain, now says "under BJ", including the alias, the status table, the sources and the N3 paragraph.
   - MEASURED status and degree-eight scope are retained, and a dated History line records the correction.
   - A topic-wide search for the chain, "central-binomial" and "Legendre" found no remaining unqualified use. The results file says "checked under BJ only".
2. **Targeted rerun.**
   - The committed `code/p1_moment_probe.py` has sha256 `877b77c0…aab5ff0`, which equals the `source_sha256` in `evidence/p1-moment-probe.json`.
   - Lines 153–161 use only `records["BJ"]`.
   - The auditor made a scratch copy that computes the same final-degree chain for every rule. It is outside Git, sha256 `4975187a…b816fa`, and ran with `python3 -I -B probe_rules.py --output <scratch>/out.json` in 1.17 s. All the original assertions still pass. The results:
     - BJ gives `1, 1/2, 1/6, 1/20, 1/70, 1/252, 1/924, 1/3432, 1/12870`, equal to 1/binom(2j,j).
     - Mirror and alternating each give `1, 0, 0, 0, 0, 0, 0, 0, 0`.

   The correction is therefore exact: the identity is BJ-only. The committed evidence is unchanged.
3. **Mechanical diff review.** Read the full theory diff of `3b0a990..84f3d50`, and scanned the LOG, report, gates, ideas, attempts, results and novelty-gate diffs. All changes are framing, scope wording, links, namespace prefixes, dispositions, chronology and status-link updates. In particular:
   - **P3-03 title and Scope** carry the required wording: "non-affine-product measures moment-equivalent to SH_n through degree 2n+1, with an n-dependent weight mode". The η-independence of the Gram matrices, basis, creators, pivots, source scales and frozen-response map is stated correctly. The statement that the represented weighted vectors vary with η is also correct. The theorem Statement and proof are unchanged apart from spacing.
   - **Threshold sentence.** The new sentence (bound (3) is below 1 for 2≤n≤17 and above 1 for n≥18; strict ordering is certified for n≥18) follows directly from (3). The bound increases from n=5 onward, so it is a corollary statement, not a new claim requiring proof review.
   - **`nonproduct-definition.md` part 2** now says "strictly positive weight at every node". This matches the record's own Definitions line and proof, so it is a clarification and not a change in what was proved.
   - **Split fields and the P2-03 parts table** are consistent with the WORKFLOW status rules. No status was upgraded.
   - **P5 checker:** only two comment lines were added (diff reviewed).
   - **Unchanged files:** no file under `evidence/`, `inventory/`, `audit-01.md`, `audit-01-checks/`, `state/`, `PROOF_STATUS.md`, `ID_CROSSWALK.md`, `RESULTS.md`, `literature/`, the rules or `.github/` changed between `1f80951` and `84f3d50` (`git diff --stat` is empty).
   - `git diff --check 1f80951 HEAD` passes.
4. **A2 record.** The canonical LOG paragraph now addresses (a)–(d). It explicitly marks as unpreserved, rather than claiming to have verified:
   - the exact proposal time;
   - the per-entry list of unread entries;
   - the formula and range identity with the unpreserved proposal.

   It records AC's Q1 acceptance. The P3 IDEA carries the permanent qualifier. Nothing is claimed as verified that could not be.

No other execution was performed.

## Findings

- **BLOCKING:** none.
- **MAJOR:** none.
- **MINOR B1 — wording at `theory/p3-03-uniform-capacity-radius.md:208`.** "At |eta|=1 some weights vanish, leaving the admitted positive full-support family" can be misread as "remaining in" the family. Suggested wording: "so |eta|=1 lies outside the admitted positive full-support family". This is wording only. Fix it at PR preparation; the readiness diff confirms it. It is not a new audit round.
- **NOTE B2.** The A2 historical-precision limits (no message timestamp, no per-entry list, no pinned original proposal) are permanent. AC accepted Q1 with them disclosed, and no action is needed.

## Disposition

- **A3 is accepted.** The single material change is correct and confirmed by an independent targeted rerun.
- **Response 01's other dispositions** are accepted as non-material record fixes that satisfy audit 01's MINOR findings and AC's Q1–Q3 decisions. They need no further audit round.
- **Next stage:** PR preparation:
  - reserve fresh final-ID ranges by the WORKFLOW procedure;
  - assign final IDs;
  - edit the shared registries directly;
  - fix B1.

  Then comes the single Claude readiness check: the reviewed registry `git diff` plus a reservation refresh against current main, all open PRs and retired reservations. Readiness is not a further substantive audit, unless preparation makes a material change beyond the audited scope.

## Remaining uncertainty

- The rerun covers the executed degree-eight scope only, as the record states.
- The mechanical diff was reviewed for materiality, and the accepted mathematics was not re-derived. Audit 01 remains the substantive record.

Only AC merges.
