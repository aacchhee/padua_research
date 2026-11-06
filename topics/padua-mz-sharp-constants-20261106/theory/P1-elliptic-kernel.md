# PD-T?mz-sharp-codex-P1-01 — elliptic kernel of the accepted corner operator

ID kind: PD-T.
Aliases: Schloemilch identification; arcsine convolution; Poisson-regularized
corner kernel.
Split from: supporting identification for PD-T381 and S3-03's operator B.
Split into: spectral positivity consequences in P1-positive-spectrum.md;
decimal enclosure remains a separate computational target.

## Statement

Let D={(a,b): a>0,b>0,a+b<1}, dmu=ab da db and H=L2(D,dmu).
Boundary changes to D are null and do not change H. Let B be exactly the
compact selfadjoint norm limit proved in S3-03:

    B_K=-16 sum_((1+j)(1+k)<=K, j+k even)
            e_j e_k (-1)^j |psi_jk><psi_jk|,
    psi_jk(a,b)=J0(pi j a)J0(pi k b),
    e_0=1/2, e_j=1 (j>=1),       ||B-B_K||<=120/K.

For 0<a,a'<1, define, almost everywhere,

    S_all(a,a')=2 K(k0)/(pi^2(a+a')),
       k0^2=4aa'/(a+a')^2,
    S_alt(a,a')=2 K(k1)/(pi^2 sqrt(aa')) * 1[a+a'>1],
       k1^2=((a+a')^2-1)/(4aa')  when a+a'>1,
    K(k)=integral_0^(pi/2) (1-k^2 sin^2 t)^(-1/2) dt.

S_all has an integrable logarithmic singularity on a=a'. Values on the
diagonal or a+a'=1 may be assigned arbitrarily as null sets. Then B is
the bounded integral operator with respect to dmu and kernel

    B(a,b;a',b')=-8 [S_alt(a,a')S_all(b,b')
                         +S_all(a,a')S_alt(b,b')].        (1)

In particular the kernel is nonpositive almost everywhere. The proof
identifies the literal product-truncated norm limit, not an alternative
ordering or a pointwise interpretation of the undamped double series.

## Definitions and assumptions

J0 is the entire power series used in S3-03. All kernels and operators are
real, with complexification allowed. Write dnu(a)=a da on (0,1).
The complete elliptic integral is defined above rather than imported from
an external formula. Products in (1) mean ordinary functions off null
singular sets, and the resulting bounded integral operator on H.

## Status by part

Overall status: **PROVED**, analytic development, with the new proof to be
independently checked. No certified decimal value is asserted.

| Mathematical part | Status | Evidence |
|---|---|---|
| Local scalar summation and elliptic evaluation | PROVED | arcsine convolution and positive Poisson regularization below |
| Boundedness of the closed integral operator | PROVED | explicit integral row bounds and tensor Schur estimate |
| Equality with the accepted product-truncated B | PROVED | L1 kernel passage and absolute smooth-test coefficient series |

Candidate disposition: retained explicit completion of the supplied route;
no historical novelty or priority claim.

## Depends on

S3-03 only for existence and boundedness of its precise norm limit B. Its
accepted proof is unchanged. The elementary Bessel angular representation
is reproved below; no source-reported Schloemilch/Gegenbauer identity is a
premise. Usual measure integration, Tonelli/dominated convergence, density
of compactly supported smooth functions in weighted L2, and the elementary
Schur quadratic-form argument are used explicitly.

## Proof

### 1. Arcsine probability densities and the Bessel product formula

For a>0 put

    w_a(t)=1[|t|<a]/(pi sqrt(a^2-t^2)).

This is a probability density on the real line. With Fourier convention
Fv(x)=integral_R exp(ixt)v(t)dt, the substitution t=a cos theta gives

    Fw_a(x)=(1/pi) integral_0^pi exp(i ax cos theta)dtheta
            =J0(ax).                                   (2)

The last equality follows by expanding the exponential: odd cosine
moments vanish and its 2r-th normalized moment is
(2r)!/[4^r(r!)^2]. The series converges absolutely uniformly on the finite
integration interval. In particular |J0(x)|<=1 for real x.

Let q_(a,a')=w_a*w_a'. It is a nonnegative probability density, even and
supported on [-(a+a'),a+a'], and

    Fq_(a,a')(x)=J0(ax)J0(a'x).

One may realize w_a as the first coordinate of a uniformly oriented circle
of radius a. Add two independently oriented circle vectors. Their relative
angle, folded to [0,pi], is uniform there; after a possible angle reversal,
the sum radius is

    r(phi)=sqrt(a^2+a'^2-2aa' cos phi).

For each fixed relative angle the common orientation remains uniform.
Thus the density of its first coordinate is, by nonnegative integration,

    q_(a,a')(t)=(1/pi^2) integral_(0<phi<pi, r(phi)>|t|)
                                   dphi/sqrt(r(phi)^2-t^2).             (3)

This proves the usual Bessel product identity as well, without a source
theorem: J0(ax)J0(a'x)=(1/pi) integral_0^pi J0(x r(phi))dphi.

### 2. Positive Abel sums and exact halfweight normalization

For 0<rho<1 let

    S_all,rho(a,a')=sum_(n>=0) e_n rho^n J0(pi n a)J0(pi n a'),
    S_alt,rho(a,a')=sum_(n>=0) e_n rho^n (-1)^n
                                             J0(pi n a)J0(pi n a').

Periodize q on the circle of length 2:

    Q_(a,a')(s)=sum_(l in Z) q_(a,a')(s+2l).

Its Fourier coefficient at integer n is (1/2)Fq(pi n). The period-2
Poisson kernel is

    P_rho(s)=sum_(n in Z) rho^|n| exp(i pi n s)
            =(1-rho^2)/(1-2rho cos(pi s)+rho^2),
    integral_-1^1 P_rho(s)ds=2.

Write Poisson convolution as (P_rho*Q)(s)=(1/2) integral_-1^1
P_rho(s-t)Q(t)dt. Its Fourier series, absolutely convergent for fixed
rho, gives

    S_all,rho=(P_rho*Q)(0),
    S_alt,rho=(P_rho*Q)(1).                             (4)

Indeed the series is (1/2)sum_(n in Z)rho^|n| Fq(pi n)exp(i pi n s),
which has constant term 1/2 and positive-frequency coefficients exactly
e_n=1. This is the reason for e_0=1/2. Both regularized kernels in (4)
are nonnegative even though that fact is not apparent term by term.

Poisson convolution tends to Q(s) at every point where this integrable
periodic density is continuous. For completeness, P_rho is nonnegative
and has normalized mass 1; outside any fixed neighborhood of 0 its
supremum tends to 0 by the displayed rational formula. Split the integral
into that neighborhood, where continuity controls Q(t)-Q(s), and its
complement, controlled by this supremum and the L1 norm of Q. This proves
the asserted approximate-identity limit.

For 0<a,a'<1 with a!=a', the density (3) is continuous at t=0. Since
a+a'<2, its periodization there is just q(0). At t=1 it is continuous
unless a+a'=1: if the sum is less than 1 it vanishes locally; otherwise
|a-a'|<1<a+a' and the square-root endpoint in (3) is removed by the
substitution in the next paragraph. Its periodization at 1 is q(1)+q(-1).
Consequently almost everywhere in (0,1)^2,

    S_all,rho -> q_(a,a')(0)=:S_all(a,a'),
    S_alt,rho -> 2q_(a,a')(1)=:S_alt(a,a').               (5)

### 3. Evaluate the scalar densities

Put s=a+a', p=aa'. From (3),

    q(0)=(1/pi^2) integral_0^pi
                        [s^2-4p cos^2(phi/2)]^(-1/2)dphi
         =2 K(2sqrt(p)/s)/(pi^2 s).

If s<1 then q(1)=0. If s>1, put k^2=(s^2-1)/(4p); because |a-a'|<1,
one has 0<k<1. In (3), first put u=(pi-phi)/2. The retained region is
0<u<arcsin k, and r^2-1=4p(k^2-sin^2 u). Then sin u=k sin v gives

    integral_(r>1) dphi/sqrt(r^2-1)=K(k)/sqrt(p),
    2q(1)=2K(k)/(pi^2 sqrt(p)).

These are exactly the formulas in the statement. The same fixed-interval
substitution makes continuity at t=1 explicit when 1 lies strictly
between |a-a'| and a+a'. No value on the exceptional null curves is used.

### 4. L1 convergence, including the singular sets

The a.e. limits (5) alone would not justify a kernel exchange. To supply
the missing uniform integrability, integrate the arcsine densities first:

    A(t):=integral_0^1 w_a(t) a da
          =sqrt(1-t^2)_+/pi.                            (6)

Here sqrt(1-t^2)_+ means sqrt(max(1-t^2,0)). Let Z=A*A. It is continuous,
even, supported on [-2,2], with Z(2)=Z(-2)=0. Nonnegative integration
shows that the nu-times-nu integral of the periodized q is the
periodization of Z. Apply (4), then the approximate-identity limit to
this continuous function. It gives

    integral S_all,rho dnu dnu -> Z(0)
                                      =integral S_all dnu dnu,
    integral S_alt,rho dnu dnu -> 2Z(1)
                                      =integral S_alt dnu dnu.         (7)

The right equalities follow directly from (3), (5), (6) and Tonelli;
they do not assume any series exchange. All four integrals are finite,
since A is bounded and integrable. Positivity, a.e. convergence and
(7) imply L1 convergence: use
integral|u_rho-u|=integral u_rho+integral u-2integral min(u_rho,u),
where the last integral converges by domination by u. Thus

    S_all,rho -> S_all,  S_alt,rho -> S_alt
                 in L1((0,1)^2,dnu times dnu).           (8)

For two L1 factors in independent coordinate pairs, the elementary
telescoping product estimate gives L1 convergence of their products;
the regularized factors have bounded L1 norms by (7). Therefore both
products in (1) converge in L1 on the four-variable square. Multiplication
by 1_D(a,b)1_D(a',b') and any bounded test function is legitimate. This
handles the diagonal, support switch and triangle boundary simultaneously.

### 5. Boundedness before identification

The following are integral row bounds against dnu(a')=a' da', not
pointwise upper bounds for the singular kernels. Equations (3) and (6)
give for almost every a,

    integral_0^1 S_all(a,a')a'da'=(w_a*A)(0)<=1/pi,
    integral_0^1 S_alt(a,a')a'da'=2(w_a*A)(1)<=2/pi.       (9)

Both kernels are symmetric and nonnegative. For such a kernel T with
row bound M, the inequality 2|f(a)f(a')|<=|f(a)|^2+|f(a')|^2, followed
by nonnegative integration, bounds its quadratic form in absolute value
by M||f||^2. Truncation and density yield the bounded selfadjoint operator
with ||T||<=M. Apply this to (9), tensor the two operators on the full
square, and extend functions on D by zero. Compression is a contraction,
so (1) defines a bounded selfadjoint operator C on H and

    ||C|| <= 8[(2/pi)(1/pi)+(1/pi)(2/pi)]=32/pi^2.        (10)

This bound is deliberately coarse; it is a boundedness proof, not a useful
decimal enclosure of the sharp constants.

### 6. Dense-domain equality with the product-truncated limit

Take f,g in C_c^infinity(D), extending them by zero to the open square.
Set c_jk(f)=integral_D f psi_jk dmu. The radial Laplacian
L_a=a^(-1)partial_a(a partial_a) is symmetric under a da on these
compact supports, and the defining J0 series gives

    L_a J0(pi j a)=-(pi j)^2 J0(pi j a).

Repeated integration by parts in both coordinates, with no boundary
terms, gives for every r,s>=0 a finite constant depending on f,r,s with

    |c_jk(f)|<=C_(f,r,s)(1+j)^(-2r)(1+k)^(-2s).         (11)

For j=0 or k=0, apply integration by parts only in the nonzero
coordinates and increase the constant. Together with |J0|<=1 this makes
the full double sum of |c_jk(f)c_jk(g)| finite. Hence its product-truncated
sum, its full sum, and its rho^(j+k)-damped limit agree by absolute
convergence. In particular

    <g,Bf>=-16 sum_(j+k even) e_j e_k (-1)^j
                                            c_jk(f)c_jk(g).           (12)

The parity identity
1[j+k even](-1)^j = [(-1)^j+(-1)^k]/2
rewrites the damped version of (12) as the integral form with kernel

    -8[S_alt,rho(a,a')S_all,rho(b,b')
                         +S_all,rho(a,a')S_alt,rho(b,b')].

For fixed rho, all series/exchanges are absolutely convergent. Passing
rho to 1 in this integral is justified by (8) and boundedness of f,g;
passing it in (12) is justified by (11). Thus <g,Bf>=<g,Cf> on the dense
smooth domain. Both B and C are bounded, so B=C on H. This proves (1)
for precisely the accepted product-truncated B. No undamped pointwise
double-series rearrangement has been used. QED.

## Checks, sources and limitations

This worker performed no numerical calculation. The audit support is
acknowledged as the supplied development lead, with no floating value
used as a proof premise. The complete prospective gate is
../novelty-gate-P1.md and candidate ../ideas/P1-kernel.md. The new proof
needs distinct supplementary reconstruction and focused Claude audit;
those are not represented as completed. The accepted S3 proofs are not
edited. No certified decimal, elementary scalar value, finite-m onset or
numerical quadrature error follows from this kernel identification.

## History

2026-11-06, bounded round 1. Codex P1 developer, requested gpt-6.1-sol
xhigh; serving metadata unexposed. Rules/input
0205690b9c4e959a28e949083e9a1808735abf4b. Derivation began only after the
coordinator reported response R published at
17ca9f441cece178354e70504a6c739df501a224 and after the saved candidate.
