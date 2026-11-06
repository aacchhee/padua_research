# PD-T?argmax-bridge-codex-D02-far-limit — Uniform true constant and parameter-explicit error

ID kind: PD-T. Aliases: full-phase renormalized primitive limit; auxiliary
cutoff error contract; geometry-valid far completion. Split from: the sharp
D02 joint-remainder target, which remains OPEN. Split into: the constant
identity is separately PROVED in D02-far-bias-identity.md.

## Statement

With exactly the definitions of D02-far-bias-identity.md, let

    M_infty(phi,L)=B0(phi)L^2+b_full(phi)L+C_infty(phi),
    F_n(phi)=S_n(phi)-B0(phi)log^2 n-b_full(phi)log n.

Then F_n tends to C_infty uniformly on the full closed phase diamond,
through every integer n and both parities. In particular, the bias of the
unchanged C06 model is identified, not just bounded:

    lim_(n->infty) [S_n(phi)-M_far(phi,log n)]
        =beta_(64,1/100)(phi), uniformly in phi.             (1)

The following explicit finite-n contract is valid for any integer R>=2,
0<delta<=pi/4 and integer n>=ceil(2pi R/delta). Put m=n+1, L=log n.
The auxiliary R,delta need not equal the fixed model parameters. Then

    |S_n(phi)-M_infty(phi,L)| <= T_n(phi;R,delta),            (2)
    T_n=e4+E_n+D_n+I_n+Q(P,delta)+|beta_(R,delta)|.           (3)

Every term is defined below. For R>=64 one may replace the last two terms
by 2Q(P,delta)+1/(R-1)^2. Consequently the unchanged-model contract is

    |S_n-M_far-beta_(64,1/100)| <= T_n,
    |S_n-M_far| <= |beta_(64,1/100)|+T_n.                   (4)

The quantities on the right depend only on fixed integrals/series and
explicit scalars; no full odd-board sum occurs. This is an honest
auxiliary-parameter bound, not a claim of a practical C(1+L)/n rate.
For example R=2,delta=pi/4 makes (2) applicable to every n>=16, without
asserting that its numerical bound is useful there.

## Complete explicit error definitions

Use the absolute phases and p,q,P,a,U0 from the bias identity. Define
u=p/2, d=(q-p)_+ and

    sbar=1/2+4a/delta, f=log(pi/delta),
    G=2u[1+log((sbar+u)/u)] if u>0, and G=0 if u=0,
    Astar=(1+8a/delta)/pi, VA=16a/(pi*delta),
    Vstar=2|U0|/delta+6, VV=4|U0|/delta+23,
    Jstar=max(5, 2sbar*f+max(2u,sbar+u)*log2),
    VJ=(16a/delta+4sbar)*f+3G+2(sbar+u)*log2+20,
    Wstar=Vstar+Jstar/pi, VW=VV+VJ/pi.

The interior replacement error in (3) is

    I_n=[(VA/2+9Astar)L+VW/2+5Wstar+4Vstar
                     +(d/pi)(4+5log m)]/m.                 (5)

The shared ordinary-row errors are

    E_n=2P(1+L)/n+2am/[n(R-1)],
    D_n=10/n^2+20a(1+L)/(pi*n^2).                          (6)

For e4, these are exactly the N1-06/07/08 component bounds with H_n
replaced by its upper bound 1+L. Set X=delta*m/pi and

    HR=log(R+1/2)+1/[8(R-1/2)^2],
    CX=[5+(1/2)log(X+1/2)]/[2(X-1/2)]
             +[6+(1/2)log(X+1/2)]/[8(X-1/2)^2],
    e_mesh=(2R+3)L/(2m)+2CX+(8+HR)/n+1/(2n^2),
    e_row=(10R+39+6L)/n+200(R+2)(R+1)^2/n^2,
    e_rows=(4+L)/n+(2R-1)*e_row,
    e_collision=(2/m)[7+(2/pi)(3+2log(4m/R))]
                             +5/(n^2*m)+1/(nm),
    e4=e_mesh+e_rows+e_collision.                          (7)

