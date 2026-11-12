# Own recomputation of the written binary64 error budget (certificate-reduction.md) incl. eta slack.
from fractions import Fraction as F
import math
u=F(1,2**53); eta=F(1,2**1074); S=2**24; ok=True
# local recurrence op error <= 8u(1+E) for all E>=0: linear in (1+E); check coefficient and constant
ok&= (5*u+2*u*u) + (1+u/2)*eta <= 8*u          # at E=0 (worst case for the eta term)
ok&= 5*u+2*u*u <= 8*u
e=[F(0),F(0)]
for k in range(1,16): e.append(2*e[k]+e[k-1]+8*u*(1+max(e[k],e[k-1])))
ok&= all(e[k]<=8*u*(4**(k-1)-1)/3 for k in range(1,17)) and all(e[k]<F(1,2) for k in range(17)) and all(e[k]<=e[k+1] for k in range(16))
g2=2*u/(1-2*u)
for n in range(4,17):
    E=max(e[n-1],e[n])
    true_needed=((1+E)**3-1) + (2*u+u*u)*(1+E)**3 + eta*((1+E)*(1+u)+1)/2 + F(1,2*S)   # rigorous total per derivation
    implemented=3*E*(1+E)**2+g2*(1+E)**3+F(1,2*S)
    beta=F(math.ceil(implemented*2**40),2**40)
    ok&= true_needed<=implemented<=beta and implemented+2*eta<=beta and E>=8*u
    print(n,float(E),float(beta),float(beta-true_needed))
print('BETA_OK' if ok else 'FAIL')
