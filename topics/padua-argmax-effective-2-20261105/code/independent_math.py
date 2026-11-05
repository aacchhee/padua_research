#!/usr/bin/env python3
"""Independent small-degree spectral checks; no developer module imported.
High-precision diagnostics are MEASURED, not interval/exact certificates.
CRT and endpoint multiplicity assertions use exact integer arithmetic.
"""
import argparse
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import time
import mpmath as mp

mp.mp.dps = 70
start = time.monotonic()
INPUT_HEAD = subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
errors = {}
counts = Counter()

def eq(key, a, b):
    err = abs(a-b)
    errors[key] = max(errors.get(key, mp.mpf(0)), err)
    counts[key] += 1
    assert err < mp.mpf('1e-60'), (key, a, b, err)

@lru_cache(None)
def cosines(n, t):
    x = mp.cos(mp.pi * t.numerator/t.denominator)
    vals = [mp.mpf(1), x]
    for k in range(2, n+1):
        vals.append(2*x*vals[-1]-vals[-2])
    return tuple(vals[:n+1])

def G(n, u, v):
    cu, cv = cosines(n, u), cosines(n, v)
    # Finite corrected rhombus spectral polynomial, including all collisions.
    return mp.fsum((1 if p == 0 else 2)*(1 if q == 0 else 2)*cu[p]*cv[q]
                   for p in range(n+1) for q in range(n+1-p))-cu[n]

def nodes(n):
    m = n+1
    for j in range(n+1):
        for k in range(m+1):
            if (j+k)%2 == 0:
                e = Q(1,2) if j in (0,n) else Q(1)
                f = Q(1,2) if k in (0,m) else Q(1)
                yield j,k,mp.mpf((2*e*f).numerator)/(2*e*f).denominator/(n*m)

def physical(n, theta, phi):
    m=n+1
    ct, cp=cosines(n,theta),cosines(n,phi)
    lam=[]; major=[]; qv=[]; qh=[]
    for j,k,w in nodes(n):
        cj,ck=cosines(n,Q(j,n)),cosines(n,Q(k,m))
        direct=mp.fsum((1 if p == 0 else 2)*(1 if q == 0 else 2)*ct[p]*cj[p]*cp[q]*ck[q]
                       for p in range(n+1) for q in range(n+1-p))-ct[n]*cj[n]
        copies=[[G(n,theta+s*Q(j,n),phi+t*Q(k,m)) for t in (-1,1)] for s in (-1,1)]
        eq('cardinal_four_copy',direct,mp.fsum(x for row in copies for x in row)/4)
        lam.append(w*abs(direct))
        major.append(w*mp.fsum(abs(x) for row in copies for x in row)/4)
        qv.append(w*mp.fsum(abs(row[0])+abs(row[1])-abs(sum(row)) for row in copies)/4)
        qh.append(w*mp.fsum(abs(copies[0][b])+abs(copies[1][b])-abs(copies[0][b]+copies[1][b]) for b in (0,1))/4)
    return tuple(mp.fsum(v) for v in (lam,major,qv,qh))

def primitive(n, alpha, beta):
    m=n+1
    return mp.fsum(abs(G(n,Q(j,n)+alpha/n,Q(k,m)+beta/m))
                   for j in range(2*n) for k in range(2*m) if (j+k)%2)/(2*n*m)

