# Claude audit-03 — focused recheck of response-02 (draft PR31)

- **Decision: ACCEPTED. Stage → PR.**
  - B2 is accepted: the new durable record `theory/P4-denominator-closed-form.md` (PD-T?mz-sharp-codex-P4-02) is PROVED at its stated scope.
  - B1 and C1–C4 are confirmed fixed by diff.
  - No BLOCKING, MAJOR or open MINOR finding remains.
  - Two stale process sentences were fixed in place under WORKFLOW's third-round rule (F1, F2 below), in a separate commit.
- **Audited input:** `99fd6c0e7a0d8912e087c81bfd9bbd6654ca6330` (handoff 06). Head at audit start: `aed39625b4fbe846b581d70088ff45da865d3e31`, which is handoff-only relative to the input.
- **Rules and base:** rules read at `aed3962` (`AGENTS.md`, `agents/WORKFLOW.md`, `agents/claude/CLAUDE_ROLES.md`), unchanged from main. Main `76ba4214b100c86a44941f5e9a662ce9ce48efb8`, refetched and unchanged.
- **Auditor:** Claude, configured `claude-opus-5-5`, high effort, as handoff 06 requests: a mathematical audit of one bounded derivation. No serving-model receipt is exposed. No subagents were used. I am distinct from the Codex developer and the Astra checker.
- **Scope:** a focused recheck, not a re-audit of P1–P4. Novelty read: the new record makes an accepted derivation durable and adds no mechanism, candidate or priority claim. So, as handoff 06 states, the full IDEAS read is not repeated. `state/IDEAS.md` is unchanged since the full read for audit-01. I read the IDEA-466 additions for C3.

## Coverage

- **Read in full:** handoff 06; `response-02.md` (`3546f7df…`); `theory/P4-denominator-closed-form.md` (`76a5b30d…`); `independent-checks-P4-denominator.md` (`579271c0…`, input only).
- **Response diff:** `git diff f3c14d7 99fd6c0` for every changed file. That covers the five B1 records, `evidence_manifest.py`, the S1/S2 history and label edits, the P3, P4 and P1 certificate edits, `novelty-gate-P4.md`, the P4/P1 idea records, `manuscript-insert.md`, the report and results file, `integrity-checks.md` and `resume-05-inputs.json`.

## Independent reconstruction of B2 (by hand)

1. **Removable points and convergence.**
   - sin(a_j+z) = s_j sin z, so F_j(a_j+z) = 2a²(sin z/z)/[(a+z)(2a+z)] → 1.
   - F_j(0) = −2s_j, and F_j(a_k) = 0 for k≠j.
   - t F_iF_j = O(t) at 0 and O(t⁻⁵) at ∞, so every C_ij converges absolutely.
2. **I(a) at a common cutoff.**
   - 1/(t(t²−a²)) = a⁻²[t/(t²−a²) − 1/t] and t/(t²−a²) = ½[1/(t−a) + 1/(t+a)].
   - Translation gives H(R−a)−H(a) and H(R+a)−H(a). The negative half-range contributes −H(a) because sin²v/v is odd.
   - |H(R±a)−H(R)| ≤ log(R/(R−a)) and log((R+a)/R), so I(a) = −H(a)/a² = −Cin(2a)/(2a²). Divergent pieces are combined only at finite R.
3. **Off-diagonal entries.** The resolvent identity [1/(t²−a²) − 1/(t²−b²)]/(a²−b²) applies to absolutely convergent pieces. It gives C_ij = 2s_is_j(a²Cin(2b) − b²Cin(2a))/(a²−b²), symmetric in i and j.
4. **K(a).**
   - Integration by parts with v = −1/(2(t²−a²)): the boundary term −sin²t/(2(t²−a²)) vanishes at 0, at a±ε (it is O(ε)) and at ∞.
   - The remaining integrand sin 2t/(2(t²−a²)) is regular at a, since sin 2a = 0.
   - Translation gives 2Si(2a) + Si(2(R−a)) − Si(2(R+a)), and the last difference is ≤ log((R+a)/(R−a)) → 0. So K(a) = Si(2a)/(2a).
5. **Diagonal entries.**
   - I checked the partial-fraction identity 1/(t(t²−a²)²) = a⁻⁴[1/t − t/(t²−a²)] + a⁻²t/(t²−a²)² by clearing denominators.
   - The bracket equals −a²/(t(t²−a²)), so C_jj = 4a²(K−I) = 2[a Si(2a) + Cin(2a)].
   - No off-diagonal limit is taken.
6. **Finite quadratic form.** This follows by expanding a finite sum under absolutely convergent integrals.
7. **Application.** P4 uses exactly these entries; S2's registered formulas are unchanged and now cite the proof. d_j = γ + log(2a_j) − Ci(2a_j) = Cin(2a_j) is the standard identity.

