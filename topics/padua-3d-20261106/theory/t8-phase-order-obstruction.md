# PD-N?padua-3d-20261106-codex-T8-02 — order-ten cyclic images fail for every phase

ID kind: PD-N. Aliases: generic-phase minimal-order obstruction;
no-fold half-period trace; all continuous phases at M10.
Split from: none. Split into: none.

## Statement

For every z in Z^3 and every phi in R^3, the full image

    X={ (cos(phi_j+2pi k z_j/10))_j : k=0,...,9 }

is not Pi_2-injective. If |X|=10 and r is the number of odd coordinates
of z, its evaluation rank is at most8 for r=1 or3 and at most9 for r=2.
Consequently the generic-phase route M=N=binom(n+3,3) cannot supply a
minimal interpolation family for every n>=2, irrespective of the uniform
phase/generator prescription. Omitting n=2 remains outside this failure.

## Definitions and assumptions

No rationality or genericity of phi is imposed. The orbit is a single
full cyclic coset image, with parameter modulus10. If its actual order is
less than10, the cardinality argument below already applies. Node sets,
polynomial space and ranks are over R. T_2 basis versus monomials changes
no eigenspace dimension or rank.

## Status by part

Overall status: **PROVED**, elementary hand proof. The finite measured
P ranks are corroboration only. Candidate disposition: the every-n>=2
M=N no-fold translated route in IDEA?padua-3d-20261106-codex-T8-02 is
**REJECTED: failed**. Other orders, omitted-degree sequences, unions and
multi-orbit constructions remain OPEN.

## Negative-result scope

Attempted mechanism: generic translated cyclic sampling with exactly
M=N torus parameters/nodes, proposed in handoff04 T8.2 and prospectively
retained in T8-02; the three P rules are concrete members. Failure is
at n=2,M10, every z, every continuous phase. No asymptotic or general
coset nonexistence is asserted.

## Depends on

Elementary intertwining under a sign involution. The trace calculation
is the same as the prerequisite in T8-03, and is rederived below in
degree two so this argument is independently readable.

## Proof

If |X|<10, the ten-dimensional Pi_2 cannot inject into R^X. Otherwise
the parameter-to-node map is bijective. Translation k->k+5 therefore
induces a fixed-point-free involution on X. Its physical action is the
coordinate sign reflection R flipping exactly those axes with odd z_j,
since cos(theta+pi z_j)=(-1)^(z_j)cos(theta), for arbitrary theta.
If all z_j were even, every node would repeat at k+5, contradicting
|X|=10. Thus r=1,2 or3. Since the action is free, R^X has plus and
minus eigenspaces of dimension5 each.

On Pi_2 the monomial trace under a flip of r axes is

    D_r = 1 + (3-2r) + 3 + ((3-2r)^2-3)/2.

Here the four terms respectively count the constant, three linear
monomials, three squares, and three mixed quadratic monomials. They
give D_1=4, D_2=2, D_3=4. Thus the polynomial plus/minus dimensions
are7/3 for r1 or3, and6/4 for r2.

Evaluation intertwines these two involutions, so it maps each polynomial
eigenspace into the corresponding nodal eigenspace. The rank is at most
min(7,5)+min(3,5)=8 in the first cases and min(6,5)+min(4,5)=9 in
the second case. Hence it cannot be10. This proves the statement for
every phase, including all special fold strata, without a phase census.

## D3 and checks

The involution principle admits 2D Padua as shown explicitly in T8-03:
its cyclic order is2n(n+1), its half-period fixed nodes number
floor(n/2)+1, exactly the polynomial trace. The bijective-parameter
M=N hypothesis here fails for the Padua cyclic representation because
its multiple folds are essential. There is no extension excluding Padua.

The continuous phase class is not a finite class needing an exhaustive
phase computation for this analytic argument. The already executed P
cases have r3/r2/r3 and reach the predicted rank ceilings8/9/8 exactly,
as recorded in evidence/t8-phases.json. Those exact finite rank equalities
retain MEASURED status separately until independent rerun. No new family
run or exhaustive phase enumeration was used in deriving this theorem.

## Sources, scope and open items

No external theorem is used and no historical novelty is claimed;
literature-T8.md records source limits. This obstruction concerns exactly
the specified single cyclic modulus10/all-phase class. Phased odd-degree
families starting at n3, other moduli and no-fold generic phases at other
degrees need new prospective structural rules and D2. It does not reject
all translated cyclic interpolation.

## History

2026-11-06, Codex T8, assigned gpt-6.1-sol high, rules e5b64450.
Written after the three frozen P kills, explaining them uniformly and
closing their generic-phase M=N every-degree parent route. The previous
three hand quadratic certificates remain intact as independent proofs.
