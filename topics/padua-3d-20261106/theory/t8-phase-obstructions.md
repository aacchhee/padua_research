# PD-N?padua-3d-codex-T8-01 — three translated rules fail in degree two

ID kind: PD-N. Aliases: phased PK/PT/PO quadratic kills.
Split from: none. Split into: none.

## Statement

Each of the three fixed translated families P in preregistration-T8.md,
defined for every n>=2 by M=N=binom(n+3,3), phases
phi=(pi/2,pi/3,pi/4) and generators PK/PT/PO, fails Pi_2 injectivity at
n=2. Each has exactly ten distinct nodes there, but a nonzero quadratic
vanishes on all of them. Consequently none supplies the specified
every-degree-n>=2 interpolation family. No other phase or generator rule
is excluded.

## Definitions and assumptions

At n=2 set t=2pi k/10, k=0,...,9. The generators reduced mod10 are
PK=(1,3,9), PT=(1,3,6), PO=(1,5,3). Write the node coordinates (x,y,w).
T_2(v)=2v^2-1. All identities below are exact over R; modular ranks are
not proof dependencies.

## Status by part

Overall status: **PROVED**, by explicit hand identities below.
The measured exact rank values 8,9,8 belong to the separate phase receipt;
they are not needed for these noninjectivity statements.
Candidate disposition: PK, PT and PO **REJECTED: failed** under D2 at
their first admissible degree. Other translated rules remain OPEN.

## Negative-result scope

Attempted mechanism: IDEA?padua-3d-codex-T8-02's three prospectively frozen
uniform translated K/T/O rules, phases as above, degrees n>=2.
Parameter failure: n=2 only suffices to kill each all-n>=2 rule.

## Depends on

Elementary sine/cosine product formulas, T3-01's notation only.
No computational or external-source theorem is required for the proof.

## Proof

For PK, theta_x=t+pi/2 and theta_w=-t+pi/4 modulo2pi, so their sum is
3pi/4. The addition formula gives the nonzero quadratic

    x^2+w^2+sqrt(2)*x*w-1/2 = 0.

For PO, y=cos(5t+pi/3)=(-1)^k/2. Hence 4y^2-1=0.

For PT define the nonzero degree-two polynomial

    P=(2sqrt(2)-2sqrt(6)/3)w + (sqrt(3)/3)T_2(w)
      +(2-4sqrt(3)/3)T_2(y)+(4sqrt(3)/3)xy+T_2(x).

It is nonzero because its x^2 coefficient is 2 and no other term supplies
x^2. Since 10t is an integer multiple of2pi, PT's coordinates satisfy

    w=(cos4t+sin4t)/sqrt(2),       T_2(w)=-sin2t,
    T_2(y)=-(cos4t)/2+(sqrt(3)/2)sin4t,
    xy=-(sin4t-sin2t)/4+(sqrt(3)/4)(cos2t-cos4t),
    T_2(x)=-cos2t.

Substitution cancels separately the coefficients of cos4t, sin4t,
sin2t and cos2t. Thus P vanishes at every sampled point. In all three
cases a nonzero member of Pi_2 vanishes, proving noninjectivity.

Exact cardinality ten can also be checked without floating cosines.
The finite-angle formula in T8-01 gives ten distinct triples modulo
L=lcm(10,24)=120 with phases (30,20,15)/120. Cardinality is reported by
the exact enumeration; the injectivity obstruction itself does not need it.

## Checks and sources

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/t8_phases.py`

The executed receipt evidence/t8-phases.json reports exact phased ranks
8,9,8 over Q(zeta_24), with nonzero kernels multiplied back exactly.
Phi_24(t)=t^8-t^4+1 and rational coefficient lists make the certificate
reconstructible. A nonzero rank mod a splitting prime lifts; modular
deficiency is separately confirmed over the cyclotomic field. Those
computed exact ranks remain MEASURED until independent rerun.

No primary source is cited for the identities; literature-T8.md records
the prior-architecture comparison and coverage limits.

## Scope and open items

This closes exactly the three frozen P rules, not all rational phases,
not generic continuous translations, not a degree sequence omitting n=2,
and not arbitrary cyclic or noncyclic cosets. A phase chosen after these
failures requires a new prospective rule and structural escape reason.
No quality run or growth fit was performed after the rank kills.

## History

2026-11-06, Codex T8, assigned gpt-6.1-sol high, rules e5b64450.
The rules were prospectively frozen; exact kernels prompted the displayed
independent elementary identities. An initial SymPy field-matrix coercion
error produced no receipt; direct typed matrix construction fixed it.
