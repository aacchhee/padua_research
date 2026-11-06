# PD-T?argmax-bridge-codex-D10-farconstant — A quadratic phase factor away from the origin

ID kind: PD-T. Aliases: far relative true-constant budget; twenty-two times one-minus-a.
Split into: none. Global, near and negative scopes have separate records.

Rules/input `9d5e8c7a1a8fab6017d5dd9406daec0d834b0bbf`; latest main
`64409c47a717aef074f611b31a9fd48b7a15101b`. Parent-assigned Sol xhigh;
serving metadata unexposed. **PROVED**, analytic developer result, distinct
review required. Exact real arithmetic; no NEW numerical execution.
The origin lower retains accepted PD-T271's computer-assisted Arb enclosure
with its analytic coefficient reduction and exact tail, as documented in
[D08 constant provenance](../attempts/D08-corner-limit.md).

Split from: original combined D10-relative-constant first freeze, whose
EXACT complete text is preserved at
[attempts/D10-relative-constant-first-freeze.md](../attempts/D10-relative-constant-first-freeze.md),
SHA256 `56c69c6e39fc0fddf9ada3505c99c293d89fe56d74c2c1a7aa1d643d30c697af`.
This is a substantive split, with no new mathematics or altered constants.
Mapping/history: [attempt](../attempts/D10-relative-constant.md).

## Statement

For D02's TRUE completed constant, every signed phase in the CLOSED FAR
domain1/2<=|alpha|+|beta|<=pi satisfies

    C_infty(alpha,beta)-C_infty(0,0)<22(1-a),
    a=[cos(abs(alpha))+cos(abs(beta))]/2.

Status: PROVED, analytic developer consequence, independent review required.
This is a standalone substantive dependency for the parent's NEXT prospective
finite-onset budget; it is not itself a finite-degree or onset theorem.

## Dependencies and proof

Use the global phase-aware bound in
[D10-global-constant.md](D10-global-constant.md), and the accepted PD-T271/D02
origin lower C_infty(0)>4383/2420. In the following preserved proof, take
nonnegative absolute phases, rho=alpha+beta, u=1-a and p=sin alpha.

### 5. A useful quadratic factor on the closed FAR domain

The accepted D08 normalization, using PD-T271 and kappa_shift>3/2,
gives C_infty(0)>4383/2420. The phase-aware upper above therefore
implies

    C_infty(phi)-C_infty(0)<8/15-(46/125)u+(9/20)p,

because320/197+89/125-4383/2420<8/15. Here no finite
Lambda_c inequality is inferred from a limiting constant. For rho>=1/2,
the cosine alternating bound gives u>=191/6144>31/1000. Also
u>=sin^2(alpha/2), hence p<=2sqrt(u). Consequently

    [C_infty(phi)-C_infty(0)]/u
        <(8/15)/u+(9/10)/sqrt(u)-46/125
        <8000/465+36/7-46/125<22.

For the middle inequality use u>31/1000>(7/40)^2. The last
comparison is rational. This proves(5a) on the entire closed FAR
domain, including a=0. No extension through u=0 is asserted.

## Scope and history

The origin lower is a LIMIT constant identity, not a finite Lambda_c lower.
All closed far phases, vertices, axes and continuous weighted collisions are
included. No statement through phase zero is made; the separate fractional
obstruction applies there. Full finite S-aS(0) stays OPEN and the current
accepted50000 theorem is unchanged. A new budget must be preregistered after
independent acceptance. No mathematical computation or new proof step occurred
in this split. 2026-11-06: root requested a separate substantive record because
another planned result will depend directly on this far conclusion.


### Supplementary review closure — 2026-11-06

Distinct Astra xhigh reconstruction ACCEPTED the preceding unchanged
final split scope; no unresolved findings. See
[independent-checks-D10-relative-constant.md](../independent-checks-D10-relative-constant.md),
report SHA256bdcadf119fb905f898612ad25b9123bf8ff58184d6ef573e1503a740d987964c.
The substantive split, inherited-Arb provenance and cutoff-domain wording
findings are closed there. This records no new analytic onset or finite
certificate. Final Claude review remains pending.