**Floating corroboration** ([denominator_check.py](audit-03-support/denominator_check.py), [output](audit-03-support/denominator_check.out); MEASURED):
- mpmath (30 digits) quadrature of C_ij for (i,j) = (1,1), (1,2), (2,3), (3,3), (1,5), (4,7) matches the closed forms.
- Every difference is within the crude truncation-tail estimate: from 2e-11 at (1,1) to 1.5e-8 at (4,7).
- Audit-02 had already matched the whole J512 denominator by closed-form-free quadrature to 1.4e-13.

## Diff confirmation of B1 and C1–C4

- **B1: fixed.**
  - Dated "postdictive" addenda appear in `theory/P2-measurements.md`, `ideas/P2.md`, `ideas/P2-protocol.md`, `report.md` and the results file.
  - They list the six pre-existing Q_min endpoints (m 1400/1401, 1800/1801, 3000/3001, committed at `5110954` before `d03e74d`) and cite the audit diagnostic. Only the mode-2 weight, L-distance and branch rate are prospective.
  - Original protocol text, thresholds, receipts, PASS_FINITE_TEST and K4 are unchanged; `evidence/` is byte-unchanged.
- **C1: fixed.**
  - `evidence_manifest.py` now excludes any `audit-*-support` path component via `fnmatchcase`.
  - `evidence_manifest.py --checks` at `aed3962` exits 0: 107 Markdown documents, 431 local links, 0 missing.
  - `audit-01.md`, `audit-02.md`, both support trees, `evidence/` and earlier handoff bodies are byte-unchanged since `f3c14d7`. The only code change is the manifest code, and `resume-05-inputs.json` is a new pinned input receipt.
- **C2: fixed.**
  - History entries in `ideas/S1.md` and `theory/S1-model.md` quote "operationally rejected".
  - `S2-endpoint-model.md` now carries "registered definition/prediction; proved via S2-05/S2-06".
  - The stale P3 status, report and manuscript-proposal text is updated.
  - The results file distinguishes PD-T020's preparation-stage application from AC's A3 decision on PD-T027/PD-T381, and adds "no useful digits" for P1.
- **C3: fixed.** IDEA-466 is added to `novelty-gate-P4.md`, `ideas/P4-rayleigh.md` and `ideas/P1-numeric-protocol.md`. The separation is falsifiable: it rests on the certified object and the reduction, not on the dyadic arithmetic. P1/P3 gate provenance is linked, and the verdicts are unchanged.
- **C4: fixed by documentation, as permitted.**
  - The P1 prose hashes are labelled historical (`c1e6e59` blobs).
  - The P2 validation and overlap requirements are documented as procedural prerequisites to release.
  - The P3 wording now reads 0<z<2π, θ∈[0,π/2] ⇔ x∈[0,1], and dx = sin θ dθ ≤ dθ.
  - No result-bearing code or receipt changed.

No edit changed an accepted statement, quantifier, proof step, threshold, receipt or status. Outside the topic, only the topic results file differs from main. No shared registry, final ID, reservation or manuscript proper was touched.

## Commands actually executed

- `python topics/padua-mz-sharp-constants-20261106/code/evidence_manifest.py --checks` at `aed3962`: exit 0, with the counts above.
- `git diff` and `git diff --stat` checks listed in the previous section.
- `python3 denominator_check.py` (Python 3.13.18, mpmath 1.4.1), about 1 CPU-min.

No numerical producer was rerun: result-bearing code, inputs and receipts are unchanged since audit-02.

## In-place MINOR fixes (third-round rule; separate commit)

- **F1.** `theory/P4-denominator-closed-form.md`, the "Checks" and "Open items" paragraphs: stale process text said the supplementary review and the Claude recheck were still to come. I replaced it with dated pointers to `independent-checks-P4-denominator.md` and this audit. The statement, proof and status are unchanged.
- **F2.** `report.md:127`, the stale "next focused Claude recheck" sentence: I added a dated pointer to this audit's acceptance and the PR-preparation stage.

## NOTES

- **N1.** `S2-endpoint-model.md` renamed its registration heading in place, from "to check after registration" to "registered for checking after publication", and recorded this in History. The formulas are unchanged, so this needs no action, though a dated addendum would have been cleaner.
- **N2.** For PR preparation:
  - PD-T020 may become PROVED via P3-03 + S1-02, to be verified at readiness.
  - The mapping of PD-T027/PD-T381 needs AC's A3 ruling; audit-02 N7 notes that P1/P4 give no decimal values.
  - The A10 shared-registry consolidation remains outstanding: IDEA-054/071/386/466/469/470, MZ obstruction memory `state/IDEAS.md:406`, PD-T027 notes 938/942, and the S3-kernel provisional suffix.

## Residual uncertainty

- One auditor (Opus 5.5, high) checked the B2 derivation, with floating corroboration. The distinct Astra check agrees.
- All other P1–P4 results rest on audit-02.
