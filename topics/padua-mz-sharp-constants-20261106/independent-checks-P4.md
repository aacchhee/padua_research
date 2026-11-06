# Independent supplementary check — P4 exact Rayleigh lower bound

Rules/input: `0205690b9c4e959a28e949083e9a1808735abf4b`.
Published numerical protocol and source:
`d03e74dcf94020ba26d9fae84d3ff6c5519db901`.
Reviewer: distinct Codex supplementary agent, requested `gpt-6-astra` high;
actual serving-model and effort metadata are unexposed. Date: 2026-11-06.

**Outcome:** the finite reduction, scalar enclosure proof, arithmetic
implementation and independently executed grouped check support the
computer-assisted one-sided claim **Lambda_edge >= 1.0044369**. No
unresolved mathematical or implementation finding was found at the
identified sources. The focused Claude audit remains separate.

This proves a lower bound on the infinite variational norm. The narrow
two-sided interval below encloses only the exact chosen finite trial's
Rayleigh quotient, not Lambda_edge itself. No sharp upper bracket, full
decimal evaluation, finite-N onset or registry mapping follows.

## Coverage and frozen inputs

Read attempts/P4.md, ideas/P4-rayleigh.md, interval_dyadic.py,
P4_rayleigh.py and P4_check_grouped.py in full; checked the accepted S2
variational definition, closed C/D formulas, positive finite Gram matrix
and qualitative norm identification. This is the technical proof and
execution check of the fixed supplied certificate. It makes no new
novelty/priority claim or independent complete-registry-search claim.

Independently retrieved the protocol and all three source files at the
published commit through GitHub, verified each Git blob hash and compared
the returned bytes to the working files before execution. The protocol
subsequently acquired completed-run status and an explicit dated outcome;
its prospective numerical instructions and scalar proof were unchanged.
The original protocol hash is correctly retained in the producer receipt.
All three code files, the trial and producer receipt were unchanged at the
end of the independent execution.

| Input | SHA-256 |
|---|---|
| Published attempts/P4.md | 101bc61acd673f71195b1e0c002101106f1e6d15dbc7b2b679eb614807d84a77 |
| code/interval_dyadic.py | 8a90618d19ffd8f8efde50bc9002b0b0e26f62d243b4086c674cedcf657945fc |
| code/P4_rayleigh.py | 7bcf4032590cf07c12943ecd5b9bf1f3cef18f32240d884acba60ad5047947eb |
| code/P4_check_grouped.py | 63d53b6686e0a5259cab30bbb233d9ad8ad566283ae3f257bfb4411e455f4163 |
| evidence/P4-trial-J512.json | a472d397b6a802d7bfe9c06bdb25d2f572d18134726b8dad9f695772f0956da8 |
| evidence/P4-rayleigh.json | a4807c3b928e8f169f6f999f2284c82991fe7535e13d6001d67fd3bb36edfe07 |

## Mathematical reconstruction

The accepted definition is the supremum over finite nonzero vectors of
u^T D u/(u^T C u), with C_ij=integral t f_i f_j dt and positive definite
C. Any single exact nonzero vector is enough for a lower bound. The
approximate generalized eigenvector is only a way to select that vector;
its numerical eigenvalue, accuracy and optimality have no proof role.
The certificate reads its hexadecimal binary64 values as exact rational
components. The denominator is directly enclosed and proved positive.

I independently checked the closed C formula as well as matching it to
the accepted record. Write alpha=pi*i and
I(alpha)=integral_0^alpha sin^2(t)/t dt=Cin(2alpha)/2. At an integer
multiple of pi, partial fractions and shifts t by plus/minus alpha give

    H(alpha)=integral_0^infinity sin^2(t)/[t(t^2-alpha^2)]dt
            =-Cin(2alpha)/(2alpha^2).

The shifted cutoff terms cancel as the cutoff tends to infinity. The
removable pole at alpha causes no principal-value ambiguity because
sin^2 vanishes there. Partial fractions of the product with alpha and
beta give exactly the stated off-diagonal C_ij. On the diagonal use

    alpha^4/[t(t^2-alpha^2)^2]
      =1/t-t/(t^2-alpha^2)
          +(alpha/4)[1/(t-alpha)^2-1/(t+alpha)^2].

The first two terms contribute Cin(2alpha)/2 before multiplication by
4. The difference of squared-pole integrals is
2 integral_0^alpha sin^2(t)/t^2 dt=2Si(2alpha), by integration by parts
and sin(alpha)=0. This gives C_jj=2[alpha Si(2alpha)+Cin(2alpha)].
The quotient numerator is exactly the accepted diagonal omega term plus
4 times the squared signed component sum; no mass or endpoint factor is
lost.

