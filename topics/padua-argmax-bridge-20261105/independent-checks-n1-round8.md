# Independent supplementary review of N1 round 8

Reviewer: distinct Codex `/root/review_n1_round4`, requested Astra high;
serving metadata are not independently exposed. Review input head
`d974329331ee4090e8ca1d5100342e69039edbf0`; author input
`a8fad0526779216d184463d046591fdfea6783f6`. The current rules diff
from the previously read `8dc1521` AGENTS/WORKFLOW/CODEX is empty.
Read the current topic LOG and round-8 preregistration. This supplements,
and does not replace, the required Claude audit.

**Disposition: accepted at the written supporting scopes, with no
mathematical finding.** The branch-artifact envelope is proved; neither
the continuous modulus nor C1 is proved. The exact definition and
continuity of the auxiliary reference are reconstructed below.

## Frozen scope and method

| Source | SHA-256 |
|---|---|
| N1-18, `theory/N1-round8-jumps.md` | `efa3fa15f17fd7f355a139616ebb951665703060095252cd1d988e7cd9ca8976` |
| N1-19, `theory/N1-round8-modulus.md` | `77ac04295f571dfce13b2793bc3164182072954977f0c595ba4f595c8cfb8cf0` |

Both frozen files were read in full and checked with `sha256sum`.
The supporting N1 definitions and proofs are the unchanged sources
read and independently reconstructed in the preceding reviews. This
review makes no new mechanism, historical priority or novelty verdict;
the workflow's no-novelty review exception applies. It does not audit
the author's full gate/search chronology. No numerical diagnostic,
mathematical program, integral evaluation or fit was run. Only this
new report was written; developer sources, old reports, shared files
and Git state were left unchanged.

## Exact strip seam and its uniform bound

On a cutoff line the transferred center is z=delta, so its actual
cell is D=[delta-h/2,delta+h/2]. With u=h*b,

    Z_n+B0 log b=U0/pi+B0[log(pi*n/m)+log b]
                 =U0/pi+B0(L+log u).

Therefore differentiating the singular boundary primitive gives exactly
the normalized singular part of H, not an approximation to it. The
fixed h_R/g_R terms do not change with K_s. The regular A and q_s log z
integrals also transfer exactly, and a change of N_s by one contributes
U_s/m=(1/pi) integral_D U_s. The jump for adding the cell to the
strip and removing it from the outer integral is consequently
-pi^-1 integral_D E_s, with the opposite sign for removing it from
the strip. All L-dependent pieces cancel.

The required small extension of the E_s bound is proved, rather than
inherited from its old z<=delta statement. On z<=1/500 the three
N1-10 coefficients remain below 1/9,1/4,3/2; its offsets remain in
[1/4,3/4], with positive numerator and no coefficient switches.
Thus |E_s|<=z(7/4+|log z|/9) there. The actual transferred cell lies
between 1/1100 and 1/990, so |log z|<8 and
|E_s|<(95/36)/990<3/1000. Its normalized integral has magnitude
less than 3/(1000m).

For fixed n, each strip K_s changes at most once as beta runs over
[0,1/2]. To make the step convention explicit, use the actual
after-minus-before jump, as a function of alpha on the cutoff line.
For a left-strip downward floor step the indicator is beta>beta_seam;
for a right-strip upward floor step it includes beta=beta_seam.
This matches the original floor values exactly. Take zero on the
origin side. Whenever a step is active, alpha<=1/2-beta<=1/2-beta_seam,
so evaluating its amplitude at the seam remains within the phase
triangle. These amplitudes are continuous in alpha. Subtracting the
two signed steps removes the seam discontinuities and costs less than
6/(1000m) in the increment from the origin. No pathwise accumulation
over a growing number of transitions is involved.

## The half-angle boundary step and origin normalization

If m is odd, floor(m/2-t_L) and floor(m/2-t_R) are constant on this
beta interval. If m is even, the right index is still constant, while
the left is m/2 at beta=0 and m/2-1 for beta>0. At the boundary its
extra cell is centered at pi/2. Integrating the reciprocal-square,
harmonic and W_b primitives shows that the value at beta=0 minus
its positive one-sided limit is exactly

    j_half(alpha)=(1/(n*pi)) integral_D J_0(z) dz.

On D, |cot z|<=2|z-pi/2|, p*alpha<=1/4 and
2az cot(z/2)<=4. Hence |J_0(z)|<2|z-pi/2| and
|j_half|<pi/(2n*m²)<2/n³.

For clarity, the origin-normalized boundary correction that is
subtracted is

    S_half(alpha,beta)=-j_half(alpha)*1_{beta>0}

when m is even, and zero when m is odd. This adds j_half to the
positive-beta branch while leaving beta=0 unchanged. The resulting
limits agree for every alpha, and S_half(0,0)=0. Thus its contribution
to the increment is bounded by one amplitude, not twice the amplitude.
This is an explicit appropriate signed step for the existence proof;
it changes no term of M_near itself.

## Special-row errors and actual collision marks

Let e_sp be the total approximate-minus-exact contribution of the at
most four nonendpoint special rows, after normalization by nm. The
previous N1-01 and N1-15 bounds give
|e_sp|<=r_n+192/(450pi*m), even when block membership changes or
the numerator vanishes identically. In the latter case the regular
negative set is empty; exact polynomial collision terms remain.
This is a pointwise error bound for the whole row collection. Its
phase increment is bounded by twice the envelope, regardless of how
many sign/block transitions occur along a phase path.

Using pi<4,H_n<=n in the explicit r_n gives
r_n<1/n^4+1/(2n³)<=1/n³. Consequently
2r_n+384/(450pi*m)<3/(10n) on n>=10^6. Only this approximation
contribution is charged twice.

