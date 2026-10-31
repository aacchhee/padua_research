#!/usr/bin/env python3
"""Independent exact U0 samples, with no imports from supplied/producer code.
Field elements are base-p encoded polynomials modulo a specified polynomial.
Checks are finite measurements, not substitutes for the written hand proof.
"""
import itertools, json, sys

class Field:
    def __init__(self,p,modulus):
        self.p,self.mod,self.d=p,modulus,len(modulus)-1
        self.order=p**self.d
    def digits(self,a):
        out=[]
        for _ in range(self.d): out.append(a%self.p);a//=self.p
        return out
    def encode(self,a): return sum((x%self.p)*self.p**i for i,x in enumerate(a))
    def add(self,a,b): return self.encode([x+y for x,y in zip(self.digits(a),self.digits(b))])
    def neg(self,a): return self.encode([-x for x in self.digits(a)])
    def sub(self,a,b): return self.add(a,self.neg(b))
    def mul(self,a,b):
        aa,bb=self.digits(a),self.digits(b);c=[0]*(2*self.d-1)
        for i,x in enumerate(aa):
            for j,y in enumerate(bb): c[i+j]+=x*y
        for i in range(len(c)-1,self.d-1,-1):
            for j in range(self.d): c[i-self.d+j]-=c[i]*self.mod[j]
        return self.encode(c[:self.d])
    def power(self,a,e):
        ans=1
        while e:
            if e&1:ans=self.mul(ans,a)
            a=self.mul(a,a);e//=2
        return ans
    def inverse(self,a):
        assert a
        return self.power(a,self.order-2)
    def div(self,a,b):return self.mul(a,self.inverse(b))
    def generator(self):
        m=self.order-1
        primes=[r for r in range(2,m+1) if m%r==0 and all(r%d for d in range(2,r))]
        return next(a for a in range(1,self.order) if all(self.power(a,m//r)!=1 for r in primes))
    def determinant(self,M):
        A=[r[:] for r in M];det=1
        for c in range(len(A)):
            pivot=next((i for i in range(c,len(A)) if A[i][c]),None)
            if pivot is None:return 0
            if pivot!=c:A[c],A[pivot]=A[pivot],A[c];det=self.neg(det)
            det=self.mul(det,A[c][c]);inv=self.inverse(A[c][c])
            for i in range(c+1,len(A)):
                f=self.mul(A[i][c],inv)
                for j in range(c+1,len(A)):A[i][j]=self.sub(A[i][j],self.mul(f,A[c][j]))
        return det

def field_for_q(q):
    if q==9:return Field(3,[2,1,0,0,1])
    r=next(a for a in range(2,q) if pow(a,(q-1)//2,q)==q-1)
    return Field(q,[-r,0,1])

def points(F,n,g,par=0):
    assert (F.order-1)%(2*n)==0 and (F.order-1)%(2*n+2)==0
    u=F.power(g,(F.order-1)//(2*n));v=F.power(g,(F.order-1)//(2*n+2))
    trace=lambda z,k:F.add(F.power(z,k),F.inverse(F.power(z,k)))
    xx=[trace(u,i) for i in range(n+1)];yy=[trace(v,j) for j in range(n+2)]
    assert len(set(xx))==n+1 and len(set(yy))==n+2
    return [(xx[i],yy[j]) for i in range(n+1) for j in range(n+2) if (i+j)%2==par]

def run():
    result={'fields':[],'determinants':[],'characters':[],'codes':[]}
    for q in [3,5,7,9,11,13,17,19,23,29,31,37,41,43,47]:
        F=field_for_q(q);g=F.generator()
        assert all(F.power(a,F.order-1)==1 for a in range(1,F.order))
        base=[a for a in range(F.order) if F.power(a,q)==a];assert len(base)==q
        result['fields'].append({'q':q,'modulus':F.mod,'generator':g,'base_elements':base if q==9 else 'prime subfield','field_test':'all nonzero a satisfy a^(q^2-1)=1'})
        for n in range(1,7):
            if (F.order-1)%(2*n) or (F.order-1)%(2*n+2):continue
            S=points(F,n,g);N=(n+1)*(n+2)//2
            rational=all(F.power(a,q)==a for pt in S for a in pt)
            predicted= q%(2*n) in {1,2*n-1} and q%(2*n+2) in {1,2*n+1}
            assert rational==predicted
            for parity in [0,1]:
                S=points(F,n,g,parity);assert len(set(S))==N
                basis=[(a,d-a) for d in range(n+1) for a in range(d+1)]
                V=[[F.mul(F.power(x,a),F.power(y,b)) for a,b in basis] for x,y in S]
                det=F.determinant(V);assert det
                expected=F.mul(F.power(2,(n*n+3*n+6)//2),F.power(n*(n+1)%F.p,N))
                assert F.mul(det,det)==expected
                result['determinants'].append({'q':q,'n':n,'parity':parity,'rational':rational,'N':N,'determinant':det,'square':expected})
        if q<=13:
            n=(q-1)//2;S={(F.div(x,2),F.div(y,2)) for x,y in points(F,n,g)}
            chi=lambda a:0 if not a else (1 if F.power(a,(q-1)//2)==1 else -1)
            minus_one=F.neg(1)
            X=[x for x in base if chi(F.sub(F.mul(x,x),1))!=-1]
            Y=[y for y in base if chi(F.sub(F.mul(y,y),1))!=1]
            eps=lambda x:chi(minus_one) if x==minus_one else chi(F.mul(2,F.add(x,1)))
            delta=lambda y:-chi(minus_one) if y==minus_one else chi(F.mul(2,F.add(y,1)))
            T={(x,y) for x in X for y in Y if eps(x)==delta(y)}
            assert S==T and len(S)==(q+1)*(q+3)//8
            raw={(x,y) for x in X for y in Y if chi(F.mul(F.add(x,1),F.add(y,1)))==1}
            result['characters'].append({'q':q,'N':len(S),'matches':True,'omitted_by_endpoint_free_shorthand':sorted(S-raw),'points':sorted(S)})
            if q==7:
                for degree in [1,2]:
                    basis=[(a,d-a) for d in range(degree+1) for a in range(d+1)]
                    G=[[pow(x,a,7)*pow(y,b,7)%7 for x,y in sorted(S)] for a,b in basis]
                    best=11;witness=None;count=0
                    for first in range(len(G)):
                        for tail in itertools.product(range(7),repeat=len(G)-first-1):
                            msg=[0]*first+[1]+list(tail)
                            cw=[sum(msg[j]*G[j][i] for j in range(len(G)))%7 for i in range(10)]
                            weight=sum(bool(x) for x in cw);count+=1
                            if weight<best:best=weight;witness=msg
                    assert best=={1:7,2:4}[degree]
                    result['codes'].append({'q':7,'n':3,'degree':degree,'N':10,'dimension':len(G),'minimum_distance':best,'projective_messages':count,'witness':witness,'basis':basis})
    return result

if __name__=='__main__':
    result=run();print(json.dumps(result,indent=2));print('ALL INDEPENDENT EXACT CHECKS PASSED',file=sys.stderr)
