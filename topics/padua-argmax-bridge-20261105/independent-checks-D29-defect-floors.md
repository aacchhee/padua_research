# D29 defect floors — independent mathematical review

Date: 2026-11-06. Rules/input head:
`4f8c169171e55b7d5f00f57a8b3ce8340a498960`.
Distinct Codex supplementary reviewer `/root/d29_floor_review`, requested
gpt-6-astra high; serving model/effort metadata are unexposed. The author
is a different worker. Only this review file is written; no mutable Git,
author-file, shared-record or scientific-source operation is performed.

**Verdict: ACCEPTED at the three frozen hashes below, with no unresolved
mathematical finding.** Both applicable projected inequalities and their
noncorner consequences hold on the stated physical odd-center domains.
This is mathematical premise acceptance, not source approval, a finite
certificate, a new global argmax degree, or the separate Claude audit.

## Frozen claims

| File in `theory/` | SHA256 | Accepted conclusion |
|---|---|---|
| D29-floor512.md | `4c86921221f75cb8dbcc978e52a6f1dfad73b1c59938ee7496523e6c381e1ec1` | Each applicable projection is strictly greater than 1/20 for every integer n>=512 |
| D29-floor41.md | `20f0d107a47d02a06c5da42eb768db7d8b10fde7213e61e4a87926fa383bea64` | Each applicable projection is strictly greater than 1/512 for every integer n>=41 |
| D29-radius41.md | `978ab5256dbdda8f6d0a041aeb5780d15ef3abdcde6cc036a7d19f4b8eebf56a` | Each applicable projection is at least max(1/512,min(1/32,B_n(r))) for every integer n>=41 and rho<=r<=1/2 |

Here rho=|alpha|+|beta|, physical angles lie in [0,pi], J+K is odd,
Q_v is applicable when 0<K<n+1, and Q_h when 0<J<n. Both signs of
both phases are allowed subject to physical admissibility. Every
noncorner odd center has at least one applicable projection. Actual
corner centers are excluded. The assumption rho<=r implies r>=0.

## Reading and gate coverage

Read AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md, the complete
topic LOG through its then-current D27 release, all three frozen proofs,
and the complete D29 idea/attempt records. Read the complete current
1154-line state/IDEAS.md, including all obstruction/disposition tables;
its SHA256 is
`d7ec3aa6cf36f72e8057bcb90d8ac6eae8bf285a5b17f12526b26472ff4bddef`.
Targeted repository searches covered dense band, straddling, capped
reciprocal, selected pairs, defect floors and quarter certificates in
the registry, bridge ideas/theory and all-degree predecessor theory;
the literature index was screened for relevant entries. No external
fulltext was opened or external theorem/priority claim adopted.

Full closest reads include C01-allclass's idea and proof, C02-defect's
idea/attempt/proof and independent review, N5-two-phase-defect,
N5-large-budget and N5-round5-budget, PD-T222, PD-T224 and PD-T366,
the IDEA-326/327/328 final candidate entries, and the complete H1
candidate file containing IDEA-454/458. PD-T364 was read in full.

Classification is a quantitative/domain variant of the selected-pair
method. The distinction is the newly proved n41 domain and the n512
quantitative onset, not a new cancellation principle. N5's failed
phase-blind quarter certificate remains failed in its stated scope;
its limiting upper bound neither proves nor contradicts these smaller
lower floors. The actual-corner zero-defect obstruction is respected.
The primitive cusp and failed coarse fixed-sign mechanisms are not
used: this review asserts no primitive upper comparison. Deferred
stronger floors and alternative bands are retained in the D29 idea
record. This review does not certify historical priority or reconstruct
the author's prospective reading chronology from tool records.

Key dependency identities verified by sha256sum:

- C02-defect-dense-band.md:
  `d28bbc8f7ae3823ff220b452630b0c30c939b9851fa0c151d2ac5962a301dec7`.
- PD-T364, padua-argmax-effective-2-20261105/theory/phase-structure.md:
  `378548a0635206c8e61111c8ddb24b51f4b7ef1bf3cb16640da16dcf94a9e718`.

## Normalization, actual numerator and full domains

PD-T364's finite corrected cardinal identity and endpoint reflection
multiplicities give lambda=S-Delta and Delta>=Q_v,Q_h>=0. I reconstructed
the projection folding: an interior physical row accounts for two
periodic orientations, and replacing both G values by their common-sign
halves multiplies the pair defect by another factor two. The resulting
coefficient is 1/N. The two periodic branches subsequently selected are
distinct terms in that sum; they do not change its coefficient to 2/N.
Endpoint physical rows retain their half weights but are never selected.

