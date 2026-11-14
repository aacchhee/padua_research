# Independent supplementary review of N1 round 7

Reviewer: distinct Codex `/root/review_n1_round4`, requested Astra high;
serving metadata are not independently exposed. Rules/input head
`8dc1521cf68f7780bd10e02495f6f71a639c03c6`. Read current AGENTS, CODEX
and handoff 04; WORKFLOW is unchanged from the previously read rules.
This supplements, and does not replace, the required Claude audit.

**Disposition: no mathematical finding.** N1-16 is accepted at its
coefficient/uniform-bounded-remainder scope. N1-17 correctly preserves
the full C1 comparison as OPEN; its residual identity and sufficient
prospective budget condition are correct. No onset or maximum bound
is established by this review.

## Frozen scope and method

| Source | SHA-256 |
|---|---|
| `theory/N1-round7-coefficients.md` | `e7a7d4464e787df527aa6f155d223ae504a9be8f79221089ee43303c5b8d21e8` |
| `theory/N1-round7-comparison.md` | `3ff66dfe8d67fe25a6ceda01c9bde7da4c225aec0b38430ae3d749ecae32fbb5` |

Read both frozen records and `ideas/N1-round7.md`. Refreshed the exact
N1-05/06/15 definitions and C1, and used the unchanged N1-07/09–14
dependencies independently reviewed in the preceding reports. Read the
PD-T269/270/271 corner chain, PD-T159's positive corner identity and
PD-T220's exact primitive cusp. This review reconstructs the analytic
claims only. It does not audit the author's novelty verdict, chronology,
full search coverage or future candidate dispositions. No new novelty
conclusion is made, so the workflow's no-novelty review exception applies;
a new full IDEAS read is not claimed.

The optional normalization code and receipt were inspected and their
hashes checked, but the mpmath pilot was not rerun:

- code: `4e78df28472e1c9464dda5e0739b333b927d19d5addcde3688c309cb150d3e5e`;
- receipt: `64a192218ea4749319c3fe35080437b3cae4833d242eb3aa3d76c21f765f4bd7`;
- its `n1_rows.py` dependency: `c8461f7f3c61e54a20844c624a1d7f094d7a8375fc798caa2fb924e328b85e46`.

No M_near evaluation, fit, numerical integral or phase sample was run.
One small independent exact-Fraction command checked three printed
rational inequalities, as recorded below. All other executable work
was read-only source/rules inspection and `sha256sum`. Only this new
review file was written; old reviews and all developer/shared files
remain untouched.

## Uniform extraction from the unchanged model

For either retained strip endpoint, b_s differs from delta*m/pi by at
most 1/2. Since delta is fixed and n>=10^6, its logarithm is
L+log(delta/pi)+log(m/n)+O(1/n), with a uniform constant. The singular
coefficient is Z_n=D0-B0*log(m/n), which is bounded independently of
L. Thus the finite h_R/g_R truncations affect only bounded terms:
there is no L times a constant-truncation error to omit. Expanding
both strip singular terms gives B0 L²+(2B0*kappa+2D0)L+O(1).
All errors containing log(m/n) or the retained cutoff discrepancy
are bounded by a constant times (L+1)/n.

The regular coefficient is uniformly bounded by 3/5. Moving its
retained lower cell limits to zero costs O(RL/n), and moving the
upper limits to delta costs O(L/n); R=128 is fixed. The q_s log z
integrals are uniformly bounded by absolute integrability near zero.
U_s is bounded by the regular-profile derivative estimate and
N_s/m<=1. This verifies the complete strip expansion (6), uniformly
through t_L=0,t_R=1 and all scalar cutoff changes.

