# PD-T?proof-attempts-2-codex-50 — Degree-seven tensor field and its principal real embedding

ID kind: PD-T.
Aliases: A5 n7 arithmetic; cos(pi/7),cos(pi/8); degree12 native-to-tensor conversion.
Split from: real-embedding obligation for the degree-seven finite certificate.
Split into: count and global argmax are separate records51/52.

## Statement

Let a be the largest real root of p3(t)=t³−t²−2t+1 and b the largest real root of p4(t)=t⁴−4t²+2. Then a=2cos(pi/7), b=2cos(pi/8), and K=Q(a,b) has degree12 with rational basis

B=(1,b,b²,b³,a,ab,ab²,ab³,a²,a²b,a²b²,a²b³).

The element theta=a+b is primitive with minimal polynomial

f(t)=t¹²−4t¹¹−14t¹⁰+64t⁹+39t⁸−292t⁷+42t⁶+436t⁵−166t⁴−172t³+40t²+24t+1.

For r=0,…,11, reduce(a+b)^r by a³=a²+2a−1,b⁴=4b²−2 and put its B coordinates in columnr of T. Then T has determinant203415409 and converts ascending theta-power coordinates to B coordinates. It identifies the exact real interpretation of any native quotient representation once its defining polynomial and conversion identities have been verified. Rational outward evaluation in a,b brackets encloses every such field element.

The principal roots have brackets a∈(9/5,181/100), b∈(46/25,37/20). A sub-bracket inside either outer bracket with p(lower)<0<p(upper) selects the same principal root. These are exact real-embedding conditions, independent of an arbitrary symbolic root selector.

## Definitions

U_m is the Chebyshev polynomial of the second kind. FIELD serialization is the12 rational B coefficients in the stated order; native coefficients ascend in theta powers. The serialized native_to_tensor is T, not T inverse. The supplied rational brackets are128-bit outward dyadics in the implementation.

## Assumptions

Exact rational/field arithmetic and inclusion-preserving interval arithmetic. An implementation must independently verify defining identities, conversion data and principal brackets before treating native coefficient intervals as real enclosures.

## Status by part

Overall status: **PROVED** (written exact representation theorem; required Claude audit PENDING).

| Part | Status | Evidence |
|---|---|---|
| field degree and tensor basis | PROVED | coprime degree argument below |
| primitive element and coordinate conversion | PROVED | exact reduction matrix and determinant |
| principal embedding and outward coefficient interpretation | PROVED | Chebyshev root identities and rational monotonicity |

This supporting theorem asserts no maxima count. Actual finite checks and independent execution are recorded separately.

## Depends on

Elementary field degrees, Eisenstein, rational-root test, Chebyshev recurrence/root identity, exact polynomial reduction, interval inclusion. The cardinal constructor uses the corrected kernel literally labelled `PD-T?proof-attempts-codex-01 (audit pending)`; dated2026-11-01 qualification: part1 audit accepted, minor dispositions complete and Part1merged(PR9/main806cc7b), as integrated by the parent; finalaliasPD-T101. Direct exact cardinal identities are checked independently as well.

## Checks

New implementation code/a5_n7_field.py. Its actual field/cardinal pilot verified36 cardinals at all1296 node pairs, partition of unity and1159 nonzero monomial coefficients under SymPy1.14/python-flint0.9,128-bit outward intervals. The observed post-import time was0.779154s. A separate independent formal-quotient and Vandermonde implementation subsequently verified the field/conversion/principal brackets, all1296 cardinal values and partition, and all36node cones. Full count verification remains separate.

## Sources

Registered A5, programme IDEA206(alias17), source06 at9bd14a6d2c4da69139a10107d8a787f2be0c5c9e; refreshed gate in attempts/T-A5-n7.md. This is implementation support for the registered target, no novelty or priority assertion.

## Proof or evidence

The cubic p3 has no rational root: the only possible integer roots are±1 and neither vanishes. It is irreducible. The quartic p4 is Eisenstein at2. Thus Q(a),Q(b) have degrees3,4. Both degrees divide[K:Q], which is at most12; consequently it equals12. The tensor monomials span by the two reduction relations and, being12 in number, form a basis.

Construct T by the stated exact binomial expansion and reductions. Its columns0 and1 are respectively e0 and e1+e4. Direct integer elimination gives detT=203415409≠0. Thus1,theta,…,theta¹¹ also form a basis, so theta is primitive. Substitution and reduction give f(a+b)=0. Since f is monic of degree12, it is the minimal polynomial. These identities can alternatively be checked through the formal quotient Q[t]/f, recovering a by the monic linear gcd in z of p3(z) and p4(t−z). No approximate embedding is needed for any coordinate identity.

The exact factorizations are

U6(t/2)=p3(t)(t³+t²−2t−1),

U7(t/2)=t(t²−2)p4(t).

At9/5, p3=−1/125,p3'=103/25>0; p3''=6t−2>0 thereafter. At181/100,p3=33641/1000000>0. Hence exactly one p3 root lies in the bracket and none lies above it. The other cubic factor is positive and strictly increasing for t≥9/5, as its value559/125 and derivative283/25 there are positive and its second derivative6t+2>0. Thus the bracketed root is the largest U6 root, namely2cos(pi/7).

At46/25, p4=−31294/390625; at37/20,p4=3761/160000>0. For t≥46/25>sqrt2 its derivative4t(t²−2)>0, so exactly one p4 root lies there and none above. The other factors t and t²−2 are positive above46/25. It is the largest U7 root, namely2cos(pi/8).

All conjugates of a and b are real, as witnessed by the Chebyshev factors. Choosing their largest roots fixes the real embedding. Every tensor field expression is a rational polynomial in a,b; interval arithmetic encloses its value inductively under addition and multiplication. Fixed-dyadic floor and ceiling rounding preserve inclusion. Verified exact conversion therefore transfers this enclosure to every native field coefficient. ∎

## Scope

Exactly the degree-seven coefficient field. No other-degree count or automatic search termination is asserted.

## Open items

Required Claude audit of Part2. The degree-seven count/value application, complete artifacts, separate checker and actual different-agent executions are now complete in51/52 and their receipts; this field theorem still asserts no other-degree count.

## History

2026-11-01, Codex /root/a5_develop, allocated gpt-6.1-sol xhigh; rules4bd1d65. Written before a degree-seven count is accepted. All older-degree code is frozen.

2026-11-01 after13:33UTC: application status synchronized after51/52's complete independent acceptance; theorem and frozen code unchanged. Required Claude audit remains PENDING.
