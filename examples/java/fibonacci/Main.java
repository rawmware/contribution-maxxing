public class Main {
static long solve(long n) { long a = 0, b = 1; for (long i = 0; i < n; ++i) { long t = a+b; a = b; b = t; } return a; }
public static void main(String[] args) {
    System.out.println(solve(0));
    System.out.println(solve(1));
    System.out.println(solve(2));
    System.out.println(solve(3));
    System.out.println(solve(10));
    System.out.println(solve(20));
    System.out.println(solve(30));
}
}