For the outer cells the two lower-boundary discrepancies total at most
h, the two omitted central end lengths total 2h because t_L+t_R=1,
and collision holes have total length at most 2h. Hence the symmetric
difference with the two [delta,pi] intervals has measure at most 5h.
Throughout it, z>delta/2 and |A_s|<=8/(pi*delta)+3/5. The outer
L coefficient therefore differs from its full-interval integral by
O(L/n). The B term is uniformly absolutely integrable: U0/z and P_s
are bounded away from the endpoint, the endpoint I formula is bounded
on [delta/2,pi/2], and the central I is d log(pi-z)+Z_s with
d<=1/2 and |Z_s|<3. Removing holes can only decrease the absolute
integral bound. No continuity of the hole enumeration is needed.

The remaining components really are uniformly bounded. N1-07 bounds
the finitely many exact endpoint rows by its bounded limiting profiles
plus a uniformly bounded error, while the model still uses the exact
N1-09 rows. For each of the at most four other special rows,
sin(v/2)>=cos(1/4)>15/16. The regularized pole norm satisfies
F_n(t)<=2L/pi+4+5/n², so the triangle inequality and ce+cd<=2 give

    R_r/n <=(16/15)(2L/pi+4+5/n²)<2(L+5).

At collisions this inequality passes from nearby noncollision phases
by continuity of the finite polynomial row. It also covers the central
coincident-pole row; no separate zero-times-infinity value is assigned.
After division by m, these rows are O((L+1)/n). Their Rhat and H8
replacement errors are bounded by the already proved r_n and
192/(450pi*m). Finally M_jump has a bounded reciprocal-square term,+a harmonic term O((L+1)/n), and bounded-length regular integrals
with |W_b|<2. All constants here are independent of phase and degree.

Combining the strip and outer L coefficients cancels kappa:

    2B0*kappa+2D0 + (1/pi)integral_0^delta(f_L+f_R)
      +(1/pi)integral_delta^pi(A_L+A_R)
      =2D0+(1/pi)integral_0^pi(f_L+f_R).

Thus the asserted single uniform finite K exists over the entire stated
degree/phase domain. This proves boundedness, without supplying a useful
numerical K or a phase-increment modulus.

## Exact linear coefficient and its quadratic deficit

Let x=max(alpha,beta), y=min(alpha,beta). The two switch values are
T(pi-x-y)=p+q and T(pi-x+y)=|p-q|. If p>=q the final two maxima are
p,p; if q>=p they are q+T,q-T. In either case their sum is exactly
the source's three pieces 2T, T+p+q, 2sin x. This covers x=y and
y=0 by empty intervals; there is no uncharged linear phase cusp.

Integrating T=2a cot(z/2) gives 4a log sin(z/2). Subtracting 8a/z
before taking the lower limit yields 8a log(2/pi). The remaining
trigonometric endpoints give 4a log a, since
cos((x+y)/2)cos((x-y)/2)=a. The constant pieces total
2y(p+q)+2(x-y)sin x=2(alpha p+beta q). Inserting this integral in
the coefficient formula yields exactly the displayed b_M, with all
R and delta dependence canceled.

Pairing the defining C series about 1/2 gives

    C(1/2+x)-C0
      =2x² sum_(j>=0) 1/[(j+1/2)((j+1/2)²-x²)].

Here |x|<1/12. The denominator is at least 35/36 of its zero-shift
value, and sum(j+1/2)^-3=7*zeta(3)<35/4. Thus the bound is
18x². Since x_-²+x_+²=r2/(2pi²), it gives
0<=D<=9r2/pi²<(15/16)r2. The identity C0=2gamma+4log2 follows
from the same half-shift harmonic sums. The two sine weights in U0
both equal the product ce*cd=a, proving
U0=(a/pi)(2C0+D-4log pi). Consequently

    (pi²/2)(b_M-b_c)
      =aD+2a log a+alpha p+beta q-4k(1-a).

The source's elementary k>3/2 proof is valid. The PD-T270 harmonic
remainder implies gamma>=H10-log10-1/20. The positive exponential
polynomial through degree 10 at 2303/1000 exceeds 10, hence
log10<2303/1000. The resulting rational slack above 23/40 is exactly
61/63000. For w=17/39, integrating the geometric series gives
log(28/11)>2(w+w³/3), whose rational slack above 37/40 is
14311/7118280. Together with pi<22/7 these establish k>3/2.

