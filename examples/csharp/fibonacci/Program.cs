using System;
class Program {
static long solve(long n) { long a = 0, b = 1; for (long i = 0; i < n; ++i) { long t = a+b; a = b; b = t; } return a; }
static void Main() {
    Console.WriteLine(solve(0));
    Console.WriteLine(solve(1));
    Console.WriteLine(solve(2));
    Console.WriteLine(solve(3));
    Console.WriteLine(solve(10));
    Console.WriteLine(solve(20));
    Console.WriteLine(solve(30));
}
}
