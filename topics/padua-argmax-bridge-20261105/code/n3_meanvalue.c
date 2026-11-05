/* Float diagnostic only. No directed rounding and no certificate claim.
 * Inherited natural interval arithmetic is imported read-only. */
#include "../../padua-argmax-effective-2-20261105/code/box_pilot.c"
typedef struct { I f,a,b; double c; } J;
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
static J kernel(int n,I u,I v){
 I s=scale(add(u,v),.5),t=scale(sub(u,v),.5);
 I rs=ratio(n+1,s),rt=ratio(n+1,t),qs=ratio(n,s),qt=ratio(n,t);
 I ds=add(mul(rp(n+1,s),rt),mul(rp(n,s),qt));
 I dt=add(mul(rs,rp(n+1,t)),mul(qs,rp(n,t)));
 J z;z.f=ginterval(n,u,v);
 z.a=scale(add(scale(add(ds,dt),.5),scale(trig(scale(u,n),0),n)),1.0/n);
 z.b=scale(sub(ds,dt),.5/(n+1));
 I cp=ginterval(n,iv((u.lo+u.hi)/2,(u.lo+u.hi)/2),iv((v.lo+v.hi)/2,(v.lo+v.hi)/2));
 z.c=(cp.lo+cp.hi)/2;return z;
}
static J jsum(J x,J y){J z={add(x.f,y.f),add(x.a,y.a),add(x.b,y.b),x.c+y.c};return z;}
static I adabs(I f,I d){if(f.lo>0)return d;if(f.hi<0)return neg(d);return iv(-maxabs(d),maxabs(d));}
typedef struct {double c,natural;I a,b;} A;
static void accum(A *q,J h){q->c+=fabs(h.c);q->natural+=maxabs(h.f);q->a=add(q->a,adabs(h.f,h.a));q->b=add(q->b,adabs(h.f,h.b));}
static double upper(A q,double ra,double rb){return fmin(q.natural,q.c+maxabs(q.a)*ra+maxabs(q.b)*rb);}
int n3_box(int n,double al,double ah,double bl,double bh,double lc,double eps,int local,double *out){
 int m=n+1,nr=2*n,ns=2*m;double pi=acos(-1.0),norm=2.0*n*m;
 J *h=calloc((size_t)nr*ns,sizeof(J));if(!h)return 1;
 A sq={0,0,{0,0},{0,0}},cq=sq;
 for(int r=0;r<nr;r++)for(int s=1-r%2;s<ns;s+=2){J z=kernel(n,iv((r*pi+al)/n,(r*pi+ah)/n),iv((s*pi+bl)/m,(s*pi+bh)/m));h[(size_t)r*ns+s]=z;accum(&sq,z);}
 for(int r=0;r<nr;r++)for(int s=1-r%2;s<ns;s+=2){int rr=(nr-r)%nr,ss=(ns-s)%ns;J z=jsum(jsum(h[(size_t)r*ns+s],h[(size_t)rr*ns+s]),jsum(h[(size_t)r*ns+ss],h[(size_t)rr*ns+ss]));accum(&cq,z);}
 double su=upper(sq,(ah-al)/2,(bh-bl)/2)/norm,cu=upper(cq,(ah-al)/2,(bh-bl)/2)/(4*norm);
 out[0]=su;out[1]=cu;out[2]=0;out[3]=0;out[4]=sq.natural/norm;out[5]=cq.natural/(4*norm);
 if(!isfinite(su)||!isfinite(cu)){free(h);return 2;}
 if(su<lc-eps||(!local&&cu>=lc-eps)){free(h);return 0;}
 /* Reuse the rigorous mathematical pair-defect predicate; floating intervals
    here are only diagnostics. Take maximum with analytic constant. */
 double lowconstant=0;
 if(n>=48&&fmax(fabs(al),fabs(ah))+fmax(fabs(bl),fabs(bh))<=.1)lowconstant=1.0/8192;
 double *qh=calloc(n+1,sizeof(double)),*qv=calloc(m+1,sizeof(double));if(!qh||!qv){free(qh);free(qv);free(h);return 1;}
 for(int k=0;k<=m;k++){double v=0;for(int r=0;r<nr;r++)for(int s=1-r%2;s<ns;s+=2)v+=pairlower(h[(size_t)r*ns+s].f,h[(size_t)r*ns+(2*k-s+ns)%ns].f);qv[k]=v/(2*norm);}
 for(int j=0;j<=n;j++){double v=0;for(int r=0;r<nr;r++)for(int s=1-r%2;s<ns;s+=2)v+=pairlower(h[(size_t)r*ns+s].f,h[(size_t)((2*j-r+nr)%nr)*ns+s].f);qh[j]=v/(2*norm);}
 double low=HUGE_VAL;
 for(int j=0;j<=n;j++){if(j*pi+ah<0||j*pi+al>n*pi)continue;for(int k=1-j%2;k<=m;k+=2){if(k*pi+bh<0||k*pi+bl>m*pi)continue;if((j==0||j==n)&&(k==0||k==m))continue;low=fmin(low,fmax(qh[j],qv[k]));}}
 out[2]=fmax(lowconstant,low);out[3]=1;free(qh);free(qv);free(h);return isfinite(out[2])?0:2;
}
void n3_jet(int n,double al,double ah,double bl,double bh,double *out){J z=kernel(n,iv(al,ah),iv(bl,bh));out[0]=z.f.lo;out[1]=z.f.hi;out[2]=z.a.lo;out[3]=z.a.hi;out[4]=z.b.lo;out[5]=z.b.hi;}
