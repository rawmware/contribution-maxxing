object Main {
def solve(n: Int): Int = { var a = 0; var b = 1; for (i <- 0 until n) { val t = a+b; a = b; b = t }; a }
def main(args: Array[String]): Unit = {
    println(solve(0))
    println(solve(1))
    println(solve(2))
    println(solve(3))
    println(solve(10))
    println(solve(20))
    println(solve(30))
}
}
