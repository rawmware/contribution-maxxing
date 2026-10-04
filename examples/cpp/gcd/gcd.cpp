#include <iostream>

long long solve(long long a, long long b) { while (b != 0) { long long r = a % b; a = b; b = r; } return a; }

int main(void) {
    std::cout << solve(0, 0) << "\n";
    std::cout << solve(0, 7) << "\n";
    std::cout << solve(7, 0) << "\n";
    std::cout << solve(48, 18) << "\n";
    std::cout << solve(17, 13) << "\n";
    std::cout << solve(270, 192) << "\n";
    return 0;
}
