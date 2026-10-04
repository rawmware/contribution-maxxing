fun solve(x: Int, y: Int): Int { var a = x; var b = y; while (b != 0) { val r = a % b; a = b; b = r }; return a }

fun main() {
    println(solve(0, 0))
    println(solve(0, 7))
    println(solve(7, 0))
    println(solve(48, 18))
    println(solve(17, 13))
    println(solve(270, 192))
}
