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
typedef struct {uint64_t bits;I value;unsigned generation;int cosine;} TrigCache;
static TrigCache cache[262144];static unsigned generation=1;
static void newbox(void){if(++generation==0){memset(cache,0,sizeof(cache));generation=1;}}
static double transcend(double x,int cosflag,int upper){
 uint64_t bits;memcpy(&bits,&x,sizeof(bits));size_t pos=(size_t)((bits^(bits>>29)^(bits>>47)^((uint64_t)cosflag*0x9e3779b97f4a7c15ULL))&262143);
 size_t probes=0;while(cache[pos].generation==generation&&!(cache[pos].bits==bits&&cache[pos].cosine==cosflag)&&probes++<262144)pos=(pos+1)&262143;
 if(probes>=262144){newbox();return transcend(x,cosflag,upper);}
 TrigCache *c=&cache[pos];if(c->generation!=generation){
  static mpfr_t a,b;static int initialized=0;if(!initialized){mpfr_init2(a,128);mpfr_init2(b,128);initialized=1;}
  mpfr_set_d(a,x,MPFR_RNDN);if(cosflag)mpfr_cos(b,a,MPFR_RNDD);else mpfr_sin(b,a,MPFR_RNDD);c->value.lo=mpfr_get_d(b,MPFR_RNDD);
  if(cosflag)mpfr_cos(b,a,MPFR_RNDU);else mpfr_sin(b,a,MPFR_RNDU);c->value.hi=mpfr_get_d(b,MPFR_RNDU);c->bits=bits;c->cosine=cosflag;c->generation=generation;
 }return upper?c->value.hi:c->value.lo;
}
static I pii(void){static I z;static int initialized=0;if(!initialized){mpfr_t p;mpfr_init2(p,128);mpfr_const_pi(p,MPFR_RNDD);z.lo=mpfr_get_d(p,MPFR_RNDD);mpfr_const_pi(p,MPFR_RNDU);z.hi=mpfr_get_d(p,MPFR_RNDU);mpfr_clear(p);initialized=1;}return z;}
static I trig(I a,int cosine){
 if(!valid(a)||a.hi-a.lo>=6.28)return iv(-1,1);
 double l=fmin(transcend(a.lo,cosine,0),transcend(a.hi,cosine,0)),h=fmax(transcend(a.lo,cosine,1),transcend(a.hi,cosine,1));
 I p=pii();double offset=cosine?0:.5,mid=(a.lo+a.hi)/2;
 long center=lround(mid/3.141592653589793-offset);
 for(long j=center-3;j<=center+3;j++){I e=scale(p,j+offset);if(e.hi>=a.lo&&e.lo<=a.hi){if(j%2)l=-1;else h=1;}}
 return iv(l,h);
}
static I sincpoint(double x){if(x==0)return iv(1,1);return divide(trig(iv(x,x),0),iv(x,x));}
static I sincinterval(I a){I pi=pii();double h=maxabs(a),l=minabs(a);if(h<=pi.lo){I x=sincpoint(h),y=sincpoint(l);return iv(x.lo,y.hi);}if(a.lo>0||a.hi<0){I z=divide(trig(a,0),a);return iv(fmax(-1,z.lo),fmin(1,z.hi));}return iv(-1,1);}
static I ratio(int k,I x){
 I den=trig(x,0),p=pii(),z;
 long pole=lround(((x.lo+x.hi)/2)/3.141592653589793);
 if(minabs(den)<1e-8){I q=sub(x,scale(p,pole));if(q.lo< -p.lo/2||q.hi>p.lo/2)return iv(-k,k);I ds=sincinterval(q);if(ds.lo<=0)return iv(-k,k);z=scale(divide(sincinterval(scale(q,k)),ds),k);if((pole*(k-1))%2)z=neg(z);}
 else z=divide(trig(scale(x,k),0),den);
 I c=iv(fmax(-k,z.lo),fmin(k,z.hi));return valid(c)?c:iv(-k,k);
}
static I ginterval(int n,I u,I v){I s=scale(add(u,v),.5),t=scale(sub(u,v),.5);return sub(add(mul(ratio(n+1,s),ratio(n+1,t)),mul(ratio(n,s),ratio(n,t))),trig(scale(u,n),1));}
static double pairlower(I a,I b){if((a.lo>0&&b.hi<0)||(a.hi<0&&b.lo>0))return dn(2*fmin(minabs(a),minabs(b)));return 0;}
