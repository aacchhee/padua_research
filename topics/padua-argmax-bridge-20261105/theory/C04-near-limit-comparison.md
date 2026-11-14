# PD-T?argmax-bridge-codex-C04-near-02 — The limiting residual fits the n>=10^6 budget

ID kind: PD-T. Aliases: directional central allocation; limiting residual
margin; exp(30) near-model onset. Split from: C04's constant-eight remainder.
Split into: none.

## Statement and status

Let T be C02's actual fixed-model limiting function, and G_n the unchanged
N1-17 coefficient loss. For every integer n>=10^6 and every alpha,beta>=0,
alpha+beta<=1/2,

    T(alpha,beta)-T(0,0)-G_n(alpha,beta)
                          <1/50000+3/(2*10^9).        (1)

This is a comparison for the limiting residual. The actual continuous
Q_n has not been replaced by its limit. Independently, the existing
explicit finite-degree estimate implies

    Q_n-G_n<1/40000, and
    M_near(alpha,beta,log n)<=Lambda_c(n)+1/4096,       (2)

for every integer n with log n>=30, on the same closed phase triangle.
The original actual comparison for every n>=10^6 remains OPEN; (1)
specifies how much finite-degree error that target can still afford.
No global argmax onset or change to certified degrees 2–40 is asserted.

**PROVED**, analytic developer helper. Dependencies: C04's noncentral
constant-eight bound; C01's directional central bound; C02's uniform
degree-limit error; the original N1-15/16/17/18 coefficient and normalization
identities. No numerical calculation, fitting or sampled evidence is used.
Independent supplementary review and formal Claude audit are separate.
The main limiting target was recorded in ../ideas/C04-near.md before this
proof was written. The log-onset30 corollary is a direct scalar refinement
of C03's existing onset allocation, not another model or computation.

## 1. Keep the directional central constants

The sharper directional bound proved in C01 is

    I_c(alpha,beta)-I_c(0,0)
       <=(15/32)alpha^(3/2)
           +(4/9)alpha²[1+log(1/alpha)]
           +(1/9)beta²[3/2+log(1/beta)]+r2/16.

All zero-axis expressions have their continuous values. Add C04's
noncentral bound. With c=15/32 this gives

    T-T(0,0)
      <=c alpha^(3/2)+(1225/144)alpha²
                   +(4/9)alpha²log(1/alpha)
          +(395/48)beta²+(1/9)beta²log(1/beta)+10^-9 beta.     (3)

This retains the actual alpha directional fractional term, rather than
replacing it by a larger radial term for this allocation.

For n>=10^6, L=log n>69/5 and pi²<10. N1-16 therefore gives

    G_n>=A(L)r2,
    A(L)>47(69/5)²/480+(69/5)/240
          =224457/12000>187/10.                      (4)

## 2. Scalar alpha and beta budgets

First suppose alpha>=exp(-8). Its logarithm in (3) is at most eight,
so (4) leaves a quadratic alpha loss greater than

    187/10-1225/144-32/9=531/80>33/5.

The elementary maximum over x>=0 gives

    c x^(3/2)-(33/5)x²<=27c^4/[256(33/5)³]<1/50000.   (5)

The last comparison is rational, with c=15/32. Explicitly its numerator
after reduction to a positive-denominator fraction is 170859375 and its
denominator is 268435456*35937; multiplication by 50000 verifies the
claimed inequality.

If 0<alpha<exp(-8), drop its negative quadratic loss. The function
x²log(1/x) increases on (0,exp(-8)], so the remaining terms are at most

    c exp(-12)+(32/9)exp(-16)<10^-5.                 (6)

For an elementary check, e>8/3 gives e^12>100000 and e^16>6000000;
the two terms in (6) are below 5*10^-6 and 6*10^-7, respectively.
The alpha=0 value is zero. Equations (5)–(6) therefore give the uniform
alpha allowance 1/50000.

For beta, the remaining quadratic coefficient is greater than
187/10-395/48>10. The exact entropy maximum is consequently

    sup_(x>=0) x²[(1/9)log(1/x)-10]
                   =(1/(18e))exp(-180)<10^-9.         (7)

The fixed-slope term in (3) is at most 1/(2*10^9). Adding the three
allowances proves (1).

## 3. The unconditional exp(30) near onset

The radial C01 bound and C04 now give, for every n>=10^6,

    Q_n<=c rho^(3/2)+9r2+(1/2)r2log(1/rho)
                        +10^-9 beta+5000000(L+1)e^-L.        (8)

Here the only finite-degree premise is C02's already proved estimate.
When L>=30, A(L)>900/11 and A(L)-9-32>40. Allocate 32r2 to the
fractional term, and the rest of the available loss to the entropy term.
Exactly as in C03, these cost less than 2*10^-6 and 10^-8, respectively.
The fixed-slope term costs less than 5*10^-10. Since e>19/7 and
(19/7)^10>20000, e^30>8*10^12. Monotonicity of (L+1)e^-L gives

    5000000(L+1)e^-L<=155000000/e^30<31/1600000.

Thus the total excess in (8) above G_n is less than

    2*10^-6+10^-8+5*10^-10+31/1600000<1/40000.

The same N1-18 rational artifact allowance and N1-17 origin identity
used in C03 then give the M_near inequality in (2). This proves the
stated actual near-model onset ceil(exp(30)).

## Exact remaining finite-degree obligation at n>=10^6

Equation (1) leaves an explicit positive allowance. For example, a proved
uniform one-sided estimate

    Q_n(alpha,beta)-[T(alpha,beta)-T(0,0)]<=1/250000,
       n>=10^6, rho<=1/2,                             (OPEN)

would imply Q_n-G_n<1/40000 throughout the originally requested range,
because 1/50000+3/(2*10^9)+1/250000<1/40000. A sharper phase-dependent
version may suffice without satisfying this uniform absolute target.
No such bound is claimed here. In particular C02's absolute error is
not small enough at n=10^6, and pointwise convergence cannot replace it.

2026-11-06. Rules/input 4b728b04216a5490910780bc609a82b853058426.
Codex, parent-requested Astra ultra; serving metadata unexposed. All
previous frozen proofs and reviews are unchanged.
