import json,math
from scipy.integrate import quad

def direct(beta,vertical):
 def row(b):
  zp=math.cos(beta+b); zm=math.cos(beta-b)
  if zm-zp<1e-14:return 0.0
  sw=(zp+zm+2*zp*zm)/(2+zp+zm) if vertical else (zp+zm)/2
  lo=math.acos(max(-1,min(1,zm))); hi=math.acos(max(-1,min(1,zp))); mid=math.acos(max(-1,min(1,sw)))
  def first(u):
   a=math.cos(u)
   return ((1+zp) if vertical else (1+a))/(a-zp)
  def second(u):
   a=math.cos(u)
   return ((1+zm) if vertical else (1+a))/(zm-a)
  return quad(first,lo,mid,epsabs=2e-10)[0]+quad(second,mid,hi,epsabs=2e-10)[0]
 points=sorted(set([0.0,beta,math.pi-beta,math.pi]))
 return 2/math.pi**2*sum(quad(row,a,b,epsabs=2e-9)[0] for a,b in zip(points,points[1:]))
rows=[]
for m in [0,.25,.5,.75,.99]:
 beta=math.acos(math.sqrt(m));rows.append({'m':m,'vertical':direct(beta,True),'horizontal':direct(beta,False)})
print(json.dumps({'status':'MEASURED_ONLY','method':'direct inherited double integrals split at exact fraction switch; scipy float64 quad','rows':rows},indent=2))
