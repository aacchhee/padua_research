# Supplementary independent checks 02 — substantive follow-up

2026-11-05. Requested allocation: gpt-6-astra high; serving model identity and
effective effort are not independently exposed. Rules/source
`823cf6a4ef7c01b4ef3d2a6fec3e9f19d4b4f6f1`, original main/base
`b4d292eea5eed373002506d5e16a3761bd7ae10e`; follow-up after published round1
checkpoints f75964bd and 929ef787. This checks newly supplied analytic growth,
finite normality and projection work. It does not replace the mandatory
Claude audit, approve developer fixes, or revise the frozen round1 report.
Prior complete-read scope and novelty limits remain those of
[the gate](novelty-gate-independent.md). No new external-primary comparison
or priority clearance is claimed. No developer files were edited.

## Analytic Krawtchouk lower bound

Read the complete frozen `theory/conditioning-lower-krawtchouk.md`, SHA-256
`409f625a57d6c0e004781f666ef35f71fbcd25b447f0cc5c938da74d77340b0f`.
No substantive proof error found. The Chebyshev/Rolle argument and positive
Cauchy–Binet sum supply all-N normality independently of the explicit C4
formulas. The scalar generating identity supplies the axes; the displayed
NN candidate satisfies the layer identities and gives field scale 1/5.

I independently checked the terminal finite-difference normalization
H(-1)=(-1)^M M!, including the subtraction of the degree-(M+1) support
polynomial in deriving B=-H'(-1)/H(-1). The perturbed second-weight jets are
those of dot H+H(-z), with no omitted alternating derivative factor when
written using zD_z. Monicity fixes dot H(-1)=0. Solving the remaining Taylor
jet with that constraint gives the stated S'(-1) and signed prefactor.
The formal coefficient substitution in (12) holds also for m=1; n=0 gives
zero for positive coefficient orders as it should. The positive binomial
expansion, central-binomial average bound and 9^N corollary have the stated
constants. The parity direction preserves mass exactly and has mixed input
norm one. Thus the analytic lower bounds apply also on the fixed-mass
subspace; they are not conclusions extrapolated from finite tables.

Separate exact sanity: `independent_check_followup_parity.py` uses the
independent defining-moment Jacobian from check01, with Fraction arithmetic
and no developer AD/C4 call. At N=2,3,4,6,8 it checks every terminal site in
formula (4), both b derivatives, exact field scale, zero mass, the weaker
axis witness and the stronger bound by squaring and comparing rationals.
All assertions passed. Normalized weaker/balanced witnesses are respectively
(5,5), (25/2,25/2), (125/3,40), (625,1776), and (78125/7,726120/7).
The balanced choice is the proof's convenient choice, not necessarily the
largest terminal derivative. These finite exact checks corroborate the
analytic proof; they are not its all-N premise. No matching upper rate,
uniform finite-perturbation radius or algorithmic stability follows.

**Dated final-addendum recheck.** The developer subsequently appended the
summed-terminal-coefficient proof, final file SHA-256
`9047c95c8bc8b6ca6ecb0dae5eab6ff1517be428bee501c9f16ee2bff164c53e`.
I read that addendum and reconstructed its formal generating function,
recurrence, root formula and max-at-least-average inequality. No flaw found:
it proves the stronger liminf lower rate 5+2sqrt(6), without a matching
upper bound. The final independent checker now also verifies the exact
sum identity for L=0,...,30 using the integer recurrence B_L=10B_(L-1)
-B_(L-2), B_0=2,B_1=10, and the bound at its five direct-moment sizes.
All passed. Earlier script/hash/receipt remain identified below; the final
run has its own source and output hashes, not a retroactive substitution.

## Fixed-N proximity obstruction

