# H02 — signed endpoint correction attempt

Rules/input: 2c69ba538473b8fdd9147635256289f74e75ccbb.
Date: 2026-11-07. Requested/API Codex Sol ultra; actual serving metadata
unexposed. Ownership: this attempt and H02 idea/theory only. PAPER ONLY;
zero executable/scalar/numerical/native/quadrature jobs.

Root released mathematical development after the full preparatory gate.
Read ../campaign-H-gate.md and its F03/IDEA-329 immediate predecessors.
The prospective exact target, separation and first kill test were written
in ../ideas/H02-endpoint.md BEFORE mathematical derivation.

## Target and inherited normalization

For m=n+1 and a=2/pi, prove

    Delta_n=kappa+(A_n^2+a*A_n-2)/m+O(log n/n^2),
    A_n=a(log n+gamma+log(8/pi)).

PD-T159/269 give exactly Lambda_c=n*L_n^2/m+Delta_n+1/m.
PD-T270 gives L_n=A_n+O(n^-2). All endpoint weights and both parities
must remain explicit. Denominator m may not be replaced by n at the
target scale. The original full target remains OPEN.

## Development

### First test: upper adjacent endpoint — passed analytically

Set r=n-j, q=1/n, t=r/n, c=pi/2 and w=c*t. For k=j+1,

    A=f(actual)=sin^2(w/(1+q)) /
      [sin((2+q)*w/(1+q))*sin(q*w/(1+q))],
    B=f(reference)=sin^2(c*(t-q)) /
      [sin(c*(2*t-q))*sin(c*q)].

The actual tiny-gap term has the exact regular form

    q*A=sinc^2(w/(1+q)) /
      [(2+q)*sinc((2+q)*w/(1+q))*sinc(q*w/(1+q))].

It is smooth even at t=0 on 0<=t,q<=1/2. The reference leaves a
retained O(q^2/t) Taylor remainder, not an unjustified uniform O(q^2).
With g(t)=tan(pi*t/2)/(pi*t), g(0)=1/2, exact coefficient
cancellation gives

    q*(A-B)=(1-t)*g(t)+q*g(t)+O(q^2/t), q<=t<=1/2.

After the exact 1/(1+q) normalization, this sums to O(log n/n^2).
The complete written proof is ../theory/H02-endpoint.md. It includes
the artificial-halfway-cut parity term and the actual full eta_n=1.
This is a substantive proved supporting slice; the full target is OPEN.

### Lower endpoint test: fixed-index layer and exact rational extraction

The other endpoint is also nonuniform. For fixed distinct j,k>=0,
j+k odd, direct quadratic sine subtraction proves

    (f(actual)-f(reference))/n
      ->8*sign(k-j)*k^2/[pi^2*(k^2-j^2)^2].

For fixed odd l, the positive and negative orientation profiles have
tails respectively

    +2/(pi^2*l^2)+2/(pi^2*l*j)+O_l(j^-2),
    -2/(pi^2*l^2)+2/(pi^2*l*j)+O_l(j^-2).

The two constants match the bulk limit at zero, but their same-sign
1/j tails survive pairing. This diagnoses the required logarithmic
boundary correction; it does not justify summing a fixed-l expansion
over all l. The fixed-index claim is also proved in the theory record.

For a possible continuation, an exact lower-strip extraction was
obtained. Let l>=1 be odd, t=j/n<=1/2, j+l<=n, q=1/n, c=pi/2,
y0=t+l*q, y1=y0/(1+q), and

    R(t,y)=cos^2(c*y) /
          [sinc(c*(t+y))*sinc(c*(y-t))].

The exact identity f(pi*t,pi*y)=R(t,y)/[c^2*abs(y^2-t^2)]
holds away from the excluded diagonal. R is smooth throughout the
lower strip 0<=t<=1/2,0<=y<=1. Setting R=1 in the exact q-scaled
deformation isolates the rational expression

    J_l(t,q)=1/(2*c^2*l)*[
       (1+q)/(l-t)+(1+q)/(t+l*q/(2+q))-1/(t+l*q/2)].    (J)

This is exact algebra, not a quadratic approximation: the remaining
residual is exactly

    K_l=(1+q)^2*[R(t,y1)-1] /
           [c^2*(l-t)*((2+q)*t+l*q)]
        -[R(t,y0)-1]/[c^2*l*(2*t+l*q)].

Thus q*(f(actual)-f(reference))=J_l+K_l. Formula (J) exposes shifted
harmonic triangles directly. It was sent to H01/H04 for comparison
with their independently assigned harmonic/smooth-residual lanes.
No one-index collapse is inferred by renaming K_l.

For l=1 only, the tentative smooth residual coefficients are

    K0=(c*t*cot(c*t)-1)/[2*c^2*(1-t)],
    K1=(cot(c*t)-1/(c*t))/[2*c*(1-t)].

An O(q^2/t) estimate can be sought on q<=t<=1/2, with j=0 treated
directly. These tentative coefficient/subtraction observations have
NOT been promoted to another proved theorem here; the complete
uniform ALL-l summed estimate was not obtained in this round.

### Exact remaining crux and disposition

The upper l=1 tiny-gap screen passed. The second preregistered test,
uniformity after summing ALL odd offsets and lower endpoint indices,
is unresolved. In particular one still needs control of K_l uniformly
when l grows with n, the negative-orientation analogue, the complementary
upper region for l>=3, all missing-pair boundaries and remaining half
weights, with the exact signed first correction retained. The explicit
normalization charge -(L_n^2-1)/(n+1) has never been dropped.

H02's full candidate is therefore DEFERRED, not rejected. The target
remains OPEN, and only the precisely scoped upper-slice/fixed-index
theorem is offered for independent review. No full formal coefficient,
fitted evidence, improved all-n origin bound or global theorem is claimed.

## Runs needed

None authorized. No computation is necessary for a paper proof.
