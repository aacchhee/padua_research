<a id="pd-tlanczos-nonproduct-codex-p2-03--exact-finite-uniform-disk-creator-probe"></a>

# PD-T476 — exact finite uniform-disk creator probe

Provisional alias: `PD-T?lanczos-nonproduct-codex-P2-03`.

ID kind: PD-T.
Aliases: μ0 disk degree8; restricted final-block impulse; no capacity closure inferred.
Split from: P2 continuous disk candidate; its full capacity-rate target remains OPEN.
Split into: none.

## Statement

For μ=0, the exact rational moment reconstruction in
[p2_disk_probe.py](../code/p2_disk_probe.py) produced positive monic norms,
pairwise orthogonality and correct full-projection creator identities for
all 45 graded-lex columns through degree8, for BJ, mirror and alt. The
finite-scope quantities reported below were obtained for degrees2–8.
These are exact-arithmetic measurements, not an all-degree claim or a
certified computer proof.

## Definitions

At target (r,j), n=r+j, BJ chooses x if j=0 and y otherwise; mirror
chooses x if r>0 and y otherwise; alt chooses x if j=0 or (r>0 and
j<n/2), and y otherwise. The parent is respectively (r-1,j) or (r,j-1).
The monic creator coefficients are

    alpha_kl=<a_k b_parent(k), b_l>/d_l,     l<k,
    b_k=a_k b_parent(k)-Σ_(l<k)alpha_kl b_l,
    d_k=||b_k||²,   sigma_k²=||a_k b_parent(k)||².

The reported largest same-degree normalized transfer squared is

    max_(k,l in degree n, l<k) alpha_kl² d_l/d_k,

where the maximum is zero if no such nonzero coefficient exists. An edge
count is the number of nonzero same-degree coefficients, not the number
of independent source responses and not a norm of the normal quotient.

For each completed degree n, let h=(n,0), set t_h=1 and, for subsequent
columns k in that same degree, recursively set

    t_k=-Σ_(l in degree n, l<k)alpha_kl t_l.

The reported first-final-source gain squared is

    G_n²=sigma_h² Σ_(k in degree n)t_k²/d_k.              (1)

It is a restricted lower witness for the full capacity in PD-T483's
continuous arbitrary-L² model, as explained below. It is not the full
capacity, a full-capacity upper bound, or a BJ/comparator capacity ratio.

## Assumptions

Uniform probability measure on the disk, μ=0; fixed graded-lex order and
parent rules above; full projection; positive monic normalization;
relative raw-product source budget. This computation does not use the
D36x9 grid for its disk moments. The grid checks in its receipt are
separate admission implementation checks.

## Status by part

Overall status: MEASURED (one finite exact-arithmetic reconstruction).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Disk orthogonality and creator checks through8 | MEASURED | Fraction assertions and compact receipt |
| Reported finite same-degree transfers and G_n² | MEASURED | Exact rational outputs below |

