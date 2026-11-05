# PD-T?padua-argmax-bridge-20261105-codex-corner-02 — Pending finite corner bounds at n33/64/128

ID kind: PD-T. Aliases: N3 actual outward weighted energy; practical corner endpoint data.
Split from: none; finite implementation of IDEA-330/457.
Split into: the analytic radius implication is in N3-corner-radius-reduction.md.

## Statement

For each n in {33,64,128}, the exact rational ell,E,u,kappa in
`../evidence/n3-corner-bounds.json`, under `runs[].certificate`, satisfy

    0<ell<=Lambda_c, W_n<=E, Lambda_n<=u,
    kappa=min(1,1/[8(E/(n^4 ell)+3u/ell)]) > 1/12500.

Consequently the preceding analytic reduction would give strict local
descent with loss n^2 Lambda_c H/16 for 0<H<=1/(12500 n^2), and at
both parity-correct nonnode corners. It would cover the symmetric scaled
phase square |alpha|,|beta|<=1/128 by sin(t)^2<=t^2.

## Definitions and assumptions

Use exactly PD-T227's even checkerboard and physical gradients; m=n+1.
Only k=0,j>0 even is omitted from W, while 00 is retained. E is an
upper bound on sum V(q_x^2+q_y^2), not on a different gradient energy.
Trusted numerical dependencies: correctly rounded MPFR 4.2.2 pi/cos and
basic arithmetic; GMP 6.3.0 exact rational conversion/assembly; compiler
and execution environment. These dependencies are explicit even after replay.

## Status by part

Overall status: **CONDITIONAL**, pending independent exact/outward replay
of the finite endpoint inequalities. The producer completed and the
developer's diagnostics passed; neither is an independent acceptance.
The analytic implication is separately PROVED and uses no computed premise.

| Part | Status | Evidence / gap |
|---|---|---|
| Bounds ell<=Lambda_c and W_n<=E for the three degrees | CONDITIONAL | Directed producer output frozen; distinct replay pending |
| Exact rational kappa assembly and phase-radius inequality | Developer verification record | Fraction checks passed; does not independently verify energy |
| Small n2–8 direct corrected-kernel comparison | MEASURED diagnostic only | 145 nonzero cardinals, maximum relative midpoint error <9.4e-75 |

Candidate disposition: retained quantitative implementation; no new
mathematical mechanism or priority claim. No full-degree/global certificate.

## Depends on

PD-T227 exact values/gradients/mask, PD-T251 slopes, PD-T368 global
norm bound, and N3-corner-radius-reduction.md for local-radius assembly.

## Finite reduction and outward algorithm

`../code/n3_corner_bounds.c` builds cosine intervals for a_j,b_k from
directed pi and cos. The endpoints 1,-1 and midpoint 0 are exact.
For interior angles the code guards 0<angle_lo<=angle_hi<pi_lo;
cosine decreases throughout, so [cos(angle_hi) down,cos(angle_lo) up]
contains the exact node coordinate. All interval operations use directed
rounding at every endpoint, with four endpoint products for multiplication,
sign-sensitive squaring, and reciprocal intervals only when zero is excluded.
Aliasing is handled through temporaries.

At regular nonzero indices put C=1-b, d=b-a, V=2wC/|d|. The code
requires the correct denominator sign, known exactly from m*j-n*k.
It evaluates the normalized PD-T227 expressions

    q_x=-n^2/2+n(ab-1)/(Cd)-a/d+2(1-a^2)/d^2,
    q_y=-m^2/2+n(ab-1)/(Cd)+(1+2b)/d+2(1-b^2)/d^2.

For 00 it instead uses V=1/m, q_x=-(2n^2+1)/6 and
q_y=-m(2n+1)/6, exactly the removable formulas after division by L_00.
Thus each exact nonzero energy is contained in V(q_x^2+q_y^2).
Summation gives intervals containing Lambda_c and W_n. The lower corner
and upper energy endpoints are converted to exact rationals by mpfr_get_q.
The optional term CSV is bulk diagnostic output, not part of the claim.

Choose u=110(1+c)^2 with c the least integer such that 2^c>=n+1.
PD-T368 and log 2<1 prove Lambda_n<=u. GMP assembles b,K,kappa,H
exactly. The dyadic symmetric phase radius is rounded downward with an
integer square root, then the collector checks its defining rational
inequality. This reduction uses O(n^2) formula evaluations and O(n)
stored node intervals; no full cardinal power-polynomial construction.

## Computed observations (decimal diagnostics only)

All exact rational endpoints are in the receipt; these rounded decimals
are not the endpoints used for proof predicates.

| n | ell (approx.) | E/(n^4 ell) | kappa | H radius | phase r | CPU seconds |
|---|---:|---:|---:|---:|---:|---:|
| 33 | 11.11752328 | 0.305924896 | 8.59244385e-5 | 7.89021474e-8 | 0.009406847 | 0.0081 |
| 64 | 13.97320781 | 0.317614160 | 8.26839023e-5 | 2.01864996e-8 | 0.009163283 | 0.0370 |
| 128 | 17.34605680 | 0.330384369 | 8.10996008e-5 | 4.94992681e-9 | 0.009040504 | 0.1195 |

Compared with max(1/[2(n(n+1))^3],10^-11/n^2), the respective candidate
physical-radius gains are approximately 222.89,2906.50,44568.48.
The old and new loss estimates each remain confined to their own domains.
No throughput/box-count benefit has yet been measured for the new radius.

## Checks, reproducibility and sources

Reproduction and actual execution details: `../attempts/N3-corner.md`.
The receipt pins code hashes, exact commands, runtime versions, header,
binary and raw-output identities. Committed evidence is 10114 bytes;
bulk output remains local. The numerical diagnostic implements the direct
corrected Chebyshev coefficient kernel and physical endpoint derivatives
at n2–8, without the quotient formulas. It is not outward arithmetic.
No external source theorem is transferred.

## Scope and open items

Independent replay must reconstruct the corner mass and energy through a
separately implemented exact/outward arithmetic path and verify the exact
endpoint inequalities. Code inspection and reading this receipt are not
a replay. Parent coordinates that work; this developer shares no arithmetic
kernel with the checker. Until it passes, use of the larger radius in
floating covers must be explicitly hypothetical. A full cover, B2 verdict,
required Claude audit and all-degree PD-T099 remain separate and unresolved.

## History

2026-11-05, Codex, parent-assigned gpt-6.1-sol xhigh; input/rules
714f3cad18859c07cd13f31561f2a185f9591a7f. No Git/shared-file changes.
First producer build failed only on two compiler indentation warnings;
they were fixed before any completed run. All reported finite results
come from the frozen successful runner receipt.
