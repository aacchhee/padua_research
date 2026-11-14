# PD-T?argmax-bridge-codex-D09-patch512 — A certified actual-corner rectangle at degree512

ID kind: PD-T. Aliases: successful three-vertex origin predicate;
degree512 inward corner patch; primary pi/4 by3pi/16 rectangle.
Split from: application of the accepted D08 three-point corner theorem.
Split into: none. No new mechanism or historical novelty claim.

## Exact statement and review status

Fix n=512,m=513 and the original corrected even-checkerboard Padua
cardinal polynomials, including the exceptional highest x mode and
their actual finite polynomial collision values. Put

    Lambda_c=lambda_512(-1,-1),
    Lambda(alpha,beta)=lambda_512(-cos(alpha/512),-cos(beta/513)),
    A=pi/4, B=3pi/16.

The completed frozen author computation and accepted mathematical
dependencies establish, for EVERY point of the CLOSED rectangle
0<=alpha<=A,0<=beta<=B,

    Lambda(alpha,beta)
       <=Lambda_c-(19/5)(alpha^2+beta^2).              (1)

Equality at the origin is preserved; every other point is strictly
below Lambda_c. Since512 is even, its node-preserving x reflection
gives the identical conclusion on the other actual nonnode-corner
patch

    lambda_512(cos(alpha/512),-cos(beta/513))
       <=Lambda_c-(19/5)(alpha^2+beta^2).              (2)

Each rectangle contains the FULL inward normalized-phase half diamond
alpha,beta>=0,alpha+beta<=1/2: A>1/2 and B>1/2 already follow from
pi>3. Here alpha,beta are radians in the NORMALIZED PHASE chart;
the physical inward angles are alpha/512,beta/513.

Status: **PROVED (developer computational application)**, with accepted
mathematics/source contract and a completed outward author receipt.
The distinct fresh-build RESULT replay/review is **PENDING**, not
reported complete by this file. The mathematical sufficient implication
and exact author premises are given below. The result is a LOCAL
corner-patch certificate only. It proves no complement cover, global
argmax at512, complete new degree certificate or statement at another
degree. Both actual corners in(1)--(2) have the even-n parity; no
odd-degree patch is inferred.

## Exact computational premises

The one-shot frozen source was published at input
`96882eaa270adbde69ce24e731256eebbbd03adb` and released by root only
after acceptance of the D08 interpolation/corner theorem, D09 global
M512=34 and the D09 controller source. The author trial completed
its primary predicate with no rectangle fallback. Independent replay
was subsequently released and was still pending at this file's freeze.

The native inward-turn API uses

    xi_pi=alpha/(pi*n), zeta_pi=beta/(pi*m),
    (x,y)=(-cos(pi*xi_pi),-cos(pi*zeta_pi)).

Thus the three exact actual-lambda inputs are

| Vertex | (alpha,beta) | (xi_pi,zeta_pi) |
| --- | --- | --- |
| x | (pi/4,0) | (1/2048,0) |
| y | (0,3pi/16) | (0,1/2736) |
| xy | (pi/4,3pi/16) | (1/2048,1/2736) |

These are exact rational multiples of pi, not rational-radian labels.
The corner is the accepted C11 common-primitive input(0,0), used through
the exact identity S_512(0,0)=Lambda_c. It does not presume corner
maximality. The corner LOWER endpoint and actual-point UPPER endpoints
are the exact dyadic rationals

    Lc=7112277937770225/281474976710656,
    Ux=3148016308623273/140737488355328,
    Uy=6644655510519255/281474976710656,
    Uxy=2916781692560455/140737488355328.             (3)

The outward enclosures establish Lc<=Lambda_c and the respective actual
point values <=Ux,Uy,Uxy. Python converts the outward binary64 values
using Fraction.from_float, preserving their exact stored dyadics; it
never interprets a printed decimal as the endpoint. No reconstructed
midpoint/radius or corner upper is an acceptance premise.

The safe lower losses are EXACTLY

    dx=Lc-Ux=816245320523679/281474976710656,
    dy=Lc-Uy=233811213625485/140737488355328,
    dxy=Lc-Uxy=1278714552649315/281474976710656.        (4)

All three are positive. No sampled interior value is used.

## Exact three-point criterion and resulting coefficient

Set u=alpha^2/2,v=beta^2/2 and

    U=pi^2/32, V=9pi^2/512,
    u'=U/pi^2=1/32, v'=V/pi^2=9/512,
    kappa=n/m=512/513, M=34, p=22/7>pi.

The exact receipt gives

    q=min(dx/u',dy/v',dxy/(u'+v'))
      =816245320523679/8796093022208,
    threshold=p^4*M*max(u',kappa^4*v')/6
             =248897/14406,
    gap=q-threshold
       =4784754461257807549/63358258038964224>0,
    epsilon_lower=gap/p^2
       =4784754461257807549/625824426344054784.       (5)

