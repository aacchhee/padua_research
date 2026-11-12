# PD-T?padua-3d-20261106-codex-D2-real-01 — a known real calibration inside both determinantal families

ID kind: PD-T. Aliases: Chung–Yao natural lattice; diagonal full-spark pencil;
diagonal plus rank-one symmetroid. Split from: none (support for C2).
Split into: none. Developer: Codex gpt-6.1-sol xhigh, rules04ef28b.

## Statement

For every integer n≥1 there are rational affine EN pencils of size
(n+3)×(n+1), and rational symmetric pencils of size n+2, whose maximal-minor
and corank-two schemes, respectively, consist of exactly N=binom(n+3,3)
distinct real affine points. After a rational diagonal affine change these
points lie in [−1,1]³ and are Π_n-unisolvent.

This is an explicit algebraic realization of **known natural-lattice
interpolation**, not a new node family or a quality theorem. The local proof
below supplies the claimed realization; it does not import an unchecked
Józefiak or Eagon–Northcott degree theorem.

## Definitions and assumptions

Put m=n+3 and l_t=x+t y+t²z−t³ for integer t=0,…,m−1. For a triple
I={a,b,c}, p_I=(abc,−ab−ac−bc,a+b+c). Its three vanishing planes are
precisely l_a,l_b,l_c. Set k=m−1 for the symmetric pencil.

## Status by part

Overall status: **PROVED** (written elementary algebraic proof). This proof
has not yet received the topic's independent audit.

| Part | Status | Evidence |
|---|---|---|
| Finite reduced real schemes, exact cardinal polynomials | PROVED | proof below |
| Their Λ and usefulness as Padua analogues | OPEN | separate measured programme; no asymptotic assertion |

The OPEN quality question is outside this file's stated existence claim.

## Depends on / sources

No unproved computational or external theorem is used in the proof.
Attribution: LIT-300/311 and the full natural-lattices-2013 repository record
already describe Chung–Yao's omitted-hyperplane cardinal formula, via Calvi–Phung
Theorem2.1/formula2.3. Original Chung–Yao1977 fulltext was not read by this
developer. This attribution is coverage-qualified LITERATURE, not a priority
claim. C2/S6 suggested EN and symmetric families; the specialization here is
retained as a known calibration.

## Proof

Every three normals (1,t,t²) are independent by the Vandermonde determinant.
The displayed p_I solves their three equations because
(T−a)(T−b)(T−c)=T³−(a+b+c)T²+(ab+ac+bc)T−abc.
Every four augmented plane rows (−t³,1,t,t²) are independent, again by a
Vandermonde determinant. Hence no fourth plane passes through p_I, the N
points are distinct, and no three planes meet at projective infinity.

For EN let B have rows (1,t,…,t^n), and M=diag(l_0,…,l_(m−1))B. Every
(n+1)-row minor of B is a nonzero Vandermonde determinant, so the maximal
minors of M are nonzero constants times all products of m−2 distinct l_t.
Rank drops precisely when at least three planes vanish: with at most two
zeros there are n+1 nonzero independent rows. Near p_I the other planes are
units. Omitting each pair from I gives a generator equal to a unit times
each one of l_a,l_b,l_c; thus the localized ideal is the maximal ideal of
p_I. There are no other complex zeros. This proves finiteness and reducedness.

For the symmetric family put
A=diag(l_0,…,l_(k−1))+l_k 11ᵀ. If l_k≠0 and r≥1 diagonal entries vanish,
the kernel equations force Σv_i=0 and all v_i outside those r positions
to vanish, so corank A=r−1. If no diagonal entry vanishes, the rank-one
update of an invertible diagonal matrix has corank at most one. If l_k=0,
corank A equals the number of vanishing diagonal entries. Consequently
corank≥2 holds exactly at the triple-plane points.

Their submaximal-minor scheme is also reduced. At a triple among the first
k planes, the kernel is the sum-zero subspace on three indices. In its basis
(e_a−e_b,e_a−e_c), the first-order restriction of a perturbation is
[[δl_a+δl_b,δl_a],[δl_a,δl_a+δl_c]]. Its three independent entries determine
the three δl values. At l_k=l_a=l_b=0, kernel basis(e_a,e_b) gives
[[δl_a+δl_k,δl_k],[δl_k,δl_b+δl_k]], again an invertible three-variable
map. At rank k−2 a nonsingular principal (k−2)-block exists. Localizing its
determinant, the submaximal-minor ideal equals the ideal of the three
entries of the 2×2 Schur complement. The preceding invertible differentials
show that this zero-dimensional local algebra has maximal ideal modulo its
square equal to zero; Nakayama's lemma then makes that maximal ideal zero.
Thus each local algebra is a field and the scheme is reduced.

For interpolation define
L_I(X)=∏_(t∉I) l_t(X) / ∏_(t∉I) l_t(p_I).
The denominator is nonzero and the degree is m−3=n. If J≠I, some t∈J\I
occurs in the product, so L_I(p_J)=0; L_I(p_I)=1. These N cardinal
polynomials prove Π_n-unisolvence since dimΠ_n=N. All coordinates are
integers. Each coordinate range has positive width for n≥1; mapping each
range affinely to [−1,1] uses rational coefficients and preserves total degree,
rank loci, reducedness and realness. This completes the proof.

## Checks and evidence

The independent written proof above is the evidence for the all-n statement.
The planned n2/3/4 exact input checks in `fd2_real.py` are supplementary;
their actual receipts are recorded in the outcome file, not assumed here.
The n2/3/4 R1 Groebner checks already yield dimensions10/20/35 for each
family over Q and GF(1000003). The coordinator has now actually replayed
all20 completed pipelines with identical non-timing fields, including
these12 structured cases
([receipt](../evidence/fdr-d2-exact-replay.json)). This does not establish
any random n4 statement. Its written-proof review found the argument
coherent; formal topic audit remains separate.

## Scope and open items

All-real-in-cube existence is therefore not an obstruction for the full C2
families. The known natural lattice may have very poor Λ. Neither positive
cubature, Chebyshev Jacobi sections, sparse higher-dimensional recurrences,
nor a log³ bound follows. The independent formal audit remains separate;
the completed bounded measured parameter search has its own record.

## History

2026-11-12: written as the explicit known calibration required by D2, preserving
the original broad C2 quality target as OPEN. No final ID assigned.
