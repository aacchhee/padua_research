/* Candidate outward first-order implementation; independent review pending. */
#include "n3_outward_interval.h"
typedef struct { I f,a,b; I c; } J;
static I rp(int k,I x){
 I den=trig(x,0);
 if(minabs(den)<.02 || x.hi-x.lo>.1){
  I z=iv(0,0);
  for(int j=0;j<k;j++){double p=k-1-2*j;z=add(z,scale(trig(scale(x,p),0),-p));}
  return z;
 }
 I top=sub(scale(mul(trig(scale(x,k),1),den),k),mul(trig(scale(x,k),0),trig(x,1)));
 return divide(top,mul(den,den));
}
static J kernel(int n,I u,I v,I uc,I vc){
 I s=scale(add(u,v),.5),t=scale(sub(u,v),.5);
 I rs=ratio(n+1,s),rt=ratio(n+1,t),qs=ratio(n,s),qt=ratio(n,t);
 I ds=add(mul(rp(n+1,s),rt),mul(rp(n,s),qt));
 I dt=add(mul(rs,rp(n+1,t)),mul(qs,rp(n,t)));
 J z;z.f=ginterval(n,u,v);
 z.a=divide(add(scale(add(ds,dt),.5),scale(trig(scale(u,n),0),n)),iv(n,n));
 z.b=divide(scale(sub(ds,dt),.5),iv(n+1,n+1));
 z.c=ginterval(n,uc,vc);return z;
}
static J jsum(J x,J y){J z={add(x.f,y.f),add(x.a,y.a),add(x.b,y.b),add(x.c,y.c)};return z;}
static I adabs(I f,I d){if(f.lo>0)return d;if(f.hi<0)return neg(d);return iv(-maxabs(d),maxabs(d));}
typedef struct {double c,natural;I a,b;} A;
static void accum(A *q,J h){q->c=up(q->c+maxabs(h.c));q->natural=up(q->natural+maxabs(h.f));q->a=add(q->a,adabs(h.f,h.a));q->b=add(q->b,adabs(h.f,h.b));}
static double upper(A q,double ra,double rb){return fmin(q.natural,up(up(q.c+up(maxabs(q.a)*ra))+up(maxabs(q.b)*rb)));}
int n3_box(int n,double al,double ah,double bl,double bh,double lc,double eps,int local,double *out){
 newbox();
 int m=n+1,nr=2*n,ns=2*m;double norm=2.0*n*m; I pi=pii();double ca=al+(ah-al)/2,cb=bl+(bh-bl)/2;double ra=fmax(up(ca-al),up(ah-ca)),rb=fmax(up(cb-bl),up(bh-cb));
 J *h=calloc((size_t)nr*ns,sizeof(J));if(!h)return 1;
 A sq={0,0,{0,0},{0,0}},cq=sq;
 for(int r=0;r<nr;r++)for(int s=1-r%2;s<ns;s+=2){I ur=scale(pi,r),vs=scale(pi,s);J z=kernel(n,divide(add(ur,iv(al,ah)),iv(n,n)),divide(add(vs,iv(bl,bh)),iv(m,m)),divide(add(ur,iv(ca,ca)),iv(n,n)),divide(add(vs,iv(cb,cb)),iv(m,m)));h[(size_t)r*ns+s]=z;accum(&sq,z);}
 for(int r=0;r<nr;r++)for(int s=1-r%2;s<ns;s+=2){int rr=(nr-r)%nr,ss=(ns-s)%ns;J z=jsum(jsum(h[(size_t)r*ns+s],h[(size_t)rr*ns+s]),jsum(h[(size_t)r*ns+ss],h[(size_t)rr*ns+ss]));accum(&cq,z);}
 double su=up(upper(sq,ra,rb)/norm),cu=up(upper(cq,ra,rb)/(4*norm));
 out[0]=su;out[1]=cu;out[2]=0;out[3]=0;out[4]=up(sq.natural/norm);out[5]=up(cq.natural/(4*norm));
 if(!isfinite(su)||!isfinite(cu)){free(h);return 2;}
 if(su<lc-eps||(!local&&cu>=lc-eps)){free(h);return 0;}
 /* Reuse the rigorous mathematical pair-defect predicate; floating intervals
    here are only diagnostics. Take maximum with analytic constant. */
 double lowconstant=0;
 if(n>=48&&up(fmax(fabs(al),fabs(ah))+fmax(fabs(bl),fabs(bh)))<=dn(.1))lowconstant=1.0/8192;
 double *qh=calloc(n+1,sizeof(double)),*qv=calloc(m+1,sizeof(double));if(!qh||!qv){free(qh);free(qv);free(h);return 1;}
 for(int k=0;k<=m;k++){double v=0;for(int r=0;r<nr;r++)for(int s=1-r%2;s<ns;s+=2)v=dn(v+pairlower(h[(size_t)r*ns+s].f,h[(size_t)r*ns+(2*k-s+ns)%ns].f));qv[k]=dn(v/(2*norm));}
 for(int j=0;j<=n;j++){double v=0;for(int r=0;r<nr;r++)for(int s=1-r%2;s<ns;s+=2)v=dn(v+pairlower(h[(size_t)r*ns+s].f,h[(size_t)((2*j-r+nr)%nr)*ns+s].f));qh[j]=dn(v/(2*norm));}
 double low=HUGE_VAL;
 for(int j=0;j<=n;j++){I ja=add(scale(pi,j),iv(al,ah));if(ja.hi<0||ja.lo>up(n*pi.hi))continue;for(int k=1-j%2;k<=m;k+=2){I kb=add(scale(pi,k),iv(bl,bh));if(kb.hi<0||kb.lo>up(m*pi.hi))continue;if((j==0||j==n)&&(k==0||k==m))continue;low=fmin(low,fmax(qh[j],qv[k]));}}
 out[2]=fmax(0,fmax(lowconstant,low));out[3]=1;free(qh);free(qv);free(h);return isfinite(out[2])?0:2;
}
void n3_jet(int n,double al,double ah,double bl,double bh,double *out){J z=kernel(n,iv(al,ah),iv(bl,bh),iv(al,ah),iv(bl,bh));out[0]=z.f.lo;out[1]=z.f.hi;out[2]=z.a.lo;out[3]=z.a.hi;out[4]=z.b.lo;out[5]=z.b.hi;}