After replacing those rows by exact rows, a noncentral collision
mark is exactly the actual normalized row minus its removed cell
integral. Filling all such holes and removing their exact row terms
leaves only the two permanent central rows. At most two marks exist
at any phase, and none exists at the origin: both candidate angles
then equal pi and the row is permanent. Duplicate rows are merged;
a simultaneous two-pole collision retains both actual grid values
within its single row.

At any such collision, one coefficient is zero and C+D=p/2, so
max(|C|,|D|)=p/2<=1/4. If both vanish, the same statement holds.
A noncentral row has distance epsilon>=h from pi; since its collision
angle lies within 1/2 of pi, |sin v|>=2/m. Taking the ordinary
N1-02/04 row estimate to the collision therefore gives

    |R_r/(nm)-H(center)/m|<=5/(n²m)+1/(2n).

The passage is legitimate: the polynomial row and the regularized
Phi products are continuous. For separated poles the cancellation
integral is continuous by domination with the bounded smaller-channel
magnitude in disjoint pole neighborhoods. These marks never contain
v=pi, so a coalescing-pole limit is not being used in that step.

Their cells lie in z>5/2, with sin(z/2)>9/10 and distance at least
h/2 from pi. The exact max formulas give Lip(A_s)<=5/(4pi).
For V_s=N_s/[2sin(z/2)], the factors satisfy
Lip(N_s)<=12/pi, |N_s|<=8, reciprocal norm<=5/9 and reciprocal
derivative<1/3, so Lip(V_s)<5. Two centered-cell Lipschitz errors
after normalization total at most [5L/8+10]/m²<1/(100n).

For I_s=d log(pi-z)+Z_s, the combined residue variation gives
15/(2pi*m), and the two cells' integrated log second derivative is
at most 4/h. Its error is at most d/(2pi*m). Their sum is below
31/(12m). These include the I/pi normalization. Together with the
two pointwise row errors, all marks at one phase have total absolute
size below

    1/n+10/(n²m)+1/(100n)+31/(12m)<4/n.

The origin mark sum is zero, so no second 4/n charge is needed for
the phase increment. Again this bounds marks present at a phase,
not the number of collision lines crossed along a path.

## Construction and continuity of Q_n

An explicit version of the helper's decomposition is as follows.
Starting with M_near, subtract e_sp and the sum of noncentral marks.
Then subtract the origin-normalized signed strip steps above and
S_half. Call the resulting function T_n. The first two subtractions
leave exact fixed-index central rows and an outer integral without
collision holes. Exact finite polynomial absolute rows are continuous
in phase. For fixed n, the filled outer integration region stays away
from both z=0 and z=pi; its pole profiles and cancellation integral
are continuous, including numerator-zero thresholds. The endpoint
rows and fixed truncated strip constants are also continuous.

Within each cutoff region the remaining bounds and integrands vary
continuously. The explicit step subtractions match the limits and
actual floor values at every strip seam and at beta=0. Thus T_n is
continuous on the closed phase triangle. This asserts continuity for
each n, not an unproved uniform phase modulus as n grows.

With P_n=B_M L²+b_M L, define

    Q_n=(T_n-P_n)(alpha,beta)-(T_n-P_n)(0,0).

The polynomial coefficients are smooth, so Q_n is continuous and
Q_n(0,0)=0. The exact difference F_n-Q_n consists of the e_sp
increment, the mark sum at the current phase, and the three possible
origin-normalized cutoff steps. The bounds above give

    |F_n-Q_n|<[4+3/10+6/1000]/n+2/n³<9/(2n).

This verifies the definition as well as the estimate. It does not
replace F_n by its artifact envelope or bound Q_n by the coefficient
loss G_n.

## The OPEN modulus companion

The remaining sufficient condition Q_n<=G_n+eta-J_n follows directly
from the helper and J_n=9/(2n). At n=10^6 the exact slack is

    eta-9/(2*10^6)-1/40000=159/448000000>0.

It increases with n. This arithmetic is an available allowance only,
not a bound for Q_n.

On beta=0, u/a=tan(alpha/2). Thus s>u is equivalent to epsilon>alpha,
and s sin epsilon=a(1-cos epsilon). The opposite-sign root condition
s sin epsilon<u gives the exact band
alpha<epsilon<arccos(1-tan(alpha/2)). The upper endpoint is within
(alpha,pi/2) for 0<alpha<=1/2. From the elementary cosine and tangent
limits its ratio to sqrt(alpha) tends to one. This proves the stated
root geometry, not a nonzero fractional coefficient or failure of
C2 regularity after all model terms are combined.

The three conditional budget constants also reconstruct exactly. Set
y=sqrt(r); maximizing c*y³-A*y^4 gives y=3c/(4A) and value
27c^4/(256A³). Since rho<=sqrt(2)r, replacing c by 2^(3/4)k gives
27k^4/(32D_f³). For x=r² and rho>=r, the entropy term is at most
(K1/2)x log(1/x); after subtracting D_e*x its maximum is
(K1/(2e))*exp(-2D_e/K1). Completing the square for the linear term
gives c_n²/(2D_l). These hold with the stated positive allocations;
zero coefficients may be omitted and their allocation reassigned.
No constants satisfying the proposed actual phase-modulus estimate
have been supplied, and the record labels all such estimates OPEN.

## Completion and limits

Both frozen records pass at their exact written scopes. The helper
fits the branch-artifact allowance uniformly, while leaving the
continuous entropy/fractional/cusp modulus unresolved. Spatial BV
bounds and continuity alone do not bound that phase increment. No
full F_n comparison, C1 theorem, onset, new correction, numerical
model evaluation or full B3/B4 conclusion is accepted here.
