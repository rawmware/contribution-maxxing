package main

import "fmt"

func solve(n int) int { a, b := 0, 1; for i := 0; i < n; i++ { a, b = b, a+b }; return a }

func main() {
    fmt.Println(solve(0))
    fmt.Println(solve(1))
    fmt.Println(solve(2))
    fmt.Println(solve(3))
    fmt.Println(solve(10))
    fmt.Println(solve(20))
    fmt.Println(solve(30))
}
