# Supplemental audit: C0 assembly, novelty and scope records

Auditor: Codex, assigned `gpt-6-astra`, high. Candidate: `895d85fdd995e9f227dabaf8a212ba4d3b188db0`; working rules/head identified by the orchestrator as `8b27da5`. Read AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md from the working tree. No Git command, development-file edit or inherited certificate replay was performed. This supplements the orchestrator's audit, not a separate approval.

## Verdict

C0 (-01) is a valid PROVED assembly of the registered dependencies at its stated ranges. No mathematical finding against that corollary. The novelty record needs a coverage/timing clarification, and the final report contains two incorrect scope/threshold assertions. Findings below do not reject the actual torus limitation theorem or the explicit-gamma theorem.

## Findings

### MAJOR C-N1: unsupported extension of the finite torus obstruction

`report.md:89` places the sentence “The torus route is proved useless there (-06)” immediately after the range `110 <= n <= 217`. Record -06 says precisely the opposite about its coverage boundary: `theory/limitation-torus-lp-finite.md:17` has S={2,...,109}, with hypotheses and excluded methods at lines23–29. No obstruction on 110–217 follows. The report itself correctly leaves this range undecided at line68 and states that witnesses of the specified kind cannot exist from110 at line83.

Fix: explicitly restrict the finite obstruction to2–109 (or the unknown package range4–109), retain torus Delsarte improvements as a possible route on110–217, and describe the orbit-conversion hypothesis rather than “in any form” without qualification. Also qualify report line20 and results line26:2–109 is the range where the **best possible capped uniform bound** cannot exclude packages; the currently certified lower constant excludes packages only from218. It is not the entire presently unresolved range.

### MAJOR C-N2: equality of the integer cutoff does not require equality of constants

`report.md:100` says arbitrary rules reach the same threshold110 “if and only if gamma_A=1/18”. This is false for the integer threshold. The strict comparison at n110 is

    gamma_A > (111*112*113)/110^3 - 1
            = 9227/166375 = 0.05545905334335086...

which is strictly below1/18. For example gamma=111/2000=0.0555 is below1/18 and gives

    (1+gamma)*110^3 - 111*112*113 = 109/2 > 0,
    (1+gamma)*109^3 - 110*111*112 = -1233781/2000 < 0.

Because the required ratio `(n+1)(n+2)(n+3)/n^3` decreases with n, this constant already has cutoff110. Python Fraction arithmetic independently checked these exact expressions. This is a narrow false assertion in prose, not a failure of the correctly computed cap or either theorem's threshold.

Fix: replace “same threshold iff” with “same coefficient19/108 iff”, or state the correct strict interval for matching the threshold. No new theorem is needed to remove the false equivalence.

### MAJOR C-N3: the recorded E1 novelty gate does not establish the required coverage

`novelty-gate-E1.md:7–10` records all section headings, **one** obstruction table (IDEAS106–117), the 3D rows, and selected full rows. WORKFLOW63 requires the complete headings/identifiers/aliases/summaries inventory and **every obstruction and disposition table in full**, followed by full shortlisted entries and linked theory. The file records no completion of the other tables. The gate is dated at0f1d797 (line3), which LOG says already contains the new mathematics; this alone does not prove when the reading occurred, but the current record does not demonstrate prospective completion.

Fix: reconstruct and record the actual coverage and timing, supplying existing evidence if all required reads preceded generation. If they did not, complete the missing comparison now and label it retrospective, preserving the actual chronology. Do not relabel a later check as a prospective gate. No automatic mathematical rejection or permission requirement follows. The C0 exception is defensible: its file explicitly identifies a citation-only assembly and does not generate a mechanism. This finding concerns E1/E3/new gamma mechanisms, not C0's assembly.

The full registry audit found no prior registered implementation of this Delsarte transference or cube-native kernel LP. This supports the substantive bounded variant verdict but does not itself supply the developer's missing prospective record. S4 already explicitly proposes a Delsarte/Cohn–Elkies effective-constant route, and the gate acknowledges that hit at line15: the new ingredient should remain the explicit inequality/transference/certificate, not invention of that broad route. The registry's IDEA-168 contains a different, orthogonal-polynomial Turán certificate; it is not a Delsarte positive-definite extremal problem and does not duplicate this work.

### MINOR C-N4: current next-step and completed-check text is stale

`results/padua-effective-cubature-20261112.md:38` still names handoff02 and treats -05 certification as future work; LOG109 likewise lists certified phi(-05) under Runs needed. `theory/lebesgue-constant-corollary.md:130` lists the completed C0 independent check as open despite line138 recording its disposition. `report.md:125` names handoff02. `attempts/E3.md:38` retains the original non-effective-threshold conclusion without a dated campaign update.

Fix current pointers to handoff03 and distinguish the retained session1 history from the current gamma result. The original -05 compact-support target and its CLOSED/OPEN status conflict require the mathematical disposition reported separately by the transference auditor; do not erase that target by a mechanical wording update.

