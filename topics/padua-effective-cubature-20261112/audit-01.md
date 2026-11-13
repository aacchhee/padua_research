# Audit 01 — effective cubature and Lebesgue corollary

Date: 2026-11-13. Role: independent audit of Claude development, coordinated by Codex. Bounded proof, novelty and computation audits use **gpt-6-astra, high**. Parent runtime metadata limitation is disclosed once in LOG.md.

- Candidate: `895d85fdd995e9f227dabaf8a212ba4d3b188db0`.
- Rules/handoff head: `8b27da5ea2e0d363d2a416482b176466dc33efa9`.
- Base/current main fetched at audit start: `b5388c25a2a5ccb8d0faf816ab87023cf347bcd3`.
- Development files are unchanged by this audit. No final IDs allocated (no range), shared registry edits or readiness decision.

## Overall verdict

**WORK — developer response required.** The local Delsarte transference, qualitative uniform bound, critical-lattice cap and threshold arithmetic survive independent reconstruction. The explicit-gamma independent checker appears sound on inspection, but its data-dependent replay was unavailable. Neither that limitation nor the developer-checker defect below is a counterexample to the cubature theorem. The claims of target completion and two rigorous verification paths, and several conclusions in the report/gates, require correction before readiness.

The finite regeneration and direct-ball replay are complete: all 278 checks pass, and all 139 compact witness rows exactly reproduce committed evidence. Overall findings: **six MAJOR, three MINOR, no BLOCKING**. The missing gamma replay remains an explicit audit limitation.

## Findings already established

### A1 — MAJOR: explicit compact-support target is silently closed by a different witness

`theory/explicit-gamma-target.md:8` requires an explicit compactly supported function. Lines 4/14 say -07 completes it, while `theory/explicit-gamma.md:70` uses a nonzero polynomial times a Gaussian. The qualitative cutoff approximation in -02 does not specify an explicit certified cutoff with retained excess. `CLOSED` also replaces, rather than accompanies, an allowed epistemic status. Preserve the original target and its actual status, explicitly record a changed/general-L1 target, or supply the missing explicit compact-support certificate. See [transference.md](audit-work/transference.md), T1. This is material scope/status work and requires focused review.

### A2 — MAJOR: one claimed rigorous gamma path lacks certified Fourier-coefficient conversion

`code/gamma_certificate.py:297–300` evaluates every G coefficient through ordinary 60-digit mpmath and converts to binary64 without a retained interval or proved evaluation-error bound. The Taylor error budget assumes correctly rounded exact coefficients; the Arb value calculation certifies only G(0). Certify all coefficient errors and their propagation, or label that path a numerical cross-check and identify the rigorous proof-bearing path accurately. The use of NumPy powers also needs to agree with the stated elementary-operation error model. See [gamma.md](audit-work/gamma.md), G1. The independent Bernstein implementation carries Arb coefficient radii and avoids this particular gap; this finding does not refute the theorem.

### A3 — MAJOR: report extends the torus limitation outside its proved range

`report.md:89` calls the torus route proved useless in the discussion of 110–217. Record -06 proves its limitation only for 2–109, as `report.md:83` correctly states. Restrict the negative conclusion to its actual degree range and keep the remaining torus route unresolved. A larger uniform gamma itself comes from this route, so the broader negative conclusion is unjustified.

### A4 — MINOR: sufficient finite-route criterion is described as necessary/exact

`theory/explicit-gamma-target.md:10` gives a valid conservative sufficient criterion but says the construction loses exactly the displayed factor and the level “must” satisfy it. The exact normalization is `6 R/(2L+r)^3`, with `6m_(L+1)=(2L+1)^3+5(2L+1)`. Call the displayed criterion sufficient and conservative; no downstream result needs the sharper expression. See transference T2.

### A5 — MINOR: stale local-certificate prose

`theory/explicit-gamma.md:5,135–140` describes the local verification as future or literature-dependent despite the present completion claims. Reconcile those descriptions with the final proof route and audit limitations. See gamma G2.

### A6 — MAJOR: the claimed preregistered plain-LP kill is not established

`gates.md:88–90` treats values within numerical tolerance as zero and declares the original kill rule met. The preregistered rule instead requires a non-increasing fitted `n(rho-1)` over the last four tested degrees. Recomputed from the committed upper values for n=9–12, these are approximately `2.74106e-5, 2.64366e-5, 2.84971e-5, 3.24709e-5`; no qualifying fit is supplied. The literature alternative is still open. Preserve the original gate, append an accurate verdict and distinguish a discretionary decision to stop/defer this route from passing that gate. Synchronize resulting summaries/dispositions. See [finite.md](audit-work/finite.md), F1. No proved theorem depends on this numerical verdict.

### A7 — MAJOR: matching the integer cutoff does not require the cap constant

`report.md:100` says cutoff 110 is reached if and only if gamma_A=1/18. But at n=110 it suffices that gamma_A>9227/166375, strictly below 1/18. For example gamma=111/2000 gives cutoff 110: its exact package margin is 109/2 there and negative at 109. Matching the coefficient 19/108 does require equality with the cap; matching the integer cutoff does not. Correct the equivalence. See [corollary-novelty.md](audit-work/corollary-novelty.md), C-N2.

### A8 — MAJOR: recorded mechanism-gate coverage/timing is incomplete

