# C11 fixed J16 variant — independent focused check

2026-11-06. Input head
`4ca11b81e4906b9789894907618b511a6a702423`; repository rules previously
read at `e8fad1671fb736247e4c510284f6f935e6345efb` and confirmed unchanged
by the coordinator. Distinct Codex supplementary reviewer, assigned Astra
high; actual serving model/effort metadata independently unexposed.
Formal Claude audit remains separate.

**ACCEPTED within the existing guarded C06/C07 point and partial-sum
contracts on LP64. No unresolved mathematical or enclosure finding.**
J16 is allowed by the accepted C02 theorem, and the implementation
consistently recomputes its larger smooth remainder. This is one fixed
parameter variant, not a uniform1e-8 guarantee, adaptive-order algorithm,
whole-box implementation, production throughput result or new certified
degree.

Read the C11 prospective attempt, source/controls/receipt and the complete
diff against accepted C10; refreshed C02's general-J statement and
fourth-derivative tail argument. The C02/C06/C07/C10 reconstructions are
already documented in this reviewer's preceding reports. There is no
new mathematical mechanism, novelty or priority claim, so a full historical
registry/literature gate is outside this narrowly scoped check. No author,
shared, prior-review or Git state was changed.

## Frozen change and analytic applicability

| File in code/cheap_rows_C11 | SHA256 |
| --- | --- |
| partial.cpp | `bde1ce4850849dd402acc91eb3cee7d40883bbd51d5f7cff13334abc0f4ee23c` |
| point.cpp | `6e2f1920ca293ac5a34f01c6369d94345b0d0c9b8a03d3e58ef15d453fbcf1d9` |
| controls.cpp | `844e053a70bda2daa6a9ab969d395052eff4f366c438d14fe19226c776d50f56` |
| control.py | `5bd4544d26562281d74f46ec58ae5be4cfb3d1523f03274ea5acfafbc171e252` |

Byte comparison proves partial.cpp is exactly accepted C10 after replacing
J48 by J16 in its constant declaration. The point source is byte-identical
to C10, with its local include resolving the new C11 partial source.
The independent driver asserts both relations and all four source pins
before/after execution. Accepted C10 partial remains
`209fa24300219884b97ce267e898b085593534d97ecc31640909c4c772061ac5`.

C02 explicitly proves, for every integer J>=1,

    M_J=389120/(19683*pi^5)*(2J+3)^4*4^-J,
    |smooth error|<=7*q*h^4*M_J/5760.

Its proof starts the residual tail at j=J+1>=2, uses the coefficient
bound valid there, and sums the geometric fourth-derivative majorant.
There is no requirement J>=48 or96. Taking J16 therefore gives precisely

    M_16=389120/(19683*pi^5)*35^4*4^-16.

The stronger J96 all-row numerical inequality is a distinct specialization
and is not inherited by this variant. All coefficient identities and the
corrected midpoint formula remain applicable to the shorter polynomial.

Every result-bearing use of J was checked:

- Polynomial degree is2J+1=33; moments cover0..33.
- work/out/half-step vectors have34 entries; endpoint-power vectors
  have35 and are filled through degree34, covering every d+1 access.
- Moment recurrence and input-radius charges run through degree33.
- Polynomial value, integral and derivative loops all run j=0..16,
  using powers d,d+1,d-1 and the original scaling factors.
- Both actual returned smooth-error radius and diagnostic budget use
  `(2J+3)^4*4^-J`, hence the new order and its full larger remainder.

The coefficient vector still extends through WD96 because the independent
w' evaluation requires those coefficients. Its640-bit preparation,
WD96 derivative tail, K32/L16 harmonic calculation and both harmonic
error charges are unchanged. The moment recurrence remains explicit
Arb640, with outward rounding of the entire work ball to160 followed
by exactly one unchanged input-radius derivative charge. Thus the
accepted C10 enclosure proof applies with fewer recurrence terms.

Every partial ball is multiplied by the complete C/D coefficient balls
and accumulated over all ordinary rows by unchanged C07 assembly.
No special-row bound substitutes for the full row charge, and no larger
J16 radius is discarded. Retained/direct primitive balls and the final
n(n+1) normalization are unchanged. All guards, native failure semantics,
LP64 domain limits, parity and closed-boundary handling remain accepted
dependencies. Old exact-rational J48 appears only in the developer's
diagnostic namespace; there is no production fallback.

