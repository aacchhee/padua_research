# PD-T?argmax-bridge-codex-N1-12 — Corrected endpoint assembly and budget

ID kind: PD-T. Aliases: one-correction endpoint certificate; finite-h
endpoint and jump assembly. Split from: the full N1 compact model.
Split into: none. The central/interior outer sum explicitly remains.

## Statement

Let alpha,beta>=0, rho=alpha+beta<=1/2, n>=10^6, m=n+1,
R=128 and delta=1/1000. All kernel, phase, exceptional-mode and
polynomial-collision conventions are those of N1-01/02/09.
Let E_R be the first and last R rows, A_R the special set of N1-02,
and O_delta={r outside A_R: min(v_r,2pi-v_r)>delta}. Define

    K_endpoint = (1/(nm))*{
          sum_{r in E_R} R_r^finite-h
             +sum_{r in A_R outside E_R} Rhat_r }
          +M_strip+M_jump
          +(1/m)*sum_{r in O_delta} H(log n,v_r).     (1)

The exact finite-h rows are N1-09(5); M_strip is N1-10(1), M_jump is
N1-11(3), and H is N1-05(1). In particular M_jump covers the entire
ordinary angular endpoint halves z<=pi/2, not just z<=delta. Then

    |S_n(alpha,beta)-K_endpoint|
       <=r_n+E5(n,128)+D_n+1/32768+1/40000000
       <1/14000<1/4096,                              (2)

where

    r_n=[7pi^4/1800+7pi^3 H_n/900]/n^4,
    E5=a*m^2/[4n^2(R-1)^2]
          +P*pi*m/[8n^2(R-1)]+P*H_n/n+4a/n,
    D_n=10/n^2+20a H_n/(pi*n^2),
    a=(cos alpha+cos beta)/2, P=sin alpha+sin beta.

Extend (1)-(2) by separate absolute phases, giving rho=|alpha|+|beta|
<=1/2. No mesh exchange is used. The endpoint profile and jump sums
have a number of terms/functions independent of n, and all 2R endpoint
rows are exact finite-h functions with O(R^2) evaluation count. The
last sum in (1) still has degree-dependent length. Consequently (2)
is a proved endpoint-reduction bound, not the complete requested model
M(alpha,beta,L) or an all-degree maximum theorem.

## Status and dependencies

Overall status: **PROVED**, analytic developer assembly; independent
review pending. N1-09 proves the finite-h row identities and corrected
quadrature error. N1-10 proves the H-strip compaction; N1-11 the entire
jump compaction. N1-01/04/05 give the special-row and single-pole errors.
The model and correction terms were fixed in ../ideas/N1-round5.md
before their development. No external theorem or numerical fit is used.

## Proof

First form the auxiliary model using the exact single-pole norms B_n
in every ordinary row, the exact finite-h endpoint rows, and Rhat on
the remaining special rows. Add N1-09's jumps on z<=pi/2. Its row
cancellation error is bounded by E5, by N1-09 sections 2-4; the errors
of the remaining special rows are at most r_n. Endpoint rows have zero
error. This use of exact B_n avoids paying its N5 approximation error
a second time.

N1-04 supplies |B_n/n-[2log n+C(t)-2log pi]/pi|<=5/n^2.
The complete nonendpoint coefficient sum is at most
2m+4am H_n/pi. Therefore replacing those exact pole norms by their
regularized Phi products costs at most D_n, exactly as in N1-05's
proof of its connection to the primitive. The resulting ordinary
profile is H(log n,v), while the jump terms are unchanged. Actual
collision rows remain special and are not replaced by profile limits.

On rho<=1/2 there are no collisions in z<=pi/2: the two offsets in
N1-09 stay strictly between successive integers there. Thus the
ordinary endpoint strips consist precisely of the two index ranges
used in N1-10. Its replacement error is less than 1/32768. N1-11
replaces all ordinary endpoint-half jump terms with error less than
1/40000000. These disjoint replacements leave exactly (1), proving
the first inequality in (2).

For the fixed-count finite-h assertion, the nonzero effective rows
have w=r*pi+b bounded away from zero on rho<=1/2. Each F_j in
N1-09(5) is given by the exact sinc/T formula N1-07(5), with
T(y)=y cot y and its continuous value T(0)=1. Thus each of its O(R^2)
terms has a closed finite-h expression, without evaluating a growing
polynomial sum. The row r=0 uses the exact signed-row expression and
its beta=0 continuation. Every exceptional-mode contribution remains
the corrected G_n=D_n-cos(nu) one.

For the budget, N1-09's proof gives uniformly for n>=10^6

    r_n+E5 <1/40000+1/80000+1/10^6.

Also H_n<=1+log n, monotonicity of (1+log n)/n^2, pi>3 and
log(10^6)<14 give D_n<1/10^8. Consequently the total in (2) is less than

    1/40000+1/80000+1/10^6+1/10^8+1/32768+1/40000000
       <1/14000.

This is a rational comparison. Separately the additional endpoint
compaction error D_n+1/32768+1/40000000 is below 1/8192, as required by
the preregistration, while N1-09 proves r_n+E5<1/8192. No empirically
chosen margin is used.

## Precise remaining obligations and gate verdict

The single correction passes its preregistered component test: it
removes both old certificate floors, retains exact finite-h endpoint
rows and compacts the endpoint profile and the whole jump sum. The
unchanged-model STOP and its proved budget obstruction remain intact.
This is the one allowed correction, not a reset or a spare allowance.

The residual O_delta sum includes the central v=pi chart and the
remaining interior. Its degree-independent reduction with a proved
error remains OPEN. In addition, a maximum comparison for the final
model and coverage outside rho<=1/2 remain OPEN. Merely deleting this
sum, fitting it, or treating its present length as fixed would not close
those obligations. The current known error leaves at least
1/4096-1/14000 for a future uniform reduction within the same model;
that arithmetic is not a proof such a reduction exists.

There is therefore no full B3 PASS, no usable argmax onset n1 and no B4
release. The proposed next falsifiable test, only after a new published
boundary and parent authorization, is an explicit central logarithmic
subtraction plus a uniform quadrature modulus for the remaining
O_delta profile. It must fit the remaining budget with a degree-
independent count. It may not add an unregistered second row/jump
correction if this corrected model ultimately fails the original gate.

## Verification and history

No mathematical computation, numerical integral, fit or repeated old
run was performed. All inequalities above are analytic; distinct
review of the frozen support files and this assembly is pending.
2026-11-06, round 5 after fc8c288, requested gpt-6-astra ultra. Previous
rounds' source and review files are unchanged. Root owns the review
integration, publication and any next-round authorization.
