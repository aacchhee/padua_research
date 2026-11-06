# Supplementary mathematical review — D09 check of D08 point-to-box proofs

Rules/read input `084a64f6465956f9c75b5538f83752c30318f151`.
Initial source head `d4956aea3bda9d5ff9917a5b410778fc7adf4fb7`;
final observed head `9d5e8c7a1a8fab6017d5dd9406daec0d834b0bbf`.
Rules are unchanged. Worktree: `/workspace/padua_research`.
Reviewer: distinct Codex agent `/root/d01_far_review`, requested Astra
xhigh; serving metadata unexposed. Formal Claude audit remains separate.

## Verdict and frozen scope

**ACCEPTED as written; no unresolved mathematical finding.** The exact
odd-grid square mean supplies an unconditional global norm. The common
signed-vector derivative and Peano arguments prove both interpolation
contracts, including all axes, zero cardinals, collisions and degenerate
rectangles. The three-loss application proves its stated strict origin
barrier whenever its explicit certified premises hold.

This accepts analytic sufficient statements only. No three-point premise,
successful corner patch, implementation, full cover, new certified degree,
runtime bound or global onset is established by this review. In particular
the coarse global norm is valid but is not asserted to make the proposed
three numerical losses pass.

All five assigned files were read completely; these identities match:

| Record | SHA-256 |
| --- | --- |
| [Global norm](theory/D08-point-box-norm.md) | `3bb26d7e7e196e039e62f2ef0d3eb927cd071f798e7eb6edff0e83a9fae10e8c` |
| [Point-to-box](theory/D08-point-box.md) | `f5a2c138db5d3265ee0a123922d86f3f5f8f826fdb8e19a9693124e385b816cd` |
| [Corner barrier](theory/D08-point-box-corner.md) | `b50ede2debf5714ac0c4d0d67e34a919cf8421e83de6bae77eaf2859d5614cc5` |
| [Idea](ideas/D08-point-box.md) | `cb213e5b374b15d449a2e4c8a15b22cc76f71e7046623964deb158c87f2f3b2f` |
| [Attempt](attempts/D08-point-box.md) | `b55c0211fb4263565f214decf8479ffa8a18dfcfc9d8b9341990d28a12fa4741` |

## Exact normalization, aliases and global norm

There are 4N points on the full shifted tensor grid and 2N on its odd
half. Multiplying by the odd indicator therefore gives precisely
`odd_average(f)=full_average(f)-full_average((-1)^(j+r)f)`.
The phase shifts multiply Fourier averages by phases but do not change
which frequencies survive. Twisting requires simultaneously
k_x congruent n modulo 2n and k_y congruent m modulo 2m. Every such
frequency has l1 size at least n+m=2n+1. The square of G has support
inside l1 size 2n. Its twisted average is consequently zero for every
real alpha,beta, including grid collisions and phase vertices.

In the untwisted average, distinct cosine modes in the second coordinate
are orthogonal since their frequencies never reach 2m. The first
coordinate has the same orthogonality below degree n, with cross terms
to degree n also zero. Its exceptional square is cos^2(alpha), not 1/2:
cos(nu_j)=(-1)^j cos(alpha). The weighted triangular count is
1+4n+2n(n-1)=2N+1. Removing the old exceptional contribution two and
inserting its corrected coefficient-one square gives

    odd_average(G^2)=2N-1+cos^2(alpha)=2N-sin^2(alpha).

Thus Cauchy-Schwarz on the normalized odd average yields exactly the
claimed S upper, without a missing factor of two or endpoint weight.
PD-T364's finite reflection identity supplies lambda<=S in physical
odd-center charts, whose closed domains cover the square. It retains
all endpoint multiplicities and polynomial collisions. This proves the
global physical bound sqrt(2N); neither a sampled maximum nor the
unknown location of the maximizer has entered.

The period adapter also checks. Reindexing by two in j gives the period
(2pi,0), while reindexing by one in both meshes gives (pi,pi). Their
lattice contains (pi,-pi). Separate reflection preserves odd parity and
gives separate phase evenness. Reducing
s=(alpha+beta)/(2pi), t=(alpha-beta)/(2pi) into [-1/2,1/2] by that
lattice yields |alpha|+|beta|=2pi max(|s|,|t|)<=pi. Hence an independently
proved upper on the entire closed diamond really is global. This does
not prove that a particular model upper or numerical phase sample is
such an upper.

