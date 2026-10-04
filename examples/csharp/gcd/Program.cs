using System;
class Program {
static long solve(long a, long b) { while (b != 0) { long r = a % b; a = b; b = r; } return a; }
static void Main() {
    Console.WriteLine(solve(0, 0));
    Console.WriteLine(solve(0, 7));
    Console.WriteLine(solve(7, 0));
    Console.WriteLine(solve(48, 18));
    Console.WriteLine(solve(17, 13));
    Console.WriteLine(solve(270, 192));
}
}
