#include <iostream>

long long solve(long long n) { long long r = 1; for (long long i = 2; i <= n; ++i) r *= i; return r; }

int main(void) {
    std::cout << solve(0) << "\n";
    std::cout << solve(1) << "\n";
    std::cout << solve(2) << "\n";
    std::cout << solve(5) << "\n";
    std::cout << solve(10) << "\n";
    std::cout << solve(12) << "\n";
    return 0;
}
