# Independent supplementary review — C04 constant eight and limiting budget

Reviewer: distinct Codex `/root/c01_near_review`, parent-assigned Astra high;
serving identity and effective effort are not independently exposed.
Date: 2026-11-06. Rules were read at
`4b728b04216a5490910780bc609a82b853058426`; their diff to review input
HEAD `b6e67b3c78cb668b6d2f9da5a5560537d2960bf3` is empty.
Branch: `codex/padua-argmax-bridge-20261105`.

**Final disposition: accepted at the stated scopes, with no unresolved
finding.** The one MINOR degree-domain wording finding was corrected by
the author and independently closed below. The noncentral constant-eight
bound and limiting comparison at n>=10^6 are proved. The actual near-model
comparison is proved for log n>=30. These are distinct conclusions: the
actual comparison for every n>=10^6 remains OPEN. Formal Claude audit is
separate and remains pending.

## Frozen source identities and method

| Source | SHA-256 |
|---|---|
| `theory/C04-near-sharp-remainder.md` | `c8a2244e1e3ebb5a739134421df70745f67fdb57e26ce52714a3698054d7cfe4` |
| `theory/C04-near-limit-comparison.md`, original submitted bytes | `0eca9bddfcbcf3f6fa2713846338f90f7c6849d380ab35adce57ce8f70f4a210` |
| `theory/C04-near-limit-comparison.md`, corrected wording | `3544d01605560ad498e96648841d8ce9c1a4bfbe69e1b94573112995df6aac1a` |

The original files and C04 idea were read in full. The C03 proofs were
independently reconstructed in the separate `independent-checks-C03-near.md`.
The fixed T definition, all N1 dependencies and the C01/C02 central and
finite-degree estimates retain the identities used in the preceding review
reports. Full N1-04 was refreshed, PD-T270's harmonic proof was read in full,
and PD-T269's local cotangent partial fraction was inspected. In particular
the sign of the integer derivative atom is verified from the actual series.

The scope is analytic validity, including the distinction between limiting
and finite-degree comparisons. Historical novelty, priority, registry
allocation and a full author-search audit are excluded. No mathematical
program, numerical integral, fit or sampled evidence was used. A read-only
string/hash program checked the author's single wording change; it was a
source-integrity check only. No author source, previous report, shared file
or Git state was edited by the reviewer.

## One-sided periodic second derivative, including its atom

The N1-04 expansion on 0<t<=1/2 is exactly

    Phi(t)=sinc(pi t)+k0 sin(pi t)/pi+R(t)sin(pi t)/pi,
    k0=2gamma-2log pi,
    R(t)=2 sum_(j>=1) zeta(2j+1)t^(2j).

The differentiated power series converge uniformly on this closed
half-period. Positive coefficients and zeta(2j+1)<5/4 give
R'(t)<=5t/(1-t²)². They also make R'' increasing. Differentiating
the reciprocal C series at 1/2 gives C''(1/2)=28zeta(3); subtracting
(1/t)''=16 yields R''(1/2)<19, with the stated normalization.

The sinc integral yields its second derivative upper bound
-pi²(1/3-pi²/40)<=-pi²/12. The k0 term contributes at most
(5/4)pi, since gamma>23/40 and log pi<6/5. For the cross term,
cos(pi t)<=pi(1/2-t) and

    3(1-t²)²-40t(1/2-t)=3+34t²+3t^4-20t>0

give 2R'(t)cos(pi t)<=3pi/4. The term -pi R(t)sin(pi t) is
nonpositive and is legitimately dropped. The remaining R'' contribution
is at most 19/pi. Thus Phi''<=-pi²/12+2pi+19/pi<12 on the
open half-period. The rational bounds 31/10<pi<22/7 suffice for
the final comparison.

Reflection has no derivative jump at a half-integer because C is symmetric
there and C'(1/2)=0. At an integer, the right derivative is k0 and the
left derivative is -k0, so the jump is 2k0<0. Consequently the global
distributional inequality Phi''<=12dt includes every atom. Convolving
with the nonnegative triangular second-difference kernel proves (3)
with total kernel mass t², without a positive cusp allowance.

