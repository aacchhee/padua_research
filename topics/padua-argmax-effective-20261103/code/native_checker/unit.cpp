// Focused mathematical controls for signed rounding and de Casteljau.
#define main certificate_kernel_entry
#include "kernel.cpp"
#undef main
void require(bool value) { if(!value) throw std::runtime_error("unit control failed"); }
int main() {
    require(down(frac(-5,2)) == -3 && up(frac(-5,2)) == -2);
    require(down(frac(5,2)) == 2 && up(frac(5,2)) == 3);
    I negative = grid(frac(-1,3));
    require(ratio(negative.l,S) <= frac(-1,3) && ratio(negative.h,S) >= frac(-1,3));
    I product = mul({-S,2*S},{-3*S,4*S});
    require(product.l == -6*S && product.h == 8*S);
    I weighted = linear({{-2,3}},{frac(-1,3)});
    require(weighted.l == -1 && weighted.h == 1);
    Coeff root = {{{-5,-4},{-5,-4},{-5,-4},
                   {0,1},{0,1},{0,1},
                   {8,9},{8,9},{8,9}}};
    auto children = split(root,2,0);
    require(children.first[0][0].l == -5 && children.first[0][0].h == -4);
    require(children.first[0][3].l == -3 && children.first[0][3].h == -1);
    require(children.first[0][6].l == 0 && children.first[0][6].h == 2);
    require(children.second[0][0].l == 0 && children.second[0][0].h == 2);
    require(children.second[0][3].l == 4 && children.second[0][3].h == 5);
    require(children.second[0][6].l == 8 && children.second[0][6].h == 9);
    auto p=atanb(5),q=atanb(239);
    Q lo=16*p.first.first-4*q.first.second, hi=16*p.first.second-4*q.first.first;
    require(frac(314159,100000) < lo && hi < frac(314160,100000));
    auto v=axis(2,lo,hi);
    require(v[0].l==S && v[1].l==0 && v[1].h==0 && v[2].l==-S);
    std::cout << "signed rounding, multiplication, negative transform, subdivision and trigonometric controls passed\n";
}