The max is u' because0<kappa<1 and v'<u'. The minimum in(5) is
the x ratio: in a common denominator the two comparison differences
are135750951302409 and53299829297065, respectively, both positive.
These integer checks, the subtraction in(4), and both identities in(5)
were checked from the saved rational metadata, without a numerical call.

Use c=q/pi^2 in the accepted D08-point-box-corner theorem. Equation(4)
gives dx>=cU,dy>=cV,dxy>=c(U+V). The strict positive gap in(5)
implies c>(M/6)max(U,kappa^4V). Moreover the theorem's actual barrier
coefficient obeys

    epsilon=c-(M/6)max(U,kappa^4V)
      =[q-(M*pi^4/6)max(u',kappa^4v')]/pi^2
      >=gap/p^2=epsilon_lower>38/5.                 (6)

The last comparison is exact: five times the numerator of epsilon_lower
minus38times its denominator equals

                    142444105214955953>0.

The accepted theorem therefore yields

    Lambda(alpha,beta)<=Lambda_c-epsilon_lower*(u+v)
      =Lambda_c-(epsilon_lower/2)(alpha^2+beta^2)
      <=Lambda_c-(19/5)(alpha^2+beta^2).

This proves(1), including the closed axes and equality at the true
symbolic origin. The accepted even-n x reflection proves(2). In
particular no rounded origin upper was substituted into interpolation.

## Normalization, finite reduction and trusted arithmetic

The n512 vertex API evaluates the ACTUAL Lebesgue function, not the
common primitive S. For inward physical angle turns xi,zeta it forms

    V_r(t_j)=sum_(sigma,tau=+/-1)
           G_n(pi*(xi+sigma*j/n),pi*(zeta+tau*r/m)),
    lambda=(1/(2nm))sum_(r=0)^m f_r
                           sum_(j+r odd) e_j*|V_r(t_j)|,

where e_j,f_r are1/2 at their respective endpoints and1 otherwise.
The four kernel copies are combined BEFORE taking the absolute value.
G_n is the original corrected finite rhombus polynomial. Its sine-ratio
polynomial continuation is used directly at all integer-pi/removable
collisions; an off-grid rational alias or zero-times-infinity convention
never supplies an actual collision value.

The independently accepted D06 cubic-over-quartic parity-grid reduction
and D07 point implementation divide rows by certified numerator/denominator
events. Acb root candidates alone are not proof: disjoint disks with
strict Rouche coverage certify the complete coefficient family, and
uncertain events move samples to direct finite evaluation. An unresolved
degree/root/sign/pole test causes a safe WHOLE-ROW finite fallback.
The complete returned C11 cotangent partial balls are multiplied by their
full coefficient balls: CP640/J16 smooth, K32/L16 harmonic and WD96
derivative tails are retained, with Arb160 ball arithmetic. No radius,
tail, failed attempt or exceptional mode is discarded. Any nonfinite
direct result propagates failure. The n32 API control uses the unchanged
independent512-bit finite reference and passed full reference containment;
it is a control, not a patch claim at32 or a full reference run at512.

Both native exporters use arb_get_lbound_arf/arb_get_ubound_arf followed
by ARF_RND_FLOOR/ARF_RND_CEIL binary64 conversion. Python rejects
nonfinite/reversed endpoints and treats each finite binary64 endpoint
as its exact rational value. The point radii and hex encodings are saved
but are not replacements for these certified bounds. The numerical
trusted base is the accepted finite reduction/tail proofs, FLINT/Arb
outward ball and Acb root-coverage operations with MPFR/GMP, the
compiler/runtime closure, outward endpoint export and exact Python
integer/Fraction arithmetic. Source/loaded-library identities are
preserved in the fresh build/runtime manifests; no floating agreement
with a sampled maximum is a premise.

## Scope and counts of the completed author run

There were five complete native API calls: one n32 point/reference
control, one n512 C11 corner, and the three n512 primary vertices.
No pending call or unexecuted primary point remained. The smaller
rectangle fallback was NOT used. This is distinct from the ONE safe
numerical ROOT/WHOLE-ROW fallback at the xy vertex.

The n512 point counter order is
rows,eta-degenerate,numerical-fallback,root-failure,sign-failure,
direct,blocks,partials,verified-root-disks,axis-reduced,node-shortcut,
corner-shortcut,max-direct-buffer. All work, including discarded attempts,
is counted. The exact recorded vectors are

    x:  (514,2,0,0,0,3213,1014,8112,512,512,0,0,11),
    y:  (514,0,0,0,0,2661,1015,8120,514,514,0,0,9),
    xy: (514,0,1,1,0,3074,1016,8128,1539,0,0,0,11).

