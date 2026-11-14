# C06 partial cotangent backend — independent implementation check

2026-11-06. Rules/input `b6e67b3c78cb668b6d2f9da5a5560537d2960bf3`;
base `f654e32daff27b6846849311092f6daebbbf235b`.
Distinct Codex reviewer, assigned Astra high supplementary review;
actual serving model/effort metadata independently unexposed. Read
AGENTS, WORKFLOW, CODEX, handoff06, the C06 attempt/source/header/driver
and receipt, the snapshot builder, C02 theory and its completed independent
mathematical review. No author, shared, old review or Git state was changed.
Formal Claude audit remains separate.

**ACCEPTED within the frozen partial-cotangent backend scope on the
recorded x86-64 LP64 target. No unresolved enclosure finding.** This
acceptance covers successful calls to the native Arb interface, including
interval inputs passing its guards, with the explicit analytic and
arithmetic radii retained. It neither promises success/tightness for all
valid balls nor supplies a complete one-point S evaluator. Whole-box
branches, gradients, corner-orbit and defect interfaces remain OPEN.

This is an implementation check of already accepted C02 mathematics,
without historical novelty, priority, new mechanism or literature claims;
the full registry/literature novelty gate is outside this declared scope.

## Frozen identities and executed controls

Reviewed sources in `code/cheap_rows_C06/`:

| File | SHA256 |
| --- | --- |
| partial.cpp | `f381738049d793e81a93626bef11eeb1d2a0ff49d0027b6518dd3fec8ff0bcf0` |
| partial.h | `b053eafcf79a77ab4d8fd921c8bb1c25a5e4b15312ecdeee0518855579b3771d` |
| control.py | `8a7d48848510915508528a3849fef11f5b01341319ce2103466bdaba608064aa` |

The C02 mathematical input is `theory/C02-row-cotangent.md`, SHA256
`820e655e0df600299767b32712f2290d973c11d83f6d676a32daa3e36d11b4a8`,
with accepted reconstruction in `independent-checks-C02-row.md`.
The developer receipt `evidence/c06-rows-partial.json` is 2293 bytes,
SHA256 `97ede1e9c40838e9ecb67b155730bb9c1fcf6afa3f7998d889db44d9803f5570`.
An independent recursive byte-size/SHA256 check of that receipt and its
local raw manifest verified all 230 encountered identity records. This
was identity verification, not a rerun of the developer's controls.

Independently executed once:

    python topics/padua-argmax-bridge-20261105/code/cheap_rows_C06_review/control.py

Exit0, **PASS**, 2.685291 parent-plus-child CPU seconds including fresh
compilation, below the 90-CPU-second budget. Python3.12.14;
x86_64-linux-gnu-g++-14 Debian14.2.0-19; `sizeof(long)*CHAR_BIT=64`.
No random inputs or seed. This compiles the exact frozen implementation
into a new review translation unit, includes its public header, and calls
the native `c06_partial_arb` entry. It does not load the author's binary.

The 76 cases comprise 54 complete endpoint-image containments, 15
invalid-input rejections, five empty-block cases, and two maximum-integer
symmetry controls. Small direct-reference cases use n=2,3,7,32,33,64,
including q=31,32,33 around the harmonic transition, full/interior/single
blocks, removable cell endpoints, intervals of several widths, and both
poles with 1e-30 distance. Two singleton references additionally exercise
n=2147483647 near each side. Two exact symmetry cases at this largest
supported n use q=n,y=1/2 and q=n-1,y=1 and check containment of zero;
they do not enumerate billions of summands or certify that degree.

For every direct-reference case, the reviewer extracts both exact Arb
input-ball endpoints with outward 512-bit rounding, evaluates the full
direct cotangent sum independently at each endpoint at 512 bits, and
forms their hull. On the guarded domain every summand is decreasing in y,
so this hull encloses the entire input image. All 54 such reference hulls
are contained by the returned backend ball. Input/output aliasing also
returns the identical ball in all 54 cases. This is stronger than checking
only a midpoint or interval overlap, but remains a finite measurement.

Invalid cases cover nonpositive pole distances, balls crossing a pole,
NaN/infinities, invalid n/q and native LONG_MIN/LONG_MAX. All 15 return
failure and a nonfinite native output. The five q=0 cases, including NaN
and infinities in y, return exact zero as the explicit unconditional empty
contract permits. Independently computed rational direct moments for
degrees0 through97, n=2,7,33,64 and q=1,n give 784/784 containments.

Small retained evidence: `evidence/c06-review-rows.json`. Its manifest
pins both reviewer source files, the unchanged builder, compiler/binary,
and local raw `c06-review-rows/check-t0i44d6x/review.json` (59894 bytes,
SHA256 `a3ce297902ee261c0d7957a1fc8ab0ea52ef5c46c518b8139dc44dbf3ef8e882`).
The raw record includes all case values and the full closure: 182 source/
header identities, four compiler tools, 13 tool dependencies, eight
linked dependencies and eight actually mapped runtime dependencies.
Loaded identities match before/after execution; frozen author-source
hashes match before/after. The preprocessed translation unit includes
the pinned author source/header, and its bytes are checked across the
compile. Raw material remains local; physical cold-storage transfer is
pending, with no remote archival claim.

## Mathematical and code reconstruction

