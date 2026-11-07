#include "partial.h"
#include "partial.cpp"
#include <climits>
// Independent controls; direct q loops occur only in this review translation unit.
extern "C" int review_case(long n,long q,const char *ys,int mode,double *out){
 B y,a,lo,hi,pp,angle,c,reflo,refhi,ref;
 if(arb_set_str(y.x,ys,160))return 9;
 int rc=c06_partial_arb(n,q,y.x,a.x);
 out[0]=rc;out[1]=arb_is_finite(a.x);out[2]=mag_get_d(arb_radref(a.x));
 if(mode==2){out[3]=arb_is_zero(a.x);return 0;}
 if(mode==3){out[3]=arb_contains_zero(a.x);return 0;}
 if(mode==1){out[3]=!arb_is_finite(a.x);return 0;}
 if(rc)return 8;
 arb_get_lbound_arf(arb_midref(lo.x),y.x,512);
 arb_get_ubound_arf(arb_midref(hi.x),y.x,512);
 arb_const_pi(pp.x,512);
 for(long i=0;i<q;i++){
  for(int side=0;side<2;side++){
   arb_add_si(angle.x,side?hi.x:lo.x,i,512);
   arb_mul(angle.x,angle.x,pp.x,512);arb_div_si(angle.x,angle.x,n,512);
   arb_cot(c.x,angle.x,512);
   arb_add(side?refhi.x:reflo.x,side?refhi.x:reflo.x,c.x,512);
  }
 }
 // Every cotangent summand decreases on the positive-pole domain.
 arb_union(ref.x,reflo.x,refhi.x,512);
 out[3]=arb_contains(a.x,ref.x);
 // Native input/output aliasing must preserve the same enclosure.
 rc=c06_partial_arb(n,q,y.x,y.x);out[4]=(rc==0&&arb_equal(a.x,y.x));
 return 0;
}
extern "C" int review_moments(){
 int checks=0;
 for(long n: {2L,7L,33L,64L})for(long q: {1L,n}){
  B y;arb_set_si(y.x,1);arb_mul_2exp_si(y.x,y.x,-1);
  auto mom=moments(n,q,y);Q total,z;
  for(int d=0;d<=97;d++){
   total=Q();for(long i=0;i<q;i++){z=(Q(1)/Q(2)+Q(i))/Q(n)-Q(1)/Q(2);total=total+powerq(z,d);}
   if(!arb_contains_fmpq(mom[d].x,total.x))return -1;
   checks++;
  }
 }
 return checks;
}
extern "C" int review_long_bits(){return sizeof(long)*CHAR_BIT;}