On the odd board, subtraction of cos(nu) before halving gives exactly

    A(u,v)=a_actual*(1+cos v)
               -(sin alpha/2)*sin u+(sin beta/2)*sin v.

The exceptional first-coordinate mode is therefore retained. The bound
a_actual>=1-rho^2/4>=15/16 and total sine perturbation <=rho/2<=1/4
allows signed phases. In the horizontal pair, v is fixed, and it is
this same fixed cosine that supplies the baseline. No kernel transpose
or unsupported transfer from an edge-only parity class occurs.

Near the upper endpoint, reflecting the physical row to M-l gives
cos(chi+(pi-b))=cos(gamma+b) and
cos(chi-(pi-b))=cos(gamma-b), with chi=pi-gamma. Thus the top and
bottom target sets really agree, up to order. Actual sine signs can
differ and are already covered by the absolute perturbation bound.
Selected points have strictly opposite nonzero denominators; all
unselected collision terms remain in the full polynomial projection
and have nonnegative defect. Collisions are not assigned a quotient.

## New degree-41 nearest and small-angle proofs

For s=1,...,4, writing q for the offset in the displayed s-term list,
the exact displacement is

    M(w-b)=(M/L-1)*l*pi+(M/L)*q*pi+(M/L)*phase.

Adjacency, l<=M/2, |q|<=s-1<=3 and L>=41 give the residual
M/(2L)+3/L<=24/41 after extracting (s-1)*pi. The total weighted
phase contribution, including the physical phase, is <=21/41.
Consequently the strict slack is at least (17*pi-21)/41>0, so both
periodic branches straddle the physical cosine targets regularly.

The endpoint recheck is genuinely at the new domain:

    t<=(4*pi+1/2)/M<183/574<1/3,
    l+q>=ceil(M/4)-3>=8,
    l+q<=M/2+3<L.

The last inequality holds in the worst orientation M=L+1 already at
L=41. Together with b in [pi/4,pi/2], these bounds keep all effective
angles in (0,pi), all s offsets distinct, and the positive and reflected
periodic branches distinct. The earlier index bound 13 is not imported.

At a lower center, row plus periodic index has parity q=s-1=1-s
modulo 2. At an upper center it has parity M+q=1-M+s modulo 2.
These are precisely the parity complementary to the interior center
index, hence the prescribed parity in both folded projections. Periodic
index negation preserves parity. The argument covers both n parities
and all admissible other-coordinate indices.

Both vertical targets, and the intervening horizontal fixed cosine,
are greater than -1/3. Hence A>3/8. The full cosine span is <=2t,
giving pair defect >3/(8t). Counting 2s points on each of at least
M/4-1 rows yields

    Q > [3*s/(4*(s*pi+1/2))]*(M/L)*(1/4-1/M)
      >=37/[224*(pi+1/2)]>37/816>1/32.

The middle comparison uses the increasing function s/(s*pi+1/2),
M/L>=41/42 and 1/4-1/M>=37/164. This independently verifies the
new 1/32 cap used in the radius corollary.

For s>=5, gamma>= (5*pi-1/2)/M>4*pi/L: the worst orientation
reduces to (L-4)*pi-L/2>0, implied by (5/2)*L-12>0 at L>=41.
When gamma<pi/6, rows b in [pi/6,pi/3] give two disjoint open arcs
of length 2gamma. Their combined count is at least
2Lgamma/pi-2>3Lgamma/(2pi). All relevant baselines are >=1,
so the pair defect is >=11/[8*sqrt(3)*gamma]. The count M/6-1 gives

    Q >=[33/(16*pi*sqrt(3))]*(1/6-1/M)
       >(3/8)*(1/6-1/41)=35/656>1/20.

Thus neither easy-case estimate silently uses the old n64 constants.

## Degree-41 full open arcs in the middle case

For gamma>=pi/6 and b in [pi/12,pi/6], the first open arc
(gamma-b,gamma+b) lies in (0,2pi/3) and the reflected arc in the
opposite half-circle. At gamma=b=pi/6, the possible zero endpoint
is excluded. The arcs remain disjoint; periodic representatives handle
either phase sign. The cosine is strictly between cos(gamma+b) and
cos(gamma-b) on each arc, so selected collisions are impossible,
including the tangency at cosine 1.

Vertical target cosines and the horizontal fixed cosine are >=-1/2.
Hence A>=7/32; the span 2*sin(gamma)*sin(b)<=1 gives d>=7/16.
An open arc of length 2b>=pi/6 on a translated L-point parity circle
contains at least L/12-1 points, even when both endpoints are mesh
points. There are at least M/12-1 interior physical rows. Multiplying
the positive real count bounds and the correct coefficient 1/(ML)
gives exactly

    Q >=(7/8)*(1/12-1/M)*(1/12-1/L)
      >=(7/8)*(29/492)^2
       =5887/1936512>1/512.

