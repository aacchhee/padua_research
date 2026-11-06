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
  arb_set_str(y.x,t.ys,160);int c=exact_moment_cases(t.n,t.q,y,2*J+1);if(c<0)return c;checks+=c;
 }
 Q one_third=Q(1)/Q(3);arb_set_fmpq(y.x,one_third.x,1024);
 int c=exact_moment_cases(7,2,y,13);if(c<0)return c;return checks+c;
}

// Reviewer reference: evaluate every original finite cosine term directly.
// No collapsed ratio, row formula, Chebyshev recurrence or C06 partial sum.
static B direct_board(long n,const Q&a,const Q&b){
 constexpr long RP=512;B p,sum;arb_const_pi(p.x,RP);
 for(long r=0;r<2*(n+1);r++)for(long j=0;j<2*n;j++)if((j+r)%2){
  Q uf=(Q(j)+a)/Q(n),vf=(Q(r)+b)/Q(n+1);B u,v,t,g;
  arb_set_fmpq(u.x,uf.x,RP);arb_mul(u.x,u.x,p.x,RP);
  arb_set_fmpq(v.x,vf.x,RP);arb_mul(v.x,v.x,p.x,RP);
  std::vector<B>cu(n+1),cv(n+1);
  for(long k=0;k<=n;k++){
   arb_mul_si(t.x,u.x,k,RP);arb_cos(cu[k].x,t.x,RP);
   arb_mul_si(t.x,v.x,k,RP);arb_cos(cv[k].x,t.x,RP);
  }
  for(long k=0;k<=n;k++)for(long l=0;l<=n-k;l++){
   arb_mul(t.x,cu[k].x,cv[l].x,RP);arb_mul_si(t.x,t.x,(k?2:1)*(l?2:1),RP);arb_add(g.x,g.x,t.x,RP);
  }
  arb_sub(g.x,g.x,cu[n].x,RP);arb_abs(g.x,g.x);arb_add(sum.x,sum.x,g.x,RP);
 }
 arb_div_si(sum.x,sum.x,2*n*(n+1),RP);return sum;
}
extern "C" int review_point(long n,const char*as,const char*bs,int mode,double*out){
 B result;int rc=c07_point_arb(n,as,bs,result.x);out[0]=rc;out[1]=arb_is_finite(result.x);out[2]=mag_get_d(arb_radref(result.x));
 if(mode==1){out[3]=!arb_is_finite(result.x);return 0;}
 if(rc)return 0;
 Q a,b;fmpq_set_str(a.x,as,10);fmpq_set_str(b.x,bs,10);fmpq_canonicalise(a.x);fmpq_canonicalise(b.x);
 B ref=direct_board(n,a,b);out[3]=arb_contains(result.x,ref.x);out[4]=arb_is_one(result.x)&&arb_contains(ref.x,result.x);out[5]=arb_overlaps(result.x,ref.x);
 return 0;
}
