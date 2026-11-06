# Independent supplementary check — P1 coarse rectangle instance

Rules/input: `0205690b9c4e959a28e949083e9a1808735abf4b`.
Published source/protocol: `c1e6e59dd9155b87d9847155d3455d602a5f84e9`.
Reviewer: distinct Codex supplementary agent, requested `gpt-6-astra` high;
actual serving-model and effort metadata are unexposed. Date: 2026-11-06.

**Outcome:** inspected arithmetic and actual independent N16/theta256
rerun support the stated coarse computer-assisted enclosure. All exact
endpoint integers agree with the developer result. No unresolved
mathematical or implementation finding remains at this scope.

    0.013164946500379018110831 <= ||B||
                              <= 0.477809279990884889210594.

For c_minus=-||B|| reverse the endpoints and signs. This certifies no
three-digit value and supplies no separate c_plus approximation; only
its inherited positivity and the same norm upper bound apply. The
focused Claude audit remains separate.

## Read coverage and provenance

Read P1_rectangle.py, ideas/P1-numeric-protocol.md,
theory/P1-numeric-certificate.md and both developer receipts in full.
The kernel, positive-spectrum and finite rectangle reduction were
independently reconstructed in independent-checks-P1-kernel.md. The
unchanged interval_dyadic.py and Machin enclosure were inspected in
independent-checks-P4.md.

Independently fetched the numerical source and original protocol at
c1e6e59, verified their Git blob hashes and matched the source bytes.
The current protocol differs only in completed-run status metadata and
a completion pointer; its exact numerical protocol is unchanged. This
explains the differing protocol prose hash in the independent rerun.
It is not a source, grid, threshold or arithmetic change.

| Item | SHA-256 |
|---|---|
| code/P1_rectangle.py | c65b45fc2d4748e21ae7540bb47824dbc033f0d22917e49ac68084b7c1652963 |
| code/interval_dyadic.py | 8a90618d19ffd8f8efde50bc9002b0b0e26f62d243b4086c674cedcf657945fc |
| Original numerical protocol | 568fc2b9f2de6b328d4d2d69980302aba984cac425b43e8c09fd6c31c49d647f |
| Protocol at independent execution | 16db3990af40fe4bf87f13519aa88c27a5e2d647d187741467b66d676e2538a4 |
| Rectangle reduction | 4cee5449c0b1634e4d868a41c474b0c938a5394bc87e8f45e197219508a911a9 |

N8/theta64 had 0<L<U and used 0.117550468 CPU seconds, satisfying the
published trigger for N16/theta256. I read the N8 result; I did not rerun
it. No third grid or improved trial was introduced.

## Scalar and finite-sum reconstruction

The positive square-root helper returns floor(sqrt(max(lo,0)*2^256))
and the corresponding ceiling for the upper endpoint, using integer
isqrt and exact-square detection. It therefore encloses the positive
square root on the full input interval. The dedicated square helper
sets its lower bound to zero when the input crosses zero; otherwise
it takes the smaller endpoint square. Both endpoints are rounded
outward on the dyadic grid.

Cosine uses its entire even Taylor series. The next-term ratio
x^2/((2k+1)(2k+2)) decreases in k, so twice the next positive term
bounds the remaining absolute tail once the ratio is at most one
half. Interval widths are retained through cancellation. Intersecting
with [-1,1] is valid. Exact angular endpoints lie in the computed
pi-dependent endpoint intervals; monotonicity of cosine on the true
[0,pi] then encloses every entire angular cell, not just its midpoint.

For every target/source bin and t=0,1, interval multiplication and
the dedicated square enclose (t-a cos(theta))^2 for every target a and
every angle in that cell. Each square root is outward bounded. Their
difference is safely intersected with the previously proved range
[0,sqrt(v^2-u^2)]. Summing and multiplying by kappa_t/(pi*T) is exactly
the scalar source integral prefactor kappa_t/pi^2 times angular
width pi/T. Full target-bin evaluation already encloses target
variation, so an additional omitted Hölder term is not required.

For uniform N bins, i+j<N selects precisely the rectangles whose
intersection with D has positive measure, while i+j<=N-2 selects
rectangles contained in D up to null edges. The upper calculation
includes all outer source and target cells. Positivity permits full
source rectangles crossing the slanted boundary to overestimate their
intersection. The maximum row upper endpoint is therefore a Schur
upper bound for h=1.

The lower calculation retains only inner target/source rectangles.
The source mass is already integrated into I_t. It multiplies each
product by the target-bin masses (2i+1)/(2N^2) exactly once, then sums
the positive contributions. Dividing by the full-D norm squared
integral_D ab da db=1/24 is correct even though the numerator drops
boundary cells. This gives the Rayleigh lower bound. All operations
use exact rational or outward dyadic arithmetic; no floating
quadrature or elliptic special-function value is a premise.

## Actual independent rerun

Executed after publication and coordinator authorization, from
/workspace/sharp-work:

```sh
python topics/padua-mz-sharp-constants-20261106/code/P1_rectangle.py --N 16 --theta 256 --output topics/padua-mz-sharp-constants-20261106/evidence/check-P1-independent-N16.json
```

Exit 0; 1.677272098 wall seconds and 1.677119789 CPU seconds. Python
3.12.14 and platform are recorded in the receipt. Its SHA-256 is
`6557a68428a6a31708485f4506808a0d9dff3eff156673991b30c83c053cc909`.
The exact r and c_minus endpoints, grid, 136 outer cells, 120 inner
cells, norm 1/24, source/arithmetic/reduction hashes and positive-lower
flag all agree bit-for-bit with the developer N16 receipt. The only
provenance-hash difference is the disclosed protocol completion text.

This was an actual distinct same-code execution after inspection, not
an independently implemented scalar library. Trusted dependencies are
the reviewed analytic reduction, inspected code, Python unbounded
integer/Fraction/isqrt semantics and the recorded runtime. The exact
enclosure is coarse; neither a finer grid nor an unrecorded positive
trial was tested. No numerical feasibility beyond these fixed cases
is inferred.
