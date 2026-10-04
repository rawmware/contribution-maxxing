#include <stdio.h>

long long solve(long long n) { long long r = 1; for (long long i = 2; i <= n; ++i) r *= i; return r; }

int main(void) {
    printf("%lld\n", solve(0));
    printf("%lld\n", solve(1));
    printf("%lld\n", solve(2));
    printf("%lld\n", solve(5));
    printf("%lld\n", solve(10));
    printf("%lld\n", solve(12));
    return 0;
}
