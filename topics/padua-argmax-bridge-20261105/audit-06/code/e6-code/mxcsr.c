#include <xmmintrin.h>
unsigned get_csr(void) { return _mm_getcsr(); }
void set_csr(unsigned v) { _mm_setcsr(v); }