summaries=[]
energy_samples=[]
max_scaled_profile_error=mp.mpf(0)
for n in range(2,9):
    m=n+1; N=n*m
    # Exact finite multiplicity count: signed lifts have count 4 e_j f_k.
    lifts=Counter((j%(2*n),k%(2*m)) for j,k,_ in nodes(n) for j in (j,-j) for k in (k,-k))
    for j in range(2*n):
        for k in range(2*m):
            if (j+k)%2: assert lifts[(j,k)] == 0
            else:
                expected=(2 if j in (0,n) else 1)*(2 if k in (0,m) else 1)
                assert lifts[(j,k)] == expected
    counts['integer_endpoint_multiplicity']+=1
    # CRT injectivity on the odd board, including proof-relevant residue parity.
    board=[(j,k) for j in range(2*n) for k in range(2*m) if (j+k)%2]
    residues=[(m*j+n*k)%(2*N) for j,k in board]
    assert sorted(residues)==list(range(2*N))
    odd_residues=[(2*t+2*n+1)%(4*N) for t in residues]
    assert sorted(odd_residues)==list(range(1,4*N,2))
    assert all((m*(2*j+1)-n*(2*k+1))%(4*N) != 0 for j,k in board)
    assert all((m*(2*j+1)+n*(2*k+1))%(4*N) != 0 for j,k in board)
    counts['integer_crt_bijection_no_collisions']+=1
    zero=primitive(n,Q(0),Q(0))
    eq('zero_phase_collision',G(n,Q(1),Q(1)),2*n*(-1)**n)
    eq('positive_endpoint_collision',G(n,Q(0),Q(0)),2*N)
    # Every r=m odd-board entry other than (n,m) vanishes.
    for j,k in board:
        if k==m and j != n:
            eq('zero_endpoint_row',G(n,Q(j,n),Q(1)),0)
    xs=[Q(0),Q(1,2*n),Q(1,2),1-Q(1,2*n),Q(1)]
    ys=[Q(0),Q(1,2*m),Q(1,2),1-Q(1,2*m),Q(1)]
    minimum_defect=None
    for theta in xs:
        for phi in ys:
            centers=[(abs(n*theta-j)+abs(m*phi-k),j,k) for j in range(n+1) for k in range(m+1) if (j+k)%2]
            rho,J,K=min(centers)
            assert rho<=1
            alpha,beta=n*theta-J,m*phi-K
            lam,S,qv,qh=physical(n,theta,phi)
            eq('physical_to_periodic',S,primitive(n,alpha,beta))
            assert min(S-lam,S-lam-qv,S-lam-qh) > -mp.mpf('1e-60')
            H={(r,s):G(n,Q(r,n)+alpha/n,Q(s,m)+beta/m) for r,s in board}
            dv=mp.fsum(abs(x)+abs(H[(r,(2*K-s)%(2*m))])-abs(x+H[(r,(2*K-s)%(2*m))]) for (r,s),x in H.items())/(4*N)
            dh=mp.fsum(abs(x)+abs(H[((2*J-r)%(2*n),s)])-abs(x+H[((2*J-r)%(2*n),s)]) for (r,s),x in H.items())/(4*N)
            orbit_lambda=mp.fsum(abs(x+H[((2*J-r)%(2*n),s)]+H[(r,(2*K-s)%(2*m))]+H[((2*J-r)%(2*n),(2*K-s)%(2*m))]) for (r,s),x in H.items())/(8*N)
            eq('periodic_full_lambda',lam,orbit_lambda)
            eq('periodic_projected_vertical',qv,dv)
            eq('periodic_projected_horizontal',qh,dh)
            counts['defect_projection_inequalities']+=1
            minimum_defect=S-lam if minimum_defect is None else min(minimum_defect,S-lam)
            if theta in (0,1) and phi in (0,1):
                eq('corner_reflections_coincide',lam,S)
                eq('corner_node_or_nonnode',lam,zero if (int(n*theta)+int(m*phi))%2 else 1)
    # Coset independence at one phase pair over every physically valid odd center.
    alpha,beta=Q(1,11),Q(-1,13)
    reference=primitive(n,alpha,beta)
    for J in range(n+1):
        for K in range(m+1):
            theta,phi=(J+alpha)/n,(K+beta)/m
            if (J+K)%2 and 0<=theta<=1 and 0<=phi<=1:
                _,S,_,_=physical(n,theta,phi)
                eq('all_valid_cosets_at_fixed_phase',S,reference)
    boundary=primitive(n,Q(1,2),Q(1,2))
    L=mp.fsum(mp.cot((2*k-1)*mp.pi/(4*N)) for k in range(1,N+1))/N
    eq('boundary_L_N',boundary,L)
    eq('boundary_opposite_sign',primitive(n,Q(1,2),Q(-1,2)),L)
    # Boundary signed kernel before summing and noncollision divided difference.
    for j,k in board:
        u,v=Q(2*j+1,2*n),Q(2*k+1,2*m)
        eq('boundary_signed_cotangent',(-1)**j*G(n,u,v),mp.cot(mp.pi*(mp.mpf(u.numerator)/u.denominator+mp.mpf(v.numerator)/v.denominator)/2))
    for t in (Q(0),Q(1,1000000),Q(1,7),Q(1,2*n+1),Q(1,2),Q(2*n,2*n+1),Q(6,7),1-Q(1,1000000),Q(1)):
        val=primitive(n,t,1-t)
        if t in (0,1):
            eq('boundary_vertex',val,1)
            profile=mp.mpf(1)
        else:
            z=mp.mpf(t.numerator)/t.denominator
            collapsed=mp.sin(mp.pi*z)/(2*N)*mp.fsum(abs(mp.cot(mp.pi*(q+z)/(2*N))) for q in range(2*N))
            eq('boundary_general_cotangent',val,collapsed)
            # -psi(t)-psi(1-t) equals the theorem's convergent C(t) series.
            C=-mp.digamma(z)-mp.digamma(1-z)
            profile=mp.sin(mp.pi*z)/mp.pi*(2*mp.log(2*N/mp.pi)+C)
        scaled_error=N*N*abs(val-profile)
        assert scaled_error <= Q(7,12)+mp.mpf('1e-60')
        max_scaled_profile_error=max(max_scaled_profile_error,scaled_error)
        counts['boundary_uniform_profile_bound']+=1
    energy=mp.mpf(0)
    for j,k,w in nodes(n):
        cj,ck=cosines(n,Q(j,n)),cosines(n,Q(k,m))
        def corner_sum(dx,dy):
            def factor(p,deriv):
                return (-1)**p if not deriv else (-1)**(p+1)*p*p
            return w*(mp.fsum((1 if p==0 else 2)*(1 if q==0 else 2)*factor(p,dx)*cj[p]*factor(q,dy)*ck[q]
                     for p in range(n+1) for q in range(n+1-p))
                     -(factor(n,dx)*cj[n] if not dy else 0))
        value,gx,gy=corner_sum(0,0),corner_sum(1,0),corner_sum(0,1)
        if k==0 and j>0:
            eq('corner_zero_cardinal',value,0)
            continue
        energy+=(gx*gx+gy*gy)/abs(value)
        if j==0 and k==0:
            eq('removable_gradient_x',gx,-(-1)**n*mp.mpf(2*n*n+1)/(6*m))
            eq('removable_gradient_y',gy,-(-1)**n*mp.mpf(2*n+1)/6)
        else:
            a,b=cj[1],ck[1]; C=1-b; d=b-a
            qx=-mp.mpf(n*n)/2+n*(a*b-1)/(C*d)-a/d+2*(1-a*a)/(d*d)
            eq('corner_ratio_x',gx/value,qx)
            eq('corner_ratio_cancellation',gy/value-gx/value,-mp.mpf(2*n+1)/2+(1-a)/d)
    tau=Q(n,m)
    exact_K=-2*n*(1+tau*tau)/(tau*tau*(1-tau*tau))-2/(1-tau*tau)+8/(1-tau*tau)**2
    assert exact_K == -Q(2*m**3,n*(2*n+1)**2)
    counts['exact_diagonal_cancellation']+=1
    assert energy <= 10**10*n**4*zero
    energy_samples.append({'n':n,'W_over_n4_Lambda_c':mp.nstr(energy/(n**4*zero),25)})
    summaries.append({'n':n,'S_origin':mp.nstr(zero,25),'S_boundary':mp.nstr(boundary,25),'min_sampled_defect':mp.nstr(minimum_defect,5)})

