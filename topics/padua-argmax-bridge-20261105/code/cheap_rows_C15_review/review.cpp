#include "../cheap_rows_C15_global/global.cpp"
#undef partial
#include <string>
static std::string review_failure;
static long unit_checks=0;
static void require15(bool condition,const char*why){++unit_checks;if(!condition)throw std::runtime_error(why);}
extern "C" const char* review_error(){return review_failure.c_str();}
extern "C" void review_fault(long at){review_fault_at=at;review_partial_calls=0;}
extern "C" long review_calls(){return review_partial_calls;}
// Independent original finite cosine polynomial; no ratio or cotangent formula.
static B reference_polynomial(long n,long j,long r,const Q&a,const Q&b){
 B pi0,u,v,t,g;arb_const_pi(pi0.x,512);
 Q uf=(Q(j)+a)/Q(n),vf=(Q(r)+b)/Q(n+1);
 arb_set_fmpq(u.x,uf.x,512);arb_mul(u.x,u.x,pi0.x,512);
 arb_set_fmpq(v.x,vf.x,512);arb_mul(v.x,v.x,pi0.x,512);
 std::vector<B>cu(n+1),cv(n+1);
 for(long x=0;x<=n;x++){
  arb_mul_si(t.x,u.x,x,512);arb_cos(cu[x].x,t.x,512);
  arb_mul_si(t.x,v.x,x,512);arb_cos(cv[x].x,t.x,512);
 }
 for(long x=0;x<=n;x++)for(long y=0;y<=n-x;y++){
  arb_mul(t.x,cu[x].x,cv[y].x,512);arb_mul_si(t.x,t.x,(x?2:1)*(y?2:1),512);arb_add(g.x,g.x,t.x,512);
 }
 arb_sub(g.x,g.x,cu[n].x,512);return g;
}
static B reference_board(long n,const Q&a,const Q&b){
 B sum;
 for(long j=0;j<2*n;j++)for(long r=0;r<2*(n+1);r++)if((j+r)%2){
  B g=reference_polynomial(n,j,r,a,b);arb_abs(g.x,g.x);arb_add(sum.x,sum.x,g.x,512);
 }
 arb_div_si(sum.x,sum.x,2*n*(n+1),512);return sum;
}
extern "C" int review_point(long n,const char*as,const char*bs,double upper,double*out){
 try{
  if(n<2||n>17)throw std::runtime_error("reference degree guard");
  Q a=parse12(as),b=parse12(bs);B ref=reference_board(n,a,b),bound=point12(upper);
  out[0]=arb_le(ref.x,bound.x);out[1]=(upper==1.0&&arb_contains_si(ref.x,1));
  arf_t t;arf_init(t);arb_get_lbound_arf(t,ref.x,512);out[2]=arf_get_d(t,ARF_RND_FLOOR);
  arb_get_ubound_arf(t,ref.x,512);out[3]=arf_get_d(t,ARF_RND_CEIL);arf_clear(t);return 0;
 }catch(const std::exception&e){review_failure=e.what();return 1;}
}
extern "C" int review_units(long*out,double*values){
 unit_checks=0;review_failure.clear();review_fault_at=0;review_partial_calls=0;
 try{
  // Center projection must preserve the entire uncertain center ball.
  std::vector<B>centers={B(),range12(B(4),B(6)),range12(B(-9),B(-5)),range12(B(6),B(8)),range12(point12(.125),point12(.375))};
  for(const B&center:centers){B rho,point=centered15(center,rho),enclosure=point;arb_add_error(enclosure.x,rho.x);
   require15(arb_is_exact(point.x),"center point exact dyadic");
   require15(arb_ge(point.x,B(-5).x)&&arb_le(point.x,B(5).x),"center projection range");
   require15(arb_contains(enclosure.x,center.x),"full center radius retained");
  }
  // Complete fixed root families and empty-band cuts, using exact dyadics.
  std::set<long>D,E,cuts;
  struct Root{long c,p,delta;std::set<long>direct,edges;};
  std::vector<Root> roots={{0,0,0,{}, {0,8}},{1,0,0,{}, {0,8}},
   {0,1,0,{0,4},{0,1,4,5,8}},{0,1,1,{}, {0,4,8}},
   {1,1,0,{2},{0,2,3,8}},{-1,1,0,{6},{0,6,7,8}}};
  for(const Root&t:roots){cuts={0,8};E.clear();numerator12(B(t.c),B(t.p),8,t.delta,B(),D,cuts,E);
   require15(E==t.direct&&cuts==t.edges,"fixed root family");}
  cuts={0,8};E.clear();rootband12(range12(point12(3.25),point12(3.75)),8,D,cuts,E);
  require15(E.empty()&&cuts==std::set<long>({0,4,8}),"empty root band cut");
  cuts={0,8};poleband12(B(2),8,cuts,D);require15(D==std::set<long>({1,2,3}),"actual buffered collision equality");
  bool rejected=false;try{poleband12(range12(B(1),B(2)),8,cuts,D);}catch(const std::exception&){rejected=true;}
  require15(rejected,"width-one pole band rejection");
  auto av=endpoints12(range12(B(-1),B(3)),0,2),pv=endpoints12(B(),0,1);
  require15(av.size()==2&&arb_is_zero(av[0].x)&&arb_equal(av[1].x,B(2).x),"global A clipping");
  require15(pv.size()==1&&arb_is_zero(pv[0].x),"global vertex degeneracy");
  for(const B&v:av)require15(arb_is_exact(v.x),"global vertex endpoints exact");
  // Independent units check: pi cancels from the phase-only freeze allowance.
  // With normalized beta width db, Ephase=Lmax*db*(1+log n)^2/(n+1).
  const long n=17;Q al=Q(1)/Q(6),ah=Q(11)/Q(64),bl=Q(1)/Q(10),bh=Q(7)/Q(64);
  Stats15 st;B freeze,cube,tail,rho;
  B got=global15(n,al,ah,bl,bh,st,freeze,cube,tail,rho);
  B af=range12(qb12(al),qb12(ah)),bf=range12(qb12(bl),qb12(bh));
  auto aa=endpoints12(cos12(pi()*af)+cos12(pi()*bf),0,2),qq=endpoints12(sin12(pi()*bf),0,1);
  B L,h,db,required;arb_add(L.x,aa.back().x,qq.back().x,512);
  arb_set_si(h.x,n);arb_log(h.x,h.x,512);arb_add_si(h.x,h.x,1,512);arb_mul(h.x,h.x,h.x,512);
  Q width=bh-bl;arb_set_fmpq(db.x,width.x,512);arb_mul(required.x,L.x,db.x,512);
  arb_mul(required.x,required.x,h.x,512);arb_div_si(required.x,required.x,n+1,512);
  require15(st.vertices==8&&st.successful==32&&st.row.fallback==0,"units input all eight coherent vertices");
  require15(arb_ge(freeze.x,required.x),"radian beta width in freezing allowance");
  require15(arb_gt(rho.x,B().x),"nonzero center arithmetic radius survives");
  values[0]=upper12(got);values[1]=upper12(freeze);values[2]=upper12(required);values[3]=upper12(rho);
  out[0]=unit_checks;out[1]=st.vertices;out[2]=st.successful;out[3]=review_partial_calls;return 0;
 }catch(const std::exception&e){review_failure=e.what();out[0]=unit_checks;return 1;}
}