The all-source capacity recursion/rate is the separate OPEN parent target
in [IDEA-573](../ideas/P2.md#idea-573--continuous-radial-disk-quotient),
not a mathematical part of this MEASURED probe. It is not computed or
implied by these quantities.

Candidate disposition: finite structural check retained. The proposed
shortcut from sparse basis recurrence to N3 capacity closure is not
pursued; this is a limit of the attempted route, not a refutation of any
bounded-order recursion that might later be found.

## Depends on

PD-T474's exact disk moment formula and positive polynomial form; PD-T482
and PD-T483 supply the relative raw-product normal-capacity model. PD-T475's
analytic covariance proof is separate and does not depend on this run.

## Checks

Frozen executed command, from repository root:

    python3 -B topics/padua-lanczos-nonproduct-20261105/code/p2_disk_probe.py --degree 8 --output /tmp/padua-lanczos-nonproduct-20261105/p2-disk-probe-full.json > topics/padua-lanczos-nonproduct-20261105/evidence/p2-disk-probe.json

Exit status 0. The full scratch JSON is 66,663 bytes and has SHA256
`6909c27f62626fe820846ace4a61f666d19ea16d944ede44cab0c64e3f990667`.
The producer SHA256 at execution is
`6588dfa56a4942d31ff053ee92588fea0939559b56c6de69db0381117284b652`.
The committed [compact receipt](../evidence/p2-disk-probe.json) contains
all table quantities, the degree-two basis and the exact grid checksum.
The full report remains regenerable scratch, not cold-storage evidence.
No independent replay, audit or second arithmetic implementation is
claimed. Its execution timing is recorded once in attempts/P2.md.

## Sources

No unread literature formula is used. The exact moment formula is
analytically proved in PD-T474; finite Gram–Schmidt is reconstructed from it.

## Proof or evidence

The producer uses standard-library Fraction throughout result-bearing
arithmetic. It constructs the monic basis directly from moments, checks
all pairwise inner products and positive norms, and independently
reconstructs each creator residual using each rule's parent. It then
solves the finite triangular system defining (1).

| n | BJ G_n² | mirror G_n² | alt G_n² | max same-degree transfer², BJ / mirror / alt |
|---|---|---|---|---|
| 2 | 9/4 | 9/4 | 9/4 | 1/8 / 1/8 / 1/8 |
| 3 | 5/2 | 2 | 5/2 | 1/4 / 4/81 / 1/4 |
| 4 | 175/64 | 2 | 175/64 | 5/14 / 9/320 / 5/14 |
| 5 | 189/64 | 2 | 2 | 25/56 / 16/875 / 14/81 |
| 6 | 1617/512 | 2 | 2 | 25/48 / 25/1944 / 56/243 |
| 7 | 429/128 | 2 | 2 | 7/12 / 36/3773 / 27/176 |
| 8 | 57915/16384 | 2 | 2 | 7/11 / 49/6656 / 81/416 |

The measured same-degree edge counts at n=2,…,8 are respectively

    BJ:      1,2,3,4,5,6,7;
    mirror:  1,1,1,1,1,1,1;
    alt:     1,2,3,3,4,4,5.

For clarity about the witness interpretation, choose a unit vector
e∈Π_n^⊥ and inject f_h=sigma_h e at h=(n,0), with every other source
zero. Earlier responses vanish. Each creator's parent has degree n-1,
so no coordinate multiplication of an already perturbed parent occurs
within the final degree block. The frozen final-block responses are
therefore sigma_h t_k e. PD-T483's normal quotient retains e, and its output
matrix has rank one with squared spectral norm (1). Thus a correct value
of (1) is a lower witness. This elementary interpretation does not certify
the table independently of the producer. It also explains why the table
does not involve a finite-node leverage factor.

The full all-source quotient includes earlier source injections and
coordinate-dependent transfer polynomials. Norms of individual edges and
one final-block response omit interactions among those sources. They
cannot be substituted for max_support||C_s(z)||₂ from PD-T483.

## Scope

Only μ=0 and degrees2–8 are measured. No asymptotic fit is made. All
reported individual same-degree normalized transfers are below one,
which alone implies neither stability nor instability of the aggregate
normal quotient. The BJ final-block witness increases over this finite
range, but no exponential rate or comparison of full capacities follows.
The finite-grid N2 scan belongs to P6 and concerns a different measure.

## Open items

N3's bounded-order capacity recursion was not obtained by degree8.
Accordingly the P2 direct all-degree route is redirected to P4's
structural criterion route, with these exact moments and sparse measured
creator rows as family data. The main P2 rate target remains OPEN. N2
cross-family tests are still required; no all-degree P2 capacity theorem
has been attempted. Independent replay and mathematical audit remain
needed before upgrading consequential computations.

## History

- 2026-11-05: finite run in Round1's original cheap identity-check scope;
  interpretation in Round2 after pushed checkpoint `7e56471`. Codex P2
  developer, assigned gpt-6.1-sol xhigh, serving metadata unexposed.
