# Independent supplementary review — C08 million-degree global assembly

2026-11-06. Distinct reviewer: Codex `/root/c01_review`, parent-assigned
gpt-6-astra high; actual serving identity and effective effort are not
independently exposed. Rules/input:
`4b728b04216a5490910780bc609a82b853058426`; coordinator-supplied published
head `4ca11b8`. This supplements, and does not replace, formal Claude audit.

## Disposition and frozen scope

**ACCEPTED. No unresolved mathematical finding.** For every integer
`n>=1000000`, the corrected Padua Lebesgue function has global maximum
`Lambda_c(n)=lambda_n(-1,-1)` and equality set exactly

    {(-1,-1),(1,-1)} for even n,
    {(-1,-1),(-1,1)} for odd n.

Reviewed `theory/C08-effective-million.md`, frozen SHA-256
`539502c1b64499c86917201b9046e83785066d0641aaf1d542b669c352291caf`.
The full source and full PD-T364 structural proof were read. This report
independently reconstructs the global coverage, dependency interfaces and
strict equality classification. The companion C08 far comparison was
independently reconstructed in the same bounded review, without an author
repair. Accepted component proofs remain explicit dependencies.

This is routine analytic integration with no new mechanism or novelty
content. The workflow's no-novelty exception applies; historical priority,
exhaustive IDEAS/registry checking and author-search coverage are excluded.
Only the two assigned C08 review files were written. No author source,
old report, shared record or Git state was changed.

## Exact input identities and degree interfaces

Executed hashes matched every claimed identity:

| Input | Source SHA-256 | Acceptance |
|---|---|---|
| C08 actual far comparison | `0b69e38a8d27f36228c41374b51766bd7955d0bc11d9ba6239b0171d422ba8f3` | Companion `independent-checks-C08-comparison.md` |
| C05 actual near noncorner comparison | `a0a29f76ad72abab9c44684c8793e9a7c500d12abfefce51dab9fcfed7ba5e4e` | Review SHA `b80c9380025b23314ffe7b7f9bb08c098dd8b6a9b0eedd4fa71de3ecfa7c47d8` |
| C07 actual corner comparison | `9fa0d3f3b507f1a772adda1bbc4841e42b13b7f0adada39b6ede2ab8ee5247e4` | Review SHA `d79a9568e9177bf7f9dda6b66ce509313682c953e8b537f19188ab810280c8ba` |
| PD-T364 structural source | `378548a0635206c8e61111c8ddb24b51f4b7ef1bf3cb16640da16dcf94a9e718` | Inherited accepted structural theorem; full reconstruction here |

The C07 positive-deformation source remains
`2b2870f236cf1c6ab58a01d3331c413b07b50bdbdf8e73fd839a47cd8479893c`.
It was independently reconstructed in this reviewer's earlier C07 report,
whose accepted mathematical conclusion is used unchanged here.

All three pointwise comparisons hold for every integer `n>=10^6`, including
the literal endpoint. The near theorem uses the C02 defect floor for
`n>=4096`, already satisfied. The corner result used is C07's full million
onset, not C05's older sufficient `log n>=25` consequence. The far result
is the newly proved actual primitive comparison, not merely C06's model
validity threshold or the older `exp(256)` global onset. There is no
remaining logarithmic, parity-dependent or existential degree threshold.

## Corrected kernel and exact full defect

Set `m=n+1`, `N=nm`. With `h_0=1` and `h_i=2` otherwise,

    G_n(u,v)=sum_(i+j<=n) h_i h_j cos(iu)cos(jv)-cos(nu).

Its exceptional x coefficient is one. For a physical even-board node
`(p,q)`, endpoint factors `e_p,f_q` are one half at endpoints and one
otherwise; its weight is `w_pq=2e_p f_q/N`. The corrected cardinal identity
gives `L_pq=(w_pq/4)sum_four G_n`. Subtracting the absolute value of
this sum from the sum of its four absolute values therefore defines the
nonnegative full defect exactly, rather than supplying a guessed error.

For every residue r modulo 2n,

    sum_(p,sigma: sigma*p=r mod 2n) e_p=1.

An interior residue has a single weight-one reflected preimage. Each
endpoint residue has two coincident weight-one-half preimages. The
same identity holds for the m mesh. Thus reflecting both coordinates
turns the weighted majorant into the even periodic-board sum with factor
`1/(2N)`, without an endpoint correction. Translating by any physical
odd center `(J,K)` converts that board bijectively to the odd board.
Consequently the source's exact identity is

    lambda_n=S_n(alpha,beta)-Delta_JK(alpha,beta),
    Delta_JK>=0, Delta_JK>=max(Q_v,Q_h).

The projected defects are never substituted for the full defect as an
equality and their lower bounds are not added. The common primitive
has the same normalization as the far and near theorems. Reindexing
`r -> -r` or `s -> -s`, using separate cosine evenness and periodicity,
proves separate phase evenness of S. The actual defect remains attached
to its signed physical phases and center. No mesh interchange or change
to the exceptional x mode is made.

