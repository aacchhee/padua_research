# Supplementary independent review — N3 round8 analytic energy bound

2026-11-06. Rules/input `8dc1521cf68f7780bd10e02495f6f71a639c03c6`.
Distinct reviewer `/root/review_bootstrap_r8`, coordinator allocation Astra
high; runtime model/effort metadata unexposed. This analytic subtask was
assigned separately after the maximum-cover review. No author proof,
old record, source, shared registry or Git state was edited. This report
supplements, and does not replace, the required Claude audit.

**ACCEPTED at the stated mathematical scope**, with no unresolved finding:

    W_n <= n^4[(21/32)Lambda_c+1500000000(1+log(n+1))], n>=32,

and consequently W_n<=(3/4)n^4 Lambda_c for every integer
n>=ceil(exp(128000000000)). The intervening energy range129 through that
onset minus one remains OPEN. This is no global argmax onset or complement
certificate, and it does not authorize the finite r8 checker above128.

## Frozen input and scope

Read the entire author theory `theory/N3-uniform-energy-r8.md`,12450bytes,
SHA2565de050b48e6fdc5e3ee62213e5968730d01ea34806aa258a607f0d37c260f61b.
Also read its complete idea/attempt records, PD-T227 and PD-T251, the
complete PD-T367 proof including the exact intermediate sums, PD-T157 and
its PD-T156 lower-bound derivation, and the bootstrap implication/review.
No numerical sweep, symbolic diagnostic or finite experiment was performed
or needed for this review. The exact algebra below is hand reconstruction.

This review judges the inequality and its domains, not novelty or priority;
full state/IDEAS.md was not reread. The author's gate scope, disclosed
reading chronology, shortlist, variant classification and limitations are
in ideas/N3-uniform-energy-r8.md. They were inspected, not independently
certified as an exhaustive search. The author expressly preserves the
original open target and does not infer a uniform energy theorem from the
finite2..128 computation. Prose hashes here are review provenance only.

## Ratios, masks and inherited estimates

The regular nonzero corner terms are exactly k>=1, with the removable00
term separate; the k=0,j>0 even row has zero corner values and is excluded
only from W, not from the inward slopes used by the bootstrap. With
V=|L(c)| and physical ratios q_x=L_x/L, q_y=L_y/L, each regular energy
term is V(q_x^2+q_y^2), with no angular scaling factor missing.

Subtracting PD-T227's exact ratios gives

    q_x=-n^2/2+T_2+T_3+T_4,
    q_y-q_x=-(2n+1)/2+(1-a)/d,

because 2(a^2-b^2)/d^2=-2(a+b)/d. This leaves precisely(1-a)/d.
PD-T367's diagonal cancellation bounds |q_x|<30m^2 and |q_y|<31m^2;
1861(3/2)^4=150741/16<10000, so q_x^2+q_y^2<10000n^4 there.
The cancellation cannot be replaced by separate estimates of singular
summands. The existing proof retains it, including j=n.

For off-diagonal indices parity gives L=|j-k|>=2. Reconstructing the
geometry gives |d|>=DL/m^2, C>=2k^2/m^2, with
D=min(j+k,2n+1-j-k)>=1. The larger endpoint bounds include j=0,j=n,k=m.
The inherited termwise constants22500,61,2000000 and multiplicities
(at most two j for fixed(k,L), at most four pairs for fixed(L,D)) yield

    sum V T_2^2 <=360000n^4 H,
    sum V T_3^2 <=976n^4,
    sum V T_4^2 <=32000000n^4 H,
    H=1+log m.

In particular the last needed sum is obtained directly, not by dividing
an estimate involving a possibly zero a:

    V/d^2=2w C/|d|^3 <=8m^5/(nD^3L^3)
            <=61n^4/(D^3L^3),
    sum_off V/d^2<=976n^4.

Thus all four displayed residual bounds have the exact domain and constants
claimed by the new proof. No uniform per-cardinal O(n^2) ratio is used.

## Diagonal mass reconstruction

For j=k>=1, let s=pi*j(2n+1)/(2nm), t=pi*j/(2nm), so
v=j*pi/m, d=2sin(s)sin(t)>0. Using w<=2/(nm) and C=2sin^2(v/2)
gives

    V<=4sin^2(v/2)/(nm sin(s)sin(t)).

