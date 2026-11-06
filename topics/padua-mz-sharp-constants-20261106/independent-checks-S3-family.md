# Supplementary independent check — inherited negative carrier ceiling

Date: 2026-11-06. Separate Codex mathematical checker; requested
gpt-6-astra high, runtime model metadata not independently exposed.
Rules/source: `2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861`.
Required Claude audit remains separate.

Reviewed in full: `theory/S3-carrier-family-ceiling.md`, SHA-256
`296cc8ef799d79e9ed639b71d5995d05f29e0bc360d38e5010ddae62f972eae0`.
The actual file hash matches the developer's frozen identity.

**Verdict: no unresolved mathematical finding.** The bound applies to
the entire stated fixed-parameter inherited negative packet family and
correctly excludes the full signed spectrum and varying-parameter
asymptotics. No numerical execution is needed or claimed for this proof.

## Reconstruction

- The displayed centered fourth difference is exactly one half of
  the fourth difference of h(q)=q^2 log(q) on q>0. Since
  h''''(q)=-2/q^2, four fundamental-theorem integrations give the
  stated negative integral for C(q). Differentiation is justified at
  every fixed q>2 by its positive denominator on the compact cube,
  and gives strictly positive C'(q). This is the identity previously
  read in S3-01, not an assumption about an optimizer.
- Continuity of h at zero implies continuity of the finite formula
  for C at q=2. For 2<r<q, monotonicity and the one-sided limit give
  C(q)>C(r)>=C(2). Thus J(a)>J_endpoint for every 0<a<1/2. No
  differentiation at q=2 or interchange through a singular endpoint
  integral is used.
- Direct substitution gives C(2)=28log2-18log3 and
  J_endpoint=(4log2+C(2))/2=16log2-9log3.
  The integer comparisons 65536>19683 and65536>59049 are correct;
  the latter yields J_endpoint>log3, not merely positivity.
- The strict budget a+b<1/2 yields
  ab<a(1/2-a)=1/16-(a-1/4)^2<=1/16. Combining both strict
  inequalities with A>0 and J_endpoint>0 proves each coefficient
  is strictly below U_minus. Taking the supremum correctly changes
  this to the non-strict bound sup kappa_minus<=U_minus; no attainment
  or optimality conclusion follows. Every limit of scalar coefficients
  from the interior also obeys this ceiling, without needing an
  admissible packet at a boundary parameter.
- The strict midpoint convexity bound for1/t on [1,2] gives log2>2/3;
  on [1,3] it gives log3>1. Hence A>8/3 and J_endpoint>1 imply
  9A J_endpoint>24 and U_minus<1/24. All inequalities have the
  required orientation and positive denominators.

## Scope and dependencies

The exact normalized coefficient16ab/[9A J(a)] is the accepted
PD-T379 fixed-interior-parameter result, with the prescribed carrier
coordinate on each parity and unnormalized dxdy measure. Its
denominator is essential. The bound does not transfer to arbitrary
negative packets, superpositions, changed envelopes, the positive
family, or parameters depending on degree; the theorem explicitly
retains these exclusions.

The rational comparison0.0915=183/2000>1/24 is correct. It demonstrates
that retuning this scalar family cannot produce that limiting trial
coefficient. It neither identifies the reported finite fitted number
with a true spectral limit nor explains the entire finite spectral
branch. No fit was read or run in this check, and the compact-operator
proof is neither changed nor used as a premise.

This audit addresses mathematical validity only, without novelty,
priority or literature assertions; the workflow exception to reading
the full ideas registry applies. The unchanged accepted carrier formula
and the explicitly reconstructed finite-difference identity are the
only substantive mathematical dependencies.
