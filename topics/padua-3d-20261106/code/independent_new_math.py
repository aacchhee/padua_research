#!/usr/bin/env python3
"""Independent T7/T9 checks; no producer imports and no prose pins."""
import argparse
import hashlib
import itertools as it
import json
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path
import sympy as s


def require(ok, msg):
    if not ok:
        raise RuntimeError(msg)


def indices(d, n):
    return [a for a in it.product(range(n + 1), repeat=d) if sum(a) <= n]


def cheb(a, x):
    if a == 0:
        return s.Integer(1)
    p, q = s.Integer(1), x
    for _ in range(1, a):
        p, q = q, s.expand(2*x*q-p)
    return q


def qdegree(u):
    a = [abs(t) for t in u if t]
    return 0 if not a else max(a) if len(a) < 3 else max(2*max(a), sum(a))


def h4_check():
    h = {(i, j, (i+j)%4) for i in range(4) for j in range(4)}
    c = (1, 0, -1, 0)
    mult = Counter(tuple(c[t] for t in p) for p in h)
    x = sorted(mult)
    v = s.Matrix([[s.prod(s.Integer(t)**a for t,a in zip(p, alpha))
                   for alpha in indices(3,2)] for p in x])
    require(len(x) == 10 and abs(v.det()) == 256, 'H4 count/determinant')
    reflection = [set(tuple((-t)%4 if j==k else t for j,t in enumerate(p)) for p in h) == h for k in range(3)]
    require(reflection == [False]*3, 'H4 reflections')
    cubic = lambda p: sum(t*t for t in p)-2*s.prod(p)-1
    require(all(cubic(p)==0 for p in x), 'H4 cubic')
    rows = []
    moment = []
    mismatch = []
    for alpha in indices(3,3):
        row = [s.prod(cheb(a,s.Integer(t)) for a,t in zip(alpha,p)) for p in x]
        target = int(not any(alpha))
        rows.append(row); moment.append(target)
        val = sum(Q(mult[p],16)*int(y) for p,y in zip(x,row))
        if val != target:
            mismatch.append([list(alpha), str(val)])
    m = s.Matrix(rows)
    require(m.rank()==10 and m.row_join(s.Matrix(moment)).rank()==11, 'H4 no weights degree3')
    require(mismatch == [[[1,1,1], '1/4']], 'H4 moments')
    return dict(torus_count=16,node_count=10,abs_monomial_determinant=256,
                coordinate_reflections=reflection,haar_degree3_nonzero_moments=mismatch,
                moment_matrix_rank=10,augmented_rank=11,
                weights_histogram={str(k):v for k,v in sorted(Counter(str(Q(t,16)) for t in mult.values()).items())})


def phase_check():
    ranks = []
    for a in [(s.Rational(1,12),s.Rational(1,12)),(s.Rational(1,12),s.Rational(1,4))]:
        x = [tuple(s.simplify(s.cos(2*s.pi*(z+s.Rational(k,3)))) for z in a) for k in range(3)]
        v = s.Matrix([[1,*p] for p in x])
        ranks.append(v.rank())
        require(len(set(x))==3, 'phase count')
        require(all(6*t != int(6*t) for t in a), 'generic collision stratum')
    require(ranks == [2,3], 'phase rank variation')
    # Shifted two-point cyclic orbit, cos(pi/4), cos(5pi/4): exact degree3.
    nodes = [s.sqrt(2)/2, -s.sqrt(2)/2]
    mom = [s.simplify(sum(cheb(j,t) for t in nodes)/2) for j in range(4)]
    require(mom == [1,0,0,0], 'phase cancellation degree3')
    return dict(diagonal_C3_generic_fold_ranks=ranks,shifted_C2_moments=[str(t) for t in mom],
                shifted_C2_shortest_dual_l1=2)


def rank2_check():
    dual = lambda u: (u[0]+2*u[2])%5==0 and (u[1]+2*u[2])%5==0
    short = [u for u in it.product(range(-3,4), repeat=3) if any(u) and qdegree(u)<=3 and dual(u)]
    require(not short and dual((1,1,2)) and qdegree((1,1,2))==4, 'rank2 short relation')
    return dict(group='C5 x C5, (i,j,2i+2j)/5',order=25,no_q_le_3=True,witness_q4=[1,1,2])