## Independent bounded execution

Executed once:

    python topics/padua-argmax-bridge-20261105/code/cheap_rows_C11_review/control.py

Exit0, **PASS**, 2.520223 parent-plus-child CPU seconds including a fresh
compile, below the20-second allocation. Python3.12.14; g++14 Debian
14.2.0-19, x86-64 LP64. No random cases/seed, large finite-board reference,
scaling-pilot replay or degree certification.

Nine partial calls contain complete512-bit direct endpoint-reference
hulls. They cover n2,3,7,64 and a singleton at the maximum supported n;
q31/32/33; interval offsets; removable cell endpoints; both poles and a
1e-60 left-pole input. Monotonicity of the guarded cotangent sum makes
the endpoint hull a full input-image enclosure, not a midpoint test.

Four interval-moment cases at(n,q)=(3,3),(11,5),(5,1),(2147483647,1)
check exact rational direct sums through degree33 at the midpoint and
both exact input-ball endpoints. An additional n7,q2 input formed from
1/3 at1024 bits is checked through degree13 at those same three
positions. All450 comparisons pass. These finite controls supplement
the unchanged input-radius derivative proof; endpoint checks alone are
not asserted to prove every even moment's full interval image.

Six small native point calls at n3/8 exercise an alpha0 nodal row,
origin, beta0 collision, a halfphase closed-edge tangency, a generic
phase and a vertex. Five returned production balls contain complete
512-bit reference balls. The exact vertex output1 lies inside its
reference ball; this converse containment is reported separately.
The reviewer reference explicitly sums the original finite cosine
polynomial over the odd board, without a collapsed ratio, C06 partial
sum, root selector or Chebyshev recurrence.

The independent n2,q2,y1/2 radius is
**3.339952381331557e-7**, reproducing the intentionally larger paid
truncation budget. This is a valid enclosure and is incompatible with
describing J16 as uniformly accurate to1e-8. The attempt makes no such
claim.

Small receipt `evidence/c11-review-rows.json` pins reviewer sources,
driver, builder, compiler/binary and local raw
`c11-review-rows/check-6lshh41l/review.json`,49192 bytes, SHA256
`7f2e6afcee4cccd299145d8d928d638618821bf239d28e4cdec5faaf5b3d3624`.
The raw closure contains196 source/header identities, four compiler tools,
13 tool dependencies, eight linked dependencies and eight actually mapped
runtime dependencies. Preprocessed/toolchain identities are checked
through compilation; loaded dependencies and frozen sources agree
before/after controls. Large raw artifacts remain local/regenerable;
physical archival transfer is pending, with no remote retrieval claim.

Separately verified264 byte-size/SHA256 identities from the developer
receipt and raw manifest. The5986-byte developer receipt has SHA256
`4eef1af7d3250af391bed60ab2a243d1510393fa838c28f491b211ea775c310d`.
That check verifies provenance, not execution of the developer's pilot
by this reviewer.

## Measured accuracy and remaining limits

The frozen developer receipt records successful point diagnostics at
n32,128,512,2048, all at rational phase fractions1/12,1/16, with full
S radii approximately1.53e-11,9.33e-14,4.97e-16,2.46e-18. Each meets
the prospective desired1e-8 threshold for those particular inputs.
The n32/n128 endpoint overlap checks against preserved C10 results are
consistent with that receipt. They neither imply identical output balls
nor a uniform accuracy bound over other phases or degrees.

The smaller fixed polynomial order reduces work while increasing its
explicit analytic remainder. The reported warm native call times are
finite measurements, not a general scaling proof or cold-start benchmark.
The n512/n2048 calls are point-cost diagnostics; no reference-board
comparison, phase cover or argmax certificate was produced there.

This acceptance leaves total point success, useful enclosure tightness
on arbitrary inputs, executable whole-box root handling, phase gradients,
corner orbits, projected defects and complete certification OPEN. The
analytic C08 contract does not automatically turn this point evaluator
into a whole-box implementation. Formal Claude review remains separate.
