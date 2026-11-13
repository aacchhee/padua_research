"""Audit-03 arithmetic cross-checks of stated formulas (exact integers)."""
from math import comb
from fractions import Fraction
import itertools
N=lambda n: comb(n+3,3)
A=lambda m: m//2+1; B=lambda m: (m+1)//2
F=lambda n: A(n)*A(n+1)**2+B(n)*B(n+1)**2
census=[5,12,26,45,75,112,164,225,305,396,510,637,791,960,1160,1377]
print('parity counts match census n1..16:', [F(n) for n in range(1,17)]==census)
print('max ratio F/N n1..16:', max(Fraction(F(n),N(n)) for n in range(1,17)), 'any >1.5:', any(Fraction(F(n),N(n))>Fraction(3,2) for n in range(1,17)))
print('F(n)>N(n) all n1..109:', all(F(n)>N(n) for n in range(1,110)), 'F(109)=',F(109))
f=lambda n: n**3-108*n**2-198*n-108
print('f(109),f(110)=',f(109),f(110),' first n with 19n^3/108>N:', next(n for n in range(1,400) if Fraction(19*n**3,108)>N(n)))
ok=all(sum((a+1)**2*(b+1)**2*(c+1)**2 for a in range(n+1) for b in range(n+1-a) for c in range(n+1-a-b))==sum(comb(3,j)*comb(n-j+9,9) for j in range(0,min(3,n)+1)) for n in range(0,17))
print('R-Leja sum identity n0..16:', ok, ' <=8C(n+9,9):', all(sum(comb(3,j)*comb(n-j+9,9) for j in range(0,min(3,n)+1))<=8*comb(n+9,9) for n in range(0,60)))
def D(r,n):
    # trace of coordinate sign flip on r axes on monomials of total degree <= n
    return sum((-1)**(sum(e[:r])) for e in itertools.product(range(n+1),repeat=3) if sum(e)<=n)
perm=[n for n in range(1,21) if (N(n)%2==1) or any(D(r,n)==0 for r in (1,2,3))]
print('parity-permitted n<=20:', perm, ' == n!=2 mod 4:', perm==[n for n in range(1,21) if n%4!=2])
Bc=[[2,-1,-3],[3,-2,1],[1,3,-2]]
det=(Bc[0][0]*(Bc[1][1]*Bc[2][2]-Bc[1][2]*Bc[2][1])-Bc[0][1]*(Bc[1][0]*Bc[2][2]-Bc[1][2]*Bc[2][0])+Bc[0][2]*(Bc[1][0]*Bc[2][1]-Bc[1][1]*Bc[2][0]))
print('det Bcrit=',Fraction(det,27),' density=',Fraction(4,3)/abs(Fraction(det,27)))
print('38n^3/27 integer & equals seed det at n=3,6,9,12,15:', [ (n, Fraction(38*n**3,27)) for n in (3,6,9,12,15)])
