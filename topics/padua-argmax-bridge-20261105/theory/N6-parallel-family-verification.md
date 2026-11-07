# N6 verification — Covering parallel family and exact one-variable norms

Record kind: verification of inherited PD-T101/364, not a new PD-T claim.
Aliases: unimodular diagonal-phase parallels; shifted generating traces.
Split from / into: none. The mathematical identities are routine
substitutions, recorded explicitly to gate subsequent comparisons.

## Statement and definitions

For every integer n>=2, put m=n+1 and N=nm. On the parameter torus
T²=(R/2pi Z)² define

    Gamma_s(t)=(cos(mt+s),cos(nt+s)).                         (1)

This family covers the whole closed square. Every interior square point
has exactly four parameter preimages in T²; every noncorner boundary
point has exactly two, and every corner has exactly one. These are family
multiplicities, not the number of visits by a single fixed-s trace.

At every fixed s, each restricted cardinal is a real trigonometric
polynomial of t of degree at most N; at fixed t its degree in s is at
most n. Its exact l1 norm representation is (3) below. The exceptional
(n,0) coefficient remains one, and four-copy cancellation remains inside
each absolute value.

## Assumptions and status

Use exactly PD-T101's even checkerboard, total-degree interpolation,
positive endpoint weights and exceptional x-mode correction. Exact real
arithmetic. Status: **verification of inherited PROVED identities**;
no new primitive, maximum bound or registered dependency is asserted.
The failed additional comparison is a separate negative record.

## Proof / reconstruction

Write physical angles theta,phi in [0,pi]. The angular map

    (t,s) -> (theta,phi)=(mt+s,nt+s) mod2pi

has integer determinant m-n=1, and its inverse is

    t=theta-phi,  s=m phi-n theta mod2pi.                    (2)

Consequently it is bijective on the angular torus. Each physical
coordinate strictly between -1 and1 has two distinct angle preimages;
each endpoint has one. Multiplying those two counts and applying (2)
proves the 4/2/1 family multiplicities, with no missing boundary point.

For a point with chosen angles theta,phi, the complete family fiber is

    t_(epsilon,eta)=epsilon theta-eta phi,
    s_(epsilon,eta)=m eta phi-n epsilon theta,

for epsilon,eta in {+1,-1}, modulo2pi, with duplicates removed exactly
when a physical coordinate is an endpoint. In a single fixed-s trace,
the visit times are precisely the t entries of this list whose s entry
equals the fixed parameter. Thus the same formula also accounts for
self-intersections and their multiplicities. For interior points,
coincidence of s entries is equivalent to one of
n theta, m phi, m phi-n theta, m phi+n theta being in pi Z,
depending on the two sign pairs compared. Equal (t,s) pairs cannot
occur for distinct angular sign choices, by the torus bijection.

For a corner theta=j pi,phi=k pi, j,k in{0,1}, its unique s entry is
(mk-nj)pi modulo2pi. The physical mesh indices are (nj,mk), and their
sum has the same parity as mk-nj. Therefore s=0 at the node corners
and s=pi at the two nonnode corners. The bare-s0 coverage fact is
already in N086; it is not a new negative claim. The shifted trace s=pi
is retained because it reaches both required candidate corners.

For mesh angles a_j=j pi/n,b_k=k pi/m let w_jk be T101's weights.
Use the finite-polynomial kernel G_n=D_n-cos(nu) from T364, and set

    p_jk(t,s)=(w_jk/4) sum_(sigma,eta=+-1)
                    G_n(mt+s+sigma a_j,nt+s+eta b_k),
    lambda_n(Gamma_s(t))=sum_(j+k even) |p_jk(t,s)|.         (3)

T101/T364's product-to-sum identity proves (3) without a bound. In
the product-Chebyshev version it is

    p_jk/w_jk = sum_(a+b<=n) h_a h_b cos(a a_j)cos(b b_k)
                      cos(a(mt+s))cos(b(nt+s))
                - (-1)^j cos(n(mt+s)),

where h_0=1,h_a=2 for a>0. Thus the top (n,0) mode has coefficient
2-1=1. Products have t frequencies a m +- b n, with absolute value
at most a m+b n<=nm, and s frequencies a+-b of absolute value<=n.
The corrected exceptional term has exactly the stated degree bounds.

All formulas are finite trigonometric polynomials, including collisions,
nodes, edges and zeros. If an implementation instead uses the divided
difference P_n=T_(n+1)+T_n, the collision cos u=cos v uses
P_n'(cos u)-cos(nu), as in T364; it is not assigned zero. If a product-U
quotient is used, sin(kz)/sin z at z=l pi takes the continuous value
k(-1)^((k-1)l). The family introduces no extra singularity.

## Checks, sources and scope

Dependencies: complete locally proved PD-T101 and inherited PD-T364.
No external source theorem, interpolation theorem in one variable,
convexity or sign-stability assumption is used. Formula(3) is an exact
one-variable norm for each parallel but supplies no maximum inequality.
Replacing its absolute four-copy sum by separate absolute values
recreates the obstructed primitive majorant and is not an accepted step.

The exact n2 checker in `../code/n6_two_trace_exact.py` independently
compares rational Vandermonde cardinals with the corrected kernel; it
does not validate these general algebraic identities by sampling.

Open item: a useful additional inequality must be specified independently
of PD-T099 and survive its own exact low-degree gate. The two-trace
comparison fails in the companion negative record. The family itself
remains an equivalent identity, not all-degree proof progress.

## History

2026-11-05, Codex N6, assigned gpt-6.1-sol xhigh; rules/input98d6c00.
Round1 verification is retained alongside the narrow comparison failure.
