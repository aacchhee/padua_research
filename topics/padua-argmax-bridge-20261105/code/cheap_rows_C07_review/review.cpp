#include "point.cpp"
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
extern "C" int review_rootcuts(){
 int checks=0;
 for(long k=0;k<8;k++){
  std::set<long>cuts{0,8},direct;rootcut(qb(Q(k)/Q(8)),8,B(),cuts,direct);
  if(direct!=std::set<long>{k}||!cuts.count(k)||!cuts.count(k+1))return -1;checks++;
  cuts={0,8};direct.clear();rootcut(qb((Q(k)+Q(1)/Q(2))/Q(8)),8,B(),cuts,direct);
  if(!direct.empty()||(k<7&&!cuts.count(k+1)))return -2;checks++;
 }
 for(long s:{-2L,2L}){
  std::set<long>cuts{0,8},direct;rootcut(B(s),8,B(),cuts,direct);
  if(!direct.empty()||cuts!=std::set<long>{0,8})return -3;checks++;
 }
 {
  B wide;arb_set_str(wide.x,"[.5 +/- .2]",P);std::set<long>cuts{0,8},direct;bool rejected=false;
  try{rootcut(wide,8,B(),cuts,direct);}catch(const std::runtime_error&){rejected=true;}
  if(!rejected)return -4;checks++;
 }
 for(long sign:{-1L,1L}){
  B threshold(sign),epsilon;arb_set_str(epsilon.x,"1e-30",P);arb_add_error(threshold.x,epsilon.x);
  std::set<long>cuts{0,8},direct;sinecuts(threshold,8,B(),cuts,direct);
  if(direct!=std::set<long>{sign>0?2L:6L})return -5;checks++;
 }
 return checks;
}
