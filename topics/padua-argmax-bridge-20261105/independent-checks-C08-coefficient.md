# Independent supplementary review — C08 full-phase coefficient bound

Reviewer: distinct Codex `/root/c01_near_review`, parent-assigned Astra high;
serving identity and effective effort are not independently exposed.
Date: 2026-11-06. Rules were read at
`4b728b04216a5490910780bc609a82b853058426`; the AGENTS/WORKFLOW/CODEX
diff to review input HEAD `cc4e51210f51ff51c773dcdd458e25f934d02598`
is empty. Branch: `codex/padua-argmax-bridge-20261105`.

**Disposition: accepted at the stated auxiliary scope, with no mathematical
finding.** The weighted reciprocal-pair inequality holds on the full closed
interval, the coefficient comparison holds on the full closed phase triangle,
and the asserted monotonicity in L follows. The compact constant bound and
full far-model comparison remain OPEN. Formal Claude audit is separate and
remains pending.

## Frozen source and coverage

Reviewed source: `theory/C08-far-weighted-coefficient.md`, SHA-256
`6d905b6c634043992af9f51b6871fe8bcc1ead3b6bc32ca1daa68d844d4e2f1a`.
The full source, `ideas/C08-far-comparison.md`, and
`attempts/C08-far-comparison.md` were read. The full C06 far-profile
and far-comparison records were read, including their full-domain
coefficient calculation and a=0 boundary formula. The N1-04 C/Phi0
definitions, N1-16 reciprocal-pair identity and scalar proof of k>3/2,
and PD-T269's local cotangent partial fraction were already read in
this review sequence and were used with their original scopes intact.

This is analytic review of the new lemma and its exact coefficient
interface, not a fresh review of every C06 approximation-error claim.
Historical novelty, priority and a full author-search/registry audit are
excluded. No mathematical program, numerical quadrature, fit, sample or
computational certificate was used. Source reads, file hashes and the
unchanged-rules diff were the checking commands. Only this new report was
written; no author source, shared file, old report or Git state was changed.

## Tangent partial fraction and cosine estimate

The identity tan z=cot z-2cot(2z) applied to the locally proved
cotangent partial fraction yields exactly

    (pi/2)tan(pi*y/2)=sum_(l positive odd) 2y/(l²-y²),
       0<=y<1.

Its normalization is correct. The subtracted series are absolutely
convergent on compact subintervals of this domain, and the resulting
series and its derivative near zero have summable majorants. Comparing
the derivative at zero therefore gives sum_(l odd)l^-2=pi²/8.
The value at y=0 is the continuous zero value, not an isolated
cotangent evaluation.

For Q=(1-y²)/c, c=cos(pi*y/2)>0, differentiation of log Q
cancels precisely the l=1 term of that series. The remaining terms
have positive denominators, so

    (log Q)'=sum_(l odd>=3)2y/(l²-y²)
             >=2y(pi²/8-1).

Integrating from zero and using Q(0)=1 yields
Q>=exp[(pi²/8-1)y²]>=1+(pi²/8-1)y². The conversion to
the asserted estimate (5) is valid: cQ=1-y² implies

    Q(1-c)=Q-1+y²>=(pi²/8)y²,
    c*y²/[(1-c)(1-y²)]=y²/[Q(1-c)]<=8/pi².

Every division here is confined to 0<y<1. The endpoint cases are
handled separately below. Multiplication by 1-y² also gives the
weaker bound c*y²/(1-c)<=8/pi² used for the nonsingular tail.

## Positive C-series and the factor 7/2

The reciprocal-pair identity from the exact C series is

    C(1/2+y/2)-C0
       =4y² sum_(l positive odd) 1/[l(l²-y²)].

This follows by substituting x=y/2 and j+1/2=l/2 into the
N1-16 algebraic identity; no near-domain estimate or small-x
denominator bound is inherited. The identity itself is valid for
every |y|<1, and the terms are nonnegative there.

For l>=3, replacing l²-y² by l²-1 increases the summand. Its
tail is exactly 3/4-log2. To verify the telescoping value, for
l=2j+1, j=1,...,N, the partial sum is

    H_N-H_(2N+1)+3/4+1/[4(N+1)],

which tends to 3/4-log2. This confirms the constant and the
spacing-two indexing, including exclusion of the l=1 singular term.

Separating that l=1 term and applying the two cosine bounds above gives

    c[C(1/2+y/2)-C0]/(1-c)
       <=(32/pi²)[1+(3/4-log2)].

The source's elementary constants log2>69/100 and pi²>197/20
make the last expression smaller than
(32*53/50)/(197/20)=3392/985<7/2. All comparisons are in the
correct upper-bound direction. The positive log-series terms justify
the strict lower bound on log2 without a numerical evaluation.

