/* Natural floating intervals only; no directed rounding or proof claim. */
#include <math.h>
#include <stdlib.h>
typedef struct {double lo,hi;} I;
static int valid(I a){return isfinite(a.lo)&&isfinite(a.hi)&&a.lo<=a.hi;}
static I iv(double a,double b){I z={a,b};return z;}
static I add(I a,I b){return iv(a.lo+b.lo,a.hi+b.hi);}
static I neg(I a){return iv(-a.hi,-a.lo);}
static I sub(I a,I b){return add(a,neg(b));}
static I mul(I a,I b){double x[]={a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi};double l=x[0],h=x[0];for(int i=1;i<4;i++){l=fmin(l,x[i]);h=fmax(h,x[i]);}return iv(l,h);}
static I scale(I a,double x){return mul(a,iv(x,x));}
static I divide(I a,I b){return mul(a,iv(1/b.hi,1/b.lo));}
static I trig(I a,int cosine){
 double pi=acos(-1.0),l=cosine?cos(a.lo):sin(a.lo),h=cosine?cos(a.hi):sin(a.hi);
 I z=iv(fmin(l,h),fmax(l,h));if(a.hi-a.lo>=2*pi)return iv(-1,1);
 double offset=cosine?0:pi/2;
 long p=(long)ceil((a.lo-offset)/pi),q=(long)floor((a.hi-offset)/pi);
 for(long j=p;j<=q;j++){double v=(j%2)?-1:1;z.lo=fmin(z.lo,v);z.hi=fmax(z.hi,v);}return z;
}
static double minabs(I a){return a.lo<=0&&a.hi>=0?0:fmin(fabs(a.lo),fabs(a.hi));}
static double maxabs(I a){return fmax(fabs(a.lo),fabs(a.hi));}
static double sincpoint(double x){if(fabs(x)<1e-4){double t=x*x;return 1-t/6+t*t/120-t*t*t/5040;}return sin(x)/x;}
static I sincinterval(I a){double pi=acos(-1.0),h=maxabs(a),l=minabs(a);if(h<=pi)return iv(sincpoint(h),sincpoint(l));if(a.lo>0||a.hi<0){I z=divide(trig(a,0),a);return iv(fmax(-1,z.lo),fmin(1,z.hi));}return iv(-1,1);}
static I ratio(int k,I x){
 double pi=acos(-1.0);I den=trig(x,0),z;
 long pole=lround(((x.lo+x.hi)/2)/pi);
 double p=pole*pi;
 int chart=(den.lo<=0&&den.hi>=0)||(x.lo<=p+1e-12&&x.hi>=p-1e-12)||minabs(den)<1e-8;
 if(chart){I q=sub(x,iv(p,p));if(q.lo < -pi/2||q.hi > pi/2)return iv(-k,k);
  I ds=sincinterval(q);if(ds.lo<=0)return iv(-k,k);z=scale(divide(sincinterval(scale(q,k)),ds),k);
  if((pole*(k-1))%2)z=neg(z);
 }else z=divide(trig(scale(x,k),0),den);
 I clipped=iv(fmax(-k,z.lo),fmin(k,z.hi));
 /* An empty floating intersection is uncertainty, never an empty range. */
 return valid(clipped)?clipped:iv(-k,k);
}
static I ginterval(int n,I u,I v){I s=scale(add(u,v),.5),t=scale(sub(u,v),.5);return sub(add(mul(ratio(n+1,s),ratio(n+1,t)),mul(ratio(n,s),ratio(n,t))),trig(scale(u,n),1));}
void pilot_g_interval(int n,double ul,double uh,double vl,double vh,double *out){I z=ginterval(n,iv(ul,uh),iv(vl,vh));out[0]=z.lo;out[1]=z.hi;}
static double pairlower(I a,I b){if((a.lo>0&&b.hi<0)||(a.hi<0&&b.lo>0))return 2*fmin(minabs(a),minabs(b));return 0;}

/* out S_upper,corner_upper,noncorner_lower,profile_computed. */
int pilot_box(int n,double al,double ah,double bl,double bh,double lc,double eps,int localcorner,double *out){
 int m=n+1,nr=2*n,ns=2*m;double pi=acos(-1.0),norm=2.0*n*m;
 I *h=calloc((size_t)nr*ns,sizeof(I));if(!h)return 1;
 double su=0,cu=0;
 for(int r=0;r<nr;r++)for(int s=1-r%2;s<ns;s+=2){I u=iv((r*pi+al)/n,(r*pi+ah)/n),v=iv((s*pi+bl)/m,(s*pi+bh)/m);I z=ginterval(n,u,v);if(!valid(z)){free(h);return 2;}h[(size_t)r*ns+s]=z;su+=maxabs(z);}
 su/=norm;
 for(int r=0;r<nr;r++)for(int s=1-r%2;s<ns;s+=2){int rr=(nr-r)%nr,ss=(ns-s)%ns;I z=add(add(h[(size_t)r*ns+s],h[(size_t)rr*ns+s]),add(h[(size_t)r*ns+ss],h[(size_t)rr*ns+ss]));cu+=maxabs(z);}
 cu/=(4*norm);if(!isfinite(su)||!isfinite(cu)){free(h);return 2;}out[0]=su;out[1]=cu;out[2]=0;out[3]=0;
 if(su<lc-eps||(!localcorner&&cu>=lc-eps)){free(h);return 0;}
 if(n>=48&&fmax(fabs(al),fabs(ah))+fmax(fabs(bl),fabs(bh))<=.1){out[2]=1.0/8192;free(h);return 0;}
 double *qh=calloc(n+1,sizeof(double)),*qv=calloc(m+1,sizeof(double));if(!qh||!qv){free(qh);free(qv);free(h);return 1;}
 for(int k=0;k<=m;k++){double v=0;for(int r=0;r<nr;r++)for(int s=1-r%2;s<ns;s+=2)v+=pairlower(h[(size_t)r*ns+s],h[(size_t)r*ns+(2*k-s+ns)%ns]);qv[k]=v/(2*norm);}
 for(int j=0;j<=n;j++){double v=0;for(int r=0;r<nr;r++)for(int s=1-r%2;s<ns;s+=2)v+=pairlower(h[(size_t)r*ns+s],h[(size_t)((2*j-r+nr)%nr)*ns+s]);qh[j]=v/(2*norm);}
 double low=HUGE_VAL;
 for(int j=0;j<=n;j++){if(j*pi+ah<0||j*pi+al>n*pi)continue;for(int k=1-j%2;k<=m;k+=2){if(k*pi+bh<0||k*pi+bl>m*pi)continue;if((j==0||j==n)&&(k==0||k==m))continue;low=fmin(low,fmax(qh[j],qv[k]));}}
 if(!isfinite(low)||low<0){free(qh);free(qv);free(h);return 2;}
 out[2]=low;out[3]=1;free(qh);free(qv);free(h);return 0;
}