# Conditional threshold arithmetic; C is an input, not a proved global constant.
A=4/mp.pi**2; b=8/mp.pi**2*(mp.euler+mp.log(8/mp.pi)); c=mp.mpf('1.846')
thresholds=[]
for denom in (64,16):
    rho=mp.mpf(1)/denom; f=rho*rho/(2*mp.pi**2)
    for C in map(mp.mpf,('1.4','1.45','1.6','1.7')):
        lead=C/(f*A)
        q=b-C/f
        model=(-q+mp.sqrt(q*q-4*A*c))/(2*A)
        def conditional_root(q):
            return (C+mp.sqrt(C*C+4*q*A*(54*q+C*mp.log(mp.mpf(3)/2))))/(2*q*A)
        thresholds.append({'rho':f'1/{denom}','C_input':str(C),'leading_log_n':mp.nstr(lead,20),'quadratic_model_log_n':mp.nstr(model,20),
                           'coarse_conditional_lower_bound_root':mp.nstr(conditional_root(f),20),
                           'sharp_phase_conditional_lower_bound_root':mp.nstr(conditional_root(1-mp.cos(rho/2)),20)})

source=Path(__file__).resolve()
result={'status':'PASS; numerical checks MEASURED, integer checks exact finite scope',
 'precision_decimal_digits':mp.mp.dps,'degrees':list(range(2,9)),
 'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'input_head':INPUT_HEAD,
 'environment':{'python':platform.python_version(),'mpmath':mp.__version__,'platform':platform.platform()},
 'counts':dict(counts),'max_absolute_errors':{k:mp.nstr(v,8) for k,v in errors.items()},
 'summaries':summaries,'energy_samples':energy_samples,'boundary_profile_max_N_squared_error':mp.nstr(max_scaled_profile_error,20),
 'conditional_A0_arithmetic':thresholds,
 'elapsed_seconds':time.monotonic()-start,
 'limitations':'No developer kernel imported; high precision is not outward rounding; no all-degree proof follows from finite tests; A0 constants are hypothetical.'}
parser=argparse.ArgumentParser(); parser.add_argument('--output',type=Path,required=True); args=parser.parse_args()
args.output.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'counts':result['counts'],'elapsed_seconds':result['elapsed_seconds'],'output':str(args.output)}))
