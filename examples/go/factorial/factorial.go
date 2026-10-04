package main

import "fmt"

func solve(n int) int { r := 1; for i := 2; i <= n; i++ { r *= i }; return r }

func main() {
    fmt.Println(solve(0))
    fmt.Println(solve(1))
    fmt.Println(solve(2))
    fmt.Println(solve(5))
    fmt.Println(solve(10))
    fmt.Println(solve(12))
}
