# PD-N?nn-mop-stability-codex-D6-copy — full standard-grade two-sheet obstruction

ID kind: PD-N. Aliases: two-sheet annihilator; original dictionary-obstructions C.
Split from: PD-N?nn-mop-stability-codex-D6-literal, exactly its C statement.
Split into: none.

## Statement

For every N>=1, distinct real x_l and strictly positive w1,w2, the
labelled-copy measure sigma=sum_l w_(1,l)delta_(x_l,0)+w_(2,l)delta_(x_l,1)
has singular Gram matrix on the full standard bivariate Pi_2. It cannot
directly meet PD-T057's full Pi_d positive-definiteness hypothesis for any
d>=2 without quotienting, deflation or changing representation.

## Definitions and assumptions

Pi_d is the full formal total-degree polynomial space before evaluation.
The representation has exactly two sheets y=0,1 and performs no deflation.

## Status and negative-result scope

Overall status: PROVED. Candidate disposition: REJECTED: failed, only for
the no-deflation full-Pi_d two-sheet mechanism, not positive ambient encodings.
Attempted mechanism: IDEA?nn-mop-stability-codex-D6-copies interpreted as a
full standard-grade scalar model. Parameter range: all stated finite positive
two-sheet inputs, d>=2. Other quotient, vector, graded and boundary models
remain outside this result.

## Depends on

Elementary Gram linear algebra. PD-T057 supplies the positivity hypothesis
being tested; none of its converse claims is used.

## Proof

The nonzero formal polynomial q=y^2-y belongs to Pi_2 and vanishes at every
support point. Thus <q,q>_sigma=0. Its nonzero coefficient vector is a Gram
null vector. The same polynomial belongs to every Pi_d with d>=2. This
proves the stated singularity and no broader impossibility.

## Checks and sources

The four-node Fraction diagnostic is in code/dictionary_probe.py and
attempts/D6.md. Completed separate checks: independent-checks-01.md;
Claude's independent exact reconstruction: audit-01.md, priority9. The
finite rank5-of6 observation is MEASURED support, not a proof premise.

## Scope and open items

The positive selector identities remain valid. The full recurrence/stability
transfer remains OPEN in dictionary-target.md and its copy/pair sub-target
dictionary-lifts.md. No blanket bivariate no-go or stable-solver claim follows.

## History

The original C statement and proof appeared in dictionary-obstructions.md
at4e87fc0a771fc13c6d5791f0f4c2e746e4eb9a71. Split without mathematical
change for audit-01 MINOR3, 2026-11-06, Codex requested gpt-6.1-sol high.