The integer guard in partial.cpp:53 runs before q-1 or any arithmetic
requiring a valid n. It restricts 2<=n<=2147483647 and 0<=q<=n. The two
strict Arb positivity guards certify every represented y satisfies
0<y and y+q-1<n. For q>0, nonfinite inputs cannot pass both guards.
These inequalities place every normalized sample z_i in (-1/2,1/2),
and both centered cell endpoints in (-3/4,3/4). Guards may reject a
valid but numerically unresolved ball; rejection is not an enclosure.

The rational tangent recurrence has t0=1 and the correct division by
2j+1. Coefficients `2^(2j+3)/pi-t_j*pi^(2j+1)` agree with C02's combined
residual coefficients. All cancellation occurs within Arb640 enclosures;
subsequent Arb160 operations retain their input radii. No inaccurate
coefficient midpoint is silently treated as exact. The initialized static
coefficient vector is read-only after C++'s guarded initialization.

For the exact moment recurrence, integrating each centered cell gives

    [zr^(d+1)-zl^(d+1)]/((d+1)s)
      = M_d + sum_even k>=2 binom(d,k)(s/2)^k M_(d-k)/(k+1).

The implementation has the matching binomial recurrence, powers, sign,
degree and denominator. It computes this at the exact rational Arb
midpoint, not a rounded decimal or binary64 surrogate. Throughout the
input ball, |M_d'(y)|<=d*q*2^(1-d)/n, since every |z_i|<1/2. The code
converts the input radius exactly to an Arb midpoint and adds this
derivative bound times that radius. Thus the exact midpoint calculation
and its interval extension are both valid, including even moments whose
derivatives change sign. Its rational bit complexity is not constant.

The assembly uses degree d=2j+1 for the polynomial sum, d+1 divided by
d+1 for the normalized integral, and d-1 times d for its derivative.
Multiplication of the normalized integral by pi and division of the
normalized derivative by pi are correct. The correction sign is
`-h/24`; the reversed second pole progression starts at n-y-q+1. Thus
partial.cpp:60 implements C02(1) without a missing pi factor or sign.

For q>K, the harmonic tail uses log(z/x), (1/x-1/z)/2 and the Bernoulli
corrections B_(2r)/(2r)*(x^(-2r)-z^(-2r)), through r=16. The added
|B32|/(32*32^32) is the proved periodic-Bernoulli remainder bound, not
a presumed next-term estimate. Each harmonic ball gets its own radius;
their difference divided by h carries both. For q<=32 there is no
harmonic truncation. Every harmonic production loop has at most32
iterations, irrespective of n or q.

The smooth remainder added at line61 is exactly
7*q*h^4*M48/5760, with the C02 constant and exponent4^-48. It is added
to the final Arb ball, alongside all arithmetic and harmonic uncertainty.
The implementation does not silently use the much smaller J96 theorem.

W is log(sinc(x)/(pi-x)) with a valid reflection x->pi-x when the whole
ball lies above pi/2. Its identity and its removable endpoint values
agree with C02. Arb's sinc supplies the removable zero value. A broad
ball can make the quotient/log enclosure fail; the final finiteness
guard then returns failure instead of an invalid enclosure.

For w', differentiate the combined residual series and bound its tail
at |z|<=3/4. The coefficient bound gives

    |tail| <=16/(9*pi^2)*sum_(j>=97)(2j+1)*4^-j
           =16/(9*pi^2)*4^-97*(195*4/3+8/9).

Both endpoint derivative balls receive this radius; multiplication by
h/24 carries the total h/12 charge. Interval dependency may widen the
endpoint polynomial evaluation beyond the exact domain, but its
polynomial part still encloses the true endpoint values and the added
tail bound applies to those true endpoints. No omitted numerical tail
or differentiation of an unvalidated approximation was found.

## Interface and scope notes

All Arb operations take explicit160/640 precision; the reference takes
512. There is no mutable global precision setting. RAII owns ordinary
Arb/rational temporaries. Native C++ exceptions, including std::bad_alloc,
are caught at the native interface and produce an indeterminate output;
no exception is intentionally passed through the C boundary. This is
not a guarantee that allocation failure inside a C dependency cannot
abort the process. No allocation-failure injection was performed.

The binary64 string wrapper is diagnostic: bounds round down/up and the
full Arb radius is reported, but consumers must check its return code.
`c06_budget` and `c06_compare` are unguarded/reference diagnostics outside
the public native contract; the q-sized reference loop is never called
from `partial` or `c06_partial_arb`. Null or uninitialized C pointers are
outside the valid native Arb object contract.

**NOTE — platform scope.** The expression `7*q` in lines61 and68 is safe
on the recorded 64-bit-long target: at most15032385529. It would overflow
a signed32-bit long near the supported maximum q. This review therefore
does not approve an ILP32/LLP64 build under the same header contract;
such a port should use an explicit width guard or multiply in Arb.
No source change is necessary for the frozen LP64 target being accepted.

The historical 2.6e-4 radius from the original moment recurrence remains
preserved in the author's attempt. The corrected 1.16e-24 regular-case
radius is consistent with the explicit J48 smooth budget. The large
absolute radius near the right pole is valid conditioning of a160-bit
input near n, not an absolute-accuracy result or a failed containment.

There is no new full-board/cover execution, no certified-degree extension,
timing extrapolation, all-row error-budget implementation, or completeness
claim. This partial-sum acceptance leaves guarded arc-to-index conversion,
sign/pole/parity assembly, retained/direct primitive radii, all-row
normalization, point S, gradients, corner and defect machinery OPEN.
