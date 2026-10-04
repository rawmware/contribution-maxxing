public class Main {
static long solve(long n) { long r = 1; for (long i = 2; i <= n; ++i) r *= i; return r; }
public static void main(String[] args) {
    System.out.println(solve(0));
    System.out.println(solve(1));
    System.out.println(solve(2));
    System.out.println(solve(5));
    System.out.println(solve(10));
    System.out.println(solve(12));
}
}
