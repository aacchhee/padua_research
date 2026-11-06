# PD-T?argmax-bridge-codex-D08-corner — Three certified point losses imply an origin-box corner barrier

ID kind: PD-T. Aliases: three-point corner barrier; origin-weighted Peano
loss; squared-phase strict corner box. Split from: application of D08
point-to-box interpolation. Split into: none. Successful point premises
and any complete global certificate remain separate obligations.

## Exact sufficient statement

Fix n>=2, m=n+1, kappa=n/m, and the actual corner chart

    Lambda(alpha,beta)=lambda_n(-cos(alpha/n),-cos(beta/m)),
    Lambda_c=Lambda(0,0).

Let M be any PROVED global bound for lambda_n on the physical square.
Let U,V>0, and suppose three certified losses obey

    Lambda(sqrt(2U),0)<=Lambda_c-delta_x,
    Lambda(0,sqrt(2V))<=Lambda_c-delta_y,
    Lambda(sqrt(2U),sqrt(2V))<=Lambda_c-delta_xy.       (1)

If a real c>0 satisfies

    delta_x>=cU, delta_y>=cV, delta_xy>=c(U+V),
    c>(M/6)*max(U,kappa^4*V),                        (2)

then, for every 0<=u<=U,0<=v<=V,

    Lambda(sqrt(2u),sqrt(2v))
       <=Lambda_c-epsilon*(u+v),
    epsilon=c-(M/6)*max(U,kappa^4*V)>0.              (3)

Thus every nonorigin point of this closed box has strict descent from
the actual corner. The result transfers to the other parity-correct
nonnode corner by the accepted node-preserving reflection.

Safe numerical premises for (1) are a certified corner lower L<=Lambda_c
and certified point uppers U_x,U_y,U_xy, with

    delta_x=L-U_x, delta_y=L-U_y, delta_xy=L-U_xy.     (4)

Any lower enclosures for these differences are also valid. The true
origin value in the proof remains the symbolic Lambda_c, not a rounded
corner upper. No energy, inward slope or cardinal sign-stability premise
is required. Assumptions (1)-(2) must actually be verified before use;
this theorem does not assert that any degree passes them.

Status: **PROVED**, analytic sufficient implication; distinct review
pending. No point evaluation, corner patch instance or global onset is
claimed by this result.

## Proof

Write H(u,v)=Lambda(sqrt(2u),sqrt(2v)). The point-dependent theorem
D08-point-box.md gives on this origin box

    H(u,v)<=I H(u,v)+(M/6)[u(U-u)+kappa^4*v(V-v)],    (5)

where I uses nonnegative bilinear weights. Put x=u/U, y=v/V. Its
origin value is exactly H(0,0)=Lambda_c, and (1) gives

    I H<=Lambda_c-[x(1-y)*delta_x
                       +(1-x)y*delta_y+xy*delta_xy].

By the first three inequalities in (2), the bracket is at least

    c[x(1-y)U+(1-x)yV+xy(U+V)]
       =c(xU+yV)=c(u+v).                             (6)

This is an exact cancellation of the mixed bilinear terms, not a lower
bound obtained from a sampled interior deficit. On the other hand,

    u(U-u)+kappa^4*v(V-v)
        <=Uu+kappa^4*Vv
        <=max(U,kappa^4*V)*(u+v).                    (7)

Insert (6)-(7) into (5). This is precisely (3), with the strict positive
epsilon in (2). Its vanishing factor u+v preserves equality at the
origin and strictness at every other point, including all nonorigin
closed edges. Formula (4) implies (1), since L<=Lambda_c and each
point upper encloses the corresponding actual value. QED.

## The parent's illustrative half-diamond geometry

Take positive phase endpoints

    A=pi/4, B=3pi/16,
    U=A^2/2=pi^2/32, V=B^2/2=9pi^2/512.

Both A and B exceed 1/2 already from pi>3, so the phase rectangle
0<=alpha<=A,0<=beta<=B contains the full inward diamond
alpha,beta>=0, alpha+beta<=1/2. Also kappa^4 V<=V<U, so the last
condition in (2) simplifies exactly to

    c>M*pi^2/192.                                    (8)

If the three actual point losses and (8) are independently certified,
(3) proves strict descent on that full punctured half diamond, with no
use of the older tiny energy radius. This is only an explicit sufficient
criterion; no successful losses are supplied here.

The D07 rational inward-turn point API would represent these three
nonorigin vertices by

    (1/(4n),0), (0,3/(16m)), (1/(4n),3/(16m)).

This exact conversion does not authorize a call or enlarge its literal
degree/input guards. The choice of asymmetric endpoints was supplied
by the parent; no claim about root conditioning or measured cost is made.

## Scope and provenance

The result depends only on the proved global M, the actual certified
point losses and the common-kernel interpolation theorem. The coarse
independent choice M=sqrt(2n(n+1)) is valid. A smaller independently
proved GLOBAL M can improve the criterion; an unknown argmax, point
maximum or unverified model upper cannot replace it.

This is a pointwise local descent predicate, distinct from N3's
energy-based maximum-exclusion implication. It does not supply the
three successful point enclosures, a strict complement cover, a complete
producer/checker, finite degree extension, effective global onset or
runtime bound. No numerical, code, native, board or quadrature job ran.

2026-11-06. Parent supplied this application prospectively within the
same D08 gate, before this proof was written. Rules/input
`d4956aea3bda9d5ff9917a5b410778fc7adf4fb7`; ordinary Sol xhigh,
serving metadata unexposed. Root owns Git/shared records. The separate
developer proof awaits distinct reconstruction before source adoption.
