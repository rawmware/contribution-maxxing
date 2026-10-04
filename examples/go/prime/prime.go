package main

import "fmt"

func solve(n int) int { if n < 2 { return 0 }; for d := 2; d*d <= n; d++ { if n%d == 0 { return 0 } }; return 1 }

func main() {
    fmt.Println(solve(0))
    fmt.Println(solve(1))
    fmt.Println(solve(2))
    fmt.Println(solve(3))
    fmt.Println(solve(4))
    fmt.Println(solve(25))
    fmt.Println(solve(97))
    fmt.Println(solve(121))
    fmt.Println(solve(997))
}
