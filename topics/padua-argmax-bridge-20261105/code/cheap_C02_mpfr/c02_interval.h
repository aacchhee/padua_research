/* Binary64 endpoint outward arithmetic. MPFR evaluates transcendental endpoints.
 * Requires default IEEE round-to-nearest, no fast-math and no reassociation.
 * Directed transcendental evaluation occurs at 128 bits before directed
 * conversion. Every arithmetic operation expands one binary64 ulp. */
#include <math.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <mpfr.h>
typedef struct {double lo,hi;} I;
static double dn(double x){return nextafter(x,-INFINITY);}
static double up(double x){return nextafter(x,INFINITY);}
static I iv(double a,double b){I z={a,b};return z;}
static int valid(I a){return isfinite(a.lo)&&isfinite(a.hi)&&a.lo<=a.hi;}
static I add(I a,I b){return iv(dn(a.lo+b.lo),up(a.hi+b.hi));}
static I neg(I a){return iv(-a.hi,-a.lo);}
static I sub(I a,I b){return add(a,neg(b));}
static I mul(I a,I b){double v[]={a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi};double l=v[0],h=v[0];for(int j=1;j<4;j++){l=fmin(l,v[j]);h=fmax(h,v[j]);}return iv(dn(l),up(h));}
static I scale(I a,double x){return mul(a,iv(x,x));}
static I divide(I a,I b){if(b.lo<=0&&b.hi>=0)return iv(-INFINITY,INFINITY);return mul(a,iv(dn(1/b.hi),up(1/b.lo)));}
static double minabs(I a){return a.lo<=0&&a.hi>=0?0:fmin(fabs(a.lo),fabs(a.hi));}
static double maxabs(I a){return fmax(fabs(a.lo),fabs(a.hi));}
static double c02_stat[8]={0};static int c02_fault=0;
static void newbox(void){}
static double transcend(double x,int cosine,int upper){
 static mpfr_t a,b;static int initialized=0;if(!initialized){mpfr_init2(a,128);mpfr_init2(b,128);initialized=1;}
 mpfr_rnd_t rnd=upper?MPFR_RNDU:MPFR_RNDD;mpfr_set_d(a,x,MPFR_RNDN);
 if(cosine)mpfr_cos(b,a,rnd);else mpfr_sin(b,a,rnd);c02_stat[2]++;
 return mpfr_get_d(b,rnd);
}
static I pii(void){static I z;static int initialized=0;if(!initialized){mpfr_t p;mpfr_init2(p,128);mpfr_const_pi(p,MPFR_RNDD);z.lo=mpfr_get_d(p,MPFR_RNDD);mpfr_const_pi(p,MPFR_RNDU);z.hi=mpfr_get_d(p,MPFR_RNDU);mpfr_clear(p);initialized=1;}return z;}
static I trig(I a,int cosine){
 c02_stat[1]++;
 if(!valid(a)||a.hi-a.lo>=6.28||maxabs(a)>1000000.)return iv(-1,1);
 double l=fmin(transcend(a.lo,cosine,0),transcend(a.hi,cosine,0)),h=fmax(transcend(a.lo,cosine,1),transcend(a.hi,cosine,1));
 I p=pii();double offset=cosine?0:.5,mid=(a.lo+a.hi)/2;
 long center=lround(mid/3.141592653589793-offset);
 for(long j=center-3;j<=center+3;j++){I e=scale(p,j+offset);if(e.hi>=a.lo&&e.lo<=a.hi){if(j%2)l=-1;else h=1;}}
 return iv(l,h);
}
static double pairlower(I a,I b){if((a.lo>0&&b.hi<0)||(a.hi<0&&b.lo>0))return dn(2*fmin(minabs(a),minabs(b)));return 0;}

