using System;
class Program {
static long solve(long n) { long r = 1; for (long i = 2; i <= n; ++i) r *= i; return r; }
static void Main() {
    Console.WriteLine(solve(0));
    Console.WriteLine(solve(1));
    Console.WriteLine(solve(2));
    Console.WriteLine(solve(5));
    Console.WriteLine(solve(10));
    Console.WriteLine(solve(12));
}
}
