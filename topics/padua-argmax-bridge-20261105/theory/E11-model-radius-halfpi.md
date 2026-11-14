# E11 — The true central decomposition on its closed half-pi baseline domain

Provisional developer theorem, no global ID. Aliases: natural endpoint-
positivity radius; closed half-pi true model; dominated boundary completion.
Split from the SAME E11 model-domain continuation, prospectively released
by root AFTER the main pair/5/4 first freeze. The main pair theorem and
the successful weaker5/4-domain proof remain unchanged in their own files.

## Exact statement and status

Let x=|alpha|,y=|beta|,rho=x+y<=pi/2. All phases are RADIANS. Use
EXACTLY D02/D10's TRUE completed constant C_infty, and set

    d=x-y,e=x+y,ce=cos(e/2),cd=cos(d/2),a=ce*cd,
    p=sin x,q=sin y,v=p/2,delta=q/2,
    u=1-a,z=(1-ce)(1-cd),
    c=1/3+(4/pi²)(log²pi-log²2).

Let E_infty,H and J be the accepted global endpoint, scalar finite-part
and generic cancellation functions. On this NEW domain define Ec by the
SAME formula used in E10/E11, with no added correction:

    s0(t)=a tan(t/2),sL(t)=s0(t)+delta,sR(t)=|s0(t)-delta|,
    Ec=pi^-2 integral_0^(pi/2)
          [J(v,sL(t),t)+J(v,sR(t),t)-4s0(t)log(sin t)]dt.

Then on the ENTIRE CLOSED signedrho<=pi/2,

    C_infty=E_infty+ce H(d)+cd H(e)-c*a+Ec.             (1)

With kappa=4I4/pi² as in accepted E10, and with the EXACT negative
baseline from E11-central-pair,

    b=2atan(q/(2a)),
    Bbeta=(4/pi²)integral_0^b
             [q/2-a tan(t/2)][-log(sin t)]dt>=0,

one has

    Ec<=kappa*p^(3/2)/sqrt(a)-Bbeta
       <=sqrt2*kappa*p^(3/2)-Bbeta.                    (2)

The zero-q integral is0 directly. The new CLOSED boundary b=pi/2 is
allowed with its actual convergent integrand. At x0, Ec=-Bbeta EXACTLY;
at y0 the unchanged actual alpha-axis leading coefficient is kappa>0.

For the accepted E07 Hmax and E06 regular constants
j=H0+d0-(c-1/3)>23/250,v0>0, the same NEW domain satisfies

    Delta(C_infty-Ec)<=-j*u-(H0+v0)z,
    Delta C_infty<=kappa*p^(3/2)/sqrt(a)-Bbeta-j*u-(H0+v0)z. (3)

No finite-row/error/floor/corner/physical guard is enlarged. In particular
a finite relative theorem proved throughrho1 is NOT used atpi/2 here.
No degree endpoint, new global onset, minimality or quadratic modulus.

Status: **PROVED developer PAPER theorem**, distinct mathematical audit
and root adoption pending. This new closed-domain proof is substantive
and separate;5/4 remains a successful weaker subset, not a failed attempt.

## 1. Exact phase geometry and the strict interior

Onrho<=pi/2 the exact identities give

    2a=2cos(rho/2)cos(d/2),
    P=p+q=2sin(rho/2)cos(d/2),
    2a-P=2cos(d/2)[cos(rho/2)-sin(rho/2)]>=0.           (4)

Since |d|<=rho<=pi/2, ce,cd>=cos(pi/4)=1/sqrt2>0 and

    a>=1/2,0<=p,q<=1,0<=v/a<=1.                        (5)

The inequality(4) is STRICT if rho<pi/2. For such an interior phase,
the same complete endpoint-half numerator, for0<t<=pi/2, is at least
2a-P>0. With T=2a cot(t/2),

    T>=2a>P,
    (T-q)sin t=2a(1+cos t)-q sin t>=2a-q>p.          (6)

