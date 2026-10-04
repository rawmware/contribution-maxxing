#include <iostream>

long long solve(long long n) { long long a = 0, b = 1; for (long long i = 0; i < n; ++i) { long long t = a+b; a = b; b = t; } return a; }

int main(void) {
    std::cout << solve(0) << "\n";
    std::cout << solve(1) << "\n";
    std::cout << solve(2) << "\n";
    std::cout << solve(3) << "\n";
    std::cout << solve(10) << "\n";
    std::cout << solve(20) << "\n";
    std::cout << solve(30) << "\n";
    return 0;
}
