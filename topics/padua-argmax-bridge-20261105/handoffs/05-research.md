# Handoff 05 — continuous near-model comparison and calibrated bootstrap research

- Status: superseded by 06: AC authorizes a fresh fifteen-round campaign and prioritizes the analytic upper boundary and very cheap certification
- Previous handoff: 04-research.md
- Next agent / model / effort: Codex, gpt-6-astra high coordinator; Sol medium technical development, Sol xhigh ordinary mathematics, distinct Astra high supplementary mathematical checks. Handoff01 permits Astra ultra only for a genuinely hard decisive step, with a written justification before allocation.
- Role: orchestrator and developer
- Branch: codex/padua-argmax-bridge-20261105
- Input head SHA: `2aa097767a508a7d94c6f24c8bccdbf01aa8aefa`
- Main / base: `be9a8318150204711d5446d2ea26284cf1ed0819`
- Stage: WORK
- Written by / date: Codex, requested gpt-6-astra high; serving metadata unexposed · 2026-11-06

## Scope and authority

AC explicitly approved pushes, allows up to10MB total for now, and directs major cleanup to a separate topic. Continue checked research checkpoints without asking again. Final conservative inventory is6,703,431bytes; all93essential evidence files are individually below16KiB, and their index is12,724bytes. Keep small evidence/provenance; bulk physical cold-storage transfer remains pending. No cross-topic cleanup, dependency trees, raw logs or third-party text in Git.

Only the orchestrator mutates Git, shared topic files or PR27. Write only this topic and results/padua-argmax-bridge-20261105.md. Never push main, merge, force-push, change tags or .github. Keep PR27 draft at WORK. Required substantive Claude Opus5.5 xhigh audit is PENDING; Codex supplementary reviews do not replace it. Final IDs remain unassigned. Preserve permanent reservations T392–431,N146–161,IDEA490–529,LIT598–613, first published f708a83; refresh at preparation/readiness, not repeatedly during exploration.

## Read first

Read AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md at the current head and record the full SHA. This session read them at8dc1521cf68f7780bd10e02495f6f71a639c03c6; the adopted proportionate-record rules are unchanged. Fetch current main/topic and reconcile without rewriting published history. Read [report](../report.md), [results](../../../results/padua-argmax-bridge-20261105.md), [LOG](../LOG.md), [gates](../gates.md), [rounds](../rounds.md), handoff04, and handoff01's scientific budgets.

For N1 read the unchanged N1-round5/6 proofs and their reviews, then theory/N1-round7-coefficients.md, N1-round7-comparison.md, N1-round8-jumps.md, N1-round8-modulus.md and independent-checks-n1-round7.md / independent-checks-n1-round8.md. Read the full relevant idea/attempt/gate records and C1 near-edge-model-criterion.md. Follow all load-bearing dependencies, especially N1-14's central root/entropy formulas and PD-T271 normalization.

For N3 read N3-bootstrap-corner.md, N3-bootstrap-finite.md, N3-bootstrap-cover-r8.md, N3-uniform-energy-r8.md and N3-defect-enclosure-r9.md; their independent reviews; both failed independent-checks-bootstrap-r8-n32.md and accepted independent-checks-phase-r9-n32.md. Preserve the failed records and every old source. New runtime code/data pins are allowed; no new prose validation pins.

## Exact current boundary

Global exact corner argmax remains every integer2–40, with exactly two nonnode-corner maximizers. This session adds no global degree. PD-T099 remains OPEN, the bridge begins41, and the inherited eventual argmax onset N_* is still ineffective. Near-model validity n>=10^6 and the energy onset below are not argmax onsets. B3 remains OPEN and B4 blocked.

N1 completed rounds7/8, with distinct accepted mathematical reconstruction:

- The unchanged fixed-count M_near satisfies |S−M_near|<3/14000 on rho<=1/2,n>=10^6. Its one permitted correction was already used in round5.
- N1-16 gives both favorable coefficient gaps, uniformly: B_c−B_M>=47r²/(48pi²), b_c−b_M>=r²/(24pi²), r²=alpha²+beta². The remainder is uniformly bounded, with no useful small bound yet. The log coefficient is smooth/even at0; this does not remove a finite-degree cusp from the residual.
- N1-17 defines F_n as the phase increment after subtracting those exact logarithmic terms, and G_n as their exact favorable loss. The target is F_n<=G_n+eta, eta107/3584000.
- N1-18 constructs continuous Q_n, Q_n(0,0)=0, with |F_n−Q_n|<9/(2n). This charges exact strip seams, the whole H8/special-row error once per phase, noncentral collision marks and the beta0 half-angle cutoff. Its signed continuous-reference construction is explicit in the independent review. It is a bookkeeping decomposition, not a new model correction or a bound on Q_n.
- Hence it SUFFICES to prove Q_n−G_n<=1/40000 throughout the same domain: eta−9/(2n)>1/40000 at n>=10^6. No such continuous modulus constants have been proved. N1-19 keeps this target OPEN.

The C1 criterion would then exclude the stated complementary interior vertical-edge classes using N5's1/2048 deficit. It would not by itself settle far phases, other center classes, actual-corner coherence or the full square. No finite2–128 energy extrapolation to n>=10^6 is allowed.

N3 completed rounds8/9:

