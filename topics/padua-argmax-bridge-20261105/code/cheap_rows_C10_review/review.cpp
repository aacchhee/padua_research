#include "point.cpp"
// Independent monotone endpoint reference, outside production call paths.
extern "C" int review_partial(long n,long q,const char*ys,int mode,double*out){
 B y,ans,lo,hi,p,ref[2],hull,t,c;
 if(arb_set_str(y.x,ys,160))return 9;
 int rc=c06_partial_arb(n,q,y.x,ans.x);out[0]=rc;out[1]=arb_is_finite(ans.x);out[2]=mag_get_d(arb_radref(ans.x));
 if(mode){out[3]=mode==1?!arb_is_finite(ans.x):arb_is_zero(ans.x);return 0;}
 if(rc)return 8;
 arb_get_lbound_arf(arb_midref(lo.x),y.x,512);arb_get_ubound_arf(arb_midref(hi.x),y.x,512);arb_const_pi(p.x,512);
 for(long i=0;i<q;i++)for(int side=0;side<2;side++){
  arb_add_si(t.x,side?hi.x:lo.x,i,512);arb_mul(t.x,t.x,p.x,512);arb_div_si(t.x,t.x,n,512);arb_cot(c.x,t.x,512);arb_add(ref[side].x,ref[side].x,c.x,512);
 }
 arb_union(hull.x,ref[0].x,ref[1].x,512);out[3]=arb_contains(ans.x,hull.x);return 0;
}
static int exact_moment_cases(long n,long q,const B&y,int degree){
 auto output=moments(n,q,y);Q center,radius,end,total,z;
 arf_get_fmpq(center.x,arb_midref(y.x));B rad;arf_set_mag(arb_midref(rad.x),arb_radref(y.x));arf_get_fmpq(radius.x,arb_midref(rad.x));
 int checks=0;
 for(int side=-1;side<=1;side++){
  end=center+Q(side)*radius;
  for(int d=0;d<=degree;d++){
   total=Q();for(long i=0;i<q;i++){z=(end+Q(i))/Q(n)-Q(1)/Q(2);total=total+powerq(z,d);}
   if(!arb_contains_fmpq(output[d].x,total.x))return -1;
   checks++;
  }
 }
 return checks;
}
extern "C" int review_interval_moments(){
 int checks=0;B y;
 struct Case{long n,q;const char*ys;};
 for(auto t:{Case{3,3,"[.5 +/- .125]"},Case{11,5,"[.375 +/- .03125]"},Case{5,1,"[4.5 +/- .125]"},Case{2147483647,1,"[2147483646.5 +/- .125]"}}){
  arb_set_str(y.x,t.ys,160);int c=exact_moment_cases(t.n,t.q,y,97);if(c<0)return c;checks+=c;
 }
 Q one_third=Q(1)/Q(3);arb_set_fmpq(y.x,one_third.x,1024);
 int c=exact_moment_cases(7,2,y,13);if(c<0)return c;return checks+c;
}
