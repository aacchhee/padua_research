import numpy as np, math
t=np.linspace(1e-6,math.pi/4,200001)
lhs=np.abs(2/np.tan(t/2)*np.log(np.sin(t))-(4/t)*np.log(t))
rhs=t*(1+np.abs(np.log(t)))
print('max ratio |2cot(t/2)log sin t-(4/t)log t|/(t(1+|log t|)) =',float(np.max(lhs/rhs)))
# pole remainder pieces: 12/pi + 8*pi*t/48 vs 6+pi t/6 ; total envelope constant
tt=math.pi/4
print('12/pi=',12/math.pi,' sum at t=pi/4:',12/math.pi+math.pi*tt/6+tt*(1+abs(math.log(tt)))/math.pi)
# a >= 49/64 on rho<=1, 2a>=p+q on rho<=pi/2
X=np.random.default_rng(1).uniform(0,1,(200000,2)); X=X[X.sum(1)<=1]
a=np.cos(X.sum(1)/2)*np.cos((X[:,0]-X[:,1])/2); print('min a on rho<=1',a.min(),'>=49/64',a.min()>=49/64)
X=np.random.default_rng(2).uniform(0,math.pi/2,(200000,2)); X=X[X.sum(1)<=math.pi/2]
a=np.cos(X.sum(1)/2)*np.cos((X[:,0]-X[:,1])/2); print('min 2a-p-q on rho<=pi/2',(2*a-np.sin(X[:,0])-np.sin(X[:,1])).min())
# amplitude-phase step for C_inf<9/4
j=23/250; t0=2*math.log(2)/math.pi
xs=np.linspace(0,math.pi,100001); print('max -j(1-cos x)/2+t0 sin x =',float(np.max(-j*(1-np.cos(xs))/2+t0*np.sin(xs))),' formula',-j/2+math.sqrt(j*j/4+t0*t0))
