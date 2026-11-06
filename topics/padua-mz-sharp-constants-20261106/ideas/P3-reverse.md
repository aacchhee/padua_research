# IDEA-071 — signed reciprocal interpolation completion

2026-11-06 ID history: `IDEA?mz-sharp-codex-P3-01` → `IDEA-071` (retained record consolidated under this ID); statements, original registrations and historical dispositions are preserved.

Aliases: discrete log-Hardy bound; dyadic signed sinc remainder; global
cotangent interpolation; reverse Volterra transfer.

- Question / scope: prove liminf (log N)^2 lambda_min(CC,N-1) >= pi^4/8
  through every integer N, retaining the existing S1 limsup separately.
- Mechanism and hypotheses: on the full interpolation space Pi_N use
  exact cotangent cardinal interpolation. Extract two endpoint logarithmic
  primitives, bound the remaining signed operator in the actual CC norm,
  and use a sharp discrete Volterra bound with the oscillatory factor 1/2.
- Closest registry entries (read in full): IDEA-065–071, IDEA-385/386,
  PD-T013/017/018/020/294, PD-N005/006 and the entire S1 transfer record;
  reading scope is in ../novelty-gate-P3.md.
- Separation criterion: an all-input upper interpolation bound with
  leading coefficient 8/pi^4 in squared norm, beyond S1's fixed smooth
  trials. A nonuniform estimate depending on envelope derivatives, or
  a leading constant obtained only after removing arbitrary nodal inputs,
  kills this claimed completion. This is a continuation of the existing
  S1 mechanism, not a fresh mechanism allocation at PR preparation.
- Literature baseline and search limitations: bounded repository screen;
  no external singular-integral theorem or priority claim is imported.
  Any Fourier/sinc estimate used must be proved locally.
- Applicable obstructions and exact hypotheses broken: PD-N005 forbids
  the uniform absolute-cardinal L1-column bound. This route keeps signed
  sums on comparable dyadic scales and uses L2 orthogonality. PD-N006
  does not obstruct a full-space upper interpolation bound by restriction;
  S1's existing degree-constrained trial supplies the opposite direction.
- Novelty gate verdict: resumed continuation of S1 / IDEA-071.
- Cheapest decisive test: derive the exact full-space kernel split and
  establish a uniform signed near-diagonal L2 estimate; then check the
  discrete primitive's sharp leading norm with exact quadrature weights.
- Kill criterion written before testing: an uncontrolled logarithmic
  leading contribution from a discarded endpoint, microscopic cell,
  middle index or signed pole blocks the proof at that estimate. A mere
  incomplete proof defers this route and never rejects PD-T020.
- Test discriminability: analytic all-vector estimates can establish
  the liminf; numerical agreement cannot. No new experiment is planned.
- Actual test results and committed evidence: after R publication
  `17ca9f441cece178354e70504a6c739df501a224`, two productive analytic
  rounds give the uniform signed remainder P3-01, sharp discrete primitive
  P3-02 and complete reverse-transfer theorem P3-03. Supplementary
  independent reconstruction passed at the frozen theory hashes; see
  ../independent-checks-P3-remainder.md and
  ../independent-checks-P3-assembly.md. No new numerical execution.
- Disposition and precise rejected scope, if any: retained analytic
  completion at the stated scope, supplementary check passed;
  [audit-02](../audit-02.md) accepted the completed proof.
- Disposition reason: exact all-input norm estimates satisfy the
  separation criterion; no equality rejection or K1/K2 alteration.
- Canonical theory / negative-result ID: PD-T544,
  P3-02 and P3-03 in ../theory/P3-*.md. Original registry PD-T020
  is PROVED via PD-T546 together with PD-T523.
- Topic / completed audit link / history: 2026-11-06, Codex developer,
  requested gpt-6.1-sol xhigh; serving metadata unexposed. No Git or
  shared-registry edits. Up to six rounds, stop after two consecutive
  no-progress rounds; ../attempts/P3.md records the actual outcomes.
