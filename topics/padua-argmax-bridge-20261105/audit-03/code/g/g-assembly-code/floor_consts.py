from fractions import Fraction as F
E=lambda n: F(245931,6050000)-F(206,157*n)-F(55,3*n*n)
print('E64-1/64 ', E(64)-F(1,64), E(64)-F(1,64)==F(34466881,729484800000))
print('E160-1/32', E(160)-F(1,32), E(160)-F(1,32)==F(88079689,182371200000))
# B_n(1/2) with U,V,W replaced by r=1/2 bounds 21/125, 11/20, 14/25 reproduces E_n
B=lambda n,U,V,W: F(11711,48400)*U-120*V/(157*n)-250*W/(157*n)-100*V/(3*n*n)
print('B_n(1/2 bounds)==E_n', all(B(n,F(21,125),F(11,20),F(14,25))==E(n) for n in (64,100,160,511)))
# coefficient identities: 11711/48400 = (239/100)*(7/22)^2 ; 120/157=(12/5)/(157/50); 250/157 = 5/(157/50); 100/3 = 5/(3/20)
print(F(239,100)*F(49,484)==F(11711,48400), F(12,5)/F(157,50)==F(120,157), 5/F(157,50)==F(250,157), 5/F(3,20)==F(100,3))
# full-arc floor and class-1 constants
print('fullarc', F(7,8)*F(29,492)**2 > F(1,512), '37/224 identity', F(3,4)*F(41,42)*F(37,164)==F(37,224))
# E_n increasing in n: derivative of -206/(157n)-55/(3n^2) positive
print('monotone', all(E(n+1)>E(n) for n in range(41,600)))
# D29 41..63 tier: B_n(r) clamp check of formula equivalence min(1/32,max(1/512,B))==max(1/512,min(1/32,B))
import random
print('clamp-equiv', all(min(F(1,32),max(F(1,512),b))==max(F(1,512),min(F(1,32),b)) for b in [F(random.randint(-100,100),1000) for _ in range(1000)]))
