# PD-T?padua-3d-20261106-codex-U2-03 — an explicit 455-node degree-twelve set

ID kind: PD-T. Aliases: U2-AB-12; essential dyadic degree12 witness.
Split from: none; this exact finite claim is distinct from the measured
optimization/quality claim U2-02. Split into: none.

## Statement

Let X be the455 ordered coordinate triples decoded from the
`coordinates_base85` field of
[u2-degree12-nodes.json](../evidence/u2-degree12-nodes.json), whose
complete file SHA256 is
`ade51c2e459b2d3161eddab564e1ada2233d2f841b5dd64bf808b2e607f7140f`.
Decode RFC1924 base85, interpret the10920 bytes as455 rows of three
little-endian IEEE754 binary64 words, and interpret each finite word as
its exact rational value. Then X consists of455 distinct points of
[-1,1]^3 and is unisolvent for the real total-degree space Pi_12.
Equivalently, every vector of455 real data values has exactly one
interpolant in Pi_12 on this particular stored set.

## Definitions

Pi_12 is the space of real polynomials in three variables of total degree
at most12, with dimension binom(15,3)=455. Its monomial evaluation matrix
M has rows indexed by the stored points, and columns x^a y^b z^c for
0<=a,b,c and a+b+c<=12, ordered by increasing a, then b, then c.
The exact rational interpretation of the stored binary64 words is part
of the definition of X; no trigonometric idealization or optimizer replay
is required to define this theorem's points.

## Assumptions

The essential payload and exact checker/receipt identified below are
the stated bytes. The trusted execution model is ordinary Python
unbounded integer arithmetic and its standard-library JSON/base85/byte
decoding, operating on those committed inputs. No floating rank tolerance,
condition estimate, optimizer success or continuous norm sample is a
hypothesis of this claim.

The checker's verifications are Python assert statements; the trusted execution is CPython without -O/PYTHONOPTIMIZE. The committed receipt does not record sys.flags.optimize; the independent audit rerun used default flags (audit04 note, 2026-11-08).

## Status by part

Overall status: **PROVED, computer-assisted finite statement**.

| Part | Status | Evidence |
|---|---|---|
| Stored set has455 distinct exact dyadic points in the cube and is Pi_12-unisolvent | PROVED | Written modular reduction plus independent exact integer checker and essential payload |

Candidate disposition: retained finite construction. Its numerical
quality remains the separate **MEASURED** claim
[U2-02](u2-admissible-norm.md). There is no all-degree quality or
polylogarithmic interpolation theorem here.

## Depends on

Essential payload:14853 bytes, SHA256 above; its coordinate-byte SHA256 is
`1dbd239694d98bee67c861633e03c311c52496af745d8cd43e7bb584ef53c534`.
Independent checker:
[uc12_payload_check.py](../code/uc12_payload_check.py),5193 bytes,
SHA256`c7a2d190758cc246b9037b13065115ae5ec63312d5a811de4c429cc4f452b3a0`.
Actual independent receipt:
[uc12-u2-payload.json](../evidence/uc12-u2-payload.json).
The theorem does not depend on retrieving a raw temporary array or on
reproducing the continuous optimization history.
The separate [payload-to-measurement linkage](../evidence/uc12-u2-payload-link.json)
was also independently executed with a standard-library-only NPY parser;
it verifies exact coordinate-byte equality with the measured n12 set.
That linkage connects the measured quality to this set, but is not needed
for the unisolvence argument once the essential payload defines X.

## Checks

The developer exported the actual highest registered degree output,
losslessly, then checked its hash/shape/domain/distinctness and rank455
using product Chebyshev recurrence modulo1000003. Exact command:

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/u2_node_payload.py --check topics/padua-3d-20261106/evidence/u2-degree12-nodes.json`

A distinct supplementary checker actually executed the independently
written standard-library-only monomial checker, using manual integer-bit
IEEE754 decoding rather than float.as_integer_ratio, a separately checked
prime, and Python integer arithmetic:

`python topics/padua-3d-20261106/code/uc12_payload_check.py --payload topics/padua-3d-20261106/evidence/u2-degree12-nodes.json --output topics/padua-3d-20261106/evidence/uc12-u2-payload.json`

Its frozen source and payload hashes match the receipt. It checks455
distinct exact dyadic triples in the closed cube and returns rank455,
determinant residue318086 modulo prime1000037, with23 row swaps.
The actual execution took3.292 wall seconds on Python3.12.14; timing is
not part of the proof. It imports no NumPy, SciPy or producer module.
This supplements the required Claude audit, without asserting that
audit has occurred.

## Sources

Elementary interpolation linear algebra and modular arithmetic, proved
below. No external literature theorem is a load-bearing premise.
Known-method attribution for finding the set is in the shared gate and
U2-02; no priority claim is made for modular unisolvence certification.

## Proof

Every finite binary64 value is a dyadic rational: after decoding sign,
exponent and fraction bits it has the form m*2^e. The checker performs
that decoding with integers, reduces numerator/denominator by gcd, checks
that every denominator is a power of two and that -denominator<=numerator
<=denominator, and checks455 distinct rational triples. These tests
establish the stated domain and cardinality.

Let A=Z[1/2]. Since1000037 is an odd prime, there is a ring
homomorphism phi:A→F_1000037 that reduces integers modulo the prime and
maps1/2 to the inverse of2. The checker proves primality by testing every
integer divisor from2 through floor(sqrt(1000037)). It then constructs
phi(M) by reducing each exact numerator times the modular inverse of
its denominator and evaluating the complete455 monomials.

Gaussian elimination over this field finds a nonzero pivot in every
column. Row swaps change determinant sign, pivot scaling multiplies it
by the pivot inverse, and row subtraction preserves it; the checker
accumulates the inverse scaling factors and swap signs. The recorded
determinant of phi(M) is318086, which is nonzero in F_1000037.

The determinant is a polynomial with integer coefficients in matrix
entries, so phi(det M)=det(phi(M))!=0. Thus det M!=0 in A and hence in
Q and the real field. The real evaluation map Pi_12→R^455 therefore has an
invertible square matrix M. It is bijective, proving the exact
interpolation statement for the455 stored points.

## Scope

One explicitly stored rational set at degree12. The statement uses no
numerical rank inference and makes no claim about every optimizer output,
the same algorithm at other degrees, a global minimum, a certified
continuous interpolation norm or an asymptotic rate. It does not promote
the measured record U2-02 to PROVED.

## Open items

Required independent Claude audit and root's normal registry/ID treatment.
Continuous norm enclosure and any useful all-degree theory remain open.
No additional computation is needed merely to re-run optimization for
this set: the essential coordinates and exact checker are supplied.

## History

2026-11-07, Codex U2 developer, assigned gpt-6.1-sol xhigh; runtime
metadata unexposed. Rules/input38227202bc6908d5a5a874950145761a8ca4312f.
The stored set was selected as the highest registered degree example,
without selection by assessment quality. Root authorized the small
essential witness and this narrow exact claim. Independent supplementary
execution supplies the fresh exact determinant; quality remains separate.