- A new explicit maximum-exclusion certificate mode uses the accepted3/4 energy premise only for true-corner classes and still checks strict S_upper−Delta_lower<Lc_lower for every admissible noncorner class. It is not pointwise corner descent before global closure. Old pointwise predicates remain unchanged.
- The single new n32 MPFR producer completed724visits/364leaves in222.81307childCPU-s, versus992leaves/620.093411CPU-s in round6. Essential gzip3367bytes SHAa01bc14b968676161afa0690e5ed41005da8cb3f87fb8c6393594bc37ed3986a; plain21338bytes SHA97c339181652d37e7e3c34522959f1b7157b8ea26d3f0ab83c0ebc1c3901528e.
- The first independent v2 replay failed20bootstrap defect predicates, checked364/364,0pending,136.175287totalCPU-s. All20defect lower bounds were0. This failure is preserved, not relabeled a counterexample or accepted run.
- After a separate prospective gate, independent Arb v3 keeps positive/opposite-sign pair lower bounds before profile aggregation, alongside all old natural bounds. This is independent implementation of an existing formula, not a novelty claim or copied MPFR arithmetic. Math/source controls passed before publicationb39eec3f61b90815f465442268630c2b2c6b8522.
- One changed-source replay of the ORIGINAL candidate passes364/364,0failed/0pending,exit0,139.405409totalCPU-s. All20old failures have strict new margins; all332numerical leaves retain bit-identical nondefect outputs and no defect bound weakens. Source/input/supervisor and254build/runtime entries remain stable. Combined accepted producer/checker cost is about362.218CPU-s versus1003.756CPU-s round6 at known n32. No producer rerun, tree refinement or other degree occurred; no higher-degree scaling law follows.

The new analytic energy estimate, independently accepted, is W<=n^4[(21/32)Lambda_c+1.5e9(1+log(n+1))] for n>=32. It implies3/4 energy only for log n>=128000000000. Finite energy2–128 remains separately proved;129<=n<ceil(exp(128000000000)) remains OPEN. This enormous energy onset neither makes a practical bridge nor changes the checker's finite premise.

## Next bounded research

1. **N1: the actual continuous residual comparison.** Preregister the precise Q_n modulus and cheapest decisive coefficient test before a new round. Use N1-19's formulas and conditional scalar budgets. A quadratic-only or quadratic-plus-finite-cusp ansatz may be false: on beta=0 the exact central root band is alpha<epsilon<arccos(1−tan(alpha/2)), with width of order sqrt(alpha). Fractional rho^(3/2), r²log(1/rho) and finite linear cusp allowances may be needed. No nonzero fractional coefficient has been proved merely by identifying that band. Derive constants uniformly through the coalescing roots/zero phases and compare the COMPLETE budget with1/40000; do not drop terms, differentiate through an uncharged branch or infer a constant from a fit. The polynomial coefficient gaps and branch allowance are already frozen/accepted and should not be re-proved as substitute progress. A hard decisive coalescing-root modulus may justify Astra ultra under handoff01, but record what and why ordinary effort was insufficient before allocation. No second model/correction family or cosmetic restart.

2. If continuous analytic estimates leave an explicit compact parameter function, implement validated integrals/series/tails and interval bounds for that function under a registered error budget. A sampled or fitted maximum is not a proof. The n17/24/32 normalization pilot is MEASURED only and never validates M_near below n>=10^6. A proved larger comparison onset must be identified as such and assessed for practical relevance;10^6 remains only approximation validity until comparison is proved.

3. **N3: assess cost before a higher-degree cover.** The improved known n32 calibration is accepted; do not repeat it on unchanged sources. Any higher-degree job needs a new prospective bounded cost assessment and explicit cap; current kernels still contain degree-growing finite-harmonic/projected-profile work. No automatic n64/128 full run, inferred log² law or Syvert pack. Preserve independent MPFR producer and Arb/GMP checker arithmetic, exact all-class defect and fixed finite-energy receipt/code/data guards. An accepted isolated higher degree would not fill41..that degree automatically. Source optimization requires its own mathematical/source controls before consequential runs.

4. Far phases, remaining center defects and true-corner/all-n energy are separate obligations. N5's full quarter target remains OPEN; only its specified phase-blind certificate failed. N4/N6 broad routes remain deferred after their scoped obstructions. Do not divert into cleanup or restart killed certificates.

## Reproduction, budgets and publication

Use code/phase_checker/setup.py for pinned ignored runtime/dependencies. The current independent backend is check_r9.py with --kernel round9; its new builder/source are separate from immutable v2/r8. The committed essential gzip can be decompressed to the recorded local candidate path after verifying its plain/gzip hashes. Source, input, exact argv, build/header/runtime/loaded closure, actual CPU/exit and small receipts are required. Existing run-once wrappers refuse output reuse; do not run them just to restate a published result. All raw outputs remain local/regenerable; no physical archive delivery is claimed.

Round counts: N1=8,N2=1,N3=9,N4=1,N5=5,N6=2. Original maximum15 per direction, continued only on recorded progress; two consecutive empty rounds stop, and kill gates apply independently. Original caps6h wall/48CPU-h per direction-round; smaller preregistered caps remain binding. Syvert is preapproved only when B4 has a proved or nearly proved ACTUAL argmax onset and measured throughput showing the bridge is feasible; an approximation or energy onset is insufficient. AC launches any justified pack; no access or launch is implied here.

Update durable proof/idea/attempt records, LOG, gates/rounds, results and report at pushed checkpoints. No final-ID/shared-registry application until audited preparation; formal Claude audit follows completed development, with focused re-audit only for material changes under current rules. Push with the established credential helper and network permission option; no new AC confirmation is required. At the next session boundary commit outputs first, then separately change only this handoff's status and add handoff06, leaving exactly one open. Push both before the short continuation prompt.
