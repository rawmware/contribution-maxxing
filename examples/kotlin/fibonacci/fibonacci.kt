fun solve(n: Int): Int { var a = 0; var b = 1; repeat(n) { val t = a+b; a = b; b = t }; return a }

fun main() {
    println(solve(0))
    println(solve(1))
    println(solve(2))
    println(solve(3))
    println(solve(10))
    println(solve(20))
    println(solve(30))
}