The phase-dependent Q and exact signed beta are defined in the separate
bias theorem. All these formulas have finite continuous phase limits,
including u=0, a=0, every axis and phase vertex. No mesh swap is used.

## Assumptions, status and dependencies

Exact real arithmetic; the original corrected finite polynomial and
odd-board normalization are unchanged. **PROVED**, analytic developer
result. Supplementary review and final Claude review remain separate.

Dependencies read: N1-02 cancellation quadrature, N1-04 pole profile,
N1-05 endpoint residual; N1-06/07/08 full-domain endpoint block with its
actual degree condition; C06 full-profile collision-continuity bound and
exact coefficient integration; C06 compact-error sections 1–4 for the
full-domain P and central J bounds; D02-far-bias-identity.md. This proof
rechecks the degree condition and supplies its own delta-dependent
interior constants. It does not extend the old fixed n>=10^6 theorem by
changing its displayed quantifier.

## Proof

### 1. Interior suprema and variations

Let K=[delta/2,2pi-delta/2] and z=min(v,2pi-v). Use C06's decomposition

    V(v)=U0/z+P_s(z),
    ell(v)=log(2|v-pi|/pi) on |v-pi|<=pi/2, zero otherwise,
    W(v)=V(v)+[I(v)-d ell(v)]/pi.

C06 proves sup|P_s|<6 and Var(P_L)+Var(P_R)<23 on the entire folded
interval, independently of delta. This yields the displayed Vstar,VV.
The exact max formulas are

    pi A_L=max(p,q+T), pi A_R=max(p,|q-T|),
    T=2a cot(z/2), 0<=T<=8a/delta on K.

Each max is 1-Lipschitz in the monotone variable T, so sup A<=Astar and
Var_K A<=VA. Their two values agree at the center; no seam jump is lost.

On either endpoint half delta/2<=z<=pi/2, the cancellation parameters
are u=p/2, s_L=q/2+a cot(z/2), s_R=|q/2-a cot(z/2)|. They lie in
[0,sbar], with at most three monotone pieces in total and combined
variation at most 8a/delta. C06's exact generic identity reads

    J(u,s,z)=2(s-u)_+ log(sin z)+R(u,s,z),
    |R|<=max(2u,s+u)log2,
    |R_s|<=log((u+s)/|u-s|).

The integral of the last envelope over [0,sbar] is at most G, including
its continuous zero value at u=0. The parameter-motion cost is therefore
at most 3G. C06 also proves R_z>=0 for s>u, zero for s<=u, and R_z is
nondecreasing in s. Integrating its value at sbar bounds each
separation-motion cost by (sbar+u)log2, so both cost at most twice this.

For k_s=2(s_s-u)_+, total variation is at most 16a/delta and each sup
is at most 2sbar. Since sin(delta/2)>=delta/pi, the magnitude and
variation of log sin z on either endpoint half are at most f. The
product variation bound gives (16a/delta+4sbar)f. Its sup contribution
is at most 2sbar*f. This proves the endpoint parts of Jstar,VJ.

On the two central halves C06 proves sup|I-d ell|<5 and combined
variation <20. The expressions match the endpoint ones at pi/2 and
3pi/2 because ell=0 there; their central finite limits agree. Hence
Jstar,VJ bound the full regularized I on K. Combining them with V proves
sup|W|<=Wstar and Var_K W<=VW. Thus every constant in (5) bounds the
stated complete interval, including all coefficient/root switches.

### 2. Actual partition and interior comparison

Use precisely the first/last R rows, the two central rows and all
polynomial-collision rows as the special set. The condition
n>=2pi R/delta implies n>=8R and puts the first/last R rows strictly
inside the endpoint strips z<=delta. No low-degree geometry is inferred
from the R64,delta=.01 partition. At most four other special rows lie in
the retained interior D=(delta,2pi-delta).

On ordinary rows the actual normalized row is approximated by
H=A L+W+d ell/pi. N1-02/04/05 bound all ordinary errors, over both
endpoint and interior subsets together, by (6). Use exact polynomial
values on every special row. C06's finite-polynomial continuity argument
bounds each interior special row by A L+V plus its single-pole profile
error. Ordinary and special shares of the latter are charged once by D_n.