The integer comparison is 512*5887=3014144>1936512. Integer rounding
can only improve these lower counts. Together with the two easy cases,
this exhausts all applicable projections at n>=41 and proves the
strict uniform floor, including closed phase and band boundaries.

## Degree-512 floor and the old C02 domains

C02(16) and (18) already prove >1/20 for the two easy cases when
n>=64; they therefore apply at n>=512. The stronger numerator in
C02(27) requires its n4096 small-t condition and is not used here.

For middle angles the cap-2 band [pi/100,pi/4] uses exactly the same
finite layer-cake and physical-mesh inequalities as C02(19)-(23).
Its constants in (28) have no degree premise. Positivity, gamma>=pi/6
and M,L>=n are the relevant assumptions; n4096 entered only the old
final 1/16 comparison and its separate easy cases. Thus H_n(29) is a
valid middle-case lower bound on the entire claimed n>=512 domain.

I checked the four rational terms at 512 by hand:

    H_512=1617/24200-385/(628*512)
                       -640/(157*512)-550/(3*512^2).

The displayed cross-products in D29-floor512(5) are correct. They
give H_512>33/500-1/800-1/125-7/10000=1121/20000>1/20.
Each loss is a positive constant times 1/n or 1/n^2, so H_n is
increasing for all positive n. No degree scan or endpoint evaluation
by a numerical library is needed.

## Radius-dependent middle bound at n>=41

Let a=1-r^2/4 and A(b)=a-r/2-a*sin b. On [pi/20,pi/4], A and
A/sin b are positive and decreasing for every 0<=r<=1/2. In the
cosine band z0-D<x<z0+D, the pair defect is at least
2A/(D+|x-z0|), with D=sin(gamma)*sin b. This applies horizontally
because the fixed v lies in that same band.

The cap c=5/4 gives integral T*A, T=3/2+4log(5/4), and maximum
c*A/D. Every positive superlevel set gives one interval per
half-circle; translated-grid counting and layer cake lose at most
2*max f, including open endpoints and tangencies. The angular density
bound 1/sqrt(1-x^2)>=1 supplies the row estimate LT*A/pi-2c*A/D.

Using the lower physical-mesh bound for the positive A sum and the
upper bound for the subtracted A/sin b sum gives, before coarsening,

    Q >=T*I/pi^2-T*A0/(M*pi)
          -2*c*R/(L*pi*sin gamma)
          -2*c*A0/(ML*sin gamma*sin a0).

Both mesh inequalities hold for arbitrary mesh spacing; they introduce
no hidden n64 premise. All three losses are nonnegative. Substituting
sin gamma>=1/2 and M,L>=n proves D29-radius41(6) at the new domain.

I reconstructed the elementary C02 constants: the sine/cosine bounds
follow from the displayed Taylor inequalities and squaring; the upper
Taylor polynomial for log(5/4) gives T<115/48<12/5, and the positive
atanh series gives T>239/100. The positive exponential sum supplies
log[tan(pi/8)/tan(pi/40)]<5/3. For the cap-2 band, its squared
exponential lower bound gives the required logarithm <10/3; the log2
series supplies 11/4<T<14/5. These arguments are independent of n.

The resulting I>U, A0<V and R<W have positive right sides on the
whole radius interval. Their minima are the stated endpoint values
2693/16000, 35/64 and 1337/2400. Correctly directed substitution in
the positive main term and three negative losses gives exactly the
four rational coefficients of B_n(r). No positivity of B_n itself is
needed. Combining the middle estimate with >1/32 in the two easy
cases gives min(1/32,B_n(r)); independently combining with the
strict uniform floor gives the stated maximum. No old cap 1/20 is
extended below its n64 scope.

## Findings, execution and adoption boundary

No BLOCKING, MAJOR, MINOR or mathematical NOTE finding remains within
this scope. All arithmetic reported above is written rational/integer
reconstruction. Commands were read/search/hash operations and the patch
creating this review: git rev-parse, rg/rg --files, cat/sed, wc and
sha256sum. No scientific script, Fraction execution, native process,
scalar job, phase/degree scan, source test or independent numerical
rerun was performed. Existing C02/N5 execution records were read, not
rerun or relabeled as this review's evidence.

A consumer still needs exact integer degree guards, physical noncorner
guards and a validated bound rho<=r<=1/2 on every point to which it
applies the floor. For a whole box, the displayed maximum-absolute
endpoint sum is sufficient; a mere nonempty intersection is not.
Intersected-subdomain use requires its own correct geometry. The
D32 generic-certifier adapter, executable arithmetic, complete cover,
finite global degree and full argmax claim are outside this review.
The required later Claude audit remains separate.