static I square(I x){double l=minabs(x),u=maxabs(x);return iv(l==0?0:dn(l*l),up(u*u));}
static I meet(I a,I b){I z=iv(fmax(a.lo,b.lo),fmin(a.hi,b.hi));if(!valid(z))c02_fault=1;return z;}
static int paired(I *r,I *d,I v,I g){
 if(!valid(v)||!valid(g))return 0;
 I rr=meet(*r,v),dd=meet(*d,g);if(c02_fault)return 0;*r=rr;*d=dd;return 1;
}
static I rational_factorial(unsigned j){
 mpfr_t f,v;mpfr_init2(f,256);mpfr_init2(v,256);
 mpfr_fac_ui(f,j,MPFR_RNDU);mpfr_ui_div(v,1,f,MPFR_RNDD);double lo=mpfr_get_d(v,MPFR_RNDD);
 mpfr_fac_ui(f,j,MPFR_RNDD);mpfr_ui_div(v,1,f,MPFR_RNDU);double hi=mpfr_get_d(v,MPFR_RNDU);
 mpfr_clear(f);mpfr_clear(v);return iv(lo,hi);
}
static I c02_remainder(unsigned power,unsigned factor){
 mpfr_t f,v;mpfr_init2(f,256);mpfr_init2(v,256);
 mpfr_fac_ui(f,67,MPFR_RNDD);mpfr_ui_pow_ui(v,4,power,MPFR_RNDU);mpfr_mul_ui(v,v,factor,MPFR_RNDU);mpfr_div(v,v,f,MPFR_RNDU);
 double e=mpfr_get_d(v,MPFR_RNDU);mpfr_clear(f);mpfr_clear(v);return iv(-e,e);
}
static void sinc_jet(I x,I *s,I *d){
 static I a[33],er,ed;static int initialized=0;
 if(!initialized){for(unsigned j=0;j<=32;j++){a[j]=rational_factorial(2*j+1);if(j%2)a[j]=neg(a[j]);}er=c02_remainder(66,1);ed=c02_remainder(65,66);initialized=1;}
 if(x.lo==0&&x.hi==0){*s=iv(1,1);*d=iv(0,0);return;}
 I xx=square(x),p=a[32],q=scale(a[32],64);
 for(int j=31;j>=0;j--){p=add(mul(p,xx),a[j]);if(j)q=add(mul(q,xx),scale(a[j],2*j));}
 *s=meet(add(p,er),iv(-1,1));*d=meet(add(mul(q,x),ed),iv(-.5,.5));
}
static void fixed_pair(int k,I z,I *value,I *derivative){
 if(k<1||k>513||!valid(z)){c02_fault=1;*value=*derivative=iv(NAN,NAN);return;}
 c02_stat[0]++;*value=iv(-k,k);int cap=k*k/2;*derivative=iv(-cap,cap);
 if(k==1){*value=iv(1,1);*derivative=iv(0,0);return;}
 I sn=trig(z,0);
 if(minabs(sn)>0){I cs=trig(z,1),arg=scale(z,k),top=trig(arg,0),costop=trig(arg,1),den=square(sn);
  if(minabs(den)>0){I v=divide(top,sn),d=divide(sub(scale(mul(costop,sn),k),mul(top,cs)),den);if(paired(value,derivative,v,d))return;}}
 double mid=z.lo+(z.hi-z.lo)/2;
 if(!isfinite(mid)||fabs(mid)>100){c02_stat[4]++;return;}
 long turn=lround(mid/3.141592653589793);I r=sub(z,scale(pii(),turn)),kr=scale(r,k);
 if(maxabs(r)>1.5||maxabs(kr)>4){c02_stat[4]++;return;}
 I sr,dr,sk,dk;sinc_jet(r,&sr,&dr);sinc_jet(kr,&sk,&dk);sr=meet(sr,iv(.625,1));
 int sign=(turn%2!=0&&k%2==0)?-1:1;
 I v=scale(divide(sk,sr),sign*k),d=scale(divide(sub(scale(mul(dk,sr),k),mul(sk,dr)),square(sr)),sign*k);
 if(paired(value,derivative,v,d))c02_stat[3]++;else c02_stat[4]++;
}
static int full_half_radius(double al,double ah,double bl,double bh){
 double a=fmax(fabs(al),fabs(ah)),b=fmax(fabs(bl),fabs(bh));mpfr_t x,y;mpfr_init2(x,256);mpfr_init2(y,256);
 mpfr_set_d(x,a,MPFR_RNDN);mpfr_set_d(y,b,MPFR_RNDN);mpfr_add(x,x,y,MPFR_RNDU);int ok=mpfr_cmp_d(x,.5)<=0;mpfr_clear(x);mpfr_clear(y);return ok;
}