The centered cells of ordinary interior samples lie in K. Their midpoint
quadrature error for A L+W, after division by pi, is at most
(VA*L+VW)/(2m). Their union differs from D by at most four omitted cells
and boundary pieces of total length at most one cell. The regular
integral over that difference is bounded by 5(Astar*L+Wstar)/m.
The four actual special rows cost at most 4(Astar*L+Vstar)/m. These are
the regular terms in (5).

The ordinary central distances are at least h=pi/m, so their cells have
distance at least h/2. The variation of ell on both truncated halves is
at most 2log m. Its normalized quadrature error is at most
(d/pi)*log m/m. Missing cells have total length at most 4h, whose
|ell| integral is at most 4h(1+log m). This follows by placing that
measure closest to the center and integrating the logarithm; the exact
integral is 4h[1+log(pi/(4h))]. The boundary pieces lie outside the
support of ell: delta<=pi/4 and h<=delta/(2R) ensure this. The resulting
logarithmic charge is precisely the last term in (5). Thus (5) is the
complete interior error, with (6) still shared globally.

### 3. Endpoint assembly and completion

N1-08 applies at exactly the stated degree floor and bounds the endpoint
block by its quadratic polynomial with error e4 in (7). N1-05 charges
the remaining ordinary strip residual by Q(P,delta). C06's exact
coefficient identity joins the endpoint coefficient to the interior A
integral, giving precisely b_full, without a delta-dependent leftover L.
Therefore

    |S_n-[B0 L^2+b_full L+C_(R,delta)]|
                      <=e4+E_n+D_n+I_n+Q(P,delta).        (8)

This holds for the actual geometry just described, not the invalid
small-n R64/.01 geometry of the D01 diagnostic. The separate exact bias
identity C_infty-C_(R,delta)=beta_(R,delta) proves (2)–(4).

### 4. Uniform identification of the true constant

Fix R>=64 and delta>0. The terms e4,D_n,I_n and 2P(1+L)/n tend to zero
uniformly in phase; this follows directly from (5)–(7), whose phase
factors are bounded on the compact diamond. Equations (3) and the bias
bound imply

    limsup_(n->infty) sup_phi |F_n(phi)-C_infty(phi)|
       <=2/(R-1)+1/(R-1)^2+2Q(2,delta).

First choose R arbitrarily large and delta arbitrarily small, then let
n tend to infinity through the domain of (8). The right side can be
made arbitrarily small. This proves uniform convergence and (1).
No interchange of a nonuniform endpoint limit and a phase supremum has
been made: every bound used before the final limit is phase-uniform.
QED.

## Phase-relative comparison and limits of this result

At phase zero the inherited exact identity is S_n(0,0)=Lambda_c(n).
Consequently

    S_n(phi)-Lambda_c(n)
       <= M_infty(phi,L)-M_infty(0,L)
                           +T_n(phi;R,delta)+T_n(0;R,delta). (9)

This uses the actual primitive at zero and avoids a separate lower
estimate for its constant. For the unchanged M_far the analogous model
difference additionally carries the signed bias difference
beta_(64,.01)(phi)-beta_(64,.01)(0). A phase-uniform absolute corner
constant should not replace that difference without its own bound.

The present error is generally much too large at small n: it retains
2a/(R-1), e_rows of order R^2(1+L)/n+R^4/n^2, and the strip Q charge.
Their cancellation has not been proved. The theorem establishes the
true complete constant and a valid parameter contract, not a useful new
argmax onset or the desired O((1+L)/n) estimate. The sharp target remains
OPEN; uniform convergence alone does not imply that rate.

No numerical execution is a premise. Independent review must check the
explicit variation constants, collision accounting and degree floor.
History: 2026-11-06, rules/input 084a64f6465956f9c75b5538f83752c30318f151;
parent-requested Astra ultra, prospective LOG justification, serving
metadata unexposed. Gate: ideas/D02-far-joint.md.
