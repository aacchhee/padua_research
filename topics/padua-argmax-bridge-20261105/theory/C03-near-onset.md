# PD-T?argmax-bridge-codex-C03-near-02 — Near-model comparison for log n at least 32

ID kind: PD-T. Aliases: quadratic-remainder near onset; fixed-model
comparison at exp(32). Split from: C03's sharpened noncentral bound.
Split into: none.

## Statement and status

For every integer n with log n>=32 and every alpha,beta>=0 with
alpha+beta<=1/2, N1-18's continuous residual satisfies

    Q_n(alpha,beta)-G_n(alpha,beta)<1/40000.             (1)

Consequently exactly N1-15's unchanged near model satisfies

    M_near(alpha,beta,log n)<=Lambda_c(n)+1/4096        (2)

throughout that domain. The onset is ceil(exp(32)). This is a near-model
comparison onset, not a global argmax onset. The original n>=10^6
comparison remains OPEN, as does the full global theorem; the certified
finite range 2–40 is unchanged.

**PROVED**, analytic developer helper. Dependencies are C03's explicit
noncentral remainder, C01's central majorant, C02's quantitative
degree-limit comparison, and the unchanged N1-15/16/17/18 normalization
and envelopes. No numerical computation, fit or sampled evaluation is
used. The prospective log-onset 32 was registered in ../ideas/C03-near.md.
Distinct supplementary review and formal Claude audit are separate.

## Proof

Write L=log n, rho=alpha+beta, r2=alpha²+beta² and c=15/32. The
three new input estimates give, for every n>=10^6,

    Q_n<=c rho^(3/2)+26r2+(1/2)r2 log(1/rho)
                         +10^-8 beta+5,000,000(L+1)e^-L.       (3)

The origin convention is the continuous value zero for r2 log(1/rho).
N1-16 gives G_n>=A(L)r2 with A(L)>L²/11. Thus if L>=32,

    A(L)-26-32>35.

Allocate 32r2 of the remaining coefficient loss to the fractional term,
and the remainder to the entropy term. Since r2>=rho²/2, maximizing
over rho>=0 gives

    c rho^(3/2)-32r2
       <=27c^4/(32*32³)<27/(512*32³)<2*10^-6.

For D=A(L)-58>35, the same elementary entropy maximization as in C02
gives

    (1/2)r2 log(1/rho)-D r2
       <=(1/(4e))exp(-4D)<10^-8.

The linear allowance in (3) is at most 5*10^-9. Finally (L+1)e^-L is
decreasing for positive L. The elementary bound e>8/3 and the integer
comparison (8/3)^16>6,000,000 imply

    e^32>36,000,000,000,000,
    5,000,000(L+1)e^-L<=165,000,000/e^32<5*10^-6.

Therefore

    Q_n-G_n<2*10^-6+10^-8+5*10^-9+5*10^-6<1/40000,

which proves (1), including the origin. Since e^32>10^6, N1-18 applies
and gives |F_n-Q_n|<9/(2n). The rational comparison

    1/40000+9/(2n)<107/3584000=1/4096-3/14000

holds for all n>=10^6. Hence F_n-G_n is below that last quantity.
N1-15 and the exact normalization S_n(0,0)=Lambda_c(n) give
M_near(0,0,L)-Lambda_c(n)<3/14000. Substituting in N1-17's exact
origin-increment identity proves (2).

## Limitations and next obligation

The constant 25 for the noncentral quadratic remainder is still too
large for the coefficient budget at log(10^6). C02's absolute
5,000,000(L+1)/n error is also much too large there. This theorem
does not replace either with an assumed asymptotic cancellation.
Sharper joint quadratic constants and a proved phase-sensitive finite-h
error are the next obligations. The fixed model, spent correction,
central fractional term, exact log coefficients and certified finite
degree ranges have not changed.

2026-11-06. Rules/input 4b728b04216a5490910780bc609a82b853058426.
Codex, parent-requested Astra ultra; serving metadata unexposed.