Thus BOTH actual generic channels have s>v and their no-root criterion
s sin t>v. The accepted FULL-parameter identity gives the EXACT
endpoint-half baseline4a cot(t/2)log(sin t). The central half keeps the
unchanged two-channel Ec expression. The same global scalar-pole and
finite-part calculation as D10 therefore gives(1) at EVERYrho<pi/2.

This proof uses the strict guard only in the open interior. The next
section proves its boundary extension; replacing “>” with “>=” without
that work would not supply the claimed closed domain.

## 2. Prove continuity of the COMPLETE central functional

On the compact actual phase setrho<=pi/2 and the central integration
range0<t<=pi/2,

    0<=v<=1/2,0<=sL,sR<=3/2,0<=s0<=1.

These are precisely within the globally proved C06 generic parameter
box. Its SAME-SIGN entropy and OPPOSITE-SIGN root formulas join by
their complete finite limits at s=v, zero coefficients and root/no-root
thresholds. For each FIXED t>0, J(v,s,t) is continuous in these parameters;
no separate divergent cotangent-channel integrals are evaluated.

C06/N1's FULL generic representation is

    J(v,s,t)=2(s-v)_+ log(sin t)+R(v,s,t),
    |R(v,s,t)|<=max(2v,s+v)log2.

For the stated box this supplies the PHASE-UNIFORM bound

    |J(v,s,t)|<=3|log(sin t)|+2log2.

Consequently the COMPLETE numerator of the Ec integrand obeys

    |J(v,sL,t)+J(v,sR,t)-4s0 log(sin t)|
                             <=10|log(sin t)|+4log2.   (7)

The right side is integrable on(0,pi/2): the sine chord bounds its only
possible singularity by a constant plus|log t| at0, while it is bounded
atpi/2. Dominated convergence now proves that Ec is continuous on the
WHOLE CLOSED phase set, including itsrho=pi/2 edge and both axes.
All moving coefficient/positive-root thresholds use the same domination.
No limit exchange requiring a phase-dependent root separation occurs.

The exact true C_infty is continuous on the FULL closed phase diamond
by accepted D02-far-bias-identity: its K_delta functions are continuous
under the globally dominated central logarithm and converge uniformly
toK0; weighted E_infty is continuous. This entire proof/idea/attempt
history was read before the present candidate. E_infty and ce,cd,a are
therefore continuous here. H is continuous as well: its accepted paired
formula has Lipschitz-f numerator differences bounded uniformly by a
constant times t, giving an integrable dominator after dividing by
2sin(t/2); pointwise continuity and dominated convergence apply.

Approach anyrho=pi/2 phase by interior scaled phases(x,y)*(1-epsilon),
epsilon decreasing to0. Every term in(1) is continuous by the preceding
arguments. Passing to the limit in the EXACT interior equality proves
(1) on the ENTIRE closed boundary. This is an equality of COMPLETE
weighted finite-part objects, not a value assigned to an unweighted pole.

For an explicit degeneracy check, at the boundary T=2a=P may occur
only at integration endpointt=pi/2; then the right generic s equalsv
and log sin t=0, so the same-sign/opposite-sign formulas have their
common value0. When p0 or q0 the complete zero-coefficient limits above
are used directly. The uniform bound(7) covers all these cases together;
no edge, vertex, weighted zero or root threshold is omitted.

## 3. Paired-root and exact-baseline bounds on the NEW closed domain

The E11-central-pair proof establishes its paired-root inequality for
ALL a>0,v>=0,delta>=0, using actual real-line truncated weights. It
does not require rho<=1. Its final E10 full-root application needs
0<=v/a<=1, which is newly proved in(5), including EQUALITY at a possible
boundary phase. E10's root kernel already includes its k1 collapsed
interval and its k0 improper endpoint. No strict tau<1 assumption is
being extended by assertion.

The actual beta-baseline support is also newly checked:

    b=2atan(q/(2a))<=rho<=pi/2,

