#include <stdio.h>

long long solve(long long n) { if (n < 2) return 0; for (long long d = 2; d*d <= n; ++d) if (n%d == 0) return 0; return 1; }

int main(void) {
    printf("%lld\n", solve(0));
    printf("%lld\n", solve(1));
    printf("%lld\n", solve(2));
    printf("%lld\n", solve(3));
    printf("%lld\n", solve(4));
    printf("%lld\n", solve(25));
    printf("%lld\n", solve(97));
    printf("%lld\n", solve(121));
    printf("%lld\n", solve(997));
    return 0;
}
