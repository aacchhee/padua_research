# T6 novelty gate and retained candidates

Rules/input SHA: `ccd9e905d19c0c625c196c4a3f3e707058ed042a`.
Developer: Codex, gpt-6.1-sol xhigh, 2026-11-06. Coordinator owns Git and
all shared records. This file precedes the executable T6 checks and durable
proof writeup. Literature survey preceded local argument development.

## Search scope and closest predecessors

The complete `state/IDEAS.md` heading/alias inventory and campaign summaries
were scanned, including the obstruction and disposition sections. Sequential
reads also covered unrelated campaign tables; tool output truncation was
addressed by smaller repeated reads and a complete heading inventory. The
task uses handoff01's relaxed scan, not exhaustive historical-priority
certification. `literature/INDEX.md` was searched before primary fulltexts.
Search terms across ideas, literature, theory and topic records were:
`lower bound`, `projection constant`, `minimal projection`, `Sündermann`,
`Sundermann`, `Lozinski`, `Kharshiladze`, `log^3`, `log³`, `tensor subspace`,
`cube`, `polyhedral`, and `simplex`.

Full shortlisted predecessor reading:

- IDEA-206's complete record in
  `topics/programme-ideas-20261031/ideas/candidates.md`: its proposed square
  lower bound at the Padua leading constant was abandoned because a
  projection argument cannot reach that constant. That limit is respected.
- IDEA-013/029/120/178/185/186 and the lattice obstruction/disposition table:
  total-degree unisolvence, correct counts, finite poor-quality fibres and
  axis factorization are different claims. No finite screen supplies this
  universal lower bound. Historical 3-D exclusion is superseded by this task.
- LIT-379 and its complete source record: bivariate Fourier/interpolation
  asymptotics, not a theorem for every 3-D interpolation set.
- LIT-488 and its complete source record: MZ inequalities for particular LC
  spectral spaces, not universal cube projection lower bounds.
- LIT-512 and its complete source record: Fourier sums over simplices;
  inherited coverage does not prove an interpolation statement.

Primary survey and exact actual coverage are in [literature-T6](literature-T6.md).
The DEKL 2017 Theorem2.3 Fourier order already covers the octahedral frequency
set. Therefore logarithmic-cubed growth is not offered as a new discovery.

## IDEA?padua-3d-20261106-codex-T6-01 — quantified even-subspace transfer

Aliases: cosine lift; translation averaging; coordinate-zero correction;
cube projection comparison.

- Question/scope: give a valid explicit factor comparing any projection
  onto total-degree algebraic polynomials with the Fourier projection onto
  the integer l1 ball.
- Mechanism/hypotheses: lift to coordinate-even torus functions, extend by
  reflection averaging, average translation conjugates, and explicitly
  correct the multiplier `2^(-number of nonzero coordinates)` by coordinate
  integration operators.
- Closest entries: IDEA-206, LIT-379/488/512; DEKL Theorem3.4 is a
  particular-node comparison, not by itself the universal operator claim.
- Separation: the local argument supplies a norm-bounded map for **every**
  bounded projection, with the full l1 Fourier support proved. It does not
  claim a sharp constant. A missing Fourier mode or an unbounded correction
  would erase this distinction.
- Literature baseline/limits: known projection/Fourier mechanism;
  literature-T6 makes no exhaustive priority claim.
- Applicable obstructions: an even cosine space is not translation
  invariant; averaging is not assumed to preserve projection. The resulting
  diagonal multiplier is calculated and corrected instead. Tensor-subspace
  containment does not transfer a projection lower bound and is unused.
- Verdict (corrected 2026-11-06, audit m6): literature duplicate, retained
  as local reproof. The same 3^(-d) comparison is attributed to Subbotin
  under the primary-reading coverage qualifier below; no novelty claim.
- Cheapest decisive test/prewritten kill: calculate the multiplier on a
  character, including zero coordinates and frequencies outside the total
  degree ball. Any mismatch kills the proposed identity.
- Discriminability: exact character equality decides the finite-rank
  operator identity after density; sampled operator norms would not.
- Result: written proof in `theory/t6-universal-lower-bound.md`; exact
  multiplier sanity checks in `code/t6_sanity.py`.
- Disposition: retained; historical novelty unresolved, not asserted.
- Canonical result: PD-T?padua-3d-20261106-codex-T6-01.
- Audit/history: developer result, independent review pending.

