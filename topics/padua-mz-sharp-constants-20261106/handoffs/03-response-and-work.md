# Handoff 03 — padua-mz-sharp-constants-20261106 — response to audit-01 and closing development

- Status: done in 2429e750cedb18b0a7903e7ed10dd3296a181204
- Previous handoff: [02-audit.md](02-audit.md), done in ed5acba02fa30eba7ca6c22b2e41b19c86792ba7

- Next agent / model / effort: Codex coordinator, `gpt-6-astra` high. Allocate:
  - response record edits to `gpt-6.1-sol` medium;
  - P1 and P3 mathematics to `gpt-6.1-sol` xhigh;
  - P2 and the P1/P4 interval-arithmetic code to `gpt-6.1-sol` medium;
  - supplementary checks to a distinct `gpt-6-astra` high.

  Record actual models.
- Role: developer and topic orchestrator
- Branch: `codex/padua-mz-sharp-constants-20261106`
- Input head SHA: `ed5acba02fa30eba7ca6c22b2e41b19c86792ba7` (the audit-01 output commit; the commit that publishes this handoff comes later)
- Main / base: `76ba4214b100c86a44941f5e9a662ce9ce48efb8`
- Stage: WORK
- Written by / date: Claude, claude-opus-5-5 (xhigh) · 2026-11-06

## Task

Read the rules at the branch head and record the SHA. Fetch main and the topic head first; merge main only if it has moved, and never rewrite history. Then carry out parts R and D. AC instructed this continuation: "If you see some promising ways to close remaining open items, write a handoff and set the branch to work, codex will continue". The development in part D is therefore authorized.

### R — response to audit-01 (do first; one commit)

Write `response-01.md` answering every finding A1–A13 of [audit-01](../audit-01.md): fixed (file and commit), rejected (with an evidence-based reason), or explicitly unresolved.

- **A1.** Disclose in `report.md`, `gates.md` (as a dated K2 interpretation addendum below the unchanged outcome), `theory/S1-model.md`, `ideas/S1.md`, `attempts/S1.md`, `manuscript-insert.md` and the results file that the K1 intercept 13.0611 exceeds the PROVED bound π⁴/8 = 12.1761.
  - The K2 KILL_MODEL is retained as the registered operational outcome, but it carries no evidence against equality.
  - Replace "operationally rejected" with the IDEA disposition `deferred`, with the resume condition stated in audit-01 A1.
  - Do not create a PD-N. Do not change K1/K2 thresholds, windows or receipts.
- **A2.** Add a dated K4 interpretation addendum in `gates.md`, `report.md`, S3-03 "Checks" and `ideas/S3-corner-operator.md`. It says that (3)/(4) predict nothing about finite-window slopes and cites the audit diagnostic (`audit-01-support/S3/big.json`, MEASURED). The K4 outcome stays unchanged.
- **A3.** Do not choose the registry mapping; AC decides it. Record both options and the auditor's recommendation in the log and results file. Revisit after part D.
- **A4.** Create compact durable MEASURED records, one per direction or as justified in the response. They cover the K1/K3 fits, the Λ_edge J512 proxy, the B_K proxies, the 16 Padua minima and their slopes, and the normalization diagnostic, each with scope, commands, receipts and limitations. Link them from `report.md`.
- **A5–A12.** Make the listed text, citation, ID-format, idea-template, cold-storage-format and preregistration-blob edits. These change no statement, proof, quantifier, status or result. For A9, screen the named sources at search or abstract level only, record coverage limits, and make no priority claim.
- **A13.** Exclude `audit-01-support/` from the `code/evidence_manifest.py` scope (or inventory it deliberately), regenerate the manifest intentionally, and record why.

### D — development aimed at closing open items

Run the novelty gate for each new mechanism and give each candidate a record (`templates/IDEA.md`). Register every numerical prediction and protocol in `gates.md` and publish it before computing. Keep the existing per-run (6 h) and cumulative (48 CPU-h) ceilings, at most 2 concurrent heavy processes, and no Syvert. Use up to 6 rounds per direction, and stop a direction after 2 consecutive no-progress rounds.

