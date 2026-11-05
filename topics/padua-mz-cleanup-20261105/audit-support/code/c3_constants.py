import mpmath as mp
mp.mp.dps=30
L=lambda x: mp.mpf(0) if x==0 else x*x*mp.log(abs(x))
C=lambda q: 3*L(q)-2*L(q+1)-2*L(q-1)+(L(q+2)+L(q-2))/2
A=4*mp.log(2)
Jm=lambda a:(A+C(1/a))/2
Jp=lambda a:(A-C(1/a)-C(2)+(C(1/a+2)+C(1/a-2))/2)/4
print('c-',1/(9*A*Jm(mp.mpf(1)/4)),'c+',1/(36*A*Jp(mp.mpf(1)/8)))
# best within family: minus: b->1/2-a ; plus: b->1/2-2a
fm=lambda a:16*a*(mp.mpf(1)/2-a)/(9*A*Jm(a)); fp=lambda a:8*a*(mp.mpf(1)/2-2*a)/(9*A*Jp(a))
for f,name,hi in ((fm,'minus',0.5),(fp,'plus',0.25)):
    best=max((f(mp.mpf(k)/1000*hi),k) for k in range(1,1000)); print(name,'grid best',best[0],'at a=',best[1]/1000*hi)
