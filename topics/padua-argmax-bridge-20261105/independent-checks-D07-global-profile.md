# D07 global outer profile and mesh — distinct mathematical review

2026-11-06. Rules/review head
`2e4ac49fa0687a7736bc1df82c12e6483b1c7a94`.
Reviewer: Codex, distinct agent `/root/d01_corner_review`, parent-requested
`gpt-6-astra`, high. Serving model/effort metadata are not independently
exposed. Author allocation: Sol xhigh. This is supplementary mathematical
review, not the formal cross-provider Claude audit.

## Verdict and exact scope

**Both claims ACCEPTED as written. No BLOCKING, MAJOR or MINOR findings.**
The fixed-six-row global intermediate has the stated full closed-phase
outer error for n>=16. On the closed near half diamond its outer charge
is strictly below 1/64 for every integer n>=10000. The exact h/g/Gamma
identities, completed-constant matching, and Bmesh/Blog bounds are valid
on their stated full domain.

The 1/64 conclusion concerns only E_global. It includes neither E_D04
nor the difference between the new intermediate and M_infty. The term
|J6-C_2| remains explicit and unbounded by these two files. This review
uses no separately authored D07 retained-row result and therefore has
no circular dependence on its pending review. A useful complete
M_infty allowance, relative comparison, interval implementation or
argmax threshold does not follow from the reviewed claims alone.
The existing global threshold remains 500000.

## Frozen inputs, rules and gate

All four assigned files were read completely and directly hash-checked:

| File, relative to this topic | SHA256 |
| --- | --- |
| theory/D07-global-outer.md | `84e43b4ba67bca6cdf19320a4f2ae16aa692b5c5b787fdc63303c19c8e174ec2` |
| theory/D07-global-mesh.md | `d33980848d3ab9fb3ac393a76673f328ac1d7886df964978fe27b18d570d5589` |
| ideas/D07-global-profile.md | `4bb2d5a12f434d2a53df6776815e95fd9c905345b58486c718ba0c49ca73a4b2` |
| attempts/D07-global-profile.md | `6a261e963837ab508e161e207cbb605d1dabc1a1ad39915e4dd0ea836f1b512b` |

The accepted fixed-special theorem is unchanged at
`5df0e17dce65cb917f967e3066a46b628e6cf9284c00e8e0b5af8816ebb2fc16`,
and its distinct review is unchanged at
`4c69a09fc5c848be981ed2535a9836f422b42131f51a6dba080b796e47307c94`.
The accepted D05 outer-variation proof remains
`47fc61298520609f591c03eea323e93949d59d54cbcfa90e0d4943548113bd66`.
These are inputs, not claims reconstructed from new samples.

AGENTS/WORKFLOW/CODEX were read in this agent session. The rules-only
diff from f9b64a6 to this head is empty; root owns all Git/shared work.
The complete 1112-line state/IDEAS.md and every obstruction/disposition
table were read earlier by this same reviewer. Its refreshed SHA256
is still `68bf789c82967944421e6fc54f8164dbdb91d1096fa10694008261fbd54f9e9d`.
This retains the full identical-byte reading without claiming another
full 291 KB read in this subtask.

Fresh searches/reads covered global regularization, harmonic/logarithmic
meshes, Gamma, cell gaps and cutoff/budget obstructions. Read the full
new candidate/attempt; refreshed N1-round4-mesh.md and
N1-round6-regular-variation.md in full, C06's full-phase numerator and
central-cancellation proof, and D02-far-bias-identity.md in full.
D05's complete outer proof/review, fixed-special proof/review, D04's
reference and row proofs, N1's endpoint sources, and D06's scoped
allowance obstruction were read in this same session for the preceding
reviews. Their conclusions are reused at the accepted scope. The
separately owned D07 endpoint/central/six-row proofs were not imported.

The duplicate disposition is correct: A_reg's bounded variation and
the actual-cell regularized midpoint estimate already occur in D05
and N1-13. D07 does not present them as new. The distinct quantitative
step completes the fixed cell union after both singular subtractions,
retains exact global reference meshes and exact rows, and pays the
actual missing intervals. This changes the allocation underlying D06's
specific obstruction; it does not contradict that obstruction or
silently modify an old model. No historical novelty or external-source
claim is made.

## Global cell completion

### Literal fixed labels and endpoint geometry

For R=2 the fixed ordinary physical labels are r=2,...,m-2 on the
left and r=m+1,...,2m-3 on the right. On the right put
k=2m-1-r; then z=h(k+1-t). Consequently both folded index sets are
exactly k=2,...,m-2, with offsets t and 1-t, including t=0 and t=1.
There are no moving collision holes because the accepted fixed-special
theorem already continues the complete H values at those ordinary
labels. It does not assert rowwise equality between H and a collision
polynomial norm.

The centered-cell endpoints are exactly

    l_L=h(3/2+t),       l_R=h(5/2-t),
    u_L=pi-h(3/2-t),    u_R=pi-h(1/2+t).

