"""Independent Lebesgue enclosure (Claude audit05 D4). Does not import producer code.
V exact (rational Chebyshev recurrence on exact dyadic nodes, rounded to 2^-KV);
mesh rows exact at TRUE Chebyshev-Lobatto points via T_k(cos t)=cos(kt), with own
rational Machin/Taylor enclosure of cos(l*pi/(mn)); int128 C++ kernels; Fraction endpoints."""
import sys, json, base64, hashlib, math, subprocess, time, os
from fractions import Fraction as F
import numpy as np
HERE=os.path.dirname(os.path.abspath(__file__)); KV=50; KC=40
def load(path):
    d=json.load(open(path)); raw=base64.b85decode(d['coordinates_base85'])
    assert hashlib.sha256(raw).hexdigest()==d['coordinates_sha256']
    x=np.frombuffer(raw,dtype='<f8').reshape(-1,3)
    return x, d['coordinates_sha256'], d.get('n')
def exps(n):  # my own order: by total degree, then reverse-lex
    return [(a,b,s-a-b) for s in range(n+1) for a in range(s,-1,-1) for b in range(s-a,-1,-1)]
def cheb_exact(t,n):  # exact T_0..T_n at exact rational t
    T=[F(1),t]
    for k in range(1,n): T.append(2*t*T[k]-T[k-1])
    return T[:n+1]
def rnd(fr,K):  # nearest integer to fr*2^K (ties up), exact
    v=fr*(1<<K); return math.floor(v+F(1,2))
# ---- rigorous pi and cos enclosures, pure rationals ----
def atan_inv(x,terms):  # atan(1/x) bracket via alternating series
    s=F(0);
    for k in range(terms): s+=F((-1)**k, (2*k+1)*x**(2*k+1))
    nxt=F(1,(2*terms+1)*x**(2*terms+1))
    return (s,s+nxt) if terms%2==0 else (s-nxt,s)
def pi_enc():
    a=atan_inv(5,60); b=atan_inv(239,30)
    return 16*a[0]-4*b[1], 16*a[1]-4*b[0]
def cos_enc(th,terms=60):  # 0<=th<=pi rational; alternating, terms decrease from k>=1
    s=F(0); t=F(1)
    for k in range(terms):
        s+=t; t=-t*th*th/((2*k+1)*(2*k+2))
    # remainder bounded by |t| (alternating, decreasing since (2k+1)(2k+2)>pi^2 for k>=1)
    return s-abs(t), s+abs(t)
def lobatto_table(G):
    plo,phi=pi_enc(); assert F(314159,100000)<plo<phi<F(314160,100000)
    C=[];eps=F(0)
    for l in range(G+1):
        if l==0: lo=hi=F(1)
        elif l==G: lo=hi=F(-1)
        elif 2*l==G: lo=hi=F(0)
        else:
            tlo=plo*l/G; thi=phi*l/G; c0,c1=cos_enc(tlo); lo=c0-(thi-tlo); hi=c1  # cos decreasing on [0,pi], 1-Lipschitz
        mid=(lo+hi)/2; Ci=rnd(mid,KC); C.append(Ci)
        eps=max(eps,abs(mid-F(Ci,1<<KC))+(hi-lo)/2)
    eps=F(math.ceil(eps*(1<<200)),1<<200)  # outward (up) dyadic
    return C,eps
def secant_upper(m):  # rational q >= 1/cos(pi/(2m)) for m=2,3 exactly
    target={2:F(2),3:F(4,3)}[m]; s=1<<60
    q=F(math.isqrt(math.floor(target*s*s))+1,s); assert q*q>=target; return q
