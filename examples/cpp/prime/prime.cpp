#include <iostream>

long long solve(long long n) { if (n < 2) return 0; for (long long d = 2; d*d <= n; ++d) if (n%d == 0) return 0; return 1; }

int main(void) {
    std::cout << solve(0) << "\n";
    std::cout << solve(1) << "\n";
    std::cout << solve(2) << "\n";
    std::cout << solve(3) << "\n";
    std::cout << solve(4) << "\n";
    std::cout << solve(25) << "\n";
    std::cout << solve(97) << "\n";
    std::cout << solve(121) << "\n";
    std::cout << solve(997) << "\n";
    return 0;
}