1. **P1, PD-T381 values (priority 1).**
   - **(i) Kernel identification.** Prove that the norm limit B of S3-03 equals the integral operator on H=L²(D, ab da db) with kernel

         B(a,b;a',b') = −8[S_alt(a,a')S_all(b,b') + S_all(a,a')S_alt(b,b')],
         S_all(a,a') = 2K(k̃)/(π²(a+a')),  k̃² = 4aa'/(a+a')²,
         S_alt(a,a') = 2K(k)/(π²√(aa'))·1[a+a'>1],  k² = ((a+a')²−1)/(4aa').

     Route: the j+k-even split ½[1+(−1)^(j+k)], Gegenbauer's product formula and the Schlömilch series in audit-01 P1. The obligation is to justify the conditionally convergent exchange under the product truncation (1+j)(1+k) ≤ K. For example, prove weak convergence on a dense set of smooth test functions plus boundedness of the closed-form operator; uniqueness of the norm limit then identifies them.
   - **(ii) Consequences.** If (i) holds, prove the consequences of the nonpositive kernel: c_minus = −‖B‖, and a positive, simple ground state (irreducibility).
   - **(iii) Certified enclosures.** Enclose c_minus by a Rayleigh lower bound on ‖B‖ (positive trial) and a Schur-test upper bound sup(−Bh)/h. Enclose c_plus with a Galerkin method plus a rigorous residual or Temple/Lehmann bound, or a kernel-regularity tail bound. Use exact or interval arithmetic with committed checker code and an independent rerun.
   - **Target.** At least 3 certified digits, honestly reported if fewer are reached. A certified enclosure would be a computer-assisted PROVED result only under WORKFLOW's computer-proof requirements; otherwise it is MEASURED.
2. **P2, finite-m mechanism behind K4 (priority 1, cheap).**
   - First register the predictions in audit-01 P2 (mode-2 branch, branch-difference rate 0.038±0.006 per unit log R, window slopes within 0.006 of b₂ ≈ −0.0955, and the stated kill criteria). Register b₂ from B_K together with its K-stability.
   - Then run the matrix-free diagnostic (`audit-01-support/S3/lm_spectra2.py` as a starting point; re-implement or review it before reuse) at m=1600, 1601, 3000 and 3001. Estimated cost: 1–2 CPU-h.
   - Record the outcome as MEASURED. It never revises K4.
   - **Optional theorem target:** the two-term law λ_±(m) = log R·c_± + d_± + o(1), with an explicit O(1) corner operator.
3. **P3, the reverse CC bound for PD-T020 (priority 2, hard).**
   - Attempt liminf (log N)²λ_min ≥ π⁴/8 by the operator-splitting route in audit-01 P3: global cot kernel; e-part O(√L); P → discrete log-Hardy via the Volterra lemma; E = O(1). The decisive obligation is a signed weighted Plancherel/sinc estimate on dyadic blocks; PD-N005 shows the absolute majorant fails.
   - Track constants, and handle endpoints, microscopic cells and k ≈ N/2.
   - If it succeeds, PD-T020's limit is π⁴/8 on both parities. If it fails, record the exact obstruction scoped to this route.
   - Any new numerics need a fresh preregistered protocol (for example structured-solver rows to N=10⁶–10⁷ with the ansatz fixed in advance). They do not revise K1/K2.
4. **P4, certified bracket for Λ_edge (priority 3, optional).**
   - Interval-arithmetic Rayleigh lower bound Λ_edge ≥ 1.0044369.
   - An upper bound by a sharper certificate: graded mesh, Toeplitz-plus-Hankel FFT products with a Lehmann/Temple bound, or a dual variational principle. Report the digits actually certified.

Theory results go in new theory files with explicit statuses and split rules. Leave PD-T020, PD-T027 and PD-T381 at their current registry status. Update `report.md`, LOG, the results file and the PR31 WORK section.

## Read first

`AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md`; this handoff; `audit-01.md` and the novelty report `audit-01-support/records/novelty-records-findings.md`; `LOG.md`; `gates.md`; `theory/S1-sharp-one-sided.md`, `theory/S2-finite-certificate.md`, `theory/S3-corner-operator-limit.md`, `theory/S3-full-form-log-model.md`; and the audit support scripts relevant to each direction.

## Scope limits

- Do not edit `audit-01.md` or `audit-01-support/`, except the manifest-scope handling of A13, which happens in the manifest code.
- Do not change any registered gate criterion, window, threshold, outcome or receipt. Interpretation addenda are dated and placed below the original text.
- Do not change any accepted PROVED statement or proof, except the A5–A7 wording and citation edits, which must leave statements and quantifiers intact. A substantive change returns that item to AUDIT.
- No final IDs, reservations, shared registries (`PROOF_STATUS.md`, `state/IDEAS.md`, `state/CURRENT.md`, `ID_CROSSWALK.md`, `RESULTS.md`), manuscript, main, tags, workflows or settings. No merge and no force-push. Only AC merges.
- Do not launch an upper Padua eigenvalue campaign or retry the capped m800 upper pilot.

## Acceptance and outputs

- **Outputs:**
  - `response-01.md` covering A1–A13;
  - the record edits and new MEASURED records;
  - for each of P1–P4 attempted: novelty gate, idea record, registration, theory or attempt files with statuses, receipts and independent checks;
  - updated LOG, results file and PR31 body.
- **Commit order:** commit the outputs first. Then, in a following commit, set this handoff's status to `done in <output-commit-sha>` and add handoff 04. Handoff 04 asks Claude for a focused audit of the material changes only: the new theory, the certified computations, the MEASURED records, and any changed interpretation or disposition. If part R alone was completed with only MINOR edits, handoff 04 may instead go to PR preparation, which awaits AC's A3 decision.
- **Done when:** every finding is answered; P1 and P2 are attempted to a recorded outcome; P3 and P4 are attempted or explicitly deferred with reasons; and exactly one open handoff remains.
