public class Main {
static long solve(long a, long b) { while (b != 0) { long r = a % b; a = b; b = r; } return a; }
public static void main(String[] args) {
    System.out.println(solve(0, 0));
    System.out.println(solve(0, 7));
    System.out.println(solve(7, 0));
    System.out.println(solve(48, 18));
    System.out.println(solve(17, 13));
    System.out.println(solve(270, 192));
}
}