Apply this to C03's exact paired folded numerator. Nonnegative cosine
weights are at most one, and the baseline cosine change multiplies
Phi>=0, so its contribution is nonpositive. With
t_-²+t_+²=r²/(2pi²) and integral_delta^pi csc(z/2)dz<18,
the pole increment is at most 54r²/pi³<=(15/8)r².
Both coordinate phases and t_- of either sign are covered.

## Endpoint baseline loss

The positive reciprocal origin sum P0 has exactly the row counts in (5):
twice r=1,...,R-1 and once r=R. From PD-T270,

    H_odd(r)>=0.5log r+log2+gamma/2-1/(32r²).

For the log-weighted sum, monotonicity of log x/x for x>=3 and
the r=2 term give

    sum_(r=1)^(R-1) log r/r
       >=0.5log²R-0.5log²3+0.5log2
       >0.5log²R-1/3.

Together with H_(R-1)>=log R>24/5, log2>69/100,
gamma>23/40 and sum r^-3<5/4, this gives exactly the written
lower bound greater than 10 for sum H_odd(r)/r. Multiplication by
16/pi²>8/5 proves P0>16 without using the additional positive
unpaired origin term.

C03 gives P-P0<=d_P beta+K_P r², where d_P>0 follows by direct
differentiation of the unpaired b=-beta reciprocal row. Its right side
is nonnegative. Multiplication by a<=1 is therefore valid in the form

    aP-P0<=d_P beta+K_P r²-(1-a)P0.

The paired sine and closest-row contributions remain nonpositive. Adding
the already charged unpaired sine remainder and using
1-a>=47r²/192 yields the coefficient 5-47/12=13/12 and exactly
the same d_C beta. No first-order cosine term is introduced or removed.

## Coupled strip and endpoint cancellation

The expression E in section 3 combines exactly the singular strip
constant and the cancellation integral on [delta,pi/2]. Its common
factor a and D dependence agree with the fixed T definition. The
central integral Ic is still excluded here.

All h_J corrections to the initial negative logarithm are nonpositive
by convexity, so -H(beta)>2log(127.5)>48/5 for the actual finite
J=4096 constants. The elementary exponential comparisons in the source
give 8<t=log(1000pi)<81/10. Together with the other C03 constants
and -J_delta<=log²(pi/(2delta))=(t-log2)², these imply

    -W0<4(81/10)(4-138/100)+80+104+4(7/10)²
        =33856/125.

Thus the baseline a variation is at most
169280r²/24625 using 1-a<=r²/4 and pi²>197/20. If W0 is
positive its baseline contribution is negative, which also obeys this
upper bound; no sign assumption about W0 is needed.

The reciprocal-pair series has j=0 contribution at least 16x² in
C(1/2+x)-C0. Summing the two phase offsets gives D>=8r²/pi².
With a>=15/16 and -(2k+H)>128/5, its contribution to E is at
most -192r²/pi^4<=-(48/25)r². The negative sign is essential
and has the correct direction in each comparison.

The beta-dependent finite H/G Taylor remainder from C03 is below
beta²/30000. The coefficients at zero satisfy D0(0)<1 and B0(0)<1/2;
the previously proved derivative bounds give |d_S|<1/10. Consequently
the difference between a*d_S*beta and d_S*beta is at most r²/80.
The full quadratic coefficient is therefore

    169280/24625-48/25+1/80+1/30000<5.

This verifies the coupled allocation (10). It uses the actual finite
H/G constants and their uncancelled slope; replacing either by an infinite
constant would not justify this argument.

For the limiting jump, subtracting d_J beta gives
2beta/pi³ times [(a-1)U(beta)+(U(beta)-U(0))]. The bounds
|U|<1/50, |U'|<1/15000 and beta<=1/2 give exactly
(2r²/27)(1/400+1/15000)<r²/1000. The fixed one-summand
q_R constant is retained.

