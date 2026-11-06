# IDEA?argmax-bridge-codex-N5-04 — Two-phase defect near every interior vertical-edge center

Aliases: N5 round4; radius-half projected vertical defect; shifted middle
lines; inward vertical-edge charts; exceptional cos(alpha) correction.

## Preregistration — 2026-11-06, before numerical work

- Question / scope: for every integer n>=64, m=n+1, J in {0,n}, and
  integer 1<=q<=m-1 with J+q odd, does the actual Lebesgue function obey

      lambda_n(cos theta,cos phi) < S_n(alpha,beta)-1/2048,
      theta=(J*pi+alpha)/n, phi=(q*pi+beta)/m,
      |alpha|+|beta|<=1/2, 0<=theta<=pi?                 (C)

  Thus alpha>=0 at J=0 and alpha<=0 at J=n. Both beta signs are
  admissible. Corner centers q=0,m are explicitly excluded; their
  zero-phase defect is zero. No independently optimized phase ordering
  or primitive maximum is part of (C).
- Mechanism and hypotheses: use the exact projected four-copy vertical
  defect Q_v<=Delta and the physical/periodic weight 1/[n(n+1)]. Retain
  the corrected highest x mode. If P_n=T_(n+1)+T_n and
  D_n(x,y)=[P_n(x)-P_n(y)]/(x-y), continued polynomially, define

      H_r(u,v)=[(-1)^r D_n(cos u,cos v)-cos alpha]/2,
      u=(r*pi+alpha)/n, v=((q +/- k)*pi+beta)/m,
      r+k=J mod 2.

  The subtraction is cos(alpha), not 1 and not cos(beta). The two
  regular half numerators must equal

      a*(1+cos v)-(sin alpha/2)*sin u+(sin beta/2)*sin v,
      a=(cos alpha+cos beta)/2.

  All total identities retain polynomial collisions. Selected lower
  blocks must be collision-free. Shift the N5-03 endpoint middle lines
  with alpha and reconstruct the adaptive far rectangles with the
  periodic first grid; the physical-edge factor 2 must not be imported.
- Closest entries read in full: N5-03 and N5-02; PD-T215, PD-T219,
  PD-T222, PD-T366; IDEA-318, IDEA-327/328/330 and IDEA-459 including
  their original linked candidate records. N5-01 and the distinct
  N5-03 supplement were read. PD-T224 is the finite-line predecessor
  cited inside T366; its complete proof is read before proof development.
- Separation criterion: T366 has both varying phases but only radius
  1/10 and loss 1/8192; N5-03 has radius 1/2 and loss 1/1024 but
  alpha=0. The exact distinction is radius 1/2 with both phases varying,
  all stated interior vertical-edge centers, and loss 1/2048. A matching
  existing theorem would erase it; an excluded sign/weight or missing
  cos(alpha) correction would kill this implementation.
- Literature baseline and limits: bounded repository comparison only.
  The literature INDEX warning was read; no external fulltext, source
  theorem transfer or historical originality claim. Existing N5 source
  access limits remain in ../literature-N5.md.
- Applicable obstructions: IDEA-318's ambiguous ordering, E-P's precise
  reversed translation, IDEA-330's corner energy obligation, and
  IDEA-459's missing interior profile concern different comparisons.
  Positive Q_v does not bound S_n itself. Primitive-cusp and leading-only
  profile obstructions remain intact. Constant positivity at actual
  nonnode corner centers is impossible at zero phase, so they stay out.
- Novelty verdict: **quantitative variant with difference**, conditional
  on the stated enlarged phase domain surviving. No new mechanism.
- Cheapest decisive test: selected n=64,65, both J, q nearest 1, m/2,
  m-1 with the required parity, phases on the alpha/beta axes at
  magnitude 1/2 and mixed inward alpha of magnitude 1/4 with
  beta=+/-1/4. Check the corrected polynomial recurrence against the
  numerator identity and actual selected projected defects. Do not fit
  or scan degrees.
- Kill criterion written before testing: one genuine counterexample to
  (C), duplicate theorem, sign/count failure of the proposed uniform
  selected blocks, or loss of 1/2048 after the correct periodic weight
  stops this bounded candidate. Record the obstruction; no cosmetic
  smaller radius or weaker constant in this round.
- Test discriminability: recurrence/quotient mismatch exposes the
  exceptional-mode error; selected-block deficits test the proposed
  uniform geometry. Finite successes do not prove all degrees/phases.
  A surviving candidate requires an analytic count/numerator proof.
- Resource ledger: bounded representative diagnostics only; small receipt
  below 16KiB and optional bulk outside Git, within AC's temporary 10MB
  aggregate generated-output allowance. No round5 or major cleanup.
- Actual result: not run at preregistration.
- Disposition: candidate OPEN at preregistration.
- Canonical theory: assigned only if a substantive proof or obstruction
  results; parent alone integrates shared records and Git.
- History: parent-assigned Codex mathematical developer; inherited serving
  model/effort, runtime metadata unexposed; rules/input
  3888dd37c362a0689943f33e6b7e44c1dd1c3050. Parent supplied (C) as a
  target to test, not a theorem.

## First diagnostic and bounded coverage addendum — before the second run

The first 72 cases passed at 80 decimal digits in 11.2543 CPU seconds.
Minimum selected/case-floor ratio 17.8836387471; maximum recurrence versus
quotient difference 2.11856009867e-77; minimum full actual S-lambda
0.523048574748. These are MEASURED diagnostics. The first representative
set exercised 48 near and 24 middle cases; it left the small-angle
selection and the exact gamma=pi/6 transition unexercised.

Before a second run, add only q5 at (n,J)=(64,0), q11/55 at (65,0),
and q4/6/62 at (65,65), with the same six phase points. These 36
additional cases cover the a4/a5 change, both sine orientations, the
missing far-small block, and both sides of gamma=pi/6. No new theorem
or weaker target is introduced. Preserve the first source identity,
receipt and raw output in local output, then run the changed final source
once on the resulting 108-case bounded set.

## Frozen outcome

The 108-case run passes: 60 near, 20 small, 28 middle cases, including
the a4/a5 and gamma=pi/6 controls. Minimum selected/case-floor ratio
11.8382054814; maximum polynomial/quotient discrepancy
2.11856009867e-77; minimum actual S-lambda 0.523048574748.
See the [small receipt](../evidence/n5-two-phase-defect.json).
The samples remain MEASURED. The separate uniform analytic developer
theorem is [N5-04](../theory/N5-two-phase-defect.md), with (C) PROVED
at its original quantifiers and the N1-model margin 255/524288.

Disposition: **retained quantitative variant**, no rejection or PD-N.
The proof uses the inherited finite lines/moving rectangles; no new
ordering or profile mechanism is claimed. Alternative unchanged edge
normalization 2/N and subtraction 1 are abandoned incorrect
transcriptions, caught by formula reconstruction before testing rather
than tested mechanisms or separate negative results. Full-square center
coverage, corner charts, primitive/model maximization and E-C remain
outside this bounded candidate. Stop after this round4 result.