Read complete frozen `theory/conditioning-lower-proximity.md`, SHA-256
`c8939f19ad9f3504375d67b58db5171f1ee545a459d8816145048680dd62e4ca`.
No substantive gap found. The normalized alternating direction has zero
mass and relative sup norm one for 2/5<q<=1/2. Its signed moment vanishes
below degree M and equals (-q)^M M! at the monic degree-M polynomial.
Differentiating the two-polynomial representation gives the displayed
derivative; the affine vertex values of b2 give field scale exactly 1/5.
Interior d_min excludes the identically zero terminal differences. Thus
the product lower bound diverges at fixed N>=4, refuting the stated
single-inverse-d_min upper-growth claim in this metric and family.

An independent Fraction direct-moment check passed N4 with delta=1/10,
1/20,1/40 and N6 with delta=1/20, including all moment cancellations,
normality solves, mass/scale and exact derivative factors. The respective
normalized directional witnesses are 125/3,243/2,4913/12,59049/10; their
products with d_min are 25/9,81/20,4913/720,59049/500. The all-delta
conclusion rests on the written proof, not these four finite observations.

## Finite Hahn normality certificate

Read the complete frozen proof `theory/conditioning-normality-certificate.md`
and exact checker. No circularity found: normality through k-1 makes true
coefficients available only through k-2; nonzero d at that last layer gives
the opposite degree-k corner by the bordered Schur complement. The argument
uses h_(eta,2) nonzero because eta+e2 is already normal. No degree-k
normality or terminal divisor is used prematurely. Positivity proves the
axes through N. The certificate is sufficient, with no converse claimed.

I separately ran the frozen Fraction graph for every integer N=4,...,64,
Hahn family. All 61 passed; N64 checks 2016 interior sites through degree62,
minimum |d|=524/10614807. The N64 exact coefficient payload SHA-256 is
`03acf79d9ac7eb9dce5fb95f4608f75d82440941b867923898799f001eb34eb2`.
A separate Python JSON comparison with the developer receipt
`/tmp/conditioning-exact-hahn-full.json` removed only `elapsed_seconds`
from each case and asserted equality of all 61 complete case payloads;
it passed, covering 43,676 interior d checks.
The previous independent exact direct-moment/AD comparison at N3/4/6 checks
the graph's interpretation separately. This is finite exact computational
evidence for the stated 61 inputs plus the written general implication,
not an all-N Hahn-family normality theorem.

## Full-data numerical projection follow-up

Read frozen `backward_projection.py` completely. The residual sign, softmax
chart chain rule, fixed SPD field scales and real Householder reflector
with sign(0)=+1 are consistent. The 3N-2 chart removes both mass gauges;
ordered nodes remain shared by both positive normalized measures. The code
correctly calls its fit a numerical stationary candidate, not a certified
nearest minimizer. The separate written local geometry theorem does not
by itself certify this optimization's convergence neighborhood or output.

I independently executed the N4 fits at 160 digits for LU/nodeqr and both
families. All four returned rational inputs exactly equal the developer's
frozen receipts. For each, independent Fraction defining moments solved
all 14 systems through degree4, reconstructed all 40 coefficient entries
and their Jacobian, checked order/positivity/unit masses, and formed the
full SPD objective and chart gradient exactly. Input, field correction and
SPD norm agree with reported floats within the checker's 1e-12 relative
tolerance. A separate known-solution least-squares test with a structural
zero row checked the custom QR routine at 160 digits, tolerance 1e-140.

| N4 method | Family | Input distance/u | Full coefficient correction/u |
|---|---|---:|---:|
| LU | Krawtchouk | 0.984546554 | 1.930382038 |
| nodeqr | Krawtchouk | 6.848631739 | 29.885159922 |
| LU | Hahn | 1.578826130 | 3.061702016 |
| nodeqr | Hahn | 4.859904472 | 9.686572319 |

Here u=2^-53. These are feasible data-plus-coefficient-correction witnesses;
the exact dyadic raw-array incompatibility from check01 still applies.
No strict raw backward error or nearest-point certificate is inferred.
This follow-up independently reran four N4 fits only; the developer's
remaining C4 and N8 projection cases were not separately replayed here.