void n3_constants(int n,double *out){I pi=pii();out[0]=pi.lo;out[1]=pi.hi;I total=iv(0,0);int m=n+1;for(int r=0;r<2*n;r++)for(int s=1-r%2;s<2*m;s+=2){I z=ginterval(n,divide(scale(pi,r),iv(n,n)),divide(scale(pi,s),iv(m,m)));total=add(total,iv(minabs(z),maxabs(z)));}total=divide(total,iv(2.0*n*m,2.0*n*m));out[2]=total.lo;out[3]=total.hi;}
int n3_geometry(int n,double al,double ah,double bl,double bh){I pi=pii();double mina=(al<=0&&ah>=0)?0:fmin(fabs(al),fabs(ah)),minb=(bl<=0&&bh>=0)?0:fmin(fabs(bl),fabs(bh));if(dn(mina+minb)>pi.hi)return 1;double aa=fmax(fabs(al),fabs(ah)),bb=fmax(fabs(bl),fabs(bh));I x=trig(divide(iv(aa,aa),iv(2*n,2*n)),0),y=trig(divide(iv(bb,bb),iv(2*(n+1),2*(n+1))),0);I h=scale(add(mul(x,x),mul(y,y)),2);I N=iv((double)n*(n+1),(double)n*(n+1));I radius=divide(iv(1,1),scale(mul(mul(N,N),N),2));I r2=divide(iv(1,1),mul(iv(100000000000.,100000000000.),iv(n*n,n*n)));
return h.hi<=fmax(radius.lo,r2.lo)?2:0;}
const char *n3_mpfr_version(void){return mpfr_get_version();}