C is symmetric about 1/2 and c is even, so negative y has exactly
the same value. At y=0, the original weighted increment and its
right side are both zero. As y tends to one,

    c*4y²/(1-y²) -> pi.

The l>=3 sum is uniformly bounded by 3/4-log2, and its product
with c tends to zero. The full weighted left side thus has endpoint
value pi, while the right side has value 7/2. The negative endpoint
is the same by symmetry. Since pi<7/2, inequality (1) extends to
the entire closed interval |theta|<=pi with theta=pi*y.
No divergent unweighted endpoint C value has been assigned.

## Weighted products on the full closed phase triangle

Let e=alpha+beta, d=alpha-beta, c_e=cos(e/2), c_d=cos(d/2).
For alpha,beta>=0 and e<=pi, both cosines lie in [0,1] and
a=c_e*c_d lies in [0,1]. In the open triangle,

    aD=c_d{c_e[C(1/2+e/(2pi))-C0]}
        +c_e{c_d[C(1/2+d/(2pi))-C0]}.

Apply the newly proved bound to each braced expression. This gives
(7/2)[c_d(1-c_e)+c_e(1-c_d)]. The elementary inequality
c_e+c_d<=1+c_e*c_d, equivalent to
(1-c_e)(1-c_d)>=0, then gives aD<=(7/2)(1-a).

These factored products also verify every boundary value. When e=pi
and |d|<pi, the first braced expression tends to pi and the second
is finite, so aD has limit pi*c_d. At either phase vertex e=pi,
|d|=pi, both braced expressions tend to pi while both external
cosines tend to zero, so the limit is zero. Thus the extension is
jointly continuous, including approaches to a vertex from inside the
triangle. It does not rely on treating the separate divergent D as a
finite number at a=0.

## Exact b_full algebra and endpoint matching

C06 defines U0=c_e Phi0(1/2+d/(2pi))+c_d Phi0(1/2+e/(2pi)).
For a>0, the two sine factors in Phi0 are c_d and c_e respectively.
Hence the exact identity is

    U0=(a/pi)[2C0+D-4log pi].

Substitute this into C06's b_full formula and use
C0=2gamma+4log2 and k=gamma+log(8/pi). The result is exactly

    b_full-b_c=(2/pi²)[aD+2a loga
       +alpha sin alpha+beta sin beta-4k(1-a)].

This is algebra on the full open triangle. It uses neither the
near-domain bound D<=9r²/pi² nor N1-16's near-only negative
coefficient conclusion. The weighted products just checked and
a loga->0 extend the identity to the boundary.

As an explicit normalization check, on e=pi one has c_d=sin alpha,
aD=pi sin alpha and alpha sin alpha+beta sin beta=pi sin alpha.
The displayed identity therefore becomes
b_full-b_c=4sin alpha/pi-b_c, matching C06's exact boundary formula.
At either vertex b_full=0. In particular the midpoint's positive
coefficient excess is permitted rather than suppressed by an invalid
global assertion b_full<=b_c.

For 0<=t<=pi, tan(t/2)>=t/2 implies
t sin t<=2(1-cos t), with both endpoints supplied by continuity.
Summing gives alpha sin alpha+beta sin beta<=4(1-a).
Also a loga<=0, and the parameter-free scalar k>3/2 from N1-16
applies everywhere. Substituting these bounds and aD<=(7/2)(1-a)
gives precisely

    b_full-b_c<=3(1-a)/pi².

All weights, signs and constants remain valid on the full closed
triangle, not only alpha+beta<=1/2.

## Logarithmic monotonicity and its scope

For a fixed phase and a finite term C_far independent of L, the
derivative of the stated polynomial difference is exactly

    -8(1-a)L/pi²+(b_full-b_c)
       <=(1-a)(3-8L)/pi².

It is nonpositive for L>=3/8 and strictly negative for L>3/8
whenever a<1. The sole a=1 phase in this triangle is the origin;
there b_full=b_c and the derivative is zero. The a=0 cases use
the same finite coefficient extension and have strictly negative
derivative on L>3/8. On the specified far region e>=1/2,
a<=cos(1/4)<1, so strictness follows uniformly in the stated
pointwise sense.

This establishes the claimed reduction in the unbounded degree
parameter for a fixed phase-only constant term. It supplies no upper
bound for that constant, no error bound between a far model and the
actual primitive, and no comparison at the finite L endpoint by itself.
The proposed C_far<=5/2 and complete million-degree far comparison
remain separate OPEN obligations. This review does not infer either
from the monotonicity lemma.

## Completion

No BLOCKING, MAJOR or MINOR finding in the frozen source. No author
repair was made or required before acceptance. The weighted 7/2
inequality, the full-phase coefficient estimate, and the stated
degree monotonicity support the lemma's PROVED status at its written
scope. No model maximum, global argmax onset or new certified degree
is accepted through this auxiliary result. Formal Claude audit remains
pending.
