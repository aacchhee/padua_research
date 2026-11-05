# PD-N?argmax-bridge-codex-N6-01 — Fixed-t two-trace comparison fails at n2

ID kind: PD-N.
Aliases: fixed diagonal-phase endpoints; two-parallel envelope.
Split from: none; explicit operationalization of deferred IDEA-319/341.
Split into: none.

## Statement

For Gamma_s(t)=(cos((n+1)t+s),cos(nt+s)), the universal comparison

    lambda_n(Gamma_s(t)) <= max(lambda_n(Gamma_0(t)),
                                lambda_n(Gamma_pi(t)))       (C)

is false. At exactly n=2,t=s=pi/4,

    lambda_2(Gamma_0(pi/4))
      =lambda_2(Gamma_pi(pi/4))=3/2+sqrt(2)/6,
    lambda_2(Gamma_(pi/4)(pi/4))=1/3+sqrt(2),

and their difference is (5sqrt(2)-7)/6>0.

## Definitions and assumptions

Use PD-T101's even-checkerboard cardinals and weights at degree2,
with coefficient1 at mode(2,0). Gamma is defined in the companion
family verification. Exact real arithmetic. No corner-value theorem,
global maximum, approximate optimizer or external result is assumed.

## Status by part

Overall status: **PROVED**, elementary analytic proof below; independent
supplementary review and the required Claude audit are pending.

Candidate disposition: **REJECTED: refuted**, only for
`IDEA?argmax-bridge-codex-N6-01` comparison(C). Broad319/341 and PD-T099
remain OPEN. No failure of arbitrary parallel-family comparisons follows.

## Negative-result scope

Attempted mechanism: bound the complete cardinal l1 norm at Gamma_s(t)
by the larger of the two complete cardinal l1 norms at s=0/pi, with
the same t. Parameter range: one exact n2,t=s=pi/4 witness refutes a
universal assertion containing that point. Other phase maps, grouped
envelopes, signed decompositions, optimized trace suprema or finer
partitions are outside this negative statement.

## Depends on

PD-T101's corrected cardinal normalization. The companion family
verification fixes the family and shows it covers the square; no general
coverage claim is needed to prove the single exact reversal.

## Proof

At n2, in node order (j,k)=(0,0),(0,2),(1,1),(1,3),(2,0),(2,2),
the six cardinals are

    (x²+2xy+x+2y²+y-1)/6,
    (2x²-2xy+2x-2y²-y+1)/6,
    -(2x²+2y²-y-3)/3,
    -(x²-2y²+y)/3,
    (x²-2xy-x+2y²+y-1)/6,
    (2x²+2xy-2x-2y²-y+1)/6.                                (1)

They follow by direct expansion of T101; alternatively their values
are the six Kronecker vectors on the six n2 nodes, so unisolvence
identifies them independently. Let r=sqrt(2). The family points are

    Gamma_0(pi/4)=(-r/2,0),
    Gamma_pi(pi/4)=(r/2,0),
    Gamma_(pi/4)(pi/4)=(-1,-r/2).

At the first point, (1) gives respectively

    -(r+1)/12, 1/3-r/6, 2/3, -1/6, (r-1)/12, 1/3+r/6.

The signs are (-,+,+,-,+,+) because1<r<2. Their absolute sum is
3/2+r/6. At the second point the entries are permuted by
1<->5,2<->6, with3,4 fixed, so the absolute sum agrees.

At the witness point the entries are

    r/12, -r/12, -r/6, r/6, 1/3-r/4, 2/3+r/4.

Here1/3-r/4<0 because r>4/3, which follows by squaring
2>16/9. The absolute sum is1/3+r. The exact positive difference is

    (1/3+r)-(3/2+r/6)=(5r-7)/6>0,

since5r and7 are positive and (5r)²=50>49=7². This proves the claim.

## Checks

Actual supplementary command, from the repository root:

    python -B topics/padua-argmax-bridge-20261105/code/n6_two_trace_exact.py --output topics/padua-argmax-bridge-20261105/evidence/n6-two-trace.json

The checker uses only standard-library rational arithmetic and pairs
a+b sqrt(2), with sign decisions by rational square comparison. It
independently inverts the rational n2 Vandermonde, compares all36
cardinal coefficients with a separately assembled corrected T101 kernel,
and checks all18 cardinal values and the strict gap. Receipt: PASS.
The script hash, Python version, command and input head are in the
receipt. This is a developer execution, not an independent rerun.

Before the decisive point, a direct SymPy diagnostic at t=pi/3,s=pi/3
gave endpoint norms1,2 and witness23/12, hence no reversal there.
The candidate allowed another exact n2 point after an inconclusive first
point. The pi/4 witness was then evaluated exactly and frozen above.
Those diagnostics are discovery history, not premises of the proof.

## Sources, scope and open items

Internal sources only. This is not a source transfer or historical
novelty claim. Unlike N086, the obstruction uses complete cardinal
norms and requires no individual fixed signs on coarse diamonds.
No corner counterexample occurs: the witness value1/3+sqrt(2)<3,
the accepted n2 corner value. The exact all-degree argmax target remains
unaffected. A different comparison for the covering family is OPEN.

## History

2026-11-05, Codex N6 mathematics developer, parent-assigned Sol xhigh;
effective runtime metadata are not independently exposed. Rules/input
`98d6c00d8a474cf97602c9cfdea631a837191ac0`. Candidate and first exact
test were written before execution in `../ideas/N6-two-trace.md`.
