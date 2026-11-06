# PD-T?padua-3d-20261106-codex-T9-r06-06 — exact parity-family data for the finite complement

Aliases: T9-R06-FINITE; density complement1..109; parity-anisotropic exact Gram. Supporting obstruction: PD-N?padua-3d-20261106-codex-T9-r06-03 (this full family is always oversized). No global lattice-minimum claim.

## Statement and proof

For every n>=1 use the T10 parity-anisotropic lattice with orders (n,n+1,n+1). Its annihilator H is the union of the rectangular torus grid with these lengths and its simultaneous half-step translate. Their coordinatewise cosine images are disjoint: an integer and a half-integer angle index cannot agree up to sign modulo the same integer order. A length-m unshifted cosine grid has A(m)=floor(m/2)+1 points; the half-step grid has B(m)=ceil(m/2). Thus the exact number of folded points is

```
F(n)=A(n)A(n+1)^2+B(n)B(n+1)^2.
```

The exact orthonormal degree-n Gram matrix is I+ee^T, with e indexing (n,0,0), as proved in T10's `t10-parity-log4.md`: the only extra dual frequencies through2n are ±(2n,0,0). This identity proves full column rank N=binom(n+3,3) for every n. It is an analytic rank result, not a dense numerical rank estimate.

For even n, F(n)=(n+1)(n+2)^2/4 and

```
F(n)-N=n(n+1)(n+2)/12 >0.
```

For odd n, F(n)=(n+1)(n^2+4n+5)/4 and

```
F(n)-N=(n+1)(n^2+2n+3)/12 >0.
```

Hence this complete explicit parity-anisotropic family cannot itself be a minimal-node interpolation set, in **any** degree, including every1..109 degree in the density theorem's complement. Selecting N nodes is a different construction with a separate extraction/quality question. The node ratio tends3/2. This is an established-family calculation/variant, with no novelty claim.

## Actual finite work and feasibility

`code/t9_r06_complement.py` records exact family determinants, folded counts, analytic ranks, minimal N and imported-density lower bounds for every n1..109. Its formulas agree with all16 T10 owner count controls. Additional actual group enumeration and sparse rational boundary-rank calculations were performed at n17,24,32, respectively:

| n | Folded points | Exact rank | Group/fold CPU seconds | Sparse rank CPU seconds |
|---:|---:|---:|---:|---:|
|17|1629|1140|0.0172|0.0047|
|24|4225|2925|0.0592|0.0105|
|32|9537|6545|0.1129|0.0176|

All probes stayed within the prospective15-second cap. Exact folded payload hashes and all109 rows are in `evidence/t9-r06-complement.json`, under16KiB. Total CPU0.2281 seconds. At109 the family has338855 points and rank227920. A dense float64 evaluation matrix would require617854652800 bytes, and a square inverse415580211200 bytes; neither was allocated. The registered fallback is the exact count/Gram proof plus sparse controls, rather than an infeasible dense solve.

The global finite-complement problem remains different: unrestricted determinant-minimizer enumeration is certified only through n3 by T10, literature/structured candidate data cover through16, and the present additional data cover an explicitly stated family through109. No minimum determinant, minimum folded count, or exhaustive all-lattice census is claimed at17..109. This is concrete bounded work in the complement, with an exact all-degree family obstruction; it does not silently turn seed data into global minima.