Thus both axes have zero numerical fallback; their eta/axis reductions
are separate counters. The xy row failure is enclosed by actual finite
evaluation and is not called a successful root certificate. The C11
corner vector in its original order retained,direct,blocks,maxdirect,
maxblocks,ordinary is(2048,511,2042,1,2,1022).

The worker-summary CPU subset is10.337808s. The later complete waited-
descendant plus supervisor sample in final-accounting.json is11.265079s;
root's earlier supervisor sample was11.264637s. These are differently
timed metadata samples, not mathematical premises or a general runtime
bound. No numerical/native job was run by the author of THIS theorem.

## Frozen dependencies, evidence and pending review

Accepted mathematical inputs:

- D08-point-box.md and D08-point-box-corner.md, supplementary review
  independent-checks-D09-point-box.md, SHA256
  `486f58f8a7d460134922c26c02889e1eca69f482359ed66d7618b34d8b43535a`;
- D09-global-norm.md, global norm34 independently accepted in
  independent-checks-D09-global-norm.md, SHA256
  `6e721695a76c0a8b622ec4a04420a87b761ebec8d063ed45256333170bf4accc`;
- accepted D06 structural/D07 actual-point and C11 complete-tail
  contracts, pinned by the source manifest below.

The pre-execution source review is
independent-checks-D09-threepoint-source.md, SHA256
`b8d85fc23a4c6001af2fc8c838b29aa90a7ed8b9520372c530ef876b701fbd1b`.
It accepted the frozen technical protocol, not the numerical instance.
The source hashes are

    D09 controller.py:
      5642ad6fdf2c28165fc8d17ce8e62330ed695e7b64bb1242c13312d53d47fd73
    D09 SOURCES.json:
      f7d2bd992d93ec631000e98a657e119ade3d24f843e4280cb1d27f0a0069794a
    D09 FREEZE.md (machine JSON):
      6cd130544e02b9734bba710de27d9cba62bfe49a67e0fffbb031782234685d60
    D07 point.cpp:
      03dc79bbbc7563ba9066137c0a52467624c810a758f865f9931511c82985ff6f
    D07 controls.cpp:
      5db13088e9fff85a134c95851337750ca03ea62be2f5d3ecf07e1f6e7d49c3fa
    C11 point.cpp:
      6e2f1920ca293ac5a34f01c6369d94345b0d0c9b8a03d3e58ef15d453fbcf1d9
    C11 partial.cpp:
      bde1ce4850849dd402acc91eb3cee7d40883bbd51d5f7cff13334abc0f4ee23c

Preparation-era 'prospective/pending norm' strings inside the immutable
machine provenance are historical: the norm/theorem reviews above and
root's published release preceded this run. Prose provenance is passive;
the code/data source identities are the enforced execution pins.

The observed author evidence lives in
local-output/argmax-bridge-20261105/post-audit-D09/threepoint/:

    checkpoint.json SHA256
      0fce06f43badb32db45bc514aa1b1791c4112cb31dc7e97140e70c82715fd48e
    worker-summary.json SHA256
      f17915fe1b713374f809739bd6f9f37831231af4a1105393f2b3bfa0f079a802

The compact essential record evidence/d09-threepoint.json is being
prepared by its separate owner, and the distinct fresh-build result
review independent-checks-D09-threepoint-result.md is PENDING. This
file does not invent their final hashes or claim that replay completed.
The full raw path is an observed local input, not a promise of permanent
external archival delivery. Root retains evidence/index publication.

## Limits and history

The accepted gate is a D09 APPLICATION, not a new idea. Only this
one theory file is owned/edited here; no author attempt, source, shared
registry or Git state was changed. Metadata reads and exact integer
cross-multiplications supplied(3)--(6), with no fresh native/board/root
job. The author instance is completed; supplementary result acceptance
remains pending. This proves neither a complement exclusion at512 nor
global512 argmax nor a new complete degree certificate. No interpolation
of the nonsmooth primitive S in squared coordinates is used.

2026-11-06, parent-requested Codex Sol xhigh metadata application,
input`96882eaa270adbde69ce24e731256eebbbd03adb`, bounded10min.


### Supplementary result/application closure — 2026-11-06

Distinct fresh-build replay and exact local-theorem application ACCEPTED,
with no unresolved findings: [independent-checks-D09-threepoint-result.md](../independent-checks-D09-threepoint-result.md),
report SHA256a54927a81158f8f1094057c0fc1f21b2e39bd922f8c0784567d3cabada2e85ca.
The complete author receipt34553e6d... and independent receipt54b4ce6e...
are committed separately. Their five native intervals/counters and exact
loss arithmetic agree. The earlier pending replay wording is historical;
the preceding audited proof text is unchanged. Final Claude audit remains
pending. Full complement/global degree512 coverage remains OPEN.
