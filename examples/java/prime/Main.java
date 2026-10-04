public class Main {
static long solve(long n) { if (n < 2) return 0; for (long d = 2; d*d <= n; ++d) if (n%d == 0) return 0; return 1; }
public static void main(String[] args) {
    System.out.println(solve(0));
    System.out.println(solve(1));
    System.out.println(solve(2));
    System.out.println(solve(3));
    System.out.println(solve(4));
    System.out.println(solve(25));
    System.out.println(solve(97));
    System.out.println(solve(121));
    System.out.println(solve(997));
}
}