def main(path,n_expect,m_list,label):
    t0=time.time(); x,sha,n=load(path); n=n_expect if n is None else n; assert n==n_expect
    N=math.comb(n+3,3); assert x.shape==(N,3) and len({tuple(r) for r in x.tolist()})==N and np.max(np.abs(x))<=1
    E=exps(n); assert len(E)==N and len(set(E))==N
    vals={}
    for t in set(x.flatten().tolist()): vals[t]=cheb_exact(F(t),n)
    # exact V rounded at 2^-KV, row=node, col=basis
    Vi=np.zeros((N,N),dtype=np.int64)
    for i,(p,q_,r) in enumerate(x.tolist()):
        A,B,Cc=vals[p],vals[q_],vals[r]
        for j,(a,b,c) in enumerate(E): Vi[i,j]=rnd(A[a]*B[b]*Cc[c],KV)
    betaV=F(1,1<<(KV+1))
    Vf=Vi.astype(np.float64)/2.0**KV; Wf=np.linalg.inv(Vf)
    KW=61-int(math.ceil(math.log2(np.max(np.abs(Wf))+1)))
    Wi=np.rint(Wf*2.0**KW).astype(np.int64); assert np.max(np.abs(Wi))<2**61
    w=F(max(sum(abs(int(v)) for v in row) for row in Wi.tolist()),1<<KW)
    tmp=os.path.join(HERE,'tmp_'+label); os.makedirs(tmp,exist_ok=True)
    Vi.tofile(tmp+'/V.bin'); Wi.tofile(tmp+'/W.bin')
    out=subprocess.run([HERE+'/cert','res',str(N),str(KV+KW),tmp+'/V.bin',tmp+'/W.bin'],capture_output=True,text=True,check=True).stdout.split()
    r0=F(int(out[1]),1<<(KV+KW)); rho=r0+N*betaV*w; assert rho<1
    res={'label':label,'path':path,'sha':sha,'n':n,'N':N,'KV':KV,'KW':KW,'KC':KC,'w':str(w),'r0':str(r0),'rho':str(rho),'rho_f':float(rho),'w_f':float(w),'prep_s':time.time()-t0,'meshes':[]}
    for m in m_list:
        t1=time.time(); G=m*n; C,eps=lobatto_table(G)
        np.array(C,dtype=np.int64).tofile(tmp+f'/C{m}.bin'); np.array(E,dtype=np.int64).tofile(tmp+'/E.bin')
        o=subprocess.run([HERE+'/cert','mesh',str(N),str(n),str(m),str(KC),tmp+f'/C{m}.bin',tmp+'/E.bin',tmp+'/W.bin'],capture_output=True,text=True,check=True).stdout.split()
        Mx=F(int(o[1]),1<<(KC+KW)); cnt=int(o[7]); assert cnt==(G+1)**3
        betam=(1+eps)**3-1+F(1,1<<(KC+1)); e=N*betam*w
        mlo=max(F(0),Mx-e)/(1+rho); mhi=(Mx+e)/(1-rho); cm=secant_upper(m); up=cm*mhi
        mlo=F(math.floor(mlo*(1<<120)),1<<120); mhi=F(math.ceil(mhi*(1<<120)),1<<120); up=F(math.ceil(up*(1<<120)),1<<120)  # outward
        res['meshes'].append({'m':m,'points':cnt,'arg_index':[int(o[3]),int(o[4]),int(o[5])],'eps_cos':float(eps),'beta_mesh':float(betam),'e':float(e),
            'mesh_max':float(Mx),'mesh_lower':str(mlo),'mesh_upper':str(mhi),'cm_upper':str(cm),'lambda_lower':str(mlo),'lambda_upper':str(up),
            'display':[float(mlo),float(up)],'seconds':time.time()-t1})
    return res
if __name__=='__main__':
    path,n,ms,label,outp=sys.argv[1],int(sys.argv[2]),[int(v) for v in sys.argv[3].split(',')],sys.argv[4],sys.argv[5]
    r=main(path,n,ms,label); json.dump(r,open(outp,'w'),indent=1); print(json.dumps({k:(v if k!='meshes' else [{kk:mm[kk] for kk in ('m','points','display','mesh_max','e','seconds','arg_index')} for mm in v]) for k,v in r.items() if k not in ('w','r0','rho')}))