For the new scalar identities, differentiation under the exponentially
convergent F,G integrals gives F'=-G and G'=F-1/x. Therefore
pi/2-cos(x)F-sin(x)G has derivative sin(x)/x. At zero F tends to pi/2
and sin(x)G tends to zero, so this is Si(x). Likewise sin(x)F-cos(x)G
has derivative cos(x)/x and tends to zero at infinity, identifying Ci.
At n*pi the trigonometric factors are exact parity signs. Expanding
1/(1+t^2) by the finite geometric identity leaves the stated positive
even-order remainder. Its integral is bounded by the first omitted
factorial moment: 40!/x^41 for F and 41!/x^42 for G. These are finite
exact identities with bounded remainders, not a convergent-asymptotic
series assumption.

The Si and Cin Taylor terms and their recurrences match their entire
power series. In both recurrences the unsigned ratio has the form
x^2 t/[(t+1)(t+2)^2] with t increasing by 2. Its difference from the
next ratio has positive numerator
4t^3+22t^2+28t-8 for t>=1. Thus after the certified ratio is at most
one half, twice the next term bounds the whole remaining unsigned tail.
Severe finite-sum cancellation does not invalidate an outward interval
sum. The Cin anchor formula also follows directly by subtracting the
derivatives of Cin, log and Ci; no numerical Euler constant is needed.

Power-of-two range reduction keeps the logarithm argument in [1,2].
The atanh parameter is then in [0,1/3], and the stated geometric tail
dominates the remaining positive series. Machin's identity has the
correct factors 16 and -4. In particular tan(4 atan(1/5))=120/119,
and subtracting atan(1/239) gives tangent one on the first-quadrant
branch. The alternating arctangent remainder is bounded with its next
term's correct sign.

## Code inspection

The interval endpoints are arbitrary-precision integers on a fixed
2^-256 grid. Fraction conversion uses exact numerator/denominator
arithmetic. Multiplication takes the four exact endpoint products and
rounds outward; division checks exclusion of zero and likewise bounds
all endpoint quotients, handling a negative denominator by sign reversal.
Addition and subtraction are exact on this grid. No rounding-to-nearest
operation is used to certify a bound.

The Taylor implementation retains accumulated endpoint widths and adds
an unsigned tail radius. The Laplace recurrence produces the omitted
40! and 41! terms after exactly 20 summands and adds those positive
remainders only to the upper endpoint. The logarithm and Machin
implementations follow the inspected remainder proofs. Output decimal
strings are themselves rounded outward and are only human-readable
views of the decisive integer endpoints.

The producer and grouped checker use the same scalar interval module,
which was explicitly inspected here. Their form assemblies differ:
the producer encloses each C_ij term separately; the checker first
collects the rational coefficient of each d_j. For i<j, the pair
coefficient is 4(-1)^(i+j)u_i u_j/(i^2-j^2), contributing i^2 times
that value to d_j and minus j^2 times it to d_i. This exactly matches
the inspected quadratic form. Exact target comparison is
quotient.lo*10000000 >= 10044369*2^256.

Trusted computation consists of the inspected Python code, Python's
integer/Fraction and JSON/hex parsing semantics, and the recorded runtime.
NumPy/SciPy are used only to select the finite trial; the rigorous check
imports neither. This was a distinct execution of the supplied alternate
assembly, not a claim that the reviewer independently implemented the
shared scalar library.

As an additional input check, I parsed all 512 hexadecimal components
directly into rational integers/powers of 16 and 2, without float parsing,
and compared them with the checker's Fraction(float.fromhex(...)) values.
Every component agrees exactly; no trial-component rounding enters this
particular certificate.

## Actual independent execution

Executed after the coordinator explicitly confirmed protocol publication
and authorized evaluation, from /workspace/sharp-work:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/padua-mz-sharp-constants-20261106/code/P4_check_grouped.py --trial topics/padua-mz-sharp-constants-20261106/evidence/P4-trial-J512.json --producer topics/padua-mz-sharp-constants-20261106/evidence/P4-rayleigh.json --output /tmp/P4-independent-grouped.json
```

Exit 0; 3.255791057 wall seconds and 3.25258175 CPU seconds. Python
3.12.14; platform and full source/input hashes are in the receipt. The
check independently obtained denominator >0 and this outward enclosure:

    1.004436918864667280457775 <= q(u)
                            <= 1.004436918864667280457778.

It passes the fixed rational target and overlaps the producer enclosure.
The threshold conclusion is decided by exact endpoint comparison, not by
overlap alone. The independent receipt is preserved byte-for-byte as
`evidence/check-P4-independent.json`, SHA-256
`28bb283a2cc3ca65153fd3afbb4a4b0473a7f3f6e96075a52d91a27d8c471a8e`;
copied from the executed `/tmp/P4-independent-grouped.json` and checked
to retain this exact identity.
No new trial, threshold, J, scalar algorithm, upper solve or expensive
numerical campaign was introduced by this review.

The implementation and proof obligations for this lower certificate are
satisfied at the recorded scope. Publication of the checked sources,
trial and receipts and the later focused Claude audit remain the
coordinator's responsibility; no readiness or merge decision is made.
