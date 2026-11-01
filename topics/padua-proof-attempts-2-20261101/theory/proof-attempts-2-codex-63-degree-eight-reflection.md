# PD-T?proof-attempts-2-codex-63 — Exact degree-eight x-reflection identities

ID kind: PD-T.
Aliases: n8 x-reflection; ordinary witness proposal by node permutation; no symmetry acceptance predicate.
Split from: supporting algebra for the degree-eight A5 attempt61.
Split into: the finite strict count61 and global-value assertion62 remain separate OPEN results.

## Statement

For the45 degree-eight Padua nodes
`z_(j,k)=(cos(j*pi/8),cos(k*pi/9))`, `0<=j<=8`, `0<=k<=9`, `j+k` even,
let `pi(j,k)=(8-j,k)`, `T(x,y)=(-x,y)`, and `D=diag(-1,1)`.
For their total-degree<=8 cardinal polynomials `L_i`,

`L_i(Tz)=L_pi(i)(z)`, and consequently `lambda_8(Tz)=lambda_8(z)`.

If a sign mask `s` is permuted by `(pi s)_pi(i)=s_i`, then

`P_(pi s)(z)=P_s(Tz)`,
`grad P_(pi s)(z)=D grad P_s(Tz)`,
`H_(pi s)(z)=D H_s(Tz) D`.

Thus exact stationary and strict-local-maximum witnesses have reflected proposals: reflect the x-coordinate of root/hull boxes and exact points, permute masks, and replace a rational preconditioner `C` by `D C D`. Widest-side binary paths reflect by complementing bits at x-splits (indices0,2,4,...). Complete coverage of the negative half-square and its reflected ordinary proof records cover the whole square. Every serialized record still requires its original independent predicate check; this statement introduces no verifier shortcut.

For an axis-crossing root, suppose additionally that the mask is unchanged by pi, both root witnesses are valid for that SAME signed polynomial, and its gradient is injective on the convex hull of `R` and `T R`. Then their unique critical points coincide and lie on x=0. Reusing an existing ID is justified only with this exact uniqueness proof and valid injectivity checks on every enlarged leaf/reference hull. Proximity or overlap alone does not imply equality.

## Definitions

`P_s=sum_i s_i L_i`, with every `s_i` equal to+1 or-1. Root and leaf predicates are those of18/53 and the frozen n8 schema. The independent checker reconstructs the cardinals by exact Vandermonde inversion, rather than trusting a reflection assertion supplied by the producer.

## Assumptions

The stated node set, degree<=8 polynomial space, exact cardinal identities/unisolvence, and the physical FIELD12 embedding60. The optional axis-reuse conclusion assumes the existing full root and gradient-injectivity predicates, rather than an unverified geometric coincidence.

## Status by part

Overall status: **PROVED** (written analytic identities and their stated conditional witness consequences). Required Claude audit PENDING. No finite maxima count, complete half-square certificate, successful boundary census, or global argmax is asserted here. Results61/62 stay OPEN.

## Depends on

Cardinal interpolation/unisolvence: literal required source dependency `PD-T?proof-attempts-codex-01 (audit pending)`; dated qualification2026-11-01: its accepted Claude audit and dispositions are complete, mathematical source unchanged, now also aliased PD-T101. Exact finite cardinal reconstruction is separately checked in60 and the independently owned checker. Generic injectivity/root correctness is18; universal-gradient records use53. No new hypothesis from the floating source's symmetry observations is inherited.

## Checks

The proof below is analytic. The bounded developer reflection pilot additionally checked all45 coefficient identities exactly, path/mask/box/preconditioner involutions and fail-closed controls on an explicitly incomplete fixture. Its receipt is `../outputs/a5_n8_reflection_controls.json`. The separate verifier's ACTUAL11.099s preflight independently reconstructed all45 full coefficient/node identities from its own formal-field/Vandermonde cardinals and reverified the nine current root boxes, all strictly left of the axis; no axis test or merge was applicable. Exact record `../outputs/a5_checker_n8_reflection_preflight.json`,7945bytes SHA256 `426c4131ff63441f2175b4b37ee88772c0392f4ceb9f9fc2fba04f304f1a3634`; receipt `../independent-checks-a5-n8-reflection.md`. Its subsequent reading of this full analytic file is a supplementary scope check, not a full analytic audit. The actual separate proposer/checker executions are recorded below. These checks supplement the required Claude audit and do not supply a count.