Thus the initial missing lengths total 4h and the central missing
lengths total 2h. For m>=17 the initial endpoints lie between 3h/2
and 5h/2, with 5h/2<pi/4; the upper endpoints exceed pi/2. The
largest ordinary sample is still at most pi-h, so no ordinary sample
is evaluated at the central logarithmic singularity. All these bounds
hold at both endpoint phases and for both degree parities.

The D05 BV theorem applies with epsilon=3h/2<=pi/4 and yields the
actual-cell normalized charge (L V_A+V_B)/(2m). Its proof handles
moving coefficient/root transitions and weighted offsets already;
D07 changes no such hypotheses. The normalization is h/pi=1/m,
and the variation is the combined two-side variation, not a per-cell
constant multiplied by the number of cells.

### Initial and central missing intervals

From the exact global max formulas, |f_s|<=M_A. The initial L*f_s
loss is therefore 4L*M_A/m. The accepted endpoint residual envelope
has integral

    J_P(x)=x[7+(P/pi)(5+2log(4pi/x))].

Its second derivative is -2P/(pi*x)<=0. Jensen at the two actual
initial lengths, whose average is 2h, bounds their combined normalized
residual integral by 2J_P(2h)/pi=Q(P,2h). At P=0 this is the exact
linear-envelope case. Both gaps lie in the proved z<=pi/4 envelope
domain; no larger strip or arbitrary phase-dependent cutoff is used.
There pi-z>1 and |log(pi-z)|<=log pi, giving the additional initial
central-reference charge 4d log pi/(pi*m).

For the missing central intervals, C06 proves the full-phase bounds
|P_s|<6 and |I_s-d log(pi-z)|<4 on pi/2<=z<=pi. Since log z/z<=1/e
there, the remaining regular profile satisfies

    |F_s|<=L*M_A+6+(4+4a/e)/pi=L*M_A+C_B.

Its two missing lengths total 2h, so their cost is
2(L*M_A+C_B)/m. This uses the unnormalized log(pi-z) bound from
C06's central proof, not the different normalized logarithm ell used
later in that source's interior bookkeeping. The full-phase C_B<8
follows from e>5/2, pi>3 and a<=1.

Adding the cell, initial and central charges gives exactly E_global.
The actual six rows, Delta_2 and both singular meshes agree in
K_fixed and the new G_n and cancel algebraically. Hence
|K_fixed-G_n|<=E_global. Adding the accepted E_D04 gives the second
inequality; E_D04 is not included in E_global or silently reduced.

### Near-domain constants and the all-n threshold

On rho<=1/2, p,q,P,d<=1/2 and a<=1. N1-13's explicit bounds give
M_A<3/5 and V_A<6/5. For the entropy term, the D05 argument gives

    Gpar<=p[1+log(6/epsilon)]+p log(1/p)
         <=(1/2)[1+log(2m)]+1/e,

with its continuous zero value at p=0. Also ell<=log(2m).
The braces of V_B are bounded by 50+(11/2)log(2m), giving
V_B<40+(11/6)log(2m). The initial envelope contributes
[94/3+(4/3)log(2m)]/m, and 4d log pi/pi<4/5. Combining with
C_B<8 yields respectively

    L coefficient:        3/5+18/5=21/5,
    log(2m) coefficient:  11/12+4/3=9/4,
    constant:             20+94/3+4/5+16=1022/15.

These reconstruct E_near exactly. Its derivative numerator is the
one in the theory and is strictly negative for all real n>=16:
the positive derivative terms are below 11, while the constant in
the numerator exceeds 68. At n10000, both logarithms are below 10.
The elementary exponential partial sum gives e>163/60>19/7, and
the exact integer comparison 19^10>20002*7^10 suffices. Therefore

    E_near(10000)<3979/300030<1/64,

where the final integer comparison is 254656<300030. Monotonicity
proves the full n>=10000 assertion; no sample grid, fitted threshold
or new numerical execution is used. Only this simplification uses
the near domain; the general E_global formula remains full-phase.

## Exact singular meshes and completed constant

### Finite telescopes and Gamma endpoints

The h_j definition is the limit of
sum_(k=j)^K 1/(k+t)-log(K+t+1/2); g_j is the corresponding limit
with log(k+t)/(k+t) and half the squared logarithm. Subtracting two
such definitions cancels their absolutely convergent tails and gives
exactly h_j-h_(K+1) and g_j-g_(K+1) for the finite sums. Here
K=m-2, so the endpoint is m-1, independent of phase. Direct substitution
of h=pi/m gives

    T(L,h(k+t))/m
      =[D0-B0 log(m/n)]/(k+t)+B0 log(k+t)/(k+t).

Thus the coefficient is Z_n, including the exact n/m displacement,
and Tmesh has the written factors. No old e_mesh or C_X approximation
is involved.

