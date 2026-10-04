object Main {
def solve(n: Int): Int = { if (n < 2) return 0; var d = 2; while (d*d <= n) { if (n % d == 0) return 0; d += 1 }; 1 }
def main(args: Array[String]): Unit = {
    println(solve(0))
    println(solve(1))
    println(solve(2))
    println(solve(3))
    println(solve(4))
    println(solve(25))
    println(solve(97))
    println(solve(121))
    println(solve(997))
}
}