The independent exact command used Python `fractions.Fraction` and
`math.factorial` to calculate
`sum((2303/1000)^j/j!, j=0..10)-10`,
`H10-2303/1000-1/20-23/40`, and
`2*(17/39+(17/39)^3/3)-37/40` as rational numbers. It returned
positive, `61/63000`, and `14311/7118280`, respectively. No decimal
approximation or model computation was used in that check.

Set u=1-a. On the stated phase interval, the cosine Taylor inequality
gives u>=47r2/192. Also log a<=-u and alpha p+beta q<=r2. Therefore
the right side above is at most

    [(15/16)a+1]r2-(2a+6)u
      <=[-15/32+(43/96)a]r2<=-r2/48.

The factor 2/pi² gives exactly -r2/(24pi²). The leading gap is
4u/pi²>=47r2/(48pi²). At zero phase these are equalities, not strict
negative constants. The paired series is smooth near every used offset;
interchanging x_- and x_+ under either phase reflection proves evenness.
Together with a>0 this supplies a smooth even extension and uniform
O(r2) for b_M-b_c near the origin.

## Corner normalization and the OPEN residual comparison

PD-T271 uses N=n+1/2 and the linear coefficient
8[gamma+log(8/pi)]/pi². Since 0<=log(N/n)<=1/(2n), transferring its
quadratic and linear terms to L=log n costs O((L+1)/n). Its stated
remainder is uniformly bounded on n>=10^6 and tends to zero. The
corner coefficients therefore match exactly, for both parities.
Subtracting the uniformly bounded expansions proves the stated
uniform O(t²) remainder on the integer sequence t=1/log n and its
uniform t=0 extension. No continuous-degree interpolation is asserted.

The exact S_n(0,0)=Lambda_c identity is analytic, not inferred from
the pilot. At zero phase the noncollision half-kernel is
(1+cos v)/(cos u-cos v). Folding its periodic absolute sum gives
PD-T159's positive corner sum with factor 4/(nm) and the actual
endpoint polynomial contribution 1/(n+1). The inspected pilot uses
that same independently weighted sum and includes the one polynomial
endpoint collision. Its 60-digit agreement at n=17,24,32 is correctly
labeled MEASURED calibration, with no M_near evaluation or use of the
n>=10^6 model theorem at those degrees. The receipt's execution claim
was inspected, not independently rerun.

At the origin B_M=B_c and b_M=b_c, so N1-17's residual identity is
exact. The slack is
eta=1/4096-3/14000=107/3584000. Hence F_n<=G_n+eta is sufficient
for C1, while the two coefficient gaps give the stated A(L)r2 lower
bound on G_n. For any prospective increment constants with
D=A(L)-K0>0, rho<=sqrt(2r2) and completing the square give

    -D*r2+c(n)*rho+J(n) <= J(n)+c(n)^2/(2D).

The same upper bound remains valid if c(n)<0 by first replacing it
with |c(n)|. A(L) increases on the degree range, so K0<A(L0) makes
all denominators positive. This verifies the sufficient budget test;
none of its proposed constants or modulus estimates has been proved.

PD-T220's exact cusp coefficient and harmonic upper bound agree with
N1-17. Subtracting the smooth even logarithmic coefficients does not
remove that fixed-degree linear cusp in the exact primitive. The
source correctly avoids transferring the cusp formula directly to
the cutoff-dependent M_near. Its alternative primitive target and the
warning that two uniform model errors exceed eta are also correct.

## Completion and limitations

The two frozen records pass this analytic review at their stated
statuses. In particular, phases of order 1/L make the leading gap
only O(1), the same scale as the uncontrolled finite remainder.
Favorable coefficients and uniform boundedness therefore do not prove
C1, a finite-part modulus, a small numerical bound, full B3 PASS or
an effective onset. The future model/cutoff-jump test remains unexecuted.
Far phases, other center classes and the global finite degree range
are unchanged. No correction of the model or old review was made.