**Rounding distinction communicated to developer.** At each returned
70-digit rational witness, the squared normalized stationarity residual
||J^T r||²/(||J||_F²||r||²) is exactly less than 10^-100, checked as a
Fraction inequality. Its displayed square roots are approximately
8.34e-54,7.29e-55,9.39e-53,3.40e-53 in table order. Thus the developer's
stricter 1e-55 optimizer stopping flag concerns the pre-rounding iterate;
it must not be transferred unchanged to the returned rational witness.
Neither iterate is proved exactly stationary. This qualification does not
alter the exact feasible-input check or the measured correction values.

## Commands, frozen identities and receipts

Working directory `/workspace/scratch/nn-mop-stability-20261105`.
Python3.12.14, standard-library Fraction, Linux6.18.57-x86_64/glibc2.41.
The imported generic graph environment is unchanged from check01:
mpmath1.3.0, NumPy2.3.5, SciPy1.17.0. Certificate arithmetic uses no floats;
elapsed timings are diagnostic floats. These commands actually exited 0:

```sh
python topics/nn-mop-stability-20261105/code/independent_check_followup_parity.py > /tmp/nn-mop-independent-parity.json
python topics/nn-mop-stability-20261105/code/conditioning_exact_normality.py --family hahn --sizes {4..64} > /tmp/nn-mop-independent-hahn-normality.json 2> /tmp/nn-mop-independent-hahn-normality.stderr
python topics/nn-mop-stability-20261105/code/independent_check_followup_parity.py > /tmp/nn-mop-independent-parity-final.json
python topics/nn-mop-stability-20261105/code/independent_check_followup_proximity.py > /tmp/nn-mop-independent-proximity.json
python topics/nn-mop-stability-20261105/code/independent_check_followup_projection.py > /tmp/nn-mop-independent-projection.json
```

The parity script first ran under the name `independent_check_parity.py`,
then was renamed to match round2 ownership and rerun; the retained receipt
uses the final name. Its source identities are checked before and after.
Hahn source hashes were checked against the freeze message after execution;
the output itself records checker and graph hashes. No source changes were
reported during that run. Raw outputs remain in /tmp, not Git/cold storage.
The projection checker initially exited 1 while hashing a very large exact
rational objective as decimal text, hitting Python's 4300-digit conversion
limit. I changed only my hash serialization to hexadecimal numerator and
denominator, then reran all four fits successfully. The retained output
records hashes of those exact objective strings without dumping them.

| Source | SHA-256 |
|---|---|
| independent_check_followup_parity.py, first run | `158e3f8861b0f00296a5b45a03511189b4d3c46de538541ccde053ecd9b00025` |
| independent_check_followup_parity.py, final | `ba31d832f875ca52a11bb8866ae8027da367ab87946d2e2cb3d0650645c060a4` |
| independent_check_followup_proximity.py | `b2d860fe2e76891cfb5fb6174b4f988f3bda875e0df90b35b896e2689f029fd8` |
| independent_check_followup_projection.py, initial | `5d67888628acbb39b2eda7df27a10fbd22a03616fe3138f6a22d421a73df648e` |
| backward_projection.py, initial | `aa11495923263601ea26760db012e1ff7f55dab202fa2e05378f6c52fa175e72` |
| independent_check_moments.py | `58d6da632647e309e6299f9f67890237536172694864f18f15b721f5e7ffe0d9` |
| conditioning_exact_normality.py | `7aa4115143a51bd3abcea50abd4ea7b8de9a7507bea711ca7e19ab662a2be24a` |
| conditioning-normality-certificate.md | `e2e48c81865cf998845b69cc318edc66fcde26c65689cd564e060fee78ac44ce` |
| conditioning.py | `11c4b49be8541697e74d383b908db47b42480e11c60f92c35821340eacea929c` |
| predecessor c4_float_baseline.py | `9ce76ae88fb798f73127f75819bcdfb6c7bffb0d9cd092d70957164cb9b6a2e8` |

