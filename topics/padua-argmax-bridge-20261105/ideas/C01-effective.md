# IDEA?argmax-bridge-C01-effective — numerical constants in the eventual-argmax proof

Aliases: PD-T216 effectivization; coarse global phase entry; explicit enormous
argmax onset; quantitative PD-T229 continuation.

- Question / scope: can the existing PD-T216/221/224/228 assembly supply an
  actual explicit global argmax onset, even if the resulting finite bridge
  is impractical?
- Mechanism and hypotheses: retain the exact corrected kernel, odd periodic
  mesh, full phase diamond, polynomial collision values and physical center
  cover. Replace the unspecified constants in PD-T216's existing proof by
  numerical strip, endpoint and far-mesh bounds. Optimize PD-T221's full
  quadratic/fractional/linear envelope; then apply PD-T224 and PD-T228.
- Closest registry entries (read in full): IDEA-326/327/328/331 in
  `padua-argmax-alln-20261101/FINAL_CANDIDATES.md`, their original
  `ideas-codex-fallback.md` and `gated/CANDIDATES.md` source records;
  IDEA-336/337 in `padua-argmax-effective-20261103/ideas/r1-r2-r5.md`;
  IDEA-455/456/457/459/460/461 in
  `padua-argmax-effective-2-20261105/ideas/H2-H3.md`. The complete PD-T216
  proof, PD-T217/221/224/225/228/229, PD-T157 and PD-T368 were inspected.
- Separation criterion: numerical constants and a literal global onset
  distinguish this result from the inherited existential theorem. There is
  no new mechanism. An unresolved uniform estimate in the written global
  proof, an uncovered physical center, or a loss of polynomial collision
  values kills the proposed explicit assembly until repaired.
- Literature baseline and search limitations: repository comparisons only.
  The complete current `state/IDEAS.md` headings, identifiers, aliases and
  summaries were scanned, with obstruction/disposition tables read; searches
  used `effective|explicit.*constant|global.*bound|phase.*far|threshold|onset|
  uniform.*diamond` and the closest primitive/defect/corner terminology
  across the argmax ideas, theory, logs and literature INDEX. No external
  source was opened, no priority claim is made and no source proof is
  transferred. LIT-312/379 remain context for the global norm order, not
  premises of the phase-dependent estimate.
- Applicable obstructions: PD-N079 rules out primitive-only coset
  maximality and a purely quadratic local primitive envelope. The full
  fractional and finite-degree linear terms in PD-T221 are retained.
  PD-N082/083's raw-profile failures are not used. PD-N132 forbids replacing
  the global logarithmic remainder by an o(1) leading-factor-only model.
  PD-N085 does not obstruct the averaged actual-corner theorem PD-T228.
- Novelty gate verdict: quantitative explicit-constant variant of
  IDEA-326/327/328/331/336, without a new-mechanism or practical-onset claim.
- Cheapest decisive test: audit the individual estimates in PD-T216 before
  any global assembly. The parent-assigned test was stated before this
  development; this record does not retroactively preregister the ensuing
  algebra.
- Kill criterion: stop the PROVED global-onset claim if even one global
  constant, endpoint/collision case, center class or parity case remains
  unspecified. A bounded lemma may still be retained separately.
- Test discriminability: an explicit analytic bound decides uniform
  effectivity; fitting or extending finite degrees cannot do so.
- Actual test results: the written numerical extraction yields the bounded
  lemma in [C01-effective-global.md](../theory/C01-effective-global.md).
  The candidate global assembly is separate in
  [C01-effective-argmax.md](../theory/C01-effective-argmax.md), with its own
  exact status and reconstruction requirement.
- Disposition: retained quantitative continuation. No degree extension,
  numerical phase scan, energy extrapolation or cheap-certifier benchmark
  is part of this task.
- Canonical theory: the two linked files; final IDs unassigned.
- History: 2026-11-06, auxiliary Codex worker, parent-assigned mathematical
  development; serving model/effort are not independently exposed. Rules
  and scientific input `4b728b04216a5490910780bc609a82b853058426`.

## Other considered routes and their dispositions

| Route | Exact reason / disposition |
|---|---|
| Use PD-T368's global norm bound as far-phase entry | Abandoned for this purpose: `Lambda_n<=27500 Lambda_c` has no factor `a(alpha,beta)` and cannot force the phases into the near diamond. Its rotated-bin count remains useful context for explicit finite sums. No theorem is rejected. |
| Reprove the sharp unchanged near model | Deferred to the separately assigned N1 worker; it addresses a much smaller practical threshold. This task neither changes that model nor spends a correction term. |
| Require a new all-n energy estimate | Not pursued: the existing PD-T228 already handles actual-corner nonzero phases at the enormous degrees relevant here. Finite or analytic energy onsets are not used as argmax onsets. |
| Estimate missing global constants numerically | Abandoned: finite samples cannot make PD-T216 uniform or explicit. All displayed numerical constants below come from exact inequalities. |
