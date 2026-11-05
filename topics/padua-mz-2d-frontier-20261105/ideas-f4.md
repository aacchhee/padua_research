# F4 candidate and novelty memory

Rules/input `83cf6f1ee244f2e72057332a7ec04ee74db1f0de`, 2026-11-05.
Codex mathematical worker; requested gpt-6.1-sol xhigh; resolved runtime
metadata not independently exposed. Gate scope and G5 preregistration:
`attempts/F4.md`. No numerical computation at registration.

## IDEA?mz2d-frontier-codex-f4-01 — density tail in the actual weighted L1 norm

Aliases: signed-cardinal density; triangular Chebyshev density truncation;
positive main density plus endpoint-controlled remainder.

- Question / scope: prove `sup_(m>=2) ||H_(m,m-1)||_(C->L2(dx dy))<infinity`
  with an explicit constant for the unchanged PD-T114 operator.
- Mechanism and hypotheses: write `w_z=rho_z d_m(z)` using the accepted
  cardinal formula, and `d_m=g(x)g(y)+e_m`, `g(x)=pi sqrt(1-x^2)`.
  Bound `||e_m||infinity<=C/m`. Control the positive main term by tensor
  CC and the error by `(C/m) sum rho_z |p(z)|`, with an O(m) polynomial
  norm comparison.
- Closest entries read in full: IDEA-219–223, IDEA-073–076,
  IDEA-212–214; PD-T101/106/111/112/114, PD-T017 and PD-T022.
  IDEA-210–227 and all PD-N044–053 obstruction/disposition rows were read.
- Separation criterion: the proof must retain one power of `|p(z)|`
  when treating the density error. Any indispensable replacement by a
  uniform absolute-Gram bound erases the distinction and is killed by
  PD-N052. A tail larger than O(m^-1), or Chebyshev L1 loss larger than
  O(m), kills this particular coarse compensation.
- Literature baseline and limits: complete local INDEX screened for
  relevant terms; no new primary source contacted, and no priority claim.
  Generic density truncation/duality/norm comparison are classical tools.
- Applicable obstructions: PD-N050 rules out signed upper-Gram-only
  transfer; PD-N052 kills uniform absolute Gram and negative leverage.
  This candidate instead uses a different scalar remainder and the exact
  weighted L1 norm. PD-N046's factor-two nodal majorant is not asserted.
- Novelty gate verdict: variant with the explicit difference above;
  new within the documented local mechanism comparison only.
- Cheapest decisive test: derive the density exactly, telescope its
  coefficient tail, and prove the O(m) comparison analytically before runs.
- Kill criterion written before testing: a missing exceptional cardinal
  correction, wrong probability normalization, or insufficient power of m
  stops the proof until repaired. No numerical asymptotic fit is decisive.
- Test discriminability: the analytic estimates quantify every m and
  therefore can settle the norm target; a finite screen cannot.
- Actual results: a complete analytic development proof gives
  `2<=||H_(m,n)||<=C_*<30` for every m>=2 and 0<=n<m. No numerical
  run is used. The exact density, tail bookkeeping, raw-Chebyshev norm
  comparison and positive-main comparison all close.
- Disposition: retained; PROVED in development, supplementary independent
  review and required Claude audit pending. Canonical record:
  `theory/f4-uniform-density-bound.md`,
  `PD-T?mz2d-frontier-codex-f4-01`. No PD-N is generated.
- Topic / audit / history: F4; supplementary check and required Claude
  audit pending.

## IDEA?mz2d-frontier-codex-f4-02 — numerical sign-pattern lower witnesses

Aliases: infinity-to-two quadratic maximization; alternating signed input;
continuous disjoint-tent realization.

- Question / scope: G5 finite lower witnesses through m=200.
- Mechanism: maximize the feasible output norm over nodal sign vectors,
  using the exact continuous-input realization already proved in PD-T112.
- Closest entries: IDEA-220 / PD-T112, read in full.
- Separation criterion: no new mechanism is claimed; this is an explicit
  computational application of the old exact norm identity.
- Literature limits: no external optimization optimality result used.
- Obstructions: finite growth and local maxima do not prove divergence
  or the exact operator norm; PD-N052 is not lower evidence here.
- Verdict: equivalent norm application, retained as the requested screen.
- Cheapest test / frozen kill: check weight/moment normalization and
  feasible output norms at small m; terminate if these disagree.
- Actual result: NOT RUN. The orchestrator subsequently confirmed G0 PASS.
- Disposition: deferred; the complete analytic uniform theorem supersedes
  the boundedness-screen purpose, as recorded in the dated F4 attempt
  entry. Resume only for sharper quantitative measurements with the
  proof's uniform result kept separate from finite lower witnesses.
- Canonical record: preregistration `attempts/F4.md`; no PD-N.

## IDEA?mz2d-frontier-codex-f4-03 — sharper raw Chebyshev L1 comparison

Aliases: endpoint-cutoff logarithmic comparison; possible vanishing error.

- Question: improve the O(m) raw sampling loss to O(log m), potentially
  yielding a vanishing density-remainder contribution.
- Mechanism: endpoint cutoff and weighted Cauchy-Schwarz for continuous
  L1 Chebyshev mass, plus discrete sampling comparison.
- Closest entries: IDEA-065/069/074 and IDEA-220; linked lower-bound and
  filtered-kernel proofs were inspected for their endpoint hypotheses.
- Separation criterion: must control the forward weighted L1 sampling
  functional; existing inverse Schur bounds do not establish it.
- Literature limits: no claimed novelty; no source theorem inherited.
- Applicable obstruction: endpoint column L1 domination PD-N005 cannot
  be reused. This direction is unnecessary if the coarser bound closes.
- Verdict: variant with an explicitly sharper norm comparison.
- Cheapest test / kill: check endpoint reproducing kernels before trying
  an all-polynomial statement; absence of a sampling proof leaves it OPEN.
- Actual result: not tested or used.
- Disposition: deferred to avoid unnecessary dependence in the uniform proof.
- Canonical record: none; no PD-N for deferral.
