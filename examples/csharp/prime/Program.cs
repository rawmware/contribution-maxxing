using System;
class Program {
static long solve(long n) { if (n < 2) return 0; for (long d = 2; d*d <= n; ++d) if (n%d == 0) return 0; return 1; }
static void Main() {
    Console.WriteLine(solve(0));
    Console.WriteLine(solve(1));
    Console.WriteLine(solve(2));
    Console.WriteLine(solve(3));
    Console.WriteLine(solve(4));
    Console.WriteLine(solve(25));
    Console.WriteLine(solve(97));
    Console.WriteLine(solve(121));
    Console.WriteLine(solve(997));
}
}
