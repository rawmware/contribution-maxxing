object Main {
def solve(n: Int): Int = { var r = 1; for (i <- 2 to n) r *= i; r }
def main(args: Array[String]): Unit = {
    println(solve(0))
    println(solve(1))
    println(solve(2))
    println(solve(5))
    println(solve(10))
    println(solve(12))
}
}
