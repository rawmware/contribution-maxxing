/* Browser-facing C11 implementations. -1 means input outside the demo domain. */
int lab_gcd(int a, int b) {
    if (a < 0 || b < 0 || a > 1000000 || b > 1000000) return -1;
    while (b) { int remainder = a % b; a = b; b = remainder; }
    return a;
}
int lab_factorial(int n) {
    if (n < 0 || n > 12) return -1;
    int value = 1;
    for (int i = 2; i <= n; ++i) value *= i;
    return value;
}
int lab_prime(int n) {
    if (n < 0 || n > 1000000) return -1;
    if (n < 2) return 0;
    for (int d = 2; d <= n / d; ++d) if (n % d == 0) return 0;
    return 1;
}
int lab_fibonacci(int n) {
    if (n < 0 || n > 30) return -1;
    int a = 0, b = 1;
    for (int i = 0; i < n; ++i) { int next = a + b; a = b; b = next; }
    return a;
}