`novelty-gate-E1.md:7–10` records headings, one obstruction table and selected rows. It does not establish the complete inventory and every obstruction/disposition table required by WORKFLOW, or when that coverage preceded generation. Reconstruct the actual coverage/timing from existing evidence; if some comparison was missing, complete it and explicitly label it retrospective. This is a record/coverage finding, not proof that the developer did not read the omitted material. The present audit read all 1,278 IDEAS lines and found no duplicate registered result; that cannot be backdated into a prospective development gate. See corollary-novelty C-N3.

### A9 — MINOR: numerical and current-status records need reconciliation

`gates.md:89` reports all plain ratios within 3e-6, but n=7,8,9 exceed that envelope (maximum approximately 5.621e-6). `gates.md:81` says B&B was incomplete for every run, although three n=2 rows report completion. Their lower bounds remain below Fisher, so the valid conclusion is unchanged. The cube Q1a reproduction requires `--out`; record a corrected command in the next handoff without editing the immutable old instruction body. Several results/report/log/theory pointers still name handoff 02 or describe completed work as future. See finite F3/F4 and corollary-novelty C-N4 for exact locations. Preserve historical entries and correct current summaries with dated dispositions.

## Per-claim verdicts

| Provisional claim | Audit outcome |
| --- | --- |
| -01, C0 assembly | Accepted at its stated finite and eventual ranges; no new global argmax bridge claimed. |
| -02, finite/continuous Delsarte bound | Accepted; local elementary proof, exactness conventions checked. |
| -03, qualitative uniform Theorem A | Accepted with the declared literature dependencies. |
| -04, cap and dual lattice references | Accepted; exact reruns pass. |
| -05, explicit compact-support target | Completion/status not accepted as written; A1/A4. |
| -06, finite torus limitation | Accepted: reduction, committed witnesses and full regeneration/direct-ball replay pass. Scope is only 2–109 with the stated conversion. |
| -07, explicit gamma | Scaling/arithmetic and independent code inspection pass; A2 and unavailable input-dependent replay prevent complete local computational acceptance in this audit. |

## Verified coverage and execution

- [Transference review](audit-work/transference.md): independent proofs of -02/-03/-04, primary KLM/Greenfeld–Lev/Lev–Matolcsi text, cap script rerun and independent integer enumeration. Thresholds 55, 110, 138, 109, 218 and 220 checked with exact polynomial comparisons and the unique-positive-root argument.
- [Gamma review](audit-work/gamma.md): both certificate implementations, independent exact Fourier controls (105 coefficients), rational Bernstein controls (six synthetic boxes), primary DGOV theorem/normalization/table and ancillary facets. The complete gamma input-dependent runs were **not performed**: shell downloads returned HTTP403 and the web reader did not expose the C++ evaluator bytes. Existing receipts were inspected, not counted as fresh runs. The pinned input hash and outstanding commands are in that review.
- [Corollary and novelty review](audit-work/corollary-novelty.md): all 1,278 IDEAS lines and every obstruction/disposition table, relevant complete entries, dependency statements/statuses, topic candidates, gates and report. The C0 equality ranges, corner convention and expansion constants match the accepted dependencies. Inherited accepted certificates were not all rerun. No registered duplicate was found; the existing broad Cohn–Elkies route is attributed, and candidates 01–07 and failed/deferred attempts are retained. No exhaustive historical-priority claim is accepted or made.
- [Finite review](audit-work/finite.md): Q0 D1 controls and exact D3 certificate PASS, leverage receipt matches, Q1a torus/cube exact controls PASS n=2–8, all 15 reference lattices pass, and a separate exact coefficient-box calculation checks all 139 committed strong witnesses and coverage flags. Q1b's 32 stored upper values respect their Fisher/lattice references. Numerical LP minimality/continuum positivity are not upgraded to proof.
- Full prescribed finite reruns: `pdn_lattice_witness.py --nmin 2 --nmax 140 --extra evidence/lp-lattice.json --perturb` followed by `pdn_check_ball.py --full ... --out ...`, with full paths/environment in the finite review. All 278 avoidance/index checks pass; all 139 compact rows match exactly. Strong coverage is 108 degrees (2–109), weaker coverage 127 degrees (2–128). Raw outputs, hashes and byte sizes are recorded off-repository. The statement that no possible stronger witness exists above 109 uses the cited optimal packing result, not the unsuccessful heuristic searches there.
- Optional n=5, extra=5 final-code LP replay completes with upper value 139.552493588972 and rho 1.081802275884, approximately 1.04e-5 relative from the stored earlier-code upper value. It reproduces the qualitative measurement, not the original receipt exactly; no rigorous lower bound above Fisher is obtained.
- The orchestrator ran `python -B topics/padua-effective-cubature-20261112/code/evidence_manifest.py --verify`: all nine evidence files pass their committed size/hash checks. This script does not verify producer hashes; those remain separate code/receipt comparisons.
- `git diff 0abf5e7 HEAD -- topics/padua-effective-cubature-20261112/gates.md` confirms original Q0–Q3 definitions were retained; changes begin under Verdicts and append results/addenda.

Generated outputs remain outside Git. Audit records are small prose; no third-party source or PDF is committed. Literature results retain explicit LITERATURE dependencies and the audit does not claim to have reproved the cited external theorems.

## Next step and review boundary

Claude must answer A1–A9 in `response-01.md`, preserve disagreements, and synchronize the actual claim/disposition records. Scope/proof/status or result-bearing code changes require a focused Codex review of those changes and dependencies. This audit does not allocate IDs, apply shared registries or mark PR #34 ready. Handoff 04 contains the complete response instruction; only AC merges.