| /tmp/nn-mop-independent- output | Bytes | SHA-256 |
|---|---:|---|
| parity.json | 3604 | `e6bcb579c176415565fc505c0d3c8fbeaf8b12622e567aa90f7a0d20f46013fe` |
| hahn-normality.json | 24906 | `aa880df02ce17f664aad81412a78d2c8e7f743534774973ed3c5996b39cf8d69` |
| parity-final.json | 7456 | `3308cd745d9790d3d7200adbc5acaf06ab8d830308b3634cf4cbc2d57d0fd806` |
| proximity.json | 1537 | `755a0d36d3d65c088c2297e411d443fab96a9a10bf4dd8a27266a25bd158e9f6` |
| projection.json | 4162 | `0a36cc22bab89fd3a3a2dab9d440fdecbec22878b34d82511c18e4f08e2668b8` |

Projection source dependencies `native_mixed.py`, `backward_joint.py`,
`conditioning.py` and the predecessor baseline retain their check01 hashes;
the new receipt records every full hash, checked before and after execution.
The initially compared developer receipts were
`/tmp/backward-projection-krawtchouk-r2-160.json` SHA-256
`e382823d47bc7b24366bf4c57515189b63503379d95beadda75145c39766a45f`
and `/tmp/backward-projection-hahn-r2-160.json` SHA-256
`f2c704a113aa83ddc93cfd641b340d5f9d928bbc3709de6fef788090409ef22f`.

This supplementary follow-up is complete for the explicitly stated scopes.
Mandatory Claude audit and any coordinator gate/merge decision remain
separate; no claim about unseen subsequent revisions is made.

## Dated final projection reporting recheck — 2026-11-05

The developer addressed the stage distinction explicitly: optimizer fields
now name the unrounded iterate and its stop reason, while a separate
`returned_witness_scaled_stationarity` evaluates the rational witness at
180 digits. I inspected the extracted chart Jacobian and revised reporting,
then reran all four N4 fits and exact moment checks with an added comparison
of that new field against the independent exact rational stationarity.
The comparison passed at 1e-12 relative tolerance. A Python JSON comparison
confirmed that all four complete independent case payloads are unchanged
except the added `returned_stationarity_checked` flag. The returned rational
input identities and every input/correction/objective value are unchanged.
This closes the reporting issue without certifying a nearest minimizer.

Executed exit-0 command, same environment/versions and scope as above:

```sh
python topics/nn-mop-stability-20261105/code/independent_check_followup_projection.py > /tmp/nn-mop-independent-projection-final.json
```

Final SHA-256 identities:

| Item | SHA-256 |
|---|---|
| backward_projection.py, 9825 bytes | `9deb74ef75b1972b8ece6d995aaac441cce03ba125e93c62691c0d8d6634bc57` |
| independent_check_followup_projection.py | `3d2ae221d2d641f3f6fcf94cd25362589235bb89e00ecdebd7c89ae53deebc9c` |
| /tmp/nn-mop-independent-projection-final.json, 4342 bytes | `048f5291518071d60f89632f937e4cb3375b961176c0e4b803b7e48f421c12bb` |
| final developer Krawtchouk r2-160 JSON | `2dcace699983fa41ed7ac2f806b245f8fff2e77c0efa5602dd3546104264bd3c` |
| final developer Hahn r2-160 JSON | `9edc3937ceeecb0c13f2989eb69480298636b2dd5785183bf3ae4d30258d9b30` |

The two developer output paths are the same as above and now hold these
final revisions; their prior hashes identify the earlier comparison rather
than current path contents. My initial projection.json and final
projection-final.json are both retained separately in /tmp. Dependency
hashes were checked before and after the final run and remain unchanged.
