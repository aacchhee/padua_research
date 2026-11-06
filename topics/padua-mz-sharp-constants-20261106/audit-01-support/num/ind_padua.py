# Independent signed Lebesgue Padua rule check. No repo imports.
import numpy as np, json, sys, time
def legn(n,x):
    P=np.zeros((n,len(x))); P[0]=1.0
    if n>1: P[1]=x
    for i in range(1,n-1): P[i+1]=((2*i+1)*x*P[i]-i*P[i-1])/(i+1)
    return P*np.sqrt((2*np.arange(n)+1)/2)[:,None]
def nodes(m):
    J,K=[],[]
    for j in range(m+1):
        for k in range(m+2):
            if (j+k)%2==0: J.append(j); K.append(k)
    J=np.array(J); K=np.array(K); return J,K,J*np.pi/m,K*np.pi/(m+1)
def mom(i): return 2/(1-i*i) if i%2==0 else 0.0
def weights_moment(m):
    J,K,th,ph=nodes(m)
    rows=[(i,j) for i in range(m+1) for j in range(m+1-i)]
    V=np.array([np.cos(i*th)*np.cos(j*ph) for i,j in rows]); b=np.array([mom(i)*mom(j) for i,j in rows])
    assert V.shape[0]==V.shape[1]
    w=np.linalg.solve(V,b); return w, np.linalg.cond(V), np.max(np.abs(V@w-b))
def weights_formula(m):
    J,K,th,ph=nodes(m); M=m+1; R=m//2
    t=np.array([2.0]+[-4/(4*a*a-1) for a in range(1,R+1)])
    S=np.zeros(len(J))
    for a in range(R+1):
        for b in range(R+1-a): S+=t[a]*t[b]*np.cos(2*a*th)*np.cos(2*b*ph)
    h=2/(1-m*m) if m%2==0 else 0.0
    eps=np.where((J==0)|(J==m),0.5,1.0); eta=np.where((K==0)|(K==M),0.5,1.0)
    return 2*eps*eta/(m*M)*(S-2*h*np.cos(m*th))
def main():
  ref={}
  try:
      for r in json.load(open(sys.argv[1]))['results']: ref[r['m']]=r
  except Exception as e: print('ref load',e)
  out=[]
  for m in [10,11,20,21,40,41]:
      t0=time.time(); J,K,th,ph=nodes(m); x,y=np.cos(th),np.cos(ph)
      w,cond,res=weights_moment(m); wf=weights_formula(m)
      n=m  # Pi_{m-1}: Legendre product i+j<=m-1
      Px,Py=legn(n,x),legn(n,y)
      idx=[(i,j) for i in range(n) for j in range(n-i)]
      Phi=np.array([Px[i]*Py[j] for i,j in idx])
      A=(Phi*w)@Phi.T; ev=np.linalg.eigvalsh(A)
      # exactness of moment weights on degree <= 2m-1? report max err on Pi_{2m-2} Chebyshev moments
      errs=[abs(np.sum(w*np.cos(i*th)*np.cos(j*ph))-mom(i)*mom(j)) for i in range(2*m-1) for j in range(2*m-1-i)]
      d=dict(m=m,npts=len(w),dim=len(idx),weight_sum=w.sum(),neg_count=int((w<0).sum()),neg_mass=float(-w[w<0].sum()),
             vander_cond=cond,moment_residual=res,formula_vs_moment_maxdiff=float(np.max(np.abs(w-wf))),
             max_moment_err_deg_2m_minus_2=float(max(errs)),lam_min=ev[0],lam_max=ev[-1],sec=time.time()-t0)
      if m in ref:
          r=ref[m]; d.update(ref_min=r['dense_extrema'][0],ref_max=r['dense_extrema'][1],ref_neg_count=r['solves'][0]['negative_weight_count'],
              ref_neg_mass=r['solves'][0]['negative_weight_mass'],rel_min=abs(ev[0]-r['dense_extrema'][0])/abs(r['dense_extrema'][0]),
              rel_max=abs(ev[-1]-r['dense_extrema'][1])/abs(r['dense_extrema'][1]))
      out.append(d); print(d,flush=True)
  json.dump(out,open(sys.argv[2],'w'),indent=1,default=float)

if __name__=='__main__': main()