package main

import "fmt"

func solve(a, b int) int { for b != 0 { a, b = b, a % b }; return a }

func main() {
    fmt.Println(solve(0, 0))
    fmt.Println(solve(0, 7))
    fmt.Println(solve(7, 0))
    fmt.Println(solve(48, 18))
    fmt.Println(solve(17, 13))
    fmt.Println(solve(270, 192))
}