Those two supplementary execution obligations subsequently passed. The actual different-agent proposer-controls execution passed45coefficient identities and6fail-closed controls from its OWN cap artifact, all ten pinned sources unchanged. Exact comparison found identical field/node/root/disposed-leaf fields between the independently generated small proposals (`../outputs/a5_n8_reflection_comparison.json`). The fixed developer fixture was then literally accepted as supplied witnesses by unchanged checker `a9cff574…` in174.316s: all45cones/3474breakpoints,18disjoint root records,8leaves/516ordinary records,2centered universal leaves and2node leaves. Its incomplete partition/no-boundary/count=false status was retained. Exact checker output copied without modification to `../outputs/a5_n8_reflection_checker_fixture.json`,5829bytes SHA256 `4c4c0d06e4c711873c4853167298fed2d092aeb0bb469b0c0b5027805adf3b46`. This proves no full n8 count; full artifact obligations61/62 are unchanged.

## Sources and gate

The complete original relaxed gate and current mechanism addendum are in Candidate5 of `../attempts/T-A5-n8.md`. Closest records: IDEA206/PD-T100 (A5 remains uncertified there), IDEA048, IDEA058, and the n4 reflection-orbit implementation advice in `../independent-checks-a5-reduction.md`. This is standard coordinate relabeling used to construct witnesses for an existing target. No novelty or priority claim; no y-reflection identity is asserted.

## Proof

The map pi preserves the checkerboard because `(8-j)+k` has the same parity as `j+k`. It is an involution, and the trigonometric identity `cos((8-j)pi/8)=-cos(j pi/8)` gives `T z_i=z_pi(i)`. Composition with T preserves the total-degree<=8 polynomial space. For every node z_h,

`(L_i composed with T)(z_h)=L_i(z_pi(h))=delta_(i,pi(h))=delta_(pi(i),h)`.

Uniqueness of cardinal interpolation therefore gives `L_i composed with T=L_pi(i)`. Summing absolute values yields the stated invariance of lambda. Relabeling the finite signed sum proves the P identity, and the chain rule proves both derivative identities. T is an isometric homeomorphism of the closed square and preserves its interior, edges and corner strata. Consequently it carries strict relative local maxima bijectively to strict relative local maxima. This does not determine how many there are.

The Hessian relation is a congruence by D, so negative definiteness is preserved. If C is a source preconditioner and `C'=D C D`, then

`I-C' H_(pi s)(z)=D [I-C H_s(Tz)] D`.

Conjugation by D preserves the infinity operator norm. The exact Krawczyk expression similarly reflects when its centre, box, gradient and Hessian enclosure are reflected. This supplies candidate witnesses. Actual outward interval evaluation, exact cardinal signs, Krawczyk inclusion, whole-hull injectivity and root disjointness must nevertheless be recomputed by the unchanged checker; no assumption that two implementations produce byte-identical intervals is required.

Starting from a square, widest-side splitting with x on ties alternates x,y by depth: after each pair of splits the two side lengths again agree. Reflecting x therefore complements precisely the even-indexed path bits. Induction on the word length gives `Q_reflected-path=T Q_path`. Prefix disjointness is preserved. If the stripped negative-half words form a complete binary prefix partition, adjoining their reflected words gives a complete prefix partition of the whole square. Every ordinary implicit mask list must still be permuted and sorted, with its newly recomputed compatible masks checked exactly. An actual node-cone record is retained only after strict containment in the actual stored target cube is checked anew; rounding of algebraic node centres does not authorize copying cube containment without that check.

For the optional axis case, let p and p' be the unique critical points in R and T R. The same-mask reflection identity gives p'=T p. Gradient injectivity on their convex hull implies p=p', hence p lies on x=0. One sufficient existing injectivity check is an invertible rational C with `sup_U ||I-C H(z)||_infinity<1`. Indeed, if `grad P(u)=grad P(v)` for u,v in convex U, integrate the Hessian along the segment to obtain

`||u-v||_infinity <= q ||u-v||_infinity`, with q<1,

so u=v. This proves exact reuse under the stated hypotheses. Each new reference hull must contain the selected stored root box and satisfy its own original injectivity predicate. Neither overlap nor a distance threshold establishes these conditions.

## Scope

Degree8 and x-reflection only. Complete counts and all global values still require61/62 and their full finite evidence. Current helper implementation takes the simpler fail-closed route for any axis-crossing root or unsupported non-left reference; the optional analytic reuse lemma is not silently treated as an executed implementation.

## Open items

Independent analytic audit; complete negative-half coverage if available at the current registered cap; all final count/boundary/global checks; required Claude audit. Bounded actual different-agent reflection pilot and unchanged-checker small-fixture replay are completed supporting checks.

## History

2026-11-01, Codex `/root/a2_develop`, requested gpt-6.1-sol xhigh (resolved runtime metadata not separately exposed). Gate and kill criteria preceded the reflection pilot. Written separately as a supporting analytic result; does not upgrade61 or62.