The four quadratic coefficients sum to
15/8+13/12+5+1/1000=191/24+1/1000<8. The linear terms
sum to the exact C03 d_C+d_S+d_J with |d|<10^-9. This proves
the sharp noncentral bound on the whole closed triangle. No symmetry
is used to declare the finite-truncation beta slope zero.

## Limiting comparison for every integer n>=10^6

C01's directional central estimate, including its baseline r²/16,
combines with the constant eight to give the exact coefficients

    alpha²: 8+1/16+4/9=1225/144,
    beta²:  8+1/16+1/6=395/48.

Only alpha carries the fractional term (15/32)alpha^(3/2).
Replacing it by a radial term at this stage would change the allocation;
the source correctly retains its direction.

Since log n>69/5 and pi²<10, N1-16 gives
A(L)>224457/12000>187/10. On alpha>=exp(-8), the entropy
logarithm is at most eight, leaving loss
187/10-1225/144-32/9=531/80>33/5. The exact fractional
maximum is then below 1/50000. The displayed rational fraction
170859375/[268435456*35937] and its comparison with 1/50000
are correct.

For alpha<exp(-8), the remaining pure quadratic coefficient is
negative and may be dropped. Monotonicity of x²log(1/x) on this
interval bounds the gain by c exp(-12)+(32/9)exp(-16)<10^-5.
The zero-axis value is zero. Thus 1/50000 is a uniform alpha allowance.

The beta quadratic loss is greater than 10. Its exact entropy maximum
is (1/(18e))exp(-180)<10^-9. The fixed beta-slope allowance is at
most 1/(2*10^9). Summing proves the written limiting bound

    T(phase)-T(origin)-G_n<1/50000+3/(2*10^9).

This statement uses a phase-only T against the n-dependent coefficient
loss; it does not replace Q_n by a pointwise limit or assert a finite-n
error smaller than the separately established C02 bound.

## Actual near-model onset at log n>=30

Using the radial C01 version and C02's actual finite error instead gives
the written bound (8) with quadratic coefficient nine. For L>=30,
A(L)>900/11 and A-9-32>40. The fractional allocation 32r²
costs less than 2*10^-6, and the remaining entropy allocation costs
less than 10^-8. The slope allowance is at most 5*10^-10.

The elementary e>19/7 and (19/7)^10>20000 imply e^30>8*10^12.
Monotonicity of (L+1)e^-L therefore bounds the finite error by
155000000/e^30<31/1600000. The sum of these four allowances is
strictly below 1/40000. N1-18's artifact budget and N1-17's exact
origin identity then yield the actual near-model inequality at every
integer n>=ceil(exp(30)), with both parities included.

The proposed remaining uniform error 1/250000 would fit the limiting
margin at n>=10^6, since 1/50000+3/(2*10^9)+1/250000<1/40000.
It is correctly labeled OPEN. The existing C02 finite error does not
supply that estimate at n=10^6. The actual original-range comparison
and the global argmax theorem therefore remain unresolved.

## MINOR wording finding and independent closure

The original limiting-comparison Statement said "for every integer
log n>=30." The intended and proved domain is every integer n with
log n>=30. This MINOR wording finding was sent to the coordinator before
an author change. No constants, proof steps or mathematical scope needed
repair.

The author changed that phrase to "for every integer n with log n>=30"
and supplied the corrected SHA listed above. The reviewer read the
correction and ran a read-only Python string/hash check: reversing only
that phrase in memory recovers the exact original SHA
`0eca9bddfcbcf3f6fa2713846338f90f7c6849d380ab35adce57ce8f70f4a210`.
The check passed. Thus no other byte changed, and the finding is **closed**.
The main analytic acceptance carries to the corrected source. No author
file was edited by the reviewer.

No BLOCKING or MAJOR finding, and no unresolved MINOR finding. The sharp
remainder, limiting comparison and actual exp(30) near-model onset are
accepted at their distinct stated scopes. Certified degrees 2–40 remain
unchanged; formal Claude audit remains pending.
