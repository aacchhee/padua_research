# Response to audit-01 (Codex, gpt-6-astra high, 2026-11-14)

Responder: Claude, claude-opus-5-5 (configured xhigh; effort not exposed), orchestrator. Rules read at `c0e57a9`, unchanged on the branch. Audit input head `be28d32`; audit output `f9bf997`; response input `303a564`. [audit-01.md](audit-01.md) and its supplementary reports are not edited.

No theorem, assumption, proof, status, bound or evidence item was changed. All changes are wording and metadata (see the last section).

## F1 — MAJOR: present-tense archive claims — **Accepted, fixed**

- **MZ-CC, data and code availability** (`tracks/mz-constants/paper/manuscript.tex`, the paragraph after §9):
  - Old: "…are archived at [Zenodo DOI to be added] … The archive contains … a README lists the files."
  - New: the files are in the public repository at the commit to be fixed at submission. The paragraph then lists what is committed (trial vector, enclosure program, independent exact-rational program, output logs, table script), with exact paths. "An archived copy is planned ([Zenodo DOI to be added])". The archive README sentence is removed.
  - The TeX comment now cites F1.
- **MZ-CC, Appendix C end:**
  - "are in the archive listed in the data availability statement" → "are in the repository named in the data availability statement";
  - "the archived code" → "the published code".
- **MZ-SP, after Prop 8.2:**
  - Old: "The witness data are archived with the deposit".
  - New: "The programs and the small certificate files are in the public repository; the witness coefficient arrays and exact norm files are not (see the data and code availability statement)."
- **MZ-SP, data and code availability:**
  - "archived as [Zenodo DOI to be added]" → "an archived copy is planned ([Zenodo DOI to be added])".
  - The witness sentence now says that the arrays and the exact rational norm files "whose SHA-256 identities are recorded in the committed payload-identity file, are to be included in the planned archive; until then they are not publicly available."
- **READMEs:** both README assurances are reconciled with the text. The MZ-SP README now says plainly:
  - the witness arrays and norm files are not publicly available, are not in Git, have no delivered copy, and were not replayed by the audit;
  - before submission AC must either retrieve the exact package (identities in [report §6.2](report.md)) so its committed checkers can be replayed and it can go into the planned deposit, or decide the publication scope of Prop 8.2.
- **report §6.2** keeps the honest missing-package identities, unchanged.
- **Unresolved, for AC (not invented):** the exact PD-T376 package (arrays and norm files) has not been retrieved, and no replay was done; receipt inspection is not counted as either. The accepted mathematics of PD-T376 is not reopened. No witness was regenerated, and Prop 8.2 is not converted to a measured statement. Until the package is retrieved and replayed, or AC decides the scope, Prop 8.2's public replayability stays an open submission obligation. The PR remains a draft on this point.

## F2 — MAJOR (subreviewer disagreement preserved): trial interval vs true minimum — **Accepted, fixed**

MZ-SP §8.3 item (2):
- Old parenthesis: "(at m=1600 it lies in the interval of Proposition 8.2)".
- New: "(at m=1600 the computed minimum agrees, to the displayed precision, with the certified trial quotient of Proposition 8.2; that proposition gives only an upper bound for the true minimum)".

The measured-only disclaimer of §8.3 and the trial/eigenvalue sentence right after Prop 8.2 are kept. No new eigensolve. The severity disagreement between the subreviewers (MINOR vs MAJOR) is recorded in audit-01 and is not resolved here; the fix satisfies both readings.

## F3 — MINOR: signed supremum — **Accepted, fixed**

MZ-SP, after the proof of Prop 5.3 (carriers):
- Old: "have suprema 1/9 and 1/36".
- New: "have infimum −1/9 and supremum 1/36, respectively, over the parameter domains a+b<1/2 and 2a+b<1/2, approached on their closures".

The normalized bounds are unchanged.

## F4 — MINOR: notation remnants — **Accepted, fixed**

- MZ-CC Appendix C, finite reduction: `(\mathsf M_{ij})_{i,j\le J}` → `_{i,j\le\mathsf J}`.
- MZ-SP (fourth difference): "of h" → "of υ".
- MZ-SP Lemma A.4 proof: `N C_U/m` → `N_{\mathcal Z} C_U/m`, in both places. That is the defined local dimension; the bound is the entrywise bound (eq:gram-diff) times the matrix dimension, as before.
- MZ-SP end of the Thm 6.3 proof: `E_K(m)` → `\mathcal E_K(m)`, the defined symbol.

## F5 — MINOR: stale metadata — **Accepted, fixed**

- `correspondence-cc.md` and `correspondence-sp.md` now open with a status note. The first table is the **historical planning table** of 2026-11-13, kept unchanged. The current mapping is the *Frozen numbering* table at the end of each file plus the README scope tables (frozen number → PD IDs → status → exact scope), with departures listed in the changes logs.
- The provisional records `theory/cc-defect-condition-corollary.md` and `theory/sp-corner-norm-lower.md`:
  - the stale "independent check pending" rows now point to the PASS checks and to the audit reconstruction;
  - "Open items" now says there is no mathematical item left, only the final ID at PR preparation.

  The History sections are unchanged. Earlier handoff bodies and reports are untouched.

## Builds and frozen numbering after the response

`tools/build.sh` at the response commit:
- MZ-CC: 32 pp. (486×720 pt);
- MZ-SP: 50 pp. (A4);
- both: zero warnings, no over/underfull boxes, no undefined references, BibTeX clean.

Every non-equation, non-table label keeps its frozen number: 104/104 CC labels (52 theorem-like) against the freeze build `cc12`, and 56/56 SP labels against `sp5`. No PDF is committed.

## Classification for the readiness check

Wording and metadata only, within stated scopes. Per audit-01 and handoff 06, a diff-based readiness check is proportionate. No focused re-audit is requested, because no theorem, proof, bound, status or evidence changed. The open evidence obligation (F1: the PD-T376 package) is disclosed and remains with AC.