## Bernstein and common-vector interpolation

The finite differentiation formula was reconstructed rather than assumed
from a named inequality. On the 2q half-shifted roots, orthogonality
gives the multipliers ip for -q+1<=p<=q. Differentiating the geometric
sum before using r^(2q)=-1 gives

    sum_(ell=-q+1)^q ell*r^ell=2r^(1-q)/(1-r)^2.

After r=1/z and z^q=i(-1)^(k-1), this gives the displayed real
coefficient (-1)^(k-1)/(4q sin^2(t_k/2)), with its correct sign.
The omitted frequency -q has the negative of the +q root values and
therefore gets multiplier -iq. Both endpoint modes are covered.
The finite sine-product second derivative gives sum csc^2=4q^2,
so the absolute coefficient sum is q. Iteration is valid because
derivatives retain degree at most q. Rescaling gives precisely the
alpha bound one and beta bound kappa=n/(n+1), for every derivative
order used in the proof.

For any fixed sign vector, the signed sum of components is bounded by
the same global l1 norm M. At a selected derivative point, choosing
signs to agree with its derivative components gives their l1 sum after
applying the scalar bound. Those signs need not persist at other
points. Thus the argument controls the summed derivative at a common
point; it does not sum separate component suprema and introduces no
cardinal/grid-count multiplier. For the actual cardinals, every real
phase maps into the physical square, so the proved physical M_lambda
is indeed a global bound for every signed polynomial in this step.

The Peano kernel has the stated negative-error sign and mass
(x-a)(b-x)/2. It is nonnegative and identical for all components.
Consequently the l1 integral triangle inequality applies directly to
the common derivative bound even if some cardinal changes sign.
The exact decomposition

    f-I_x I_y f=(f-I_x f)+I_x(f-I_y f)

and the positive interpolation weights add just the two coordinate
errors. No mixed derivative term is required. Taking maxima of each
Peano product gives the M_S/8 constant in ordinary phase coordinates.
This proof differentiates the finite signed G vector, never the
possibly cusped S itself. Positive weights may vanish on closed edges;
nonnegativity and sum one are the properties actually used.

## Squared axes, origin constant and the corner barrier

