# PD-T?argmax-bridge-codex-D07-central — Two retained central rows on the near half diamond

ID kind: PD-T. Aliases: actual central weighted-pole upper; collision-safe
fixed central allowance. Split from: D07 six retained rows. Split into:
none.

## Statement and status

For integer n>=32, m=n+1, alpha,beta>=0, alpha+beta<=1/2, use the
actual corrected polynomial row norms R_r from D05-fixed-special-rows.md.
Put a=(cos alpha+cos beta)/2, p=sin alpha, q=sin beta, P=p+q and L=log n.
Then

    0<=[R_(m-1)+R_m]/(nm)<=[10a+P(1+L)]/n.          (1)

This includes beta=0, alpha=0, v=pi, either parity and every exact
polynomial collision. For signed phases define this central-row
quantity by separate absolute phases, as in the fixed-row model, and
extend (1) accordingly; raw row labels at negative beta are not assumed
invariant.

Status: **PROVED**, analytic developer result, distinct review pending.
The bound concerns actual finite polynomial rows, not the central
cancellation integral or a presumed smooth motion of its roots.
No numerical premise or old model change occurs.

## Dependency: actual weighted row bound

C06-far-full-profile.md section 1 proves, for every interior row
0<v_r<2pi including v_r=pi and all polynomial collisions,

    R_r/n<=A(v_r)L+V(v_r)+5(|C(v_r)|+|D(v_r)|)/n^2,
    C(v)=(p-q-2a cot(v/2))/4,
    D(v)=(p+q+2a cot(v/2))/4,
    A(v)=2(|C(v)|+|D(v)|)/pi,
    V(v)=[c_e Phi_0(eta_-(v))+c_d Phi_0(eta_+(v))]
                                             /[2sin(v/2)],
    c_e=cos((alpha+beta)/2), c_d=cos((alpha-beta)/2).

The offsets and continuous periodic Phi_0 are exactly N1-04/05's,
with |Phi_0|<=4 and Phi_0(integer)=1. The source proof extends the
whole weighted-pole inequality from dense noncollision phases using
finite-polynomial continuity. It never assigns zero to an unweighted
vanishing coefficient times a divergent pole norm. That precise
collision-safe inequality is inherited here.

## Proof with the actual two row angles

The two angles are

    v_(m-1)=pi-(pi-beta)/m, v_m=pi+beta/m.

Thus |v_r-pi|<=pi/m for each. On this phase domain
c_e,c_d>=cos(1/4)>=31/32. Also, since m>=33 and pi^2<10,

    sin(v_r/2)>=1-pi^2/(8m^2)>99/100,
    |cot(v_r/2)|=tan(|v_r-pi|/2)<=pi/m.             (2)

The tangent bound follows by integrating sec^2 u<=2 on [0,pi/4].
Since c_e*c_d=a,

    c_e+c_d=a(1/c_e+1/c_d)<=(64/31)a,
    V(v_r)<=[2*(64/31)/(99/100)]a
                       =(12800/3069)a<(9/2)a.      (3)

This remains a valid upper if a particular Phi_0 is negative.
The exact absolute-value identity gives

    |C|+|D|=(1/2)max(p,|q+2a cot(v/2)|)
                                   <=P/2+a*pi/m.

Consequently A(v_r)<=P/pi+2a/m. Apply the inherited weighted row
upper to both rows and divide their sum by m. This proves the more
explicit intermediate bound

    [R_(m-1)+R_m]/(nm)
      <=9a/m+2P L/(pi*m)+4aL/m^2
                              +5P/(m*n^2)+10pi*a/(m^2*n^2).     (4)

To simplify, L<=n/4 for n>=32: n/4-log n is increasing there and
log32<4<8. The latter follows, for example, from e>8/3. Hence

    4L/m^2+10pi/(m^2*n^2)<=1/n,

because 4Ln+10pi/n<=n^2+40/n<=(n+1)^2. Also
2L/(pi*m)+5/(m*n^2)<=(L+1)/n. Substituting in (4) gives (1).
The lower bound is immediate from the actual absolute row norms.

## Scope and checks

No assumption on the sign of the central numerator, on p being
positive, or on smooth root motion is used. The only special-value
transfer is the already proved whole weighted-pole continuity above.
The exceptional (n,0) mode remains in the inherited polynomial R_r.

This proves a small absolute allowance for the two central rows. It
does not prove a phase increment relative to a times the origin, the
central-log mesh comparison, a full model rate or a practical global
argmax onset. Those require separate terms and proofs. No numerical,
native, board, quadrature, fitting or code job was executed.

Candidate/gate: ../ideas/D07-short-endpoints.md. 2026-11-06,
parent checkpoint 2e4ac49fa0687a7736bc1df82c12e6483b1c7a94; requested Astra ultra, runtime metadata
unexposed. Independent review of the frozen proof is required.
