# PD-T?lattice-c0-codex-03 — Finite cardinality catalogue for potentially unisolvent single fibers

Final ID: **PD-T083** (allocated 2026-11-01 under AC's authorisation; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-T. Aliases: C0 finite exact-count screen; small modulus catalogue.
Split from: none. Split into: analytic density PD-T?lattice-c0-codex-01 and infinite diagonal counts PD-T?lattice-c0-codex-02 are separate statements, not parts of this finite computation.

## Statement

Within the frozen scope of C0/frozen-scope.md, the developer execution found5061 canonical primitive nonzero-coefficient fibers (representing77616 raw tuples), with451 meeting `|S|=binom(n+d,d)`:39 in d2 and412 in d3. By n=1,...,6, the d2 totals are23,8,4,1,2,1; the d3 totals are119,68,78,45,56,46. Every admissible representative and its explicit unit/reversal/equal-length-permutation aliases is in C0/catalogue.json; every canonical failure is in C0/count-trials.json. These counts describe cardinality-admissible tuples, not unisolvent patterns.

## Definitions and assumptions

Scope: d2/d3,n1..6,k2..6, single fibers with a_j in1..k-1 and gcd(k,a_1,...,a_d)=1, index lengths1..n+3. Tuples with any L_j<=n are analytically excluded as universally nonunisolvent under PD-N?lattice-c0-codex-01 and are not individually counted here. Remaining lengths are sorted n+1..n+3. Characters with zero coefficients and coset unions are excluded/deferred, not silently treated as absent. Each row of count-trials.json is a retained parameter-specific candidate under C0/candidates.md's inheritance convention.

## Status by part

Overall status: MEASURED (exact arithmetic finite developer run; independent rerun/completeness audit pending). No probabilistic or generic-rank assertion.

Candidate / claim disposition: cardinality failures REJECTED: failed only as exact minimal-node candidates for the row's parameters; survivors sent to C3. The finite catalogue's audit/acceptance remains pending.

## Depends on

The scope pre-screen uses PD-N?lattice-c0-codex-01. Exact integer count and group actions are elementary; no literature/charter theorem used.

## Algorithm and finite reduction

Every allowed sorted length vector is a combination with replacement of n+1,n+2,n+3; every k,a,c in the explicit ranges is iterated. Unit multiplication sends `(a,c)` to `(u*a,u*c)` and defines the same fiber. Reversing axes in J sends `a_j` to `-a_j` for j in J and sends c to `c-sum_(j in J) a_j*(L_j-1)`; it bijects the index box. Permuting axes of equal length also bijects the box. These actions generate a finite orbit, so keeping its lexicographic minimum loses no count class. Sorted length vectors additionally identify arbitrary coordinate permutations. The checker records each admitted orbit explicitly and verifies raw coverage by accumulating all orbit members.

For each axis, the exact residue histogram is

`h_j(s)=sum_(0<=r<k, a_j*r=s modk) (floor(L_j/k)+1_(r<L_j modk))`.

Starting with the point mass at0, convolve these histograms cyclically modulo k. The c entry equals exactly the number of allowed index tuples by partitioning every tuple by its axis residues. The checker verifies each canonical tuple's computed count independently by direct enumeration of all Cartesian-product points, and checks every orbit member's histogram count. This proves the reduction to exact finite integer checks. A computer-assisted PROVED classification additionally needs the independent replay and audited completeness, so the present recorded status remains MEASURED.

## Checks

Actual command: `python tracks/lattice-unisolvence/code/c0_catalogue.py --output-dir topics/lattice-unisolvence-20261031/directions/C0`.

Developer run used Python3.12.14 on this managed Linux workspace, source/rules SHA e949ef06895acd5463cdf8df7e0e5f795218f70f; source file SHA-256 and output hashes are in C0/rounds.md. No seed: enumeration is deterministic. Source is `tracks/lattice-unisolvence/code/c0_catalogue.py`; inputs are its frozen constants and C0/frozen-scope.md. Outputs are the three small JSON files. All assertions passed. The convolution/direct-enumeration checks are two implementations within this same developer run; they are not an independent agent rerun. Independent Astra reconstruction pending.

## Sources, scope and open items

Baseline C0/candidates.md records complete registry reading and bounded repository predecessor search. No novelty claim. Property(a) periodic yes; property(b) axis factorization/structural unisolvence criterion unknown for every survivor here; property(c) Lebesgue growth unknown. C3 independently supplies exact ranks and any annihilators; a count failure is not a universal determinant obstruction. Beyond the finite scope, nothing is claimed except the separate analytic statements. Runs needed: independent rerun into a separate directory plus comparison, and C3 ranks over its frozen primes/axes.

## History

2026-10-31, Codex assigned gpt-6.1-sol xhigh. Frozen scope preceded code and run. No independent audit or public novelty acceptance is implied.

## Audit history addendum — 2026-11-01

The pre-acceptance pending wording above is historical. Supplementary [Astra reconstruction](../../../topics/lattice-unisolvence-20261031/independent/report.md) completed, and [Claude audit-01](../../../topics/lattice-unisolvence-20261031/audit-01.md) accepted this exact existing statement and epistemic status. [Response-01](../../../topics/lattice-unisolvence-20261031/response-01.md) changes audit/integration metadata only; no proof, hypothesis, status or finite observation is upgraded. Literature/novelty gaps remain unresolved where stated. Codex administrative response, requested gpt-6.1-sol high; runtime metadata unexposed.
