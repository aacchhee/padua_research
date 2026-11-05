# N3 enclosure specification (implementation lemma, review pending)

ID kind: none assigned. Aliases: whole-sum mean-value; nonsmooth sign hull.
Split from/into: none. This implements PD-T364 rather than replacing it.

## Statement and definitions

For a phase rectangle B with center c and radii r_a,r_b, let each smooth
primitive term h_i have an enclosure H_i containing h_i(B), center enclosure
C_i containing h_i(c), and gradient intervals A_i,B_i. Define a derivative
interval D(H,A) by A if H>0, -A if H<0, and
[-maxabs(A),maxabs(A)] otherwise. Then a sufficient upper enclosure is

    sum_i maxabs(C_i)
       + r_a maxabs(sum_i D(H_i,A_i))
       + r_b maxabs(sum_i D(H_i,B_i)).

Take the minimum with sum_i maxabs(H_i). Apply appropriate positive
normalization 1/(2n(n+1)) for S and 1/(8n(n+1)) for the corner orbit.
For the latter, each h_i is the sum of the four reflected G values; its
value, center value and derivatives are summed before D or absolute values.

## Assumptions and status

Exact or outward enclosures, smooth primitive h_i and finite sums.
Overall phase-cover target: OPEN. The displayed routine enclosure derivation
is written for review; executable v1 is float-only and does not fulfill its
arithmetic assumptions. No new registered theorem or accepted degree follows.

## Derivation

Along the line c+t(x-c), |h_i| is absolutely continuous. At every point with
h_i nonzero its derivative is sign(h_i) times the smooth derivative. At zeros
the absolute-value Lipschitz inequality gives the symmetric derivative hull;
equivalently use a.e. chain derivatives and integrate. These derivative values
lie in D(H_i,A_i) and D(H_i,B_i). Sum before bounding the line integral, then
use |x_a-c_a|<=r_a and |x_b-c_b|<=r_b. The natural interval upper bound is
independently valid, so their minimum remains valid. This avoids assuming
sign stability where H_i contains zero. A zero center value does not remove
the term's derivative contribution.

## Implementation and scope

`../code/n3_meanvalue.c` differentiates the finite kernel identity in PD-T364.
R_k'(x) is evaluated by a differentiated sine quotient away from its zeros;
near zeros it uses the finite sum
R_k(x)=sum_{j=0}^{k-1} cos((k-1-2j)x), including all collision points.
The variable derivatives are divided by n and n+1 for the phase chart.
The exact same physical local radius max(1/(2[n(n+1)]^3),10^-11/n²) from
PD-T251/369 is retained; no new true-sign radius is asserted.

The float driver uses a numerical safety budget only as a diagnostic. Its
libm functions, point centers, interval endpoints and arithmetic are not
outward rounded. An outward implementation and an independent checker are
unresolved. PD-T210 and PD-T364 are the sole acceptance reductions; finite
checks cannot replace their assumptions. No external source is transferred.

History: 2026-11-05, Codex Sol medium implementation worker; rules/input
98d6c00d8a474cf97602c9cfdea631a837191ac0. Independent review pending.