For the central logarithm, each side contains m-3 terms and
pi-h(k+t_s)=h(m-k-t_s)>0. Reversing the finite product gives
Gamma(m-1-t_s)/Gamma(2-t_s). For the two offsets this is precisely
the four Gamma arguments in Cmesh. The denominator arguments belong
to [1,2]; the numerator arguments are at least m-2. There are no
Gamma poles at t=0 or 1, no rounding or Stirling approximation, and
no missing factor of 1/m: Cmesh is the unnormalized log sum, later
multiplied by d/(pi*m).

### Full regular integral and signed matching

Write l=log delta and c=log pi. Integrating the two copies of S0
over [delta,pi] with normalization 1/pi gives

    2(U0/pi)(c-l)+B0(c^2-l^2).

Adding this to B0(l-c)^2+2D0(l-c) cancels exactly because
D0=U0/pi+B0*c. Therefore K_delta equals the normalized integral
of Z_L+Z_R on [delta,pi], with no residual constant. The accepted
integrable endpoint envelope allows delta down to zero and gives
K_0=integral_0^pi(Z_L+Z_R)/pi. The central logarithm is integrable;
no divergent channel integral has been evaluated separately.

Likewise the exact b_end formula plus the complementary coefficient
integral cancels its two log(delta/pi) terms, leaving
b_full=2D0+integral_0^pi(f_L+f_R)/pi. Finally
integral_0^pi log(pi-z) dz=pi(log pi-1). Thus

    U(L)=(b_full-2D0)L+K_0-(2d/pi)(log pi-1).

The factor two comes from the two folded sides, and the remaining
factor 1/pi from the central term in F. Insert this and the exact
meshes in G_n, then use Delta_2=E_infty-E_2 and
M_infty=B0 L^2+b_full L+E_infty+K_0. The result is exactly the
displayed J_n, including -E_2,-B0 L^2,-2D0 L and the central sign.
The R=2 Delta identity is already accepted in D04; no R>=64 tail
bound has been extended to R=2. The central and endpoint weighted
phase limits remain those of D02/D05, including a=0.

## Scalar remainder estimates, with the six rows still retained

The two upper dimensionless cell endpoints are
b_L=n-1/2+t and b_R=n+1/2-t. Set c=t-1/2, so they are n+c,n-c,
with |c|<=1/2. N1-06's tail estimates apply to these exact finite
sums, with b>=n-1/2 and without a small-strip assumption on the
scalar shifted-sum identity.

Putting eta_+=log(1+c/n), eta_-=log(1-c/n), and j=eta_++eta_-,
the expansion before absolute values is

    Rmesh=-B0*eps_n*(2L+H2)
          +(D0+B0*L-B0*eps_n)*j
          +(B0/2)*(eta_+^2+eta_-^2)+tail.

This follows by expanding the two squared logarithms and the harmonic
part together. In particular an artificial uncancelled upper-end L^2
term is not retained. Elementary log estimates give

    eps_n<=1/n,
    |j|=-log(1-c^2/n^2)<=1/(4n^2-1),
    |eta_+|,|eta_-|<=1/(2n-1).

The combined two-side tail is at most
[|Z_n|+B0(log(n+1/2)+2)]/[4(n-1/2)^2]. These yield each of the
four terms of Bmesh with the written constants. B0 is nonnegative
and can be exactly zero; no division by it or by a phase occurs.

For Rlog, each ordinary union has log(pi-z) variation at most
log(2m), since its distance from pi is at least h/2 and at most pi.
The total normalized centered-cell error is at most log(2m)/m.
The initial missing intervals have total length 4h and cost at most
4log pi/m. Each central missing length is below 1 for m>=17;
their sum is 2h. Concavity of x(1-log x) bounds the combined absolute
central log integral by 2h(1-log h). After normalization, the three
charges sum to

    [3log m+log2+2log pi+2]/m=Blog.

Subtracting E_2=C_2+D0 H2+B0 G2 in the exact J identity gives
J_n=(J6-C_2)+Rmesh+(d/pi)Rlog. Its triangle inequality is therefore
the displayed bound in the theory. This estimates only the scalar
complement; no proof of smallness of J6-C_2 is assumed. The six rows
continue to mean actual corrected finite polynomial norms.

## Execution and remaining limits

Paper review only. Tools performed file reads/searches, hash checks,
`git rev-parse HEAD`, and a read-only rules diff. No numerical scalar
helper, native binary, board, quadrature, fit, phase grid, degree job
or source implementation was executed. Rational comparisons above
were checked as paper algebra; no computational receipt is claimed.
Only this assigned report was written. No author proof, old model,
shared record or Git state was changed.

The exact formulas use a bounded number of h/g/Gamma expressions,
but that is not a bit/operation/runtime guarantee or an outward
evaluator. The current acceptance establishes the new outer charge
and exact mesh complement, not a whole-box source contract, the
separate six-row bound, a complete useful M_infty budget or a global
argmax conclusion. Root was notified of the mathematical result
before this report was written.
