fun solve(n: Int): Int { var r = 1; for (i in 2..n) r *= i; return r }

fun main() {
    println(solve(0))
    println(solve(1))
    println(solve(2))
    println(solve(5))
    println(solve(10))
    println(solve(12))
}