If j<=n/2, then t<=s<=pi/2. Applying sine's chord lower bound to s,t
and sin(v/2)<=v/2 yields

    V<=pi^2 v^2/(4nm st)
      =pi^2 n/[m(2n+1)]<5/m.

There are at most n/2 such indices; their mass is below5/2.
If integer j>n/2, then j>=m/2 and s>pi/2. With r=n-j>=0,

    pi-s=pi[(2n+1)r+n]/(2nm)>=pi(r+1/2)/m,

while t<pi/2. The two chord estimates now give
V<=2m/[j(r+1/2)]<=6/(r+1/2). Summing the r=0 term separately and
bounding the rest by the ordinary harmonic sum proves

    D_n=sum_diag V<5/2+6(3+log n)<=21H.

The endpoint r=0 (j=n) is present, and its endpoint weight was only
increased, never dropped. Consequently W_diag<=210000n^4 H. This is the
substantive improvement over charging its large per-ratio constant to all
of Lambda_c; it does not change PD-T367's hard cancellation argument.

## Square decomposition and exact constants

For b=(-n^2/2,-n^2/2), r=T_2+T_3+T_4 and R=q_y-q_x,
Young's inequality with parameter1/4 gives

    |b+(r,r+R)|^2 <=(5/4)|b|^2+5|(r,r+R)|^2,
    |(r,r+R)|^2<=3r^2+2R^2,
    r^2<=3(T_2^2+T_3^2+T_4^2),
    R^2<=2m^2+8/d^2.

After multiplication by V and summation, the leading coefficient is
5/8 and the residual multiplier is45. The R contribution is
20m^2 Lambda_off+80*976n^4. The constants assemble exactly as

    45(360000+32000000)=1456200000,
    45*976+80*976=122000.

Thus W_off<=[(5/8)n^4+20m^2]Lambda_c+1456322000n^4 H.
The function (n+1)^2/n^4 decreases for positive n. At n=32,
20*33^2=21780<32768=32^4/32, proving the additional coefficient is
<1/32 throughout n>=32. This justifies21/32, with no sampled check of
higher degrees.

The separate00 contribution follows from PD-T227 exactly:

    W_00=(2n^2+1)^2/(36m)+m(2n+1)^2/36
        <=n^4/(4m)+mn^2/4<n^4.

For n>=2, 2n^2+1<=3n^2 and2n+1<=3n give the first step; m>=3 and
m<=3n/2 give the final strict inequality. Adding diagonal and00 to the
off-diagonal estimate yields residual coefficient1456532001, which is
below1500000000 by43467999. The declared inequality follows.

## Lower bound, onset and equality scope

PD-T157's convention takes the maximum of the four corner values.
The two nonnode values agree by node-preserving reflection and are>=2;
the two node corners have value1. Therefore its Lambda_c is exactly the
same nonnode-corner mass used in the energy proof, not a global norm.
Its lower bound, also read in PD-T156, is
Lambda_c>=(4/pi^2)(log n)^2-54, with no global argmax hypothesis.

For ell=log n>=20, pi^2<10 and(3/20)ell^2>=60>54 imply
Lambda_c>=ell^2/4. Also H<=ell+1+log(3/2)<=2ell. Hence

    1500000000H<=3000000000ell<=3ell^2/128
                    <=(3/32)Lambda_c

as soon as ell>=128000000000. Adding21/32 and3/32 gives3/4.
The exact integer ceil(exp(128000000000)) satisfies that condition;
no floating exponentiation or threshold rounding is used. Equality in
this final energy threshold is permitted by the bootstrap premise.

For even n the x reflection, and for odd n the y reflection, permute
the prescribed checkerboard nodes and cardinal polynomials. Absolute
corner values and squared physical derivatives are invariant, so both
inequalities transfer to the second nonnode corner.

The accepted result is the displayed bound for all n>=32 plus its eventual
energy corollary. Combined with the existing finite theorem it supplies
energy on2..128 and on the very large eventual tail. It supplies no claim
on129<=n<ceil(exp(128000000000)), no strict complement, no new global degree,
and no effective argmax onset. The finite checker remains restricted to
its authenticated2..128 premise; this analytic review does not widen it.
