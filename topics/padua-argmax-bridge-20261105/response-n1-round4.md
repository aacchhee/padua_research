# N1 round-4 response — F1

2026-11-06. F1 in [the independent review](independent-checks-n1-round4.md)
is accepted: the original N1-08 proof omitted the case where both right
endpoint offsets are integers. The original source is preserved at
`7e457c7fc54b32b45b0870d53a5fd4c37cd45fce`, file SHA-256
`4a9b0f908f0b5cf12dbf56856bee47da47f860ef1c5f9fd5bf01f00676edc552`.

The [corrected proof](theory/N1-round4-endpoint-block.md) now treats
eta_-=1, eta_+=0 explicitly. They force alpha=0, beta=pi-z, so
c_e=c_d=sin(z/2) and C=D=0. The two distinct polynomial pole samples
each equal n/2; all others vanish. Therefore R_r=n and H(L,v)=1,
giving exactly zero correction in (6). The subsequent ordinary-norm
argument is now explicitly restricted to a single pole channel.
The reviewer's n=16, beta=7pi/8, r=31 example has z=pi/8 and thus
R_r=16, H=1 by this exact calculation.

Corrected SHA-256:
`49c910ab1835008fd70cb2968fdea01773e427adc1541832c10dd379317fcc62`.
An executed source comparison confirms that the complete statement,
definitions and error-bound block before the status section is byte
identical to the original. N1-06, N1-07 and the budget proof retain their
previous hashes. No mathematical program, fit or numerical test was run;
the correction is analytic. The reviewer report was not edited.

F1 is addressed in development; focused independent re-review is pending.
This repairs proof coverage within round 4 and spends no model correction.
The separate budget obstruction still requires its own independent review.
