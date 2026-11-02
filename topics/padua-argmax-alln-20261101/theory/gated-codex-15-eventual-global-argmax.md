# PD-T?argmax-alln-gated-codex-15 — Eventual global argmax at exactly the two nonnode corners

ID kind: PD-T.
Aliases: direction2 round2 assembly; sufficiently-large-degree Padua corner argmax; eventual equality and equality classification.
Split from: large-degree portion of the local/global obligation for PD-T099. The original all-degree n>=2 target is retained OPEN with an unresolved finite bridge.
Split into: none. The local bound is independently recorded in gated-codex-14.

## Statement

Use exactly the even-checkerboard Padua points and total-degree cardinal polynomials of PD-T101. There exists an integer N_* such that for every integer n>=N_*,

   max_[-1,1]^2 lambda_n=Lambda_c(n),

and its set of global maximizers is exactly

   {(-1,-1),(1,-1)} if n is even,
   {(-1,-1),(-1,1)} if n is odd.

The existence of N_* is proved. **No effective value of N_* is supplied.** This result does not certify any particular previously uncovered finite degree and does not close all-degree PD-T099.

## Definitions and assumptions

Exact real arithmetic, corrected exceptional x-mode convention and positive weights of PD-T101. Lambda_c(n) is the common value of lambda_n at the two physical nonnode corners. Its global optimality is a conclusion, not an assumption. Physical angle coordinates are(theta,phi) in[0,pi]^2 with(x,y)=(cos theta,cos phi).

## Status by part

Overall status: **PROVED**, by the finite-dependency argument below. Supplementary independent assembly review and required Claude audit remain pending at initial publication.

| Mathematical part | Status | Evidence / limits |
|---|---|---|
| Existential eventual global equality and exact two-corner equality set | PROVED | Gated-codex-11 actual-corner phase localization and gated-codex-14 strict local comparison |

Candidate disposition: retained assembly variant of original P3 / Claude-02 / fallback-04 / IDEA305. No external theorem or priority claim. PD-T099 stays OPEN, as required by this campaign's effective-threshold and finite-coverage acceptance criteria.

## Depends on

- PD-T101: finite cardinal conventions, continuity and common nonnode-corner value under the parity-valid reflection.
- Gated-codex-11: for every epsilon>0, every global maximizer, at all sufficiently large degrees, has an actual nonnode-corner phase representation with rho<epsilon. Its thresholds are non-effective.
- Gated-codex-14: for every n with log n>=10^7, lambda_n is strictly below Lambda_c on every punctured inward corner phase neighborhood0<rho<=1/64, at either nonnode corner.

The inherited proofs supporting gated-codex-11 remain at their existing scopes; this theorem neither strengthens their rates nor treats their pending Claude audit as complete.

## Proof

Continuity of a finite sum of absolute polynomial values on the compact physical square gives a nonempty global-maximizer set M_n for every n. Every z in M_n has lambda_n(z)>=Lambda_c(n), because the nonnode corners are legitimate evaluation points.

Apply gated-codex-11 with epsilon=1/64. There exists an integer N_loc such that for every n>=N_loc, every global maximizer is within inward scaled phase distance rho<1/64 of one of the two actual physical nonnode corners. This statement is uniform over all global maximizers. At a corner the physical-domain phases are inward; the parity-valid reflection transports either corner to the canonical one while preserving their magnitudes.

Choose any integer N_* at least both N_loc and ceil(exp(10^7)). Let n>=N_* and z in M_n. If its corner representation had rho>0, gated-codex-14 would give lambda_n(z)<Lambda_c(n), contradicting maximality. Therefore rho=0, so z is exactly a nonnode corner. Thus M_n is a nonempty subset of the two corners.

The x reflection for even n and y reflection for odd n preserves the node set and total-degree polynomial space, hence permutes the cardinal polynomials. It interchanges the two nonnode corners, whose values are equal to Lambda_c(n). Since at least one is a global maximizer and both have the same value, both are global maximizers. No further point can be a global maximizer by the preceding argument. This proves the value and exact equality set. QED.

## Scope and finite bridge

This closes the eventual large-degree corner-equality question as a mathematical consequence of the stated proved dependencies. It strengthens phase localization to exact equality for all sufficiently large n. The bound N_* remains non-effective through N_loc; an explicit but enormous local threshold does not make the assembled global threshold effective.

The accepted and newly developed finite certificates through16 retain their recorded scopes and audit states. They do not cover an unknown range17<=n<N_*. In particular no finite global scan or optimizer can fill that gap. All-degree PD-T099 remains OPEN in this campaign; the proof here is preserved as a separate substantive eventual theorem rather than silently narrowing the all-degree statement.

A complete all-degree proof still needs an effective global threshold with matching coverage or a direct comparison covering the remaining degrees without enumerating them. Neither is supplied. The round1 weighted-energy approach remains an independent OPEN option and is unnecessary for this eventual assembly.

## Checks and sources

No numerical computation is a premise. The logical proof uses uniform quantifiers in gated-codex-11 and the strict local comparison at both corners in gated-codex-14. Independent review should verify the normalization, the absolute regular Taylor bounds, the finite B Hessian, and the uniform localization quantifier; the present developer does not approve its own work. Required Claude audit remains pending.

## History

2026-11-02, Codex, parent-assigned gpt-6.1-sol xhigh; actual runtime metadata not independently exposed. Rules/checkpointaa1883f2fd9a837bb931ce804cb4b210c7475886, scientific source base7d308b10d946b607ae0690454f6c0103690775a4, with locally checked D1 round6/D2 round1 records. Authorized direction2 round2 only. No effective global threshold, new finite certification, shared-registry update, Git action, future-round execution or direction3 work.
