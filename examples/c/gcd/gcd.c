#include <stdio.h>

long long solve(long long a, long long b) { while (b != 0) { long long r = a % b; a = b; b = r; } return a; }

int main(void) {
    printf("%lld\n", solve(0, 0));
    printf("%lld\n", solve(0, 7));
    printf("%lld\n", solve(7, 0));
    printf("%lld\n", solve(48, 18));
    printf("%lld\n", solve(17, 13));
    printf("%lld\n", solve(270, 192));
    return 0;
}