Each actual signed cardinal composed with -cos(alpha/n),-cos(beta/m)
is separately even and analytic. Therefore its first and third alpha
derivatives vanish at alpha=0, and the analogous beta statement holds.
With u=alpha^2/2, differentiation gives

    h_uu=(alpha*f_alphaalpha-f_alpha)/alpha^3
         =alpha^(-3) integral_0^alpha t integral_0^t f''''(s) ds dt.

The common positive kernel has mass exactly 1/3. Upon scaling t and s
by alpha, it is a fixed-domain integral of f''''(alpha*z), so its
continuous origin value is f''''(0)/3. This also follows from the even
Taylor series and confirms that there is no extra factor of two.
The vector inequality therefore gives ||h_uu||_1<=M_lambda/3 and
||h_vv||_1<=kappa^4 M_lambda/3, uniformly including both axes and the
doubly zero origin. The result holds for all finite nonnegative phase
rectangles; it does not rely on a small-angle expansion.

Applying the common Peano argument yields coefficient M_lambda/6 in
the point-dependent squared-coordinate error. The squared coordinate
widths are (b^2-a^2)/2 and (d^2-c^2)/2. Combining the maximum product
factor 1/4, Peano factor 1/2, derivative factor 1/3 and squared-width
factor 1/4 gives M_lambda/96 exactly. Zero-width intervals contribute
zero error and identity interpolation. Zero cardinals and removable
kernel points pose no differentiability problem for the signed vector.
Applying this squared chart to S would not be justified; the proof
explicitly avoids that inference.

For the origin box, x=u/U and y=v/V are in [0,1]. The three certified
losses give the interpolated deficit at least

    c[x(1-y)U+(1-x)yV+xy(U+V)]=c(u+v).

The mixed terms cancel exactly. The remaining point-dependent Peano
charge is at most M*max(U,kappa^4 V)*(u+v)/6. The stipulated strict
gap in c therefore proves epsilon>0 and the claimed vanishing barrier
epsilon(u+v). Equality is retained at the origin; every other point,
including all nonorigin boundary points, is strictly below Lambda_c.
The true origin stays symbolic. A certified corner lower minus a
certified point upper is a safe lower bound on each actual loss, so
the proposed numerical premises have the correct direction.

For A=pi/4 and B=3pi/16, pi>3 gives A>3/4>1/2 and
B>9/16>1/2. Hence their rectangle contains the entire inward
alpha+beta<=1/2 diamond. Here U=pi^2/32 and V=9pi^2/512<U;
kappa<1 gives max(U,kappa^4 V)=U. The strict coefficient threshold
is therefore exactly c>M*pi^2/192. The three D07 inward turns are
1/(4n), 3/(16m) and their mixed pair, as stated. Physical turns,
scaled phases and radians are not interchanged.

The node-preserving reflection is in x for even n and in y for odd n.
It permutes the cardinals and exchanges the two nonnode corners without
swapping n and m, so all kappa factors and loss statements transfer.
This is pointwise descent under certified losses, unlike N3's
maximum-exclusion implication before global closure.

## Novelty gate and source coverage

The complete 1112-line registry reading from this continuing review
assignment was reused at its unchanged initial SHA-256
`68bf789c82967944421e6fc54f8164dbdb91d1096fa10694008261fbd54f9e9d`.
This is explicit reuse, not a claim of another fresh full-file reading.
Fresh D09 searches covered the full heading/alias inventory and Peano,
Parseval, Riesz, signed dual, Bernstein/Markov, interpolation, squared
coordinates and related norms; the scoped obstruction tables and
retained-alias table were refreshed. Searches included literature INDEX and current topic
records. Broad search output was scoped, and no external fulltext or
historical-priority claim is made.

Fresh full relevant proof reads include PD-T210 and its constructor
appendix, PD-T227, PD-T364, PD-N079/085/086, C14, N3 corner-radius
reduction, N3 bootstrap-corner and N3 uniform-energy-r8. Full candidate
comparison includes original/final IDEA320/330, IDEA338's candidate and
R1/R2/R5 attempt, the full H2-H3 candidate record including IDEA460,
the N3 uniform-energy and bootstrap-cover candidates, and C12/C15
attempts. C12/C14/C15 candidate records and PD-T101's complete cardinal
normalization were already read in this continuing assignment and are
reused. D07's source/point-domain review is also already complete.

During this review the parent merged the conditioning continuation.
The entire six-row/paragraph update and 23-line append were then read,
including IDEA590–603. The resulting 1135-line registry SHA-256 is
`08e6886269a7bb76eaeb60b57f37935f5a390f37ae1df5d0167cdaac2ed7093a`;
this is a file hash, not a commit. The new IDEA598 entry prompted a
full read of its original candidate and PD-N183 proof. That obstruction
concerns an unweighted equispaced grid-supnorm derivative transfer.
D08 uses a proved global continuous norm for a trigonometric signed
family, so it does not assume the refuted discrete norm inequality.
The merge leaves all assigned D08 proof hashes and repository rules
unchanged and introduces no different matching point-to-box theorem.

The precise separation from the closest predecessors survives: signed
aggregate derivative control belongs to PD-T227/IDEA460, positive
certificate weights to PD-T210, and artificial coefficient-vertex
uppers to C12/C14/C15. D08 supplies the stated actual-point interpolation
remainders and their squared-origin loss application. The record
appropriately calls this a technical quantitative variant. It assumes
neither PD-N085's affine sign preservation nor PD-N086's coarse fixed
signs, and it preserves PD-N079's primitive cusp obstruction.

## Execution and remaining adoption obligations

Analytic reconstruction only, within the assigned twenty-minute block.
No numerical/scalar helper, native library, root solve, board, quadrature,
point call or cover was executed. File reads/searches, clock reads and
identity checks are not independent numerical verification. There is
no scientific runtime or measurement receipt for this review.

A future producer still must enclose M upward, certify a corner lower
and all three actual point uppers, form safe lower losses, and verify
all normalized-loss inequalities and the strict positive gap outward.
The three nonorigin calls alone do not supply those additional inputs.
It must retain D07's literal n<=2048/input/failure guards and the exact
radian-to-inward-turn conversion. Full complement coverage remains a
separate obligation even after a successful local patch instance.

Preliminary and final conclusions were communicated to the parent.
No author/source/shared/Git edits, no fixes and no stronger statement
were introduced. Only this assigned report was written.
