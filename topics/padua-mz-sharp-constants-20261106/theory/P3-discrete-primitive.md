# PD-T?mz-sharp-codex-P3-02 — a sharp leading discrete primitive bound

ID kind: PD-T.
Aliases: discrete log-Hardy norm; oscillatory logarithmic primitive.
Split from: supporting sharp primitive estimate for PD-T020.
Split into: none; the original limit target is separate.

## Statement and definitions

Let T>=1, J=floor(T), H_J=sum_(k=1)^J 1/k, and let g be any
real or complex sequence supported on 1,...,J. Put

    S(t)=sum_(k<t) g_k/k,   E=sum_(k=1)^J |g_k|^2/k,
    A_J=2H_J/pi+1.

Then

    integral_0^T sin^2(pi t)|S(t)|^2 dt/t
       <=(A_J^2/2+3/2)E.                            (1)

In particular the right side is [2/pi^2 (log T)^2+O(log T+1)]E,
with an absolute implied constant. No smoothness or sign assumption
is imposed on g; the average factor 1/2 is uniform over every input.

## Assumptions and status

Exact finite sequences, natural logarithms, Lebesgue dt/t.
Overall status: PROVED in analytic development. This is a supporting
operator estimate, not a proved case of PD-T020. No computation.

## Depends on

S1-volterra-model.md (S1-01): ||V||=2/pi, and its rescaling to an
interval of length H_J. The remaining steps are proved below.

## Proof

Put H_0=0 and embed g as the function f(x)=g_m on
(H_(m-1),H_m]. Its squared L2 norm is E. For F(x)=integral_0^x f,
one has F(H_m)=S_m:=sum_(k<=m)g_k/k. Let Z be the function
equal to S_m on the same harmonic interval. Since

    integral_(H_(m-1))^(H_m) |Z-F|^2dx=|g_m|^2/(3m^3),

one has ||Z-F||<=sqrt(E), and the exact Volterra norm gives

    sum_(m=1)^J |S_m|^2/m=||Z||^2<=A_J^2 E.          (2)

For integer m>=1 the ordinary-cell oscillation satisfies

    integral_m^(m+1) sin^2(pi t)dt/t
      <=(1/2)log(1+1/m)+1/(4m^2).                   (3)

Indeed the unweighted integral of sin^2(pi t)-1/2 on that cell is
zero. Replace 1/t in the difference by 1/t-1/m, bound the sine
difference by 1/2, and integrate (t-m)/m^2 to obtain the error.

Cauchy–Schwarz gives |S_m|^2<=H_m E. Moreover H_m<=2sqrt(m),
and sum_(m>=1)m^(-3/2)<=3, so

    sum_(m=1)^J |S_m|^2/m^2<=6E.                    (4)

On (m,m+1), S(t)=S_m. Enlarge the last partial cell to the full
cell, which only increases the nonnegative integral; S=0 on (0,1).
Sum (3), use log(1+1/m)<=1/m, then apply (2) and (4). This proves
(1), including integral and nonintegral T. Finally H_J<=1+log J
<=1+log T proves the displayed asymptotic consequence.

## Checks, sources, scope and open items

Pure analytic proof, no numerical input or execution. Gate and
candidate: ../novelty-gate-P3.md, ../ideas/P3-reverse.md. Rules/source
`0205690b9c4e959a28e949083e9a1808735abf4b`; R release
`17ca9f441cece178354e70504a6c739df501a224`. This lemma by itself
does not normalize actual CC weights or control endpoint columns.
Independent mathematical review remains separate.

## History

2026-11-06, P3 round2, Codex developer; requested gpt-6.1-sol xhigh,
serving metadata unexposed. Separate substantive supporting lemma;
the accepted Volterra statement/proof is unchanged.