## IDEA?padua-3d-20261106-codex-T6-02 — explicit octahedral Fourier lower bound

Aliases: vertex facet coordinates; positive-frequency sawtooth test;
harmonic minimum-coordinate subset.

- Question/scope: replace an unspecified Fourier lower-bound constant with
  a short, fully written explicit estimate suitable for T6.
- Mechanism/hypotheses: an integer nonsingular facet-coordinate transform
  places all frequencies in the nonnegative orthant; test against the
  product of bounded sawtooth functions; retain a harmonic-weighted subset.
- Closest entries: LIT-512 and DEKL Theorem2.3 already establish the Fourier
  logarithmic order; classical polyhedral lower-bound methods are prior art.
- Separation: only the explicit elementary certificate and constant, not
  the growth order or a new general mechanism. A nonpositive transformed
  frequency, noninjective frequency map, wrong Haar normalization or absent
  subset point kills this certificate.
- Literature baseline/limits: primary theorem statement and named proof
  coverage in literature-T6; no earlier absence/priority assertion.
- Applicable obstructions: the coordinate matrix has determinant −4 in d3;
  one must use its surjective torus covering, not an incorrect ordinary
  change of variables with an extra determinant factor. The sawtooth is
  merely bounded measurable, which is sufficient for its integral against
  a finite trigonometric polynomial.
- Verdict: variant with difference in explicit local constant, no novelty
  claim. The d3 result is `||D_n||_1 >= H_floor(n/2)^3/(24*pi^3)`.
- Cheapest decisive test/prewritten kill: enumerate small octahedra exactly
  and verify transformed support, retained subset and harmonic inequality.
  Any failed inclusion or sign kills the argument.
- Discriminability: finite checks detect formula errors but do not prove
  the all-n result; that rests entirely on the written argument.
- Result: `theory/t6-fourier-lower-bound.md`, with sanity checks only.
- Disposition: retained explicit known-mechanism proof; no rejected family.
- Canonical result: PD-T?padua-3d-20261106-codex-T6-02.
- Audit/history: developer result, independent review pending.

No separate candidate was pursued for the unjustified tensor-subspace
shortcut or the claim that translation averaging alone is a projection.
They are excluded proof steps, preserved above, not new PD-N entries.

## Subsequent source refinement and final disposition

After the initial survey, gate and local proof writeup, reading DEKL's
Theorem 3.4 proof exposed equation (3.15)'s precise Subbotin attribution.
Subbotin1983's full primary text was then read. Its Theorem 1 and
Corollary 1 already contain the same `3^-d` comparison, and Corollary 3
already yields universal total-degree cube `c_d log^d n` growth. See
LIT?padua-3d-20261106-codex-T6-02 in `literature-T6.md` for hypotheses and coverage.

This supersedes any weaker description above of historical novelty as
unresolved: T6-01 is a known-result reproving certificate, and T6-02 is
an explicit known-mechanism constant certificate. No novel order, transfer
mechanism, or priority for the displayed constant is asserted. Both are
retained only for their complete local proof and useful explicit bound.


## Audit-response qualification — 2026-11-06 — m5/m6/m8/m14/m15

Audit-01 completed independent mathematical reconstruction and actual reruns;
initial pending process language is historical. The T6-01 verdict field and
the signed determinant have been corrected explicitly above. The known
logarithmic order is not novel. The Subbotin attribution relies on the
recorded developer primary read, not a second source verification: Theorem1,
Cor1/Cor3 read; Yudin input unread; Astra did not check the source; Claude
could not retrieve it. Russian original1982, English translation1983.

The prewritten decisive character test was proved analytically but the
producer did **not** implement an actual projection/translation-averaging
check: t6_sanity.py only verifies preset multiplier factors algebraically.
Its multiplier part is tautological. Audit-01's genuine projection check is
separate evidence; no new developer run of that check is claimed here.

LIT-391 (Wang–Wang–Wang 2014, reported O(log^d n) cube hyperinterpolation)
is an additional predecessor/context row. That is a redundant-node cubature
operator upper, not a matching N-node interpolation construction. The
inherited LIT row is secondary/UNVERIFIED; no source theorem is imported and
no primary fulltext read is claimed by this addendum.
