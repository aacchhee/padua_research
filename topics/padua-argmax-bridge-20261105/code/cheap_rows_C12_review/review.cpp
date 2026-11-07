#include "../cheap_rows_C12_box/box.cpp"
#undef partial
#include <string>
static std::string failure;
static long checks=0;
static void require(bool ok,const char*why){++checks;if(!ok)throw std::runtime_error(why);}
extern "C" const char* review_error(){return failure.c_str();}
extern "C" void review_fault(long at){review_fault_at=at;review_partial_calls=0;}
extern "C" long review_calls(){return review_partial_calls;}
// Independent original finite cosine polynomial, at 512 bits.
static B polynomial(long n,long j,long r,const Q&a,const Q&b){
 B p,u,v,t,g;arb_const_pi(p.x,512);
 Q uf=(Q(j)+a)/Q(n),vf=(Q(r)+b)/Q(n+1);
 arb_set_fmpq(u.x,uf.x,512);arb_mul(u.x,u.x,p.x,512);
 arb_set_fmpq(v.x,vf.x,512);arb_mul(v.x,v.x,p.x,512);
 std::vector<B>cu(n+1),cv(n+1);
 for(long x=0;x<=n;x++){
  arb_mul_si(t.x,u.x,x,512);arb_cos(cu[x].x,t.x,512);
  arb_mul_si(t.x,v.x,x,512);arb_cos(cv[x].x,t.x,512);
 }
 for(long x=0;x<=n;x++)for(long y=0;y<=n-x;y++){
  arb_mul(t.x,cu[x].x,cv[y].x,512);
  arb_mul_si(t.x,t.x,(x?2:1)*(y?2:1),512);arb_add(g.x,g.x,t.x,512);
 }
 arb_sub(g.x,g.x,cu[n].x,512);return g;
}
static B board(long n,const Q&a,const Q&b){
 B sum;
 for(long j=0;j<2*n;j++)for(long r=0;r<2*(n+1);r++)if((j+r)%2){
  B g=polynomial(n,j,r,a,b);arb_abs(g.x,g.x);arb_add(sum.x,sum.x,g.x,512);
 }
 arb_div_si(sum.x,sum.x,2*n*(n+1),512);return sum;
}
extern "C" int review_point(long n,const char*as,const char*bs,double upper,double*out){
 try{
  if(n<2||n>17)throw std::runtime_error("review reference degree");
  Q a=parse12(as),b=parse12(bs);B ref=board(n,a,b),bound=point12(upper);
  out[0]=arb_le(ref.x,bound.x);
  out[1]=upper==1.0&&arb_contains_si(ref.x,1);
  arf_t x;arf_init(x);arb_get_lbound_arf(x,ref.x,512);out[2]=arf_get_d(x,ARF_RND_FLOOR);
  arb_get_ubound_arf(x,ref.x,512);out[3]=arf_get_d(x,ARF_RND_CEIL);arf_clear(x);
  return 0;
 }catch(const std::exception&e){failure=e.what();return 1;}
}
static B ratio_reference(long k,long turn,const Q&r){
 B p,z,t,c,sum;arb_const_pi(p.x,512);arb_mul_si(z.x,p.x,turn,512);
 arb_set_fmpq(t.x,r.x,512);arb_add(z.x,z.x,t.x,512);
 for(long j=0;j<k;j++){
  arb_mul_si(t.x,z.x,k-1-2*j,512);arb_cos(c.x,t.x,512);arb_add(sum.x,sum.x,c.x,512);
 }return sum;
}
static B vertex_reference(long n,long r,long c,long p,const Q&a,const Q&b,const std::set<long>&D){
 B pi0,u,v,s,t,num,den,sum;arb_const_pi(pi0.x,512);long delta=(1-r)%2;if(delta<0)delta+=2;
 Q vf=(Q(r)+b)/Q(n+1);arb_set_fmpq(v.x,vf.x,512);arb_mul(v.x,v.x,pi0.x,512);
 arb_cos(t.x,v.x,512);
 for(long k=0;k<n;k++)if(!D.count(k)){
  Q uf=(Q(delta+2*k)+a)/Q(n);arb_set_fmpq(u.x,uf.x,512);arb_mul(u.x,u.x,pi0.x,512);
  arb_sin(s.x,u.x,512);arb_mul_si(s.x,s.x,p,512);arb_neg(num.x,s.x);arb_add_si(num.x,num.x,c,512);
  arb_cos(den.x,u.x,512);arb_sub(den.x,den.x,t.x,512);arb_mul_2exp_si(den.x,den.x,1);
  require(!arb_contains_zero(den.x),"reference vertex denominator");
  arb_div(s.x,num.x,den.x,512);arb_abs(s.x,s.x);arb_add(sum.x,sum.x,s.x,512);
 }return sum;
}
extern "C" int review_units(long*out){
 checks=0;failure.clear();review_fault_at=0;review_partial_calls=0;
 try{
  // Exact dyadic endpoints and degenerate coefficient vertices.
  auto zero=endpoints12(B(),0,1),p=endpoints12(range12(B(-2),B(3)),0,1);
  auto c=endpoints12(range12(B(-8),B(8)),-5,5);
  require(zero.size()==1&&arb_is_zero(zero[0].x),"zero coefficient degeneracy");
  require(p.size()==2&&arb_is_zero(p[0].x)&&arb_is_one(p[1].x),"p clipping");
  require(c.size()==2&&arb_equal(c[0].x,B(-5).x)&&arb_equal(c[1].x,B(5).x),"c clipping");
  for(const B&v:c)require(mag_is_zero(arb_radref(v.x)),"vertex must be exact");
  std::set<long>D,E,cuts{0,8};
  poleband12(B(2),8,cuts,D);require(D==std::set<long>({1,2,3}),"closed buffered collision");
  bool rejected=false;try{poleband12(range12(B(1),B(2)),8,cuts,D);}catch(const std::exception&){rejected=true;}
  require(rejected,"literal width-one guard");
  cuts={0,8};E.clear();D.clear();rootband12(B(3),8,D,cuts,E);
  require(E==std::set<long>({3})&&cuts==std::set<long>({0,3,4,8}),"closed integer root");
  cuts={0,8};E.clear();rootband12(range12(point12(3.25),point12(3.75)),8,D,cuts,E);
  require(E.empty()&&cuts==std::set<long>({0,4,8}),"empty-band cut");
  struct Root{long c,p,delta;std::set<long>direct,edges;};
  std::vector<Root> roots={{0,0,0,{}, {0,8}},{1,0,0,{}, {0,8}},
   {0,1,0,{0,4},{0,1,4,5,8}},{0,1,1,{}, {0,4,8}},
   {1,1,0,{2},{0,2,3,8}},{-1,1,0,{6},{0,6,7,8}}};
  for(const Root&t:roots){cuts={0,8};E.clear();numerator12(B(t.c),B(t.p),8,t.delta,B(),D,cuts,E);
   require(E==t.direct&&cuts==t.edges,"exact root family and cuts");}
  // Full ratio images: negative turns, zero crossings, first numerator zero,
  // largest value-only k, rejected charts, and multiple removable poles.
  struct RC{long k,turn;Q lo,hi;};
  std::vector<RC> ratios={{1,0,Q(-2),Q(2)},{2,-1,Q(-1)/Q(4),Q(1)/Q(4)},
   {3,0,Q(1),Q(7)/Q(6)},{17,1,Q(-1)/Q(17),Q(1)/Q(17)},
   {4097,0,Q(3)/Q(4097),Q(7)/Q(8194)},{3,0,Q(7)/Q(4),Q(9)/Q(4)},
   {2,0,Q(-4),Q(4)},{2,40,Q(-1)/Q(8),Q(1)/Q(8)}};
  long ratio_rejections=0;
  for(const RC&t:ratios){Stats12 st;B z=pi()*B(t.turn)+range12(qb12(t.lo),qb12(t.hi)),got=ratio12(t.k,z,st);
   for(const Q&r:std::vector<Q>{t.lo,(t.lo+t.hi)/Q(2),t.hi}){
    B ref=ratio_reference(t.k,t.turn,r);
    require(arb_contains(got.x,ref.x)||(arb_is_exact(got.x)&&arb_contains(ref.x,got.x)),"full ratio image containment");
   }ratio_rejections+=st.ratioFallback;
  }
  require(ratio_rejections>=3,"ratio rejection branches reached");
  // Actual full-box primitive at collisions and special rows.
  struct PC{long n,r,k;Q al,ah,bl,bh;};
  std::vector<PC> primitives={{3,1,0,Q(2)/Q(3),Q(5)/Q(6),Q(),Q()},
   {5,0,1,Q(),Q(1)/Q(8),Q(),Q(1)/Q(8)},
   {8,8,3,Q(1)/Q(4),Q(1)/Q(3),Q(),Q(1)/Q(10)},
   {17,35,16,Q(),Q(),Q(7)/Q(8),Q(1)}};
  for(const PC&t:primitives){Stats12 st;B got=finite12(t.n,t.r,t.k,range12(qb12(t.al),qb12(t.ah)),range12(qb12(t.bl),qb12(t.bh)),st);
   long delta=(1-t.r)%2;if(delta<0)delta+=2;
   for(const auto&ab:std::vector<std::pair<Q,Q>>{{t.al,t.bl},{t.al,t.bh},{t.ah,t.bl},{t.ah,t.bh},{(t.al+t.ah)/Q(2),(t.bl+t.bh)/Q(2)}}){
    B ref=polynomial(t.n,delta+2*t.k,t.r,ab.first,ab.second);
    arb_mul_si(ref.x,ref.x,delta?-1:1,512);arb_mul_2exp_si(ref.x,ref.x,-1);
    require(arb_contains(got.x,ref.x),"actual full-box finite primitive");
   }
  }
  // Arbitrary artificial vertices, including regular root samples and zero.
  const long n=16,r=3,delta=0;Q lo,hi=Q(1)/Q(8),mid=Q(1)/Q(16);
  B af=range12(qb12(lo),qb12(hi)),bf=af,alpha=pi()*af,v=pi()*(B(r)+bf)/B(n+1);
  D.clear();cuts={0,n};poleband12((B(n)*v-alpha)/(B(2)*pi()),n,cuts,D);
  poleband12((B(n)*(B(2)*pi()-v)-alpha)/(B(2)*pi()),n,cuts,D);
  directcut12(0,n,cuts,D);directcut12(n-1,n,cuts,D);
  long regular_hits=0;
  for(auto cp:std::vector<std::pair<long,long>>{{0,0},{1,0},{1,1},{-1,1},{0,1}}){
   Stats12 st;B got=vertex12(n,r,af,bf,qb12(mid),qb12(mid),B(cp.first),B(cp.second),D,cuts,st);
   for(const auto&ab:std::vector<std::pair<Q,Q>>{{lo,lo},{lo,hi},{hi,lo},{hi,hi},{mid,mid}}){
    B ref=vertex_reference(n,r,cp.first,cp.second,ab.first,ab.second,D);
    require(arb_contains(got.x,ref.x)||(cp.first==0&&cp.second==0&&arb_contains_zero(ref.x)),"arbitrary vertex full-box containment");
   }regular_hits+=st.regular;
  }
  require(regular_hits>=3,"regular artificial root samples reached");
  out[0]=checks;out[1]=ratio_rejections;out[2]=regular_hits;out[3]=review_partial_calls;return 0;
 }catch(const std::exception&e){failure=e.what();out[0]=checks;return 1;}
}