These statements concern finite polynomials and absolute values. Kernel
collisions and initially zero terms are included without a sign-stability
assumption, quotient singularity, or limiting interchange.

## Full physical cover, including ties and boundaries

Every physical angle point belongs to a closed mesh rectangle. At the
outer boundary choose an adjacent interior rectangle. In its normalized
coordinates `X,Y in[0,1]`, the two odd vertices are opposite. Their L1
distances are either `X+Y,2-X-Y` or `1-X+Y,1+X-Y`. Each pair sums to
two, so one distance is at most one. Choosing that odd vertex supplies

    theta=(J*pi+alpha)/n, phi=(K*pi+beta)/m,
    rho=|alpha|+|beta|<=pi.

The vertex is in the physical index ranges, and the displayed angles
remain in `[0,pi]`. Boundary signs are automatic: `J=0` forces
`alpha>=0`, `J=n` forces `alpha<=0`, and similarly for beta. This is
the actual physical domain of PD-T364, not an extension of a local
chart outside the square.

No unique nearest center is required; ties may be resolved either way.
The two phase regions share the closed `rho=1/2` boundary and cover
the entire diamond. Every mesh node has even parity. Its index distance
from the selected odd center is a positive odd integer, and the cover
makes it at most one. Hence it equals one and the node has `rho=pi`.
This includes both node corners, which cannot be mistaken for zero-phase
odd corners. An odd center that is not a corner has at least one interior
coordinate, including every noncorner center on the four edges.

## Exhaustive strict comparisons

If `rho>=1/2`, the accepted C08 theorem and nonnegative full defect give

    lambda_n<=S_n<Lambda_c-6/25<Lambda_c.

It applies to every selected center class, both parities and the full
closed far boundary. No localization of an unknown maximizer is assumed.

If `rho<=1/2` and at least one center coordinate is interior, the accepted
C05 finite comparison gives

    lambda_n<Lambda_c-869/28000<Lambda_c.

Its actual finite-degree mechanism retains both legitimate near-model
allowances and C02's strict defect floor:

    1/16-1/32-3/14000=869/28000>0.

Thus a limiting-model comparison, the tighter still-open `1/4096`
tolerance, or an additional model correction is not a premise. The
accepted noncorner scope includes signed physical phases, both axes,
zero phase at a noncorner center, all edge-center classes and both
parities. The application here is pointwise on the exact radius-half
domain, without treating a box intersection as a whole-box bound.

The only remaining centers have both coordinates at endpoints. Their
odd parity pairs are exactly `(n,m)` always, `(0,m)` when n is even,
and `(n,0)` when n is odd. Set `A=|alpha|`, `B=|beta|`. Physical
admissibility gives precisely the inward corner coordinates, with
`A+B<=1/2`. C07 supplies directly

    lambda_n<=Lambda_c-(A^2+B^2).

It is strict at every nonzero inward phase, however close to the origin.
No fixed positive approximation error is used there. This conclusion
covers actual corners, unlike the projected noncorner defect bound.

## Origins, parity and equality classification

At `A=B=0` the point is the nonnode corner itself. `(n,m)` maps to
`(-1,-1)`, whose value defines Lambda_c. For even n, `(0,m)` maps
to `(1,-1)` and x reflection preserves the node checkerboard because
`(n-p)+q` has the same parity as `p+q`. For odd n, m is even;
y reflection preserves parity and maps `(n,m)` to `(n,0)`, namely
`(-1,1)`. Both reflections preserve endpoint weights and the polynomial
interpolation space, so uniqueness permutes the cardinal polynomials.
The corresponding Lebesgue functions, and hence the two corner values,
are equal. No interchange of the unequal meshes is involved.

Equivalently at a physical corner the four reflected kernel copies
coincide by evenness and periodicity, so the full defect is zero; at
an odd corner the common primitive is `S_n(0,0)=Lambda_c`. These exact
origin identities agree with the C07 normalization.

Every other point is strictly excluded by one of the three cases above.
The closed angular square maps onto the entire closed physical square,
and the cover leaves no omitted node, edge, collision or tied chart.
The maximum and equality set in the frozen global statement follow.

## Executed checks and remaining limits

Source reads and hashes checked the dependency closure. The single tiny
exact `Fraction` invocation recorded in the companion comparison report
also verified the noncorner margin `869/28000`; it exited zero. There
was no kernel evaluation, numerical integration, degree or phase scan,
certificate construction, energy extrapolation or hidden computational
premise. No further computation was needed for the cover or parity proof.

No BLOCKING, MAJOR or MINOR finding. This establishes the sufficient
analytic upper boundary `1000000`, without claiming it is minimal.
The existing exact finite range 2–40 is unchanged, the entire interval
41–999999 remains OPEN, and the all-degree target PD-T099 remains OPEN.
Formal Claude audit is still PENDING. This supplementary acceptance
does not validate a backend implementation, runtime bound or numerical
whole-box certificate.
