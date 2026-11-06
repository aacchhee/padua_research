// Exact basis-only exporter derived from the accepted P6 native basis path.
// No source propagation or capacity endpoint is executed by this binary.
// Weighted formulas: theory/p4-weighted-normal-quotient.md, read before adaptation.
// All original nodes are explicit. No producer functions or libraries are used.
#include <gmpxx.h>
#include <vector>
#include <string>
#include <iostream>
#include <stdexcept>
#include <chrono>
#include <algorithm>
#include <fstream>
using Z=mpz_class; using Q=mpq_class;
void need(bool b,const char*m){if(!b)throw std::runtime_error(m);}
Q rational(const Z&n,const Z&d){need(d!=0,"zero rational denominator");Q q(n,d);q.canonicalize();return q;}
int compare(const Q&a,const Q&b){Z z=a.get_num()*b.get_den()-b.get_num()*a.get_den();return mpz_sgn(z.get_mpz_t());}
struct Vector {
 std::vector<Z> a; Z D=1;
 Vector()=default;
 explicit Vector(size_t n,long c=0):a(n,Z(c)){}
 Vector(std::vector<Z> n,Z d):a(std::move(n)),D(std::move(d)){need(D>0,"nonpositive vector denominator");reduce();}
 void reduce(){
  need(D>0,"nonpositive vector denominator");Z g=D;
  for(const Z&x:a){mpz_gcd(g.get_mpz_t(),g.get_mpz_t(),x.get_mpz_t());if(g==1)break;}
  if(g!=1){D/=g;for(Z&x:a)x/=g;}
 }
 void scale(const Q&c){
  if(c==0){for(Z&x:a)x=0;D=1;return;}
  for(Z&x:a)x*=c.get_num();D*=c.get_den();reduce();
 }
 void addScaled(const Vector&v,const Q&c){
  need(a.size()==v.a.size(),"vector dimension mismatch");if(c==0)return;
  Z E=v.D*c.get_den(),F;mpz_lcm(F.get_mpz_t(),D.get_mpz_t(),E.get_mpz_t());
  Z left=F/D,right=(F/E)*c.get_num();
  for(size_t i=0;i<a.size();++i)a[i]=a[i]*left+v.a[i]*right;
  D=std::move(F);reduce();
 }
 Vector pointProduct(const Vector&v)const{
  need(a.size()==v.a.size(),"vector dimension mismatch");Vector w(a.size());w.D=D*v.D;
  for(size_t i=0;i<a.size();++i)w.a[i]=a[i]*v.a[i];w.reduce();return w;
 }
 Vector squareWeighted(const Q&c)const{
  Vector w(a.size());w.D=D*D*c.get_den();
  for(size_t i=0;i<a.size();++i)w.a[i]=a[i]*a[i]*c.get_num();w.reduce();return w;
 }
 Q sum()const{Z n=0;for(const Z&x:a)n+=x;return rational(n,D);}
 Q value(size_t i)const{return rational(a.at(i),D);}
};
Q dot(const Vector&v,const Vector&w){need(v.a.size()==w.a.size(),"dot dimension mismatch");Z n=0;for(size_t i=0;i<v.a.size();++i)n+=v.a[i]*w.a[i];return rational(n,v.D*w.D);}
long checkColumn(const std::vector<Vector>&basis,const Vector&v,const Q&d){
 need(d>0,"nonpositive pivot");need(dot(v,v)==d,"diagonal Gram failure");
 for(const Vector&b:basis)need(dot(v,b)==0,"off-diagonal Gram failure");return basis.size();
}
// Unreduced scalar pairs avoid per-node GCDs in source maxima; comparisons are
// integer cross products. Canonical rationals are constructed only at output.
struct Peak {Z n=0,d=1;void update(const Z&x,const Z&y){need(y>0,"invalid peak denominator");if(x*d>n*y){n=x;d=y;}}};
struct Step {int axis=0,parent=0;std::vector<Q> alpha;Q sigma;};
void selfTest(){
 Vector a({Z(2),Z(-3),Z(0)},Z(6)),b({Z(-5),Z(7),Z(9)},Z(15));
 std::vector<Q> av={Q(1,3),Q(-1,2),Q(0)},bv={Q(-1,3),Q(7,15),Q(3,5)};
 auto verify=[](const Vector&v,const std::vector<Q>&q){need(v.a.size()==q.size(),"selftest size");for(size_t i=0;i<q.size();++i)need(v.value(i)==q[i],"primitive mismatch");};
 verify(a,av);verify(b,bv);Vector v=a;v.addScaled(b,Q(-7,11));for(size_t i=0;i<av.size();++i)av[i]-=Q(7,11)*bv[i];verify(v,av);
 Vector w=v.squareWeighted(Q(3,17));std::vector<Q> expected;for(const Q&q:av)expected.push_back(q*q*Q(3,17));verify(w,expected);
 Vector u=v.pointProduct(b);for(size_t i=0;i<av.size();++i)expected[i]=av[i]*bv[i];verify(u,expected);Q sd=0;for(size_t i=0;i<av.size();++i)sd+=av[i]*bv[i];need(dot(v,b)==sd,"dot mismatch");
 v.scale(Q(-19,23));for(Q&q:av)q*=Q(-19,23);verify(v,av);v.scale(Q(0));verify(v,std::vector<Q>(3,Q(0)));need(v.D==1,"zero normalization");
 int rejected=0;auto reject=[&](auto f){try{f();}catch(const std::exception&){++rejected;return;}throw std::runtime_error("malformed control accepted");};
 reject([](){Vector bad({Z(1)},Z(0));});reject([](){Vector bad({Z(1)},Z(-1));});
 reject([&](){Vector z(2);z.addScaled(b,Q(1));});reject([&](){Vector z(2);dot(z,b);});
 reject([](){std::vector<Vector>B;Vector v(2,1);checkColumn(B,v,Q(0));});
 reject([](){std::vector<Vector>B;Vector v(2,1);checkColumn(B,v,Q(3));});
 reject([](){std::vector<Vector>B{Vector(2,1)};Vector v(2,1);checkColumn(B,v,Q(2));});
 reject([](){Peak p;p.update(Z(1),Z(0));});
 need(rejected==8,"malformed control count");std::cout<<"{\"primitive_tests\":\"PASS exact scalar-GMP cross-check\",\"malformed_native_controls_rejected\":8}\n";
}
int main(int argc,char**argv){try{
 if(argc==2&&std::string(argv[1])=="--self-test"){selfTest();return 0;}
 need(argc==5,"usage: executable input.txt maxdegree bj|mirror|alt|pivot family");
 std::string grid=argv[4],rule=argv[3];int degree=std::stoi(argv[2]);
 need(degree>=2&&degree<=20,"degree outside2..20");
 need(rule=="bj"||rule=="mirror"||rule=="alt"||rule=="pivot","invalid rule");
 auto start=std::chrono::steady_clock::now();
 std::ifstream input(argv[1]);need(input.good(),"cannot open input");int M;input>>M;need(M>0&&M<=10000,"invalid input count");
 std::vector<Q> xx,yy,ww;Q weight=0;
 for(int i=0;i<M;++i){Q a,b,w;input>>a>>b>>w;need(input.good()&&w>0,"invalid input row");
  a.canonicalize();b.canonicalize();w.canonicalize();weight+=w;xx.push_back(a);yy.push_back(b);ww.push_back(w);}
 std::string extra;need(!(input>>extra),"extra input tokens");
 auto pack=[](const std::vector<Q>&v){Z den=1;for(const Q&q:v)mpz_lcm(den.get_mpz_t(),den.get_mpz_t(),q.get_den().get_mpz_t());std::vector<Z>num;for(const Q&q:v)num.push_back(q.get_num()*(den/q.get_den()));return Vector(num,den);};
 need(weight==1,"normalized weights required");Vector weights=pack(ww);
 auto wdot=[&](const Vector&a,const Vector&b){return dot(a.pointProduct(weights),b);};
 Vector x=pack(xx),y=pack(yy);int N=(degree+1)*(degree+2)/2;need(M>N,"M>N failure");
 std::vector<Vector>B{Vector(M,1)};std::vector<Q>d{Q(1)};std::vector<Step>rec(1);std::vector<int>ends(degree+1);std::vector<std::vector<int>>index(degree+1);index[0]={0};ends[0]=1;
 std::string choices;std::vector<std::pair<int,int>>ties;long gram=0;
 for(int t=1;t<=degree;++t){for(int j=0;j<=t;++j){
  std::vector<Step>cs;std::vector<Vector>res;std::vector<Q>norms;
  for(int axis=0;axis<2;++axis){if((axis==0&&j==t)||(axis==1&&j==0))continue;
   int wanted=rule=="bj"?(j==0?0:1):rule=="mirror"?(j!=t?0:1):(2*j<t?0:1);if(rule!="pivot"&&axis!=wanted)continue;
   int p=index[t-1][j-axis];Vector z=B[p].pointProduct(axis?y:x);Q sigma=wdot(z,z);need(sigma>0,"nonpositive source scale");std::vector<Q>alpha;
   for(size_t l=0;l<B.size();++l)alpha.push_back(wdot(B[l],z)/d[l]);Vector r=z;
   for(size_t l=0;l<B.size();++l)if(alpha[l]!=0)r.addScaled(B[l],-alpha[l]);Q dk=wdot(r,r);need(dk>0,"nonpositive pivot");cs.push_back({axis,p,alpha,sigma});res.push_back(std::move(r));norms.push_back(dk);
  }
  need(!cs.empty(),"missing parent");int pick=0;if(cs.size()==2){int c=compare(norms[0]/cs[0].sigma,norms[1]/cs[1].sigma);if(c==0)ties.push_back({t,j});if(c<0)pick=1;}
  need(wdot(res[pick],res[pick])==norms[pick],"weighted diagonal Gram failure");for(const Vector&v:B){need(wdot(v,res[pick])==0,"weighted off-diagonal Gram failure");++gram;}index[t].push_back(B.size());B.push_back(std::move(res[pick]));d.push_back(norms[pick]);rec.push_back(std::move(cs[pick]));choices+=rec.back().axis?'Y':'X';
 }
 ends[t]=B.size();std::cerr<<"basis "<<grid<<" "<<rule<<" "<<t<<"\n";
 }
 need((int)B.size()==N,"basis cardinality failure");
 // Export unweighted polynomial values; weights remain separate.
 std::cout<<"{\"schema\":\"p6-exact-basis-v1\",\"family\":\""<<grid<<"\",\"rule\":\""<<rule<<"\",\"max_degree\":"<<degree<<",\"point_count\":"<<M<<",\"basis_count\":"<<N;
 std::cout<<",\"points\":[";
 for(int i=0;i<M;++i){if(i)std::cout<<",";std::cout<<"[\""<<x.value(i)<<"\",\""<<y.value(i)<<"\",\""<<weights.value(i)<<"\"]";}
 std::cout<<"],\"B\":[";
 for(int k=0;k<N;++k){if(k)std::cout<<",";std::cout<<"[";for(int i=0;i<M;++i){if(i)std::cout<<",";std::cout<<"\""<<B[k].value(i)<<"\"";}std::cout<<"]";}
 std::cout<<"],\"d\":[";for(int k=0;k<N;++k){if(k)std::cout<<",";std::cout<<"\""<<d[k]<<"\"";}
 std::cout<<"],\"steps\":[null";
 for(int k=1;k<N;++k){const Step&s=rec[k];std::cout<<",{\"axis\":"<<s.axis<<",\"parent\":"<<s.parent<<",\"alpha\":[";for(int l=0;l<k;++l){if(l)std::cout<<",";std::cout<<"\""<<s.alpha[l]<<"\"";}std::cout<<"],\"sigma_squared\":\""<<s.sigma<<"\"}";}
 std::cout<<"],\"ends\":[";for(int t=0;t<=degree;++t){if(t)std::cout<<",";std::cout<<ends[t];}
 std::cout<<"],\"meta\":[";bool sep=false;for(int t=0;t<=degree;++t)for(int j=0;j<=t;++j){if(sep)std::cout<<",";sep=true;std::cout<<"["<<t<<","<<j<<"]";}
 std::cout<<"],\"choices\":[";for(int k=0;k<N-1;++k){if(k)std::cout<<",";std::cout<<"\""<<choices[k]<<"\"";}
 std::cout<<"],\"ties\":[";for(size_t i=0;i<ties.size();++i){if(i)std::cout<<",";std::cout<<"["<<ties[i].first<<","<<ties[i].second<<"]";}
 std::cout<<"],\"exact_gram_pairs_checked\":"<<gram<<"}"<<std::endl;
 return 0;
}catch(const std::exception&e){std::cerr<<e.what()<<"\n";return 2;}}
