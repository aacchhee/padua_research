# T1 novelty gate and retained candidates

2026-11-06. Codex mathematical worker; assigned gpt-6.1-sol xhigh;
runtime-resolved metadata unexposed. Rules/input SHA
`ccd9e905d19c0c625c196c4a3f3e707058ed042a`. No shared registry or Git ownership.
D0/D1 PASS was communicated by the coordinator before this work.

## Gate

Read the topic BRIEF, plan and handoff; scanned the complete IDEAS registry
headings/identifiers/aliases and read its obstruction/disposition material.
Read the literature index and the relevant inherited source records, including
their explicit partial/secondary-reading limits. Searched ideas, topics,
tracks and literature for subgroup, coset, character, annihilator, reflection,
parity, short axis, total degree, cubature, Li–Sun–Xu and Lissajous.
Shortlist: IDEA-013/029/120/178–189; especially IDEA-179/PD-N032,
IDEA-181 (coset unions), IDEA-185/186, PD-T081/091, and PD-T106's actual
cosine-alias proof. Full C0/C3 candidate records and the corresponding
short-axis/density/annihilator/alias theory were inspected. Existing finite
mod-6 catalogues concern arbitrary labelled grid fibres and do not assert
that their torus lifts are stable under coordinate reflections.

The new proposed scope is an elementary classification of **reflection-stable
torus cosets**, followed by a cardinality obstruction using its binary code.
It is a variant of standard character duality and coordinate annihilators;
no publication-priority or historical novelty claim is made. Dencker–Erb's
parity-index constructions are a close source comparison. The local result
must not reject their different spectral interpolation spaces. The
Li–Sun–Xu bound is conjectural and is not a proof premise.

## IDEA?padua-3d-20261106-codex-T1-01 — reflection-stable single coset

Aliases: binary annihilator code; parity coupling; reflection folding.

- Question / scope: exclude minimal-cardinality total-degree interpolation
  for a single coordinate-reflection-invariant finite subgroup coset in T^3.
- Mechanism and hypotheses: classify its annihilator and translations;
  use short coordinate projections and explicit Chebyshev aliases, then
  count folded nodes exactly. No cubature or weights assumed.
- Closest entries: the shortlist above; standard short-axis PD-N032 and
  parity aliases PD-T106; Dencker–Erb parity spaces as source comparison.
- Separation criterion: arbitrary finite subgroup orders, no fixed modulus
  or consecutive-grid-size hypothesis, but reflection invariance of the
  coset itself. An inherited theorem with the identical class and all-degree
  obstruction would erase a possible distinction; none is claimed yet.
- Literature baseline / limits: source records are coverage-qualified;
  direct source comparison remains in literature-T1.md. No exhaustive
  priority search or source-proof inheritance.
- Applicable obstructions: a short coordinate projection kills injectivity;
  pair aliases kill it when their maximal degree is <=n. Escape: neither
  condition alone suffices, so use the remaining count.
- Verdict: variant with explicit class difference, no novelty claim.
- Cheapest decisive test: classify binary subspaces in dimensions 2 and 3;
  verify Padua survives and search exact finite cosets for a counterexample.
- Kill criterion, before enumeration: an invariant coset outside the code
  classification, an incorrect folded count, or a minimal-cardinality
  injective n>=2 example invalidates the respective proposed conclusion.
- Discriminability: finite enumeration checks its entire declared finite
  universe; the all-order theorem needs a separate written proof.
- Actual results: classification and restricted all-n>=2 obstruction
  proved in the owned theory files; exact finite D3 diagnostic PASS at
  20,304 3D cosets and 450 2D cosets, with separate Padua n=1..10 sanity.
  The pre-run checkpoint above preceded execution; actual command and
  result are in attempts/T1.md and evidence/t1-reflection-enum.json.
- Disposition: retained/successful obstruction route; the minimal-node
  construction within this class fails. No broader target is rejected.
- Canonical theory: PD-T?padua-3d-20261106-codex-T1-01 (classification),
  PD-N?padua-3d-20261106-codex-T1-01 (obstruction).

## IDEA?padua-3d-20261106-codex-T1-02 — unrestricted C_k obstruction

Aliases: arbitrary coset phases; unions of cosets; near-minimal cubature.

- Question / scope: the original handoff's C_k with arbitrary finite H,
  arbitrary translations, fixed k, and orthogonality/positive cubature.
- Mechanism: first test whether the reflection classification applies.
- Closest entries: IDEA-029/120/181; Li–Sun–Xu conjectural counting; T1-01.
- Separation / falsifier: removing reflection invariance requires a genuine
  additional argument; treating a reflection saturation as a subgroup is
  invalid. A sign-unstable cyclic subgroup already kills that shortcut.
- Literature baseline / limits: LSX is conjectural; general cubature and
  lattice literature require exact-hypothesis/fulltext checks.
- Applicable obstructions: T1-01 only when the **whole single coset** is
  reflection invariant. A union is not automatically in that class.
- Verdict: deferred broader target, no new mechanism asserted.
- Cheapest test / prewritten kill: check closure after reflection for one
  mod-6 fibre. Failure kills only the classification shortcut.
- Discriminability: the class boundary is logical, not an asymptotic fit.
- Actual results: original target remains OPEN; no cubature nonexistence is
  inferred from the LSX conjecture or from T1-01's narrower result.
- Disposition: deferred until a separate valid argument is available.
- Canonical theory: t1-open-class.md.

## Audit-response predecessor addendum — 2026-11-06 — M1

The earlier shortlist missed the nearest published comparator. Read the
existing full DMVX source record (LIT-322/306), the Xu-1994 record including
its d=3 addenda (LIT-374), Cools–Poppe record (LIT-381), IDEA-109 and
OBST?bivariate-lanczos-claude-11. Primary coverage is inherited and bounded,
as stated in [literature-T1.md](literature-T1.md); no new source fulltext
reading is claimed by this response.

- **DMVX 2009:** its union of two all-parities-equal Lobatto subgrids is
  c(H), where H consists of i_j modulo 2m_j with all three parities equal.
  This is the B=span(110,101) member of T1's reflection classification.
  The parity condition is closed under addition and each coordinate
  negation, so the inclusion is direct. DMVX p.7 already says its
  hyperinterpolation "is not interpolation" because it has too many nodes.
  T1 treats every classified code/order/allowed translate, rather than
  just this published grid, and excludes minimal Π_n injectivity without
  a cubature premise. This scope difference is not a historical novelty claim.
- **Xu 1994 / IDEA-109 / OBST-11 / LIT-374:** the single-Γ Gaussian
  construction and degree-(2n−2) criterion concern a particular cubature
  system; the reported d=3,n=3 unsuccessful Γ search/author expectation
  is not an all-coset interpolation obstruction. The product second-kind
  weight there is distinct from T1's optional first-kind product-cubature
  conjunct. No source nonexistence theorem is imported.
- **Cools–Poppe / LIT-381:** rank-one Chebyshev/blending lattices and their
  reported 1.5–2.4× dimension counts are close predecessors, not a universal
  minimal interpolation lower bound; T1's class hypothesis must still be
  checked for each construction. Cubature/hyperinterpolation and Π_n
  interpolation remain distinct targets.

Closest-entry fields for T1-01/02 now include these records. Verdict remains
variant of known mechanisms with historical novelty unestablished. The
cheapest separation test is exact class membership and matching the source
statement's quantifiers, not a new numerical search. A predecessor giving
the complete same classification/quantifiers would erase the possible scope
distinction. No structural-note or publishability claim is authorized by
this comparison. The original broader C_k target remains OPEN.
