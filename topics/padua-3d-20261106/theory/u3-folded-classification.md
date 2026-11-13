# PD-T?padua-3d-20261106-codex-U3-04 — bounded coherent rank-two folded classification

ID kind: PD-T. Aliases: U3-F exact460completion; C6×C18quintic.
Split from: none. Split into: family-boundary PD-N?padua-3d-20261106-codex-U3-02.

## Statement

For every n=3..8let N=binom(n+3,3). For M in{2N,2N−4}, a>=2,
a|b,ab=M, r=0..a−1,s=0..b−1, form

    h1=(1/a,0,r/a), h2=(1/b,1/b,s/b), H=<h1,h2>,
    phase in{0,h1/2,h2/2,(h1+h2)/2}.

The full cosine image has exactly Nnodes and is Pi_n-unisolvent if
and only if n5and the parameters are

    (M,a,b,r,s,phase-index)=(108,6,18,1,14,0), (108,6,18,5,4,0).

Each listed parameter instance has56distinct nodes and exact rank56.
The two labelled hits give **one distinct physical node set**: replacing
(r,s)=(1,14)by(5,4)negates the third torus coordinate modulo1and leaves
its cosine unchanged, with the first two coordinates unchanged.
No positive cubature exactness is claimed.

## Status by part

Overall status: **PROVED**, computer-assisted finite classification.
The independent canonical-residue/gcd-rational checker actually completed
all460cases and matched every exact rank, with separate actual-node
monomial ranks at two fresh primes for every one of these cases.

Candidate disposition: finite quintic retained; every rejected fixed
parameter has an exact count, axis, trace or rational-rank reason. The
through-3..8family fails its n4existence condition by a separate hand proof.

## Definitions, assumptions and dependencies

Angles in turns, full subgroup and exact cosine images, total-degree Pi_n.
The embedding has invariant factors(a,b) because first-minus-second and
second recover its two parameters. Coherent phases satisfy2phase∈H.
Use [integer rank reduction](u3-coherent-integer-reduction.md), the already
proved fixed-node trace test and coordinate annihilator. All tests are
in characteristic zero or exact integers/rationals; deficient modular
ranks are never upper bounds.

## Proof reduction and exact outcomes

There are finitely many listed divisors and residues. Folded residues
modulo the common angle denominator identify actual equal cosine nodes
because cosine is injective on[0,pi]. Wrong count cannot yield minimal
interpolation. An axis with<=nphysical values gives a nonzero coordinate
annihilator of allowed degree. For h∈H[2], evaluation intertwines its
physical coordinate sign involution; its polynomial trace must equal
the number of actual fixed folded nodes. Mismatch certifies deficiency.
All remaining cases have their EXACT real ranks equal to the rational
integer-dictionary rank by the coherent reduction.

| n | All parameters | Wrong count | Trace kill | Axis kill | Exact QQ cases | Full rank |
|---:|---:|---:|---:|---:|---:|---:|
|3|592|420|139|5|28|0|
|4|0|0|0|0|0|0|
|5|2192|1553|460|29|150|2|
|6|1328|660|668|0|0|0|
|7|2864|1593|912|77|282|0|
|8|0|0|0|0|0|0|

The table uses producer precedence: a trace mismatch can replace an
earlier short-axis reason. The independent checker may prioritize the
axis; the union of certified exclusions and remaining460parameter
instances must agree, and every exact rank is compared by parameter.
Zero unresolved cases remain in the producer's finite universe.

The two positive tuples are not counted as distinct constructions. For
u mod6,v mod18their third numerators modulo18are3u+14vand15u+4v;
the latter is the negative of the former modulo18. Thus their folded
triples agree pointwise. An actual exact-node-list comparison after the
census confirms common denominator18,56nodes each and identical lists
(canonical JSON node-key SHA256
d6bdd58ccb395d78d8df039626b029c62124b37721159b9ef72fa16446a93b08).

## Checks and evidence

Initial protocol3b5cb29f5d68306fa61d3079627247110911b552; exact-completion
append995062b42aa73648bd591a21c9ea240feffc3c6f. Original source8c230e3a
and its [receipt](../evidence/u3-f.json) stay unchanged. New exact source
73619ff1c4f46c95f4e9fc2cf93f3c91d8a1a9bce42f949a4ca533f51572c823
actually ran:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/u3_folded_exact.py --receipt topics/padua-3d-20261106/evidence/u3-f-exact.json

[Exact receipt](../evidence/u3-f-exact.json):6.2544seconds,460QQtests,
262distinct normalized matrices after caching, no120-second warning.
All finite parameters, decisions/ranks and full raw704135-byte identity
are recorded. SymPy exact DomainMatrix QQ elimination is trusted;
the independent checker uses canonical residue references and its own
gcd/rational elimination, plus fresh actual-node monomial certificates.
Its actual19.9185-second result is [uc3-f-exact.json](../evidence/uc3-f-exact.json).
[Casewise comparison](../evidence/uc3-comparison.json) matches all6976count/
trace/axis outcomes and all460exact ranks. Fresh actual-node rank pairs
also agree at every case, including both positive tuples. These modular
checks are lower-bound cross-checks; the rational dictionary supplies
the deficient upper bounds. See [usable-check3](../usable-check3.md).

## Sources, scope, open items and history

No external theorem, no cubature premise, no historical novelty claim.
Other group orders, embeddings and free phases are outside this finite
classification. The selected n5mesh performance51.7630is measured and
loses to controls; that is a separate finite negative statement.
2026-11-07, Codex assigned gpt-6.1-sol xhigh, rules3822720.