## C0 reconstruction and dependency coverage

Read -01 in full and the C0 novelty gate/independent-check record. Checked the registry rows for PD-T101/159/162/166/169/174/177/181/209/214/225/228/229/246/269/270/271: all are PROVED, with accepted Claude audit links and no rejected disposition.

Checked direct dependency statements, definitions, assumptions and dated status qualifiers for PD-T101/159, all finite global argmax results2–16, and PD-T269/270. Read PD-T246, PD-T229 and PD-T271 in full. This is an assembly audit, not a re-audit or replay of every inherited certificate. Historical “audit pending” body text is superseded by dated accepted-status headers/registry rows; no hidden unproved hypothesis was introduced.

- Node convention: `(cos(j*pi/n),cos(k*pi/(n+1)))`, j+k even, corrected exceptional(n,0) cardinal coefficient. Same closed-square domain and total-degree space throughout.
- PD-T209 gives n2; PD-T162/166/169/174/177 give3–7; PD-T181 gives8; PD-T214 gives9–16; PD-T246 gives17–32. The equality sets agree: two bottom nonnode corners for even n, two left nonnode corners for odd n.
- PD-T229 gives an existential integer N_* and precisely the same equality set for every n>=N_*. It is not an effective global threshold. Its proof may take N_*>=ceil(exp(10^7)), so taking it at least32 causes no problem.
- PD-T271 is a corner-value expansion for every n>=32. Substitution is justified for n>=max(32,N_*), plus the separately mentioned n32. Every coefficient, remainder term and strict decimal endpoint in -01 matches PD-T271. PD-T269 supplies the integral defining kappa; PD-T270 supplies the quadratic one-dimensional remainder. The two definitions of Lambda_c agree by PD-T159/229.
- The missing33<=n<N_* bridge and the sharper -1/N expansion remain unclaimed. No numerical measurement is a premise of the assembly; inherited computer-assisted trust bases are explicit.
- PR27 is expressly not a dependency. The corrected gate and theory record disclose its stronger unmerged claim and the scope in which it would supersede C0. I did not access PR27's branch or independently check its current remote status; the root audit owns that read-only verification.

## Novelty and candidate coverage

Read **all1278 lines of state/IDEAS.md**, including every obstruction/disposition table and the long historical source rows. Truncated initial tool outputs were followed by smaller range reads to cover omitted spans. This full audit read includes the unisolvence, MZ, lattice, programme, bivariate-Lanczos, signed-MZ, argmax, follow-up, conditioning and 3D sections. Read both C0/E1 gates, BRIEF, plan, LOG, rounds, report, results and attempts E1-gamma/E2/E3. Read the full D1 candidate record, full T9 response candidate collection, the T9-r06 packing/positive-weight candidate entries, S4, T4's full gate/candidate record and their directly relevant registered theory statements.

Searches used Delsarte, Turan/Turán, Cohn–Elkies, packing, positive definite, negative semidefinite, cube-native LP, Lebesgue/corner/argmax and explicit constants across registry, topics, tracks and literature. Read literature/INDEX's introduction, complete relevant rows/addenda and section inventory; this was a targeted INDEX read, not a claim of all729 lines. Relevant source IDs:379/482/484,640/663,659/660/662/668/669. Read the full P1 comparison. Source-original verification of KLM/DGOV is assigned to the separate literature/theorem reviewers; I opened no PDF and make no fresh external-priority claim.

Substantive classification is conservative: C0 assembles existing registered results; E1 extends arbitrary-rule scope beyond the old single-unshifted-lattice class and provides a uniform inequality beyond D1's compactness conclusion. The general LP mechanism and packing-function source are attributed. No duplicate registered theorem needing withdrawal was identified. The C0 priority paragraph correctly limits its second/third-term comparison to P1's documented search and distinguishes the old leading coefficient. Its report's “No priority claim” should be understood as no unconditional historical-priority claim; the theory does retain this explicitly qualified comparison.

Candidates01–07 are preserved. Plain Turán and quantitative compactness remain deferred; the cube LP keeps its measured small-degree kill and untested higher degrees; the cube-Delsarte extension is unrun; separation strengthening is deferred. Gamma round3's failed numerical improvement and the discarded enclosure/tail approaches are preserved with concrete reasons in attempts/E1-gamma.md rather than generalized into universal negative claims. The numerical kill statements are labeled MEASURED; they do not refute the Turán conjecture or all higher degrees. Round counts are ceilings and the3/7 stop is documented, with no unauthorized extension evident.

## Limitations

No consequential computation was rerun by this subauditor. Only exact threshold-counterexample arithmetic was executed, using Python's Fraction. No claims are made about the LP solver, gamma checker, lattice witness executables or their manifests; those are assigned elsewhere. Existing theorem statements and accepted dependency statuses were inspected without reopening the full inherited proof/certificate programme. The standalone -05 target closure issue was forwarded to, and is owned by, the transference auditor.
