#include <stdio.h>

long long solve(long long n) { long long a = 0, b = 1; for (long long i = 0; i < n; ++i) { long long t = a+b; a = b; b = t; } return a; }

int main(void) {
    printf("%lld\n", solve(0));
    printf("%lld\n", solve(1));
    printf("%lld\n", solve(2));
    printf("%lld\n", solve(3));
    printf("%lld\n", solve(10));
    printf("%lld\n", solve(20));
    printf("%lld\n", solve(30));
    return 0;
}