def modular_rank(a,p):
    a = [list(row) for row in a]
    row = 0
    for col in range(len(a[0])):
        piv = next((k for k in range(row,len(a)) if a[k][col]%p),None)
        if piv is None: continue
        a[row],a[piv] = a[piv],a[row]
        inv = pow(a[row][col],-1,p)
        a[row] = [v*inv%p for v in a[row]]
        for k in range(row+1,len(a)):
            z=a[k][col]%p
            a[k]=[(v-z*w)%p for v,w in zip(a[k],a[row])]
        row+=1
        if row==len(a): break
    return row


def rank2_cubic_survivor():
    gens=[(7,7,4),(5,0,5)]
    h=sorted({tuple((i*gens[0][j]+k*gens[1][j])%10 for j in range(3))
              for i in range(10) for k in range(2)})
    order=1010; prime=5051; root=32
    require(s.isprime(prime), 'survivor reduction prime')
    require(pow(root,order,prime)==1 and
            all(pow(root,order//q,prime)!=1 for q in (2,5,101)),
            'survivor primitive order1010')
    require(s.isprime(607) and pow(122,101,607)==1 and 122!=1,
            'producer primitive order101 root')
    phase=(1,2,4)
    angles=[tuple((10*phase[j]+101*x[j])%order for j in range(3)) for x in h]
    folds={tuple(min(v,order-v) for v in x) for x in angles}
    matrix=[]
    for theta in angles:
        row=[]
        for alpha in indices(3,3):
            val=1
            for a,t in zip(alpha,theta):
                val=val*(pow(root,a*t%order,prime)+pow(root,-a*t%order,prime))*pow(2,-1,prime)%prime
            row.append(val)
        matrix.append(row)
    rank=modular_rank(matrix,prime)
    cosine=lambda exponent:(pow(root,exponent%order,prime)+pow(root,-exponent%order,prime))*pow(2,-1,prime)%prime
    c=cosine(-20)  # delta=-4*pi/101, in turn denominator1010.
    for theta in angles:
        u,v=cosine(2*theta[0]),cosine(2*theta[1])
        require((u*u+v*v-2*c*u*v-(1-c*c))%prime==0,'quartic nodal identity')
    require(c*c%prime!=0,'quartic nonzero integral specialization')
    require(len(h)==20 and len(folds)==20 and rank==20,'cubic survivor actual nodes')
    return dict(group_generators_tenths=gens,phase_101ths=phase,group_order=20,
                folded_nodes=20,direct_Chebyshev_rank=rank,prime=prime,
                cyclotomic_order=order,primitive_root=root,
                exact_root_order_verified=True,producer_607_root122_order101=True,
                quartic_nodal_identity=True,quartic_integral_mod_prime=c*c%prime,
                matrix_sha256=hashlib.sha256(json.dumps(matrix,separators=(',',':')).encode()).hexdigest())


def dictionary_checks():
    # Independent exact finite-field evaluations with order12 roots.
    p=1009; order=12; rho=pow(int(s.primitive_root(p)),(p-1)//order,p)
    require(pow(rho,order,p)==1 and all(pow(rho,order//q,p)!=1 for q in [2,3]),'root order')
    cases=[(4,[(1,0,1),(0,1,1)]),(3,[(1,1,1)]),(3,[(1,0,2),(0,1,2)]),(2,[(1,0,0),(0,1,0),(0,0,1)])]
    out=[]
    for modulus,gens in cases:
        group=sorted({tuple(sum(v*g[j] for v,g in zip(coeff,gens))%modulus for j in range(3)) for coeff in it.product(range(modulus),repeat=len(gens))})
        # Distinct characters represented by their full values on H.
        chars={}
        for u in it.product(range(modulus),repeat=3):
            sig=tuple(sum(v*t for v,t in zip(u,h))%modulus for h in group)
            chars.setdefault(sig,u)
        sigs=list(chars)
        require(len(sigs)==len(group),'character completeness')
        for phase in [(0,0,0),(1,2,3)]:
            alphas=indices(3,3); b=[[0]*len(alphas) for _ in sigs]
            sig_index={sig:i for i,sig in enumerate(sigs)}
            for j,alpha in enumerate(alphas):
                for eps in it.product([-1,1],repeat=3):
                    u=tuple(a*e for a,e in zip(alpha,eps))
                    sig=tuple(sum(v*t for v,t in zip(u,h))%modulus for h in group)
                    b[sig_index[sig]][j]=(b[sig_index[sig]][j]+pow(rho,sum(v*t for v,t in zip(u,phase))%order,p))%p
            ev=[]
            for h in group:
                t=[(phase[j]+order//modulus*h[j])%order for j in range(3)]
                row=[]
                for alpha in alphas:
                    val=1
                    for a,z in zip(alpha,t):
                        val=val*(pow(rho,a*z%order,p)+pow(rho,-a*z%order,p))*pow(2,-1,p)%p
                    row.append(val)
                ev.append(row)
            for i,h in enumerate(group):
                for j in range(len(alphas)):
                    rhs=sum(pow(rho,(order//modulus)*sig[i],p)*b[k][j] for k,sig in enumerate(sigs))*pow(8,-1,p)%p
                    require(rhs==ev[i][j],'phase dictionary identity')
            re,rb=modular_rank(ev,p),modular_rank(b,p)
            require(re==rb,'phase dictionary rank')
            out.append(dict(modulus=modulus,group_order=len(group),phase_twelfths=phase,rank=re))
    return out


def packing_checks():
    f=lambda n:n**3-108*n*n-198*n-108
    require(f(109)<=0 and f(110)>0,'n110 transition')
    # f increments positive for all n>=110 by explicit quadratic formula.
    require(3*110**2-213*110-305>0,'threshold monotonicity')
    padua=[]
    for n in range(1,11):
        m=2*n*(n+1)
        dual=lambda u: ((n+1)*u[0]+n*u[1])%m==0
        short=[u for u in it.product(range(-2*n,2*n+1),repeat=2) if any(u) and sum(map(abs,u))<=2*n and dual(u)]
        require(set(short)=={(-2*n,0),(2*n,0)},'2D Padua dual exclusion')
        nodes={(min(k*(n+1)%m,(-k*(n+1))%m),min(k*n%m,(-k*n)%m)) for k in range(m)}
        require(len(nodes)==(n+1)*(n+2)//2,'2D Padua nodes')
        padua.append(dict(n=n,torus_order=m,nodes=len(nodes),shortest_dual_l1=2*n))
    return dict(conditional_density='18/19; not verified here',threshold_polynomial_at109=f(109),threshold_polynomial_at110=f(110),padua=padua)


def lower_checks():
    a=s.Matrix([[-1,-1,-1],[-1,1,-1],[-1,-1,1]])
    require(abs(a.det())==4,'torus endomorphism determinant')
    checks=[]
    for n in range(1,21):
        h=n//2
        oddharm=sum((Q(1,2*j+1) for j in range(h+1)),Q(0))
        selected=Q(0)
        for v in it.product(range(h+1),repeat=3):
            if v[0]>min(v[1],v[2]): continue
            k=(n-v[1]-v[2],v[1]-v[0],v[2]-v[0])
            require(sum(map(abs,k))<=n,'selected frequency admissible')
            r=tuple(n+1+sum(int(a[j,l])*k[l] for l in range(3)) for j in range(3))
            require(r==tuple(2*t+1 for t in v),'selected frequency map')
            selected+=Q(1,r[0]*r[1]*r[2])
        require(3*selected>=oddharm**3,'minimum-first symmetric cube comparison')
        checks.append(dict(n=n,odd_harmonic=str(oddharm),weighted_cube_lower=str(oddharm**3/3)))
    full=[]
    # Enumerate transformed odd r directly, independent of the producer's k loop.
    for n in [1,2,4,8,16,32]:
        val=Q(0)
        for r in it.product(range(1,2*n+2,2),repeat=3):
            k=(n+1-(r[1]+r[2])//2,(r[1]-r[0])//2,(r[2]-r[0])//2)
            if sum(map(abs,k))<=n:
                val+=Q(1,2**sum(t!=0 for t in k)*r[0]*r[1]*r[2])
        odd=sum((Q(1,2*j+1) for j in range(n//2+1)),Q(0))
        require(val>=odd**3/24,'full sum lower bound')
        full.append(dict(n=n,exact_sum=str(val)))
    return dict(integer_map_determinant=int(a.det()),subset_checks=checks,full_squarewave_sums=full,
                practical_lower_exact='3/4 + 3/(2*pi)',negative_box_integral='1/8 - 3/(4*pi)',
                asymptotic_coefficient='1/(24*pi^3)')


def main():
    p=argparse.ArgumentParser();p.add_argument('--output');args=p.parse_args()
    result=dict(status='PASS',scope='Independent exact finite sanity checks; analytic/source conclusions remain in review record',
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                sympy=s.__version__,h4=h4_check(),phase=phase_check(),rank2=rank2_check(),
                dictionary=dictionary_checks(),packing=packing_checks(),lower=lower_checks(),
                rank2_cubic_survivor=rank2_cubic_survivor())
    data=json.dumps(result,indent=2)+'\n'
    if args.output:Path(args.output).write_text(data)
    print(data)

if __name__=='__main__':main()
