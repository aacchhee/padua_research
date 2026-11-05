// Independent common-denominator GMP port of the frozen PD-T136/137 formulas.
// All original nodes are explicit. No producer functions or libraries are used.
#include <gmpxx.h>
#include <vector>
#include <string>
#include <iostream>
#include <stdexcept>
#include <chrono>
#include <algorithm>
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
 need(argc==4,"usage: executable triangle|rotated maxdegree bj|mirror|alt|pivot");
 std::string grid=argv[1],rule=argv[3];int degree=std::stoi(argv[2]);
 need(grid=="triangle"||grid=="rotated","invalid grid");need(degree>=2&&degree<=20,"degree outside2..20");
 need(rule=="bj"||rule=="mirror"||rule=="alt"||rule=="pivot","invalid rule");
 auto start=std::chrono::steady_clock::now();std::vector<Z> xn,yn;
 for(int i=0;i<=24;++i)for(int j=0;j<=24;++j){if(grid=="triangle"&&i+j>24)continue;
  long u=i-12,v=j-12;xn.push_back(grid=="triangle"?u:3*u-4*v);yn.push_back(grid=="triangle"?v:4*u+3*v);}
 Vector x(xn,Z(grid=="triangle"?12:60)),y(yn,Z(grid=="triangle"?12:60));int M=x.a.size(),N=(degree+1)*(degree+2)/2;
 need(M==(grid=="triangle"?325:625)&&M>N,"node cardinality or M>N failure");
 std::vector<Vector>B{Vector(M,1)};std::vector<Q>d{Q(M)};std::vector<Step>rec(1);std::vector<int>ends(degree+1);std::vector<std::vector<int>>index(degree+1);index[0]={0};ends[0]=1;
 std::string choices;std::vector<std::pair<int,int>>ties;long gram=0;
 for(int t=1;t<=degree;++t){for(int j=0;j<=t;++j){
  std::vector<Step>cs;std::vector<Vector>res;std::vector<Q>norms;
  for(int axis=0;axis<2;++axis){if((axis==0&&j==t)||(axis==1&&j==0))continue;
   int wanted=rule=="bj"?(j==0?0:1):rule=="mirror"?(j!=t?0:1):(2*j<t?0:1);if(rule!="pivot"&&axis!=wanted)continue;
   int p=index[t-1][j-axis];Vector z=B[p].pointProduct(axis?y:x);Q sigma=dot(z,z);need(sigma>0,"nonpositive source scale");std::vector<Q>alpha;
   for(size_t l=0;l<B.size();++l)alpha.push_back(dot(B[l],z)/d[l]);Vector r=z;
   for(size_t l=0;l<B.size();++l)if(alpha[l]!=0)r.addScaled(B[l],-alpha[l]);Q dk=dot(r,r);need(dk>0,"nonpositive pivot");cs.push_back({axis,p,alpha,sigma});res.push_back(std::move(r));norms.push_back(dk);
  }
  need(!cs.empty(),"missing parent");int pick=0;if(cs.size()==2){int c=compare(norms[0]/cs[0].sigma,norms[1]/cs[1].sigma);if(c==0)ties.push_back({t,j});if(c<0)pick=1;}
  gram+=checkColumn(B,res[pick],norms[pick]);index[t].push_back(B.size());B.push_back(std::move(res[pick]));d.push_back(norms[pick]);rec.push_back(std::move(cs[pick]));choices+=rec.back().axis?'Y':'X';
 }
 ends[t]=B.size();std::cerr<<"basis "<<grid<<" "<<rule<<" "<<t<<"\n";
 }
 need((int)B.size()==N,"basis cardinality failure");
 std::vector<Vector>normal(degree+1),rows(degree+1);std::vector<std::vector<Peak>>peaks(degree+1);Vector nd(M,1);
 for(int k=0;k<N;++k){nd.addScaled(B[k].squareWeighted(Q(1)/d[k]),Q(-1));
  for(int s=2;s<=degree;++s)if(k+1==ends[s]){for(const Z&v:nd.a)need(v>=0&&v<=nd.D,"invalid projector diagonal");need(nd.sum()==M-ends[s],"projector trace mismatch");normal[s]=nd;rows[s]=Vector(M);peaks[s]=std::vector<Peak>(M);}}
 auto finish=[&](int s){Q lo=0;Peak lower;const Vector&n=normal[s];
  for(int i=0;i<M;++i)lower.update(n.a[i]*peaks[s][i].n,n.D*peaks[s][i].d);lo=rational(lower.n,lower.d);
  Q hs=dot(n,rows[s]);Z rowmax=0;for(const Z&v:rows[s].a)if(v>rowmax)rowmax=v;Q row=rational(rowmax,rows[s].D),upper=compare(hs,row)<0?hs:row;
  need(lo>0&&compare(lo,upper)<=0,"endpoint order failure");
  std::cout<<"{\"set\":\""<<grid<<"\",\"rule\":\""<<rule<<"\",\"degree\":"<<s<<",\"sources\":\"all\",\"source_count\":"<<ends[s]-1<<",\"point_count\":"<<M<<",\"basis_count\":"<<ends[s]<<",\"Knode_squared\":{\"exact\":\""<<lo<<"\"},\"KHS_squared\":{\"exact\":\""<<hs<<"\"},\"Urow_squared\":{\"exact\":\""<<row<<"\"},\"upper_squared\":{\"exact\":\""<<upper<<"\"},\"pivot_choices\":[";
  for(int k=0;k<ends[s]-1;++k){if(k)std::cout<<",";std::cout<<"\""<<choices[k]<<"\"";}std::cout<<"],\"pivot_ties\":[";bool comma=false;for(auto p:ties)if(p.first<=s){if(comma)std::cout<<",";std::cout<<"["<<p.first<<","<<p.second<<"]";comma=true;}
  double seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();std::cout<<"],\"normal_trace_exact\":\""<<normal[s].sum()<<"\",\"exact_gram_pairs_checked\":"<<gram<<",\"elapsed_seconds\":"<<seconds<<"}"<<std::endl;
 };
 for(int h=1;h<N;++h){std::vector<Vector>g(N);g[h]=Vector(M,1);Vector energy(M,1);energy.scale(Q(1)/d[h]);
  for(int k=h;k<N;++k){if(k>h){const Step&s=rec[k];Vector v(M);if(s.parent>=h)v=g[s.parent].pointProduct(s.axis?y:x);for(int l=h;l<k;++l)if(s.alpha[l]!=0)v.addScaled(g[l],-s.alpha[l]);g[k]=std::move(v);energy.addScaled(g[k].squareWeighted(Q(1)/d[k]),Q(1));}
   for(int s=2;s<=degree;++s)if(k+1==ends[s]){Vector weighted=energy;weighted.scale(rec[h].sigma);rows[s].addScaled(weighted,Q(1));for(int i=0;i<M;++i)peaks[s][i].update(weighted.a[i],weighted.D);}
  }
  std::cerr<<"source "<<h<<"/"<<N-1<<"\n";for(int s=2;s<=degree;++s)if(h+1==ends[s])finish(s);
 }
 return 0;
}catch(const std::exception&e){std::cerr<<e.what()<<"\n";return 2;}}