using (cos x+cos y)tan(rho/2)=p+q and2a>0. On0<t<b, its factor
q/2-a tan(t/2) is nonnegative. At t0 it is bounded and -log sin t is
integrable; at a possible b=pi/2 both its weight and -log sin t vanish.
Thus Bbeta is finite and has the claimed nonnegative sign everywhere.
Atq0 it is directly0; no log0 value or0 times an infinite integral is
invented. Its exact relation to Ec has the SAME factor4/pi² and sign.

Apply the GENERIC paired-root bound and E10's GENERIC v<=a integral
bound, retaining that exact baseline, to obtain the first upper in(2).
The second follows froma>=1/2 in a NONNEGATIVE fractional term.
Atv0,E=Z0 gives Ec=-Bbeta exactly even at y=pi/2; this also checks
the new endpoint support. Atbeta0,Bbeta0 and the accepted C01/D10
small-alpha limit remains the same positive fractional coefficient.

No actual Ec monotonicity in beta follows: the convolution comparison
is only for its positive MAJORANT at fixed a,v. The true actual a moves,
and the generic E is not always equal to Z. This domain theorem does
not assert either false implication.

## 4. Recheck the regular part using only GLOBAL predecessors

The accepted D10/C08 weighted endpoint inequality is globally valid
onrho<=pi with ce,cd>=0. In E06 notation it reads

    E_infty<=a/3+B-d0*u-v0*z, B=C0²/pi².

Accepted E07 Hmax holds for every real scalar phase by periodicity;
in particular it applies at|d|,e<=pi/2 with nonnegative ce,cd. Hence

    ce H(d)+cd H(e)-2H0<=H0(ce+cd-2)=-H0(u+z).

Subtract the origin value in(1), use E_infty(0)=1/3+B and
g0=c-1/3. The regular increment is at most

    (g0-d0-H0)u-(H0+v0)z=-j*u-(H0+v0)z.

Adding(2) proves(3). These are global endpoint/H predecessors applied
INSIDE their literal domains, not a local H derivative proof extrapolated
past1. The quantitative j,H0 constants keep E06's named PD-T271
limiting-origin/outward-enclosure premise. The new root/decomposition
proofs themselves need no PD-T271 enclosure or new numerical input.

## History, scope and execution boundary

Root supplied the natural pi/2-domain candidate prospectively in LOG
AFTER the first successful pair/5/4 freeze. The completed gate-only
prefix remains8110B1fbad9d3...; the main pair proof10942Bdea44db8...
and weaker5/4 proof9450Bee98de67... are untouched. Newly relevant
FULL D02 continuity idea/theory/attempt and C08 global records were
completed before this extension was developed. The exact chronology
and all alternatives are in the appended E11 idea/attempt.

The full stronger beta-monotonicity claim, full D13 and finite mixed
error targets remain OPEN. No finite relative-error, physical floor,
corner square, actualargmax/onset or source guard is enlarged by this
MODEL domain. The earlier5/4 theorem is a valid weaker subset with its
own first proof retained. The optional higher-moment kernel candidate
is DEFERRED and unused. No historical priority or new model claim.

Requested Codex gpt-6.1-sol xhigh; serving metadata unexposed,2026-11-07.
Only assigned new E11 prose records changed. No script/import, scalar,
endpoint, phase/root/board/native/quadrature/degree/threshold/compile/
control/scientific/source/pack/shared/Git job or mutation occurred. No
numerical boundary or integral value was evaluated. Distinct mathematical
audit/root adoption is required before any downstream assembly use.


## Root adoption —2026-11-07

Root adopts this exact10157B frozen proof (SHA256695800c16c70d6d7a1224758bc654e9833c3441d553754e31c87f972a794a6f8) after distinct [E11 same-batch ACCEPT](../independent-checks-E11-central-pair.md), report22172B3407c50d16d23001e5a2532af80dd82d920263366d9091af1877b3d6c9ab29d2. Original proof prefix remains unchanged. The exact paired-root upper/negative baseline and model-domain scopes are accepted; no actual beta-monotonicity, finite-error domain or new onset is inferred. The weaker5/4 domain remains a preserved successful subset of the new closedpi/2 theorem. Optional kernel-moment sharpening remains deferred. No numerical/source job occurred; final Claude audit is separate.
